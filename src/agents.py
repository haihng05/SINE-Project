import re
import json
from llama_cpp import Llama

def extract_ink_code(text: str) -> str:
    """Trích xuất khối mã ```ink ... ``` từ phản hồi của LLM."""
    match = re.search(r"```(?:ink)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        code = match.group(1).strip()
    else:
        code = text.strip()
    # Loại bỏ các tag thừa ngoài Ink nếu có
    return code

class SINEGenerator:
    def __init__(self, llm: Llama):
        self.llm = llm

    def generate(self, seed: dict) -> tuple[str, str]:
        """Sinh kịch bản ban đầu theo chiến lược S3 (Reasoning Required + Few-Shot)."""
        prompt = f"""Bạn là một chuyên gia thiết kế game giáo dục tương tác văn bản (Interactive Fiction Serious Game) bằng ngôn ngữ Ink (.ink).

Hãy dựa vào dữ liệu SEED JSON dưới đây để tạo ra một kịch bản game Ink hoàn chỉnh:

DỮ LIỆU SEED (JSON):
{json.dumps(seed, ensure_ascii=False, indent=2)}

VÍ DỤ CẤU TRÚC KỊCH BẢN INK CHUẨN MẪU:
```ink
-> location_start

=== location_start ===
Bạn bước vào căn phòng âm thanh cũ kỹ. Không gian tĩnh lặng, chỉ có tiếng kim đĩa than rè rè.
* [Kiểm tra bàn điều khiển] -> task_01_knot

=== task_01_knot ===
Hệ màu nào sau đây được sử dụng chủ yếu trong kỹ thuật in ấn thương mại?
* [RGB] -> task_01_fail
* [CMYK] -> task_01_success
* [HSV] -> task_01_fail
* [Lab] -> task_01_fail

=== task_01_success ===
Chính xác! Bàn điều khiển bật sáng đèn xanh, mở ra cánh cửa dẫn đến phòng tiếp theo.
-> location_next

=== task_01_fail ===
Sai rồi! Báo động đỏ kêu vang.
* [Thử lại câu hỏi này] -> task_01_knot

=== location_next ===
... (tiếp tục dẫn tới câu hỏi tiếp theo) ...
-> END
```

CÁC NGUYÊN TẮC BẮT BUỘC:
1. Viết toàn bộ câu chuyện và lời thoại bằng TIẾNG VIỆT tự nhiên, hấp dẫn.
2. BẮT BUỘC in NGUYÊN VĂN câu hỏi (stem) và tất cả phương án lựa chọn (options) từ Seed, không được tự ý tóm tắt hay bỏ bớt.
3. Đáp án đúng (correct index) phải chuyển tới knot thành công (`_success`), đáp án sai chuyển tới knot thất bại (`_fail`) cho phép thử lại.
4. Cuối game phải có đường dẫn tới `-> END`.

ĐỊNH DẠNG ĐẦU RA:
Hãy suy luận ngắn gọn kế hoạch cốt truyện trong <think>...</think>, sau đó xuất toàn bộ mã nguồn trong khối ```ink ... ```.
"""
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "Bạn là chuyên gia lập trình kịch bản Ink cho game giáo dục nghiêm túc (SINE). Hãy luôn xuất kịch bản trong khối ```ink ... ```."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Giảm nhiệt độ để tăng độ chính xác cấu trúc
            top_p=0.9,
            max_tokens=2048
        )
        full_text = response["choices"][0]["message"]["content"]
        ink_script = extract_ink_code(full_text)
        return ink_script, full_text

class SINEFixer:
    def __init__(self, llm: Llama):
        self.llm = llm

    def repair(self, seed: dict, current_ink: str, error_log: str) -> tuple[str, str]:
        """Tác tử sửa lỗi (Fixer Agent): Sửa kịch bản dựa trên Error Log."""
        prompt = f"""Kịch bản Ink của bạn gặp các lỗi kiểm tra tự động sau:

NHẬT KÝ LỖI (ERROR LOG):
{error_log}

KỊCH BẢN INK CẦN SỬA:
```ink
{current_ink}
```

DỮ LIỆU SEED GỐC:
{json.dumps(seed, ensure_ascii=False, indent=2)}

HƯỚNG DẪN SỬA LỖI:
1. Hãy đảm bảo IN ĐẦY ĐỦ VÀ CHÍNH XÁC TỪNG CHỮ của các câu hỏi (stem) và các lựa chọn (options) trong Seed.
2. Đảm bảo mọi nhánh lựa chọn đều có đích đến hợp lệ và có đường đi đến `-> END`.
3. Xuất kịch bản đã sửa hoàn chỉnh trong khối ```ink ... ```.
"""
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "Bạn là kỹ sư sửa lỗi kịch bản Ink tự động. Hãy xuất kịch bản đã sửa trong khối ```ink ... ```."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            top_p=0.9,
            max_tokens=2048
        )
        full_text = response["choices"][0]["message"]["content"]
        repaired_ink = extract_ink_code(full_text)
        return repaired_ink, full_text
