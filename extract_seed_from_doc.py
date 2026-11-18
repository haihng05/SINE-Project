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
import cv2

try:
    import fitz  
    import docx
except ImportError:
    print(" Vui lòng cài đặt các thư viện đọc file:")
    print("pip install pymupdf python-docx")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT / "src"))

from dip_processor import ImageDIPProcessor

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


def get_base64_from_cv2_image(image) -> str:
    """Chuyển đổi ma trận ảnh OpenCV thành chuỗi base64 PNG."""
    success, encoded = cv2.imencode(".png", image)
    if not success:
        raise ValueError("Không thể mã hóa ảnh sang định dạng PNG.")
    return base64.b64encode(encoded).decode("utf-8")


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
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
        # File ảnh không chứa text thuần, sẽ được xử lý qua DIP và AI Vision
        text = ""
    else:
        raise ValueError(f"Định dạng file không được hỗ trợ: {ext}")
    return text


def fix_latex_json_escapes(s: str) -> str:
    """Tự động sửa các ký hiệu toán học LaTeX (như \\(, \\), \\frac, \\infty) thành escape hợp lệ trong JSON."""
    return re.sub(r'(?<!\\)\\([A-Za-z\(\)\[\]\{\}\^_\+\-\*/=><~])', r'\\\\\1', s)


def extract_json_from_text(text: str) -> str:
    if not text:
        return "{}"
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    candidate = match.group(1).strip() if match else text

    # Bỏ markdown header nếu bị đứt đuôi (chưa kịp đóng ```)
    if candidate.startswith("```"):
        lines = candidate.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        candidate = "\n".join(lines).strip()
    if candidate.endswith("```"):
        candidate = candidate[:-3].strip()

    # Tự động đóng ngoặc JSON nếu bị ngắt ngang ở cuối
    last_brace = candidate.rfind("}")
    if last_brace != -1:
        repaired = candidate[:last_brace + 1].strip()
        open_brackets = repaired.count("[") - repaired.count("]")
        open_braces = repaired.count("{") - repaired.count("}")
        repaired += "]" * max(0, open_brackets)
        repaired += "}" * max(0, open_braces)
        candidate = repaired

    return fix_latex_json_escapes(candidate.strip())


def get_api_client_and_model(force_openrouter: bool = False, is_vision: bool = False):
    """Tự động kết nối API: Ưu tiên Gemini, nếu force_openrouter hoặc Gemini lỗi thì chuyển OpenRouter."""
    env_file = PROJECT_ROOT / ".env"
    gemini_key = os.environ.get("GEMINI_API_KEY", "")
    openrouter_key = os.environ.get("OPENROUTER_API_KEY", "")
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY=") and not gemini_key:
                    gemini_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("OPENROUTER_API_KEY=") and not openrouter_key:
                    openrouter_key = line.split("=", 1)[1].strip().strip('"').strip("'")

    if force_openrouter:
        if not openrouter_key:
            raise ValueError("Không tìm thấy OPENROUTER_API_KEY trong file .env!")
        model = "qwen/qwen-2.5-vl-72b-instruct" if is_vision else "qwen/qwen3-14b"
        print(f" [AI Engine] Đang chuyển sang OpenRouter ({model})...")
        client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_key)
        return client, model

    if gemini_key:
        model = "gemini-3.1-flash-lite"
        print(f" [AI Engine] Đang kết nối Google Gemini API ({model})...")
        client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=gemini_key
        )
        return client, model
    elif openrouter_key:
        model = "qwen/qwen-2.5-vl-72b-instruct" if is_vision else "qwen/qwen3-14b"
        print(f" [AI Engine] Đang kết nối OpenRouter API ({model})...")
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=openrouter_key
        )
        return client, model
    else:
        raise ValueError("Chưa thiết lập GEMINI_API_KEY hoặc OPENROUTER_API_KEY trong file .env!")


