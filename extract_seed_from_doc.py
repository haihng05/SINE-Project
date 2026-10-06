import os
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
import json
import re
import argparse
import base64
from pathlib import Path
from openai import OpenAI
try:
    import fitz  
    import docx
except ImportError:
    print(" Vui lòng cài đặt các thư viện đọc file:")
    print("pip install pymupdf python-docx")
    sys.exit(1)
PROJECT_ROOT = Path(__file__).parent
SEEDS_DIR = PROJECT_ROOT / "seeds"
SEEDS_DIR.mkdir(exist_ok=True)
def get_base64_images_from_pdf(file_path: str) -> list:
    """Chuyển đổi các trang PDF thành danh sách ảnh base64."""
    doc = fitz.open(file_path)
    base64_images = []
    for page in doc:
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        img_bytes = pix.tobytes("png")
        b64_str = base64.b64encode(img_bytes).decode("utf-8")
        base64_images.append(b64_str)
    return base64_images
def extract_text_from_docx_with_word(file_path: str) -> str:
    """Chuyển đổi file DOCX sang PDF tạm bằng Word COM để đọc toàn bộ công thức MathType / Equation."""
    temp_pdf = None
    try:
        import win32com.client
        import tempfile
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        temp_pdf = os.path.join(tempfile.gettempdir(), f"sine_conv_{os.getpid()}_{Path(file_path).name}.pdf")
        abs_docx = str(Path(file_path).resolve())
        doc = word.Documents.Open(abs_docx)
        doc.SaveAs(temp_pdf, FileFormat=17)  # 17 = wdFormatPDF
        doc.Close()
        word.Quit()
        
        if os.path.exists(temp_pdf):
            pdf_doc = fitz.open(temp_pdf)
            full_text = ""
            for page in pdf_doc:
                full_text += page.get_text() + "\n"
            pdf_doc.close()
            try:
                os.remove(temp_pdf)
            except Exception:
                pass
            return full_text
    except Exception as e:
        print(f" [Thông báo] Không thể trích xuất nâng cao qua Word COM ({e}), sử dụng bộ đọc DOCX chuẩn...")
        if temp_pdf and os.path.exists(temp_pdf):
            try:
                os.remove(temp_pdf)
            except Exception:
                pass
    return ""

def extract_text_from_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
    ext = path.suffix.lower()
    text = ""
    if ext == ".pdf":
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text() + "\n"
    elif ext == ".docx":
        # 1. Thử dùng Word COM trước để đọc được các công thức MathType / Hóa học / Toán học
        advanced_text = extract_text_from_docx_with_word(str(path))
        if advanced_text.strip():
            print(f" Đã trích xuất thành công {len(advanced_text)} ký tự (bao gồm công thức MathType/Equation).")
            return advanced_text
        
        # 2. Dự phòng: dùng python-docx thông thường
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif ext in [".txt", ".md"]:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError(f"Định dạng file không được hỗ trợ: {ext}")
    return text
