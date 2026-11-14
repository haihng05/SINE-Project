# title: Hành Trình Khám Phá Trái Đất
# author: SINE Expert
# theme: Geography Education

-> khoi_dau

=== khoi_dau ===
Chào mừng bạn đến với Học viện Địa lý Toàn cầu. Hôm nay là ngày thi cuối kỳ để bạn trở thành một Chuyên gia Địa lý thực thụ. Bạn cần vượt qua 5 khu vực khảo sát quan trọng để hoàn thành bài thi.

Hãy bắt đầu tại khu vực đầu tiên: **Phòng Bản Đồ**.
+ [Bước vào Phòng Bản Đồ] -> location_phong_ban_do

/* ======================================================
   LOCATION: PHÒNG BẢN ĐỒ
   Tasks: 001, 002, 003
   ====================================================== */
=== location_phong_ban_do ===
Phòng Bản Đồ ngập tràn các tấm bản đồ số và hệ thống máy tính hiện đại. Một giáo sư đang chờ bạn ở bàn điều khiển.
-> task_dialy_001

=== task_dialy_001 ===
Giáo sư hỏi: "Để thể hiện các đối tượng địa lí phân bố theo những điểm cụ thể như sân bay, nhà máy điện, cảng biển trên bản đồ, người ta dùng phương pháp nào?"
+ [Phương pháp kí hiệu điểm] -> task_dialy_001_success
+ [Phương pháp đường chuyển động] -> task_dialy_001_fail
+ [Phương pháp bản đồ - biểu đồ] -> task_dialy_001_fail
+ [Phương pháp vùng phân bố] -> task_dialy_001_fail

=== task_dialy_001_success ===
"Chính xác! Đó là kiến thức cơ bản nhất về bản đồ học."
-> task_dialy_002

=== task_dialy_001_fail ===
"Chưa đúng rồi. Hãy nhớ lại cách chúng ta đánh dấu một điểm cụ thể trên bản đồ."
+ [Thử lại] -> task_dialy_001

=== task_dialy_002 ===
"Tiếp theo, phương pháp đường chuyển động trên bản đồ thường được dùng để biểu hiện đối tượng nào sau đây?"
+ [Hướng di chuyển của bão, hướng gió và dòng biển] -> task_dialy_002_success
+ [Mật độ dân số các tỉnh] -> task_dialy_002_fail
+ [Các mỏ khoáng sản kim loại] -> task_dialy_002_fail
+ [Diện tích rừng phòng hộ] -> task_dialy_002_fail

=== task_dialy_002_success ===
"Rất tốt! Các mũi tên chính là biểu tượng của sự chuyển động."
-> task_dialy_003

=== task_dialy_002_fail ===
"Sai rồi. Đường chuyển động phải thể hiện sự di chuyển chứ."
+ [Thử lại] -> task_dialy_002

=== task_dialy_003 ===
"Câu hỏi cuối cùng tại phòng này: Hệ thống thông tin địa lí (GIS) có chức năng chính nào sau đây?"
+ [Thu thập, lưu trữ, quản lí, phân tích và hiển thị dữ liệu không gian] -> task_dialy_003_success
+ [Định vị tọa độ vệ tinh GPS mặt đất đơn thuần] -> task_dialy_003_fail
+ [Đo đạc độ ẩm không khí bằng cơ học] -> task_dialy_003_fail
+ [Vẽ bản đồ tay truyền thống] -> task_dialy_003_fail

=== task_dialy_003_success ===
"Tuyệt vời! Bạn đã nắm vững công nghệ GIS hiện đại. Mời bạn sang khu vực tiếp theo."
-> location_bao_tang_dia_chat

=== task_dialy_003_fail ===
"Chưa đúng. GIS là một hệ thống tích hợp nhiều chức năng xử lý dữ liệu không gian."
+ [Thử lại] -> task_dialy_003

/* ======================================================
   LOCATION: BẢO TÀNG ĐỊA CHẤT
   Tasks: 004, 005, 006, 007, 008
   ====================================================== */
=== location_bao_tang_dia_chat ===
Bạn bước vào một sảnh lớn trưng bày các mẫu đá và mô hình cấu tạo Trái Đất.
-> task_dialy_004

