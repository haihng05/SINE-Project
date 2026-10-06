import sys
import json
import time
from pathlib import Path
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
PROJECT_ROOT = Path(__file__).parent
MODELS_DIR = PROJECT_ROOT / "models"
TOOLS_DIR = PROJECT_ROOT / "tools"
SEEDS_DIR = PROJECT_ROOT / "seeds"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
import os
import re
INKLECATE_PATH = TOOLS_DIR / "inklecate.exe"
sys.path.append(str(PROJECT_ROOT / "src"))
from validator import SINEValidator
from agents import SINEGenerator, SINEFixer, extract_ink_code
from openai import OpenAI

def generate_multistage_ink(client, model_name, seed, max_chunk=10):
    tasks = seed["tasks"]
    chunks = [tasks[i:i+max_chunk] for i in range(0, len(tasks), max_chunk)]
    total_stages = len(chunks)
    print(f" ⚙️ Tự động kích hoạt cơ chế Đa Màn ({total_stages} Màn chơi, mỗi màn tối đa {max_chunk} câu)!")
    
    stage_scripts = []
    topic = seed.get("topic", "Tổng hợp")
    
    for idx, chunk_tasks in enumerate(chunks, 1):
        print(f"  -> Đang sinh Màn {idx}/{total_stages} ({chunk_tasks[0]['id']} -> {chunk_tasks[-1]['id']})...")
        sub_seed = {
            "topic": topic,
            "locations": seed.get("locations", [])[(idx-1)*max_chunk : idx*max_chunk],
            "tasks": chunk_tasks
        }
        
        next_knot = f"act_{idx+1}_start" if idx < total_stages else "END"
        if idx == 1:
            guide = f"""1. Bắt đầu bằng:
-> start_knot
=== start_knot ===
(Đoạn văn mở đầu cốt truyện nhập vai, giới thiệu bối cảnh {topic})...
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn 1.
3. Khi hoàn thành câu hỏi cuối cùng của Màn 1:
   -> {next_knot}"""
        elif idx < total_stages:
            guide = f"""1. Bắt đầu ngay bằng knot (không có '-> start_knot' ở đầu):
=== act_{idx}_start ===
(Đoạn văn mở đầu Hồi {idx}, bước vào khu vực thử thách mới)...
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn {idx}.
3. Khi hoàn thành câu hỏi cuối cùng của Màn {idx}:
   -> {next_knot}"""
        else:
            guide = f"""1. Bắt đầu ngay bằng knot (không có '-> start_knot' ở đầu):
=== act_{idx}_start ===
(Đoạn văn mở đầu Hồi cuối / Trận chung kết)...
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn cuối.
3. Khi hoàn thành câu hỏi cuối cùng của Màn cuối:
   -> END"""

        prompt = f"""Bạn là chuyên gia thiết kế game giáo dục tương tác văn bản bằng ngôn ngữ Ink (.ink).
Nhiệm vụ: Lập trình HỒI {idx} (MÀN {idx}/{total_stages}) cho game chủ đề {topic}.

DỮ LIỆU CÂU HỎI MÀN {idx}:
{json.dumps(sub_seed, ensure_ascii=False, indent=2)}

QUY TẮC CẤU TRÚC:
{guide}

VÍ DỤ CẤU TRÚC INK CHUẨN:
```ink
=== task_01 ===
Nội dung câu hỏi?
+ [Phương án A] -> task_01_fail
+ [Phương án B] -> task_01_success
+ [Phương án C] -> task_01_fail
+ [Phương án D] -> task_01_fail

=== task_01_success ===
Chính xác!
-> next_knot

=== task_01_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_01
```

CÁC NGUYÊN TẮC BẮT BUỘC:
1. Viết toàn bộ câu chuyện và lời thoại bằng TIẾNG VIỆT tự nhiên, lôi cuốn.
2. BẮT BUỘC in NGUYÊN VĂN câu hỏi (stem) và tất cả phương án lựa chọn (options) từ Seed, không được tự ý tóm tắt hay bỏ bớt.
3. Đáp án đúng (correct index) chuyển tới knot thành công (`_success`), đáp án sai chuyển tới knot thất bại (`_fail`) cho phép thử lại.
4. SỬ DỤNG DẤU `+` (sticky choice) THAY VÌ DẤU `*`.
5. TUYỆT ĐỐI KHÔNG XUẤT ĐỊNH DẠNG JSON. BẮT BUỘC xuất mã nguồn Ink theo đúng mẫu ví dụ trên.

ĐỊNH DẠNG ĐẦU RA:
Hãy xuất toàn bộ mã nguồn Ink của Màn {idx} trong khối ```ink ... ```.
"""
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": f"Bạn là kỹ sư lập trình kịch bản Ink chuyên nghiệp cho Màn {idx}/{total_stages}. Chỉ xuất kịch bản Ink hợp lệ."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            top_p=0.9,
            max_tokens=4096
        )
        ink_script = extract_ink_code(response.choices[0].message.content)
        
        # Tự động escape { và }
        fixed_lines = []
        for line in ink_script.splitlines():
            if line.strip().startswith("===") or line.strip().startswith("->"):
                fixed_lines.append(line)
            else:
                l = re.sub(r'(?<!\\)\{', r'\{', line)
                l = re.sub(r'(?<!\\)\}', r'\}', l)
                fixed_lines.append(l)
        stage_scripts.append("\n".join(fixed_lines))
        print(f"    Hoàn tất Màn {idx} ({len(stage_scripts[-1].splitlines())} dòng)")

    # Ghép nối các màn
    combined_parts = []
    for s_idx, script in enumerate(stage_scripts, 1):
        cleaned = script.strip()
        if s_idx > 1:
            lines = cleaned.splitlines()
            start_line = 0
            for l_idx, line in enumerate(lines):
                if line.strip().startswith("==="):
                    start_line = l_idx
                    break
            cleaned = "\n".join(lines[start_line:])
            if f"=== act_{s_idx}_start ===" not in cleaned:
                first_knot_m = re.search(r"===\s*([a-zA-Z0-9_]+)\s*===", cleaned)
                if first_knot_m:
                    cleaned = f"=== act_{s_idx}_start ===\n-> {first_knot_m.group(1)}\n\n" + cleaned
                else:
                    cleaned = f"=== act_{s_idx}_start ===\n\n" + cleaned
