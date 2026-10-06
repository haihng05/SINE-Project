# BÁO CÁO NGHIÊN CỨU KHOA HỌC CHUẨN IEEE: HỆ THỐNG SINE-VN

**Đề tài:** Tự Động Hóa Sinh và Đánh Giá Trò Chơi Giáo Dục Tương Tác Văn Bản Tiếng Việt Quy Mô Lớn Sử Dụng Mô Hình Ngôn Ngữ Lớn và Ngôn Ngữ Kịch Bản Ink  
**Tác giả:** Nguyễn Hoàng Hải, Đỗ Ngọc Thiện  
**Đơn vị:** Khoa Công nghệ Đa phương tiện, Học viện Công nghệ Bưu chính Viễn thông (PTIT)  
**Email:** nghoanghaihn@gmail.com, dongocthien1411@gmail.com  
**Định dạng:** IEEE Conference Proceedings (2 cột, chuẩn bài báo nghiên cứu khoa học từ 4 đến 6 trang)

---

## TÓM TẮT (ABSTRACT)
Thiết kế trò chơi giáo dục (Educational Serious Games) phục vụ giáo dục thường đòi hỏi chi phí sản xuất cao và kỹ năng lập trình chuyên sâu, tạo nên rào cản kỹ thuật đáng kể đối với phần lớn giáo viên và các nhà sư phạm. Nghiên cứu này trình bày việc bản địa hóa, mở rộng và hoàn thiện hệ thống **SINE-VN (Serious Interactive Narrative Engine for Vietnamese)**, tự động hóa hoàn toàn quy trình chuyển đổi các bộ đề thi trắc nghiệm tĩnh quy mô lớn (lên tới 40–50 câu hỏi) sang các trò chơi giáo dục tương tác văn bản (Interactive Fiction Serious Games - IF-SG) bằng Tiếng Việt. Hệ thống tích hợp mô hình ngôn ngữ lớn nguồn mở họ Qwen 2.5 cùng ngôn ngữ kịch bản chuyên dụng Ink. 

Nghiên cứu đóng góp bốn giải pháp kỹ thuật cốt lõi:
1. **Kiến trúc Đa Hồi Ghép Nối Tất Định (Multi-Stage Stitched Architecture):** Tự động phân đoạn đề thi quy mô lớn ($>12$ câu hỏi) thành các hồi liên tiếp, sinh mã có kiểm soát ngữ cảnh và ghép nối tất định, triệt tiêu hoàn toàn lỗi tràn bộ đệm token và suy thoái ngữ cảnh của LLM.
2. **Cơ chế Khử Trùng lặp Không gian tên và Tự lành Cú pháp (`deduplicate_knots`):** Tự động loại bỏ xung đột định danh phân cảnh trùng lặp giữa các hồi và chuẩn hóa ngoặc vuông lựa chọn (`+ [Option] ->`) ngăn ngừa lỗi đóng băng giao diện Web (Black Screen Freeze).
3. **Cải tiến Đột phá Cú pháp Sticky Choice (`+`):** Triệt tiêu hoàn toàn lỗ hổng cạn kiệt nhánh trạng thái (Choice Exhaustion) trong ngôn ngữ Ink, bảo đảm 100% tính chơi được ($P=1$) cho chu trình tự sửa lỗi sư phạm.
4. **Bộ Trích xuất Đề thi Đa Thể thức Chuyên sâu:** Tự động hóa Microsoft Word COM, bảo toàn nguyên vẹn công thức MathType/OMML, chỉ số hóa học ($Al_2(SO_4)_3$), ký hiệu vật lý, các lượt thoại trong đề Tiếng Anh và tự sửa lỗi JSON lồng nhau.

Thực nghiệm toàn diện trên 5 môn thi chuẩn Kỳ thi Tốt nghiệp THPT Quốc gia 2023 (Toán học, Hóa học 40 câu, Vật lý 40 câu, Tiếng Anh 50 câu, Địa lý 24 câu) chứng minh hệ thống đạt tỷ lệ biên dịch cú pháp ($C$), khả năng chơi toàn vẹn ($P$) và độ trung thực học thuật ($Q$) tuyệt đối 100% ($S = C \cdot P \cdot Q = 1$), mở ra bước đột phá cho ứng dụng AI tạo sinh vào EdTech tại Việt Nam.

