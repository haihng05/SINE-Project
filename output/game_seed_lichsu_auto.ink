// Kịch bản Ink: Hành Trình Di Sản Lịch Sử Việt Nam
// Chuyên gia thiết kế: SINE Expert

-> location_bao_tang_lich_su

=== location_bao_tang_lich_su ===
Bạn đang đứng trước sảnh chính của Bảo tàng Lịch sử Quốc gia. Ánh đèn vàng dịu nhẹ soi sáng những hiện vật cổ kính. Một hướng dẫn viên ảo xuất hiện và nói: "Chào mừng bạn đến với hành trình tìm hiểu về trật tự thế giới và các tổ chức quốc tế."
+ [Bắt đầu tìm hiểu về Trật tự I-an-ta] -> task_lichsu_001

=== task_lichsu_001 ===
Trật tự thế giới hai cực I-an-ta (hình thành sau Hội nghị Ianta 1945) bị chi phối bởi hai siêu cường đại diện cho hai hệ tư tưởng đối lập nào?
+ [Mỹ (tư bản chủ nghĩa) và Liên Xô (xã hội chủ nghĩa).] -> task_lichsu_001_success
+ [Anh và Pháp.] -> task_lichsu_001_fail
+ [Mỹ và Trung Quốc.] -> task_lichsu_001_fail
+ [Liên Xô và Đức.] -> task_lichsu_001_fail

=== task_lichsu_001_success ===
Chính xác! Sự đối đầu giữa Mỹ và Liên Xô đã định hình lịch sử thế giới suốt nhiều thập kỷ.
-> task_lichsu_002

=== task_lichsu_001_fail ===
Rất tiếc, đó chưa phải là đáp án đúng. Hãy nhớ về hai phe trong Chiến tranh Lạnh.
+ [Thử lại] -> task_lichsu_001

=== task_lichsu_002 ===
Mục tiêu bao trùm cao nhất của tổ chức Liên hợp quốc được nêu rõ trong Hiến chương là gì?
+ [Duy trì hòa bình và an ninh quốc tế, phát triển quan hệ hữu nghị hợp tác giữa các quốc gia.] -> task_lichsu_002_success
+ [Thiết lập liên minh quân sự chống lại các nước nghèo.] -> task_lichsu_002_fail
+ [Thống nhất tiền tệ trên quy mô toàn cầu.] -> task_lichsu_002_fail
+ [Xóa bỏ hoàn toàn biên giới các quốc gia.] -> task_lichsu_002_fail

=== task_lichsu_002_success ===
Đúng vậy! Hòa bình là mục tiêu tối thượng của nhân loại.
-> task_lichsu_003

=== task_lichsu_002_fail ===
Sai rồi. Hãy đọc kỹ lại tôn chỉ của Liên hợp quốc nhé.
+ [Thử lại] -> task_lichsu_002

=== task_lichsu_003 ===
Cơ quan nào của Liên hợp quốc giữ vai trò trọng yếu trong việc duy trì hòa bình và an ninh thế giới, với 5 nước ủy viên thường trực có quyền phủ quyết?
+ [Hội đồng Bảo an.] -> task_lichsu_003_success
+ [Đại hội đồng.] -> task_lichsu_003_fail
+ [Ban Thư kí.] -> task_lichsu_003_fail
+ [Tòa án Công lí Quốc tế.] -> task_lichsu_003_fail

=== task_lichsu_003_success ===
Chính xác! Hội đồng Bảo an là cơ quan quyền lực nhất của LHQ.
-> task_lichsu_004

=== task_lichsu_003_fail ===
Chưa đúng. Đây là cơ quan có 5 nước ủy viên thường trực.
+ [Thử lại] -> task_lichsu_003

