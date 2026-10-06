-> start_knot

=== start_knot ===
Bạn đang đứng trong phòng thí nghiệm vật lý, ánh sáng lấp ló qua các khe hở. Trên bàn là những thiết bị thí nghiệm, sách vở và tài liệu học liệu. Hãy bắt đầu bằng việc trả lời các câu hỏi để khám phá bí mật của vật lý!
-> task_vatly_001

=== task_vatly_001 ===
Trong thí nghiệm Y-âng về giao thoa với ánh sáng đơn sắc có bước sóng , khoảng cách giữa hai khe hẹp là a, khoảng cách từ hai khe đến màn quan sát là D. Trên màn, tính từ vị trí vân sáng trung tâm, vị trí vân tối được xác định bằng công thức nào sau đây?
+ [(k + 1/5) * (Dλ/a); k = 0, ±1, ±2,...]  -> task_vatly_001_fail
+ [(k + 1/2) * (Dλ/a); k = 0, ±1, ±2,...]  -> task_vatly_001_success
+ [k * (Dλ/a); k = 0, ±1, ±2,...]  -> task_vatly_001_fail
+ [(k + 1/3) * (Dλ/a); k = 0, ±1, ±2,...]  -> task_vatly_001_fail

=== task_vatly_001_success ===
Chính xác! Vị trí vân tối được xác định bằng công thức (k + 1/2) * (Dλ/a).
-> task_vatly_002

=== task_vatly_001_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_001

=== task_vatly_002 ===
Đặt điện áp xoay chiều vào hai đầu đoạn mạch gồm điện trở R, cuộn cảm thuần và tụ điện mắc nối tiếp thì cảm kháng và dung kháng của đoạn mạch lần lượt là Z_L và Z_C. Tổng trở Z của đoạn mạch được tính bằng công thức nào sau đây?
+ [Z = sqrt(Z_L + Z_C + R^2)]  -> task_vatly_002_fail
+ [Z = sqrt(R^2 + Z_L + Z_C)]  -> task_vatly_002_fail
+ Z = sqrt(R^2 + Z_L - Z_C) -> task_vatly_002_success
+ Z = sqrt(R^2 + Z_C - Z_L) -> task_vatly_002_fail

=== task_vatly_002_success ===
Chính xác! Tổng trở Z được tính bằng công thức sqrt(R^2 + Z_L - Z_C).
-> task_vatly_003

=== task_vatly_002_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_002

=== task_vatly_003 ===
Một con lắc đơn đang dao động điều hòa với tần số góc ω, biên độ s_0 và pha ban đầu là φ. Phương trình dao động của con lắc là
+ [s = s_0 cos(ωt + φ)]  -> task_vatly_003_success
+ [s = s_0 cos(φ + ωt)]  -> task_vatly_003_fail
+ [s = s_0 cos(ωt + φ)]  -> task_vatly_003_fail
+ [s = s_0 cos(ωt + φ)]  -> task_vatly_003_fail

=== task_vatly_003_success ===
Chính xác! Phương trình dao động là s = s_0 cos(ωt + φ).
-> task_vatly_004

=== task_vatly_003_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_003

=== task_vatly_004 ===
Một máy biến áp lí tưởng có số vòng dây của cuộn sơ cấp và số vòng dây của cuộn thứ cấp lần lượt là N_1 và N_2. Đặt điện áp xoay chiều có giá trị hiệu dụng U_1 vào hai đầu cuộn sơ cấp thì điện áp hiệu dụng giữa hai đầu cuộn thứ cấp ở chế độ không tải là U_2. Công thức nào sau đây đúng?
+ [U_2/U_1 = N_2/N_1]  -> task_vatly_004_fail
+ [U_2/U_1 = N_1/N_2]  -> task_vatly_004_fail
+ [U_2/U_1 = N_1/N_2]  -> task_vatly_004_fail
+ [U_2/U_1 = N_2/N_1]  -> task_vatly_004_success

=== task_vatly_004_success ===
Chính xác! Công thức đúng là U_2/U_1 = N_2/N_1.
-> task_vatly_005

