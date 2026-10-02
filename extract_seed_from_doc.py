import os
import sys
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
1. Xác định đúng câu hỏi (stem), các lựa chọn (options) và đáp án đúng (nếu văn bản có chỉ định, nếu không hãy tự suy luận đáp án đúng hợp lý nhất).
2. Tạo danh sách các "locations" (địa điểm trong game) tương ứng. Bạn có thể tự sáng tạo tên địa điểm (ví dụ: "location_phong_thi_nghiem", "location_thu_vien") sao cho phù hợp với chủ đề "{topic_name}".
3. Trả về DUY NHẤT một khối JSON theo cấu trúc mẫu sau (nằm trong ```json ... ```):
VÍ DỤ CẤU TRÚC JSON:
```json
{ 
  "topic": "{topic_name}",
  "locations": [
    { "id": "location_s001"} 
  ],
  "tasks": [
    { 
      "id": "task_{topic_name}_001",
      "seq": 1,
      "question": { 
        "stem": "Nội dung câu hỏi 1 là gì?",
        "options": ["Lựa chọn A", "Lựa chọn B", "Lựa chọn C", "Lựa chọn D"],
        "correct": 1
      } 
    } 
  ]
} 
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
        content_list.append({"type": "text", "text": f"\\nNỘI DUNG VĂN BẢN:\\n{text_content}"})
        model_to_use = "qwen/qwen3-14b"
    print(f" Đang gửi dữ liệu cho AI (Model: {model_to_use}) để trích xuất...")
    import time
    for attempt in range(10):
        try:
            response = client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": "Bạn là công cụ trích xuất dữ liệu sang JSON. Chỉ trả lời bằng JSON."},
                    {"role": "user", "content": content_list}
                ],
                temperature=0.1
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
        return seed_data
    except json.JSONDecodeError as e:
        print(" Lỗi: AI không trả về JSON hợp lệ.")
        print(f"Chi tiết phản hồi của AI:\n{full_response}")
        raise e
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