=== task_lichsu_004 ===
Hiệp hội các quốc gia Đông Nam Á (ASEAN) được thành lập vào ngày 8/8/1967 tại Băng Cốc (Thái Lan) với sự tham gia của 5 nước sáng lập đầu tiên là:
+ [In-đô-nê-xi-a, Ma-lai-xi-a, Phi-líp-pin, Xin-ga-po và Thái Lan.] -> task_lichsu_004_success
+ [Việt Nam, Lào, Cam-pu-chia, Mi-an-ma và Thái Lan.] -> task_lichsu_004_fail
+ [Bru-nây, Xin-ga-po, Thái Lan, In-đô-nê-xi-a và Việt Nam.] -> task_lichsu_004_fail
+ [Ma-lai-xi-a, Xin-ga-po, Đông Ti-mo, Lào và Thái Lan.] -> task_lichsu_004_fail

=== task_lichsu_004_success ===
Rất tốt! Đó là 5 quốc gia đặt nền móng cho sự hợp tác khu vực.
-> task_lichsu_005

=== task_lichsu_004_fail ===
Sai rồi. Việt Nam gia nhập ASEAN muộn hơn nhiều (năm 1995).
+ [Thử lại] -> task_lichsu_004

=== task_lichsu_005 ===
Văn kiện pháp lí nền tảng xác định mục tiêu xây dựng Đông Nam Á thành khu vực hòa bình, tự do và trung lập (ZOPFAN) là:
+ [Tuyên bố Băng Cốc và Tuyên bố Cua-la Lăm-pơ (1971).] -> task_lichsu_005_success
+ [Hiệp ước Ba-li năm 1976.] -> task_lichsu_005_fail
+ [Hiến chương ASEAN năm 2007.] -> task_lichsu_005_fail
+ [Kế hoạch Colombo.] -> task_lichsu_005_fail

=== task_lichsu_005_success ===
Chính xác! ZOPFAN là một dấu mốc quan trọng của ASEAN.
-> task_lichsu_006

=== task_lichsu_005_fail ===
Chưa đúng. Hãy chú ý đến mốc thời gian 1971.
+ [Thử lại] -> task_lichsu_005

=== task_lichsu_006 ===
Năm 1995 ghi dấu mốc lịch sử đặc biệt nào trong quan hệ đối ngoại và hội nhập khu vực của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam?
+ [Việt Nam chính thức gia nhập ASEAN và bình thường hóa quan hệ ngoại giao với Hoa Kỳ.] -> task_lichsu_006_success
+ [Việt Nam gia nhập Tổ chức Thương mại Thế giới (WTO).] -> task_lichsu_006_fail
+ [Việt Nam kí Hiệp định Thương mại Tự do EVFTA.] -> task_lichsu_006_fail
+ [Việt Nam được bầu làm Ủy viên không thường trực Hội đồng Bảo an LHQ.] -> task_lichsu_006_fail

=== task_lichsu_006_success ===
Tuyệt vời! Năm 1995 là năm bản lề trong chính sách đối ngoại của Việt Nam.
-> task_lichsu_007

=== task_lichsu_006_fail ===
Sai rồi. Hãy nhớ lại sự kiện Việt Nam gia nhập ASEAN.
+ [Thử lại] -> task_lichsu_006

=== task_lichsu_007 ===
Sự sụp đổ của Trật tự hai cực I-an-ta và sự tan rã của Liên Xô (1991) đã thúc đẩy trật tự thế giới chuyển biến theo xu thế nào?
+ [Xu thế đa cực, nhiều trung tâm, hợp tác và cạnh tranh hòa bình.] -> task_lichsu_007_success
+ [Trật tự đơn cực do một mình Hoa Kỳ thống trị tuyệt đối vĩnh viễn.] -> task_lichsu_007_fail
+ [Một cuộc chiến tranh thế giới thứ ba bùng nổ toàn diện ngay lập tức.] -> task_lichsu_007_fail
+ [Tất cả các nước đóng cửa biên giới ngừng giao thương.] -> task_lichsu_007_fail

=== task_lichsu_007_success ===
Đúng vậy! Thế giới đang chuyển mình mạnh mẽ sang đa cực.
-> task_lichsu_008

=== task_lichsu_007_fail ===
Không đúng. Thế giới không còn bị thống trị bởi một cực duy nhất.
+ [Thử lại] -> task_lichsu_007