=== task_vatly_004_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_004

=== task_vatly_005 ===
Vật (chất) nào sau đây không dẫn điện?
+ [Cao su]  -> task_vatly_005_success
+ [Kim loại đồng]  -> task_vatly_005_fail
+ [Dung dịch muối NaCl trong nước]  -> task_vatly_005_fail
+ [Dung dịch axit HCl trong nước]  -> task_vatly_005_fail

=== task_vatly_005_success ===
Chính xác! Cao su là vật liệu cách điện.
-> task_vatly_006

=== task_vatly_005_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_005

=== task_vatly_006 ===
Quang phổ liên tục
+ [gồm các vạch màu riêng lẻ, ngăn cách nhau bằng những khoảng tối.]  -> task_vatly_006_fail
+ [gồm các vân sáng và tối xen kẽ, song song và cách đều nhau.]  -> task_vatly_006_fail
+ [do các chất rắn, chất lỏng hoặc chất khí có áp suất lớn, phát ra khi bị nung nóng.]  -> task_vatly_006_success
+ [do các chất khí hoặc hơi ở áp suất thấp phát ra khi bị kích thích.]  -> task_vatly_006_fail

=== task_vatly_006_success ===
Chính xác! Quang phổ liên tục do các chất rắn, chất lỏng hoặc chất khí có áp suất lớn phát ra khi bị nung nóng.
-> task_vatly_007

=== task_vatly_006_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_006

=== task_vatly_007 ===
Một sóng âm có chu kì T. Tần số f của sóng được tính bằng công thức nào sau đây?
+ [f = T/π]  -> task_vatly_007_fail
+ [f = 2π/T]  -> task_vatly_007_fail
+ [f = 2/T]  -> task_vatly_007_fail
+ [f = 1/T]  -> task_vatly_007_success

=== task_vatly_007_success ===
Chính xác! Tần số f = 1/T.
-> task_vatly_008

=== task_vatly_007_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_007

=== task_vatly_008 ===
Trong mọi phản ứng hạt nhân, luôn có bảo toàn
+ [số nuclôn]  -> task_vatly_008_success
+ [khối lượng nghỉ]  -> task_vatly_008_fail
+ [động năng]  -> task_vatly_008_fail
+ [số nơtron]  -> task_vatly_008_fail

=== task_vatly_008_success ===
Chính xác! Số nuclôn luôn được bảo toàn trong mọi phản ứng hạt nhân.
-> task_vatly_009

=== task_vatly_008_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_008

=== task_vatly_009 ===
Đại lượng nào sau đây của sóng luôn có giá trị bằng quãng đường mà sóng truyền được trong một chu kỳ?
+ [Biên độ của sóng]  -> task_vatly_009_fail
+ [Tần số của sóng]  -> task_vatly_009_fail
+ [Tốc độ truyền sóng]  -> task_vatly_009_fail
+ [Bước sóng]  -> task_vatly_009_success

=== task_vatly_009_success ===
Chính xác! Bước sóng là quãng đường sóng truyền được trong một chu kỳ.
-> task_vatly_010

=== task_vatly_009_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_009

=== task_vatly_010 ===
Tia tử ngoại có cùng bản chất với
+ [tia α]  -> task_vatly_010_fail
+ [tia β−]  -> task_vatly_010_fail
+ [tia X]  -> task_vatly_010_success
+ [tia β+]  -> task_vatly_010_fail

=== task_vatly_010_success ===
Chính xác! Tia tử ngoại có cùng bản chất với tia X.
-> act_2_start

=== act_2_start ===

Bạn đã vượt qua màn đầu tiên! Bây giờ, hãy bước vào thư viện học liệu để khám phá những câu hỏi vật lý đầy thử thách. Hãy chọn một câu hỏi để bắt đầu.
-> task_vatly_011

=== task_vatly_011 ===
Trên một sợi dây đàn hồi đang có sóng dừng, bụng sóng là các điểm luôn dao động
+ ["nhỏ nhất"]  -> task_vatly_011_fail
+ ["lớn nhất"]  -> task_vatly_011_success
+ ["bằng một bước sóng"]  -> task_vatly_011_fail
+ ["bằng một nữa bước sóng"]  -> task_vatly_011_fail

