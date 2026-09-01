# Ứng Dụng Mô Hình Ngôn Ngữ Lớn Mã Nguồn Mở Trong Tự Động Hóa Sinh Kịch Bản Trò Chơi Giáo Dục Tương Tác Tiếng Việt

**Tác giả:** Hải, Thiện  
**Nghiên cứu Khoa học - Chuyên đề Phát triển Ứng dụng Đa phương tiện**  

---

## TÓM TẮT (ABSTRACT)
**Tóm tắt**—Việc thiết kế và phát triển các trò chơi giáo dục (Serious Games) thường đòi hỏi chi phí cao và kỹ năng lập trình chuyên sâu, tạo ra rào cản lớn đối với các nhà giáo dục. Nghiên cứu này trình bày việc ứng dụng, bản địa hóa và mở rộng khung hệ thống SINE (Serious Interactive Narrative Engine) nhằm tự động hóa hoàn toàn quy trình sinh kịch bản trò chơi tương tác văn bản (Interactive Fiction - IF) bằng Tiếng Việt. Sử dụng mô hình ngôn ngữ lớn nguồn mở Qwen 2.5 7B GGUF chạy trên phần cứng cá nhân, hệ thống cho phép sinh kịch bản game từ cấu trúc dữ liệu hạt giống (JSON Seeds) mà không cần can thiệp thủ công. Đặc biệt, nghiên cứu đề xuất giải pháp tinh chỉnh cú pháp lựa chọn vĩnh viễn (sticky choices) trong ngôn ngữ Ink, khắc phục triệt để lỗi cạn kiệt nhánh trạng thái (state exhaustion) khi người chơi trả lời sai nhiều lần. Hệ thống được đánh giá tự động dựa trên ba tiêu chí: Biên dịch (Compilation), Khả năng chơi (Playability) và Độ trung thực học thuật (Learning-Goal Fidelity), chứng minh tính khả thi cao trong việc áp dụng AI tạo sinh vào EdTech tại Việt Nam.

**Từ khóa**—Serious Games, Interactive Fiction, Large Language Models, SINE, Generative AI, Ink Script.

---

## I. MỞ ĐẦU (INTRODUCTION)
Các trò chơi giáo dục (Serious Games) đã được chứng minh là công cụ hiệu quả để tăng cường sự tham gia và cải thiện kết quả học tập của người học. Tuy nhiên, rào cản lớn nhất trong việc áp dụng rộng rãi phương pháp này là sự thiếu hụt kỹ năng thiết kế trò chơi (Game Design) và lập trình ở phần lớn các giáo viên [1]. Quá trình chuyển đổi từ mục tiêu sư phạm sang cơ chế trò chơi (game mechanics) thường tiêu tốn nhiều tháng phát triển bởi các studio chuyên nghiệp.

Với sự bùng nổ của Trí tuệ Nhân tạo Tạo sinh (Generative AI), đặc biệt là các Mô hình Ngôn ngữ Lớn (LLMs), cơ hội tự động hóa quy trình thiết kế game đang trở nên rõ ràng. Mặc dù vậy, các LLM hiện tại vẫn gặp hạn chế nghiêm trọng về tính ảo giác (hallucination), dẫn đến việc làm sai lệch nội dung giáo dục hoặc sinh ra mã nguồn không thể thực thi. 

Nghiên cứu này kế thừa khung lý thuyết SINE (Serious Interactive Narrative Engine) [2] và đóng góp ba điểm mới mang tính thực tiễn:
1. **Bản địa hóa (Localization):** Chuyển đổi và tối ưu hóa hệ thống để sinh kịch bản hoàn toàn bằng Tiếng Việt.
2. **Triển khai cục bộ (Local Deployment):** Thu gọn hệ thống để chạy trên mô hình Qwen 2.5 7B GGUF qua `llama-cpp-python`, phù hợp với phần cứng phổ thông.
3. **Cải tiến tính bền vững của vòng lặp (Robust Loop Fixing):** Đề xuất thay thế toán tử lựa chọn tiêu hao (`*`) bằng lựa chọn vĩnh viễn (`+`) trong Ink script để đảm bảo tính Playability trong các vòng lặp thất bại (failure loops).