=== task_lichsu_008 ===
Tổ chức liên kết kinh tế - chính trị khu vực lớn nhất và có mức độ hội nhập sâu rộng nhất hành tinh hiện nay là:
+ [Liên minh châu Âu (EU).] -> task_lichsu_008_success
+ [Hiệp hội các quốc gia Đông Nam Á (ASEAN).] -> task_lichsu_008_fail
+ [Diễn đàn Hợp tác Kinh tế châu Á - Thái Bình Dương (APEC).] -> task_lichsu_008_fail
+ [Thị trường chung Nam Mỹ (MERCOSUR).] -> task_lichsu_008_fail

=== task_lichsu_008_success ===
Chính xác! EU là mô hình liên kết khu vực thành công nhất.
-> location_dien_bien_phu

=== task_lichsu_008_fail ===
Sai rồi. Hãy nghĩ đến một tổ chức có đồng tiền chung và thị trường chung rất sâu rộng.
+ [Thử lại] -> task_lichsu_008

=== location_dien_bien_phu ===
Rời bảo tàng, bạn được đưa đến vùng lòng chảo Điện Biên. Tiếng súng đã dứt từ lâu, nhưng hào khí vẫn còn đó.
+ [Tìm hiểu về chiến thắng lừng lẫy năm châu] -> task_lichsu_017

=== task_lichsu_017 ===
Thắng lợi quân sự nào của quân và dân ta đã làm phá sản hoàn toàn Kế hoạch Nava của thực dân Pháp có sự can thiệp của Mỹ năm 1954?
+ [Chiến dịch Điện Biên Phủ.] -> task_lichsu_017_success
+ [Chiến dịch Biên giới Thu Đông 1950.] -> task_lichsu_017_fail
+ [Chiến thắng Việt Bắc Thu Đông 1947.] -> task_lichsu_017_fail
+ [Chiến dịch Thượng Lào 1953.] -> task_lichsu_017_fail

=== task_lichsu_017_success ===
Chính xác! Điện Biên Phủ là "cái mốc bằng vàng" của lịch sử dân tộc.
-> location_dao_truong_sa

=== task_lichsu_017_fail ===
Sai rồi. Hãy nhớ đến chiến dịch kết thúc cuộc kháng chiến chống Pháp.
+ [Thử lại] -> task_lichsu_017

=== location_dao_truong_sa ===
Sóng biển rì rào, bạn đang đứng trên đảo Trường Sa Lớn. Giữa biển khơi, lòng tự hào dân tộc trỗi dậy mạnh mẽ.
+ [Tiếp tục hành trình lịch sử kháng chiến và chủ quyền] -> task_lichsu_018

=== task_lichsu_018 ===
Chiến thắng quân sự nào mở đầu cho cao trào 'Tìm Mỹ mà đánh, lùng ngụy mà diệt' ở miền Nam năm 1965?
+ [Chiến thắng Vạn Tường (Quảng Ngãi).] -> task_lichsu_018_success
+ [Chiến thắng Ấp Bắc (Mỹ Tho).] -> task_lichsu_018_fail
+ [Chiến thắng Ba Gia.] -> task_lichsu_018_fail
+ [Chiến dịch Đồng Xoài.] -> task_lichsu_018_fail

=== task_lichsu_018_success ===
Đúng! Vạn Tường đã chứng minh ta có khả năng đánh thắng Mỹ về quân sự.
-> task_lichsu_019

=== task_lichsu_018_fail ===
Chưa đúng. Ấp Bắc là năm 1963, còn đây là năm 1965 tại Quảng Ngãi.
+ [Thử lại] -> task_lichsu_018