**Từ khóa:** *Trò chơi giáo dục, Kịch bản tương tác văn bản, Mô hình ngôn ngữ lớn, Hệ thống SINE-VN, Ngôn ngữ kịch bản Ink, Kiến trúc đa hồi ghép nối, Công nghệ giáo dục.*

---

## I. GIỚI THIỆU (INTRODUCTION)
Trò chơi giáo dục (Serious Games) đóng vai trò là công cụ đột phá thúc đẩy chuyển đổi số và nâng cao chất lượng giáo dục hiện đại [1]. Khác với các trò chơi giải trí thuần túy, trò chơi giáo dục tích hợp chặt chẽ các mục tiêu sư phạm vào cơ chế tương tác, tạo nên môi trường học tập kích thích sự tò mò, khám phá và tăng cường phản hồi nhận thức theo thời gian thực [2]. Nhiều nghiên cứu thực nghiệm đã chứng minh rằng hình thức học tập dựa trên trò chơi (Game-Based Learning) giúp gia tăng đáng kể mức độ gắn kết của học sinh, cải thiện khả năng ghi nhớ thông tin dài hạn và nuôi dưỡng tư duy giải quyết vấn đề độc lập [3].

Tuy nhiên, việc triển khai trò chơi giáo dục trên diện rộng trong nhà trường vẫn vấp phải rào cản kỹ thuật nghiêm trọng: **"Nút thắt cổ chai tác giả" (Authoring Bottleneck)** [3]. Giáo viên thường thiếu kỹ năng lập trình và thiết kế trò chơi phức tạp. Quy trình sản xuất truyền thống đòi hỏi phối hợp liên ngành kéo dài hàng tháng với chi phí tài chính vượt quá khả năng của đa số cơ sở giáo dục.

Sự bùng nổ của Trí tuệ Nhân tạo Tạo sinh (Generative AI), tiêu biểu là các Mô hình Ngôn ngữ Lớn (LLMs), đã mở ra triển vọng tự động hóa quy trình thiết kế nội dung trò chơi [4]. Tuy nhiên, các công trình đi trước như STORY2GAME [5], GENEVA [10] và ngay cả khung SINE nguyên bản của Rogosch và Schrader (2026) [1] đều chỉ dừng lại ở các bài kiểm tra vi mô (2 đến 5 câu hỏi, tối đa 10 câu). Khi ứng dụng vào các bộ đề thi thực tế chuẩn quốc gia (40 đến 50 câu), hệ thống đối mặt với 4 thách thức kỹ thuật nghiêm trọng:
1. **Tràn bộ đệm token (Max Output Token Ceiling):** Kịch bản 40–50 câu đòi hỏi 600–800+ dòng mã Ink. LLM sinh đơn khối tất yếu bị ngắt ngang ở câu 35–43, sinh mã dang dở gây sập biên dịch.
2. **Xung đột không gian tên phân cảnh (Namespace Collisions):** Khi ghép nối các hồi kịch bản, các nút thắt chuyển tiếp lặp lại (ví dụ `=== act_2_start ===`) khiến trình biên dịch Ink báo lỗi dừng tiến trình (*Duplicate flow error*).
3. **Cạn kiệt nhánh trạng thái (Choice Exhaustion):** Sử dụng toán tử tiêu hao (`*`) khiến lựa chọn bị hủy sau khi bấm sai, biến phân cảnh thành ngõ cụt khi học sinh thử lại nhiều lần ($P = 0$).
4. **Mất mát ký hiệu chuyên ngành và lỗi typographic:** Công thức MathType/OMML, chỉ số hóa học ($Al_2(SO_4)_3$), ký hiệu Hy Lạp, dấu typographic thông minh (`“`, `”`, `’`, `—`) và hội thoại hai nhân vật trong đề ngoại ngữ bị cắt xén hoặc gây lỗi phân tích cú pháp JSON.

Hệ thống SINE-VN được nghiên cứu nhằm giải quyết trọn vẹn các bài toán trên, đưa năng lực tự động hóa sinh trò chơi giáo dục lên quy mô đề thi quốc gia 50 câu hỏi.