def stitch_and_route_multistage_ink(stage_scripts: list[str], seed: dict, max_chunk: int = 10) -> tuple[str, str]:
    tasks = seed["tasks"]
    N = len(tasks)
    task_ids = [t["id"] for t in tasks]
    total_stages = (N + max_chunk - 1) // max_chunk
    topic = seed.get("topic", "Tổng hợp")

    combined_parts = []
    for s_idx, script in enumerate(stage_scripts, 1):
        cleaned = script.strip()
        if s_idx > 1:
            lines = cleaned.splitlines()
            start_line = 0
            for l_idx, line in enumerate(lines):
                if line.strip().startswith("==="):
                    start_line = l_idx
                    break
            cleaned = "\n".join(lines[start_line:])
            if f"=== act_{s_idx}_start ===" not in cleaned:
                first_knot_m = re.search(r"===\s*([a-zA-Z0-9_]+)\s*===", cleaned)
                if first_knot_m:
                    cleaned = f"=== act_{s_idx}_start ===\n-> {first_knot_m.group(1)}\n\n" + cleaned
                else:
                    cleaned = f"=== act_{s_idx}_start ===\n\n" + cleaned
        combined_parts.append(cleaned)
    final_ink = "\n\n".join(combined_parts)
    
    # 1. Đảm bảo điểm khởi đầu -> start_knot
    if not final_ink.strip().startswith("->"):
        final_ink = "-> start_knot\n\n" + final_ink
        
    # 2. Đảm bảo start_knot tồn tại và dẫn tới câu hỏi đầu tiên
    first_task = task_ids[0]
    if "=== start_knot ===" not in final_ink:
        final_ink = f"-> start_knot\n\n=== start_knot ===\nChào mừng bạn đến với thử thách môn {topic}!\n-> {first_task}\n\n" + final_ink
    else:
        parts = final_ink.split("=== start_knot ===", 1)
        body_rest = parts[1].split("===", 1)
        body = body_rest[0]
        if "->" not in body:
            body = body.strip() + f"\n-> {first_task}\n\n"
        elif not re.search(rf"->\s*{first_task}\b", body):
            body = re.sub(r"->\s*[a-zA-Z0-9_]+", f"-> {first_task}", body, count=1)
        final_ink = parts[0] + "=== start_knot ===" + body + ("===" + body_rest[1] if len(body_rest) > 1 else "")

    # 3. Chuẩn hóa chuyển màn act_{act_num}_start
    for act_num in range(2, total_stages + 1):
        act_first_task = task_ids[(act_num - 1) * max_chunk]
        act_knot = f"=== act_{act_num}_start ==="
        if act_knot in final_ink:
            parts = final_ink.split(act_knot, 1)
            body_rest = parts[1].split("===", 1)
            body = body_rest[0]
            if "->" in body:
                body = re.sub(r"->\s*[a-zA-Z0-9_]+", f"-> {act_first_task}", body)
            else:
                body = body.strip() + f"\n-> {act_first_task}\n\n"
            final_ink = parts[0] + act_knot + "\n" + body + ("===" + body_rest[1] if len(body_rest) > 1 else "")
        else:
            final_ink += f"\n\n=== act_{act_num}_start ===\nBước vào Hồi {act_num}!\n-> {act_first_task}\n"

    # 4. Định tuyến chính xác cho từng câu hỏi (Success & Fail knots)
    for i in range(N):
        curr_t = task_ids[i]
        success_knot = f"{curr_t}_success"
        fail_knot = f"{curr_t}_fail"
        
        if i == N - 1:
            target = "END"
        elif (i + 1) % max_chunk == 0:
            act_num = (i + 1) // max_chunk + 1
            target = f"act_{act_num}_start"
        else:
            target = task_ids[i+1]
            
        # Success knot
        if f"=== {success_knot} ===" not in final_ink:
            final_ink += f"\n\n=== {success_knot} ===\nChính xác! Bạn trả lời rất chuẩn.\n-> {target}\n"
        else:
            parts = final_ink.split(f"=== {success_knot} ===", 1)
            body_rest = parts[1].split("===", 1)
            body = body_rest[0]
            if "->" in body:
                body = re.sub(r"->\s*[a-zA-Z0-9_]+", f"-> {target}", body)
            else:
                body = body.strip() + f"\n-> {target}\n\n"
            final_ink = parts[0] + f"=== {success_knot} ===" + body + ("===" + body_rest[1] if len(body_rest) > 1 else "")
            
        # Fail knot
        if f"=== {fail_knot} ===" not in final_ink:
            final_ink += f"\n\n=== {fail_knot} ===\nSai rồi! Hãy thử lại.\n+ [Thử lại câu hỏi này] -> {curr_t}\n"

    # 5. Đảm bảo các sticky choices được bọc trong [ ... ] để nội dung nút bấm không bị in dính vào câu phản hồi
    def wrap_choice_brackets(match):
        prefix = match.group(1)
        text = match.group(2).strip()
        divert = match.group(3)
        if not text.startswith("["):
            return f"{prefix}[{text}] {divert}"
        return match.group(0)
    final_ink = re.sub(r"^(\s*[\+\*]\s*)([^\[\-\n]+?)(\s*->\s*[a-zA-Z0-9_]+)", wrap_choice_brackets, final_ink, flags=re.MULTILINE)

    # 6. Dọn dẹp bất kỳ divert tạm bợ (next_task, next_knot)
    final_ink = re.sub(r"->\s*next_task\b", f"-> {task_ids[1] if len(task_ids)>1 else 'END'}", final_ink)
    final_ink = re.sub(r"->\s*next_knot\b", f"-> {task_ids[1] if len(task_ids)>1 else 'END'}", final_ink)

    # 7. Khử trùng lặp knot (ngăn ngừa tuyệt đối lỗi: Story already contains flow named '...')
    final_ink = deduplicate_knots(final_ink)

    return final_ink, "Multi-stage auto-chunk generation completed successfully."

