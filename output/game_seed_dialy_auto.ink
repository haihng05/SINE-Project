// Kịch bản Ink: Hành Trình Khám Phá Địa Lí Trái Đất
// Chuyên gia thiết kế: SINE Script Expert

-> location_dialy_001

=== location_dialy_001 ===
Bạn đang đứng trước một tấm bản đồ thế giới khổng lồ tại Trung tâm Dữ liệu Địa lí. Để bắt đầu hành trình, bạn cần hiểu cách các đối tượng được thể hiện trên bản đồ.
+ [Kiểm tra kiến thức về phương pháp bản đồ] -> task_dialy_001

=== task_dialy_001 ===
Để thể hiện các đối tượng địa lí phân bố theo những điểm cụ thể như sân bay, nhà máy điện, cảng biển trên bản đồ, người ta dùng phương pháp nào?
+ [Phương pháp kí hiệu điểm.] -> task_dialy_001_success
+ [Phương pháp đường chuyển động.] -> task_dialy_001_fail
+ [Phương pháp bản đồ - biểu đồ.] -> task_dialy_001_fail
+ [Phương pháp vùng phân bố.] -> task_dialy_001_fail

=== task_dialy_001_success ===
Chính xác! Các kí hiệu điểm giúp ta xác định vị trí chính xác của đối tượng.
-> location_dialy_002

=== task_dialy_001_fail ===
Rất tiếc, câu trả lời chưa đúng. Hãy nhớ rằng các đối tượng như sân bay hay cảng biển thường được coi là một "điểm" trên bản đồ tỉ lệ nhỏ.
+ [Thử lại] -> task_dialy_001

=== location_dialy_002 ===
Tiếp theo, hãy nhìn vào những mũi tên đang di chuyển trên bản đồ khí tượng.
+ [Tìm hiểu về phương pháp đường chuyển động] -> task_dialy_002

=== task_dialy_002 ===
Phương pháp đường chuyển động trên bản đồ thường được dùng để biểu hiện đối tượng nào sau đây?
+ [Hướng di chuyển của bão, hướng gió và dòng biển.] -> task_dialy_002_success
+ [Mật độ dân số các tỉnh.] -> task_dialy_002_fail
+ [Các mỏ khoáng sản kim loại.] -> task_dialy_002_fail
+ [Diện tích rừng phòng hộ.] -> task_dialy_002_fail

=== task_dialy_002_success ===
Đúng vậy! Những mũi tên sinh động chính là cách tốt nhất để mô tả sự di chuyển.
-> location_dialy_003

=== task_dialy_002_fail ===
Sai rồi. Phương pháp này dùng để thể hiện sự di chuyển cơ động của các đối tượng.
+ [Thử lại] -> task_dialy_002

=== location_dialy_003 ===
Bạn bước vào phòng máy chủ, nơi vận hành hệ thống GIS hiện đại.
+ [Tìm hiểu về chức năng của GIS] -> task_dialy_003

=== task_dialy_003 ===
Hệ thống thông tin địa lí (GIS) có chức năng chính nào sau đây?
+ [Thu thập, lưu trữ, quản lí, phân tích và hiển thị dữ liệu không gian.] -> task_dialy_003_success
+ [Định vị tọa độ vệ tinh GPS mặt đất đơn thuần.] -> task_dialy_003_fail
+ [Đo đạc độ ẩm không khí bằng cơ học.] -> task_dialy_003_fail
+ [Vẽ bản đồ tay truyền thống.] -> task_dialy_003_fail

=== task_dialy_003_success ===
Hoàn toàn chính xác! GIS là một công cụ mạnh mẽ trong quản lí dữ liệu địa lí hiện đại.
-> location_dialy_004

=== task_dialy_003_fail ===
Chưa đúng. GIS không chỉ đơn thuần là định vị, nó bao gồm cả một quy trình xử lí dữ liệu phức tạp.
+ [Thử lại] -> task_dialy_003

=== location_dialy_004 ===
Bây giờ, hãy cùng thám hiểm sâu vào lòng đất để tìm hiểu về cấu tạo của hành tinh chúng ta.
+ [Khám phá lớp vỏ Trái Đất] -> task_dialy_004