---

## II. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN NGHIÊN CỨU
### A. Trò chơi Tương tác Văn bản Giáo dục (IF-SG) và Ngôn ngữ Ink
Trò chơi tương tác văn bản (Interactive Fiction - IF) mô tả thế giới ảo bằng ngôn ngữ tự nhiên và tương tác qua các lựa chọn phân nhánh [6]. Trong nghiên cứu về AI và giáo dục, thể loại IF loại bỏ sự phức tạp của cơ chế vật lý 3D để tập trung tối đa vào cấu trúc dẫn dắt câu chuyện và kiểm tra nhận thức [1].

Ngôn ngữ kịch bản Ink của Inkle Studios [7] là chuẩn công nghiệp với cấu trúc nhẹ gồm:
- **Knots:** Khối phân cảnh câu chuyện (`=== knot_name ===`).
- **Diverts:** Lệnh chuyển hướng trạng thái (`-> target_knot`).
- **Choices:** Nhánh tương tác, gồm toán tử tiêu hao `*` (chỉ chọn được một lần) và toán tử vĩnh viễn `+` (hiển thị lại trong mỗi lượt quay lại).

### B. Ứng dụng LLM trong Thiết kế Trò chơi
Gallotta et al. (2024) [4] đã tổng hợp lộ trình ứng dụng LLM trong trò chơi. Zhou et al. (2025) phát triển STORY2GAME [5] nhưng chỉ hướng đến phiêu lưu giải trí mở. Tanaka và Simo-Serra (2024) [8] áp dụng ngữ pháp GBNF cho hệ thống Ludii nhưng không đảm bảo tính toàn vẹn logic. Các nghiên cứu của Leandro et al. (2024) [10] và Farrell & Ware (2025) [15] chỉ ra rằng khi kịch bản vượt quá 10 bước, đồ thị của LLM có xu hướng gãy vụn.

### C. Khung SINE Nguyên bản và Khoảng trống Kỹ thuật
Khung SINE của Rogosch & Schrader (2026) [1] đặt nền móng đánh giá tự động ($C \cdot P \cdot Q$) và tác tử sửa lỗi. Tuy nhiên, SINE chỉ hoạt động với tiếng Anh, quy mô 2–5 câu hỏi, phụ thuộc vào toán tử tiêu hao `*`, không có cơ chế chia nhỏ đa hồi và không hỗ trợ nạp đề thi trực tiếp từ tài liệu Word/PDF thực tế.

---

## III. KIẾN TRÚC HỆ THỐNG SINE-VN ĐỀ XUẤT
Hệ thống được tổ chức thành quy trình ống nước (pipeline) tự động khép kín gồm 5 thành phần liên kết chặt chẽ:

```
[Đề thi Word / PDF] 
         │
         ▼ (Mô-đun Trích xuất COM / MathType / JSON-Repair)
[Tệp Dữ liệu Hạt giống JSON] 
         │
         ▼ (Dynamic Chunking > 12 câu -> Phân đoạn Màn)
[Tác tử Generator Agent (Qwen 2.5)] 
         │
         ▼ (Ghép nối Tất định & Deduplicate Knots)
[Kịch bản Ink Đa Hồi Hoàn Chỉnh] 
         │
         ▼ (Bộ Xác thực Định lượng S = C · P · Q)
   ┌─────┴────────────────────────┐
   ▼                              ▼
(S = 1: Thành công)        (S = 0: Lỗi)
   │                              │
   ▼                              ▼
[Đóng gói Web HTML5 / inkjs]  [Tác tử Fixer Agent (Tối đa 3 lượt)]
```

### A. Mô-đun Trích xuất Đề thi Đa Thể thức (Exam Ingestion)
Mô-đun tiếp nhận tài liệu Word (`.docx`) hoặc PDF. Với tài liệu Word, hệ thống tận dụng `win32com.client` và XML parser trích xuất cấu trúc OMML/MathType sang chuỗi văn bản, giữ nguyên vẹn chỉ số dưới, chỉ số trên và phương trình hóa học. Với đề thi Tiếng Anh có câu hỏi hội thoại nhiều lượt đối thoại (David & Mark), bộ phân tích bảo tồn 100% lời thoại của cả hai người nói, kết hợp thư viện `json-repair` tự động vá các ký tự ngoặc kép chưa escape.

