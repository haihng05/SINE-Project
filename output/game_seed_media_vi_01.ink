-> location_start

=== location_start ===
Bạn bước vào Phòng Thu Âm Cũ. Không gian tĩnh lặng, chỉ có tiếng kim đĩa than rè rè.
+ [Kiểm tra bàn điều khiển] -> task_media_vi_001_knot

=== task_media_vi_001_knot ===
Hệ màu nào sau đây được sử dụng chủ yếu trong kỹ thuật in ấn thương mại?
+ [RGB] -> task_media_vi_001_fail
+ [CMYK] -> task_media_vi_001_success
+ [HSV] -> task_media_vi_001_fail
+ [Lab] -> task_media_vi_001_fail

=== task_media_vi_001_success ===
Chính xác! Bàn điều khiển bật sáng đèn xanh, mở ra cánh cửa dẫn đến Phòng Dựng Phim Kỹ Thuật Số.
-> location_phong_dung_phim

=== task_media_vi_001_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_media_vi_001_knot

=== location_phong_dung_phim ===
Bạn bước vào Phòng Dựng Phim Kỹ Thuật Số. Không gian hiện đại với các máy móc tinh vi.
+ [Kiểm tra bàn điều khiển] -> task_media_vi_002_knot

=== task_media_vi_002_knot ===
Tần số lấy mẫu (sample rate) tiêu chuẩn của âm thanh chất lượng đĩa CD là bao nhiêu?
+ [22.05 kHz] -> task_media_vi_002_fail
+ [44.1 kHz] -> task_media_vi_002_success
+ [48.0 kHz] -> task_media_vi_002_fail
+ [96.0 kHz] -> task_media_vi_002_fail

=== task_media_vi_002_success ===
Chính xác! Bàn điều khiển bật sáng đèn xanh, mở ra cánh cửa cuối cùng.
-> location_kho_luu_tru

=== task_media_vi_002_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_media_vi_002_knot

=== location_kho_luu_tru ===
Bạn bước vào Kho Lưu Trữ Băng Từ. Không gian đầy ắp các băng từ và thiết bị lưu trữ.
-> END