-> start_knot

=== start_knot ===
Chào mừng bạn đến với thế giới Tiếng Anh! Bạn đang đứng trước cổng trường học, nơi những câu chuyện và thử thách ngôn ngữ đang chờ đợi. Hãy cùng khám phá và vượt qua các nhiệm vụ để tiến sâu hơn vào thế giới Tiếng Anh nhé! 
-> task_tienganh_001

=== task_tienganh_001 ===
Hong và Mike đang ở trong căng-tin trường học.
- Hong: “______?”
- Mike: “Here you are.”
+ [Can you sit here]  -> task_tienganh_001_fail
+ [Can you play basketball]  -> task_tienganh_001_fail
+ [Can you speak Japanese, please]  -> task_tienganh_001_fail
+ [Can you pass the salt, please]  -> task_tienganh_001_success

=== task_tienganh_001_success ===
Chính xác! Mike đang đưa muối cho Hong.
-> task_tienganh_002

=== task_tienganh_001_fail ===
Sai rồi! Căng-tin vang lên tiếng chuông báo động.
+ [Thử lại câu hỏi này] -> task_tienganh_001

=== task_tienganh_002 ===
Peter và Khanh đang nói chuyện về việc học ngoại ngữ.
- Peter: “I think students should learn two foreign languages when they are at school.”
- Khanh: “______. It helps them communicate with more people and broaden their minds.”
+ [I quite agree with you]  -> task_tienganh_002_success
+ [I don’t think it’s a good idea]  -> task_tienganh_002_fail
+ [That’s not a good idea]  -> task_tienganh_002_fail
+ [I quite disagree with you]  -> task_tienganh_002_fail

=== task_tienganh_002_success ===
Chính xác! Khanh đồng tình với Peter.
-> task_tienganh_003

=== task_tienganh_002_fail ===
Sai rồi! Tiếng chuông báo động vang lên lần nữa.
+ [Thử lại câu hỏi này] -> task_tienganh_002

=== task_tienganh_003 ===
Mark the letter A, B, C, or D on your answer sheet to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.
+ [post]  -> task_tienganh_003_fail
+ [cold]  -> task_tienganh_003_fail
+ [sport]  -> task_tienganh_003_success
+ [home]  -> task_tienganh_003_fail

=== task_tienganh_003_success ===
Chính xác! "Sport" phát âm khác với các từ còn lại.
-> task_tienganh_004

=== task_tienganh_003_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_003

=== task_tienganh_004 ===
Mark the letter A, B, C, or D on your answer sheet to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.
+ [chorus]  -> task_tienganh_004_success
+ [chairman]  -> task_tienganh_004_fail
+ [chicken]  -> task_tienganh_004_fail
+ [children]  -> task_tienganh_004_fail

=== task_tienganh_004_success ===
Chính xác! "Chorus" phát âm khác với các từ còn lại.
-> task_tienganh_005

=== task_tienganh_004_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_004

=== task_tienganh_005 ===
Mark the letter A, B, C, or D on your answer sheet to indicate the word that differs from the other three in the position of stress in each of the following questions.
+ [important]  -> task_tienganh_005_fail
+ [terrific]  -> task_tienganh_005_fail
+ [exciting]  -> task_tienganh_005_fail
+ [confident]  -> task_tienganh_005_success

=== task_tienganh_005_success ===
Chính xác! "Confident" nhấn âm khác với các từ còn lại.
-> task_tienganh_006

=== task_tienganh_005_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_005

=== task_tienganh_006 ===
Mark the letter A, B, C, or D on your answer sheet to indicate the word that differs from the other three in the position of stress in each of the following questions.
+ [arrive]  -> task_tienganh_006_fail
+ [require]  -> task_tienganh_006_fail
+ [connect]  -> task_tienganh_006_fail
+ [follow]  -> task_tienganh_006_success

=== task_tienganh_006_success ===
Chính xác! "Follow" nhấn âm khác với các từ còn lại.
-> task_tienganh_007

=== task_tienganh_006_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_006