=== task_lichsu_019 ===
Hiệp định Pa-ri năm 1973 về chấm dứt chiến tranh, lập lại hòa bình ở Việt Nam đã buộc Hoa Kỳ phải thực hiện cam kết mấu chốt nào?
+ [Tôn trọng độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của Việt Nam, rút hết quân viễn chinh về nước.] -> task_lichsu_019_success
+ [Tiếp tục viện trợ quân sự không giới hạn cho chính quyền Sài Gòn.] -> task_lichsu_019_fail
+ [Duy trì các căn cứ quân sự Mỹ lâu dài ở miền Nam.] -> task_lichsu_019_fail
+ [Được quyền can thiệp vào bầu cử tự do của nhân dân miền Nam.] -> task_lichsu_019_fail

=== task_lichsu_019_success ===
Chính xác! Đây là thắng lợi to lớn trên mặt trận ngoại giao.
-> task_lichsu_020

=== task_lichsu_019_fail ===
Sai rồi. Mỹ buộc phải rút quân, đó là điều khoản quan trọng nhất.
+ [Thử lại] -> task_lichsu_019

=== task_lichsu_020 ===
Cuộc Tổng tiến công và nổi dậy Xuân 1975 đã toàn thắng sau bao nhiêu ngày đêm tiến công thần tốc?
+ [55 ngày đêm (từ 4/3 đến 30/4/1975).] -> task_lichsu_020_success
+ [81 ngày đêm bảo vệ Thành cổ Quảng Trị.] -> task_lichsu_020_fail
+ [12 ngày đêm Điện Biên Phủ trên không.] -> task_lichsu_020_fail
+ [100 ngày đêm chiến dịch Tây Nguyên.] -> task_lichsu_020_fail

=== task_lichsu_020_success ===
Rất tốt! 55 ngày đêm thần tốc đã giải phóng hoàn toàn miền Nam.
-> task_lichsu_023

=== task_lichsu_020_fail ===
Sai rồi. Hãy nhớ mốc thời gian từ chiến dịch Tây Nguyên đến khi kết thúc chiến dịch Hồ Chí Minh.
+ [Thử lại] -> task_lichsu_020

=== task_lichsu_023 ===
Trách nhiệm công dân thiêng liêng cao cả nhất của thế hệ trẻ học sinh hiện nay trong sự nghiệp bảo vệ chủ quyền biển đảo thiêng liêng của Tổ quốc là gì?
+ [Không ngừng học tập nâng cao tri thức, rèn luyện bản lĩnh chính trị, nắm vững luật pháp quốc tế và tuyên truyền bảo vệ chủ quyền biên giới hải đảo.] -> task_lichsu_023_success
+ [Tự ý kích động biểu tình bạo lực trên mạng xã hội.] -> task_lichsu_023_fail
+ [Thờ ơ không quan tâm đến các vấn đề chủ quyền đất nước.] -> task_lichsu_023_fail
+ [Chỉ tập trung vào lợi ích cá nhân.] -> task_lichsu_023_fail

=== task_lichsu_023_success ===
Đúng vậy! Tri thức và bản lĩnh là vũ khí sắc bén nhất của các bạn.
-> task_lichsu_024

=== task_lichsu_023_fail ===
Sai rồi. Hành động của tuổi trẻ cần phải đúng pháp luật và có trách nhiệm.
+ [Thử lại] -> task_lichsu_023

=== task_lichsu_024 ===
Xu thế phát triển chung của thế giới ngày nay sau Chiến tranh Lạnh là gì?
+ [Hòa bình, hữu nghị, hợp tác cùng phát triển và lấy phát triển kinh tế làm trọng tâm.] -> task_lichsu_024_success
+ [Chạy đua vũ trang hạt nhân chuẩn bị thế chiến.] -> task_lichsu_024_fail
+ [Phân chia thế giới thành các phe khối quân sự đối đầu nghẹt thở.] -> task_lichsu_024_fail
+ [Áp đặt trừng phạt đơn phương và bế quan tỏa cảng.] -> task_lichsu_024_fail

=== task_lichsu_024_success ===
Chính xác! Hòa bình và phát triển kinh tế là xu thế chủ đạo.
-> location_quang_truong_ba_dinh