=== task_dialy_004 ===
Lớp vỏ Trái Đất (vỏ lục địa và vỏ đại dương) được cấu tạo chủ yếu bởi hai tầng đá nào?
+ [Tầng trầm tích và tầng granit (đá hoa cương) / bazan.] -> task_dialy_004_success
+ [Tầng sắt và niken nóng chảy.] -> task_dialy_004_fail
+ [Tầng quặng manhetit nguyên chất.] -> task_dialy_004_fail
+ [Tầng bùn lỏng biến chất.] -> task_dialy_004_fail

=== task_dialy_004_success ===
Đúng! Granit và bazan là hai thành phần đá chủ chốt tạo nên lớp vỏ vững chắc.
-> location_dialy_005

=== task_dialy_004_fail ===
Sai rồi. Sắt và niken nằm ở nhân Trái Đất, không phải lớp vỏ.
+ [Thử lại] -> task_dialy_004

=== location_dialy_005 ===
Bạn đang đứng trên ranh giới giữa lớp vỏ và lớp man-ti. Đây chính là thạch quyển.
+ [Xác định phạm vi thạch quyển] -> task_dialy_005

=== task_dialy_005 ===
Thạch quyển bao gồm những bộ phận nào sau đây của Trái Đất?
+ [Vỏ Trái Đất và phần trên cùng của lớp man-ti (đến độ sâu khoảng 100km).] -> task_dialy_005_success
+ [Toàn bộ vỏ Trái Đất và nhân Trái Đất.] -> task_dialy_005_fail
+ [Chỉ bao gồm lớp vỏ lục địa bên trên mặt nước.] -> task_dialy_005_fail
+ [Toàn bộ lớp man-ti trên và man-ti dưới.] -> task_dialy_005_fail

=== task_dialy_005_success ===
Chính xác! Thạch quyển là phần cứng ngoài cùng của Trái Đất.
-> location_dialy_006

=== task_dialy_005_fail ===
Không đúng. Thạch quyển rộng hơn lớp vỏ nhưng không bao gồm nhân.
+ [Thử lại] -> task_dialy_005

=== location_dialy_006 ===
Mặt đất dưới chân bạn dường như đang chuyển động rất chậm. Đó là do thuyết kiến tạo mảng.
+ [Tìm hiểu nguyên nhân dịch chuyển mảng] -> task_dialy_006

=== task_dialy_006 ===
Theo thuyết kiến tạo mảng, nguyên nhân làm cho các mảng kiến tạo dịch chuyển liên tục trên lớp man-ti quánh dẻo là do:
+ [Các dòng đối lưu vật chất nhiệt quyển trong lớp man-ti trên.] -> task_dialy_006_success
+ [Lực hấp dẫn của Mặt Trời và Mặt Trăng.] -> task_dialy_006_fail
+ [Tác động của lực Coriolis do Trái Đất tự quay.] -> task_dialy_006_fail
+ [Hiện tượng triều cường và sóng thần đáy biển.] -> task_dialy_006_fail

=== task_dialy_006_success ===
Đúng! Các dòng đối lưu nhiệt chính là "động cơ" đẩy các mảng kiến tạo đi.
-> location_dialy_007

=== task_dialy_006_fail ===
Sai rồi. Lực triều hay lực Coriolis không đủ mạnh để dịch chuyển các đại lục.
+ [Thử lại] -> task_dialy_006

=== location_dialy_007 ===
Bạn đang đứng ở rìa một vực biển sâu thẳm, nơi hai mảng kiến tạo đang va chạm.
+ [Quan sát kết quả của sự xô húc mảng] -> task_dialy_007

=== task_dialy_007 ===
Khi hai mảng kiến tạo đại dương và lục địa xô húc (va chạm) vào nhau, kết quả thường hình thành nên:
+ [Các dãy núi uốn nếp cao đồ sộ và các vực biển sâu kèm theo động đất núi lửa.] -> task_dialy_007_success
+ [Các sống núi ngầm giữa đại dương tách giãn.] -> task_dialy_007_fail
+ [Các vùng đồng bằng châu thổ phẳng lặng.] -> task_dialy_007_fail
+ [Các bồn trũng yên tĩnh không có địa chấn.] -> task_dialy_007_fail