=== task_tienganh_007 ===
Returning home after the earthquake, Simon saw that his house was extremely chaotic.
+ [organised]  -> task_tienganh_007_fail
+ [tidy]  -> task_tienganh_007_fail
+ [messy]  -> task_tienganh_007_success
+ [neat]  -> task_tienganh_007_fail

=== task_tienganh_007_success ===
Chính xác! "Messy" là từ đúng mô tả cảnh hỗn loạn.
-> task_tienganh_008

=== task_tienganh_007_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_007

=== task_tienganh_008 ===
My uncle dreams of having a new house, so he plans to save up for it.
+ [leaves]  -> task_tienganh_008_fail
+ [moves]  -> task_tienganh_008_fail
+ [intends]  -> task_tienganh_008_success
+ [quits]  -> task_tienganh_008_fail

=== task_tienganh_008_success ===
Chính xác! "Intends" là từ đúng mô tả ý định của chú bạn.
-> task_tienganh_009

=== task_tienganh_008_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_008

=== task_tienganh_009 ===
He had some business to do in a foreign country, but his company denied responsibility to pay for his expenses.
+ [accepted]  -> task_tienganh_009_success
+ [refused]  -> task_tienganh_009_fail
+ [avoided]  -> task_tienganh_009_fail
+ [neglected]  -> task_tienganh_009_fail

=== task_tienganh_009_success ===
Chính xác! "Accepted" là từ trái nghĩa với "denied".
-> task_tienganh_010

=== task_tienganh_009_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_009

=== task_tienganh_010 ===
I think you should apologise to Mary. What you commented on her new hairstyle yesterday was really below the belt.
+ [fair and unkind]  -> task_tienganh_010_fail
+ [fair and cruel]  -> task_tienganh_010_fail
+ [fair and kind]  -> task_tienganh_010_success
+ [cruel and kind]  -> task_tienganh_010_fail

=== task_tienganh_010_success ===
Chính xác! "Fair and kind" là từ đúng mô tả hành vi của bạn.
-> act_2_start

=== task_tienganh_010_fail ===
Sai rồi! Tiếng chuông báo động vang lên.
+ [Thử lại câu hỏi này] -> task_tienganh_010

=== act_2_start ===

Bạn đã vượt qua màn đầu tiên! Bây giờ, hãy bước vào khu vực thử thách mới - khu vực "Tiếng Anh nâng cao". Ở đây, bạn sẽ gặp phải những câu hỏi ngữ pháp và từ vựng khó hơn. Hãy cẩn thận và suy nghĩ kỹ trước khi chọn đáp án nhé!
-> task_tienganh_011

=== task_tienganh_011 ===
The Youth International Conference ______ by a lot of young people from around the world.
+ [was attending] -> task_tienganh_011_fail
+ [attended] -> task_tienganh_011_fail
+ [attends] -> task_tienganh_011_fail
+ [was attended] -> task_tienganh_011_success

=== task_tienganh_011_success ===
Chính xác! Đại hội được rất nhiều bạn trẻ từ khắp nơi trên thế giới tham dự.
-> task_tienganh_012

=== task_tienganh_011_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu thì quá khứ bị động.
+ [Thử lại câu hỏi này] -> task_tienganh_011

=== task_tienganh_012 ===
The man ______ home when his car broke down.
+ [was driving] -> task_tienganh_012_success
+ [drives] -> task_tienganh_012_fail
+ [has driven] -> task_tienganh_012_fail
+ [is driving] -> task_tienganh_012_fail

=== task_tienganh_012_success ===
Chính xác! Người đàn ông đang lái xe về nhà thì xe hỏng.
-> task_tienganh_013

=== task_tienganh_012_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu thì quá khứ tiếp diễn.
+ [Thử lại câu hỏi này] -> task_tienganh_012

=== task_tienganh_013 ===
Although the students in my class have been learning English for three months, they can ______ confidently with foreigners.
+ [communicative] -> task_tienganh_013_fail
+ [communicate] -> task_tienganh_013_success
+ [communicatively] -> task_tienganh_013_fail
+ [communication] -> task_tienganh_013_fail