def extract_json_from_text(text: str) -> str:
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text.strip()
def get_openrouter_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("OPENROUTER_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""

def generate_seed_with_ai(file_path: str, text_content: str, topic_name: str, use_vision: bool = False) -> dict:
    api_key = get_openrouter_api_key()
    if not api_key:
        raise ValueError("Chưa thiết lập OPENROUTER_API_KEY! Vui lòng cấu hình biến môi trường hoặc khai báo trong file .env.")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    prompt = f"""Bạn là một trợ lý AI chuyên phân tích đề thi và trích xuất dữ liệu.
Nhiệm vụ của bạn là đọc nội dung (văn bản hoặc hình ảnh) dưới đây, tự động bỏ qua các phần không phải là câu hỏi trắc nghiệm (ví dụ: tiêu đề, lời mở đầu, hướng dẫn). 
Sau đó, trích xuất tất cả các câu hỏi trắc nghiệm có trong đó và chuyển đổi chúng thành định dạng JSON Seed (SINE format).
YÊU CẦU:
1. Xác định đúng câu hỏi (stem), các lựa chọn (options) và đáp án đúng. CHỈ TRÍCH XUẤT BỘ ĐỀ THI ĐẦU TIÊN trong văn bản (ví dụ từ Câu 1 đến Câu 40 hoặc 50). Nếu tài liệu có kèm đề thi thứ hai hoặc mã đề phụ ở phía sau, hãy dừng lại và KHÔNG trích xuất các câu của đề thứ hai.
2. TUYỆT ĐỐI KHÔNG ĐỂ CÁC LỰA CHỌN (OPTIONS) BỊ RỖNG HOẶC CHỈ CÓ DẤU CÁCH "". Mỗi phương án phải chứa đầy đủ nội dung hoặc công thức (ví dụ: "HCl", "Ba(OH)2", "CH3COOH", "150", v.v.). Nếu đề thi bị thiếu chữ ở đáp án nào, hãy tự suy luận điền công thức/đáp án phù hợp với câu hỏi.
3. Tạo danh sách các "locations" (địa điểm trong game) tương ứng. Bạn có thể tự sáng tạo tên địa điểm (ví dụ: "location_phong_thi_nghiem", "location_thu_vien") sao cho phù hợp với chủ đề "{topic_name}".
4. ĐẶC BIỆT CHÚ Ý CÁC CÂU GIAO TIẾP / HỘI THOẠI (Exchanges/Conversations):
   - BẮT BUỘC phải trích xuất TRỌN VẸN ngữ cảnh và lời thoại của TẤT CẢ các nhân vật tham gia vào 'stem' (bao gồm câu dẫn bối cảnh, câu nói của nhân vật trước và câu đáp của nhân vật sau).
   - TUYỆT ĐỐI KHÔNG được cắt xén chỉ lấy 1 vế có chỗ trống, vì người học phải đọc được câu của nhân vật trước mới hiểu được ngữ cảnh để chọn câu trả lời đúng.
   - Ví dụ: "stem": "Peter and Khanh are talking about learning foreign languages.\\n- Peter: “I think students should learn two foreign languages when they are at school.”\\n- Khanh: “______. It helps them communicate with more people and broaden their minds.”"
5. CÚ PHÁP JSON BẮT BUỘC:
   - Nếu trong câu hỏi hoặc lựa chọn có dấu ngoặc kép, BẮT BUỘC phải escape bằng dấu gạch chéo ngược: \"từ ngữ\" (ví dụ: \"fulfilling\") hoặc đổi thành dấu nháy đơn 'fulfilling'.
   - Phải có dấu phẩy ',' ngăn cách giữa các đối tượng trong mảng tasks.
   - Chỉ xuất DUY NHẤT một khối ```json ... ``` theo cấu trúc mẫu sau:

VÍ DỤ CẤU TRÚC JSON:
```json
{{ 
  "topic": "{topic_name}",
  "locations": [
    {{ "id": "location_s001"}} 
  ],
  "tasks": [
    {{ 
      "id": "task_{topic_name}_001",
      "seq": 1,
      "question": {{ 
        "stem": "Nội dung câu hỏi 1 là gì?",
        "options": ["Phương án A", "Phương án B", "Phương án C", "Phương án D"],
        "correct": 1
      }} 
    }} 
  ]
}} 
```
"""
    content_list = [{"type": "text", "text": prompt}]
    if use_vision:
        print(" Đang chuyển đổi PDF sang ảnh để AI đọc (Vision Mode)...")
        b64_images = get_base64_images_from_pdf(file_path)
        for b64 in b64_images:
            content_list.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{b64}"}
            })
        model_to_use = "qwen/qwen3-14b"
    else:
        content_list.append({"type": "text", "text": f"\nNỘI DUNG VĂN BẢN:\n{text_content}"})
        model_to_use = "qwen/qwen3-14b"
    print(f" Đang gửi dữ liệu cho AI (Model: {model_to_use}) để trích xuất...")
    import time
    for attempt in range(10):
        try:
            response = client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": "Bạn là công cụ trích xuất dữ liệu sang JSON chuẩn xác 100%. Mọi dấu ngoặc kép bên trong chuỗi phải được escape thành \\\"."},
                    {"role": "user", "content": content_list}
                ],
                temperature=0.1,
                max_tokens=8192
            )
            break
        except Exception as e:
            if '503' in str(e) or '429' in str(e):
                print(f" Server bận (lần {attempt+1}/10), đang thử lại sau 10 giây...")
                time.sleep(10)
            else:
                raise e
    else:
        raise Exception("Server quá tải, đã thử lại 10 lần không thành công.")
    full_response = response.choices[0].message.content
    json_str = extract_json_from_text(full_response)
    try:
        seed_data = json.loads(json_str)
    except json.JSONDecodeError as json_err:
        print(f" [Auto-Fix] Phát hiện lỗi cú pháp JSON ({json_err}). Đang tự động sửa chữa bằng json_repair...")
        try:
            from json_repair import repair_json
            seed_data = repair_json(json_str, return_objects=True)
            if not isinstance(seed_data, dict) or "tasks" not in seed_data:
                raise ValueError("JSON repair không khôi phục được cấu trúc seed hợp lệ.")
            print(" -> Sửa lỗi JSON thành công 100%!")
        except Exception as e2:
            print(" Lỗi: Không thể phân tích JSON từ AI.")
            print(f"Chi tiết phản hồi của AI:\n{full_response}")
            raise e2

    # Hậu kiểm: Đảm bảo không có lựa chọn nào bị rỗng hoặc chỉ có khoảng trắng
    for task in seed_data.get("tasks", []):
        q = task.get("question", {})
        opts = q.get("options", [])
        for idx, opt in enumerate(opts):
            if not str(opt).strip():
                opts[idx] = f"Phương án {chr(65 + idx)}"
    return seed_data
def main():
    parser = argparse.ArgumentParser(description="Trích xuất câu hỏi từ File thành Seed JSON")
    parser.add_argument("file_path", help="Đường dẫn tới file tài liệu chứa câu hỏi")
    parser.add_argument("--topic", default="tong_hop", help="Chủ đề của bộ câu hỏi")
    args = parser.parse_args()
    input_file = args.file_path
    try:
        raw_text = extract_text_from_file(input_file)
        use_vision = False
        if len(raw_text.strip()) < 100 and input_file.lower().endswith('.pdf'):
            print(" Phát hiện PDF dạng Scan (không có text). Kích hoạt chế độ AI Vision!")
            use_vision = True
        else:
            print(f" Đã trích xuất {len(raw_text)} ký tự văn bản.")
        seed_json = generate_seed_with_ai(input_file, raw_text, args.topic, use_vision=use_vision)
        output_path = SEEDS_DIR / f"seed_{args.topic}_auto.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(seed_json, f, ensure_ascii=False, indent=2)
        print(f"\n THÀNH CÔNG! Đã lưu seed file tại: {output_path}")
        print(f" Số câu hỏi: {len(seed_json.get('tasks', []))}")
    except Exception as e:
        print(f" Quá trình tạo Seed thất bại: {e}")
if __name__ == "__main__":
    main()