=== task_dialy_007_success ===
Tuyệt vời! Dãy Andes là một ví dụ điển hình cho hiện tượng này.
-> location_dialy_008

=== task_dialy_007_fail ===
Chưa đúng. Sự va chạm thường tạo ra địa hình hiểm trở và hoạt động địa chất mạnh mẽ.
+ [Thử lại] -> task_dialy_007

=== location_dialy_008 ===
Tiếng nổ vang trời và ánh lửa rực sáng từ xa. Bạn đang tiến gần đến khu vực bất ổn nhất hành tinh.
+ [Xác định vành đai lửa] -> task_dialy_008

=== task_dialy_008 ===
Vành đai động đất và núi lửa lớn nhất thế giới chiếm hơn 75% số núi lửa hoạt động trên cạn là:
+ [Vành đai lửa Thái Bình Dương.] -> task_dialy_008_success
+ [Vành đai Địa Trung Hải.] -> task_dialy_008_fail
+ [Vành đai Đại Tây Dương.] -> task_dialy_008_fail
+ [Vành đai Ấn Độ Dương.] -> task_dialy_008_fail

=== task_dialy_008_success ===
Chính xác! Vành đai lửa Thái Bình Dương là nơi diễn ra các hoạt động địa chất dữ dội nhất.
-> location_dialy_009

=== task_dialy_008_fail ===
Sai rồi. Hãy nhớ đến khu vực bao quanh đại dương lớn nhất thế giới.
+ [Thử lại] -> task_dialy_008

=== location_dialy_009 ===
Rời khỏi lòng đất, bạn bắt đầu leo lên một ngọn núi cao. Càng lên cao, bạn càng cảm thấy lạnh.
+ [Giải thích hiện tượng giảm nhiệt độ] -> task_dialy_009

=== task_dialy_009 ===
Càng lên cao, nhiệt độ không khí càng giảm vì nguyên nhân chủ yếu nào sau đây?
+ [Không khí càng loãng, bức xạ nhiệt từ mặt đất lên càng yếu dần.] -> task_dialy_009_success
+ [Gần Mặt Trời hơn nên không khí bị đóng băng.] -> task_dialy_009_fail
+ [Gió trên cao thổi quá mạnh làm mát không khí.] -> task_dialy_009_fail
+ [Tầng ôzôn hấp thụ hết nhiệt năng.] -> task_dialy_009_fail

=== task_dialy_009_success ===
Đúng vậy! Mặt đất mới là nguồn nhiệt chính làm ấm tầng đối lưu.
-> location_dialy_010

=== task_dialy_009_fail ===
Sai rồi. Càng lên cao không khí càng loãng, khả năng hấp thụ và giữ nhiệt của không khí càng giảm.
+ [Thử lại] -> task_dialy_009

=== location_dialy_010 ===
Bạn đang so sánh nhiệt độ giữa vùng Xích đạo nóng ẩm và vùng Cực băng giá.
+ [Phân tích biên độ nhiệt năm] -> task_dialy_010

=== task_dialy_010 ===
Biên độ nhiệt độ năm (sự chênh lệch giữa nhiệt độ tháng cao nhất và tháng thấp nhất) có xu hướng thay đổi như thế nào từ Xích đạo về Cực?
+ [Tăng dần từ Xích đạo về hai Cực.] -> task_dialy_010_success
+ [Giảm dần từ Xích đạo về hai Cực.] -> task_dialy_010_fail
+ [Không thay đổi trên toàn Trái Đất.] -> task_dialy_010_fail
+ [Ở Xích đạo là lớn nhất, ở Cực bằng không.] -> task_dialy_010_fail

=== task_dialy_010_success ===
Chính xác! Ở Xích đạo nhiệt độ ổn định quanh năm, còn vùng Cực có sự chênh lệch rất lớn giữa các mùa.
-> location_dialy_011

=== task_dialy_010_fail ===
Sai rồi. Càng xa Xích đạo, sự chênh lệch nhiệt độ giữa mùa hè và mùa đông càng lớn.
+ [Thử lại] -> task_dialy_010

=== location_dialy_011 ===
Bầu khí quyển bao quanh chúng ta không có áp suất đồng đều.
+ [Tìm hiểu quy luật phân bố khí áp] -> task_dialy_011