def deduplicate_knots(ink_text: str) -> str:
    """Loại bỏ các knot bị định nghĩa trùng lặp (ví dụ 2 lần === act_2_start ===)."""
    parts = re.split(r"(===\s*[a-zA-Z0-9_]+\s*===)", ink_text)
    seen_knots = set()
    result = [parts[0]]
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1] if i + 1 < len(parts) else ""
        knot_name_match = re.search(r"===\s*([a-zA-Z0-9_]+)\s*===", header)
        if knot_name_match:
            knot_name = knot_name_match.group(1).strip()
            if knot_name in seen_knots:
                continue
            seen_knots.add(knot_name)
        result.append(header)
        result.append(body)
    return "".join(result)

def auto_heal_ink(ink_text: str, seed: dict, error_log: str, max_chunk: int = 10) -> str:
    """Tự động sửa chữa lỗi liên kết divert và knot thiếu mà không phá vỡ cấu trúc kịch bản."""
    # 0. Khử trùng lặp knot nếu có lỗi: "Story already contains flow named"
    ink_text = deduplicate_knots(ink_text)

    tasks = seed.get("tasks", [])
    task_ids = [t["id"] for t in tasks]
    
    # Tìm các target divert bị thiếu từ log của inklecate
    missing_targets = re.findall(r"Divert target not found: '->\s*([a-zA-Z0-9_]+)'", error_log)
    for target in set(missing_targets):
        if f"=== {target} ===" not in ink_text:
            if target.endswith("_fail"):
                parent_task = target[:-5]
                ink_text += f"\n\n=== {target} ===\nSai rồi! Hãy suy nghĩ kỹ lại.\n+ [Thử lại câu hỏi] -> {parent_task}\n"
            elif target.endswith("_success"):
                parent_task = target[:-8]
                try:
                    idx = task_ids.index(parent_task)
                    nxt = task_ids[idx+1] if idx + 1 < len(task_ids) else "END"
                except Exception:
                    nxt = "END"
                ink_text += f"\n\n=== {target} ===\nChính xác!\n-> {nxt}\n"
            elif target.startswith("task_"):
                ink_text += f"\n\n=== {target} ===\nCâu hỏi tiếp theo...\n-> END\n"
            else:
                ink_text += f"\n\n=== {target} ===\nTiếp tục hành trình!\n-> END\n"
                
    # Dọn dẹp loose ends nếu có
    if "Apparent loose end exists" in error_log:
        if not ink_text.strip().endswith("-> END") and not ink_text.strip().endswith("END"):
            ink_text += "\n-> END\n"
            
    return ink_text