=== task_dialy_004 ===
Trên bảng thông tin có câu hỏi: "Lớp vỏ Trái Đất (vỏ lục địa và vỏ đại dương) được cấu tạo chủ yếu bởi hai tầng đá nào?"
+ [Tầng trầm tích và tầng granit (đá hoa cương) / bazan] -> task_dialy_004_success
+ [Tầng sắt và niken nóng chảy] -> task_dialy_004_fail
+ [Tầng quặng manhetit nguyên chất] -> task_dialy_004_fail
+ [Tầng bùn lỏng biến chất] -> task_dialy_004_fail

=== task_dialy_004_success ===
Đáp án đúng! Bạn nhận thấy mô hình vỏ Trái Đất sáng đèn.
-> task_dialy_005

=== task_dialy_004_fail ===
Sai rồi. Hãy chú ý đến các loại đá phổ biến ở lục địa và đại dương.
+ [Thử lại] -> task_dialy_004

=== task_dialy_005 ===
"Thạch quyển bao gồm những bộ phận nào sau đây của Trái Đất?"
+ [Vỏ Trái Đất và phần trên cùng của lớp man-ti (đến độ sâu khoảng 100km)] -> task_dialy_005_success
+ [Toàn bộ vỏ Trái Đất và nhân Trái Đất] -> task_dialy_005_fail
+ [Chỉ bao gồm lớp vỏ lục địa bên trên mặt nước] -> task_dialy_005_fail
+ [Toàn bộ lớp man-ti trên và man-ti dưới] -> task_dialy_005_fail

=== task_dialy_005_success ===
Chính xác. Thạch quyển cứng cáp bao bọc bên ngoài.
-> task_dialy_006

=== task_dialy_005_fail ===
Không đúng. Thạch quyển không chỉ có lớp vỏ đâu.
+ [Thử lại] -> task_dialy_005

=== task_dialy_006 ===
"Theo thuyết kiến tạo mảng, nguyên nhân làm cho các mảng kiến tạo dịch chuyển liên tục trên lớp man-ti quánh dẻo là do:"
+ [Các dòng đối lưu vật chất nhiệt quyển trong lớp man-ti trên] -> task_dialy_006_success
+ [Lực hấp dẫn của Mặt Trời và Mặt Trăng] -> task_dialy_006_fail
+ [Tác động của lực Coriolis do Trái Đất tự quay] -> task_dialy_006_fail
+ [Hiện tượng triều cường và sóng thần đáy biển] -> task_dialy_006_fail

=== task_dialy_006_success ===
Đúng vậy, chính nội lực từ các dòng đối lưu đã đẩy các mảng đi.
-> task_dialy_007

=== task_dialy_006_fail ===
Sai rồi. Hãy nghĩ về nguồn năng lượng khổng lồ bên trong lòng đất.
+ [Thử lại] -> task_dialy_006

=== task_dialy_007 ===
"Khi hai mảng kiến tạo đại dương và lục địa xô húc (va chạm) vào nhau, kết quả thường hình thành nên:"
+ [Các dãy núi uốn nếp cao đồ sộ và các vực biển sâu kèm theo động đất núi lửa] -> task_dialy_007_success
+ [Các sống núi ngầm giữa đại dương tách giãn] -> task_dialy_007_fail
+ [Các vùng đồng bằng châu thổ phẳng lặng] -> task_dialy_007_fail
+ [Các bồn trũng yên tĩnh không có địa chấn] -> task_dialy_007_fail

=== task_dialy_007_success ===
Chính xác! Sự va chạm này tạo nên những địa hình hùng vĩ và dữ dội nhất.
-> task_dialy_008

=== task_dialy_007_fail ===
Chưa đúng. Sự va chạm (xô húc) phải tạo ra sự biến dạng mạnh mẽ.
+ [Thử lại] -> task_dialy_007

=== task_dialy_008 ===
"Vành đai động đất và núi lửa lớn nhất thế giới chiếm hơn 75% số núi lửa hoạt động trên cạn là:"
+ [Vành đai lửa Thái Bình Dương] -> task_dialy_008_success
+ [Vành đai Địa Trung Hải] -> task_dialy_008_fail
+ [Vành đai Đại Tây Dương] -> task_dialy_008_fail
+ [Vành đai Ấn Độ Dương] -> task_dialy_008_fail

