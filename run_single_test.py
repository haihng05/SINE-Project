import sys
import json
import time
from pathlib import Path

# Đảm bảo in tiếng Việt mượt mà trên console Windows
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

INKLECATE_PATH = TOOLS_DIR / "inklecate.exe"

# Import các module SINE
sys.path.append(str(PROJECT_ROOT / "src"))
from validator import SINEValidator
from agents import SINEGenerator, SINEFixer
from llama_cpp import Llama

def run_sine_trial(seed_filename: str = "seed_media_vi_01.json", max_fix_iterations: int = 3):
    seed_path = SEEDS_DIR / seed_filename
    if not seed_path.exists():
        print(f"❌ Không tìm thấy file seed: {seed_path}")
        return

    with open(seed_path, "r", encoding="utf-8-sig") as f:
        seed = json.load(f)

    print("=" * 65)
    print("🚀 BẮT ĐẦU CHẠY THỬ NGHIỆM HỆ THỐNG SINE")
    print(f"📌 File Seed đầu vào: {seed_filename} ({seed.get('topic', 'Chung')})")
    print(f"📌 Số địa điểm: {len(seed.get('locations', []))} | Số câu hỏi: {len(seed.get('tasks', []))}")
    print("=" * 65)

    # 1. Khởi tạo mô hình LLM
    gguf_files = list(MODELS_DIR.glob("*.gguf"))
    if not gguf_files:
        print("❌ Chưa có file model .gguf trong thư mục models/!")
        return

    model_path = gguf_files[0]
    print(f"[*] Đang tải mô hình vào bộ nhớ: {model_path.name}...")
    llm = Llama(
        model_path=str(model_path),
        n_ctx=4096,
        n_gpu_layers=-1,  # Tận dụng GPU nếu có, tự về CPU nếu không
        verbose=False
    )
    print("✅ Mô hình đã sẵn sàng!\n")

    validator = SINEValidator(INKLECATE_PATH)
    generator = SINEGenerator(llm)
    fixer = SINEFixer(llm)

    temp_ink_path = OUTPUT_DIR / "temp_trial.ink"
    final_output_path = OUTPUT_DIR / f"game_{Path(seed_filename).stem}.ink"

    # 2. Generator Agent sinh bản thảo đầu tiên
    print("🤖 [BƯỚC 1/3] Generator Agent đang tư duy và viết kịch bản Ink...")
    t0 = time.time()
    ink_script, reasoning = generator.generate(seed)
    gen_time = time.time() - t0
    print(f"⏱️ Thời gian sinh kịch bản: {gen_time:.1f}s")

    # 3. Tiến hành kiểm tra tự động
    print("\n🔍 [BƯỚC 2/3] Tiến hành kiểm tra tự động 3 tiêu chí (C, P, Q)...")
    val_res = validator.validate_all(ink_script, seed, temp_ink_path)

    print(f"  • Biên dịch cú pháp (C - Compilation): {'✅ ĐẠT' if val_res['compilation'] else '❌ LỖI'}")
    print(f"  • Khả năng chơi được (P - Playability): {'✅ ĐẠT' if val_res['playability'] else '❌ LỖI'}")
    print(f"  • Trung thực mục tiêu (Q - Fidelity):   {'✅ ĐẠT' if val_res['fidelity'] else '❌ LỖI'}")

    iteration = 1
    # 4. Fixer Agent lặp sửa lỗi nếu cần
    while not val_res["success"] and iteration <= max_fix_iterations:
        print(f"\n⚠️ Phát hiện lỗi! Kích hoạt Fixer Agent (Lần sửa {iteration}/{max_fix_iterations})...")
        print(f"📋 Nội dung lỗi:\n{val_res['error_log']}\n")
        
        print(f"🛠️ Fixer Agent đang sửa đổi kịch bản...")
        t_fix = time.time()
        ink_script, _ = fixer.repair(seed, ink_script, val_res["error_log"])
        print(f"⏱️ Thời gian sửa: {time.time() - t_fix:.1f}s")
        
        print("🔍 Kiểm tra lại sau khi sửa...")
        val_res = validator.validate_all(ink_script, seed, temp_ink_path)
        print(f"  • Biên dịch (C): {'✅' if val_res['compilation'] else '❌'} | Chơi được (P): {'✅' if val_res['playability'] else '❌'} | Trung thực (Q): {'✅' if val_res['fidelity'] else '❌'}")
        iteration += 1

    print("\n" + "=" * 65)
    if val_res["success"]:
        final_output_path.write_text(ink_script, encoding="utf-8")
        print(f"🎉 THÀNH CÔNG! KỊCH BẢN GAME ĐÃ HỢP LỆ 100% VÀ SẴN SÀNG CHƠI!")
        print(f"💾 File kịch bản đã lưu tại: {final_output_path}")
        print("=" * 65)
        print("\n🎮 HƯỚNG DẪN CHƠI THỬ TRỰC TIẾP TRÊN TERMINAL:")
        print(f"Gõ lệnh sau để chơi game:")
        print(f"  .\\tools\\inklecate.exe -p output\\{final_output_path.name}")
        print("=" * 65)
    else:
        print("❌ Sau các lần sửa, kịch bản vẫn chưa vượt qua toàn bộ tiêu chí.")
        print(f"Chi tiết lỗi cuối cùng:\n{val_res['error_log']}")
        print("=" * 65)

if __name__ == "__main__":
    run_sine_trial()