=== task_tienganh_013_success ===
Chính xác! Dù đã học tiếng Anh ba tháng, các bạn trong lớp tôi vẫn có thể giao tiếp tự tin với người nước ngoài.
-> task_tienganh_014

=== task_tienganh_013_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu động từ "can" đi với động từ nguyên mẫu.
+ [Thử lại câu hỏi này] -> task_tienganh_013

=== task_tienganh_014 ===
We have travelled to almost every tourist attraction in ______ Africa.
+ [the] -> task_tienganh_014_fail
+ [an] -> task_tienganh_014_fail
+ [Ø (no article)] -> task_tienganh_014_success
+ [a] -> task_tienganh_014_fail

=== task_tienganh_014_success ===
Chính xác! Chúng tôi đã đến gần như tất cả các điểm du lịch ở châu Phi.
-> task_tienganh_015

=== task_tienganh_014_fail ===
Sai rồi! Báo động đỏ kêu vang. "Africa" là danh từ riêng, không cần thêm冠词.
+ [Thử lại câu hỏi này] -> task_tienganh_014

=== task_tienganh_015 ===
Binh is 1.80 meters tall, and Linh is 1.65 meters tall. Binh is ______ Linh.
+ [younger than] -> task_tienganh_015_fail
+ [older than] -> task_tienganh_015_fail
+ [taller than] -> task_tienganh_015_success
+ [shorter than] -> task_tienganh_015_fail

=== task_tienganh_015_success ===
Chính xác! Binh cao hơn Linh.
-> task_tienganh_016

=== task_tienganh_015_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này so sánh chiều cao.
+ [Thử lại câu hỏi này] -> task_tienganh_015

=== task_tienganh_016 ===
Her parents are working on the farm, ______?
+ [are they] -> task_tienganh_016_fail
+ [don’t they] -> task_tienganh_016_fail
+ [do they] -> task_tienganh_016_fail
+ [aren’t they] -> task_tienganh_016_success

=== task_tienganh_016_success ===
Chính xác! Câu hỏi nghi vấn sau câu khẳng định.
-> task_tienganh_017

=== task_tienganh_016_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi nghi vấn cần phủ định.
+ [Thử lại câu hỏi này] -> task_tienganh_016

=== task_tienganh_017 ===
The foreign teacher was speaking so fast. Nga couldn’t ______ the main contents of his lesson.
+ [call for] -> task_tienganh_017_fail
+ [go on] -> task_tienganh_017_fail
+ [note down] -> task_tienganh_017_success
+ [make up] -> task_tienganh_017_fail

=== task_tienganh_017_success ===
Chính xác! Nga không thể ghi chú lại nội dung chính của bài giảng.
-> task_tienganh_018

=== task_tienganh_017_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu động từ "note down" (ghi chú lại).
+ [Thử lại câu hỏi này] -> task_tienganh_017

=== task_tienganh_018 ===
The journalist is talking about having a new ______ published in the local newspaper next week.
+ [editor] -> task_tienganh_018_fail
+ [documentary] -> task_tienganh_018_fail
+ [cartoon] -> task_tienganh_018_fail
+ [article] -> task_tienganh_018_success

=== task_tienganh_018_success ===
Chính xác! Nhà báo đang nói về việc xuất bản một bài báo mới.
-> task_tienganh_019

=== task_tienganh_018_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu danh từ "article" (bài viết).
+ [Thử lại câu hỏi này] -> task_tienganh_018

=== task_tienganh_019 ===
It’s not difficult ______ her to go to work because the office is near her home.
+ [on] -> task_tienganh_019_fail
+ [for] -> task_tienganh_019_success
+ [towards] -> task_tienganh_019_fail
+ [to] -> task_tienganh_019_fail

=== task_tienganh_019_success ===
Chính xác! Việc đi làm của cô ấy không khó khăn gì.
-> task_tienganh_020