=== task_dialy_011 ===
Các đai khí áp cao và áp thấp trên bề mặt Trái Đất phân bố theo quy luật nào?
+ [Phân bố xen kẽ và đối xứng nhau qua đai áp thấp Xích đạo.] -> task_dialy_011_success
+ [Áp cao tập trung toàn bộ ở bán cầu Bắc, áp thấp ở bán cầu Nam.] -> task_dialy_011_fail
+ [Phân bố lộn xộn không theo quy luật nào.] -> task_dialy_011_fail
+ [Chỉ có áp cao ở các cực, toàn bộ phần còn lại là áp thấp.] -> task_dialy_011_fail

=== task_dialy_011_success ===
Đúng! Sự phân bố này tạo nên các hệ thống gió hoàn lưu chính trên Trái Đất.
-> location_dialy_012

=== task_dialy_011_fail ===
Sai rồi. Các đai khí áp phân bố có tính đối xứng rất rõ rệt.
+ [Thử lại] -> task_dialy_011

=== location_dialy_012 ===
Những cánh buồm của các thương nhân xưa kia luôn trông đợi vào một loại gió ổn định.
+ [Xác định hướng gió Mậu dịch] -> task_dialy_012

=== task_dialy_012 ===
Gió Mậu dịch (Tín phong) thổi quanh năm từ khu vực nào về khu vực nào?
+ [Từ áp cao cận chí tuyến về áp thấp Xích đạo.] -> task_dialy_012_success
+ [Từ áp cao cận chí tuyến về áp thấp ôn đới.] -> task_dialy_012_fail
+ [Từ áp cao cực về áp thấp ôn đới.] -> task_dialy_012_fail
+ [Từ biển vào đất liền vào mùa hạ.] -> task_dialy_012_fail

=== task_dialy_012_success ===
Chính xác! Đây là loại gió thổi rất đều đặn, giúp ích cho việc hàng hải thời xưa.
-> location_dialy_013

=== task_dialy_012_fail ===
Chưa chính xác. Hãy nhớ rằng gió Mậu dịch thổi về phía Xích đạo.
+ [Thử lại] -> task_dialy_012

=== location_dialy_013 ===
Bạn đang đứng ở sườn Tây của một dãy núi, cảm nhận luồng gió khô và rất nóng thổi tới.
+ [Giải thích hiện tượng gió Phơn] -> task_dialy_013

=== task_dialy_013 ===
Gió Phơn (gió lào khô nóng) hình thành khi luồng không khí ẩm vượt qua dãy núi cao do hiện tượng nào?
+ [Không khí ẩm gặp sườn đón gió trút hết mưa, khi vượt qua sườn khuất gió bị nén nhiệt độ tăng nhanh theo đoạn nhiệt khô.] -> task_dialy_013_success
+ [Gió mang theo cát sa mạc nóng thổi qua.] -> task_dialy_013_fail
+ [Tầng đối lưu bị thủng cục bộ làm ánh nắng chiếu rọi.] -> task_dialy_013_fail
+ [Mặt đất hấp thụ nhiệt từ nham thạch núi lửa.] -> task_dialy_013_fail

=== task_dialy_013_success ===
Đúng rồi! Đó là lý do tại sao miền Trung Việt Nam thường có những đợt nắng nóng gay gắt.
-> location_dialy_014

=== task_dialy_013_fail ===
Sai rồi. Đây là một quá trình biến đổi nhiệt ẩm khi không khí vượt núi.
+ [Thử lại] -> task_dialy_013

=== location_dialy_014 ===
Bây giờ, hãy hướng tầm mắt ra đại dương bao la. Nước bao phủ phần lớn hành tinh.
+ [Tìm hiểu về tỉ lệ nước mặn] -> task_dialy_014

=== task_dialy_014 ===
Thủy quyển là lớp vỏ lỏng liên tục bao quanh Trái Đất, trong đó nước mặn ở đại dương chiếm khoảng bao nhiêu phần trăm?
+ [Khoảng 97,5% tổng lượng nước toàn cầu.] -> task_dialy_014_success
+ [Khoảng 50% tổng lượng nước.] -> task_dialy_014_fail
+ [Khoảng 70% tổng lượng nước.] -> task_dialy_014_fail
+ [Khoảng 85% tổng lượng nước.] -> task_dialy_014_fail

