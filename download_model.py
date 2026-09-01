import sys
from pathlib import Path
from huggingface_hub import hf_hub_download

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).parent
MODELS_DIR = PROJECT_ROOT / "models"
MODELS_DIR.mkdir(exist_ok=True)

# Repository GGUF chuẩn quốc tế, công khai 100% không cần token:
REPO_ID = "bartowski/Qwen2.5-7B-Instruct-GGUF"

# Bạn có thể chọn:
# 1. "Qwen2.5-7B-Instruct-Q4_K_M.gguf" (~4.68 GB, tối ưu tốc độ & RAM)
# 2. "Qwen2.5-7B-Instruct-Q8_0.gguf"   (~7.70 GB, độ chính xác cao nhất)
FILENAME = "Qwen2.5-7B-Instruct-Q4_K_M.gguf"

print("=" * 60)
print(f"[*] Đang chuẩn bị tải mô hình: {FILENAME}")
print(f"[*] Nguồn Hugging Face: {REPO_ID}")
print(f"[*] Thư mục đích: {MODELS_DIR}")
print("=" * 60)

model_path = hf_hub_download(
    repo_id=REPO_ID,
    filename=FILENAME,
    local_dir=str(MODELS_DIR),
    local_dir_use_symlinks=False
)

print("\n" + "=" * 60)
print(f"🎉 TẢI MÔ HÌNH THÀNH CÔNG!")
print(f"Đường dẫn file: {model_path}")
print("=" * 60)