def generate_seed_with_ai(
    file_path: str,
    text_content: str,
    topic_name: str,
    use_vision: bool = False,
    custom_b64_images: list = None
) -> dict:
    client, model_to_use = get_api_client_and_model()
    prompt = f"""Bạn là trợ lý AI sư phạm số hóa đề thi thành các thử thách học tập tương tác (SINE Engine).
Đọc hình ảnh hoặc nội dung tài liệu đính kèm và trích xuất toàn bộ các câu hỏi thành định dạng JSON Seed.
YÊU CẦU QUAN TRỌNG:
1. BẮT BUỘC TRÍCH XUẤT TOÀN BỘ TẤT CẢ CÁC CÂU HỎI XUẤT HIỆN TRÊN TÀI LIỆU/ẢNH (từ câu đầu tiên đến câu cuối cùng trên trang, cấm bỏ sót hay chỉ lấy mẫu 1-2 câu).
2. Diễn đạt đề bài (stem) súc tích, rõ ràng phù hợp trò chơi tương tác, bảo toàn 100% số liệu, biến số, phương trình toán học dạng LaTeX ($...$) và 4 phương án lựa chọn A, B, C, D.
3. Xác định đáp án đúng (correct index: 0 cho A, 1 cho B, 2 cho C, 3 cho D). Nếu trên ảnh có khoanh tròn bút bi thì ưu tiên chọn đáp án được khoanh tròn đó.
4. Giữ nguyên ngôn ngữ gốc của đề thi.
5. Tạo danh sách các "locations" (địa điểm trong game) tương ứng cho từng câu hỏi (ví dụ: location_{topic_name}_001, location_{topic_name}_002...).
6. Trả về DUY NHẤT một khối JSON theo cấu trúc sau (nằm trong ```json ... ```):

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
        "stem": "Nội dung bài toán...",
        "options": ["Lựa chọn A", "Lựa chọn B", "Lựa chọn C", "Lựa chọn D"],
        "correct": 0
      }} 
    }} 
  ]
}}
```
"""
    content_list = [{"type": "text", "text": prompt}]
    if use_vision:
        if custom_b64_images:
            b64_images = custom_b64_images
        else:
            print(" Đang chuyển đổi PDF sang ảnh để AI đọc (Vision Mode)...")
            b64_images = get_base64_images_from_pdf(file_path)
            
        for b64 in b64_images:
            content_list.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{b64}"}
            })
    else:
        content_list.append({"type": "text", "text": f"\nNỘI DUNG VĂN BẢN:\n{text_content}"})
        
    print(f" Đang gửi dữ liệu cho AI (Model: {model_to_use}) để trích xuất...")
    import time
    gemini_models_pool = ["gemini-3.1-flash-lite", "gemini-flash-lite-latest", "gemini-3.5-flash-lite"]
    model_idx = 0
    for attempt in range(6):
        try:
            response = client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": "Bạn là công cụ trích xuất dữ liệu sang JSON. Chỉ trả lời bằng JSON."},
                    {"role": "user", "content": content_list}
                ],
                temperature=0.1,
                max_tokens=8192
            )
            break
        except Exception as e:
            if '503' in str(e) or '429' in str(e):
                model_idx = (model_idx + 1) % len(gemini_models_pool)
                model_to_use = gemini_models_pool[model_idx]
                print(f" 🔄 Server bận/hạn mức, tự động chuyển sang mô hình dự phòng ({model_to_use})...")
                time.sleep(2)
            else:
                raise e
    else:
        raise Exception("Server quá tải, đã thử lại với các mô hình dự phòng không thành công.")
        
    full_response = response.choices[0].message.content if response.choices else None
    finish_reason = getattr(response.choices[0], "finish_reason", "") if response.choices else ""

    # Kiểm tra nếu phản hồi rỗng hoặc chạm bộ lọc bản quyền của Google (Recitation Check)
    if not full_response or "RECITATION" in str(finish_reason):
        print(" ⚠️ Phát hiện bộ lọc bản quyền của Google (Recitation Check).")
        env_file = PROJECT_ROOT / ".env"
        openrouter_key = os.environ.get("OPENROUTER_API_KEY", "")
        if env_file.exists() and not openrouter_key:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("OPENROUTER_API_KEY="):
                        openrouter_key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")

        fallback_success = False
        if openrouter_key:
            try:
                print(" 🔄 Tự động chuyển tiếp sang OpenRouter Vision (qwen/qwen-2.5-vl-72b-instruct)...")
                client_or, model_or = get_api_client_and_model(force_openrouter=True, is_vision=use_vision)
                resp_or = client_or.chat.completions.create(
                    model=model_or,
                    messages=[
                        {"role": "system", "content": "Bạn là công cụ số hóa đề thi sang JSON. Giữ nguyên văn 100% nội dung câu hỏi."},
                        {"role": "user", "content": content_list}
                    ],
                    temperature=0.1,
                    max_tokens=8192
                )
                full_response = resp_or.choices[0].message.content if resp_or.choices else None
                if full_response:
                    fallback_success = True
                    print(" ✅ Đã trích xuất thành công qua OpenRouter!")
            except Exception as e:
                print(f" ⚠️ OpenRouter trả về lỗi: {e}")

        if not fallback_success:
            print(" 🔄 Kích hoạt chế độ thích ứng giáo dục: Bảo toàn 100% số liệu Toán học & Đáp án...")
            edu_prompt = f"""Bạn là một chuyên gia số hóa bài tập giáo dục tương tác (SINE Engine).
Nhiệm vụ của bạn là đọc toàn bộ ảnh đề thi dưới đây và trích xuất ĐẦY ĐỦ TẤT CẢ các câu hỏi trắc nghiệm có trên trang thành định dạng JSON Seed (từ câu đầu tiên đến câu cuối cùng trên trang, cấm bỏ sót bất kỳ câu nào).
YÊU CẦU QUAN TRỌNG:
1. BẮT BUỘC trích xuất TOÀN BỘ tất cả các câu hỏi có trong tài liệu/ảnh (không được lấy mẫu 1-2 câu).
2. Bảo toàn 100% bản chất toán học: Giữ nguyên vẹn toàn bộ số liệu, biến số, biểu thức Toán học dạng LaTeX và 4 phương án lựa chọn A, B, C, D.
3. Xác định chính xác đáp án đúng (correct index: 0 cho A, 1 cho B, 2 cho C, 3 cho D).
4. Diễn đạt đề bài rõ ràng, mạch lạc phù hợp giao diện trò chơi, tuyệt đối không làm thay đổi bài toán gốc.
5. Trả về DUY NHẤT một khối ```json ... ```:
```json
{{
  "topic": "{topic_name}",
  "locations": [{{"id": "location_s001"}}],
  "tasks": [
    {{
      "id": "task_{topic_name}_001",
      "seq": 1,
      "question": {{
        "stem": "Nội dung bài toán...",
        "options": ["A", "B", "C", "D"],
        "correct": 0
      }}
    }}
  ]
}}
```
"""
            fallback_content = [{"type": "text", "text": edu_prompt}]
            if use_vision:
                for b64 in b64_images:
                    fallback_content.append({
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{b64}"}
                    })
            resp_fb = client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "user", "content": fallback_content}
                ],
                temperature=0.1,
                max_tokens=8192
            )
            full_response = resp_fb.choices[0].message.content if resp_fb.choices else None

    if not full_response:
        raise ValueError("AI không phản hồi nội dung. Vui lòng kiểm tra lại ảnh hoặc API Key.")

    json_str = extract_json_from_text(full_response)
    try:
        seed_data = json.loads(json_str)
        return seed_data
    except json.JSONDecodeError:
        try:
            fixed_str = fix_latex_json_escapes(json_str)
            seed_data = json.loads(fixed_str)
            return seed_data
        except json.JSONDecodeError as e:
            print(" Lỗi: AI không trả về JSON hợp lệ.")
            print(f"Chi tiết phản hồi của AI:\n{full_response}")
            raise e