def generate_multistage_ink(client, model_name, seed, max_chunk=10):
    tasks = seed["tasks"]
    chunks = [tasks[i:i+max_chunk] for i in range(0, len(tasks), max_chunk)]
    total_stages = len(chunks)
    print(f" ⚙️ Tự động kích hoạt cơ chế Đa Màn ({total_stages} Màn chơi, mỗi màn tối đa {max_chunk} câu)!")
    
    stage_scripts = []
    topic = seed.get("topic", "Tổng hợp")
    
    for idx, chunk_tasks in enumerate(chunks, 1):
        print(f"  -> Đang sinh Màn {idx}/{total_stages} ({chunk_tasks[0]['id']} -> {chunk_tasks[-1]['id']})...")
        sub_seed = {
            "topic": topic,
            "locations": seed.get("locations", [])[(idx-1)*max_chunk : idx*max_chunk],
            "tasks": chunk_tasks
        }
        
        next_knot = f"act_{idx+1}_start" if idx < total_stages else "END"
        first_task_id = chunk_tasks[0]['id']
        if idx == 1:
            guide = f"""1. Bắt đầu bằng:
-> start_knot
=== start_knot ===
(Đoạn văn mở đầu cốt truyện nhập vai, giới thiệu bối cảnh {topic})...
-> {first_task_id}
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn 1.
3. Khi hoàn thành câu hỏi cuối cùng của Màn 1:
   -> {next_knot}"""
        elif idx < total_stages:
            guide = f"""1. Bắt đầu ngay bằng knot (không có '-> start_knot' ở đầu):
=== act_{idx}_start ===
(Đoạn văn mở đầu Hồi {idx}, bước vào khu vực thử thách mới)...
-> {first_task_id}
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn {idx}.
3. Khi hoàn thành câu hỏi cuối cùng của Màn {idx}:
   -> {next_knot}"""
        else:
            guide = f"""1. Bắt đầu ngay bằng knot (không có '-> start_knot' ở đầu):
=== act_{idx}_start ===
(Đoạn văn mở đầu Hồi cuối / Trận chung kết)...
-> {first_task_id}
2. Lần lượt dẫn dắt người chơi qua từng câu hỏi của Màn cuối.
3. Khi hoàn thành câu hỏi cuối cùng của Màn cuối:
   -> END"""

        prompt = f"""Bạn là chuyên gia thiết kế game giáo dục tương tác văn bản bằng ngôn ngữ Ink (.ink).
Nhiệm vụ: Lập trình HỒI {idx} (MÀN {idx}/{total_stages}) cho game chủ đề {topic}.

DỮ LIỆU CÂU HỎI MÀN {idx}:
{json.dumps(sub_seed, ensure_ascii=False, indent=2)}

QUY TẮC CẤU TRÚC:
{guide}

VÍ DỤ CẤU TRÚC INK CHUẨN:
```ink
=== task_01 ===
Nội dung câu hỏi?
+ [Phương án A] -> task_01_fail
+ [Phương án B] -> task_01_success
+ [Phương án C] -> task_01_fail
+ [Phương án D] -> task_01_fail

=== task_01_success ===
Chính xác!
-> task_02

=== task_01_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_01
```

CÁC NGUYÊN TẮC BẮT BUỘC:
1. Viết toàn bộ câu chuyện và lời thoại bằng TIẾNG VIỆT tự nhiên, lôi cuốn.
2. BẮT BUỘC in NGUYÊN VĂN câu hỏi (stem) và tất cả phương án lựa chọn (options) từ Seed, không được tự ý tóm tắt hay bỏ bớt.
3. Đáp án đúng (correct index) chuyển tới knot thành công (`_success`), đáp án sai chuyển tới knot thất bại (`_fail`) cho phép thử lại.
4. SỬ DỤNG DẤU `+` (sticky choice) THAY VÌ DẤU `*`.
5. TUYỆT ĐỐI KHÔNG XUẤT ĐỊNH DẠNG JSON. BẮT BUỘC xuất mã nguồn Ink theo đúng mẫu ví dụ trên.

ĐỊNH DẠNG ĐẦU RA:
Hãy xuất toàn bộ mã nguồn Ink của Màn {idx} trong khối ```ink ... ```.
"""
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": f"Bạn là kỹ sư lập trình kịch bản Ink chuyên nghiệp cho Màn {idx}/{total_stages}. Chỉ xuất kịch bản Ink hợp lệ."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            top_p=0.9,
            max_tokens=4096
        )
        ink_script = extract_ink_code(response.choices[0].message.content)
        
        # Tự động escape { và }
        fixed_lines = []
        for line in ink_script.splitlines():
            if line.strip().startswith("===") or line.strip().startswith("->"):
                fixed_lines.append(line)
            else:
                l = re.sub(r'(?<!\\)\{', r'\{', line)
                l = re.sub(r'(?<!\\)\}', r'\}', l)
                fixed_lines.append(l)
        stage_scripts.append("\n".join(fixed_lines))
        print(f"    Hoàn tất Màn {idx} ({len(stage_scripts[-1].splitlines())} dòng)")

    return stitch_and_route_multistage_ink(stage_scripts, seed, max_chunk=max_chunk)

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