---

## II. CƠ SỞ LÝ THUYẾT & NGHIÊN CỨU LIÊN QUAN
### A. Trò chơi Giáo dục Tương tác Văn bản (IF-SG)
Interactive Fiction (IF) là thể loại trò chơi phiêu lưu dựa trên văn bản, nơi người chơi tương tác với thế giới qua các lựa chọn rẽ nhánh. Định dạng này đặc biệt phù hợp cho LLMs vì toàn bộ không gian trạng thái có thể được biểu diễn bằng ngôn ngữ tự nhiên và các đoạn mã kịch bản (ví dụ: ngôn ngữ Ink của Inkle Studios).

### B. LLM trong Thiết kế Trò chơi
Nhiều nghiên cứu trước đây đã sử dụng ChatGPT để hỗ trợ lên ý tưởng hoặc sinh hội thoại NPC. Tuy nhiên, việc tạo ra một trò chơi có thể biên dịch (compilable) và giữ nguyên vẹn mục tiêu học thuật (learning goals) đòi hỏi một hệ thống phức tạp hơn chỉ là prompt thông thường. Các hệ thống đa tác tử (Multi-agent) kết hợp phản hồi xác thực tự động (Automated Validation) đang là hướng tiếp cận tiên tiến nhất.

---

## III. KIẾN TRÚC HỆ THỐNG ĐỀ XUẤT
Hệ thống SINE được triển khai theo quy trình ống nước (pipeline) tự động khép kín, bao gồm 4 thành phần cốt lõi:

### A. Dữ liệu Hạt giống (Structured Seeds)
Dữ liệu đầu vào được mô hình hóa dưới dạng JSON, chứa các thông tin bất biến (immutable context) gồm:
- **Locations**: Tập hợp các trạm/bối cảnh (Ví dụ: `Phòng Thu Âm Cũ`, `Phòng Dựng Phim`).
- **Tasks**: Các câu hỏi trắc nghiệm chuyên ngành (Ví dụ: Hệ màu RGB/CMYK, Tần số lấy mẫu), kèm danh sách lựa chọn và đáp án đúng.

### B. Tác tử Sinh kịch bản (Generator Agent)
Sử dụng phương pháp Kích thích Suy luận (Reasoning Required Prompting). Tác tử không sinh ngay mã Ink mà buộc phải lập kế hoạch cốt truyện trong thẻ `<think>`, sau đó mới ánh xạ dữ liệu mầm vào cấu trúc rẽ nhánh của Ink.

### C. Bộ Xác thực Tự động (Automated Validator)
Mỗi kịch bản sinh ra được đánh giá bằng hàm mục tiêu $S$:
$$S = C \cdot P \cdot Q$$
Trong đó:
- **C (Compilation):** Mã Ink không chứa lỗi cú pháp (kiểm tra qua `inklecate.exe`).
- **P (Playability):** Thuật toán Duyệt theo chiều rộng (BFS) tìm thấy ít nhất một đường đi hợp lệ từ Node bắt đầu đến Terminal Node (`-> END`).
- **Q (Learning-Goal Fidelity):** 100% văn bản của câu hỏi (stem) và lựa chọn (options) phải khớp hoàn toàn với dữ liệu Seed, không bị AI biến tấu.

### D. Tác tử Sửa lỗi (Fixer Agent)
Nếu $S = 0$, mã lỗi từ Validator được đưa vào Fixer Agent. Tác tử này có tối đa 3 vòng lặp (iterations) để đọc hiểu lỗi và đệ trình bản vá.

---

## IV. TRIỂN KHAI VÀ CẢI TIẾN THỰC NGHIỆM
### A. Thiết lập Môi trường
- **Mô hình:** Qwen 2.5 7B GGUF (chạy qua `llama-cpp-python` tối ưu hóa cho CPU/Consumer GPU).
- **Ngôn ngữ kịch bản:** Ink v1.2.0.
- **Tập dữ liệu:** Đề tài Đa phương tiện và Truyền thông (Tiếng Việt).

