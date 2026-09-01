import sys
import os
import json
import subprocess
from pathlib import Path

# Đảm bảo stdout không bị lỗi encoding cp1252 trên Windows
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
INKLECATE_PATH = TOOLS_DIR / "inklecate.exe"

def test_inklecate():
    print("[1/3] Kiem tra Trinh bien dich inklecate...")
    if not INKLECATE_PATH.exists():
        print(f"  [x] Chua co file inklecate.exe trong thu muc tools/")
        return False
    
    test_ink = PROJECT_ROOT / "temp_test.ink"
    test_ink.write_text("Hello SINE System! -> END\n", encoding="utf-8")
    
    try:
        res = subprocess.run([str(INKLECATE_PATH), "-j", str(test_ink)], capture_output=True, text=True)
        if test_ink.exists():
            test_ink.unlink()
        if res.returncode == 0:
            print("  [+] Trinh bien dich inklecate hoat dong tot!")
            return True
        else:
            print(f"  [x] Loi khi chay inklecate: {res.stderr}")
            return False
    except Exception as e:
        print(f"  [x] Khong the thuc thi inklecate: {e}")
        return False

def test_seeds():
    print("[2/3] Kiem tra cac kich ban goc (Structured Seeds)...")
    seed_files = list(SEEDS_DIR.glob("*.json"))
    if not seed_files:
        print(f"  [x] Khong tim thay file seed nao trong thu muc seeds/")
        return False
    
    valid_count = 0
    for sf in seed_files:
        try:
            with open(sf, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            assert "locations" in data and "tasks" in data
            valid_count += 1
        except Exception as e:
            print(f"  [x] File seed {sf.name} loi: {e}")
            
    if valid_count == len(seed_files):
        print(f"  [+] Da xac thuc thanh cong {valid_count} file seeds hop le.")
        return True
    return False

def test_llm_inference():
    print("[3/3] Kiem tra thu vien va model LLM...")
    try:
        from llama_cpp import Llama
        print("  [+] Thu vien llama-cpp-python da san sang!")
    except ImportError as e:
        print(f"  [x] Thu vien llama-cpp-python loi import: {e}")
        return False
        
    gguf_files = list(MODELS_DIR.glob("*.gguf"))
    if not gguf_files:
        print("  [!] Chua co file model .gguf nao trong thu muc models/")
        print("     -> Ban chi can chay lệnh: python download_model.py de tai model tu dong.")
        return True
        
    target_model = gguf_files[0]
    print(f"  [*] Dang thu load model: {target_model.name}...")
    try:
        llm = Llama(model_path=str(target_model), n_ctx=1024, n_gpu_layers=0, verbose=False)
        out = llm("Hello!", max_tokens=5)
        print("  [+] Load model va suy luan thanh cong!")
        return True
    except Exception as e:
        print(f"  [x] Loi khi khoi tao model: {e}")
        return False

def main():
    print("=" * 60)
    print("KIEM TRA MOI TRUONG THUC THI SINE (GIAI DOAN 2)")
    print("Thu muc lam viec: SINE_Project")
    print("=" * 60)
    
    c1 = test_inklecate()
    c2 = test_seeds()
    c3 = test_llm_inference()
    
    print("=" * 60)
    if c1 and c2 and c3:
        print(">>> MOI TRUONG PYTHON, INKLECATE, SEEDS VA LLM DA SAN SANG 100%! <<<")
    else:
        print("Vui long kiem tra lai cac muc danh dau [x] o tren.")
    print("=" * 60)

if __name__ == "__main__":
    main()