def run_sine_trial(seed_filename: str = "seed_media_vi_01.json", max_fix_iterations: int = 3):
    seed_path = SEEDS_DIR / seed_filename
    if not seed_path.exists():
        print(f" Không tìm thấy file seed: {seed_path}")
        return
    with open(seed_path, "r", encoding="utf-8-sig") as f:
        seed = json.load(f)
    
    # Bảo vệ: Đảm bảo không có lựa chọn (options) nào bị rỗng hoặc chỉ có khoảng trắng
    for task in seed.get("tasks", []):
        q = task.get("question", {})
        opts = q.get("options", [])
        for idx, opt in enumerate(opts):
            if not str(opt).strip():
                opts[idx] = f"Phương án {chr(65 + idx)}"
    print("=" * 65)
    print(" BẮT ĐẦU CHẠY THỬ NGHIỆM HỆ THỐNG SINE")
    print(f" File Seed đầu vào: {seed_filename} ({seed.get('topic', 'Chung')})")
    print(f" Số địa điểm: {len(seed.get('locations', []))} | Số câu hỏi: {len(seed.get('tasks', []))}")
    print("=" * 65)
    api_key = get_openrouter_api_key()
    if not api_key:
        print("❌ Chưa cấu hình OPENROUTER_API_KEY. Vui lòng thiết lập biến môi trường hoặc ghi vào file .env!")
        return
    print(" Đang kết nối tới API...")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    model_name = "qwen/qwen3-14b"
    print(f" Đã kết nối API! Model đang sử dụng: {model_name}")
    validator = SINEValidator(INKLECATE_PATH)
    generator = SINEGenerator(client, model_name)
    fixer = SINEFixer(client, model_name)
    temp_ink_path = OUTPUT_DIR / "temp_trial.ink"
    final_output_path = OUTPUT_DIR / f"game_{Path(seed_filename).stem}.ink"
    
    is_multistage = len(seed.get("tasks", [])) > 12
    if is_multistage:
        print(f" [BƯỚC 1/3] Kích hoạt cơ chế Đa Màn (Multi-Stage) cho bộ đề {len(seed['tasks'])} câu...")
        t0 = time.time()
        ink_script, reasoning = generate_multistage_ink(client, model_name, seed)
        gen_time = time.time() - t0
        print(f" Tổng thời gian sinh toàn bộ các màn: {gen_time:.1f}s")
    else:
        print(" [BƯỚC 1/3] Generator Agent đang tư duy và viết kịch bản Ink...")
        t0 = time.time()
        ink_script, reasoning = generator.generate(seed)
        gen_time = time.time() - t0
        print(f" Thời gian sinh kịch bản: {gen_time:.1f}s")
    print("\n [BƯỚC 2/3] Tiến hành kiểm tra tự động 3 tiêu chí (C, P, Q)...")
    val_res = validator.validate_all(ink_script, seed, temp_ink_path)
    print(f"  • Biên dịch cú pháp (C - Compilation): {' ĐẠT' if val_res['compilation'] else ' LỖI'}")
    print(f"  • Khả năng chơi được (P - Playability): {' ĐẠT' if val_res['playability'] else ' LỖI'}")
    print(f"  • Trung thực mục tiêu (Q - Fidelity):   {' ĐẠT' if val_res['fidelity'] else ' LỖI'}")
    iteration = 1
    while not val_res["success"] and iteration <= max_fix_iterations:
        print(f"\n Phát hiện lỗi! Kích hoạt cơ chế sửa đổi (Lần sửa {iteration}/{max_fix_iterations})...")
        print(f" Nội dung lỗi:\n{val_res['error_log']}\n")
        
        if is_multistage:
            print(f" [Auto-Healer] Tự động sửa chữa cấu trúc và liên kết Ink cho bộ đề lớn...")
            ink_script = auto_heal_ink(ink_script, seed, val_res["error_log"])
            ink_script, _ = stitch_and_route_multistage_ink([ink_script], seed)
        else:
            print(f" Fixer Agent đang sửa đổi kịch bản...")
            t_fix = time.time()
            ink_script, _ = fixer.repair(seed, ink_script, val_res["error_log"])
            print(f" Thời gian sửa: {time.time() - t_fix:.1f}s")
            
        print(" Kiểm tra lại sau khi sửa...")
        val_res = validator.validate_all(ink_script, seed, temp_ink_path)
        print(f"  • Biên dịch (C): {' ĐẠT' if val_res['compilation'] else ' LỖI'} | Chơi được (P): {' ĐẠT' if val_res['playability'] else ' LỖI'} | Trung thực (Q): {' ĐẠT' if val_res['fidelity'] else ' LỖI'}")
        iteration += 1
    print("\n" + "=" * 65)
    if val_res["success"]:
        final_output_path.write_text(ink_script, encoding="utf-8")
        print(f" THÀNH CÔNG! KỊCH BẢN GAME ĐÃ HỢP LỆ 100% VÀ SẴN SÀNG CHƠI!")
        print(f"💾 File kịch bản đã lưu tại: {final_output_path}")
        print("=" * 65)
        print("\n🎮 HƯỚNG DẪN CHƠI THỬ TRỰC TIẾP TRÊN TERMINAL:")
        print(f"Gõ lệnh sau để chơi game:")
        print(f"  .\\tools\\inklecate.exe -p output\\{final_output_path.name}")
        print("=" * 65)
    else:
        print(" Sau các lần sửa, kịch bản vẫn chưa vượt qua toàn bộ tiêu chí.")
        print(f"Chi tiết lỗi cuối cùng:\n{val_res['error_log']}")
        print("=" * 65)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chạy thử nghiệm hệ thống SINE với 1 file seed JSON")
    parser.add_argument("--seed", default="seed_media_vi_01.json", help="Tên file seed trong thư mục seeds/")
    args = parser.parse_args()
    run_sine_trial(seed_filename=args.seed)