=== task_dialy_008_success ===
Hoàn toàn chính xác. Bạn đã hoàn thành thử thách tại Bảo tàng Địa chất!
-> location_tram_khi_tuong

=== task_dialy_008_fail ===
"Sai rồi. Hãy nhớ đến khu vực bao quanh đại dương lớn nhất hành tinh."
+ [Thử lại] -> task_dialy_008

/* ======================================================
   LOCATION: TRẠM KHÍ TƯỢNG
   Tasks: 009, 010, 011, 012, 013
   ====================================================== */
=== location_tram_khi_tuong ===
Bạn leo lên đỉnh tháp của Trạm Khí Tượng, nơi gió thổi lồng lộng và các thiết bị đo đang quay liên tục.
-> task_dialy_009

=== task_dialy_009 ===
Một kỹ thuật viên hỏi: "Càng lên cao, nhiệt độ không khí càng giảm vì nguyên nhân chủ yếu nào sau đây?"
+ [Không khí càng loãng, bức xạ nhiệt từ mặt đất lên càng yếu dần] -> task_dialy_009_success
+ [Gần Mặt Trời hơn nên không khí bị đóng băng] -> task_dialy_009_fail
+ [Gió trên cao thổi quá mạnh làm mát không khí] -> task_dialy_009_fail
+ [Tầng ôzôn hấp thụ hết nhiệt năng] -> task_dialy_009_fail

=== task_dialy_009_success ===
Đúng rồi. Mặt đất mới là nguồn nhiệt chính cho tầng đối lưu.
-> task_dialy_010

=== task_dialy_009_fail ===
Sai rồi. Hãy nhớ rằng không khí được sưởi ấm chủ yếu từ dưới lên.
+ [Thử lại] -> task_dialy_009

=== task_dialy_010 ===
"Biên độ nhiệt độ năm có xu hướng thay đổi như thế nào từ Xích đạo về Cực?"
+ [Tăng dần từ Xích đạo về hai Cực] -> task_dialy_010_success
+ [Giảm dần từ Xích đạo về hai Cực] -> task_dialy_010_fail
+ [Không thay đổi trên toàn Trái Đất] -> task_dialy_010_fail
+ [Ở Xích đạo là lớn nhất, ở Cực bằng không] -> task_dialy_010_fail

=== task_dialy_010_success ===
Chính xác. Càng về gần cực, sự chênh lệch nhiệt độ giữa các mùa càng lớn.
-> task_dialy_011

=== task_dialy_010_fail ===
Không đúng. Ở Xích đạo nóng quanh năm nên biên độ nhiệt rất nhỏ.
+ [Thử lại] -> task_dialy_010

=== task_dialy_011 ===
"Các đai khí áp cao và áp thấp trên bề mặt Trái Đất phân bố theo quy luật nào?"
+ [Phân bố xen kẽ và đối xứng nhau qua đai áp thấp Xích đạo] -> task_dialy_011_success
+ [Áp cao tập trung toàn bộ ở bán cầu Bắc, áp thấp ở bán cầu Nam] -> task_dialy_011_fail
+ [Phân bố lộn xộn không theo quy luật nào] -> task_dialy_011_fail
+ [Chỉ có áp cao ở các cực, toàn bộ phần còn lại là áp thấp] -> task_dialy_011_fail

=== task_dialy_011_success ===
Đúng! Sự phân bố này tạo nên các hệ thống gió chính.
-> task_dialy_012

=== task_dialy_011_fail ===
Sai rồi. Khí áp phân bố có tính đối xứng rất rõ rệt.
+ [Thử lại] -> task_dialy_011

=== task_dialy_012 ===
"Gió Mậu dịch (Tín phong) thổi quanh năm từ khu vực nào về khu vực nào?"
+ [Từ áp cao cận chí tuyến về áp thấp Xích đạo] -> task_dialy_012_success
+ [Từ áp cao cận chí tuyến về áp thấp ôn đới] -> task_dialy_012_fail
+ [Từ áp cao cực về áp thấp ôn đới] -> task_dialy_012_fail
+ [Từ biển vào đất liền vào mùa hạ] -> task_dialy_012_fail

