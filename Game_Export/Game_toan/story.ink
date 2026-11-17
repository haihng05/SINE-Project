// Kịch bản Game Giáo dục Toán học: Tháp Trí Tuệ
-> location_toan_001

=== location_toan_001 ===
Bạn đứng trước cánh cổng khổng lồ của Tháp Trí Tuệ. Trên cánh cổng có khảm những viên ngọc xanh đỏ lấp lánh. Một giọng nói trầm đục vang lên: "Kẻ muốn bước vào phải thấu hiểu quy luật của sự ngẫu nhiên."

+ [Tiến lại gần và đọc câu đố trên cổng] -> task_toan_025

=== task_toan_025 ===
Trên bệ đá hiện ra dòng chữ: 
"Từ một hộp chứa 7 quả cầu màu đỏ và 5 quả cầu màu xanh, lấy ngẫu nhiên đồng thời 3 quả. Xác suất để lấy được 3 quả cầu màu xanh bằng:"

+ [\frac\{2\}\{7\}] -> task_toan_025_fail
+ [\frac\{1\}\{22\}] -> task_toan_025_success
+ [\frac\{7\}\{44\}] -> task_toan_025_fail
+ [\frac\{5\}\{12\}] -> task_toan_025_fail

=== task_toan_025_success ===
Những viên ngọc trên cổng phát sáng rực rỡ! Cánh cổng từ từ mở ra, dẫn bạn vào một hành lang dài lấp lánh ánh sao.
-> location_toan_002

=== task_toan_025_fail ===
Cánh cổng rung chuyển mạnh, một luồng điện nhẹ đẩy bạn lùi lại. Có vẻ tính toán của bạn chưa chính xác. Hãy bình tĩnh tính lại không gian mẫu và số cách chọn thuận lợi.

+ [Thử lại câu hỏi này] -> task_toan_025

=== location_toan_002 ===
Bạn bước vào căn phòng trung tâm. Ở đây, không gian dường như uốn lượn theo những đường cong đồ thị. Một bảng điều khiển bằng pha lê hiện ra, yêu cầu bạn xác định giá trị của tham số để ổn định dòng năng lượng.

+ [Kiểm tra bảng điều khiển pha lê] -> task_toan_026

=== task_toan_026 ===
Nội dung trên bảng pha lê ghi:
"Có bao nhiêu giá trị nguyên của tham số m để hàm số $y = \frac\{x+6\}\{x+5m\}$ nghịch biến trên khoảng $(10; +\infty)$?"

+ [3] -> task_toan_026_fail
+ [Vô số] -> task_toan_026_fail
+ [5] -> task_toan_026_fail
+ [4] -> task_toan_026_success

=== task_toan_026_success ===
Dòng năng lượng dần ổn định, ánh sáng xanh dịu mắt lan tỏa khắp căn phòng. Bạn đã giải mã thành công bí ẩn của hàm số!
Một lối thoát hiện ra phía trước, dẫn bạn trở về thế giới thực với kho tàng tri thức mới.

-> game_clear

=== task_toan_026_fail ===
Bảng pha lê nhấp nháy đỏ. Các đường cong đồ thị trở nên hỗn loạn. Bạn cần xem xét kỹ điều kiện để hàm số phân thức nghịch biến và điều kiện về tập xác định trên khoảng đã cho.

+ [Thử lại câu hỏi này] -> task_toan_026

=== game_clear ===
Chúc mừng bạn đã hoàn thành thử thách Toán học trong Tháp Trí Tuệ! 
Bạn đã chứng minh được khả năng tư duy logic và kỹ năng giải toán tuyệt vời của mình.
-> END