=== task_vatly_011_success ===
Chính xác! Bụng sóng là nơi dao động mạnh nhất.
-> task_vatly_012

=== task_vatly_011_fail ===
Sai rồi! Hãy suy nghĩ lại về đặc điểm của bụng sóng.
+ [Thử lại câu hỏi này] -> task_vatly_011

=== task_vatly_012 ===
Trong sơ đồ khối của máy thu thanh đơn giản không có bộ phận nào sau đây?
+ ["Anten thu"]  -> task_vatly_012_fail
+ ["Loa"]  -> task_vatly_012_fail
+ ["Mạch tách sóng"]  -> task_vatly_012_fail
+ ["Mạch biến điệu"]  -> task_vatly_012_success

=== task_vatly_012_success ===
Chính xác! Máy thu thanh không cần mạch biến điệu.
-> task_vatly_013

=== task_vatly_012_fail ===
Sai rồi! Hãy kiểm tra lại các bộ phận của máy thu thanh.
+ [Thử lại câu hỏi này] -> task_vatly_012

=== task_vatly_013 ===
Dòng điện không đổi có cường độ I chạy qua điện trở R. Công suất tỏa nhiệt trên R là:
+ ["P = RI²"]  -> task_vatly_013_success
+ ["P = RI"]  -> task_vatly_013_fail
+ ["P = I/R"]  -> task_vatly_013_fail
+ ["P = Rl²"]  -> task_vatly_013_fail

=== task_vatly_013_success ===
Chính xác! Công thức tính công suất tỏa nhiệt là P = RI².
-> task_vatly_014

=== task_vatly_013_fail ===
Sai rồi! Hãy nhớ lại công thức công suất trong mạch điện.
+ [Thử lại câu hỏi này] -> task_vatly_013

=== task_vatly_014 ===
Biết h là hằng số Plăng. Theo giả thuyết Plăng thì lượng năng lượng mà mỗi lần một nguyên tử hay phân tử hấp thụ hay phát xạ ánh sáng đơn sắc có tần số f là
+ ["4hf"]  -> task_vatly_014_fail
+ ["hf"]  -> task_vatly_014_success
+ ["3hf"]  -> task_vatly_014_fail
+ ["2hf"]  -> task_vatly_014_fail

=== task_vatly_014_success ===
Chính xác! Theo giả thuyết Plăng, năng lượng là hf.
-> task_vatly_015

=== task_vatly_014_fail ===
Sai rồi! Hãy xem lại giả thuyết Plăng về năng lượng ánh sáng.
+ [Thử lại câu hỏi này] -> task_vatly_014

=== task_vatly_015 ===
Dao động cưỡng bức có
+ ["tần số nhỏ hơn tần số của lực cưỡng bức"]  -> task_vatly_015_fail
+ ["biên độ giảm dần theo thời gian"]  -> task_vatly_015_fail
+ ["biên độ không đổi theo thời gian"]  -> task_vatly_015_success
+ ["tần số nhỏ hơn tần số của lực cưỡng bức"]  -> task_vatly_015_fail

=== task_vatly_015_success ===
Chính xác! Dao động cưỡng bức có biên độ không đổi.
-> task_vatly_016

=== task_vatly_015_fail ===
Sai rồi! Hãy nhớ lại đặc điểm của dao động cưỡng bức.
+ [Thử lại câu hỏi này] -> task_vatly_015

=== task_vatly_016 ===
Đặt điện áp xoay chiều vào hai đầu đoạn mạch gồm điện trở R, cuộn cảm thuần và tụ điện mắc nối tiếp thì tổng trở của đoạn mạch là Z. Hệ số công suất (cos φ) của đoạn mạch được tính bằng công thức nào sau đây?
+ ["cos φ = R/Z"]  -> task_vatly_016_success
+ ["cos φ = R/Z²"]  -> task_vatly_016_fail
+ ["cos φ = R/Z"]  -> task_vatly_016_success
+ ["cos φ = R²/Z"]  -> task_vatly_016_fail