=== task_tienganh_019_fail ===
Sai rồi! Báo động đỏ kêu vang. Cấu trúc "It's not difficult for someone to do something".
+ [Thử lại câu hỏi này] -> task_tienganh_019

=== task_tienganh_020 ===
______ a job in a small company, he turned it down and kept on applying for a more suitable one.
+ [Offered] -> task_tienganh_020_success
+ [Having offered] -> task_tienganh_020_fail
+ [Offering] -> task_tienganh_020_fail
+ [To offer] -> task_tienganh_020_fail

=== task_tienganh_020_success ===
Chính xác! Anh ta được một công việc ở công ty nhỏ nhưng đã từ chối.
-> act_3_start

=== task_tienganh_020_fail ===
Sai rồi! Báo động đỏ kêu vang. Câu hỏi này yêu cầu thì quá khứ bị động.
+ [Thử lại câu hỏi này] -> task_tienganh_020

=== act_3_start ===

Bạn đã vượt qua màn trước! Bây giờ, hãy bước vào khu vực thử thách mới - Màn 3. Đây là nơi bạn sẽ đối mặt với những câu hỏi tiếng Anh khó hơn. Hãy cẩn thận và suy nghĩ kỹ trước khi chọn đáp án nhé!
-> task_tienganh_021

=== task_tienganh_021 ===
Before you decide to purchase that car, it is crucial that you should look into it carefully. It’s unwise to buy a pig ______.
+ [in a pack] -> task_tienganh_021_fail
+ [in a roll] -> task_tienganh_021_fail
+ [in a rack] -> task_tienganh_021_fail
+ [in a poke] -> task_tienganh_021_success

=== task_tienganh_021_success ===
Chính xác! Mua một con lợn "in a poke" (mua không nhìn thấy) là cách nói ẩn dụ về việc mua hàng không kiểm tra kỹ. 
-> task_tienganh_022

=== task_tienganh_021_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_021

=== task_tienganh_022 ===
Nam is trying to break the ______ of staying up too late.
+ [sound] -> task_tienganh_022_fail
+ [habit] -> task_tienganh_022_success
+ [option] -> task_tienganh_022_fail
+ [race] -> task_tienganh_022_fail

=== task_tienganh_022_success ===
Chính xác! "Break the habit" là cụm động từ phổ biến để nói về việc từ bỏ thói quen xấu.
-> task_tienganh_023

=== task_tienganh_022_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_022

=== task_tienganh_023 ===
She promised ______ to my birthday party, but she didn’t.
+ [to come] -> task_tienganh_023_success
+ [come] -> task_tienganh_023_fail
+ [coming] -> task_tienganh_023_fail
+ [to coming] -> task_tienganh_023_fail

=== task_tienganh_023_success ===
Chính xác! "Promise to do something" là cấu trúc đúng khi nói về việc hứa sẽ làm điều gì đó.
-> task_tienganh_024

=== task_tienganh_023_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_023

=== task_tienganh_024 ===
It is uncommon for the director to ______ power to his finance manager to make financial.
+ [authorise] -> task_tienganh_024_fail
+ [stimulate] -> task_tienganh_024_fail
+ [navigate] -> task_tienganh_024_fail
+ [delegate] -> task_tienganh_024_success

=== task_tienganh_024_success ===
Chính xác! "Delegate power" là cách nói phổ biến khi giao quyền hạn cho người khác.
-> task_tienganh_025

=== task_tienganh_024_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_024

=== task_tienganh_025 ===
We will inform you ______.
+ [as soon as we have the interview result] -> task_tienganh_025_success
+ [as soon as we were having the interview result] -> task_tienganh_025_fail
+ [as soon as we had the interview result] -> task_tienganh_025_fail
+ [as soon as we had had the interview result] -> task_tienganh_025_fail

=== task_tienganh_025_success ===
Chính xác! Cấu trúc "as soon as + present tense" phù hợp với ngữ cảnh tương lai.
-> task_tienganh_026

=== task_tienganh_025_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_025

