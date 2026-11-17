-> location_lichsu_001

=== location_lichsu_001 ===
Bạn đang đứng trước cánh cổng đá khổng lồ của "Đền thờ Toán học Cổ đại". Những dòng chữ khắc trên tường cho biết đây là nơi lưu giữ những tri thức về xác suất và giải tích từ hàng thế kỷ trước. Để mở được cánh cổng đầu tiên, một câu đố về những quả cầu ma thuật hiện ra.

+ [Tiến lại gần bảng điều khiển và giải đố] -> task_toanhoc_025

=== task_toanhoc_025 ===
Từ một hộp chứa 7 quả cầu màu đỏ và 5 quả cầu màu xanh, lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được 3 quả cầu màu xanh bằng:
+ [2/7] -> task_toanhoc_025_fail
+ [1/22] -> task_toanhoc_025_success
+ [7/44] -> task_toanhoc_025_fail
+ [5/12] -> task_toanhoc_025_fail

=== task_toanhoc_025_success ===
Chính xác! Những quả cầu xanh trên hình vẽ phát sáng, cơ chế đá chuyển động rầm rầm, cánh cổng mở ra dẫn bạn vào sâu bên trong.
-> location_lichsu_002

=== task_toanhoc_025_fail ===
Sai rồi! Các quả cầu xám xịt lại và một luồng điện nhẹ đẩy tay bạn ra. Bạn cần tính toán lại không gian mẫu và số cách chọn quả cầu xanh.
+ [Thử lại câu hỏi này] -> task_toanhoc_025

=== location_lichsu_002 ===
Bạn bước vào một căn phòng chứa đầy những đồ thị hàm số lơ lửng giữa không trung. Đây là khu vực nghiên cứu về sự biến thiên của các đại lượng. Ở trung tâm căn phòng, một khối đa diện yêu cầu bạn xác định giá trị của tham số m để ổn định dòng năng lượng.

+ [Kiểm tra khối đa diện] -> task_toanhoc_026

=== task_toanhoc_026 ===
Có bao nhiêu giá trị nguyên của tham số m để hàm số y = (x + 6)/(x + 5m) nghịch biến trên khoảng (10; +∞)?
+ [3] -> task_toanhoc_026_fail
+ [Vô số] -> task_toanhoc_026_fail
+ [5] -> task_toanhoc_026_fail
+ [4] -> task_toanhoc_026_success

=== task_toanhoc_026_success ===
Tuyệt vời! Khi giá trị m được xác định đúng, đồ thị hàm số trở nên ổn định, ánh sáng dịu nhẹ lan tỏa khắp căn phòng. Bạn đã hoàn thành thử thách tại khu vực này.
-> game_end

=== task_toanhoc_026_fail ===
Kết quả không đúng. Hàm số không thể nghịch biến nếu m không thỏa mãn đồng thời điều kiện về đạo hàm và tập xác định. Hãy suy nghĩ kỹ về điều kiện x khác -5m.
+ [Thử lại câu hỏi này] -> task_toanhoc_026

=== game_end ===
Chúc mừng bạn đã vượt qua các thử thách toán học trong thư viện lịch sử! Kiến thức của bạn về xác suất và hàm số đã giúp bạn chinh phục được những câu đố hóc búa nhất.
-> END