=== task_vatly_016_success ===
Chính xác! Hệ số công suất là R/Z.
-> task_vatly_017

=== task_vatly_016_fail ===
Sai rồi! Hãy kiểm tra lại công thức tính hệ số công suất.
+ [Thử lại câu hỏi này] -> task_vatly_016

=== task_vatly_017 ===
Tia α là dòng các
+ ["hạt pôzitron"]  -> task_vatly_017_fail
+ ["hạt nhân ^4_2He"]  -> task_vatly_017_success
+ ["hạt notron"]  -> task_vatly_017_fail
+ ["hạt êlectron"]  -> task_vatly_017_fail

=== task_vatly_017_success ===
Chính xác! Tia α là dòng các hạt nhân helium.
-> task_vatly_018

=== task_vatly_017_fail ===
Sai rồi! Hãy xem lại đặc điểm của tia α.
+ [Thử lại câu hỏi này] -> task_vatly_017

=== task_vatly_018 ===
Khi nói về hạt tải điện trong các môi trường, phát biểu nào sau đây sai?
+ ["Hạt tải điện trong kim loại là các êlectron tự do."]  -> task_vatly_018_fail
+ ["Hạt tải điện trong chất bán dẫn là các êlectron tự do và lỗ trống."]  -> task_vatly_018_fail
+ ["Hạt tải điện trong chất điện phân là các ion dương và ion âm."]  -> task_vatly_018_fail
+ ["Hạt tải điện trong chất khí là các lỗ trống."]  -> task_vatly_018_success

=== task_vatly_018_success ===
Chính xác! Hạt tải điện trong chất khí là các ion và êlectron, không phải lỗ trống.
-> task_vatly_019

=== task_vatly_018_fail ===
Sai rồi! Hãy kiểm tra lại phát biểu về hạt tải điện trong chất khí.
+ [Thử lại câu hỏi này] -> task_vatly_018

=== task_vatly_019 ===
Một con lắc lò xo gồm lò xo và vật nhỏ đang dao động điều hòa. Lực kéo về tác dụng lên vật luôn
+ ["cùng chiều với chiều chuyển động của vật"]  -> task_vatly_019_fail
+ ["hướng ra xa vị trí cân bằng"]  -> task_vatly_019_fail
+ ["hướng về vị trí cân bằng"]  -> task_vatly_019_success
+ ["ngược chiều với chiều chuyển động của vật"]  -> task_vatly_019_fail

=== task_vatly_019_success ===
Chính xác! Lực kéo về luôn hướng về vị trí cân bằng.
-> task_vatly_020

=== task_vatly_019_fail ===
Sai rồi! Hãy nhớ lại định luật Hooke trong dao động điều hòa.
+ [Thử lại câu hỏi này] -> task_vatly_019

=== task_vatly_020 ===
Một dòng điện xoay chiều có cường độ dòng điện i = I_0 cos(ωt + φ) với I_0 > 0. Đại lượng I_0 được gọi là
+ ["cường độ dòng điện hiệu dụng"]  -> task_vatly_020_fail
+ ["tần số góc của dòng điện"]  -> task_vatly_020_fail
+ ["pha ban đầu của dòng điện"]  -> task_vatly_020_fail
+ ["cường độ dòng điện cực đại"]  -> task_vatly_020_success

=== task_vatly_020_success ===
Chính xác! I_0 là cường độ dòng điện cực đại.
-> act_3_start

=== task_vatly_020_fail ===
Sai rồi! Hãy xem lại các đại lượng trong phương trình dòng điện xoay chiều.
+ [Thử lại câu hỏi này] -> task_vatly_020

=== act_3_start ===

Chào mừng bạn đến với Hồi 3 - Khu Vực Thử Thách Vật Lý! Bạn đã sẵn sàng để vượt qua những câu hỏi khó nhất chưa? Hãy bắt đầu ngay!
-> task_vatly_021