### B. Dữ liệu Hạt giống Cấu trúc (Structured Seed)
Dữ liệu mầm JSON lưu trữ thông tin sư phạm bất biến:
- `locations`: Không gian bối cảnh nhập vai.
- `tasks`: Danh sách các câu hỏi trắc nghiệm tuần tự (gồm `stem`, mảng 4 `options`, và `correct`).

### C. Tác tử Sinh Kịch bản Đa Hồi Ghép Nối (Multi-Stage Stitched Generator Agent)
Khi số câu hỏi $N > 12$, hệ thống kích hoạt cơ chế phân hoạch đề thi thành $M = \lceil N / 10 \rceil$ hồi. Tác tử sinh từng hồi với ràng buộc:
- Hồi 1 ($k=1$): Bắt đầu từ `start_knot`, xử lý các câu 1–10, kết thúc bằng `-> act_2_start`.
- Hồi $k$ trung gian: Bắt đầu từ `=== act_k_start ===`, xử lý câu thuộc Hồi $k$, kết thúc bằng `-> act_(k+1)_start`.
- Hồi cuối ($k=M$): Bắt đầu từ `=== act_M_start ===`, kết thúc bằng `-> END`.
Bộ ghép nối `stitch_and_route_multistage_ink` tiến hành hợp nhất các đoạn mã, bảo đảm đồ thị liên thông từ đầu đến cuối.

### D. Bộ Xác thực Định lượng Tất định (Deterministic Validator)
Chất lượng kịch bản được đánh giá qua hàm mục tiêu:
$$S = C \cdot P \cdot Q, \quad C, P, Q \in \{0, 1\}$$
- **Biên dịch ($C$):** Biên dịch qua `inklecate.exe -j`, $C = 1$ khi mã thoát bằng 0.
- **Tính chơi được ($P$):** Thuật toán BFS kiểm tra tính liên thông trên đồ thị có hướng $G = (V, E)$:
  $$P = 1 \iff \exists \text{ đường đi } (v_0 \rightsquigarrow v_{\text{END}}) \text{ trong } G$$
- **Độ trung thực học thuật ($Q$):** Chuẩn hóa Unicode NFC, đồng nhất hóa ký tự typographic:
  $$Q = 1 \iff \forall t \in \text{Tasks}, \, (t.\text{stem} \subseteq \text{Script} \wedge \forall o \in t.\text{options}, \, o \subseteq \text{Script})$$

### E. Tác tử Fixer và Cơ chế Tự lành Cú pháp (`deduplicate_knots`)
Bộ tự lành tự động loại bỏ các khai báo Knot trùng lặp giữa các hồi và chuẩn hóa ngoặc vuông cho lựa chọn. Nếu vẫn còn lỗi ngữ nghĩa hoặc cú pháp, Fixer Agent nhận nhật ký lỗi và sửa đổi cục bộ trong tối đa 3 vòng lặp.

---

## IV. CÁC CẢI TIẾN KỸ THUẬT CỐT LÕI
### 1. Khắc phục Lỗi Cạn kiệt Nhánh bằng Sticky Choice (`+`)
Sử dụng toán tử tiêu hao `*` khiến các phương án sai biến mất sau mỗi lần người học bấm chọn, dẫn tới ngõ cụt khi thử lại nhiều lần ($P = 0$). Chuẩn hóa sang toán tử vĩnh viễn `+` bảo đảm toàn bộ phương án được hiển thị lại, thiết lập chu trình tự sửa lỗi sư phạm khép kín và bền vững ($P = 1$).

### 2. Kiến trúc Đa Hồi Ghép Nối Tất Định (Multi-Stage Stitched Architecture)
Đề thi 40–50 câu được phân hoạch toán học thành các tập con:
$$\mathcal{T} = \bigcup_{k=1}^M \mathcal{T}_k, \quad |\mathcal{T}_k| \le 10$$
Mỗi phân đoạn sinh mã Ink có độ dài vừa phải (120–160 dòng), hoàn toàn nằm trong bộ đệm an toàn của LLM, triệt tiêu nguy cơ cạn kiệt token hay đứt gãy cấu trúc.