=== task_dialy_012_success ===
Chính xác. Đây là loại gió quan trọng trong lịch sử hàng hải.
-> task_dialy_013

=== task_dialy_012_fail ===
Sai rồi. Hãy nhớ hướng thổi của gió Tín phong hướng về phía Xích đạo.
+ [Thử lại] -> task_dialy_012

=== task_dialy_013 ===
"Gió Phơn (gió lào khô nóng) hình thành khi luồng không khí ẩm vượt qua dãy núi cao do hiện tượng nào?"
+ [Không khí ẩm gặp sườn đón gió trút hết mưa, khi vượt qua sườn khuất gió bị nén nhiệt độ tăng nhanh] -> task_dialy_013_success
+ [Gió mang theo cát sa mạc nóng thổi qua] -> task_dialy_013_fail
+ [Tầng đối lưu bị thủng cục bộ làm ánh nắng chiếu rọi] -> task_dialy_013_fail
+ [Mặt đất hấp thụ nhiệt từ nham thạch núi lửa] -> task_dialy_013_fail

=== task_dialy_013_success ===
Rất giỏi! Bạn đã hiểu rõ cơ chế biến tính của khối khí khi vượt núi.
-> location_tram_thuy_van

=== task_dialy_013_fail ===
"Không đúng. Đây là hiệu ứng xảy ra khi gió vượt qua địa hình núi cao."
+ [Thử lại] -> task_dialy_013

/* ======================================================
   LOCATION: TRẠM THỦY VĂN
   Tasks: 014, 015, 016, 017
   ====================================================== */
=== location_tram_thuy_van ===
Rời tháp khí tượng, bạn đi xuống khu vực ven hồ, nơi đặt Trạm Thủy Văn để nghiên cứu về nước.
-> task_dialy_014

=== task_dialy_014 ===
"Thủy quyển là lớp vỏ lỏng liên tục bao quanh Trái Đất, trong đó nước mặn ở đại dương chiếm khoảng bao nhiêu phần trăm?"
+ [Khoảng 97,5% tổng lượng nước toàn cầu] -> task_dialy_014_success
+ [Khoảng 50% tổng lượng nước] -> task_dialy_014_fail
+ [Khoảng 70% tổng lượng nước] -> task_dialy_014_fail
+ [Khoảng 85% tổng lượng nước] -> task_dialy_014_fail

=== task_dialy_014_success ===
Đúng vậy, nước ngọt chỉ chiếm một phần rất nhỏ.
-> task_dialy_015

=== task_dialy_014_fail ===
Sai rồi. Lượng nước mặn chiếm đại đa số trên hành tinh chúng ta.
+ [Thử lại] -> task_dialy_014

=== task_dialy_015 ===
"Nguyên nhân chủ yếu sinh ra hiện tượng sóng biển là do:"
+ [Tác động của gió thổi trên mặt nước biển] -> task_dialy_015_success
+ [Lực hấp dẫn của Mặt Trời] -> task_dialy_015_fail
+ [Nhiệt độ nước biển thay đổi đột ngột] -> task_dialy_015_fail
+ [Động đất dưới đáy biển sinh ra sóng thường] -> task_dialy_015_fail

=== task_dialy_015_success ===
Chính xác. Không có gió thì mặt biển sẽ lặng sóng.
-> task_dialy_016

=== task_dialy_015_fail ===
Chưa đúng. Hãy nghĩ về thứ tác động trực tiếp lên bề mặt nước hàng ngày.
+ [Thử lại] -> task_dialy_015

=== task_dialy_016 ===
"Hiện tượng dao động thủy triều đạt mức nước lớn nhất (triều cường) xảy ra vào những ngày nào trong tháng âm lịch?"
+ [Ngày không trăng (mồng 1) và ngày trăng tròn (rằm 15)] -> task_dialy_016_success
+ [Ngày trăng khuyết đầu tháng (mồng 7) và cuối tháng (23)] -> task_dialy_016_fail
+ [Vào tất cả các ngày chủ nhật trong tháng] -> task_dialy_016_fail
+ [Chỉ xảy ra duy nhất vào ngày rằm tháng tám] -> task_dialy_016_fail

=== task_dialy_016_success ===
Đúng! Đó là khi Mặt Trăng, Mặt Trời và Trái Đất cùng nằm trên một đường thẳng.
-> task_dialy_017