=== task_vatly_021 ===
Cho hai dao động điều hòa cùng phương, cùng tần số có biên độ là A_1 và A_2. Biên độ dao động tổng hợp của hai dao động này có thể nhận giá trị lớn nhất là
+ [A = A_1 - A_2] -> task_vatly_021_fail
+ [A = A_2] -> task_vatly_021_fail
+ [A = A_1 + A_2] -> task_vatly_021_fail
+ [A = A_1] -> task_vatly_021_success

=== task_vatly_021_success ===
Chính xác!
-> task_vatly_022

=== task_vatly_021_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_021

=== task_vatly_022 ===
Khi nói về tia laze, phát biểu nào sau đây sai?
+ [Tia laze là chùm sáng có cường độ lớn.] -> task_vatly_022_fail
+ [Tia laze là chùm ánh sáng trắng hội tụ.] -> task_vatly_022_success
+ [Tia laze có tính kết hợp cao.] -> task_vatly_022_fail
+ [Tia laze có tính định hướng cao.] -> task_vatly_022_fail

=== task_vatly_022_success ===
Chính xác!
-> task_vatly_023

=== task_vatly_022_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_022

=== task_vatly_023 ===
Âm có tần số nào sau đây là siêu âm?
+ [5 Hz] -> task_vatly_023_fail
+ [30000 Hz] -> task_vatly_023_success
+ [5000 Hz] -> task_vatly_023_fail
+ [10 Hz] -> task_vatly_023_fail

=== task_vatly_023_success ===
Chính xác!
-> task_vatly_024

=== task_vatly_023_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_023

=== task_vatly_024 ===
Một đoạn dây dẫn uốn thành một vòng tròn tâm O, bán kính 5,8 cm. Khi cho dòng điện không đổi có cường độ I chạy trong vòng dây thì dòng điện này gây ra tại O cảm ứng từ có độ lớn 2,6.10^\{-5\} T. Giá trị của I là
+ [3,8 A] -> task_vatly_024_fail
+ [7,5 A] -> task_vatly_024_fail
+ [2,4 A] -> task_vatly_024_success
+ [1,2 A] -> task_vatly_024_fail

=== task_vatly_024_success ===
Chính xác!
-> task_vatly_025

=== task_vatly_024_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_024

=== task_vatly_025 ===
Trong chân không, một nguồn phát ra ánh sáng đơn sắc có bước sóng 660 nm. Lấy h = 6,625.10^\{-34\} J.s; c = 3.10^8 m/s và 1 eV = 1,6.10^\{-19\} J. Mỗi phôtôn của ánh sáng này mang năng lượng
+ [5,33 eV] -> task_vatly_025_fail
+ [4,80 eV] -> task_vatly_025_fail
+ [3,00 eV] -> task_vatly_025_fail
+ [1,88 eV] -> task_vatly_025_success

=== task_vatly_025_success ===
Chính xác!
-> task_vatly_026

=== task_vatly_025_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_025

=== task_vatly_026 ===
Trong thí nghiệm Y-âng về giao thoa với ánh sáng đơn sắc có bước sóng λ, khoảng cách giữa hai khe hẹp là 1,0 mm, khoảng cách từ hai khe đến màn quan sát là 1,5 m. Trên màn, khoảng vân đo được là 1,05 mm. Giá trị của λ là
+ [0,5 μm] -> task_vatly_026_fail
+ [0,4 μm] -> task_vatly_026_fail
+ [0,7 μm] -> task_vatly_026_fail
+ [0,6 μm] -> task_vatly_026_success

=== task_vatly_026_success ===
Chính xác!
-> task_vatly_027

=== task_vatly_026_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_026

=== task_vatly_027 ===
Đặt điện áp xoay chiều có tần số 50 Hz vào hai đầu cuộn cảm thuần có độ tự cảm 0,2 H. Cảm kháng của cuộn cảm có giá trị là
+ [10 Ω] -> task_vatly_027_fail
+ [20√2 Ω] -> task_vatly_027_fail
+ [10√2 Ω] -> task_vatly_027_fail
+ [20 Ω] -> task_vatly_027_success

=== task_vatly_027_success ===
Chính xác!
-> task_vatly_028