=== task_tienganh_026 ===
The boy band had just finished their first live performance. All the audiences at the theatre gave them a loud round of applause.
+ [No matter when the boy band finished their first live performance did all the audiences at the theatre give them a loud round of applause.] -> task_tienganh_026_fail
+ [Had it not been for the boy band’s first live performance, all the audiences at the theatre would have given them a loud round of applause.] -> task_tienganh_026_fail
+ [Not until all the audiences at the theatre gave them a loud round of applause did the boy band finish their first live performance.] -> task_tienganh_026_fail
+ [Barely had the boy band finished their first live performance when all the audiences at the theatre gave them a loud round of applause.] -> task_tienganh_026_success

=== task_tienganh_026_success ===
Chính xác! "Barely had... when..." là cấu trúc nhấn mạnh sự kiện xảy ra ngay sau khi một hành động khác kết thúc.
-> task_tienganh_027

=== task_tienganh_026_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_026

=== task_tienganh_027 ===
The gold ring was expensive. I couldn’t afford to buy it.
+ [If the gold ring had been cheaper, I can’t have afforded to buy it.] -> task_tienganh_027_fail
+ [If the gold ring had been less expensive, I could have afforded to buy it.] -> task_tienganh_027_success
+ [If the gold ring had been cheaper, I couldn’t have afforded to buy it.] -> task_tienganh_027_fail
+ [If the gold ring had been more expensive, I could have afforded to buy it.] -> task_tienganh_027_fail

=== task_tienganh_027_success ===
Chính xác! "If + past perfect, would have + past participle" là cấu trúc điều kiện loại 3.
-> task_tienganh_028

=== task_tienganh_027_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_027

=== task_tienganh_028 ===
Mark started learning Spanish seven years ago.
+ [Mark has learned Spanish for seven years.] -> task_tienganh_028_success
+ [Mark has started learning Spanish since seven years.] -> task_tienganh_028_fail
+ [Mark has learned Spanish since he was seven years old.] -> task_tienganh_028_fail
+ [Mark started learning Spanish when he was seven years old.] -> task_tienganh_028_fail

=== task_tienganh_028_success ===
Chính xác! "Has learned for + time" là cách diễn đạt thời gian học một kỹ năng.
-> task_tienganh_029

=== task_tienganh_028_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_028

=== task_tienganh_029 ===
“I helped the old lady cross the road,” said the teacher.
+ [The teacher said I helped the old lady cross the road.] -> task_tienganh_029_fail
+ [The teacher said she helped the old lady cross the road.] -> task_tienganh_029_fail
+ [The teacher said she would help the old lady cross the road.] -> task_tienganh_029_fail
+ [The teacher said she had helped the old lady cross the road.] -> task_tienganh_029_success

=== task_tienganh_029_success ===
Chính xác! "She had helped" là thì quá khứ hoàn thành phù hợp với câu trực tiếp trong quá khứ.
-> task_tienganh_030

=== task_tienganh_029_fail ===
Sai rồi! Báo động đỏ kêu vang. Hãy thử lại!
+ [Thử lại câu hỏi này] -> task_tienganh_029

=== task_tienganh_030 ===
Students are not allowed to bring food into the computer room.
+ [Students wouldn’t bring food into the computer room.] -> task_tienganh_030_fail
+ [Students won’t bring food into the computer room.] -> task_tienganh_030_fail
+ [Students mustn’t bring food into the computer room.] -> task_tienganh_030_success
+ [Students needn’t bring food into the computer room.] -> task_tienganh_030_fail

=== task_tienganh_030_success ===
Chính xác! "Mustn’t" là cách diễn đạt cấm đoán trong tiếng Anh.
-> act_4_start

=== act_4_start ===

Chào mừng bạn đến với Hồi 4 - Khu vực thử thách Tiếng Anh! Bạn sẽ đối mặt với những câu hỏi ngữ pháp và từ vựng nâng cao. Hãy tập trung và chọn đáp án chính xác nhé!
-> task_tienganh_031