### 3. Thuật toán Khử Xung đột Không gian tên (`deduplicate_knots`)
Giải quyết lỗi biên dịch nghiêm trọng của Inklecate (*Story already contains flow named act_k_start*) bằng cách phân tích AST, lưu vết bảng băm các knot đã định nghĩa và loại bỏ các header trùng lặp giữa các hồi ghép nối.

### 4. Chuẩn hóa Ngoặc Vuông Lựa chọn và Chống Treo Giao diện Web
Ép toàn bộ phương án về dạng `+ [Option text] -> destination` giúp tách rời văn bản hiển thị trên nút bấm khỏi văn bản phản hồi, ngăn ngừa triệt để lỗi màn hình đen (Black Screen UI Freeze) trên nền tảng Web `inkjs`.

### 5. Xử lý Ký tự STEM và Typographic
Tự động escape dấu ngoặc nhọn LaTeX `\{` và `\}` cho môn Toán học. Đồng nhất hóa dấu ngoặc kép cong (`“`, `”`), dấu lược (`’`), dấu gạch ngang (`—`) và khoảng trống điền từ (`____`) trong môn Tiếng Anh và Khoa học Xã hội.

---

## V. THỰC NGHIỆM VÀ KẾT QUẢ ĐÁNH GIÁ
### A. Thiết lập Môi trường và Tập Dữ liệu
- **Phần cứng:** Intel Core i7-13700H, 16 GB DDR5 RAM, NVIDIA RTX 4060 GPU, Windows 11 64-bit.
- **Mô hình LLM:** Qwen 2.5 7B Instruct (GGUF Q4_K_M chạy offline qua `llama-cpp-python`) và Qwen 2.5 14B.
- **Tập dữ liệu:** 5 môn thi chuẩn Kỳ thi Tốt nghiệp THPT Quốc gia 2023 chính thức của Bộ GD&ĐT:
  1. Hóa học 2023 (40 câu, phương trình hóa học, chất hữu cơ, vô cơ).
  2. Vật lý 2023 (40 câu, mật độ công thức MathType dày đặc, sóng cơ, dao động).
  3. Tiếng Anh 2023 (50 câu, ngữ âm, đối thoại xã hội 2 nhân vật, bài đọc hiểu).
  4. Địa lý 2023 (24 câu, tự nhiên, kinh tế xã hội, tra cứu Atlat).
  5. Toán học THPT (5 câu, công thức LaTeX phức tạp).

### B. Kết quả Đánh giá Định lượng Toàn diện

| Bộ Đề Thi | Số Câu | C (%) | P (%) | Q (%) | S (%) | Lượt Sửa | Thời Gian (s) | Trạng Thái |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Toán học (LaTeX)** | 5 | 100% | 100% | 100% | **100%** | 1.2 | 118 s | Xuất sắc |
| **Địa lý 2023 (3 Màn)** | 24 | 100% | 100% | 100% | **100%** | 1.0 | 210 s | Hoàn hảo |
| **Hóa học 2023 (4 Màn)** | 40 | 100% | 100% | 100% | **100%** | 1.0 | 380 s | Hoàn hảo |
| **Vật lý 2023 (4 Màn)** | 40 | 100% | 100% | 100% | **100%** | 1.0 | 538 s | Hoàn hảo |
| **Tiếng Anh 2023 (5 Màn)** | 50 | 100% | 100% | 100% | **100%** | 1.0 | 373 s | Hoàn hảo |
| *Cơ sở (Đơn khối + Dấu \*)* | 40--50 | 0.0% | 0.0% | 0.0% | **0.0%** | Hết lượt | Tràn token | Sụp đổ |

### C. Phân tích Cấu trúc Không gian Trò chơi Quy mô Lớn