=== task_vatly_027_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_027

=== task_vatly_028 ===
Một con lắc đơn có chiều dài 1,00 m, dao động điều hòa tại nơi có g = 9,80 m/s². Tần số góc dao động của con lắc là
+ [9,80 rad/s] -> task_vatly_028_fail
+ [3,13 rad/s] -> task_vatly_028_success
+ [0,498 rad/s] -> task_vatly_028_fail
+ [0,319 rad/s] -> task_vatly_028_fail

=== task_vatly_028_success ===
Chính xác!
-> task_vatly_029

=== task_vatly_028_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_028

=== task_vatly_029 ===
Một mạch dao động lí tưởng có tần số dao động riêng là 2,0 MHz. Chu kì dao động riêng của mạch là
+ [0,5 s] -> task_vatly_029_fail
+ [2,0 s] -> task_vatly_029_fail
+ [2,0 μs] -> task_vatly_029_fail
+ [0,5 μs] -> task_vatly_029_success

=== task_vatly_029_success ===
Chính xác!
-> task_vatly_030

=== task_vatly_029_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_029

=== task_vatly_030 ===
Số nuclôn không mang điện có trong một hạt nhân ^\{222\}_\{86\}Rn là
+ [222] -> task_vatly_030_fail
+ [86] -> task_vatly_030_fail
+ [308] -> task_vatly_030_fail
+ [136] -> task_vatly_030_success

=== task_vatly_030_success ===
Chính xác!
-> act_4_start

=== task_vatly_030_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_vatly_030

=== act_4_start ===
Chúc mừng bạn đã hoàn thành Hồi 3! Bạn đã vượt qua thử thách vật lý đầy thử thách. Hãy chuẩn bị tinh thần cho Hồi 4 - Khu Vực Mới đang chờ bạn khám phá!
-> task_vatly_031

=== task_vatly_031 ===
Một con lắc đơn có chiều dài 81 cm đang dao động điều hòa với biên độ góc 8° tại nơi có g = 9,87 m/s². Chọn t = 0 khi vật nhỏ của con lắc đi qua vị trí cân bằng theo chiều âm. Tính từ t = 0, vật đi qua vị trí có li độ góc 4° lần thứ 25 ở thời điểm  
+ [21,75 s]  -> task_vatly_031_fail
+ [10,95 s]  -> task_vatly_031_fail
+ [22,65 s]  -> task_vatly_031_fail
+ [11,85 s]  -> task_vatly_031_success

=== task_vatly_031_success ===
Chính xác!  
-> task_vatly_032

=== task_vatly_031_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_031

=== task_vatly_032 ===
Đặt điện áp u_\{AB\} = 120√2 cos(100πt + π/6) (V) vào hai đầu đoạn mạch AB như hình bên. Biết điện trở R = 50 Ω, tụ điện có C = 200/π μF, cuộn cảm thuần có độ tự cảm L thay đổi được. Điều chỉnh L để điện áp hiệu dụng giữa hai đầu đoạn mạch AN đạt cực đại. Khi đó, điện áp giữa hai đầu tụ điện có biểu thức là  
+ u_C = 120 cos(100πt - π/2) (V) -> task_vatly_032_fail
+ u_C = 120√2 cos(100πt - π/3) (V) -> task_vatly_032_fail
+ u_C = 120√2 cos(100πt - π/2) (V) -> task_vatly_032_success
+ u_C = 120 cos(100πt - π/3) (V) -> task_vatly_032_fail

=== task_vatly_032_success ===
Chính xác!  
-> task_vatly_033

=== task_vatly_032_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_032

=== task_vatly_033 ===
Đặt điện áp u = 200√2 cos(100πt) (V) vào hai đầu đoạn mạch gồm điện trở, cuộn cảm thuần có độ tự cảm 2/π H và tụ điện có điện dung 100/π μF mắc nối tiếp. Biết điện áp giữa hai đầu đoạn mạch lệch pha π/6 so với cường độ dòng điện trong đoạn mạch. Cường độ dòng điện hiệu dụng trong đoạn mạch là  
+ [2 A]  -> task_vatly_033_fail
+ [1 A]  -> task_vatly_033_success
+ [2√2 A]  -> task_vatly_033_fail
+ [2 A]  -> task_vatly_033_fail