=== task_dialy_016_fail ===
Sai rồi. Triều cường xảy ra khi lực hút của Mặt Trăng và Mặt Trời cùng hướng.
+ [Thử lại] -> task_dialy_016

=== task_dialy_017 ===
"Dòng biển nóng và dòng biển lạnh có ảnh hưởng rất lớn đến khí hậu ven bờ nơi chúng đi qua như thế nào?"
+ [Dòng biển nóng làm tăng nhiệt độ và gây mưa nhiều; dòng biển lạnh làm khí hậu khô hạn ít mưa] -> task_dialy_017_success
+ [Cả hai dòng biển đều làm khí hậu ven bờ trở nên băng giá quanh năm] -> task_dialy_017_fail
+ [Dòng biển lạnh mang lại mưa bão cực lớn; dòng biển nóng làm hình thành hoang mạc] -> task_dialy_017_fail
+ [Không có tác động nào đáng kể đối với đất liền] -> task_dialy_017_fail

=== task_dialy_017_success ===
Chính xác. Các dòng biển đóng vai trò điều hòa khí hậu toàn cầu.
-> location_dai_quan_sat

=== task_dialy_017_fail ===
"Sai rồi. Hãy nhớ rằng dòng biển nóng thường mang hơi ẩm, còn dòng biển lạnh thì ngược lại."
+ [Thử lại] -> task_dialy_017

/* ======================================================
   LOCATION: ĐÀI QUAN SÁT
   Tasks: 018, 019, 020, 021, 022, 023, 024
   ====================================================== */
=== location_dai_quan_sat ===
Cuối cùng, bạn đến Đài Quan Sát trên đỉnh đồi, nơi có cái nhìn bao quát về đất đai và sự sống.
-> task_dialy_018

=== task_dialy_018 ===
"Thổ nhưỡng (đất) là gì?"
+ [Lớp vật chất tơi xốp nằm ở bề mặt lục địa, có độ phì] -> task_dialy_018_success
+ [Tất cả các loại đá vụn trên sườn núi dốc] -> task_dialy_018_fail
+ [Cát và sỏi vô cơ dưới đáy sông ngòi] -> task_dialy_018_fail
+ [Lớp khoáng sản kim loại dưới sâu vỏ Trái Đất] -> task_dialy_018_fail

=== task_dialy_018_success ===
Đúng! Độ phì chính là đặc điểm quan trọng nhất của đất.
-> task_dialy_019

=== task_dialy_018_fail ===
Không đúng. Đất phải có khả năng nuôi dưỡng cây cối.
+ [Thử lại] -> task_dialy_018

=== task_dialy_019 ===
"Nhân tố nào sau đây đóng vai trò cung cấp chất vô cơ cho đất và quyết định thành phần khoáng vật, cơ giới của đất?"
+ [Đá mẹ] -> task_dialy_019_success
+ [Khí hậu] -> task_dialy_019_fail
+ [Sinh vật] -> task_dialy_019_fail
+ [Địa hình] -> task_dialy_019_fail

=== task_dialy_019_success ===
Chính xác. Đá mẹ sinh ra các hạt khoáng.
-> task_dialy_020

=== task_dialy_019_fail ===
Sai rồi. Hãy nghĩ xem nguồn gốc của các hạt cát, hạt sét trong đất từ đâu mà ra.
+ [Thử lại] -> task_dialy_019

=== task_dialy_020 ===
"Sinh vật đóng vai trò chủ đạo nào trong quá trình hình thành đất?"
+ [Cung cấp chất hữu cơ, phá hủy đá bằng cơ - sinh học và tái tạo độ phì cho đất] -> task_dialy_020_success
+ [Cung cấp các hạt khoáng sét vô cơ nặng] -> task_dialy_020_fail
+ [Điều hòa nhiệt độ và áp suất nén lòng đất] -> task_dialy_020_fail
+ [Tạo ra các đứt gãy kiến tạo] -> task_dialy_020_fail

=== task_dialy_020_success ===
Đúng vậy. Không có sinh vật, đất chỉ là những hạt khoáng chết.
-> task_dialy_021

