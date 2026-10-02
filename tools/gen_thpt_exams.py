# -*- coding: utf-8 -*-
"""
gen_thpt_exams.py
Generates comprehensive, standard Word (.docx) exam papers for High School (THPT):
- Grade 10: Lịch sử (Định dạng chuẩn khảo thí mới GDPT 2018)
- Grade 10: Địa lí (Định dạng chuẩn khảo thí mới GDPT 2018)
- Grade 12: Đề thi thử Tốt nghiệp THPT Lịch sử (Chuẩn Đề tham khảo mới của Bộ GD&ĐT)
- Grade 12: Đề thi thử Tốt nghiệp THPT Địa lí (Chuẩn Đề tham khảo mới của Bộ GD&ĐT)
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(__file__))

from exam_builder_base import (
    create_styled_document, add_exam_header, add_section_header,
    add_mcq_question, add_true_false_question, add_exam_footer_mark,
    add_answers_section
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "De_Thi_Lich_Su_Dia_Ly")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# 5. ĐỀ LỚP 10 - LỊCH SỬ (ĐỊNH DẠNG MỚI BGD 2025)
# ==============================================================================
def generate_grade_10_history():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="TRƯỜNG THPT CHUYÊN HÀ NỘI - AMSTERDAM",
        exam_title="ĐỀ KIỂM TRA ĐÁNH GIÁ CUỐI HỌC KÌ I - NĂM HỌC 2025 - 2026",
        subject_title="LỊCH SỬ - KHỐI 10 (CHƯƠNG TRÌNH GDPT 2018 - CẤU TRÚC MỚI)",
        duration_str="50 phút",
        exam_code="105"
    )
    
    add_section_header(doc, "PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (6,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 24. Mỗi câu hỏi thí sinh chỉ chọn một phương án (mỗi câu đúng được 0,25 điểm).")
    
    mcq_items = [
        ("Hiện thực lịch sử là gì?",
         "Tất cả những gì đã diễn ra trong quá khứ, tồn tại hoàn toàn khách quan độc lập với ý muốn con người.",
         "Toàn bộ những nhận thức của con người về những gì đã xảy ra trong quá khứ.",
         "Những câu chuyện cổ tích và thần thoại do nhân dân tưởng tượng ra.",
         "Các văn bản khảo cổ học đã được phiên dịch."),
        ("Nhận thức lịch sử có đặc điểm nào sau đây khác biệt so với hiện thực lịch sử?",
         "Mang tính chủ quan, phụ thuộc vào mục đích nghiên cứu, quan điểm và nguồn tư liệu của người tìm hiểu.",
         "Luôn luôn tồn tại khách quan và không bao giờ biến đổi.",
         "Chính là hiện thực lịch sử nguyên vẹn không sai lệch.",
         "Hoàn toàn không có giá trị đối với đời sống con người."),
        ("Nguồn sử liệu nào sau đây được coi là chứng cứ lịch sử trực tiếp, có giá trị tin cậy cao nhất trong việc phục dựng quá khứ?",
         "Sử liệu hiện vật và tư liệu gốc đương thời.",
         "Truyện truyền thuyết dân gian.",
         "Phim ảnh dã sử hiện đại.",
         "Các tiểu thuyết lịch sử thời kì sau."),
        ("Nhiệm vụ hàng đầu của Sử học là gì?",
         "Khôi phục hiện thực lịch sử một cách chính xác, khách quan và trung thực.",
         "Sáng tạo ra các câu chuyện ly kì để giải trí.",
         "Bảo vệ mọi quan điểm chủ quan của nhà nghiên cứu.",
         "Dự báo chính xác tương lai mà không cần chứng cứ."),
        ("Ngành công nghiệp nào sau đây có mối quan hệ tương hỗ trực tiếp với việc bảo tồn và phát huy giá trị di sản văn hóa lịch sử?",
         "Ngành du lịch văn hóa.",
         "Ngành công nghiệp luyện kim.",
         "Ngành công nghiệp khai khoáng nặng.",
         "Ngành chế biến hóa dầu."),
        ("Cư dân Ai Cập cổ đại đã sáng tạo ra hệ thống chữ viết nào đầu tiên?",
         "Chữ tượng hình khắc trên đá và viết trên giấy pa-pi-rút.",
         "Chữ hình nêm (tiết hình).",
         "Chữ cái La-tinh.",
         "Chữ Phạn (Sanskrit)."),
        ("Công trình kiến trúc vĩ đại nào của Ai Cập cổ đại được xem là kì quan duy nhất trong 7 kì quan thế giới cổ đại còn tồn tại đến ngày nay?",
         "Kim tự tháp Kê-ốp (Giza).",
         "Vườn treo Ba-bi-lon.",
         "Hải đăng A-lếch-xăng-đri-a.",
         "Đền thờ Nữ thần Ác-tê-mít."),
        ("Bộ luật thành văn cổ xưa nhất thế giới được khắc trên cột đá bazan nguyên khối của Lưỡng Hà cổ đại là:",
         "Bộ luật Ham-mu-ra-bi.",
         "Luật Mười hai bảng.",
         "Luật Hồng Đức.",
         "Bộ luật Giu-xti-ni-an."),
        ("Cư dân Lưỡng Hà cổ đại viết chữ hình nêm chủ yếu trên chất liệu gì?",
         "Các phiến đất sét ướt rồi đem nung khô.",
         "Giấy pa-pi-rút làm từ vỏ cây.",
         "Mai rùa và xương thú.",
         "Các phiến lụa tơ tằm."),
        ("Chế độ phân biệt đẳng cấp chủng tính Vác-na của Ấn Độ cổ đại chia xã hội thành 4 đẳng cấp chính, đứng đầu là đẳng cấp nào?",
         "Đẳng cấp Bra-man (Tăng lữ, giáo sĩ).",
         "Đẳng cấp Ksat-ri-a (Vua chúa, quý tộc vũ sĩ).",
         "Đẳng cấp Vai-si-a (Nông dân, thương nhân).",
         "Đẳng cấp Su-đra (Người cùng khổ, nô lệ)."),
        ("Tôn giáo nào ra đời tại Ấn Độ vào thế kỉ VI TCN chủ trương bác bỏ chế độ phân biệt đẳng cấp và hướng tới lòng từ bi, bình đẳng?",
         "Phật giáo.", "Hồi giáo.", "Đạo Hin-đu.", "Kitô giáo."),
        ("Thành tựu toán học nổi bật nhất của cư dân Ấn Độ cổ đại đã đóng góp vĩnh cửu cho nhân loại là gì?",
         "Sáng tạo ra hệ thống 10 chữ số (từ 0 đến 9) và phát minh ra số 0.",
         "Phát minh ra định lí Pi-ta-go.",
         "Tính chính xác số Pi bằng 3,1416.",
         "Sáng tạo ra phép tính lượng giác vi tích phân."),
        ("Học thuyết tư tưởng nào chiếm vị trí nòng cốt và trở thành hệ tư tưởng thống trị của chế độ phong kiến Trung Quốc suốt hơn hai nghìn năm?",
         "Nho giáo (do Khổng Tử khởi xướng).",
         "Đạo giáo (Lão Tử).",
         "Pháp gia (Hàn Phi Tử).",
         "Mặc gia (Mặc Tử)."),
        ("Bốn phát minh kĩ thuật vĩ đại ('Tứ đại phát minh') của nền văn minh Trung Hoa gồm:",
         "Kĩ thuật làm giấy, thuốc súng, la bàn và kĩ thuật in ấn.",
         "Kĩ thuật đúc đồng, đóng tàu, kính thiên văn và la bàn.",
         "Động cơ hơi nước, máy dệt, thuốc súng và máy in.",
         "Đồng hồ cơ khí, xe kéo, giấy và mực nho."),
        ("Công trình phòng thủ quân sự dài nhất thế giới được Tần Thủy Hoàng bắt đầu nối các đoạn thành lũy kiên cố là:",
         "Vạn Lý Trường Thành.", "Tử Cấm Thành.", "Cố Cung Bắc Kinh.", "Lăng mộ Tần Thủy Hoàng."),
        ("Nhà nước thành bang cổ đại nào ở Hy Lạp được xem là cái nôi của nền dân chủ chủ nô phát triển rực rỡ nhất?",
         "Thành bang A-ten (Athens).", "Thành bang Xpác-ta (Sparta).", "Thành bang Rô-ma.", "Thành bang Co-ranh-tơ."),
        ("Bảng chữ cái nào do người La Mã cổ đại hoàn thiện ngày nay đang được sử dụng phổ biến nhất trên toàn thế giới?",
         "Bảng chữ cái La-tinh (Latin).", "Bảng chữ cái Kirin.", "Chữ tượng thanh Ba Tư.", "Chữ Nôm."),
        ("Công trình kiến trúc đấu trường hình elip khổng lồ bằng bê tông và đá nổi tiếng bậc nhất ở La Mã cổ đại là:",
         "Đấu trường Cô-li-dê (Colosseum).", "Đền Pác-tê-nông.", "Đền Păng-tê-ông.", "Quảng trường La Mã Phô-rum."),
        ("Nhà bác học Hy Lạp cổ đại nào đã thốt lên câu nói bất hủ: 'Hãy cho tôi một điểm tựa, tôi sẽ nhấc bổng cả Trái Đất'?",
         "Ác-si-mét (Archimedes).", "Pi-ta-go (Pythagoras).", "Ta-lét (Thales).", "Hơ-rô-đốt (Herodotus)."),
        ("Bản chất cốt lõi của phong trào Văn hóa Phục hưng ở Tây Âu thời hậu kì trung đại là gì?",
         "Cuộc cách mạng tư tưởng của giai cấp tư sản chống lại giáo lí phong kiến lỗi thời, đề cao giá trị con người (chủ nghĩa nhân văn).",
         "Khôi phục lại hoàn toàn tôn giáo thời cổ đại.",
         "Bảo vệ quyền lợi tối cao của tầng lớp giáo hoàng và tăng lữ.",
         "Cuộc nổi dậy vũ trang lật đổ chế độ phong kiến chuyên chế."),
        ("Tác phẩm hội họa kiệt tác 'Nàng Mô-na Li-sa' và 'Bữa tiệc cuối cùng' là của thiên tài nghệ thuật nào thời Phục hưng?",
         "Lê-ô-na đơ Vanh-xi (Leonardo da Vinci).",
         "Mi-ken-lăng-giơ (Michelangelo).",
         "Ra-pha-en (Raphael).",
         "Bốt-ti-xen-li (Botticelli)."),
        ("Tác gia kịch nghệ vĩ đại người Anh thời kì Phục hưng với các vở kịch kinh điển như 'Rô-mê-ô và Giu-li-ét', 'Hăm-lét' là ai?",
         "Uy-li-am Sếch-xpia (William Shakespeare).",
         "Đăng-tơ (Dante).",
         "Xéc-van-téc (Cervantes).",
         "Gơ-tơ (Goethe)."),
        ("Nhà thiên văn học nào thời Phục hưng đã dũng cảm bảo vệ thuyết Nhật tâm (Trái Đất quay quanh Mặt Trời) trước tòa án giáo hội?",
         "Cô-péc-ních và Ga-li-lê (Galileo).",
         "Niu-tơn.",
         "Anh-xtanh.",
         "Pơ-tô-lê-mê."),
        ("Ý nghĩa lịch sử quan trọng nhất của phong trào Văn hóa Phục hưng đối với văn minh nhân loại là gì?",
         "Giải phóng tư tưởng con người, mở đường cho sự phát triển rực rỡ của khoa học và văn hóa tiến bộ phương Tây.",
         "Xóa bỏ hoàn toàn khoảng cách giàu nghèo trong xã hội.",
         "Thống nhất toàn bộ châu Âu thành một đế quốc duy nhất.",
         "Làm sụp đổ ngay lập tức các vương triều phong kiến.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_items, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)

    # ------------------ PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI ------------------
    add_section_header(doc, "PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

    # Câu 1
    p1 = "Sử học là một ngành khoa học nghiên cứu về quá khứ của loài người, từ khi xã hội loài người xuất hiện cho đến ngày nay. Tri thức lịch sử có vai trò đặc biệt quan trọng: giúp con người hiểu rõ về cội nguồn dân tộc, đúc kết các bài học kinh nghiệm của quá khứ để phục vụ hiện tại và định hướng tương lai. Ngày nay, việc gắn kết Sử học với công tác bảo tồn, phát huy các giá trị di sản văn hóa đang mở ra nhiều cơ hội phát triển bền vững cho nền kinh tế du lịch."
    stmts1 = [
        ("a", "Hiện thực lịch sử là những nhận thức chủ quan của các nhà sử học về những sự kiện đã diễn ra."),
        ("b", "Nghiên cứu lịch sử giúp chúng ta rút ra bài học kinh nghiệm để định hướng cho sự phát triển hiện tại và tương lai."),
        ("c", "Di sản văn hóa sau khi được xếp hạng thì không cần sự can thiệp của nghiên cứu Sử học trong việc bảo tồn."),
        ("d", "Bảo tồn di sản gắn với phát triển du lịch là một hướng đi mang lại hiệu quả kinh tế và quảng bá hình ảnh quốc gia.")
    ]
    add_true_false_question(doc, 1, p1, stmts1)

    # Câu 2
    p2 = "Nền văn minh Ai Cập cổ đại là một trong những nền văn minh rực rỡ và xuất hiện sớm nhất của nhân loại. Nhà sử học Hy Lạp cổ đại Hê-rô-đốt từng nhận định: 'Ai Cập là tặng phẩm của sông Nin'. Nước lũ sông Nin hàng năm dâng lên mang theo lớp phù sa đen màu mỡ, bồi đắp hai bên bờ, tạo điều kiện thuận lợi cho nông nghiệp trồng lúa phát triển. Nhu cầu đo đạc lại ruộng đất sau mỗi mùa nước lũ đã thúc đẩy môn Hình học phát triển mạnh mẽ."
    stmts2 = [
        ("a", "Sông Nin đóng vai trò huyết mạch sống còn đối với sự ra đời và tồn tại của nền văn minh Ai Cập cổ đại."),
        ("b", "Hình học ở Ai Cập cổ đại phát triển hoàn toàn bắt nguồn từ nhu cầu thực tiễn đo đạc lại ruộng đất."),
        ("c", "Ai Cập cổ đại là nền văn minh công nghiệp phát triển bậc nhất thế giới cổ đại."),
        ("d", "Nhận định của Hê-rô-đốt nhấn mạnh vai trò quyết định tuyệt đối của tự nhiên mà phủ nhận công lao của con người Ai Cập.")
    ]
    add_true_false_question(doc, 2, p2, stmts2)

    # Câu 3
    p3 = "Nho giáo do Khổng Tử sáng lập vào thời Xuân Thu, sau đó được Mạnh Tử phát triển, trở thành hệ tư tưởng chính thống của chế độ phong kiến Trung Quốc. Hạt nhân cơ bản của Nho giáo là tư tưởng 'Nhân', 'Lễ', 'Chính danh' và thuyết Tam cương - Ngũ thường. Nho giáo đề cao tôn ti trật tự xã hội, coi trọng việc tu thân, tề gia, trị quốc, bình thiên hạ và đạo đức làm người."
    stmts3 = [
        ("a", "Khổng Tử là người sáng lập học thuyết Nho giáo với tư tưởng cốt lõi là chữ 'Nhân' và 'Lễ'."),
        ("b", "Nho giáo ngay từ khi ra đời đã bị các triều đại phong kiến Trung Quốc bài trừ và xóa bỏ hoàn toàn."),
        ("c", "Hệ tư tưởng Nho giáo có ảnh hưởng sâu sắc đến đời sống văn hóa, chính trị, giáo dục của các nước Đông Á như Việt Nam, Triều Tiên, Nhật Bản."),
        ("d", "Tất cả các quan điểm của Nho giáo thời phong kiến đều hoàn toàn phù hợp và cần được giữ nguyên vẹn trong xã hội hiện đại ngày nay.")
    ]
    add_true_false_question(doc, 3, p3, stmts3)

    # Câu 4
    p4 = "Phong trào Văn hóa Phục hưng (thế kỉ XV - XVII) khởi đầu tại các thành thị phát triển ở miền Bắc nước Ý, sau đó lan rộng ra toàn Tây Âu. Các học giả và văn nghệ sĩ Phục hưng đã 'khôi phục lại' những tinh hoa rực rỡ của văn hóa cổ đại Hy Lạp - La Mã, nhưng thực chất là mượn hình thức đó để truyền tải tư tưởng mới của giai cấp tư sản. Họ lên án sự áp chế của Giáo hội Công giáo, đề cao tự do cá nhân và tinh thần khoa học thực nghiệm."
    stmts4 = [
        ("a", "Ý là quê hương khởi xướng phong trào Văn hóa Phục hưng ở châu Âu."),
        ("b", "Phong trào Phục hưng chỉ đơn thuần là sự sao chép máy móc nguyên vẹn nền văn hóa Hy Lạp - La Mã cổ đại."),
        ("c", "Chủ nghĩa nhân văn thời Phục hưng đề cao giá trị và phẩm giá con người, giải phóng tư tưởng khỏi sự kìm hãm của giáo lí trung cổ."),
        ("d", "Phong trào Văn hóa Phục hưng đã tạo nền tảng tư tưởng vững chắc cho các cuộc cách mạng tư sản bùng nổ sau này.")
    ]
    add_true_false_question(doc, 4, p4, stmts4)

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    tf_answers = [
        ("Câu 1", "Sai", "Đúng", "Sai", "Đúng"),
        ("Câu 2", "Đúng", "Đúng", "Sai", "Sai"),
        ("Câu 3", "Đúng", "Sai", "Đúng", "Sai"),
        ("Câu 4", "Đúng", "Sai", "Đúng", "Đúng")
    ]
    
    add_answers_section(doc, mcq_answers, tf_answers=tf_answers)
    
    file_path = os.path.join(OUTPUT_DIR, "De_05_Lop_10_Lich_Su_Dinh_Dang_Moi_2025.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 6. ĐỀ LỚP 10 - ĐỊA LÍ (ĐỊNH DẠNG MỚI BGD 2025)
# ==============================================================================
def generate_grade_10_geography():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="TRƯỜNG THPT CHU VĂN AN",
        exam_title="ĐỀ KIỂM TRA ĐÁNH GIÁ CUỐI HỌC KÌ I - NĂM HỌC 2025 - 2026",
        subject_title="ĐỊA LÍ - KHỐI 10 (CHƯƠNG TRÌNH GDPT 2018 - CẤU TRÚC MỚI)",
        duration_str="50 phút",
        exam_code="106"
    )
    
    add_section_header(doc, "PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (6,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 24. Mỗi câu đúng được 0,25 điểm.")
    
    mcq_items = [
        ("Để thể hiện các đối tượng địa lí phân bố theo những điểm cụ thể như sân bay, nhà máy điện, cảng biển trên bản đồ, người ta dùng phương pháp nào?",
         "Phương pháp kí hiệu điểm.",
         "Phương pháp đường chuyển động.",
         "Phương pháp bản đồ - biểu đồ.",
         "Phương pháp vùng phân bố."),
        ("Phương pháp đường chuyển động trên bản đồ thường được dùng để biểu hiện đối tượng nào sau đây?",
         "Hướng di chuyển của bão, hướng gió và dòng biển.",
         "Mật độ dân số các tỉnh.",
         "Các mỏ khoáng sản kim loại.",
         "Diện tích rừng phòng hộ."),
        ("Hệ thống thông tin địa lí (GIS) có chức năng chính nào sau đây?",
         "Thu thập, lưu trữ, quản lí, phân tích và hiển thị dữ liệu không gian.",
         "Định vị tọa độ vệ tinh GPS mặt đất đơn thuần.",
         "Đo đạc độ ẩm không khí bằng cơ học.",
         "Vẽ bản đồ tay truyền thống."),
        ("Lớp vỏ Trái Đất (vỏ lục địa và vỏ đại dương) được cấu tạo chủ yếu bởi hai tầng đá nào?",
         "Tầng trầm tích và tầng granit (đá hoa cương) / bazan.",
         "Tầng sắt và niken nóng chảy.",
         "Tầng quặng manhetit nguyên chất.",
         "Tầng bùn lỏng biến chất."),
        ("Thạch quyển bao gồm những bộ phận nào sau đây của Trái Đất?",
         "Vỏ Trái Đất và phần trên cùng của lớp man-ti (đến độ sâu khoảng 100km).",
         "Toàn bộ vỏ Trái Đất và nhân Trái Đất.",
         "Chỉ bao gồm lớp vỏ lục địa bên trên mặt nước.",
         "Toàn bộ lớp man-ti trên và man-ti dưới."),
        ("Theo thuyết kiến tạo mảng, nguyên nhân làm cho các mảng kiến tạo dịch chuyển liên tục trên lớp man-ti quánh dẻo là do:",
         "Các dòng đối lưu vật chất nhiệt quyển trong lớp man-ti trên.",
         "Lực hấp dẫn của Mặt Trời và Mặt Trăng.",
         "Tác động của lực Coriolis do Trái Đất tự quay.",
         "Hiện tượng triều cường và sóng thần đáy biển."),
        ("Khi hai mảng kiến tạo đại dương và lục địa xô húc (va chạm) vào nhau, kết quả thường hình thành nên:",
         "Các dãy núi uốn nếp cao đồ sộ và các vực biển sâu kèm theo động đất núi lửa.",
         "Các sống núi ngầm giữa đại dương tách giãn.",
         "Các vùng đồng bằng châu thổ phẳng lặng.",
         "Các bồn trũng yên tĩnh không có địa chấn."),
        ("Vành đai động đất và núi lửa lớn nhất thế giới chiếm hơn 75% số núi lửa hoạt động trên cạn là:",
         "Vành đai lửa Thái Bình Dương.",
         "Vành đai Địa Trung Hải.",
         "Vành đai Đại Tây Dương.",
         "Vành đai Ấn Độ Dương."),
        ("Càng lên cao, nhiệt độ không khí càng giảm vì nguyên nhân chủ yếu nào sau đây?",
         "Không khí càng loãng, bức xạ nhiệt từ mặt đất lên càng yếu dần.",
         "Gần Mặt Trời hơn nên không khí bị đóng băng.",
         "Gió trên cao thổi quá mạnh làm mát không khí.",
         "Tầng ôzôn hấp thụ hết nhiệt năng."),
        ("Biên độ nhiệt độ năm (sự chênh lệch giữa nhiệt độ tháng cao nhất và tháng thấp nhất) có xu hướng thay đổi như thế nào từ Xích đạo về Cực?",
         "Tăng dần từ Xích đạo về hai Cực.",
         "Giảm dần từ Xích đạo về hai Cực.",
         "Không thay đổi trên toàn Trái Đất.",
         "Ở Xích đạo là lớn nhất, ở Cực bằng không."),
        ("Các đai khí áp cao và áp thấp trên bề mặt Trái Đất phân bố theo quy luật nào?",
         "Phân bố xen kẽ và đối xứng nhau qua đai áp thấp Xích đạo.",
         "Áp cao tập trung toàn bộ ở bán cầu Bắc, áp thấp ở bán cầu Nam.",
         "Phân bố lộn xộn không theo quy luật nào.",
         "Chỉ có áp cao ở các cực, toàn bộ phần còn lại là áp thấp."),
        ("Gió Mậu dịch (Tín phong) thổi quanh năm từ khu vực nào về khu vực nào?",
         "Từ áp cao cận chí tuyến về áp thấp Xích đạo.",
         "Từ áp cao cận chí tuyến về áp thấp ôn đới.",
         "Từ áp cao cực về áp thấp ôn đới.",
         "Từ biển vào đất liền vào mùa hạ."),
        ("Gió Phơn (gió lào khô nóng) hình thành khi luồng không khí ẩm vượt qua dãy núi cao do hiện tượng nào?",
         "Không khí ẩm gặp sườn đón gió trút hết mưa, khi vượt qua sườn khuất gió bị nén nhiệt độ tăng nhanh theo đoạn nhiệt khô.",
         "Gió mang theo cát sa mạc nóng thổi qua.",
         "Tầng đối lưu bị thủng cục bộ làm ánh nắng chiếu rọi.",
         "Mặt đất hấp thụ nhiệt từ nham thạch núi lửa."),
        ("Thủy quyển là lớp vỏ lỏng liên tục bao quanh Trái Đất, trong đó nước mặn ở đại dương chiếm khoảng bao nhiêu phần trăm?",
         "Khoảng 97,5% tổng lượng nước toàn cầu.",
         "Khoảng 50% tổng lượng nước.",
         "Khoảng 70% tổng lượng nước.",
         "Khoảng 85% tổng lượng nước."),
        ("Nguyên nhân chủ yếu sinh ra hiện tượng sóng biển là do:",
         "Tác động của gió thổi trên mặt nước biển.",
         "Lực hấp dẫn của Mặt Trời.",
         "Nhiệt độ nước biển thay đổi đột ngột.",
         "Động đất dưới đáy biển sinh ra sóng thường."),
        ("Hiện tượng dao động thủy triều đạt mức nước lớn nhất (triều cường) xảy ra vào những ngày nào trong tháng âm lịch?",
         "Ngày không trăng (mồng 1) và ngày trăng tròn (rằm 15).",
         "Ngày trăng khuyết đầu tháng (mồng 7) và cuối tháng (23).",
         "Vào tất cả các ngày chủ nhật trong tháng.",
         "Chỉ xảy ra duy nhất vào ngày rằm tháng tám."),
        ("Dòng biển nóng và dòng biển lạnh có ảnh hưởng rất lớn đến khí hậu ven bờ nơi chúng đi qua như thế nào?",
         "Dòng biển nóng làm tăng nhiệt độ và gây mưa nhiều; dòng biển lạnh làm khí hậu khô hạn ít mưa.",
         "Cả hai dòng biển đều làm khí hậu ven bờ trở nên băng giá quanh năm.",
         "Dòng biển lạnh mang lại mưa bão cực lớn; dòng biển nóng làm hình thành hoang mạc.",
         "Không có tác động nào đáng kể đối với đất liền."),
        ("Thổ nhưỡng (đất) là gì?",
         "Lớp vật chất tơi xốp nằm ở bề mặt lục địa, có độ phì (khả năng cung cấp nước, nhiệt, khí và dinh dưỡng cho cây).",
         "Tất cả các loại đá vụn trên sườn núi dốc.",
         "Cát và sỏi vô cơ dưới đáy sông ngòi.",
         "Lớp khoáng sản kim loại dưới sâu vỏ Trái Đất."),
        ("Nhân tố nào sau đây đóng vai trò cung cấp chất vô cơ cho đất và quyết định thành phần khoáng vật, cơ giới của đất?",
         "Đá mẹ.", "Khí hậu.", "Sinh vật.", "Địa hình."),
        ("Sinh vật đóng vai trò chủ đạo nào trong quá trình hình thành đất?",
         "Cung cấp chất hữu cơ, phá hủy đá bằng cơ - sinh học và tái tạo độ phì cho đất.",
         "Cung cấp các hạt khoáng sét vô cơ nặng.",
         "Điều hòa nhiệt độ và áp suất nén lòng đất.",
         "Tạo ra các đứt gãy kiến tạo."),
        ("Giới hạn trên của sinh quyển tiếp giáp với tầng nào của khí quyển?",
         "Nơi tiếp giáp với tầng ôzôn (khoảng 20 - 25km).",
         "Tầng ion nhiệt quyển cao 100km.",
         "Tầng đối lưu ở độ cao 8km.",
         "Vượt ra ngoài vũ trụ không gian."),
        ("Quy luật địa đới là sự thay đổi có quy luật của tất cả các thành phần địa lí và cảnh quan địa lí theo yếu tố nào?",
         "Theo vĩ độ (từ Xích đạo về hai Cực).",
         "Theo độ cao từ thấp lên đỉnh núi.",
         "Theo khoảng cách từ biển vào sâu trong nội địa.",
         "Theo chiều sâu dưới đáy biển."),
        ("Nguyên nhân căn bản tạo nên quy luật địa đới trên Trái Đất là gì?",
         "Trái Đất hình cầu làm cho góc chiếu của tia sáng Mặt Trời thay đổi giảm dần từ Xích đạo về hai Cực.",
         "Trái Đất nghiêng 66 độ 33 phút khi quay.",
         "Sự phân bố đan xen giữa lục địa và đại dương.",
         "Tác động của các dòng biển nóng lạnh."),
        ("Quy luật đai cao là sự thay đổi của các thành phần tự nhiên và cảnh quan theo yếu tố nào?",
         "Theo độ cao địa hình (càng lên cao nhiệt độ càng giảm, độ ẩm thay đổi).",
         "Theo vĩ tuyến trải dài từ Đông sang Tây.",
         "Theo thời gian bốn mùa xuân hạ thu đông.",
         "Theo chu kì hoạt động của vết đen Mặt Trời.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_items, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)

    # ------------------ PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI ------------------
    add_section_header(doc, "PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

    # Câu 1: Nhiệt độ không khí
    p1 = "Nhiệt độ không khí trên bề mặt Trái Đất có sự phân hóa rõ rệt theo vĩ độ địa lí. Tại khu vực Xích đạo, góc nhập xạ lớn quanh năm nên nhiệt độ trung bình năm luôn cao (> 25°C) và biên độ nhiệt năm rất nhỏ (< 3°C). Ngược lại, càng lên các vĩ độ cao (vùng cận cực và cực), góc nhập xạ nhỏ dần và có sự chênh lệch thời gian chiếu sáng rất lớn giữa mùa hạ và mùa đông, khiến nhiệt độ trung bình năm xuống rất thấp và biên độ nhiệt năm tăng cao kỉ lục (> 30°C - 40°C)."
    stmts1 = [
        ("a", "Nhiệt độ trung bình năm của không khí có xu hướng giảm dần từ Xích đạo về hai Cực."),
        ("b", "Biên độ nhiệt độ năm ở vùng cực nhỏ hơn rất nhiều so với vùng Xích đạo."),
        ("c", "Góc nhập xạ thay đổi theo vĩ độ là nhân tố quyết định lượng nhiệt Trái Đất nhận được từ Mặt Trời."),
        ("d", "Ở xích đạo không có mùa đông lạnh vì quanh năm góc chiếu sáng của Mặt Trời luôn lớn.")
    ]
    add_true_false_question(doc, 1, p1, stmts1)

    # Câu 2: Thuyết kiến tạo mảng
    p2 = "Theo thuyết kiến tạo mảng, thạch quyển được chia thành các mảng kiến tạo lớn và nhỏ trôi nổi độc lập trên lớp vật chất quánh dẻo của manti trên. Vùng tiếp xúc giữa các mảng kiến tạo là nơi thường xuyên diễn ra các hoạt động địa chất dữ dội. Khi hai mảng lục địa va chạm (xô húc) với nhau, lớp trầm tích bị ép nén, uốn nếp tạo nên các dãy núi trẻ hùng vĩ (ví dụ: mảng Ấn Độ va chạm với mảng Á - Âu nâng cao dãy Hymalaya). Ngược lại, nơi hai mảng tách giãn nhau sẽ tạo nên các sống núi ngầm giữa đại dương hoặc thung lũng tách giãn lục địa."
    stmts2 = [
        ("a", "Ranh giới tiếp xúc giữa các mảng kiến tạo là nơi tập trung phần lớn các trận động đất và núi lửa trên Trái Đất."),
        ("b", "Dãy Hi-ma-lay-a hình thành do kết quả của sự tách giãn giữa hai mảng mảng kiến tạo đại dương."),
        ("c", "Các mảng kiến tạo đứng yên bất động kể từ khi Trái Đất hình thành đến nay."),
        ("d", "Thuyết kiến tạo mảng giúp giải thích khoa học nguồn gốc hình thành địa hình đồi núi đồ sộ và đáy đại dương.")
    ]
    add_true_false_question(doc, 2, p2, stmts2)

    # Câu 3: Thủy triều
    p3 = "Thủy triều là hiện tượng dao động thường xuyên và có chu kì của các khối nước trong các biển và đại dương, hình thành chủ yếu do lực hấp dẫn của Mặt Trăng và Mặt Trời kết hợp với lực li tâm của Trái Đất. Trong một tháng âm lịch, khi Mặt Trời, Mặt Trăng và Trái Đất cùng nằm trên một đường thẳng (vào các ngày mồng 1 và rằm 15), lực hút tổng hợp đạt cực đại sinh ra 'triều cường'. Khi Mặt Trăng, Trái Đất và Mặt Trời tạo thành một góc vuông 90 độ (vào ngày mồng 7 và ngày 23 âm lịch), lực hút bị triệt tiêu một phần sinh ra 'triều kém'."
    stmts3 = [
        ("a", "Lực hấp dẫn của Mặt Trăng đóng vai trò chính tạo nên hiện tượng thủy triều trên Trái Đất."),
        ("b", "Hiện tượng triều cường diễn ra khi Mặt Trăng, Trái Đất và Mặt Trời vuông góc với nhau."),
        ("c", "Dao động thủy triều có thể được con người khai thác để phát triển năng lượng điện sạch (thủy triều)."),
        ("d", "Trong một tháng âm lịch luôn có 2 lần triều cường và 2 lần triều kém.")
    ]
    add_true_false_question(doc, 3, p3, stmts3)

    # Câu 4: Quy luật đai cao
    p4 = "Ở các vùng núi cao nhiệt đới ẩm, sự thay đổi nhiệt độ và độ ẩm theo độ cao dẫn đến sự hình thành quy luật đai cao của tự nhiên. Tại chân núi có vành đai nhiệt đới ẩm gió mùa với rừng rậm thường xanh phát triển trên đất feralit đỏ vàng. Lên cao từ 600 - 700m đến 2600m là vành đai cận nhiệt đới gió mùa trên núi với rừng lá rộng, lá kim phát triển trên đất mùn. Lên cao trên 2600m khí hậu chuyển sang đai ôn đới vùng núi cao, thực vật chuyển thành rêu, địa y và cây bụi thấp."
    stmts4 = [
        ("a", "Quy luật đai cao phản ánh sự thay đổi của thực vật và đất đai theo độ cao địa hình."),
        ("b", "Càng lên cao trên núi nhiệt độ càng tăng do gần Mặt Trời hơn."),
        ("c", "Cảnh quan thiên nhiên ở chân núi phản ánh rõ đặc điểm của đới khí hậu mà ngọn núi đó tọa lạc."),
        ("d", "Việc trồng và bảo vệ rừng phòng hộ đầu nguồn trên các vùng núi dốc có vai trò sinh thái quyết định đối với vùng đồng bằng hạ lưu.")
    ]
    add_true_false_question(doc, 4, p4, stmts4)

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    tf_answers = [
        ("Câu 1", "Đúng", "Sai", "Đúng", "Đúng"),
        ("Câu 2", "Đúng", "Sai", "Sai", "Đúng"),
        ("Câu 3", "Đúng", "Sai", "Đúng", "Đúng"),
        ("Câu 4", "Đúng", "Sai", "Đúng", "Đúng")
    ]
    
    add_answers_section(doc, mcq_answers, tf_answers=tf_answers)
    
    file_path = os.path.join(OUTPUT_DIR, "De_06_Lop_10_Dia_Li_Dinh_Dang_Moi_2025.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 7. ĐỀ THI TỐT NGHIỆP THPT LỚP 12 - LỊCH SỬ (CHUẨN ĐỀ THAM KHẢO BGD 2025)
# ==============================================================================
def generate_grade_12_history():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="BỘ GIÁO DỤC VÀ ĐÀO TẠO",
        exam_title="KÌ THI TỐT NGHIỆP TRUNG HỌC PHỔ THÔNG NĂM 2026",
        subject_title="LỊCH SỬ - ĐỀ THI THỬ CHUẨN ĐỊNH DẠNG KHẢO THÍ MỚI",
        duration_str="50 phút",
        exam_code="121"
    )
    
    add_section_header(doc, "PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (6,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 24. Mỗi câu đúng được 0,25 điểm.")
    
    mcq_items = [
        ("Trật tự thế giới hai cực I-an-ta (hình thành sau Hội nghị Ianta 1945) bị chi phối bởi hai siêu cường đại diện cho hai hệ tư tưởng đối lập nào?",
         "Mỹ (tư bản chủ nghĩa) và Liên Xô (xã hội chủ nghĩa).",
         "Anh và Pháp.",
         "Mỹ và Trung Quốc.",
         "Liên Xô và Đức."),
        ("Mục tiêu bao trùm cao nhất của tổ chức Liên hợp quốc được nêu rõ trong Hiến chương là gì?",
         "Duy trì hòa bình và an ninh quốc tế, phát triển quan hệ hữu nghị hợp tác giữa các quốc gia.",
         "Thiết lập liên minh quân sự chống lại các nước nghèo.",
         "Thống nhất tiền tệ trên quy mô toàn cầu.",
         "Xóa bỏ hoàn toàn biên giới các quốc gia."),
        ("Cơ quan nào của Liên hợp quốc giữ vai trò trọng yếu trong việc duy trì hòa bình và an ninh thế giới, với 5 nước ủy viên thường trực có quyền phủ quyết?",
         "Hội đồng Bảo an.",
         "Đại hội đồng.",
         "Ban Thư kí.",
         "Tòa án Công lí Quốc tế."),
        ("Hiệp hội các quốc gia Đông Nam Á (ASEAN) được thành lập vào ngày 8/8/1967 tại Băng Cốc (Thái Lan) với sự tham gia của 5 nước sáng lập đầu tiên là:",
         "In-đô-nê-xi-a, Ma-lai-xi-a, Phi-líp-pin, Xin-ga-po và Thái Lan.",
         "Việt Nam, Lào, Cam-pu-chia, Mi-an-ma và Thái Lan.",
         "Bru-nây, Xin-ga-po, Thái Lan, In-đô-nê-xi-a và Việt Nam.",
         "Ma-lai-xi-a, Xin-ga-po, Đông Ti-mo, Lào và Thái Lan."),
        ("Văn kiện pháp lí nền tảng xác định mục tiêu xây dựng Đông Nam Á thành khu vực hòa bình, tự do và trung lập (ZOPFAN) là:",
         "Tuyên bố Băng Cốc và Tuyên bố Cua-la Lăm-pơ (1971).",
         "Hiệp ước Ba-li năm 1976.",
         "Hiến chương ASEAN năm 2007.",
         "Kế hoạch Colombo."),
        ("Năm 1995 ghi dấu mốc lịch sử đặc biệt nào trong quan hệ đối ngoại và hội nhập khu vực của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam?",
         "Việt Nam chính thức gia nhập ASEAN và bình thường hóa quan hệ ngoại giao với Hoa Kỳ.",
         "Việt Nam gia nhập Tổ chức Thương mại Thế giới (WTO).",
         "Việt Nam kí Hiệp định Thương mại Tự do EVFTA.",
         "Việt Nam được bầu làm Ủy viên không thường trực Hội đồng Bảo an LHQ."),
        ("Sự sụp đổ của Trật tự hai cực I-an-ta và sự tan rã của Liên Xô (1991) đã thúc đẩy trật tự thế giới chuyển biến theo xu thế nào?",
         "Xu thế đa cực, nhiều trung tâm, hợp tác và cạnh tranh hòa bình.",
         "Trật tự đơn cực do một mình Hoa Kỳ thống trị tuyệt đối vĩnh viễn.",
         "Một cuộc chiến tranh thế giới thứ ba bùng nổ toàn diện ngay lập tức.",
         "Tất cả các nước đóng cửa biên giới ngừng giao thương."),
        ("Tổ chức liên kết kinh tế - chính trị khu vực lớn nhất và có mức độ hội nhập sâu rộng nhất hành tinh hiện nay là:",
         "Liên minh châu Âu (EU).",
         "Hiệp hội các quốc gia Đông Nam Á (ASEAN).",
         "Diễn đàn Hợp tác Kinh tế châu Á - Thái Bình Dương (APEC).",
         "Thị trường chung Nam Mỹ (MERCOSUR)."),
        ("Đại hội đại biểu toàn quốc lần thứ VI của Đảng Cộng sản Việt Nam (tháng 12/1986) đã đề ra đường lối có tính bước ngoặt lịch sử nào?",
         "Đường lối Đổi mới toàn diện đất nước, trọng tâm là đổi mới kinh tế.",
         "Đường lối công nghiệp hóa ưu tiên phát triển công nghiệp nặng.",
         "Chủ trương đóng cửa kinh tế để tự cung tự cấp.",
         "Chuyển ngay lập tức sang kinh tế thị trường tự do hoàn toàn không có sự quản lí của Nhà nước."),
        ("Một trong những nội dung cốt lõi của đổi mới kinh tế ở Việt Nam từ năm 1986 đến nay là gì?",
         "Xóa bỏ cơ chế tập trung quan liêu bao cấp, phát triển nền kinh tế thị trường định hướng xã hội chủ nghĩa nhiều thành phần.",
         "Quốc hữu hóa toàn bộ các xí nghiệp tư nhân và cơ sở kinh doanh cá thể.",
         "Chỉ phát triển duy nhất kinh tế quốc doanh và tập thể.",
         "Dừng mọi hoạt động xuất khẩu lương thực ra thế giới."),
        ("Ba chương trình kinh tế lớn được Đại hội VI của Đảng (1986) xác định tập trung thực hiện là:",
         "Lương thực - thực phẩm, hàng tiêu dùng và hàng xuất khẩu.",
         "Năng lượng, luyện kim và cơ khí chế tạo.",
         "Giao thông vận tải, bưu chính viễn thông và du lịch.",
         "Công nghệ cao, hóa dược và đóng tàu biển."),
        ("Chính sách đối ngoại nhất quán của Đảng và Nhà nước ta trong công cuộc Đổi mới và hội nhập quốc tế là:",
         "Độc lập, tự chủ, hòa bình, hữu nghị, hợp tác và phát triển; đa phương hóa, đa dạng hóa quan hệ đối ngoại.",
         "Chỉ liên minh quân sự chặt chẽ với một cường quốc duy nhất.",
         "Không quan hệ ngoại giao với các nước có chế độ chính trị khác biệt.",
         "Ưu tiên đối đầu quân sự để giải quyết tranh chấp biên giới."),
        ("Đến nay, Việt Nam đã thiết lập quan hệ ngoại giao với gần 200 quốc gia và nâng cấp quan hệ lên Đối tác Chiến lược Toàn diện với các cường quốc hàng đầu thế giới gồm:",
         "Trung Quốc, Nga, Ấn Độ, Hàn Quốc, Hoa Kỳ, Nhật Bản, Australia, Pháp...",
         "Chỉ duy nhất có 2 nước láng giềng.",
         "Chỉ các quốc gia thuộc châu Âu.",
         "Chỉ các nước trong khối xã hội chủ nghĩa trước đây."),
        ("Năm 2007, Việt Nam chính thức trở thành thành viên thứ 150 của tổ chức kinh tế toàn cầu nào?",
         "Tổ chức Thương mại Thế giới (WTO).",
         "Quỹ Tiền tệ Quốc tế (IMF).",
         "Ngân hàng Thế giới (WB).",
         "Tổ chức Hợp tác và Phát triển Kinh tế (OECD)."),
        ("Chiến lược 'Ngoại giao Cây tre' của Việt Nam mang đặc trưng nổi bật nào sau đây?",
         "Gốc vững, thân chắc, cành uyển chuyển; kiên định về nguyên tắc, linh hoạt về sách lược.",
         "Dễ dàng ngả nghiêng theo lợi ích trước mắt của các nước lớn.",
         "Cứng nhắc không bao giờ đàm phán thỏa hiệp.",
         "Xa lánh các diễn đàn đa phương khu vực."),
        ("Khẩu hiệu hành động xuyên suốt của nhân dân ta trong giai đoạn Toàn quốc kháng chiến chống thực dân Pháp (1946) là:",
         "'Quyết tử để Tổ quốc quyết sinh'.",
         "'Không có gì quý hơn độc lập, tự do'.",
         "'Tất cả cho tiền tuyến, tất cả để đánh thắng giặc Mỹ xâm lược'.",
         "'Độc lập hay là chết'."),
        ("Thắng lợi quân sự nào của quân và dân ta đã làm phá sản hoàn toàn Kế hoạch Nava của thực dân Pháp có sự can thiệp của Mỹ năm 1954?",
         "Chiến dịch Điện Biên Phủ.",
         "Chiến dịch Biên giới Thu Đông 1950.",
         "Chiến thắng Việt Bắc Thu Đông 1947.",
         "Chiến dịch Thượng Lào 1953."),
        ("Chiến thắng quân sự nào mở đầu cho cao trào 'Tìm Mỹ mà đánh, lùng ngụy mà diệt' ở miền Nam năm 1965?",
         "Chiến thắng Vạn Tường (Quảng Ngãi).",
         "Chiến thắng Ấp Bắc (Mỹ Tho).",
         "Chiến thắng Ba Gia.",
         "Chiến dịch Đồng Xoài."),
        ("Hiệp định Pa-ri năm 1973 về chấm dứt chiến tranh, lập lại hòa bình ở Việt Nam đã buộc Hoa Kỳ phải thực hiện cam kết mấu chốt nào?",
         "Tôn trọng độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của Việt Nam, rút hết quân viễn chinh về nước.",
         "Tiếp tục viện trợ quân sự không giới hạn cho chính quyền Sài Gòn.",
         "Duy trì các căn cứ quân sự Mỹ lâu dài ở miền Nam.",
         "Được quyền can thiệp vào bầu cử tự do của nhân dân miền Nam."),
        ("Cuộc Tổng tiến công và nổi dậy Xuân 1975 đã toàn thắng sau bao nhiêu ngày đêm tiến công thần tốc?",
         "55 ngày đêm (từ 4/3 đến 30/4/1975).",
         "81 ngày đêm bảo vệ Thành cổ Quảng Trị.",
         "12 ngày đêm Điện Biên Phủ trên không.",
         "100 ngày đêm chiến dịch Tây Nguyên."),
        ("Kì họp thứ nhất Quốc hội khóa VI (tháng 6 - 7/1976) đã hoàn thành nhiệm vụ lịch sử to lớn nào sau ngày giải phóng?",
         "Thống nhất đất nước về mặt nhà nước, đặt tên nước là Cộng hòa Xã hội Chủ nghĩa Việt Nam, Thủ đô là Hà Nội.",
         "Kí hiệp ước liên minh phòng thủ quân sự Đông Dương.",
         "Ban hành Hiến pháp năm 1992.",
         "Bắt đầu thực hiện công cuộc Đổi mới."),
        ("Tuyên ngôn Độc lập ngày 2/9/1945 trích dẫn câu mở đầu trong bản Tuyên ngôn Độc lập năm 1776 của nước nào và Tuyên ngôn Nhân quyền, Dân quyền năm 1789 của nước nào?",
         "Nước Mỹ và nước Pháp.",
         "Nước Anh và nước Nga.",
         "Nước Đức và nước Ý.",
         "Nước Trung Quốc và Ấn Độ."),
        ("Trách nhiệm công dân thiêng liêng cao cả nhất của thế hệ trẻ học sinh hiện nay trong sự nghiệp bảo vệ chủ quyền biển đảo thiêng liêng của Tổ quốc là gì?",
         "Không ngừng học tập nâng cao tri thức, rèn luyện bản lĩnh chính trị, nắm vững luật pháp quốc tế và tuyên truyền bảo vệ chủ quyền biên giới hải đảo.",
         "Tự ý kích động biểu tình bạo lực trên mạng xã hội.",
         "Thờ ơ không quan tâm đến các vấn đề chủ quyền đất nước.",
         "Chỉ tập trung vào lợi ích cá nhân."),
        ("Xu thế phát triển chung của thế giới ngày nay sau Chiến tranh Lạnh là gì?",
         "Hòa bình, hữu nghị, hợp tác cùng phát triển và lấy phát triển kinh tế làm trọng tâm.",
         "Chạy đua vũ trang hạt nhân chuẩn bị thế chiến.",
         "Phân chia thế giới thành các phe khối quân sự đối đầu nghẹt thở.",
         "Áp đặt trừng phạt đơn phương và bế quan tỏa cảng.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_items, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)

    # ------------------ PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI ------------------
    add_section_header(doc, "PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

    # Câu 1: Tuyên ngôn Độc lập 1945
    p1 = "Trong bản Tuyên ngôn Độc lập bất hủ ngày 2/9/1945, Chủ tịch Hồ Chí Minh đã khẳng định đanh thép trước toàn thể quốc dân đồng bào và nhân dân thế giới: 'Nước Việt Nam có quyền hưởng tự do và độc lập, và sự thật đã thành một nước tự do, độc lập. Toàn thể dân tộc Việt Nam quyết đem tất cả tinh thần và lực lượng, tính mạng và của cải để giữ vững quyền tự do, độc lập ấy'. Bản Tuyên ngôn không chỉ khai sinh ra nước Việt Nam Dân chủ Cộng hòa mà còn khẳng định sự gắn kết biện chứng không thể tách rời giữa quyền con người và quyền tự quyết dân tộc."
    stmts1 = [
        ("a", "Bản Tuyên ngôn Độc lập tuyên bố thủ tiêu hoàn toàn chế độ phong kiến và ách thống trị thực dân trên đất nước Việt Nam."),
        ("b", "Chủ tịch Hồ Chí Minh đã phát triển sáng tạo quyền con người (quyền tự do, bình đẳng, mưu cầu hạnh phúc) thành quyền độc lập, tự chủ của mỗi dân tộc."),
        ("c", "Tuyên ngôn Độc lập năm 1945 chỉ có giá trị pháp lí và chính trị trong phạm vi nội bộ lãnh thổ Việt Nam mà không mang ý nghĩa quốc tế."),
        ("d", "Quyết tâm 'đem tất cả tinh thần và lực lượng, tính mạng và của cải để giữ vững quyền tự do, độc lập' thể hiện ý chí quật cường bất khuất của dân tộc trước nguy cơ thù trong giặc ngoài.")
    ]
    add_true_false_question(doc, 1, p1, stmts1)

    # Câu 2: Đường lối Đổi mới 1986
    p2 = "Nghị quyết Đại hội đại biểu toàn quốc lần thứ VI của Đảng (tháng 12/1986) đã thẳng thắn nhìn nhận những sai lầm khuyết điểm chủ quan, duy ý chí trong việc bố trí cơ cấu kinh tế và quản lí nhà nước trước đó, đồng thời khởi xướng đường lối Đổi mới toàn diện đất nước. Đại hội xác định: đổi mới không phải là thay đổi mục tiêu chủ nghĩa xã hội mà là làm cho mục tiêu đó được thực hiện có hiệu quả hơn bằng những nhận thức đúng đắn và bước đi phù hợp. Trong đó, Đảng nhấn mạnh đổi mới kinh tế là trọng tâm, từng bước đổi mới chính trị vững chắc; thực hiện chính sách kinh tế nhiều thành phần và mở rộng quan hệ kinh tế đối ngoại."
    stmts2 = [
        ("a", "Đại hội VI (1986) đã dũng cảm 'nhìn thẳng vào sự thật, đánh giá đúng sự thật, nói rõ sự thật' để đề ra đường lối đổi mới đúng đắn."),
        ("b", "Đổi mới theo quan điểm của Đảng Cộng sản Việt Nam là từ bỏ hoàn toàn con đường xã hội chủ nghĩa để đi theo kinh tế tư bản thuần túy."),
        ("c", "Quan điểm chỉ đạo của Đảng là lấy đổi mới kinh tế làm trọng tâm gắn liền với đổi mới từng bước vững chắc hệ thống chính trị."),
        ("d", "Công cuộc Đổi mới từ năm 1986 là bước ngoặt quyết định đưa Việt Nam thoát khỏi khủng hoảng kinh tế - xã hội và đạt nhiều thành tựu vượt bậc hôm nay.")
    ]
    add_true_false_question(doc, 2, p2, stmts2)

    # Câu 3: ASEAN
    p3 = "Trải qua gần 6 thập kỉ hình thành và phát triển, ASEAN đã trở thành một tổ chức hợp tác khu vực toàn diện, năng động và có uy tín cao trên trường quốc tế. Ngày 31/12/2015, Cộng đồng ASEAN (AEC) chính thức được thành lập dựa trên ba trụ cột vững chắc: Cộng đồng Chính trị - An ninh (APSC), Cộng đồng Kinh tế (AEC) và Cộng đồng Văn hóa - Xã hội (ASCC). Hiến chương ASEAN khẳng định các nguyên tắc nền tảng: tôn trọng độc lập, chủ quyền, toàn vẹn lãnh thổ; không can thiệp vào công việc nội bộ của nhau; giải quyết tranh chấp bằng biện pháp hòa bình và nguyên tắc đồng thuận (Consensus)."
    stmts3 = [
        ("a", "Cộng đồng ASEAN được xây dựng vững chắc dựa trên 3 trụ cột: Chính trị - An ninh, Kinh tế và Văn hóa - Xã hội."),
        ("b", "Nguyên tắc đồng thuận (Consensus) có nghĩa là mọi quyết định quan trọng của ASEAN đều phải được tất cả các nước thành viên nhất trí."),
        ("c", "Việc gia nhập ASEAN năm 1995 đã mở đầu cho tiến trình hội nhập quốc tế sâu rộng và nâng cao vị thế ngoại giao của Việt Nam."),
        ("d", "Nguyên tắc không can thiệp vào công việc nội bộ đồng nghĩa với việc các nước ASEAN hoàn toàn thờ ơ và không phối hợp ứng phó với các thách thức an ninh phi truyền thống chung.")
    ]
    add_true_false_question(doc, 3, p3, stmts3)

    # Câu 4: Biển Đông & Công ước Luật Biển UNCLOS 1982
    p4 = "Biển Đông là vùng biển có vị trí chiến lược địa chính trị và địa kinh tế huyết mạch hàng đầu thế giới, kết nối Ấn Độ Dương với Thái Bình Dương. Việt Nam là quốc gia ven biển có đường bờ biển dài trên 3.260 km, có chủ quyền lịch sử và pháp lí vững chắc, không thể tranh cãi đối với hai quần đảo Hoàng Sa và Trường Sa. Lập trường nhất quán của Đảng và Nhà nước ta là kiên quyết, kiên trì đấu tranh bảo vệ vững chắc độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ, vùng trời và biển đảo của Tổ quốc; giải quyết mọi tranh chấp trên Biển Đông bằng các biện pháp hòa bình, trên cơ sở luật pháp quốc tế, đặc biệt là Công ước Liên hợp quốc về Luật Biển năm 1982 (UNCLOS 1982) và thực hiện đầy đủ Tuyên bố về cách ứng xử của các bên ở Biển Đông (DOC), hướng tới Bộ Quy tắc ứng xử ở Biển Đông (COC) hiệu lực, thực chất."
    stmts4 = [
        ("a", "Việt Nam có đầy đủ bằng chứng lịch sử và căn cứ pháp lí quốc tế khẳng định chủ quyền đối với quần đảo Hoàng Sa và quần đảo Trường Sa."),
        ("b", "Công ước Luật Biển UNCLOS 1982 được coi là 'Hiến chương của đại dương', là cơ sở pháp lí tối cao để xác định ranh giới các vùng biển của các quốc gia ven biển."),
        ("c", "Việt Nam chủ trương dùng vũ lực quân sự tấn công phủ đầu để giải quyết nhanh chóng mọi bất đồng trên Biển Đông."),
        ("d", "Việc duy trì hòa bình, an ninh, tự do hàng hải và hàng không ở Biển Đông là lợi ích chung của toàn bộ cộng đồng quốc tế.")
    ]
    add_true_false_question(doc, 4, p4, stmts4)

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    tf_answers = [
        ("Câu 1", "Đúng", "Đúng", "Sai", "Đúng"),
        ("Câu 2", "Đúng", "Sai", "Đúng", "Đúng"),
        ("Câu 3", "Đúng", "Đúng", "Đúng", "Sai"),
        ("Câu 4", "Đúng", "Đúng", "Sai", "Đúng")
    ]
    
    add_answers_section(doc, mcq_answers, tf_answers=tf_answers)
    
    file_path = os.path.join(OUTPUT_DIR, "De_07_Lop_12_Lich_Su_Thi_Tot_Nghiep_THPT_Chuan_BGD.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 8. ĐỀ THI TỐT NGHIỆP THPT LỚP 12 - ĐỊA LÍ (CHUẨN ĐỀ THAM KHẢO BGD 2025)
# ==============================================================================
def generate_grade_12_geography():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="BỘ GIÁO DỤC VÀ ĐÀO TẠO",
        exam_title="KÌ THI TỐT NGHIỆP TRUNG HỌC PHỔ THÔNG NĂM 2026",
        subject_title="ĐỊA LÍ - ĐỀ THI THỬ CHUẨN ĐỊNH DẠNG KHẢO THÍ MỚI",
        duration_str="50 phút",
        exam_code="122"
    )
    
    add_section_header(doc, "PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (6,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 24. Mỗi câu đúng được 0,25 điểm.")
    
    mcq_items = [
        ("Vị trí địa lí nằm hoàn toàn trong vùng nội chí tuyến Bắc bán cầu quy định đặc điểm cơ bản nào của thiên nhiên nước ta?",
         "Khí hậu mang tính chất nhiệt đới ẩm gió mùa, nền nhiệt cao, chan hòa ánh nắng quanh năm.",
         "Khí hậu hàn đới băng tuyết bao phủ quanh năm.",
         "Cảnh quan hoang mạc xích đạo khô nóng tuyệt đối.",
         "Khí hậu ôn đới lục địa sâu sắc."),
        ("Hiện tượng xâm nhập mặn sâu vào đất liền trong mùa khô ở Đồng bằng sông Cửu Long chịu ảnh hưởng mạnh nhất bởi nhân tố nào?",
         "Mùa khô kéo dài sâu sắc kết hợp với triều cường và lưu lượng nước từ thượng nguồn sông Mê Công đổ về suy giảm.",
         "Các đợt gió mùa Đông Bắc lạnh buốt thổi mạnh.",
         "Hiện tượng sạt lở bờ biển do bão nhiệt đới mùa hè.",
         "Lượng mưa mùa khô quá lớn làm vỡ đê ngăn mặn."),
        ("Vùng có tiềm năng thủy điện lớn nhất nước ta tập trung ở hệ thống sông nào?",
         "Hệ thống sông Hồng (trên sông Đà: Thủy điện Sơn La, Hòa Bình, Lai Châu).",
         "Hệ thống sông Mã.",
         "Hệ thống sông Cả.",
         "Hệ thống sông Thu Bồn."),
        ("Biện pháp hàng đầu để bảo vệ và phát triển bền vững tài nguyên rừng phòng hộ ở nước ta là:",
         "Bảo vệ diện tích hiện có kết hợp trồng rừng mới, phòng chống cháy rừng trên các sườn dốc đầu nguồn.",
         "Khai thác triệt để các loài gỗ quý để tăng thu ngân sách.",
         "Chuyển toàn bộ rừng phòng hộ sang đất canh tác trồng trọt cao su.",
         "Đốt thực bì để lấy đất nuôi tôm ven biển."),
        ("Dân số nước ta hiện nay đang trải qua giai đoạn chuyển đổi nhân khẩu học với đặc điểm nổi bật nào?",
         "Quy mô dân số đông (>100 triệu dân), cơ cấu dân số vàng và đang bước nhanh vào giai đoạn già hóa dân số.",
         "Tỉ lệ gia tăng tự nhiên đang bùng nổ vượt mức 3%/năm.",
         "Tỉ lệ dân thành thị đã chiếm trên 85% tổng dân số cả nước.",
         "Lực lượng lao động suy giảm nghiêm trọng thiếu người làm việc."),
        ("Đô thị hóa ở nước ta hiện nay có vai trò chiến lược nào đối với nền kinh tế?",
         "Tạo động lực lan tỏa thúc đẩy chuyển dịch cơ cấu kinh tế, thu hút đầu tư và tạo nhiều việc làm phi nông nghiệp.",
         "Tạo ra các dòng người di cư thất nghiệp về quê.",
         "Làm suy giảm hoàn toàn ngành thương mại dịch vụ.",
         "Chỉ phát triển các ngành tiểu thủ công nghiệp truyền thống."),
        ("Xu hướng chuyển dịch cơ cấu ngành kinh tế của nước ta theo hướng công nghiệp hóa, hiện đại hóa thể hiện ở điểm nào?",
         "Giảm tỉ trọng khu vực nông - lâm - thủy sản, tăng tỉ trọng khu vực công nghiệp - xây dựng và dịch vụ.",
         "Tăng tối đa tỉ trọng nông nghiệp tự cung tự cấp.",
         "Xóa bỏ hoàn toàn khu vực dịch vụ.",
         "Giảm tỉ trọng của công nghiệp chế biến chế tạo."),
        ("Cây công nghiệp lâu năm được trồng với diện tích và sản lượng lớn nhất ở vùng Tây Nguyên là cây nào?",
         "Cây cà phê (đặc biệt là cà phê Robusta).",
         "Cây chè búp.",
         "Cây hồi và quế.",
         "Cây thuốc lá."),
        ("Điều kiện tự nhiên thuận lợi nhất để vùng Duyên hải Nam Trung Bộ phát triển nghề làm muối hạt chất lượng cao là gì?",
         "Nhiệt độ cao quanh năm, nhiều nắng gió, lượng mưa rất ít và ít có sông lớn đổ ra biển (Cà Ná, Sa Huỳnh).",
         "Có mạng lưới sông ngòi dày đặc đổ ra nhiều phù sa đục.",
         "Thời tiết lạnh có sương giá thường xuyên.",
         "Vùng biển nông nhiều bãi bùn lầy."),
        ("Vùng Đồng bằng sông Hồng có thế mạnh nổi bật hàng đầu nào sau đây so với các vùng khác trong cả nước?",
         "Lực lượng lao động dồi dào với trình độ học vấn, chuyên môn kĩ thuật cao nhất và mạng lưới đô thị dày đặc.",
         "Diện tích đất đỏ bazan rộng lớn nhất nước.",
         "Trữ lượng dầu khí dồi dào nhất thềm lục địa.",
         "Tài nguyên rừng nguyên sinh bạt ngàn."),
        ("Nguyên nhân chủ yếu làm cho ngành giao thông vận tải đường bộ nước ta phát triển nhanh chóng và hiện đại hóa vượt bậc là:",
         "Đầu tư mạnh mẽ vào các tuyến cao tốc huyết mạch Bắc - Nam và kết nối các vùng kinh tế trọng điểm.",
         "Số lượng xe đạp và xe máy tăng đột biến.",
         "Không còn sử dụng vận tải đường thủy.",
         "Địa hình nước ta hoàn toàn bằng phẳng không có sông núi cản trở."),
        ("Ngành du lịch nước ta phát triển bùng nổ trong những năm gần đây nhờ vào nhân tố chủ yếu nào?",
         "Tài nguyên du lịch phong phú, chính sách mở cửa visa thông thoáng, cơ sở hạ tầng dịch vụ lưu trú hiện đại.",
         "Giá vé máy bay luôn rẻ nhất thế giới.",
         "Chỉ đón khách du lịch nội địa.",
         "Khí hậu quanh năm không bao giờ có mưa bão."),
        ("Cơ cấu kinh tế theo thành phần kinh tế ở nước ta hiện nay bao gồm các khu vực nào?",
         "Kinh tế nhà nước, kinh tế tập thể, kinh tế tư nhân và kinh tế có vốn đầu tư nước ngoài (FDI).",
         "Chỉ gồm kinh tế nhà nước và kinh tế cá thể.",
         "Chỉ gồm các tập đoàn đa quốc gia nước ngoài.",
         "Kinh tế hợp tác xã đơn thuần."),
        ("Để nâng cao giá trị gia tăng và khả năng cạnh tranh của nông sản xuất khẩu, giải pháp hàng đầu của ngành nông nghiệp nước ta là:",
         "Đẩy mạnh ứng dụng công nghệ cao, phát triển nông nghiệp hữu cơ và công nghiệp chế biến sâu sau thu hoạch.",
         "Mở rộng tối đa diện tích đất gieo trồng bằng mọi giá.",
         "Chỉ xuất khẩu nông sản thô chưa qua sơ chế.",
         "Lạm dụng tối đa thuốc bảo vệ thực vật để diệt trừ sâu bệnh."),
        ("Trung tâm kinh tế, tài chính, khoa học công nghệ và dịch vụ hiện đại có quy mô lớn nhất nước ta hiện nay là:",
         "Thành phố Hồ Chí Minh.",
         "Thành phố Đà Nẵng.",
         "Thành phố Cần Thơ.",
         "Thành phố Hải Phòng."),
        ("Vùng kinh tế trọng điểm miền Trung gồm các tỉnh/thành phố ven biển từ:",
         "Thừa Thiên Huế, Đà Nẵng, Quảng Nam, Quảng Ngãi, Bình Định.",
         "Thanh Hóa, Nghệ An, Hà Tĩnh.",
         "Khánh Hòa, Ninh Thuận, Bình Thuận.",
         "Phú Yên, Đắk Lắk, Gia Lai."),
        ("Ý nghĩa kinh tế - an ninh quốc phòng to lớn nhất của các đảo và quần đảo trên Biển Đông đối với nước ta là gì?",
         "Là tiền tiêu bảo vệ chủ quyền biên giới biển đảo, căn cứ để tiến ra khai thác kinh tế biển sâu và kiểm soát các tuyến hàng hải.",
         "Là nơi xây dựng các nhà máy công nghiệp luyện thép nặng.",
         "Cung cấp toàn bộ nguồn nước ngọt sinh hoạt cho đất liền.",
         "Ngăn chặn hoàn toàn các cơn bão nhiệt đới từ Thái Bình Dương đổ bộ."),
        ("Bốn ngành kinh tế biển then chốt trong 'Chiến lược phát triển bền vững kinh tế biển Việt Nam đến năm 2030, tầm nhìn 2045' là:",
         "Du lịch biển; kinh tế hàng hải (cảng biển); khai thác dầu khí và khoáng sản biển; nuôi trồng và khai thác hải sản.",
         "Luyện kim màu, cơ khí đóng tàu, khai khoáng bauxit và may mặc.",
         "Sản xuất ô tô, điện tử viễn thông, hóa chất và giấy.",
         "Trồng lúa nước ngập mặn, làm gốm sứ và đan lát."),
        ("Đặc điểm khí hậu phân hóa sâu sắc thành hai mùa mưa - khô rõ rệt ở miền Nam nước ta là do tác động của:",
         "Gió mùa Tây Nam (mùa mưa) và Tín phong bán cầu Bắc (mùa khô).",
         "Gió mùa Đông Bắc lạnh khô thổi quanh năm.",
         "Dòng biển lạnh chạy dọc sát bờ biển.",
         "Địa hình chắn gió của dãy núi Hoàng Liên Sơn."),
        ("Thế mạnh tự nhiên lớn nhất để phát triển ngành công nghiệp nhiệt điện khí ở vùng Đông Nam Bộ là:",
         "Nguồn khí tự nhiên dồi dào từ các bể trầm tích thềm lục địa Cửu Long và Nam Côn Sơn (cụm Phú Mỹ, Nhơn Trạch).",
         "Mỏ than đá Quảng Ninh phong phú.",
         "Hệ thống sông suối có độ dốc lớn thuận lợi làm thủy điện.",
         "Tiềm năng quặng uranium dồi dào."),
        ("Biến đổi khí hậu toàn cầu đang gây ra thách thức môi trường nghiêm trọng nhất nào sau đây đối với vùng Đồng bằng sông Cửu Long?",
         "Nguy cơ sụt lún đất, nước biển dâng ngập úng và hạn mặn xâm nhập sâu vào nội đồng.",
         "Hiện tượng hoang mạc hóa do cát bay bao phủ.",
         "Hiện tượng núi lửa phun trào nham thạch.",
         "Bão tuyết và băng giá xuất hiện thường xuyên."),
        ("Nguyên nhân chủ yếu làm cho cơ cấu sử dụng lao động theo ngành ở nước ta chuyển dịch theo hướng tích cực là:",
         "Quá trình công nghiệp hóa, hiện đại hóa đất nước và thu hút mạnh dòng vốn đầu tư trực tiếp nước ngoài (FDI).",
         "Chính sách hạn chế người dân làm việc trong các khu công nghiệp.",
         "Lao động thanh niên không còn thích học nghề kĩ thuật.",
         "Sự gia tăng nhanh chóng của tỉ lệ lao động trong nông nghiệp."),
        ("Nhân tố kinh tế - xã hội nào sau đây có ý nghĩa quyết định nhất đến việc phân bố các trung tâm công nghiệp lớn ở nước ta?",
         "Thị trường tiêu thụ rộng lớn, nguồn lao động lành nghề dồi dào và cơ sở hạ tầng giao thông đồng bộ.",
         "Sự phong phú tuyệt đối của tài nguyên khoáng sản tại chỗ.",
         "Địa hình đồi núi dốc hiểm trở.",
         "Điều kiện thời tiết mát mẻ quanh năm."),
        ("Đẩy mạnh công nghiệp chế biến lương thực - thực phẩm ở các vùng chuyên canh nông nghiệp nước ta có tác dụng chủ yếu nào?",
         "Nâng cao giá trị thương phẩm nông sản, dễ bảo quản vận chuyển, tăng khả năng cạnh tranh và thúc đẩy sản xuất hàng hóa.",
         "Làm giảm chất lượng dinh dưỡng của nông sản tươi.",
         "Khiến nông dân bỏ ruộng đất hoang hóa.",
         "Tăng giá thành vận tải đường biển quốc tế.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_items, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)

    # ------------------ PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI ------------------
    add_section_header(doc, "PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)", 
                       "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

    # Câu 1: Cơ cấu kinh tế
    p1 = "Cho bảng số liệu: CƠ CẤU GDP THEO NGÀNH KINH TẾ CỦA VIỆT NAM NĂM 2010 VÀ NĂM 2023 (Đơn vị: %)\n- Nông, lâm, thủy sản: Năm 2010 là 18,9% -> Năm 2023 còn 11,9% (giảm 7,0%)\n- Công nghiệp và xây dựng: Năm 2010 là 38,2% -> Năm 2023 đạt 37,2%\n- Dịch vụ: Năm 2010 là 36,9% -> Năm 2023 đạt 42,5% (tăng 5,6%)\n- Thuế sản phẩm trừ trợ cấp sản phẩm: Năm 2010 là 6,0% -> Năm 2023 là 8,4%"
    stmts1 = [
        ("a", "Cơ cấu kinh tế nước ta đang chuyển dịch tích cực theo hướng giảm tỉ trọng khu vực nông - lâm - thủy sản và tăng tỉ trọng khu vực dịch vụ."),
        ("b", "Năm 2023, ngành công nghiệp và xây dựng chiếm tỉ trọng cao nhất trong cơ cấu GDP của cả nước."),
        ("c", "Tỉ trọng ngành nông nghiệp giảm đi chứng tỏ sản lượng và giá trị thực tế của nông sản Việt Nam đang bị sụt giảm tuyệt đối."),
        ("d", "Sự chuyển dịch cơ cấu ngành phản ánh rõ nét thành tựu của công cuộc công nghiệp hóa, hiện đại hóa và hội nhập quốc tế sâu rộng.")
    ]
    add_true_false_question(doc, 1, p1, stmts1)

    # Câu 2: Tài nguyên rừng
    p2 = "Rừng là lá phổi xanh bảo vệ môi trường sinh thái và là nguồn tài nguyên quý giá của đất nước. Nhờ nỗ lực thực hiện các chương trình mục tiêu quốc gia về trồng và phục hồi rừng (Dự án 5 triệu ha rừng, Đề án trồng 1 tỉ cây xanh), diện tích rừng của nước ta đã liên tục phục hồi, nâng độ che phủ rừng từ 27,8% (năm 1990) lên trên 42,0% hiện nay. Tuy nhiên, chất lượng rừng tự nhiên giàu gỗ quý vẫn còn thấp, diện tích rừng nghèo và rừng non mới phục hồi vẫn chiếm tỉ lệ lớn; nguy cơ cháy rừng trong mùa khô và phá rừng lấy đất làm nương rẫy ở một số vùng đồi núi dốc vẫn diễn biến phức tạp."
    stmts2 = [
        ("a", "Độ che phủ rừng của nước ta đã có sự phục hồi vượt bậc trong những thập kỉ gần đây."),
        ("b", "Mặc dù diện tích rừng tăng lên nhưng chất lượng rừng tự nhiên vẫn còn nhiều hạn chế cần tiếp tục phục hồi sinh thái."),
        ("c", "Trồng trọt độc canh cao su và keo lai có thể thay thế hoàn toàn chức năng phòng hộ đầu nguồn của rừng tự nhiên nguyên sinh."),
        ("d", "Bảo vệ rừng đầu nguồn là giải pháp căn cơ hữu hiệu để hạn chế lũ quét, sạt lở đất trong mùa mưa bão ở vùng núi cao.")
    ]
    add_true_false_question(doc, 2, p2, stmts2)

    # Câu 3: ĐBSCL & biến đổi khí hậu
    p3 = "Đồng bằng sông Cửu Long là vựa lúa, trái cây và thủy sản lớn nhất cả nước, đóng góp hơn 50% sản lượng lúa và 90% lượng gạo xuất khẩu của Việt Nam. Tuy nhiên, đây cũng là một trong những vùng đồng bằng châu thổ chịu tổn thương nặng nề nhất thế giới trước tác động của biến đổi khí hậu. Nghị quyết số 120/NQ-CP của Chính phủ về phát triển bền vững Đồng bằng sông Cửu Long thích ứng với biến đổi khí hậu đã đề ra phương châm hành động 'thuận thiên': chủ động thích ứng, biến thách thức thành thời cơ, chuyển đổi cơ cấu sản xuất nông nghiệp từ tư duy độc canh lúa nước sang mô hình sinh thái kinh tế nông nghiệp đa dạng (Thủy sản - Cây ăn trái - Lúa gạo)."
    stmts3 = [
        ("a", "Đồng bằng sông Cửu Long đóng vai trò rường cột số một đối với an ninh lương thực quốc gia và xuất khẩu gạo của Việt Nam."),
        ("b", "Phương châm 'thuận thiên' nghĩa là con người phó mặc hoàn toàn cho thiên nhiên mà không cần can thiệp bất kì công trình nào."),
        ("c", "Mô hình chuyển đổi kinh tế nông nghiệp theo thứ tự ưu tiên Thủy sản - Cây ăn trái - Lúa gạo giúp gia tăng giá trị kinh tế và thích nghi linh hoạt với nước mặn, nước lợ."),
        ("d", "Tình trạng thiếu nước ngọt và xâm nhập mặn ở ĐBSCL còn do tác động của các đập thủy điện bậc thang ở thượng nguồn sông Mê Kông tích nước trong mùa khô.")
    ]
    add_true_false_question(doc, 3, p3, stmts3)

    # Câu 4: Kinh tế biển & chủ quyền hải đảo
    p4 = "Vùng biển Việt Nam có diện tích trên 1 triệu km² ở Biển Đông, bao gồm hàng nghìn hòn đảo lớn nhỏ và hai quần đảo Hoàng Sa, Trường Sa. Nghị quyết số 36-NQ/TW của Ban Chấp hành Trung ương Đảng (Khóa XII) về 'Chiến lược phát triển bền vững kinh tế biển Việt Nam đến năm 2030, tầm nhìn đến năm 2045' đã xác định mục tiêu đưa Việt Nam trở thành quốc gia biển mạnh, phát triển bền vững, thịnh vượng, an ninh, an toàn; gắn kết chặt chẽ phát triển kinh tế biển với quản lí bảo vệ chủ quyền biển đảo thiêng liêng của Tổ quốc, bảo tồn đa dạng sinh học các hệ sinh thái biển (rạn san hô, rừng ngập mặn, cỏ biển) và ứng phó với biến đổi khí hậu."
    stmts4 = [
        ("a", "Phát triển kinh tế biển của nước ta phải luôn gắn liền hữu cơ với nhiệm vụ bảo vệ chủ quyền và an ninh quốc phòng biển đảo."),
        ("b", "Việt Nam chủ trương đẩy mạnh khai thác tận diệt hải sản ven bờ bằng chất nổ và xung điện để đạt mục tiêu kinh tế biển mạnh."),
        ("c", "Bảo tồn các hệ sinh thái rạn san hô và rừng ngập mặn ven biển là yếu tố then chốt bảo đảm phát triển du lịch sinh thái và nghề cá bền vững."),
        ("d", "Các đảo và quần đảo tiền tiêu như Cô Tô, Cát Bà, Bạch Long Vĩ, Phú Quý, Côn Đảo, Phú Quốc là những trung tâm kinh tế biển năng động kết hợp căn cứ phòng thủ vững chắc trên biển.")
    ]
    add_true_false_question(doc, 4, p4, stmts4)

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    tf_answers = [
        ("Câu 1", "Đúng", "Sai", "Sai", "Đúng"),
        ("Câu 2", "Đúng", "Đúng", "Sai", "Đúng"),
        ("Câu 3", "Đúng", "Sai", "Đúng", "Đúng"),
        ("Câu 4", "Đúng", "Sai", "Đúng", "Đúng")
    ]
    
    add_answers_section(doc, mcq_answers, tf_answers=tf_answers)
    
    file_path = os.path.join(OUTPUT_DIR, "De_08_Lop_12_Dia_Li_Thi_Tot_Nghiep_THPT_Chuan_BGD.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

if __name__ == "__main__":
    generate_grade_10_history()
    generate_grade_10_geography()
    generate_grade_12_history()
    generate_grade_12_geography()
    print("All THPT exams generated successfully.")