=== task_dialy_014_success ===
Chính xác! Nước ngọt chỉ chiếm một phần rất nhỏ, vì vậy chúng ta cần bảo vệ nguồn nước.
-> location_dialy_015

=== task_dialy_014_fail ===
Không đúng. Đại dương chiếm phần áp đảo trong tổng lượng nước.
+ [Thử lại] -> task_dialy_014

=== location_dialy_015 ===
Những con sóng đang vỗ rì rào vào mạn thuyền. Điều gì đã tạo ra chúng?
+ [Tìm nguyên nhân sinh ra sóng] -> task_dialy_015

=== task_dialy_015 ===
Nguyên nhân chủ yếu sinh ra hiện tượng sóng biển là do:
+ [Tác động của gió thổi trên mặt nước biển.] -> task_dialy_015_success
+ [Lực hấp dẫn của Mặt Trời.] -> task_dialy_015_fail
+ [Nhiệt độ nước biển thay đổi đột ngột.] -> task_dialy_015_fail
+ [Động đất dưới đáy biển sinh ra sóng thường.] -> task_dialy_015_fail

=== task_dialy_015_success ===
Đúng! Gió chính là "người thợ" tạo nên những con sóng nhấp nhô.
-> location_dialy_016

=== task_dialy_015_fail ===
Sai rồi. Lực hấp dẫn tạo ra thủy triều, không phải sóng thường.
+ [Thử lại] -> task_dialy_015

=== location_dialy_016 ===
Mực nước biển đang dâng cao rất nhanh. Hôm nay là ngày rằm.
+ [Xác định thời điểm triều cường] -> task_dialy_016

=== task_dialy_016 ===
Hiện tượng dao động thủy triều đạt mức nước lớn nhất (triều cường) xảy ra vào những ngày nào trong tháng âm lịch?
+ [Ngày không trăng (mồng 1) và ngày trăng tròn (rằm 15).] -> task_dialy_016_success
+ [Ngày trăng khuyết đầu tháng (mồng 7) và cuối tháng (23).] -> task_dialy_016_fail
+ [Vào tất cả các ngày chủ nhật trong tháng.] -> task_dialy_016_fail
+ [Chỉ xảy ra duy nhất vào ngày rằm tháng tám.] -> task_dialy_016_fail

=== task_dialy_016_success ===
Chính xác! Khi Mặt Trăng, Trái Đất và Mặt Trời nằm thẳng hàng, lực hấp dẫn là lớn nhất.
-> location_dialy_017

=== task_dialy_016_fail ===
Chưa đúng. Triều cường xảy ra khi lực hút của Mặt Trăng và Mặt Trời cùng hướng.
+ [Thử lại] -> task_dialy_016

=== location_dialy_017 ===
Các dòng hải lưu đang chảy cuồn cuộn dưới đại dương, mang theo hơi ấm hoặc cái lạnh đi khắp nơi.
+ [Phân tích ảnh hưởng của dòng biển] -> task_dialy_017

=== task_dialy_017 ===
Dòng biển nóng và dòng biển lạnh có ảnh hưởng rất lớn đến khí hậu ven bờ nơi chúng đi qua như thế nào?
+ [Dòng biển nóng làm tăng nhiệt độ và gây mưa nhiều; dòng biển lạnh làm khí hậu khô hạn ít mưa.] -> task_dialy_017_success
+ [Cả hai dòng biển đều làm khí hậu ven bờ trở nên băng giá quanh năm.] -> task_dialy_017_fail
+ [Dòng biển lạnh mang lại mưa bão cực lớn; dòng biển nóng làm hình thành hoang mạc.] -> task_dialy_017_fail
+ [Không có tác động nào đáng kể đối với đất liền.] -> task_dialy_017_fail

=== task_dialy_017_success ===
Đúng vậy! Dòng biển nóng thường mang lại sự trù phú, còn dòng biển lạnh thường tạo ra hoang mạc ven bờ.
-> location_dialy_018

=== task_dialy_017_fail ===
Sai rồi. Dòng biển nóng và lạnh có tác động trái ngược nhau lên độ ẩm và nhiệt độ.
+ [Thử lại] -> task_dialy_017

