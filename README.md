# SINE: Serious Interactive Narrative Engine

> **Dự án Nghiên cứu khoa học - Phát triển ứng dụng đa phương tiện**

Hệ thống SINE (Serious Interactive Narrative Engine) là một công cụ đột phá cho phép tự động hóa hoàn toàn quá trình chuyển đổi các đề thi/bài tập trắc nghiệm khô khan thành một tựa game tương tác nhập vai (Interactive Fiction Serious Games - IF-SG). Hệ thống sử dụng sức mạnh của các mô hình Ngôn ngữ Lớn (LLMs) và ngôn ngữ kịch bản Ink.

---

##  Các tính năng nổi bật

1. **Trích xuất Đề thi Thông minh (Document Extraction):**
   - Hỗ trợ đọc file PDF, Word (`.docx`).
   - Tích hợp AI Thị giác (Vision LLM) để tự động đọc và trích xuất dữ liệu kể cả khi đề thi là ảnh scan mờ hoặc chứa công thức toán học phức tạp.
2. **Sáng tác Game Tự động (AI Generation):**
   - Đóng vai một Game Designer, AI tự động sáng tạo bối cảnh, cốt truyện, và lồng ghép các câu hỏi trắc nghiệm vào từng thử thách trong game.
   - Sử dụng tư duy phân tích `<think>` để đảm bảo tính logic và liền mạch.
3. **Cơ chế Đánh giá Tự động (CPQ Validation):**
   - **Compilation (C):** Đảm bảo mã nguồn Ink biên dịch thành công 100%.
   - **Playability (P):** Đảm bảo trò chơi không bị kẹt (dead-end) và người chơi luôn có thể chơi đến phá đảo.
   - **Fidelity (Q):** Đảm bảo 100% nội dung câu hỏi và đáp án gốc của giáo viên không bị AI xuyên tạc hay rút gọn.
4. **Minh họa Trực quan (Visual Illustration):**
   - Tự động trích xuất từ khóa bối cảnh và tải ảnh minh họa tương ứng từ Wikipedia hoặc ảnh phong cảnh chất lượng cao.
5. **Giao diện Trực quan & Đóng gói Web Player:**
   - Cung cấp phần mềm giao diện (GUI) thân thiện cho giáo viên (không cần biết code).
   - Tự động xuất ra một thư mục Game hoàn chỉnh chạy trực tiếp trên trình duyệt Web.

---

##  Cấu trúc thư mục

```text
SINE-Project/
├── Game_Export/             # Thư mục chứa các game đã được đóng gói ra Web (dành cho học sinh)
├── output/                  # Chứa kịch bản mã nguồn Ink được AI sinh ra
├── seeds/                   # Chứa dữ liệu câu hỏi (JSON) đã được trích xuất
├── src/                     # Mã nguồn cốt lõi của hệ thống
│   ├── agents.py            # AI Generator & Fixer Agents (Xử lý prompt, gọi API)
│   └── validator.py         # Module kiểm thử tự động (C, P, Q)
├── tools/                   # Chứa trình biên dịch inklecate.exe
├── extract_seed_from_doc.py # Script đọc PDF/Docx và trích xuất câu hỏi bằng AI
├── run_single_test.py       # Script chạy tự động hoá pipeline từ CLI
├── sine_gui.py              # Phần mềm giao diện (GUI) thân thiện dành cho giáo viên
└── requirements.txt         # Các thư viện Python cần thiết
```

---

##  Hướng dẫn Cài đặt

Yêu cầu hệ thống: Máy tính cài đặt **Python 3.10** hoặc **3.11**.

1. **Tạo môi trường ảo (Virtual Environment):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Cài đặt thư viện:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Cấu hình API Key:**
   - Hệ thống hiện đang sử dụng OpenRouter API và Google Gemini API. Đảm bảo bạn đã cấu hình các biến môi trường hoặc nhập Key trực tiếp vào mã nguồn tại `extract_seed_from_doc.py` và `src/agents.py`.

---

##  Hướng dẫn Sử dụng

### Dành cho Giáo viên (Sử dụng Giao diện 1-Click)
1. Chạy tệp giao diện:
   ```powershell
   python sine_gui.py
   ```
2. Giao diện phần mềm sẽ hiện ra. Bạn chỉ cần:
   - Nhập tên bài học (Ví dụ: `LsuDly6`).
   - Bấm **Chọn file PDF / Word** để nạp đề thi.
   - Bấm **Tự động tạo Game**.
3. Pha một tách cà phê và đợi khoảng 2-3 phút.
4. Mở thư mục `Game_Export/Game_LsuDly6` và chạy file `Choi_Game_Truc_Quan.bat` để trải nghiệm game trên trình duyệt!

### Dành cho Lập trình viên (Chạy bằng lệnh CLI)
1. Trích xuất câu hỏi từ file PDF:
   ```powershell
   python extract_seed_from_doc.py --doc path/to/file.pdf --topic my_topic
   ```
2. Sinh kịch bản và kiểm thử tự động:
   ```powershell
   python run_single_test.py --seed seed_my_topic.json
   ```
3. Test kịch bản trực tiếp trên terminal:
   ```powershell
   .\tools\inklecate.exe -p output\game_seed_my_topic.ink
   ```

---

##  Giới hạn hiện tại & Lưu ý
- Để tránh việc AI bị quá tải và "ảo giác" (hallucination) dẫn đến lỗi mã nguồn, hệ thống hiện đang được cài đặt **tự động cắt giảm và chọn lọc tối đa 10 câu hỏi** cho mỗi ván game. Đây là con số lý tưởng để cân bằng giữa sự ổn định của hệ thống và sự tập trung của học sinh.
- Các công thức toán học (`{`, `}`) đã được cấu hình tự động escape (`\{`, `\}`) để tương thích với trình biên dịch Ink.