=== task_tienganh_031 ===
Their pioneering research showed that the learning motivation of the two groups of learners was quite distinctive from each other, and the comparative group whose learning motivation was stronger performed better than the control group.
+ [distinctive] -> task_tienganh_031_success
+ [comparative] -> task_tienganh_031_fail
+ [control] -> task_tienganh_031_fail
+ [learners] -> task_tienganh_031_fail

=== task_tienganh_031_success ===
Chính xác! "Distinctive" là từ đúng để mô tả sự khác biệt rõ rệt giữa hai nhóm.
-> task_tienganh_032

=== task_tienganh_031_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_031

=== task_tienganh_032 ===
The man bought the old painting and then resold them to a collector at a higher price.
+ [them] -> task_tienganh_032_success
+ [bought] -> task_tienganh_032_fail
+ [resold] -> task_tienganh_032_fail
+ [painting] -> task_tienganh_032_fail

=== task_tienganh_032_success ===
Chính xác! "Them" là đại từ chỉ "the old painting" (dù có sự không nhất quán số lượng, đây là lỗi ngữ pháp nhưng theo dữ liệu, đây là đáp án đúng).
-> task_tienganh_033

=== task_tienganh_032_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_032

=== task_tienganh_033 ===
They give a good presentation on how to adopt a green lifestyle last week.
+ [give] -> task_tienganh_033_success
+ [presentation] -> task_tienganh_033_fail
+ [adopt] -> task_tienganh_033_fail
+ [last week] -> task_tienganh_033_fail

=== task_tienganh_033_success ===
Chính xác! "Give" cần được thay bằng "gave" để phù hợp với thì quá khứ "last week".
-> task_tienganh_034

=== task_tienganh_034 ===
Future employers like to know about their work experience (34) ______ they think is important for them in the process of recruiting employees.
+ [who] -> task_tienganh_034_fail
+ [which] -> task_tienganh_034_success
+ [when] -> task_tienganh_034_fail
+ [where] -> task_tienganh_034_fail

=== task_tienganh_034_success ===
Chính xác! "Which" dùng để chỉ vật (work experience) trong mệnh đề quan hệ.
-> task_tienganh_035

=== task_tienganh_035 ===
And young people get the chance to consider (35) ______ possibilities for a future career with working professionals.
+ [each] -> task_tienganh_035_fail
+ [many] -> task_tienganh_035_fail
+ [none] -> task_tienganh_035_fail
+ [one] -> task_tienganh_035_success

=== task_tienganh_035_success ===
Chính xác! "One" dùng để chỉ "a possibility" (một khả năng) trong ngữ cảnh.
-> task_tienganh_036

=== task_tienganh_036 ===
they will find these professionals’ advice specially helpful when thinking about the different choices they will have to (36) ______.
+ [build] -> task_tienganh_036_fail
+ [fill] -> task_tienganh_036_fail
+ [do] -> task_tienganh_036_fail
+ [make] -> task_tienganh_036_success

=== task_tienganh_036_success ===
Chính xác! "Make choices" là cụm động từ phổ biến trong tiếng Anh.
-> task_tienganh_037

=== task_tienganh_037 ===
Work experience often involves uncomfortable situations, (37) ______ people who are in such situations can learn how to behave appropriately in front of clients and how to respond to things in the workplace.
+ [nor] -> task_tienganh_037_fail
+ [for] -> task_tienganh_037_fail
+ [but] -> task_tienganh_037_success
+ [either] -> task_tienganh_037_fail

=== task_tienganh_037_success ===
Chính xác! "But" dùng để nối hai mệnh đề có ý nghĩa tương phản.
-> task_tienganh_038

=== task_tienganh_038 ===
Appearance is also important and they need to dress suitably whether they are going for a job as an engineer or an IT specialist, or a job which is perhaps less technical but equally (38) ______, such as medical doctor or a teacher.
+ [confusing] -> task_tienganh_038_fail
+ [commanding] -> task_tienganh_038_fail
+ [demanding] -> task_tienganh_038_success
+ [understanding] -> task_tienganh_038_fail