=== location_dialy_018 ===
Trở lại đất liền, bạn cúi xuống nhìn lớp đất dưới chân mình.
+ [Định nghĩa về thổ nhưỡng] -> task_dialy_018

=== task_dialy_018 ===
Thổ nhưỡng (đất) là gì?
+ [Lớp vật chất tơi xốp nằm ở bề mặt lục địa, có độ phì (khả năng cung cấp nước, nhiệt, khí và dinh dưỡng cho cây).] -> task_dialy_018_success
+ [Tất cả các loại đá vụn trên sườn núi dốc.] -> task_dialy_018_fail
+ [Cát và sỏi vô cơ dưới đáy sông ngòi.] -> task_dialy_018_fail
+ [Lớp khoáng sản kim loại dưới sâu vỏ Trái Đất.] -> task_dialy_018_fail

=== task_dialy_018_success ===
Chính xác! Độ phì chính là đặc tính quan trọng nhất phân biệt đất với đá.
-> location_dialy_019

=== task_dialy_018_fail ===
Không đúng. Đất phải có khả năng nuôi dưỡng cây trồng (độ phì).
+ [Thử lại] -> task_dialy_018

=== location_dialy_019 ===
Mỗi loại đất có màu sắc và thành phần khác nhau. Tất cả bắt đầu từ đá.
+ [Tìm hiểu vai trò của đá mẹ] -> task_dialy_019

=== task_dialy_019 ===
Nhân tố nào sau đây đóng vai trò cung cấp chất vô cơ cho đất và quyết định thành phần khoáng vật, cơ giới của đất?
+ [Đá mẹ.] -> task_dialy_019_success
+ [Khí hậu.] -> task_dialy_019_fail
+ [Sinh vật.] -> task_dialy_019_fail
+ [Địa hình.] -> task_dialy_019_fail

=== task_dialy_019_success ===
Đúng! Đá mẹ thế nào thì đất con thế ấy, mang theo những khoáng chất đặc trưng.
-> location_dialy_020

=== task_dialy_019_fail ===
Sai rồi. Khí hậu và sinh vật quan trọng, nhưng đá mẹ mới là nguồn gốc khoáng vật.
+ [Thử lại] -> task_dialy_019

=== location_dialy_020 ===
Nhìn những rễ cây đang len lỏi trong đất, bạn nhận ra sự sống cũng góp phần tạo nên đất.
+ [Phân tích vai trò của sinh vật] -> task_dialy_020

=== task_dialy_020 ===
Sinh vật đóng vai trò chủ đạo nào trong quá trình hình thành đất?
+ [Cung cấp chất hữu cơ, phá hủy đá bằng cơ - sinh học và tái tạo độ phì cho đất.] -> task_dialy_020_success
+ [Cung cấp các hạt khoáng sét vô cơ nặng.] -> task_dialy_020_fail
+ [Điều hòa nhiệt độ và áp suất nén lòng đất.] -> task_dialy_020_fail
+ [Tạo ra các đứt gãy kiến tạo.] -> task_dialy_020_fail

=== task_dialy_020_success ===
Chính xác! Không có sinh vật, đất chỉ là những hạt khoáng vô tri.
-> location_dialy_021

=== task_dialy_020_fail ===
Chưa đúng. Vai trò quan trọng nhất của sinh vật là tạo ra mùn và chất hữu cơ.
+ [Thử lại] -> task_dialy_020

=== location_dialy_021 ===
Sự sống tồn tại ở khắp nơi, từ đại dương đến bầu trời. Đó là sinh quyển.
+ [Xác định giới hạn sinh quyển] -> task_dialy_021

=== task_dialy_021 ===
Giới hạn trên của sinh quyển tiếp giáp với tầng nào của khí quyển?
+ [Nơi tiếp giáp với tầng ôzôn (khoảng 20 - 25km).] -> task_dialy_021_success
+ [Tầng ion nhiệt quyển cao 100km.] -> task_dialy_021_fail
+ [Tầng đối lưu ở độ cao 8km.] -> task_dialy_021_fail
+ [Vượt ra ngoài vũ trụ không gian.] -> task_dialy_021_fail

