# Kiến trúc Hệ thống SINE

Tài liệu này mô tả chi tiết kiến trúc phần mềm và luồng hoạt động của hệ thống SINE (Serious Interactive Narrative Engine).

## 1. Tổng quan Kiến trúc (High-Level Architecture)

Hệ thống SINE hoạt động dựa trên một Pipeline 3 bước tự động hoàn toàn:
1. **Extraction (Trích xuất):** Chuyển đổi dữ liệu thô (PDF/Docx) thành cấu trúc JSON chuẩn (Structured Seed).
2. **Generation (Sáng tác & Lập trình):** Sử dụng LLM (Large Language Model) để viết cốt truyện và lập trình logic game bằng ngôn ngữ Ink.
3. **Validation & Packaging (Kiểm thử & Đóng gói):** Kiểm tra mã nguồn sinh ra, sửa lỗi tự động nếu cần (thông qua Fixer Agent), tải tài nguyên ảnh và đóng gói thành Web Player.

---

## 2. Sơ đồ Luồng Dữ liệu (Data Flow Diagram)

```mermaid
flowchart TD
    A[Giáo viên nạp file PDF/Word] --> B(Document Extractor)
    B -->|PyMuPDF / pdfplumber| C{Có văn bản không?}
    C -- Có --> D[Gemini LLM]
    C -- Không / Chứa ảnh --> E[Gemini Vision LLM]
    
    D --> F[(Seed JSON: Tối đa 10 câu)]
    E --> F
    
    F --> G(Generator Agent - Qwen/Gemini)
    G -->|Tư duy & Viết kịch bản| H[File .ink nháp]
    
    H --> I(Validator)
    I -->|Biên dịch inklecate| J{Compilation (C)}
    J -- Lỗi --> K(Fixer Agent)
    J -- Đạt --> L{Playability (P) - BFS}
    L -- Lỗi --> K
    L -- Đạt --> M{Fidelity (Q) - Text Matching}
    M -- Lỗi --> K
    
    K --> H
    
    M -- Đạt --> N[File .ink Hoàn chỉnh]
    
    N --> O(Packaging Module)
    O -->|Tìm từ khóa & Tải ảnh Wiki/Picsum| P[Thư mục /images]
    O -->|Biên dịch ra JSON| Q[story.json]
    O -->|Tích hợp ink.js| R[index.html & UI]
    
    P --> S((Game Web Hoàn Chỉnh))
    Q --> S
    R --> S
```

---

## 3. Chi tiết các Thành phần Cốt lõi (Core Components)

### 3.1. Document Extractor (`extract_seed_from_doc.py`)
- Làm nhiệm vụ OCR và Parsing tài liệu.
- Xử lý vấn đề độ phân giải và mã hóa phông chữ bị hỏng của tài liệu Việt Nam bằng cách kết hợp thư viện đọc text truyền thống và mô hình AI đa phương thức (Vision LLM).
- **Hard Limit:** Tự động cắt giảm số lượng câu hỏi xuống 10 (chọn ngẫu nhiên/cắt đầu) để đảm bảo Context Window của AI Generator không bị quá tải.

### 3.2. SINE Agents (`src/agents.py`)
- **Generator Agent:** Đóng vai trò là người viết kịch bản. Sử dụng phương pháp *Reasoning Required* (`<think>` block) bắt buộc LLM phải lập kế hoạch cho câu chuyện trước khi viết code.
- **Fixer Agent:** Nếu mã nguồn bị lỗi, Fixer Agent nhận được thông báo lỗi chính xác từ Validator và tiến hành sửa chữa cục bộ mã nguồn. Quá trình này được giới hạn tối đa 3 vòng lặp (Max Retries) để tránh vòng lặp vô hạn.

### 3.3. Validator (`src/validator.py`)
Kiểm tra kịch bản thông qua 3 tiêu chuẩn tối thượng:
1. **Compilation (C):** Gọi subprocess chạy `inklecate.exe`. Nếu có lỗi cú pháp, trả về Error Log.
2. **Playability (P):** Trình diễn thuật toán Breadth-First Search (BFS) duyệt qua cây quyết định của game để đảm bảo luôn tồn tại ít nhất 1 đường dẫn đi tới node `-> END`.
3. **Fidelity (Q):** Đối chiếu chuỗi văn bản (String Matching). Khử các ký tự đặc biệt, chuẩn hoá dấu cách và kiểm tra xem 100% nội dung câu hỏi/đáp án từ tệp Seed có nằm trong mã nguồn Ink hay không.

### 3.4. Giao diện & Đóng gói (`sine_gui.py`)
- Sử dụng **Tkinter** cho giao diện nhẹ, tích hợp sẵn vào Python standard library không cần cài thêm framework nặng.
- **Image Fallback Mechanism:** Thay vì phụ thuộc vào API vẽ ảnh AI tốn phí (Pollinations), hệ thống áp dụng chiến lược:
  1. Trích xuất Keyword từ prompt của AI (vd: "battlefield").
  2. Truy vấn Wikipedia API (Hoàn toàn miễn phí, không giới hạn gắt gao) để tìm ảnh minh họa thực tế.
  3. Nếu không có kết quả, Fallback về ảnh phong cảnh ngẫu nhiên (Picsum Photos).

---

## 4. Các Quyết định Thiết kế Kỹ thuật (Design Decisions)

1. **Sử dụng Dấu `+` thay vì `*` trong Ink:**
   Ngôn ngữ Ink quy định dẫu `*` là lựa chọn một lần (chọn xong sẽ biến mất mãi mãi). Điều này khiến game IF-SG bị "kẹt" (dead-end) nếu học sinh trả lời sai và phải quay lại knot đó. SINE bắt buộc LLM phải sử dụng dấu `+` (sticky choice) để đảm bảo Playability.
2. **Escaping Công thức Toán học (LaTeX):**
   Trong Ink, cặp ngoặc nhọn `{}` là ký hiệu của biến và logic. Tuy nhiên, công thức Toán (vd: `\frac{1}{2}`) dùng rất nhiều ngoặc nhọn. Hệ thống SINE có một quy tắc ngầm ép AI phải escape các dấu này thành `\{` và `\}`. Sau đó, hàm `normalize_text` trong Validator sẽ parse ngược lại để kiểm tra Fidelity mà không bị sai lệch.
3. **Tách biệt Logic và Giao diện (Decoupling):**
   Mã nguồn sinh ra (`.ink`) hoàn toàn không chứa mã HTML/CSS. Việc parse file Ink thành Giao diện Web đẹp mắt do `ink.js` và `sine_gui.py` đảm nhiệm. Điều này tuân thủ kiến trúc MVC (Model-View-Controller).