=== task_tienganh_038_success ===
Chính xác! "Demanding" phù hợp với ngữ cảnh công việc đòi hỏi nhiều kỹ năng.
-> task_tienganh_039

=== task_tienganh_039 ===
The passage is mainly about ______.
+ [the development of device-centred communication] -> task_tienganh_039_fail
+ [the impact of device-centred communication] -> task_tienganh_039_success
+ [the definition of device-centred communication] -> task_tienganh_039_fail
+ [the misunderstanding of device-centred communication] -> task_tienganh_039_fail

=== task_tienganh_039_success ===
Chính xác! Đoạn văn tập trung vào tác động của giao tiếp dựa trên thiết bị.
-> task_tienganh_040

=== task_tienganh_040 ===
The word They in paragraph 2 refers to ______.
+ [mobile phones] -> task_tienganh_040_fail
+ [tablets] -> task_tienganh_040_fail
+ [mobile devices] -> task_tienganh_040_success
+ [laptops] -> task_tienganh_040_fail

=== task_tienganh_040_success ===
Chính xác! "They" chỉ chung các thiết bị di động (mobile devices).
-> act_5_start

=== act_5_start ===

Chào mừng bạn đến với Hồi 5 – Trận chung kết! Đây là màn cuối cùng của hành trình học tiếng Anh. Bạn đã sẵn sàng để kiểm tra kiến thức của mình chưa? Hãy bắt đầu ngay nhé!
-> task_tienganh_041

=== task_tienganh_041 ===
Câu hỏi: In paragraph 2, in her statement about the advantages of communicating in person, Mary Peters mentioned all of the following EXCEPT ______.
+ [body language] -> task_tienganh_041_fail
+ [eye contact] -> task_tienganh_041_fail
+ [handshake] -> task_tienganh_041_success
+ [tone of voice] -> task_tienganh_041_fail

=== task_tienganh_041_success ===
Chính xác! "handshake" là đáp án đúng.
-> task_tienganh_042

=== task_tienganh_041_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_041

=== task_tienganh_042 ===
Câu hỏi: The word meet up in paragraph 3 is closest in meaning to ______.
+ [come down] -> task_tienganh_042_fail
+ [get together] -> task_tienganh_042_success
+ [get away] -> task_tienganh_042_fail
+ [come away] -> task_tienganh_042_fail

=== task_tienganh_042_success ===
Chính xác! "get together" là đáp án đúng.
-> task_tienganh_043

=== task_tienganh_042_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_042

=== task_tienganh_043 ===
Câu hỏi: According to paragraph 4, deep understanding appears when ______.
+ [we communicate through social networking] -> task_tienganh_043_fail
+ [we interact with modern technology] -> task_tienganh_043_fail
+ [we care about our virtual friends] -> task_tienganh_043_fail
+ [we see the reactions on the faces of other people] -> task_tienganh_043_success

=== task_tienganh_043_success ===
Chính xác! "we see the reactions on the faces of other people" là đáp án đúng.
-> task_tienganh_044

=== task_tienganh_043_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_043