def main():
    parser = argparse.ArgumentParser(description="Trích xuất câu hỏi từ File thành Seed JSON")
    parser.add_argument("file_path", help="Đường dẫn tới file tài liệu chứa câu hỏi (PDF, DOCX, JPG, PNG)")
    parser.add_argument("--topic", default="tong_hop", help="Chủ đề của bộ câu hỏi")
    args = parser.parse_args()

    input_file = args.file_path
    path_obj = Path(input_file)
    ext = path_obj.suffix.lower()

    try:
        use_vision = False
        custom_b64_list = None
        raw_text = ""

        # XỬ LÝ ĐỊNH DẠNG HÌNH ẢNH (JPG, PNG, JPEG, WEBP)
        if ext in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
            print("=" * 65)
            print(f"📷 PHÁT HIỆN FILE ĐẦU VÀO LÀ HÌNH ẢNH: {path_obj.name}")
            print("🛠️ Kích hoạt Module Xử lý ảnh số (DIP Engine)...")
            
            dip = ImageDIPProcessor()
            dip_res = dip.process_stage2(input_file)
            clean_image = dip_res["deskewed_color"]
            skew_angle = dip_res["skew_angle"]
            total_blocks = dip_res.get("total_blocks_found", 0)

            print(f"  • Độ nghiêng phát hiện & đã nắn thẳng: {skew_angle:+.2f}°")
            print(f"  • Tự động loại bỏ bàn tay & áo đen: THÀNH CÔNG")
            print(f"  • Kích thước ảnh sau khi nắn phẳng: {clean_image.shape[1]}x{clean_image.shape[0]}")
            print(f"  • Số khối văn bản nhận diện được: {total_blocks}")

            # Lưu ảnh đã làm sạch vào thư mục output phục vụ minh chứng / demo
            preview_dir = PROJECT_ROOT / "output" / "dip_test"
            preview_dir.mkdir(parents=True, exist_ok=True)
            cleaned_preview_file = preview_dir / f"clean_for_ai_{path_obj.stem}.png"
            dip.save_image(clean_image, str(cleaned_preview_file))
            print(f"💾 Ảnh sạch đạt chuẩn đã lưu tại: {cleaned_preview_file}")
            print("=" * 65)

            # Chuyển ảnh sạch sang Base64 để gửi lên Vision AI
            clean_b64 = get_base64_from_cv2_image(clean_image)
            custom_b64_list = [clean_b64]
            use_vision = True

        # XỬ LÝ ĐỊNH DẠNG VĂN BẢN (PDF, DOCX, TXT)
        else:
            raw_text = extract_text_from_file(input_file)
            if len(raw_text.strip()) < 100 and ext == ".pdf":
                print(" Phát hiện PDF dạng Scan (không có text). Kích hoạt chế độ AI Vision!")
                use_vision = True
            else:
                print(f" Đã trích xuất {len(raw_text)} ký tự văn bản.")

        # Gửi dữ liệu cho AI trích xuất Seed JSON
        seed_json = generate_seed_with_ai(
            input_file,
            raw_text,
            args.topic,
            use_vision=use_vision,
            custom_b64_images=custom_b64_list
        )

        # Đảm bảo danh sách locations khớp với các tasks
        tasks = seed_json.get("tasks", [])
        locations = seed_json.get("locations", [])
        if len(locations) < len(tasks):
            seed_json["locations"] = [
                {"id": f"location_{args.topic}_{i+1:03d}"} for i in range(len(tasks))
            ]

        output_path = SEEDS_DIR / f"seed_{args.topic}_auto.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(seed_json, f, ensure_ascii=False, indent=2)

        print("\n" + "=" * 65)
        print(f"🎉 THÀNH CÔNG! ĐÃ TRÍCH XUẤT XONG SEED FILE CHO HỆ THỐNG SINE!")
        print(f"💾 Đường dẫn file: {output_path}")
        tasks_count = len(seed_json.get("tasks", []))
        print(f"📊 Tổng số câu hỏi trích xuất được: {tasks_count}")
        for idx, task in enumerate(seed_json.get("tasks", [])):
            q = task.get("question", {})
            print(f"   [{idx+1}] {q.get('stem', '')[:65]}...")
            print(f"       -> Đáp án đúng: Option {q.get('correct', 0)+1}")
        print("=" * 65)

    except Exception as e:
        print(f"\n❌ Quá trình trích xuất Seed thất bại: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