=== task_dialy_021_success ===
Đúng! Tầng ôzôn giống như một tấm lá chắn bảo vệ sự sống khỏi tia cực tím.
-> location_dialy_022

=== task_dialy_021_fail ===
Sai rồi. Sinh quyển không thể tồn tại ở những nơi có bức xạ quá mạnh hoặc thiếu dưỡng khí.
+ [Thử lại] -> task_dialy_021

=== location_dialy_022 ===
Khi đi từ Xích đạo về hai Cực, bạn thấy cảnh quan thay đổi rõ rệt.
+ [Tìm hiểu quy luật địa đới] -> task_dialy_022

=== task_dialy_022 ===
Quy luật địa đới là sự thay đổi có quy luật của tất cả các thành phần địa lí và cảnh quan địa lí theo yếu tố nào?
+ [Theo vĩ độ (từ Xích đạo về hai Cực).] -> task_dialy_022_success
+ [Theo độ cao từ thấp lên đỉnh núi.] -> task_dialy_022_fail
+ [Theo khoảng cách từ biển vào sâu trong nội địa.] -> task_dialy_022_fail
+ [Theo chiều sâu dưới đáy biển.] -> task_dialy_022_fail

=== task_dialy_022_success ===
Chính xác! Vĩ độ quyết định lượng nhiệt nhận được, từ đó thay đổi mọi thứ.
-> location_dialy_023

=== task_dialy_022_fail ===
Chưa chính xác. "Địa đới" liên quan đến các đới theo chiều ngang của Trái Đất.
+ [Thử lại] -> task_dialy_022

=== location_dialy_023 ===
Nhưng tại sao lại có sự thay đổi nhiệt độ theo vĩ độ như vậy?
+ [Giải thích nguyên nhân quy luật địa đới] -> task_dialy_023

=== task_dialy_023 ===
Nguyên nhân căn bản tạo nên quy luật địa đới trên Trái Đất là gì?
+ [Trái Đất hình cầu làm cho góc chiếu của tia sáng Mặt Trời thay đổi giảm dần từ Xích đạo về hai Cực.] -> task_dialy_023_success
+ [Trái Đất nghiêng 66 độ 33 phút khi quay.] -> task_dialy_023_fail
+ [Sự phân bố đan xen giữa lục địa và đại dương.] -> task_dialy_023_fail
+ [Tác động của các dòng biển nóng lạnh.] -> task_dialy_023_fail

=== task_dialy_023_success ===
Đúng rồi! Hình dạng cầu của Trái Đất là gốc rễ của sự phân hóa khí hậu.
-> location_dialy_024

=== task_dialy_023_fail ===
Sai rồi. Hãy tập trung vào yếu tố hình dạng của hành tinh.
+ [Thử lại] -> task_dialy_023

=== location_dialy_024 ===
Cuối cùng, bạn đứng dưới chân một ngọn núi cao vút. Càng lên cao, thảm thực vật lại thay đổi.
+ [Khám phá quy luật đai cao] -> task_dialy_024

=== task_dialy_024 ===
Quy luật đai cao là sự thay đổi của các thành phần tự nhiên và cảnh quan theo yếu tố nào?
+ [Theo độ cao địa hình (càng lên cao nhiệt độ càng giảm, độ ẩm thay đổi).] -> task_dialy_024_success
+ [Theo vĩ tuyến trải dài từ Đông sang Tây.] -> task_dialy_024_fail
+ [Theo thời gian bốn mùa xuân hạ thu đông.] -> task_dialy_024_fail
+ [Theo chu kì hoạt động của vết đen Mặt Trời.] -> task_dialy_024_fail

=== task_dialy_024_success ===
Tuyệt vời! Bạn đã hoàn thành bài kiểm tra cuối cùng về các quy luật địa lí.
-> finish_game

=== task_dialy_024_fail ===
Không đúng. Quy luật đai cao tương tự như quy luật địa đới nhưng diễn ra theo chiều thẳng đứng.
+ [Thử lại] -> task_dialy_024

=== finish_game ===
Chúc mừng! Bạn đã vượt qua hành trình khám phá Địa lí Trái Đất một cách xuất sắc. Kiến thức này sẽ giúp bạn hiểu rõ hơn về thế giới chúng ta đang sống.
+ [Kết thúc hành trình] -> END