=== task_vatly_033_success ===
Chính xác!  
-> task_vatly_034

=== task_vatly_033_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_033

=== task_vatly_034 ===
Một sợi dây căng ngang có hai đầu A và B cố định. M là một điểm trên dây với MA = 20 cm. Trên dây có sóng dừng. Điểm N trên dây xa M nhất có biên độ dao động bằng biên độ dao động của M. Biết sóng truyền trên dây có bước sóng là 36 cm và trong khoảng MN có 5 nút sóng. Chiều dài sợi dây là  
+ [117 cm]  -> task_vatly_034_fail
+ [126 cm]  -> task_vatly_034_success
+ [108 cm]  -> task_vatly_034_fail
+ [144 cm]  -> task_vatly_034_fail

=== task_vatly_034_success ===
Chính xác!  
-> task_vatly_035

=== task_vatly_034_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_034

=== task_vatly_035 ===
Một tụ điện có điện dung 45 μF được tích điện bằng nguồn điện một chiều có suất điện động Q. Khi điện tích trên tụ điện ổn định, ngắt tụ điện ra khỏi nguồn rồi nối tụ điện với cuộn cảm thuần có độ tự cảm 2 mH thành mạch dao động lí tưởng. Chọn t = 0 là thời điểm nối tụ điện với cuộn cảm. Tại thời điểm t = 20π ms, cường độ dòng điện qua cuộn cảm có độ lớn là 0,16 A. Giá trị của Q gần nhất với giá trị nào sau đây?  
+ [2,5 V]  -> task_vatly_035_fail
+ [1,0 V]  -> task_vatly_035_fail
+ [1,5 V]  -> task_vatly_035_fail
+ [2,0 V]  -> task_vatly_035_success

=== task_vatly_035_success ===
Chính xác!  
-> task_vatly_036

=== task_vatly_035_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_035

=== task_vatly_036 ===
Đặt điện áp xoay chiều vào hai đầu đoạn mạch AB như hình H1. Hình H2 là đồ thị biểu diễn sự phụ thuộc của điện áp giữa hai đầu đoạn mạch AB, đoạn mạch MN và đoạn mạch NB theo thời gian t. Điều chỉnh tần số của điện áp đến giá trị f_0 thì trong đoạn mạch AB có cộng hưởng điện. Giá trị f_0 gần nhất với giá trị nào sau đây?  
+ [140 Hz]  -> task_vatly_036_fail
+ [120 Hz]  -> task_vatly_036_fail
+ [80 Hz]  -> task_vatly_036_success
+ [100 Hz]  -> task_vatly_036_fail

=== task_vatly_036_success ===
Chính xác!  
-> task_vatly_037

=== task_vatly_036_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_036

=== task_vatly_037 ===
Hạt nhân X là chất phóng xạ phân rã tạo thành hạt nhân Y bền. Ban đầu (t = 0), có một mẫu trong đó chứa cả hạt nhân X và hạt nhân Y. Biết hạt nhân Y sinh ra được giữ lại hoàn toàn trong mẫu. Tại thời điểm t_1, tỉ số giữa số hạt nhân Y trong mẫu và số hạt nhân X còn lại trong mẫu là 1. Tại thời điểm t_2 = 4,2 t_1, tỉ số giữa số hạt nhân Y trong mẫu và số hạt nhân X còn lại trong mẫu là 7. Tỉ số giữa số hạt nhân Y và số hạt nhân X ban đầu là  
+ [0,70]  -> task_vatly_037_fail
+ [0,35]  -> task_vatly_037_fail
+ [0,65]  -> task_vatly_037_fail
+ [0,30]  -> task_vatly_037_success

=== task_vatly_037_success ===
Chính xác!  
-> task_vatly_038

=== task_vatly_037_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_037