=== task_lichsu_024_fail ===
Sai rồi. Hãy nhìn vào xu thế hội nhập kinh tế toàn cầu hiện nay.
+ [Thử lại] -> task_lichsu_024

=== location_quang_truong_ba_dinh ===
Bạn đang đứng giữa Quảng trường Ba Đình lịch sử, nơi Bác Hồ đã đọc bản Tuyên ngôn Độc lập.
+ [Tìm hiểu về ngày khai sinh nước Việt Nam mới] -> task_lichsu_016

=== task_lichsu_016 ===
Khẩu hiệu hành động xuyên suốt của nhân dân ta trong giai đoạn Toàn quốc kháng chiến chống thực dân Pháp (1946) là:
+ ['Quyết tử để Tổ quốc quyết sinh'.] -> task_lichsu_016_success
+ ['Không có gì quý hơn độc lập, tự do'.] -> task_lichsu_016_fail
+ ['Tất cả cho tiền tuyến, tất cả để đánh thắng giặc Mỹ xâm lược'.] -> task_lichsu_016_fail
+ ['Độc lập hay là chết'.] -> task_lichsu_016_fail

=== task_lichsu_016_success ===
Đúng! Tinh thần quyết tử đã bảo vệ nền độc lập non trẻ.
-> task_lichsu_021

=== task_lichsu_016_fail ===
Sai rồi. Hãy nhớ đến lời thề của Trung đoàn Thủ đô năm 1946.
+ [Thử lại] -> task_lichsu_016

=== task_lichsu_021 ===
Kì họp thứ nhất Quốc hội khóa VI (tháng 6 - 7/1976) đã hoàn thành nhiệm vụ lịch sử to lớn nào sau ngày giải phóng?
+ [Thống nhất đất nước về mặt nhà nước, đặt tên nước là Cộng hòa Xã hội Chủ nghĩa Việt Nam, Thủ đô là Hà Nội.] -> task_lichsu_021_success
+ [Kì hiệp ước liên minh phòng thủ quân sự Đông Dương.] -> task_lichsu_021_fail
+ [Ban hành Hiến pháp năm 1992.] -> task_lichsu_021_fail
+ [Bắt đầu thực hiện công cuộc Đổi mới.] -> task_lichsu_021_fail

=== task_lichsu_021_success ===
Chính xác! Đây là mốc son thống nhất đất nước về mặt Nhà nước.
-> task_lichsu_022

=== task_lichsu_021_fail ===
Sai rồi. Sau năm 1975, nhiệm vụ cấp thiết nhất là thống nhất hai miền về mặt Nhà nước.
+ [Thử lại] -> task_lichsu_021

=== task_lichsu_022 ===
Tuyên ngôn Độc lập ngày 2/9/1945 trích dẫn câu mở đầu trong bản Tuyên ngôn Độc lập năm 1776 của nước nào và Tuyên ngôn Nhân quyền, Dân quyền năm 1789 của nước nào?
+ [Nước Mỹ và nước Pháp.] -> task_lichsu_022_success
+ [Nước Anh và nước Nga.] -> task_lichsu_022_fail
+ [Nước Đức và nước Ý.] -> task_lichsu_022_fail
+ [Nước Trung Quốc và Ấn Độ.] -> task_lichsu_022_fail

=== task_lichsu_022_success ===
Đúng vậy! Bác Hồ đã khéo léo sử dụng những giá trị tiến bộ của nhân loại để khẳng định quyền độc lập của Việt Nam.
-> location_hoi_truong_thong_nhat

=== task_lichsu_022_fail ===
Sai rồi. Hãy nhớ lại những bản tuyên ngôn nổi tiếng của phương Tây mà Bác đã trích dẫn.
+ [Thử lại] -> task_lichsu_022

=== location_hoi_truong_thong_nhat ===
Điểm dừng chân cuối cùng là Hội trường Thống nhất, nơi chứng kiến sự chuyển mình của đất nước trong thời kỳ Đổi mới.
+ [Tìm hiểu về công cuộc Đổi mới] -> task_lichsu_009