### B. Khắc phục Cấu trúc Vòng lặp Học tập (Learning Loop Fix)
Trong các nghiên cứu trước, việc dùng cú pháp `*` (standard choice) của Ink cho các lựa chọn đáp án dẫn đến hiện tượng **Tiêu hao lựa chọn (Choice Exhaustion)**. Khi người chơi trả lời sai n lần, các lựa chọn bị xóa khỏi cây đồ thị, khiến thuật toán đánh giá $P$ (Playability) thất bại do ngõ cụt (Dead-end).

**Đề xuất cải tiến:** Tinh chỉnh System Prompt ép buộc Tác tử sử dụng cú pháp `+` (sticky choice) cho mọi nút thắt nhiệm vụ học tập.
*Mã trước cải tiến (Gây ngõ cụt):*
```ink
* [Thử lại câu hỏi này] -> task_01_knot
```
*Mã sau cải tiến (Vòng lặp bền vững):*
```ink
+ [Thử lại câu hỏi này] -> task_01_knot
```
Cải tiến này triệt tiêu hoàn toàn lỗi "hết content" khi người chơi tương tác sai liên tục.

---

## V. ĐÁNH GIÁ VÀ THẢO LUẬN
### A. Ưu điểm và Khả năng Ứng dụng
Hệ thống thể hiện tính ưu việt rõ rệt trong bối cảnh EdTech Việt Nam:
- **Zero-code cho Nhà giáo dục:** Giáo viên chỉ cần soạn đề cương (JSON), hệ thống tự động hóa 100% công đoạn viết code và kịch bản hóa.
- **Chi phí cực thấp:** Việc sử dụng các mô hình nhỏ (7B) được lượng tử hóa (Quantized) cho phép triển khai cục bộ (Local), tiết kiệm chi phí gọi API đám mây (như GPT-4) và bảo mật dữ liệu học đường.
- **Khả năng Mở rộng:** Cấu trúc game có thể dễ dàng xuất ra Web qua thư viện `inkjs` để học sinh truy cập đa nền tảng.

### B. Hạn chế
- **Giới hạn Thể loại:** Hệ thống hiện chỉ hỗ trợ game thuần văn bản và tương tác dạng trắc nghiệm, chưa mở rộng cho các game có yếu tố vật lý (physics-based) hay không gian 2D/3D phức tạp.
- **Tính văn chương của AI:** Với các prompt phức tạp, đôi khi AI phân bổ hội thoại chưa mượt mà, cảm giác chuyển cảnh giữa các câu hỏi đôi chỗ còn cứng nhắc.

---

## VI. KẾT LUẬN
Nghiên cứu đã triển khai thành công khung hệ thống SINE tại Việt Nam, chứng minh khả năng của các mô hình Open-Weight LLM quy mô nhỏ gọn trong việc tự động sinh trò chơi giáo dục. Bằng việc kết hợp dữ liệu mầm có cấu trúc, chiến lược Prompt yêu cầu lập luận, và cơ chế xác thực khép kín, hệ thống giải quyết được bài toán ảo giác (hallucination) thường gặp của AI. Hướng phát triển trong tương lai bao gồm việc tích hợp AI sinh ảnh minh họa tĩnh theo từng bối cảnh và đưa sản phẩm thử nghiệm thực tế tại các trường học hoặc các đồ án môn học.

---

## TÀI LIỆU THAM KHẢO
[1] F. Rogosch and A. Schrader, "Automated Generation and Evaluation of Interactive-Fiction Serious Games with Open-Weight LLMs," *Applied Sciences*, vol. 16, no. 2932, 2026.  
[2] P. Ammanabrolu et al., "Bringing Stories Alive: Generating Interactive Fiction Worlds," in *Proc. AAAI Conf. Artif. Intell. Interact. Digit. Entertain.*, 2020.  
[3] Inkle Studios, "Ink - Inkle's Narrative Scripting Language." [Online]. Available: https://www.inklestudios.com/ink/  
[4] Qwen Team, "Qwen 2.5 Technical Report," arXiv preprint, 2025.
