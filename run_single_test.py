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
INKLECATE_PATH = TOOLS_DIR / "inklecate.exe"
sys.path.append(str(PROJECT_ROOT / "src"))
from validator import SINEValidator
from agents import SINEGenerator, SINEFixer
from openai import OpenAI
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
        print(f"\n Phát hiện lỗi! Kích hoạt Fixer Agent (Lần sửa {iteration}/{max_fix_iterations})...")
        print(f" Nội dung lỗi:\n{val_res['error_log']}\n")
        print(f" Fixer Agent đang sửa đổi kịch bản...")
        t_fix = time.time()
        ink_script, _ = fixer.repair(seed, ink_script, val_res["error_log"])
        print(f" Thời gian sửa: {time.time() - t_fix:.1f}s")
        print(" Kiểm tra lại sau khi sửa...")
        val_res = validator.validate_all(ink_script, seed, temp_ink_path)
        print(f"  • Biên dịch (C): {'' if val_res['compilation'] else ''} | Chơi được (P): {'' if val_res['playability'] else ''} | Trung thực (Q): {'' if val_res['fidelity'] else ''}")
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