=== task_lichsu_009 ===
Đại hội đại biểu toàn quốc lần thứ VI của Đảng Cộng sản Việt Nam (tháng 12/1986) đã đề ra đường lối có tính bước ngoặt lịch sử nào?
+ [Đường lối Đổi mới toàn diện đất nước, trọng tâm là đổi mới kinh tế.] -> task_lichsu_009_success
+ [Đường lối công nghiệp hóa ưu tiên phát triển công nghiệp nặng.] -> task_lichsu_009_fail
+ [Chủ trương đóng cửa kinh tế để tự cung tự cấp.] -> task_lichsu_009_fail
+ [Chuyển ngay lập tức sang kinh tế thị trường tự do hoàn toàn không có sự quản lí của Nhà nước.] -> task_lichsu_009_fail

=== task_lichsu_009_success ===
Chính xác! Đại hội VI là đại hội của Đổi mới.
-> task_lichsu_010

=== task_lichsu_009_fail ===
Sai rồi. Năm 1986 là cột mốc khởi đầu cho quá trình Đổi mới toàn diện.
+ [Thử lại] -> task_lichsu_009

=== task_lichsu_010 ===
Một trong những nội dung cốt lõi của đổi mới kinh tế ở Việt Nam từ năm 1986 đến nay là gì?
+ [Xóa bỏ cơ chế tập trung quan liêu bao cấp, phát triển nền kinh tế thị trường định hướng xã hội chủ nghĩa nhiều thành phần.] -> task_lichsu_010_success
+ [Quốc hữu hóa toàn bộ các xí nghiệp tư nhân và cơ sở kinh doanh cá thể.] -> task_lichsu_010_fail
+ [Chỉ phát triển duy nhất kinh tế quốc doanh và tập thể.] -> task_lichsu_010_fail
+ [Dừng mọi hoạt động xuất khẩu lương thực ra thế giới.] -> task_lichsu_010_fail

=== task_lichsu_010_success ===
Đúng vậy! Việc chuyển sang kinh tế nhiều thành phần đã tạo động lực lớn cho đất nước.
-> task_lichsu_011

=== task_lichsu_010_fail ===
Sai rồi. Chúng ta đã xóa bỏ bao cấp để chuyển sang kinh tế thị trường.
+ [Thử lại] -> task_lichsu_010

=== task_lichsu_011 ===
Ba chương trình kinh tế lớn được Đại hội VI của Đảng (1986) xác định tập trung thực hiện là:
+ [Lương thực - thực phẩm, hàng tiêu dùng và hàng xuất khẩu.] -> task_lichsu_011_success
+ [Năng lượng, luyện kim và cơ khí chế tạo.] -> task_lichsu_011_fail
+ [Giao thông vận tải, bưu chính viễn thông và du lịch.] -> task_lichsu_011_fail
+ [Công nghệ cao, hóa dược và đóng tàu biển.] -> task_lichsu_011_fail

=== task_lichsu_011_success ===
Chính xác! Đây là những ưu tiên hàng đầu để ổn định đời sống nhân dân lúc bấy giờ.
-> task_lichsu_012

=== task_lichsu_011_fail ===
Chưa đúng. Hãy nhớ lại ba chương trình trọng điểm nhằm giải quyết khó khăn kinh tế sau chiến tranh.
+ [Thử lại] -> task_lichsu_011

=== task_lichsu_012 ===
Chính sách đối ngoại nhất quán của Đảng và Nhà nước ta trong công cuộc Đổi mới và hội nhập quốc tế là:
+ [Độc lập, tự chủ, hòa bình, hữu nghị, hợp tác và phát triển; đa phương hóa, đa dạng hóa quan hệ đối ngoại.] -> task_lichsu_012_success
+ [Chỉ liên minh quân sự chặt chẽ với một cường quốc duy nhất.] -> task_lichsu_012_fail
+ [Không quan hệ ngoại giao với các nước có chế độ chính trị khác biệt.] -> task_lichsu_012_fail
+ [Ưu tiên đối đầu quân sự để giải quyết tranh chấp biên giới.] -> task_lichsu_012_fail