=== task_dialy_020_fail ===
Sai rồi. Vai trò của sinh vật liên quan mật thiết đến chất hữu cơ.
+ [Thử lại] -> task_dialy_020

=== task_dialy_021 ===
"Giới hạn trên của sinh quyển tiếp giáp với tầng nào của khí quyển?"
+ [Nơi tiếp giáp với tầng ôzôn (khoảng 20 - 25km)] -> task_dialy_021_success
+ [Tầng ion nhiệt quyển cao 100km] -> task_dialy_021_fail
+ [Tầng đối lưu ở độ cao 8km] -> task_dialy_021_fail
+ [Vượt ra ngoài vũ trụ không gian] -> task_dialy_021_fail

=== task_dialy_021_success ===
Chính xác. Tầng ôzôn là lá chắn bảo vệ sự sống nên cũng là giới hạn của nó.
-> task_dialy_022

=== task_dialy_021_fail ===
Sai rồi. Sự sống không thể tồn tại quá cao nơi có bức xạ vũ trụ mạnh.
+ [Thử lại] -> task_dialy_021

=== task_dialy_022 ===
"Quy luật địa đới là sự thay đổi có quy luật của tất cả các thành phần địa lí và cảnh quan địa lí theo yếu tố nào?"
+ [Theo vĩ độ (từ Xích đạo về hai Cực)] -> task_dialy_022_success
+ [Theo độ cao từ thấp lên đỉnh núi] -> task_dialy_022_fail
+ [Theo khoảng cách từ biển vào sâu trong nội địa] -> task_dialy_022_fail
+ [Theo chiều sâu dưới đáy biển] -> task_dialy_022_fail

=== task_dialy_022_success ===
Đúng! Đó là quy luật quan trọng nhất trên Trái Đất.
-> task_dialy_023

=== task_dialy_022_fail ===
Sai rồi. "Địa đới" liên quan đến các đới theo chiều ngang của Trái Đất.
+ [Thử lại] -> task_dialy_022

=== task_dialy_023 ===
"Nguyên nhân căn bản tạo nên quy luật địa đới trên Trái Đất là gì?"
+ [Trái Đất hình cầu làm cho góc chiếu của tia sáng Mặt Trời thay đổi giảm dần từ Xích đạo về hai Cực] -> task_dialy_023_success
+ [Trái Đất nghiêng 66 độ 33 phút khi quay] -> task_dialy_023_fail
+ [Sự phân bố đan xen giữa lục địa và đại dương] -> task_dialy_023_fail
+ [Tác động của các dòng biển nóng lạnh] -> task_dialy_023_fail

=== task_dialy_023_success ===
Chính xác. Hình dạng Trái Đất quyết định lượng nhiệt nhận được.
-> task_dialy_024

=== task_dialy_023_fail ===
Sai rồi. Hãy nghĩ về hình dạng của hành tinh chúng ta.
+ [Thử lại] -> task_dialy_023

=== task_dialy_024 ===
Câu hỏi cuối cùng để nhận chứng chỉ: "Quy luật đai cao là sự thay đổi của các thành phần tự nhiên và cảnh quan theo yếu tố nào?"
+ [Theo độ cao địa hình (càng lên cao nhiệt độ càng giảm, độ ẩm thay đổi)] -> task_dialy_024_success
+ [Theo vĩ tuyến trải dài từ Đông sang Tây] -> task_dialy_024_fail
+ [Theo thời gian bốn mùa xuân hạ thu đông] -> task_dialy_024_fail
+ [Theo chu kì hoạt động của vết đen Mặt Trời] -> task_dialy_024_fail

=== task_dialy_024_success ===
Chúc mừng! Bạn đã trả lời đúng câu hỏi cuối cùng.
-> ket_thuc

=== task_dialy_024_fail ===
Sai rồi. "Đai cao" thì phải liên quan đến độ cao chứ.
+ [Thử lại] -> task_dialy_024

=== ket_thuc ===
Giáo sư trưởng bước ra và trao cho bạn tấm bằng Chuyên gia Địa lý. Bạn đã vượt qua tất cả các thử thách từ bản đồ, địa chất đến khí hậu và sinh quyển. Kiến thức của bạn về hành tinh xanh thật đáng nể!

HÀNH TRÌNH KẾT THÚC TẠI ĐÂY.
-> END