| Môn Học | Số Knots ($K$) | Số Lựa Chọn ($E$) | Mật Độ Phân Nhánh ($\delta$) | Dòng Mã Ink | Tổng Số Từ ($W$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Toán học** | 16 knots | 25 choices | 1.56 | 120 dòng | 810 từ |
| **Địa lý** | 73 knots | 121 choices | 1.66 | 364 dòng | 3.184 từ |
| **Hóa học** | 124 knots | 200 choices | 1.61 | 637 dòng | 3.209 từ |
| **Vật lý** | 125 knots | 194 choices | 1.55 | 623 dòng | 4.496 từ |
| **Tiếng Anh** | 155 knots | 250 choices | 1.61 | 787 dòng | 4.650 từ |

### D. Thảo luận Kết quả
1. **Phá vỡ giới hạn độ dài:** Hệ thống xử lý mượt mà đề thi 50 câu Tiếng Anh với gần 800 dòng mã Ink và 155 phân cảnh, trong khi mô hình đơn khối luôn sụp đổ ở câu 35–43.
2. **Hiệu quả của bộ tự lành:** Nhờ `deduplicate_knots` và chuẩn hóa ngoặc vuông, 100% các môn thi 40–50 câu đều đạt $S=1$ ngay từ lượt đầu tiên ($I = 1.0$) mà không phải gọi thêm vòng lặp sửa lỗi tốn kém.
3. **Độ trung thực học thuật tuyệt đối ($Q = 100\%$):** 100% các câu hỏi và phương án được bảo tồn nguyên văn, triệt tiêu hoàn toàn rủi ro ảo giác trong giáo dục.

---

## VI. BÀN LUẬN VÀ Ý NGHĨA THỰC TIỄN
- **Thiết kế Zero-code cho Giáo viên:** Giáo viên chỉ cần đưa tệp Word có sẵn, hệ thống tự động xuất bản game Web hoàn chỉnh trong vòng 4–8 phút.
- **Triển khai Offline tiết kiệm và bảo mật:** Việc chạy trực tiếp trên mô hình nguồn mở lượng tử hóa 7B/14B giúp nhà trường triển khai miễn phí, độc lập, bảo mật dữ liệu học đường tuyệt đối.
- **Khả năng mở rộng quy mô:** Mô hình Đa Hồi Ghép Nối chứng minh LLM hoàn toàn có thể làm chủ các cấu trúc kịch bản phức tạp lên tới hàng trăm nút thắt nếu được kết hợp với bộ định tuyến đồ thị tất định.
- **Hạn chế:** Hệ thống hiện chưa tự động bóc tách và nhúng hình vẽ đồ thị từ đề thi Word vào game Web, sẽ được hoàn thiện trong các nghiên cứu tiếp theo.

---

## VII. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
Nghiên cứu đã phát triển thành công hệ thống SINE-VN, giải quyết triệt để bài toán tự động hóa sinh và đánh giá trò chơi giáo dục tương tác văn bản quy mô lớn (40–50 câu hỏi) bằng Tiếng Việt. Với bốn giải pháp đột phá: Kiến trúc Đa Hồi Ghép Nối Tất Định, Bộ Tự lành Cú pháp Khử Xung đột Không gian Tên, Cải tiến Toán tử Sticky Choice (`+`), và Động cơ Trích xuất Đề thi Chuyên sâu Đa thể thức, hệ thống đạt tỷ lệ thành công 100% trên 5 môn thi Tốt nghiệp THPT Quốc gia 2023.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
[1] F. Rogosch and A. Schrader, "Automated Generation and Evaluation of Interactive-Fiction Serious Games with Open-Weight LLMs," *Applied Sciences*, vol. 16, no. 6, p. 2932, 2026. [Online]. Available: [https://doi.org/10.3390/app16062932](https://doi.org/10.3390/app16062932)  
[2] T. M. Connolly, E. A. Boyle, E. MacArthur, T. Hainey, and J. M. Boyle, "A systematic literature review of empirical evidence on computer games and serious games," *Computers & Education*, vol. 59, no. 2, pp. 661–686, 2012. [Online]. Available: [https://doi.org/10.1016/j.compedu.2012.03.004](https://doi.org/10.1016/j.compedu.2012.03.004)  
[3] F. Horn and S. Göbel, "AI as a Co-creator: A Survey on AI Support for Educational Game Authoring Tools," in *Proc. Joint Int. Conf. on Serious Games (JCSG)*, LNCS, vol. 15259, Springer, pp. 3–18, 2025. [Online]. Available: [https://doi.org/10.1007/978-3-031-73602-5_1](https://doi.org/10.1007/978-3-031-73602-5_1)  
[4] R. Gallotta, G. Todd, M. Zammit, S. Earle, A. Liapis, J. Togelius, and G. N. Yannakakis, "Large Language Models and Games: A Survey and Roadmap," *IEEE Trans. on Games*, vol. 16, pp. 1–18, 2024. [Online]. Available: [https://doi.org/10.1109/TG.2024.3407889](https://doi.org/10.1109/TG.2024.3407889)  
[5] E. Zhou, S. Basavatia, M. Siam, Z. Chen, and M. O. Riedl, "STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game," *arXiv:2505.03547*, 2025. [Online]. Available: [https://arxiv.org/abs/2505.03547](https://arxiv.org/abs/2505.03547)  
[6] M. O. Riedl and V. Bulitko, "Interactive Narrative: An Intelligent Systems Approach," *AI Magazine*, vol. 34, no. 1, pp. 67–77, 2013. [Online]. Available: [https://doi.org/10.1609/aimag.v34i1.2449](https://doi.org/10.1609/aimag.v34i1.2449)  
[7] Inkle Studios, "Ink: Inkle's Narrative Scripting Language," 2025. [Online]. Available: [https://www.inklestudios.com/ink/](https://www.inklestudios.com/ink/)  
[8] T. Tanaka and E. Simo-Serra, "Grammar-based Game Description Generation using Large Language Models," *IEEE Trans. on Games*, vol. 18, no. 1, pp. 30–43, 2024. [Online]. Available: [https://doi.org/10.1109/TG.2024.3421256](https://doi.org/10.1109/TG.2024.3421256)  
[9] S. Buongiorno, L. Klinkert, Z. Zhuang, T. Chawla, and C. Clark, "PANGeA: Procedural artificial narrative using generative AI for turn-based RPGs," in *Proc. AAAI AIIDE*, vol. 20, pp. 156–166, 2024. [Online]. Available: [https://doi.org/10.1609/aiide.v20i1.31835](https://doi.org/10.1609/aiide.v20i1.31835)  
[10] J. Leandro, S. Rao, M. Xu, W. Xu, N. Jojic, C. J. Brockett, and W. B. Dolan, "GENEVA: Generating and Visualizing branching narratives using LLMs," in *Proc. IEEE CoG*, pp. 1–5, 2024. [Online]. Available: [https://doi.org/10.1109/CoG60054.2024.10645601](https://doi.org/10.1109/CoG60054.2024.10645601)  
[11] Qwen Team, "Qwen2.5: A Party of Foundation Models," *arXiv:2412.15115*, 2024. [Online]. Available: [https://arxiv.org/abs/2412.15115](https://arxiv.org/abs/2412.15115)  
[12] S. Arnab et al., "Mapping learning and game mechanics for serious games analysis," *Br. J. Educ. Technol.*, vol. 46, no. 2, pp. 391–411, 2015. [Online]. Available: [https://doi.org/10.1111/bjet.12113](https://doi.org/10.1111/bjet.12113)  
[13] N. Szilas and I. Ilea, "Objective Metrics for Interactive Narrative," in *Interactive Storytelling*, LNCS, vol. 8832, Springer, pp. 91–102, 2014. [Online]. Available: [https://doi.org/10.1007/978-3-319-11997-7_9](https://doi.org/10.1007/978-3-319-11997-7_9)  
[14] Y. Sun et al., "Language as Reality: A Co-Creative Storytelling Game Experience in 1001 Nights Using Generative AI," in *Proc. AAAI AIIDE*, vol. 19, pp. 425–434, 2023. [Online]. Available: [https://doi.org/10.1609/aiide.v19i1.27539](https://doi.org/10.1609/aiide.v19i1.27539)  
[15] R. Farrell and S. G. Ware, "Large Language Models as Narrative Planning Search Guides," *IEEE Trans. on Games*, vol. 17, pp. 419–428, 2025. [Online]. Available: [https://doi.org/10.1109/TG.2024.3412589](https://doi.org/10.1109/TG.2024.3412589)
