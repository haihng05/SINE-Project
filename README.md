# SINE: Serious Interactive Narrative Engine
> **Chuyên đề nghiên cứu khoa học - Phát triển ứng dụng đa phương tiện**  
> Thành viên: **Hải & Thiện**

Hệ thống tự động hóa sinh và đánh giá kịch bản trò chơi nghiêm túc dạng tương tác văn bản (Interactive Fiction Serious Games - IF-SG) từ kịch bản gốc (Structured Seeds) sử dụng các mô hình Open-Weight LLMs (Qwen 2.5) và ngôn ngữ kịch bản Ink.

---

## 📁 Cấu trúc thư mục dự án

```
SINE_Project/
├── models/                  # Nơi lưu trữ mô hình .gguf (chạy download_model.py để tải)
├── tools/                   # Trình biên dịch inklecate.exe
│   └── inklecate.exe
├── seeds/                   # Tập dữ liệu kịch bản gốc (JSON)
│   ├── seed_media_vi_01.json
│   ├── seed_media_01.json
│   └── seed_medicine_01.json
├── src/                     # Mã nguồn cốt lõi của pipeline
│   ├── agents.py            # Generator & Fixer Agent (LLM)
│   └── validator.py         # Bộ xác thực tự động (C, P, Q)
├── output/                  # Chứa kịch bản game sinh ra (.ink)
├── download_model.py        # Script tải model GGUF tự động
├── test_environment.py      # Script kiểm tra môi trường
├── run_single_test.py       # Script chạy thử nghiệm 1 kịch bản
└── requirements.txt         # Thư viện Python cần thiết
```

---

## 🚀 Hướng dẫn cài đặt nhanh (Dành cho thành viên nhóm)

### 1. Khởi tạo môi trường ảo Python (Python 3.11)
```powershell
# Tạo và kích hoạt venv
py -3.11 -m venv venv
.\venv\Scripts\activate

# Cài đặt thư viện phụ trợ
pip install -r requirements.txt

# Cài đặt llama-cpp-python (Bản Pre-built wheel cho CPU)
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

### 2. Tải mô hình LLM (Qwen 2.5 7B GGUF)
```powershell
python download_model.py
```

### 3. Kiểm tra môi trường
```powershell
python test_environment.py
```

---

## 🎮 Cách chạy sinh kịch bản và chơi thử game

### Sinh kịch bản game tự động:
```powershell
python run_single_test.py
```

### Chơi thử tương tác trực tiếp trên Terminal:
```powershell
.\tools\inklecate.exe -p output\game_seed_media_vi_01.ink
```
*(Dùng các phím số `1`, `2`, `3`... và `Enter` để chọn hành động).*

---

## 📊 Bộ tiêu chí đánh giá tự động ($S = C \cdot P \cdot Q$)
1. **Compilation ($C$):** Biên dịch cú pháp Ink qua `inklecate.exe` không lỗi.
2. **Playability ($P$):** Thuật toán BFS tìm được đường đi từ đầu tới kết thúc (`-> END`).
3. **Fidelity ($Q$):** Giữ nguyên 100% nội dung câu hỏi và các lựa chọn đáp án từ Seed.

---

## 💡 Lưu ý kỹ thuật nội bộ (Dành cho Team Dev)

### 1. Vấn đề "Cạn kiệt nhánh" (Choice Exhaustion) trong Ink
Trong quá trình thử nghiệm, hệ thống gặp lỗi người chơi trả lời sai 2 lần là game tự động văng (kết thúc đột ngột). Nguyên nhân là do cú pháp mặc định của ngôn ngữ Ink:
- Dấu `*`: Là lựa chọn dùng 1 lần (Fallback choice). Người chơi nhấn xong là nhánh đó tự động bị xóa vĩnh viễn khỏi game.
- Dấu `+`: Là lựa chọn vĩnh viễn (Sticky choice). Nhánh luôn tồn tại kể cả khi quay lại nhiều lần.

**Giải pháp đã áp dụng:** Trong file `src/agents.py`, toàn bộ **System Prompt** của Generator và Fixer đã được nâng cấp để bắt buộc AI chỉ sử dụng dấu `+` cho các câu hỏi và các nhánh `[Thử lại]`. Các thành viên **KHÔNG** thay đổi lại thành dấu `*` để tránh phá vỡ luồng đánh giá Playability ($P$).

### 2. Cấu trúc Prompting
Hệ thống hiện đang dùng chiến lược **Reasoning Required** (S3). AI bắt buộc phải viết dàn ý trong thẻ `<think>` trước khi xuất mã Ink. Khi tinh chỉnh Prompt, hãy cẩn thận không để lại các ký tự như `...` trong ví dụ mẫu vì các mô hình 7B rất dễ bắt chước (copy literal) dẫn tới bỏ sót nội dung câu hỏi (lỗi Fidelity $Q$).
