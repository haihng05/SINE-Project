# -*- coding: utf-8 -*-
"""
gen_thcs_exams.py
Generates comprehensive, standard Word (.docx) exam papers for Secondary School (THCS):
Grades 6, 7, 8, 9 (Lịch sử và Địa lí - CT GDPT 2018).
"""
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(__file__))

from exam_builder_base import (
    create_styled_document, add_exam_header, add_section_header,
    add_mcq_question, add_essay_question, add_exam_footer_mark,
    add_answers_section
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "De_Thi_Lich_Su_Dia_Ly")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================================================================
# 1. ĐỀ KIỂM TRA LỚP 6 - CUỐI HỌC KÌ I
# ==============================================================================
def generate_grade_6_exam():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="TRƯỜNG THCS NGUYỄN DU",
        exam_title="ĐỀ KIỂM TRA ĐÁNH GIÁ CUỐI HỌC KÌ I - NĂM HỌC 2025 - 2026",
        subject_title="LỊCH SỬ VÀ ĐỊA LÍ - KHỐI 6 (BỘ SÁCH KẾT NỐI TRI THỨC)",
        duration_str="60 phút",
        exam_code="601"
    )
    
    # ------------------ PHẦN I: TRẮC NGHIỆM ------------------
    add_section_header(doc, "A. PHÂN MÔN LỊCH SỬ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - Mỗi câu trả lời đúng được 0,25 điểm)")
    
    mcq_history = [
        ("Dấu tích đầu tiên của Người tối cổ trên lãnh thổ Việt Nam được tìm thấy dưới dạng công cụ đá ghè đẽo thô sơ tại đâu?",
         "An Khê (Gia Lai) và Núi Đọ (Thanh Hóa).",
         "Hang Con Moong (Thanh Hóa).",
         "Văn hóa Đông Sơn (Thanh Hóa).",
         "Văn hóa Sa Huỳnh (Quảng Ngãi)."),
        ("Tổ chức xã hội đầu tiên của loài người sau khi tiến hóa thành Người tinh khôn là gì?",
         "Thị tộc và bộ lạc.", "Nhà nước sơ khai.", "Thành bang cổ đại.", "Gia đình phụ hệ."),
        ("Nền văn minh Ai Cập cổ đại đã hình thành và phát triển gắn liền với dòng sông nào?",
         "Sông Nin (Nile).", "Sông Ti-gơ-rơ.", "Sông Ấn (Indus).", "Sông Hoàng Hà."),
        ("Thành tựu văn hóa tiêu biểu nào sau đây của cư dân Lưỡng Hà cổ đại có ý nghĩa pháp lí lớn nhất đối với lịch sử nhân loại?",
         "Bộ luật Ham-mu-ra-bi.", "Kim tự tháp Kê-ốp.", "Chữ viết tượng hình trên giấy Pa-pi-rút.", "Hệ thống số La Mã."),
        ("Chế độ phân biệt đẳng cấp khắc nghiệt Vác-na (Varna) là đặc trưng xã hội của quốc gia cổ đại nào?",
         "Ấn Độ cổ đại.", "Hy Lạp cổ đại.", "Trung Quốc cổ đại.", "La Mã cổ đại."),
        ("Ai là người có công đánh dẹp 6 nước chư hầu, chấm dứt thời Chiến quốc và lập nên triều đại phong kiến tập quyền đầu tiên ở Trung Quốc?",
         "Tần Thủy Hoàng.", "Hán Cao Tổ Lưu Bang.", "Khổng Tử.", "Tần Nhị Thế."),
        ("Kinh đô của nhà nước Văn Lang - nhà nước đầu tiên trong lịch sử dân tộc Việt Nam đặt tại đâu?",
         "Phong Châu (Phú Thọ ngày nay).", "Cổ Loa (Đông Anh, Hà Nội).", "Hoa Lư (Ninh Bình).", "Mê Linh (Hà Nội)."),
        ("Thành tựu quân sự kiệt xuất chứng minh đỉnh cao của kĩ thuật luyện kim và kiến trúc quân sự thời Âu Lạc là:",
         "Thành Cổ Loa và nỏ liên châu bắn nhiều mũi tên.", "Thành nhà Hồ và súng thần cơ.", "Trận địa cọc Bạch Đằng.", "Trống đồng Ngọc Lũ.")
    ]
    
    for i, (q, a, b, c, d) in enumerate(mcq_history, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)
        
    # Tự luận Lịch sử (3.0 điểm)
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Phần 2: Tự luận Lịch sử (3,0 điểm)")
    r_sub.font.bold = True
    
    add_essay_question(doc, 9, "1,5 điểm", 
                       "Trình bày đời sống vật chất (nguồn lương thực chính, nơi ở, trang phục) và đời sống tinh thần (tín ngưỡng, phong tục) của cư dân Văn Lang - Âu Lạc.")
    add_essay_question(doc, 10, "1,5 điểm", 
                       "Từ sự thất bại của nước Âu Lạc trước cuộc xâm lược của Triệu Đà (năm 179 TCN), bài học lịch sử sâu sắc nhất về công cuộc giữ nước và bảo vệ an ninh quốc gia cho thế hệ trẻ ngày nay là gì?")

    # ------------------ PHẦN B: PHÂN MÔN ĐỊA LÍ ------------------
    add_section_header(doc, "B. PHÂN MÔN ĐỊA LÍ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - Mỗi câu trả lời đúng được 0,25 điểm)")
    
    mcq_geo = [
        ("Trong hệ Mặt Trời, theo thứ tự xa dần Mặt Trời, Trái Đất nằm ở vị trí thứ mấy?",
         "Thứ ba.", "Thứ nhất.", "Thứ hai.", "Thứ tư."),
        ("Trái Đất có dạng hình gì?",
         "Hình cầu (hơi dẹt ở hai cực).", "Hình tròn dẹt.", "Hình bầu dục hoàn hảo.", "Hình nón cụt."),
        ("Hiện tượng ngày đêm luân phiên kế tiếp nhau trên Trái Đất là do nguyên nhân nào sau đây?",
         "Trái Đất có hình cầu và tự quay quanh trục từ Tây sang Đông.",
         "Trái Đất chuyển động tịnh tiến quanh Mặt Trời.",
         "Mặt Trời mọc ở hướng Đông và lặn ở hướng Tây.",
         "Trục Trái Đất luôn nghiêng 66 độ 33 phút so với mặt phẳng quỹ đạo."),
        ("Nếu ở khu vực giờ gốc (GMT/UTC, kinh tuyến số 0) đang là 12 giờ trưa thì ở Thủ đô Hà Nội (Việt Nam thuộc múi giờ số 7) lúc đó là mấy giờ?",
         "19 giờ cùng ngày.", "5 giờ sáng cùng ngày.", "24 giờ đêm.", "7 giờ sáng."),
        ("Trên quả Địa Cầu, đường xích đạo (vĩ tuyến 0 độ) có đặc điểm nào sau đây?",
         "Là vĩ tuyến dài nhất, chia Trái Đất thành bán cầu Bắc và bán cầu Nam.",
         "Là kinh tuyến gốc đi qua đài thiên văn Grin-uýt.",
         "Là vòng cực Bắc có băng tuyết bao phủ.",
         "Nối liền hai điểm cực Bắc và cực Nam."),
        ("Cấu tạo bên trong của Trái Đất gồm có mấy lớp chính (tính từ ngoài vào trong)?",
         "3 lớp: Vỏ Trái Đất, man-ti và nhân Trái Đất.",
         "2 lớp: Lớp vỏ và lớp lõi kim loại.",
         "4 lớp: Thạch quyển, khí quyển, thủy quyển và sinh quyển.",
         "5 lớp trầm tích biến chất."),
        ("Quá trình nội lực sinh ra các hiện tượng nào sau đây trên bề mặt Trái Đất?",
         "Động đất, núi lửa và các đứt gãy uốn nếp nâng hạ địa hình.",
         "Quá trình phong hóa đá do nhiệt độ và nước mưa.",
         "Quá trình bồi tụ phù sa tạo nên đồng bằng châu thổ.",
         "Quá trình xâm thực do dòng chảy sông ngòi."),
        ("Kí hiệu đường xá, ranh giới quốc gia, sông ngòi trên bản đồ thuộc loại kí hiệu nào?",
         "Kí hiệu đường.", "Kí hiệu điểm.", "Kí hiệu diện tích.", "Kí hiệu hình học.")
    ]
    
    for i, (q, a, b, c, d) in enumerate(mcq_geo, start=11):
        add_mcq_question(doc, i, q, a, b, c, d)

    # Tự luận Địa lí (3.0 điểm)
    p_sub_g = doc.add_paragraph()
    r_sub_g = p_sub_g.add_run("Phần 2: Tự luận Địa lí (3,0 điểm)")
    r_sub_g.font.bold = True
    
    add_essay_question(doc, 19, "2,0 điểm", 
                       "Giải thích tại sao trên Trái Đất lại sinh ra các mùa (Xuân, Hạ, Thu, Đông) trong năm? Tại sao mùa nóng và mùa lạnh ở hai bán cầu Bắc và Nam lại đối lập nhau?")
    add_essay_question(doc, 20, "1,0 điểm", 
                       "Nêu các biện pháp phòng chống và giảm nhẹ thiệt hại khi có hiện tượng động đất xảy ra nếu em đang ở trong lớp học hoặc ở nhà cao tầng.")

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", # 1-8 Lịch sử
        "A", "A", "A", "A", "A", "A", "A", "A"  # 11-18 Địa lí (tương ứng 9-16 trong bảng)
    ]
    
    rubric = [
        ("Câu 9\n(1,5 đ)", 
         "- Đời sống vật chất: Thức ăn chính là gạo nếp, gạo tẻ, cá, rau, thịt. Ở nhà sàn làm bằng gỗ, tre, nứa để tránh thú dữ và ngập lụt. Trang phục: nam đóng khố mình trần, nữ mặc váy, áo xẻ ngực. (0,75đ)\n"
         "- Đời sống tinh thần: Tín ngưỡng sùng bái tự nhiên (thờ thần Mặt Trời, thần Sông, thần Núi) và thờ cúng tổ tiên, các anh hùng có công; phong tục xăm mình, nhuộm răng đen, ăn trầu, làm bánh chưng, bánh giầy. (0,75đ)",
         "1,5 điểm"),
        ("Câu 10\n(1,5 đ)",
         "- Nguyên nhân thất bại: Do An Dương Vương chủ quan mất cảnh giác trước âm mưu gian xảo 'cầu hòa - gả con' của Triệu Đà, nội bộ bất hòa, tướng giỏi rời bỏ. (0,75đ)\n"
         "- Bài học cho thế hệ trẻ: Phải luôn đề cao tinh thần cảnh giác cách mạng, bảo vệ bí mật quốc gia; củng cố khối đại đoàn kết toàn dân tộc; ra sức học tập, rèn luyện để xây dựng đất nước vững mạnh. (0,75đ)",
         "1,5 điểm"),
        ("Câu 19\n(2,0 đ)",
         "- Nguyên nhân sinh ra các mùa: Khi Trái Đất chuyển động tịnh tiến quanh Mặt Trời, do trục Trái Đất nghiêng một góc 66°33' không đổi hướng so với mặt phẳng quỹ đạo, làm cho lần lượt bán cầu Bắc và bán cầu Nam ngả về phía Mặt Trời. (1,0đ)\n"
         "- Giải thích sự trái ngược: Bán cầu nào ngả về phía Mặt Trời nhận được nhiều góc chiếu và nhiệt -> mùa nóng; đồng thời bán cầu kia chếch xa Mặt Trời nhận được ít góc chiếu -> mùa lạnh. Vì thế hai bán cầu luôn có mùa trái ngược nhau. (1,0đ)",
         "2,0 điểm"),
        ("Câu 20\n(1,0 đ)",
         "- Biện pháp khi đang ở trong phòng: Nhanh chóng tìm chỗ trú ẩn dưới gầm bàn vững chắc, góc tường chịu lực, dùng tay hoặc cặp sách bảo vệ đầu; tránh xa cửa kính, đèn chùm, đồ đạc dễ đổ vỡ. (0,5đ)\n"
         "- Tuyệt đối không dùng thang máy, không chen lấn xô đẩy ở cầu thang bộ; bình tĩnh chờ rung lắc chấm dứt rồi di tản ra bãi đất trống an toàn. (0,5đ)",
         "1,0 điểm")
    ]
    
    add_answers_section(doc, mcq_answers, essay_rubric=rubric)
    
    file_path = os.path.join(OUTPUT_DIR, "De_01_Lop_6_Lich_Su_va_Dia_Li_Hoc_Ky_1.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 2. ĐỀ KIỂM TRA LỚP 7 - CUỐI HỌC KÌ II
# ==============================================================================
def generate_grade_7_exam():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="TRƯỜNG THCS TRẦN PHÚ",
        exam_title="ĐỀ KIỂM TRA ĐÁNH GIÁ CUỐI HỌC KÌ II - NĂM HỌC 2025 - 2026",
        subject_title="LỊCH SỬ VÀ ĐỊA LÍ - KHỐI 7 (BỘ SÁCH CÁNH DIỀU)",
        duration_str="60 phút",
        exam_code="702"
    )
    
    # ------------------ PHẦN I: LỊCH SỬ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "A. PHÂN MÔN LỊCH SỬ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - 8 câu)")
    
    mcq_history = [
        ("Chiến thắng vĩ đại nào vào năm 1288 đã đè bẹp hoàn toàn ý chí xâm lược Đại Việt lần thứ ba của đế chế Mông - Nguyên?",
         "Chiến thắng Bạch Đằng.", "Chiến thắng Đông Bộ Đầu.", "Chiến thắng Như Nguyệt.", "Chiến thắng Ngọc Hồi - Đống Đa."),
        ("Câu nói nổi tiếng: 'Nếu bệ hạ muốn hàng giặc, xin trước hãy chém đầu thần rồi hãy hàng' là của vị anh hùng dân tộc nào?",
         "Trần Hưng Đạo (Trần Quốc Tuấn).", "Trần Thủ Độ.", "Trần Quang Khải.", "Trần Quốc Toản."),
        ("Vị vua đầu tiên sáng lập nên triều đại nhà Tiền Lê sau khi dẹp loạn và đánh bại quân Tống năm 981 là ai?",
         "Lê Hoàn (Lê Đại Hành).", "Lê Thái Tổ (Lê Lợi).", "Lê Thánh Tông.", "Đinh Bộ Lĩnh."),
        ("Năm 1400, Hồ Quý Ly lên ngôi lập ra triều Hồ, ông đã đổi quốc hiệu Đại Việt thành tên gì?",
         "Đại Ngu.", "Vạn Xuân.", "Đại Cồ Việt.", "Việt Nam."),
        ("Cuộc khởi nghĩa Lam Sơn (1418 - 1427) bùng nổ nhằm đánh đuổi thế lực phong kiến xâm lược nào?",
         "Quân xâm lược nhà Minh.", "Quân xâm lược nhà Thanh.", "Quân Mông Cổ.", "Quân Tống."),
        ("Ai là tác giả của áng thiên cổ hùng văn 'Bình Ngô đại cáo' tuyên bố nền độc lập tự chủ của Đại Việt sau khởi nghĩa Lam Sơn?",
         "Nguyễn Trãi.", "Lê Lợi.", "Lê Văn Hưu.", "Chu Văn An."),
        ("Thời Lê sơ, tôn giáo nào được đề cao chiếm vị trí độc tôn trong hệ tư tưởng và giáo dục thi cử?",
         "Nho giáo.", "Phật giáo.", "Đạo giáo.", "Kitô giáo."),
        ("Bộ luật thành văn hoàn chỉnh và tiến bộ nhất thời phong kiến Việt Nam được ban hành dưới thời vua Lê Thánh Tông là:",
         "Quốc triều hình luật (Luật Hồng Đức).", "Hình thư thời Lý.", "Hoàng Việt luật lệ (Luật Gia Long).", "Hình luật thời Trần.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_history, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)
        
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Phần 2: Tự luận Lịch sử (3,0 điểm)")
    r_sub.font.bold = True
    
    add_essay_question(doc, 9, "2,0 điểm", 
                       "Phân tích nguyên nhân thắng lợi của ba lần kháng chiến chống quân xâm lược Mông - Nguyên dưới thời Trần (thế kỉ XIII). Nghệ thuật quân sự 'vườn không nhà trống' được quân dân nhà Trần vận dụng sáng tạo như thế nào?")
    add_essay_question(doc, 10, "1,0 điểm", 
                       "Đánh giá công lao của vua Lê Thánh Tông đối với sự phát triển rực rỡ của đất nước trên các lĩnh vực kinh tế, văn hóa và giáo dục.")

    # ------------------ PHẦN II: ĐỊA LÍ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "B. PHÂN MÔN ĐỊA LÍ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - 8 câu)")
    
    mcq_geo = [
        ("Châu Mỹ được ngăn cách với châu Á bởi eo biển nào sau đây?",
         "Eo biển Bê-rinh (Bering).", "Eo biển Ma-ghen-lăng.", "Eo biển Ma-lắc-ca.", "Eo biển Gibratar."),
        ("Hệ thống núi trẻ đồ sộ, hiểm trở chạy dọc phía Tây Bắc Mỹ là dãy núi nào?",
         "Dãy Coóc-đi-e (Cordillera) / Rốc-ki (Rocky).", "Dãy An-pơ (Alps).", "Dãy An-đét (Andes).", "Dãy Hia-ma-lay-a."),
        ("Rừng nhiệt đới A-ma-dôn (Amazon) - 'lá phổi xanh của Trái Đất' phân bố chủ yếu ở khu vực nào?",
         "Nam Mỹ (lưu vực sông A-ma-dôn).", "Bắc Mỹ.", "Tây Âu.", "Trung Phi."),
        ("Các đô thị có quy mô dân số trên 10 triệu người (siêu đô thị) ở Bắc Mỹ gồm những thành phố nào?",
         "Niu Oóc (New York), Lốt An-giơ-lét (Los Angeles).",
         "Oa-sinh-tơn, Xan Phran-xi-xcô.",
         "Môn-trê-an, Ôt-ta-oa.",
         "Chi-ca-gô, Hiu-xtơn."),
        ("Đặc điểm nổi bật nhất của khí hậu châu Nam Cực là gì?",
         "Khí hậu lạnh giá khắc nghiệt bậc nhất địa cầu quanh năm, nhiều bão tuyết.",
         "Nhiệt đới gió mùa nóng ẩm quanh năm.",
         "Khí hậu ôn đới hải dương mưa nhiều.",
         "Khí hậu hoang mạc khô nóng cát bay."),
        ("Động vật đặc trưng thích nghi cao với băng giá ở châu Nam Cực là loài nào?",
         "Chim cánh cụt.", "Gấu trắng Bắc Cực.", "Hươu cao cổ.", "Chuột túi Căng-gu-ru."),
        ("Nguyên nhân chính dẫn đến tình trạng suy giảm nghiêm trọng diện tích rừng A-ma-dôn hiện nay là do:",
         "Chặt phá rừng lấy đất canh tác, chăn nuôi gia súc và cháy rừng nhân tạo.",
         "Hiện tượng biến đổi khí hậu làm tuyết tan.",
         "Trồng quá nhiều cây công nghiệp che bóng.",
         "Lũ lụt tràn qua cuốn trôi cây cối."),
        ("Hiệp ước Nam Cực được kí kết năm 1959 nhằm mục đích cao nhất là gì?",
         "Duy trì Nam Cực vì mục đích hòa bình, tự do nghiên cứu khoa học, phi quân sự hóa.",
         "Phân chia chủ quyền lãnh thổ giữa các nước lớn.",
         "Khai thác triệt để dầu mỏ và than đá tại đây.",
         "Xây dựng các căn cứ thử nghiệm vũ khí hạt nhân.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_geo, start=11):
        add_mcq_question(doc, i, q, a, b, c, d)

    p_sub_g = doc.add_paragraph()
    r_sub_g = p_sub_g.add_run("Phần 2: Tự luận Địa lí (3,0 điểm)")
    r_sub_g.font.bold = True
    
    add_essay_question(doc, 19, "2,0 điểm", 
                       "Tại sao việc bảo vệ rừng nhiệt đới A-ma-dôn lại là vấn đề cấp bách mang tính toàn cầu chứ không riêng của các nước Nam Mỹ? Nêu những hệ quả nghiêm trọng nếu rừng A-ma-dôn tiếp tục bị tàn phá.")
    add_essay_question(doc, 20, "1,0 điểm", 
                       "Giải thích vì sao châu Nam Cực được mệnh danh là 'cực lạnh của Trái Đất' và 'sa mạc lạnh'?")

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    rubric = [
        ("Câu 9\n(2,0 đ)",
         "- Nguyên nhân thắng lợi: Sự đoàn kết thống nhất toàn dân (vua tôi đồng lòng, anh em hòa mục); tài chỉ huy mưu lược kiệt xuất của các danh tướng nhà Trần (Trần Hưng Đạo, Trần Quang Khải...); đường lối chiến lược quân sự đúng đắn. (1,0đ)\n"
         "- Nghệ thuật 'vườn không nhà trống': Khi thế giặc mạnh, quân ta chủ động rút lui, sơ tán người và của cải, triệt phá lương thảo khiến giặc rơi vào cảnh thiếu đói, mệt mỏi, suy sụp tinh thần, sau đó ta phản công chớp nhoáng tiêu diệt đầu não quân giặc. (1,0đ)",
         "2,0 điểm"),
        ("Câu 10\n(1,0 đ)",
         "- Vua Lê Thánh Tông ban hành Luật Hồng Đức, chấn chỉnh bộ máy quan lại liêm chính, khuyến khích nông nghiệp mở rộng đồn điền. (0,5đ)\n"
         "- Mở mang trường học, tổ chức nhiều kì thi chọn nhân tài; sáng lập Hội Tao Đàn, để lại nhiều di sản văn hóa thơ phú rực rỡ, đưa Đại Việt đạt đỉnh cao thịnh trị thời phong kiến. (0,5đ)",
         "1,0 điểm"),
        ("Câu 19\n(2,0 đ)",
         "- Tầm quan trọng toàn cầu: A-ma-dôn cung cấp khoảng 20% lượng dưỡng khí (oxy) cho khí quyển, hấp thụ lượng lớn khí CO2 giúp điều hòa khí hậu toàn cầu; là kho dự trữ sinh học đa dạng nhất thế giới với hàng triệu loài sinh vật. (1,0đ)\n"
         "- Hậu quả khi bị tàn phá: Gia tăng hiệu ứng nhà kính, thúc đẩy biến đổi khí hậu và nước biển dâng; mất cân bằng sinh thái, tuyệt chủng nhiều nguồn gen quý hiếm, sạt lở xói mòn đất và suy giảm nguồn nước ngọt. (1,0đ)",
         "2,0 điểm"),
        ("Câu 20\n(1,0 đ)",
         "- Cực lạnh: Vị trí vùng cực nhận được góc chiếu Mặt Trời cực nhỏ quanh năm; bề mặt phủ lớp băng tuyết dày phản xạ hầu hết nhiệt lượng Mặt Trời; độ cao trung bình lớn (>2000m). (0,5đ)\n"
         "- Sa mạc lạnh: Do áp cao ngự trị thường xuyên, không khí cực khô, lượng mưa tuyết hàng năm rất thấp (<200mm/năm), môi trường sống vô cùng khắc nghiệt không cây cỏ nào sống được. (0,5đ)",
         "1,0 điểm")
    ]
    
    add_answers_section(doc, mcq_answers, essay_rubric=rubric)
    
    file_path = os.path.join(OUTPUT_DIR, "De_02_Lop_7_Lich_Su_va_Dia_Li_Hoc_Ky_2.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 3. ĐỀ KIỂM TRA LỚP 8 - CUỐI HỌC KÌ I
# ==============================================================================
def generate_grade_8_exam():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="TRƯỜNG THCS LÊ QUÝ ĐÔN",
        exam_title="ĐỀ KIỂM TRA ĐÁNH GIÁ CUỐI HỌC KÌ I - NĂM HỌC 2025 - 2026",
        subject_title="LỊCH SỬ VÀ ĐỊA LÍ - KHỐI 8 (CHƯƠNG TRÌNH GDPT 2018)",
        duration_str="60 phút",
        exam_code="801"
    )
    
    # ------------------ PHẦN I: LỊCH SỬ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "A. PHÂN MÔN LỊCH SỬ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - 8 câu)")
    
    mcq_history = [
        ("Cuộc cách mạng tư sản đầu tiên trên thế giới bùng nổ dưới hình thức chiến tranh giải phóng dân tộc là cuộc cách mạng nào?",
         "Chiến tranh giành độc lập của 13 thuộc địa Anh ở Bắc Mỹ.",
         "Cách mạng tư sản Hà Lan.",
         "Cách mạng tư sản Anh.",
         "Cách mạng tư sản Pháp 1789."),
        ("Văn kiện lịch sử nổi tiếng khẳng định: 'Mọi người sinh ra đều có quyền bình đẳng, quyền được sống, quyền tự do và quyền mưu cầu hạnh phúc' là:",
         "Tuyên ngôn Độc lập của Hợp chúng quốc Hoa Kỳ (1776).",
         "Tuyên ngôn Nhân quyền và Dân quyền Pháp (1789).",
         "Tuyên ngôn của Đảng Cộng sản (1848).",
         "Hiến pháp Hoa Kỳ năm 1787."),
        ("Cuộc cách mạng tư sản nào được đánh giá là 'triệt để nhất' thời cận đại với đỉnh cao chuyên chính Gia-cô-banh?",
         "Cách mạng tư sản Pháp (1789 - 1794).",
         "Cách mạng tư sản Anh thế kỉ XVII.",
         "Cuộc Minh Trị duy tân ở Nhật Bản.",
         "Nội chiến ở Mỹ (1861 - 1865)."),
        ("Sự kiện mở đầu cuộc Cách mạng tư sản Pháp ngày 14/7/1789 là cuộc tấn công vào pháo đài nào?",
         "Pháo đài Ba-xti (Bastille).", "Cung điện Véc-xai.", "Cung điện Tuyn-lơ-ri.", "Tòa thị chính Pa-ri."),
        ("Phát minh nào mở đầu cho cuộc Cách mạng công nghiệp lần thứ nhất ở nước Anh vào nửa sau thế kỉ XVIII?",
         "Máy kéo sợi Gien-ni của Giêm Ha-gri-vơ.",
         "Máy hơi nước của Giêm Oát.",
         "Đầu máy xe lửa của Xti-phen-xơn.",
         "Tàu thủy chở khách chạy bằng hơi nước."),
        ("Tổ chức quốc tế đầu tiên của phong trào công nhân do Các Mác và Ăng-ghen sáng lập là:",
         "Quốc tế thứ nhất (Hội Liên hiệp Lao động quốc tế).",
         "Quốc tế thứ hai.",
         "Đồng minh những người cộng sản.",
         "Quốc tế Cộng sản (Quốc tế thứ ba)."),
        ("Đến cuối thế kỉ XIX - đầu thế kỉ XX, hầu hết các quốc gia ở Đông Nam Á đều trở thành thuộc địa của thực dân phương Tây, ngoại trừ nước nào?",
         "Xiêm (Thái Lan).", "Miến Điện (My-an-ma).", "Phi-líp-pin.", "Mã Lai."),
        ("Ở Việt Nam thế kỉ XVII - XVIII, sự chia cắt Đàng Trong và Đàng Ngoài lấy địa danh nào làm giới tuyến ngăn cách?",
         "Sông Gianh (Quảng Bình).", "Sông Bến Hải (Quảng Trị).", "Đèo Hải Vân.", "Sông Lam (Nghệ An).")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_history, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)
        
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Phần 2: Tự luận Lịch sử (3,0 điểm)")
    r_sub.font.bold = True
    
    add_essay_question(doc, 9, "2,0 điểm", 
                       "Trình bày tác động sâu sắc của cuộc Cách mạng công nghiệp lần thứ nhất đối với sản xuất kinh tế và làm thay đổi cơ cấu xã hội tư bản chủ nghĩa.")
    add_essay_question(doc, 10, "1,0 điểm", 
                       "Tại sao Xiêm (Thái Lan) là quốc gia duy nhất ở Đông Nam Á giữ được nền độc lập tương đối trước sự xâm lược của các đế quốc phương Tây cuối thế kỉ XIX?")

    # ------------------ PHẦN II: ĐỊA LÍ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "B. PHÂN MÔN ĐỊA LÍ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,0 điểm - 8 câu)")
    
    mcq_geo = [
        ("Vị trí địa lí của nước ta nằm trọn vẹn trong vùng đai khí hậu nào?",
         "Vùng nội chí tuyến bán cầu Bắc.", "Vùng ôn đới cận nhiệt đới.", "Vùng xích đạo ẩm.", "Vùng hàn đới."),
        ("Đường bờ biển của Việt Nam có chiều dài khoảng bao nhiêu ki-lô-mét và cong theo hình chữ gì?",
         "Dài 3.260 km, cong hình chữ S.", "Dài 4.450 km, hình chữ C.", "Dài 2.360 km, hình chữ U.", "Dài 5.000 km, hình dải lụa."),
        ("Điểm cực Đông trên đất liền của nước ta thuộc xã Vạn Thạnh, huyện Vạn Ninh thuộc tỉnh nào?",
         "Khánh Hòa (Mũi Đôi).", "Bình Thuận (Mũi Kê Gà).", "Phú Yên (Mũi Điện).", "Ninh Thuận (Mũi Dinh)."),
        ("Đặc điểm cơ bản nhất của địa hình Việt Nam là gì?",
         "Đồi núi chiếm 3/4 diện tích lãnh thổ, nhưng chủ yếu là đồi núi thấp.",
         "Đồng bằng chiếm 3/4 diện tích, đồi núi chiếm 1/4 diện tích.",
         "Địa hình núi cao trên 2.000m chiếm ưu thế tuyệt đối.",
         "Địa hình nghiêng dốc theo hướng Đông Bắc - Tây Nam."),
        ("Hai hướng chính của địa hình Việt Nam là:",
         "Hướng Tây Bắc - Đông Nam và hướng vòng cung.",
         "Hướng Bắc - Nam và hướng Tây - Đông.",
         "Hướng Đông Bắc - Tây Nam và hình nan quạt.",
         "Hướng Tây Nam - Đông Bắc và dạng mắt cáo."),
        ("Đỉnh núi Pan-xi-păng (Phan-xi-păng) cao 3.143m - được mệnh danh là 'nóc nhà Đông Dương' thuộc dãy núi nào?",
         "Dãy Hoàng Liên Sơn.", "Dãy Trường Sơn Bắc.", "Dãy Trường Sơn Nam.", "Dãy Bạch Mã."),
        ("Bể than đá có trữ lượng lớn nhất và chất lượng tốt nhất nước ta phân bố chủ yếu ở tỉnh nào?",
         "Quảng Ninh.", "Thái Nguyên.", "Lạng Sơn.", "Bà Rịa - Vũng Tàu."),
        ("Dầu mỏ và khí đốt tự nhiên của nước ta tập trung nhiều nhất ở đâu?",
         "Thềm lục địa phía Nam (bể Cửu Long, Nam Côn Sơn...).",
         "Vùng đồng bằng sông Hồng.",
         "Khu vực ven biển miền Trung.",
         "Vùng trung du miền núi Bắc Bộ.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_geo, start=11):
        add_mcq_question(doc, i, q, a, b, c, d)

    p_sub_g = doc.add_paragraph()
    r_sub_g = p_sub_g.add_run("Phần 2: Tự luận Địa lí (3,0 điểm)")
    r_sub_g.font.bold = True
    
    add_essay_question(doc, 19, "2,0 điểm", 
                       "Chứng minh rằng địa hình nước ta là địa hình già được trẻ lại và có tính chất phân bậc rõ rệt theo độ cao. Địa hình đồi núi có những thuận lợi và khó khăn gì đối với sự phát triển kinh tế - xã hội?")
    add_essay_question(doc, 20, "1,0 điểm", 
                       "Tại sao chúng ta phải sử dụng hợp lí và tiết kiệm tài nguyên khoáng sản? Nêu 3 giải pháp thiết thực để bảo vệ nguồn tài nguyên này.")

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A", "A", "A", "A"
    ]
    
    rubric = [
        ("Câu 9\n(2,0 đ)",
         "- Về kinh tế: Thay thế lao động thủ công bằng máy móc, năng suất lao động tăng vọt, thúc đẩy các ngành công nghiệp dệt, cơ khí, giao thông đường sắt phát triển; làm xuất hiện nhiều trung tâm công nghiệp lớn và thành phố sầm uất. (1,0đ)\n"
         "- Về xã hội: Hình thành hai giai cấp cơ bản đối lập nhau sâu sắc trong xã hội tư bản là giai cấp tư sản (nắm tư liệu sản xuất) và giai cấp vô sản (bán sức lao động, bị bóc lột nặng nề), dẫn đến phong trào đấu tranh của công nhân bùng nổ mạnh mẽ. (1,0đ)",
         "2,0 điểm"),
        ("Câu 10\n(1,0 đ)",
         "- Xiêm thực hiện chính sách ngoại giao khôn khéo 'cây tre uốn đầu theo gió', biết lợi dụng mâu thuẫn giữa hai đế quốc Anh và Pháp. (0,5đ)\n"
         "- Tiến hành canh tân đất nước toàn diện dưới thời vua Chu-la-long-con (Rama V) về hành chính, kinh tế, quân sự, giúp tiềm lực quốc gia nâng cao và giữ được độc lập. (0,5đ)",
         "1,0 điểm"),
        ("Câu 19\n(2,0 đ)",
         "- Tính chất trẻ lại và phân bậc: Vận động Tân kiến tạo (kỉ Neogen và Đệ tứ) đã nâng cao và trẻ lại địa hình cổ, tạo nên các bậc thềm địa hình kế tiếp nhau từ núi cao -> đồi núi thấp -> bán bình nguyên -> đồng bằng -> thềm lục địa. (1,0đ)\n"
         "- Thuận lợi & khó khăn của đồi núi: Thuận lợi: tiềm năng khoáng sản, thủy điện, rừng, cây công nghiệp lâu năm, du lịch sinh thái. Khó khăn: địa hình hiểm trở cản trở giao thông, dễ xảy ra sạt lở, xói mòn lũ quét trong mùa mưa. (1,0đ)",
         "2,0 điểm"),
        ("Câu 20\n(1,0 đ)",
         "- Lí do: Khoáng sản là tài nguyên không thể tái tạo, phải mất hàng triệu năm mới hình thành; nguy cơ cạn kiệt đe dọa sự phát triển bền vững và ô nhiễm môi trường do khai thác bừa bãi. (0,5đ)\n"
         "- 3 giải pháp: Hoàn thiện luật và thanh tra giấy phép khai thác; ứng dụng công nghệ hiện đại khai thác triệt để tránh thất thoát; nghiên cứu vật liệu và năng lượng tái tạo thay thế (gió, mặt trời). (0,5đ)",
         "1,0 điểm")
    ]
    
    add_answers_section(doc, mcq_answers, essay_rubric=rubric)
    
    file_path = os.path.join(OUTPUT_DIR, "De_03_Lop_8_Lich_Su_va_Dia_Li_Hoc_Ky_1.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

# ==============================================================================
# 4. ĐỀ KIỂM TRA LỚP 9 - ÔN THI TUYỂN SINH VÀO LỚP 10
# ==============================================================================
def generate_grade_9_exam():
    doc = create_styled_document()
    add_exam_header(
        doc,
        school_name="SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        exam_title="ĐỀ THI KHẢO SÁT CHẤT LƯỢNG ÔN THI VÀO LỚP 10 THPT",
        subject_title="LỊCH SỬ VÀ ĐỊA LÍ - KHỐI 9 (CHƯƠNG TRÌNH GDPT 2018)",
        duration_str="90 phút",
        exam_code="901"
    )
    
    # ------------------ PHẦN I: LỊCH SỬ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "A. PHÂN MÔN LỊCH SỬ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,5 điểm - 10 câu)")
    
    mcq_history = [
        ("Sự kiện lịch sử thế giới nào năm 1917 đã chặt đứt khâu yếu nhất của chủ nghĩa đế quốc và mở ra thời đại mới trong lịch sử nhân loại?",
         "Thắng lợi của Cách mạng tháng Mười Nga vĩ đại.",
         "Chiến tranh thế giới thứ nhất kết thúc.",
         "Nước Mỹ tham chiến phe Hiệp ước.",
         "Hội nghị Véc-xai nhóm họp."),
        ("Ngày 3/2/1930, tổ chức nào ra đời đã chấm dứt cuộc khủng hoảng sâu sắc về đường lối và giai cấp lãnh đạo cách mạng Việt Nam?",
         "Đảng Cộng sản Việt Nam thành lập dưới sự chủ trì của Nguyễn Ái Quốc.",
         "Hội Việt Nam Cách mạng Thanh niên.",
         "Việt Nam Quốc dân Đảng.",
         "Mặt trận Việt Minh."),
        ("Sự kiện mở đầu cho phong trào cách mạng 1930 - 1931 với đỉnh cao Xô viết Nghệ - Tĩnh là:",
         "Cuộc bãi công của công nhân Nhà máy Diêm Bến Thủy và nông dân Hưng Nguyên (Nghệ An) ngày 1/5/1930.",
         "Khởi nghĩa Yên Bái thất bại.",
         "Chiến dịch Biên giới Thu Đông.",
         "Hội nghị Ban Chấp hành Trung ương Đảng tháng 10/1930."),
        ("Đại hội đại biểu nào của Đảng hoặc Hội nghị nào đã quyết định chuyển hướng chỉ đạo chiến lược, đặt nhiệm vụ giải phóng dân tộc lên hàng đầu vào tháng 5/1941?",
         "Hội nghị lần thứ 8 Ban Chấp hành Trung ương Đảng do Hồ Chí Minh chủ trì tại Pác Bó.",
         "Hội nghị Trung ương 6 (tháng 11/1939).",
         "Đại hội đại biểu toàn quốc lần thứ I (tháng 3/1935).",
         "Hội nghị Quân sự Bắc Kì (tháng 4/1945)."),
        ("Ngày 2/9/1945, tại Quảng trường Ba Đình lịch sử, Chủ tịch Hồ Chí Minh đã đọc văn kiện bất hủ nào?",
         "Tuyên ngôn Độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa.",
         "Lời kêu gọi toàn quốc kháng chiến.",
         "Chỉ thị Toàn dân kháng chiến.",
         "Bản Yêu sách của nhân dân An Nam."),
        ("Chiến thắng quân sự nào của ta trong kháng chiến chống Pháp được đánh giá là 'Lừng lẫy năm châu, chấn động địa cầu' năm 1954?",
         "Chiến thắng Điện Biên Phủ.",
         "Chiến thắng Biên giới Thu - Đông 1950.",
         "Chiến dịch Việt Bắc Thu - Đông 1947.",
         "Chiến dịch Đường số 4."),
        ("Văn kiện quốc tế nào đã buộc chính phủ Pháp phải công nhận độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của ba nước Đông Dương năm 1954?",
         "Hiệp định Giơ-ne-vơ về Đông Dương.",
         "Hiệp định Pa-ri về Việt Nam.",
         "Tạm ước ngày 14/9/1946.",
         "Hiệp định Sơ bộ ngày 6/3/1946."),
        ("Phong trào 'Đồng khởi' (1959 - 1960) nổ ra tiêu biểu nhất tại địa phương nào ở miền Nam?",
         "Huyện Mỏ Cày (tỉnh Bến Tre).",
         "Tỉnh Quảng Trị.",
         "Tây Ninh.",
         "Bình Dương."),
        ("Chiến thắng 'Hà Nội - Điện Biên Phủ trên không' cuối tháng 12 năm 1972 đã đánh bại hoàn toàn cuộc tập kích chiến lược bằng máy bay nào của Mỹ?",
         "Máy bay ném bom chiến lược B-52.",
         "Máy bay tàng hình F-117.",
         "Máy bay trực thăng vận Huey.",
         "Chiến đấu cơ F-4 Phantom."),
        ("Cuộc Tổng tiến công và nổi dậy mùa Xuân năm 1975 kết thúc thắng lợi rực rỡ bằng chiến dịch lịch sử nào?",
         "Chiến dịch Hồ Chí Minh giải phóng Sài Gòn.",
         "Chiến dịch Tây Nguyên.",
         "Chiến dịch Huế - Đà Nẵng.",
         "Chiến dịch Đường 9 - Khe Sanh.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_history, start=1):
        add_mcq_question(doc, i, q, a, b, c, d)
        
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("Phần 2: Tự luận Lịch sử (2,5 điểm)")
    r_sub.font.bold = True
    
    add_essay_question(doc, 11, "2,5 điểm", 
                       "Phân tích ý nghĩa lịch sử và bài học kinh nghiệm sâu sắc của thắng lợi Cách mạng Tháng Tám năm 1945 đối với phong trào giải phóng dân tộc trên thế giới và sự nghiệp bảo vệ chủ quyền Tổ quốc ngày nay.")

    # ------------------ PHẦN II: ĐỊA LÍ (5,0 ĐIỂM) ------------------
    add_section_header(doc, "B. PHÂN MÔN ĐỊA LÍ (5,0 ĐIỂM)", "Phần 1: Trắc nghiệm khách quan (2,5 điểm - 10 câu)")
    
    mcq_geo = [
        ("Nước ta có bao nhiêu dân tộc anh em cùng chung sống, trong đó dân tộc nào chiếm tỉ lệ dân số cao nhất?",
         "54 dân tộc, dân tộc Kinh (Việt) chiếm đa số (>85%).",
         "53 dân tộc, dân tộc Tày chiếm đa số.",
         "50 dân tộc, dân tộc Thái chiếm đa số.",
         "56 dân tộc, dân tộc Mường chiếm đa số."),
        ("Hiện tượng 'cơ cấu dân số vàng' của Việt Nam mang lại cơ hội to lớn nhất nào sau đây?",
         "Nguồn lao động dồi dào, tỉ lệ người trong độ tuổi lao động cao gấp đôi người phụ thuộc.",
         "Tỉ lệ người già tăng nhanh cần nhiều viện dưỡng lão.",
         "Áp lực nhà ở và việc làm giảm đi tự động.",
         "Tăng chi phí phúc lợi xã hội cho người già."),
        ("Cây công nghiệp lâu năm chủ lực của vùng Tây Nguyên là cây nào sau đây?",
         "Cà phê, cao su, hồ tiêu.", "Chè, hồi, quế.", "Mía, thuốc lá, bông.", "Đay, cói, đậu tương."),
        ("Hai vùng đồng bằng châu thổ lớn nhất nước ta chuyên canh sản xuất lúa gạo xuất khẩu là:",
         "Đồng bằng sông Cửu Long và Đồng bằng sông Hồng.",
         "Đồng bằng duyên hải miền Trung và Đồng bằng Thanh Hóa.",
         "Đồng bằng sông Mã và sông Chu.",
         "Đồng bằng Nam Bộ và Thung lũng sông Cả."),
        ("Vùng kinh tế dẫn đầu cả nước về giá trị sản xuất công nghiệp, thu hút vốn đầu tư nước ngoài (FDI) và đô thị hóa năng động là:",
         "Vùng Đông Nam Bộ.",
         "Vùng Tây Nguyên.",
         "Vùng Trung du và miền núi Bắc Bộ.",
         "Vùng Bắc Trung Bộ."),
        ("Thế mạnh hàng đầu của vùng Trung du và miền núi Bắc Bộ về công nghiệp là:",
         "Khai thác khoáng sản và phát triển thủy điện (thủy điện Hòa Bình, Sơn La, Lai Châu).",
         "Công nghiệp chế biến dầu khí và hóa chất.",
         "Công nghiệp dệt may xuất khẩu.",
         "Công nghiệp lắp ráp điện tử viễn thông."),
        ("Huyện đảo Hoàng Sa và huyện đảo Trường Sa lần lượt thuộc quyền quản lí hành chính của tỉnh/thành phố nào?",
         "Thành phố Đà Nẵng và tỉnh Khánh Hòa.",
         "Tỉnh Quảng Ngãi và tỉnh Bình Định.",
         "Tỉnh Khánh Hòa và tỉnh Bà Rịa - Vũng Tàu.",
         "Thành phố Hải Phòng và tỉnh Quảng Ninh."),
        ("Tuyến đường bộ huyết mạch xuyên suốt từ Bắc vào Nam của nước ta là:",
         "Quốc lộ 1A và đường Hồ Chí Minh.",
         "Quốc lộ 5 và Quốc lộ 18.",
         "Tuyến cao tốc Nội Bài - Lào Cai.",
         "Quốc lộ 14 (đường Trường Sơn Tây)."),
        ("Tài nguyên du lịch tự nhiên nổi tiếng của vịnh Hạ Long (Quảng Ninh) thuộc dạng địa hình nào?",
         "Địa hình các-xtơ (Karst) đá vôi ngập nước độc đáo.",
         "Địa hình bờ biển cát bồi tụ.",
         "Địa hình núi lửa bazan cổ.",
         "Địa hình đồng bằng phù sa mới."),
        ("Nguyên nhân chủ yếu làm cho ngành thủy sản nước ta phát triển mạnh mẽ trong những năm gần đây là:",
         "Thị trường tiêu thụ mở rộng, đội tàu đánh bắt hiện đại và mở rộng diện tích nuôi trồng.",
         "Lao động nông nghiệp chuyển hết sang đánh bắt cá.",
         "Không còn chịu ảnh hưởng của bão gió.",
         "Nguồn lợi cá ven bờ tăng lên đột biến.")
    ]
    for i, (q, a, b, c, d) in enumerate(mcq_geo, start=21):
        add_mcq_question(doc, i, q, a, b, c, d)

    p_sub_g = doc.add_paragraph()
    r_sub_g = p_sub_g.add_run("Phần 2: Tự luận Địa lí (2,5 điểm)")
    r_sub_g.font.bold = True
    
    add_essay_question(doc, 31, "2,5 điểm", 
                       "Cho bảng số liệu: Quy mô diện tích và sản lượng lúa của nước ta giai đoạn 2015 - 2023. Hãy nhận xét sự thay đổi về năng suất lúa (tạ/ha) của nước ta và phân tích các nhân tố tự nhiên, kinh tế - xã hội tác động trực tiếp đến sự phát triển của nền nông nghiệp hàng hóa hiện nay.")

    add_exam_footer_mark(doc)

    # ------------------ ĐÁP ÁN & HƯỚNG DẪN CHẤM ------------------
    mcq_answers = [
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", # 1-10 Lịch sử
        "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"  # 21-30 Địa lí
    ]
    
    rubric = [
        ("Câu 11\n(2,5 đ)",
         "- Ý nghĩa đối với dân tộc: Phá tan xiềng xích nô lệ của thực dân Pháp gần 1 thế kỉ và ách thống trị của phát xít Nhật, lật nhào ngai vàng phong kiến hàng nghìn năm; lập nên nước Việt Nam Dân chủ Cộng hòa, mở ra kỉ nguyên độc lập tự do gắn liền với chủ nghĩa xã hội. (1,25đ)\n"
         "- Ý nghĩa quốc tế & bài học kinh nghiệm: Cổ vũ mạnh mẽ phong trào giải phóng dân tộc của các nước thuộc địa ở châu Á, châu Phi; để lại bài học nắm bắt thời cơ 'ngàn năm có một', phát huy sức mạnh khối đại đoàn kết toàn dân và xây dựng thế trận lòng dân vững chắc. (1,25đ)",
         "2,5 điểm"),
        ("Câu 31\n(2,5 đ)",
         "- Nhận xét năng suất lúa: Năng suất lúa nước ta liên tục tăng qua các năm nhờ thâm canh, áp dụng tiến bộ khoa học kĩ thuật và cơ giới hóa nông nghiệp (chứng minh bằng công thức Năng suất = Sản lượng / Diện tích). (1,0đ)\n"
         "- Phân tích nhân tố tự nhiên: Đất phù sa màu mỡ (ĐBSCL, ĐBSH), khí hậu nhiệt đới ẩm gió mùa nguồn nhiệt ẩm dồi dào, mạng lưới sông ngòi dày đặc cung cấp nước tưới tiêu. (0,75đ)\n"
         "- Phân tích nhân tố kinh tế - xã hội: Thị trường tiêu thụ trong nước và quốc tế rộng lớn; chính sách khuyến nông và hỗ trợ vốn của Nhà nước; cơ sở vật chất kĩ thuật thủy lợi và giống lúa chất lượng cao ngày càng hoàn thiện. (0,75đ)",
         "2,5 điểm")
    ]
    
    add_answers_section(doc, mcq_answers, essay_rubric=rubric)
    
    file_path = os.path.join(OUTPUT_DIR, "De_04_Lop_9_Lich_Su_va_Dia_Li_Tuyen_Sinh_10.docx")
    doc.save(file_path)
    print(f"[SUCCESS] Generated: {file_path}")

if __name__ == "__main__":
    generate_grade_6_exam()
    generate_grade_7_exam()
    generate_grade_8_exam()
    generate_grade_9_exam()
    print("All THCS exams generated successfully.")