=== task_vatly_038 ===
Sử dụng một nguồn ánh sáng trắng và một máy đơn sắc để tạo ra một nguồn sáng đơn sắc với bước sóng có thể thay đổi liên tục từ 390 nm đến 710 nm để dùng trong thí nghiệm Y-âng về giao thoa ánh sáng. Trên màn quan sát, M và N là hai điểm trong đó khoảng cách từ N đến vân sáng trung tâm gấp đôi khoảng cách từ M đến vân sáng trung tâm. Thay đổi từ từ bước sóng của ánh sáng trong thí nghiệm từ 390 nm đến 710 nm, quan sát thấy tại M có hai lần là vị trí của vân sáng và tại N cũng có một số lần là vị trí của vân sáng. Biết một trong hai bức xạ cho vân sáng tại M có bước sóng 480 nm. Xét bước sóng của các bức xạ cho vân sáng tại N, λ_0 là bước sóng ngắn nhất. Giá trị của λ_0 gần nhất với giá trị nào sau đây?  
+ [405 nm]  -> task_vatly_038_fail
+ [425 nm]  -> task_vatly_038_success
+ [415 nm]  -> task_vatly_038_fail
+ [395 nm]  -> task_vatly_038_fail

=== task_vatly_038_success ===
Chính xác!  
-> task_vatly_039

=== task_vatly_038_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_038

=== task_vatly_039 ===
Một con lắc lò xo treo thẳng đứng gồm lò xo nhẹ có độ cứng k = 100 N/m và vật M khối lượng 400 g có dạng một thanh trụ dài. Vật N được lồng bên ngoài vật M như hình bên. Nâng hai vật lên đến vị trí lò xo không biến dạng rồi thả N để N trượt thẳng đứng xuống dọc theo M, sau đó thả nhẹ M. Sau khi thả M một khoảng thời gian 2/15 s thì N rời khỏi M. Biết rằng trước khi rời khỏi M thì N luôn trượt xuống so với M và lực ma sát giữa chúng có độ lớn không đổi và bằng 2 N. Bỏ qua lực cản của không khí. Lấy g = 10 m/s² và π = 10. Sau khi N rời khỏi M, M dao động điều hòa, độ biến dạng cực đại của lò xo là Δl_max. Giá trị Δl_max gần nhất với giá trị nào sau đây?  
+ [10,0 cm]  -> task_vatly_039_fail
+ [12,0 cm]  -> task_vatly_039_success
+ [11,0 cm]  -> task_vatly_039_fail
+ [9,0 cm]  -> task_vatly_039_fail

=== task_vatly_039_success ===
Chính xác!  
-> task_vatly_040

=== task_vatly_039_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_039

=== task_vatly_040 ===
Thực hiện giao thoa sóng trên mặt chất lỏng với hai nguồn kết hợp dao động cùng pha theo phương thẳng đứng. Trên mặt chất lỏng, bốn điểm A, B, C và D tạo thành hình chữ nhật ABCD với AB > BC. Nếu đặt hai nguồn tại A và B thì C và D là vị trí của hai điểm cực tiểu giao thoa và trên đoạn thẳng CD có 7 điểm cực đại giao thoa. Nếu đặt hai nguồn tại B và C thì A và D là vị trí của hai điểm cực tiểu giao thoa và trên đoạn thẳng BC có n điểm cực tiểu giao thoa. Giá trị tối đa mà n có thể nhận là  
+ [20]  -> task_vatly_040_fail
+ [16]  -> task_vatly_040_fail
+ [14]  -> task_vatly_040_fail
+ [18]  -> task_vatly_040_success

=== task_vatly_040_success ===
Chính xác!  
-> END

=== task_vatly_040_fail ===
Sai rồi! Báo động đỏ kêu vang.  
+ [Thử lại câu hỏi này] -> task_vatly_040

=== END ===
Chúc mừng! Bạn đã vượt qua tất cả 10 câu hỏi và giành chiến thắng trong trò chơi!  
Cảm ơn bạn đã tham gia hành trình khám phá vật lý đầy thử thách này. Hẹn gặp lại!

=== task_vatly_010_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_vatly_010