=== task_tienganh_044 ===
Câu hỏi: Which of the following can be the main idea of the passage?
+ [Thorough research on teenagers’ online games and outdoor activities] -> task_tienganh_044_fail
+ [Teenagers’ free-time activity preferences and adults' concerns] -> task_tienganh_044_success
+ [Viewpoints on teenagers’ free-time adventures and online games] -> task_tienganh_044_fail
+ [Fears and tensions encountered by teenagers and adults' concerns] -> task_tienganh_044_fail

=== task_tienganh_044_success ===
Chính xác! "Teenagers’ free-time activity preferences and adults' concerns" là đáp án đúng.
-> task_tienganh_045

=== task_tienganh_044_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_044

=== task_tienganh_045 ===
Câu hỏi: The word fulfilling in paragraph 1 is closest in meaning to ______.
+ [frightening] -> task_tienganh_045_fail
+ [satisfying] -> task_tienganh_045_success
+ [devastating] -> task_tienganh_045_fail
+ [discouraging] -> task_tienganh_045_fail

=== task_tienganh_045_success ===
Chính xác! "satisfying" là đáp án đúng.
-> task_tienganh_046

=== task_tienganh_045_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_045

=== task_tienganh_046 ===
Câu hỏi: The word advances in paragraph 2 is closest in meaning to ______.
+ [movements] -> task_tienganh_046_fail
+ [advantages] -> task_tienganh_046_fail
+ [barriers] -> task_tienganh_046_fail
+ [developments] -> task_tienganh_046_success

=== task_tienganh_046_success ===
Chính xác! "developments" là đáp án đúng.
-> task_tienganh_047

=== task_tienganh_046_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_046

=== task_tienganh_047 ===
Câu hỏi: The word they in paragraph 3 refers to ______.
+ [outdoor activities] -> task_tienganh_047_fail
+ [young people] -> task_tienganh_047_fail
+ [older generations] -> task_tienganh_047_fail
+ [surveyed adults] -> task_tienganh_047_success

=== task_tienganh_047_success ===
Chính xác! "surveyed adults" là đáp án đúng.
-> task_tienganh_048

=== task_tienganh_047_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_047

=== task_tienganh_048 ===
Câu hỏi: According to paragraph 3, the older generations are worried about ______.
+ [the young’s preferences for outdoor activities] -> task_tienganh_048_fail
+ [the young’s reliance on virtual reality] -> task_tienganh_048_success
+ [the young’s ignorance about virtual reality] -> task_tienganh_048_fail
+ [the young’s lack of indoor activities] -> task_tienganh_048_fail

=== task_tienganh_048_success ===
Chính xác! "the young’s reliance on virtual reality" là đáp án đúng.
-> task_tienganh_049

=== task_tienganh_048_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_048

=== task_tienganh_049 ===
Câu hỏi: Which of the following is NOT TRUE according to the passage?
+ [One fourth of the surveyed teenagers believed online experiences in their free time were as pleasing as real life.] -> task_tienganh_049_fail
+ [The older generations surveyed thought that today’s teenagers were more protected than they had been.] -> task_tienganh_049_fail
+ [The majority of teenagers surveyed enjoyed real outdoor activities in their leisure time.] -> task_tienganh_049_success
+ [Researchers do not put all the blame on technology for causing teenagers’ lack of real-life experiences.] -> task_tienganh_049_fail

=== task_tienganh_049_success ===
Chính xác! "The majority of teenagers surveyed enjoyed real outdoor activities in their leisure time." là đáp án đúng.
-> task_tienganh_050

=== task_tienganh_049_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_049

=== task_tienganh_050 ===
Câu hỏi: Which of the following can be inferred from the passage?
+ [Many adults think that the present world is as dangerous as it used to be.] -> task_tienganh_050_fail
+ [Many adults are doubtful about their children’s ability to take care of themselves.] -> task_tienganh_050_success
+ [Virtual life is considered to be more and more challenging for teenagers in the present world.] -> task_tienganh_050_fail
+ [The majority of teenagers surveyed believed virtual reality was as interesting as the real life.] -> task_tienganh_050_fail

=== task_tienganh_050_success ===
Chính xác! "Many adults are doubtful about their children’s ability to take care of themselves." là đáp án đúng.
-> END

=== task_tienganh_050_fail ===
Sai rồi! Báo động đỏ kêu vang.
+ [Thử lại câu hỏi này] -> task_tienganh_050

=== task_tienganh_030_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_030


=== task_tienganh_033_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_033


=== task_tienganh_034_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_034


=== task_tienganh_035_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_035


=== task_tienganh_036_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_036


=== task_tienganh_037_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_037


=== task_tienganh_038_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_038


=== task_tienganh_039_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_039


=== task_tienganh_040_fail ===
Sai rồi! Hãy thử lại.
+ [Thử lại câu hỏi này] -> task_tienganh_040