=== task_lichsu_012_success ===
Rất tốt! Việt Nam muốn làm bạn với tất cả các nước.
-> task_lichsu_013

=== task_lichsu_012_fail ===
Sai rồi. Việt Nam luôn kiên trì chính sách đa phương hóa, đa dạng hóa.
+ [Thử lại] -> task_lichsu_012

=== task_lichsu_013 ===
Đến nay, Việt Nam đã thiết lập quan hệ ngoại giao với gần 200 quốc gia và nâng cấp quan hệ lên Đối tác Chiến lược Toàn diện với các cường quốc hàng đầu thế giới gồm:
+ [Trung Quốc, Nga, Ấn Độ, Hàn Quốc, Hoa Kỳ, Nhật Bản, Australia, Pháp...] -> task_lichsu_013_success
+ [Chỉ duy nhất có 2 nước láng giềng.] -> task_lichsu_013_fail
+ [Chỉ các quốc gia thuộc châu Âu.] -> task_lichsu_013_fail
+ [Chỉ các nước trong khối xã hội chủ nghĩa trước đây.] -> task_lichsu_013_fail

=== task_lichsu_013_success ===
Chính xác! Vị thế của Việt Nam trên trường quốc tế ngày càng được khẳng định.
-> task_lichsu_014

=== task_lichsu_013_fail ===
Sai rồi. Danh sách các đối tác chiến lược toàn diện của chúng ta ngày càng mở rộng với nhiều cường quốc.
+ [Thử lại] -> task_lichsu_013

=== task_lichsu_014 ===
Năm 2007, Việt Nam chính thức trở thành thành viên thứ 150 của tổ chức kinh tế toàn cầu nào?
+ [Tổ chức Thương mại Thế giới (WTO).] -> task_lichsu_014_success
+ [Quỹ Tiền tệ Quốc tế (IMF).] -> task_lichsu_014_fail
+ [Ngân hàng Thế giới (WB).] -> task_lichsu_014_fail
+ [Tổ chức Hợp tác và Phát triển Kinh tế (OECD).] -> task_lichsu_014_fail

=== task_lichsu_014_success ===
Đúng vậy! Gia nhập WTO là bước tiến lớn trong hội nhập kinh tế quốc tế.
-> task_lichsu_015

=== task_lichsu_014_fail ===
Sai rồi. Hãy nhớ đến tổ chức thương mại lớn nhất thế giới.
+ [Thử lại] -> task_lichsu_014

=== task_lichsu_015 ===
Chiến lược 'Ngoại giao Cây tre' của Việt Nam mang đặc trưng nổi bật nào sau đây?
+ [Gốc vững, thân chắc, cành uyển chuyển; kiên định về nguyên tắc, linh hoạt về sách lược.] -> task_lichsu_015_success
+ [Dễ dàng ngả nghiêng theo lợi ích trước mắt của các nước lớn.] -> task_lichsu_015_fail
+ [Cứng nhắc không bao giờ đàm phán thỏa hiệp.] -> task_lichsu_015_fail
+ [Xa lánh các diễn đàn đa phương khu vực.] -> task_lichsu_015_fail

=== task_lichsu_015_success ===
Tuyệt vời! Bạn đã hoàn thành xuất sắc hành trình lịch sử. "Ngoại giao Cây tre" chính là bản sắc độc đáo của Việt Nam.
-> end_game

=== task_lichsu_015_fail ===
Rất tiếc, đó chưa phải là đặc trưng của "Ngoại giao Cây tre". Hãy nhớ đến hình ảnh cây tre Việt Nam: "Gốc vững, thân chắc, cành uyển chuyển".
+ [Thử lại] -> task_lichsu_015

=== end_game ===
Chúc mừng bạn đã hoàn thành chuyến hành trình xuyên suốt lịch sử dân tộc và thế giới. Hy vọng những kiến thức này sẽ giúp bạn thêm yêu và tự hào về đất nước mình!
-> END