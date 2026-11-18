import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as scrolledtext
import subprocess
import threading
import os
import shutil
import sys
class SINEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SINE - AI Game Generator cho Giáo Viên & DIP Studio")
        self.root.geometry("740x580")
        tk.Label(root, text="HỆ THỐNG TẠO GAME GIÁO DỤC TỰ ĐỘNG (HỖ TRỢ DIP & ẢNH ĐỀ THI)", font=("Arial", 13, "bold")).pack(pady=10)
        frame_file = tk.Frame(root)
        frame_file.pack(fill="x", padx=20, pady=5)
        tk.Label(frame_file, text="1. Chọn Đề Thi (PDF/Word/Ảnh chụp):", font=("Arial", 10)).pack(side="left")
        self.lbl_file = tk.Label(frame_file, text="Chưa chọn file", fg="blue", font=("Arial", 10, "italic"))
        self.lbl_file.pack(side="left", padx=10)
        tk.Button(frame_file, text="🔍 DIP Studio (Xem xử lý ảnh)", bg="#3f51b5", fg="white", font=("Arial", 9, "bold"), command=self.open_dip_studio).pack(side="right", padx=5)
        tk.Button(frame_file, text="Duyệt...", command=self.browse_file).pack(side="right")
        self.selected_file = ""
        frame_topic = tk.Frame(root)
        frame_topic.pack(fill="x", padx=20, pady=5)
        tk.Label(frame_topic, text="2. Chủ đề / Tên bài học:", font=("Arial", 10)).pack(side="left")
        self.entry_topic = tk.Entry(frame_topic, width=30)
        self.entry_topic.insert(0, "tienganh")
        self.entry_topic.pack(side="left", padx=10)
        self.btn_gen = tk.Button(root, text="3. 🚀 TỰ ĐỘNG TẠO VÀ ĐÓNG GÓI GAME (1-CLICK)", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.start_generation)
        self.btn_gen.pack(pady=15)
        tk.Label(root, text="Trạng thái hệ thống:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20)
        self.log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, font=("Consolas", 9))
        self.log_area.pack(fill="both", expand=True, padx=20, pady=5)
    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
    def browse_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("Tất cả định dạng hỗ trợ", "*.pdf *.docx *.doc *.txt *.jpg *.jpeg *.png *.bmp *.webp"),
                ("Ảnh chụp đề thi (DIP Engine)", "*.jpg *.jpeg *.png *.bmp *.webp"),
                ("Tài liệu văn bản (PDF, Word)", "*.pdf *.docx *.doc *.txt"),
                ("Tất cả tập tin", "*.*")
            ]
        )
        if filename:
            self.selected_file = filename
            self.lbl_file.config(text=os.path.basename(filename))
    def open_dip_studio(self):
        cmd = [sys.executable, os.path.join("tools", "dip_viewer_gui.py")]
        if self.selected_file and any(self.selected_file.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]):
            cmd.extend(["--image", self.selected_file])
        subprocess.Popen(cmd)
    def start_generation(self):
        if not self.selected_file:
            messagebox.showwarning("Lỗi", "Vui lòng chọn file đề thi trước!")
            return
        topic = self.entry_topic.get().strip()
        if not topic:
            messagebox.showwarning("Lỗi", "Vui lòng nhập chủ đề!")
            return
        self.btn_gen.config(state="disabled", bg="gray")
        self.log_area.delete(1.0, tk.END)
        self.log("Bắt đầu quá trình tạo game tự động từ A-Z...")
        threading.Thread(target=self.run_pipeline, args=(self.selected_file, topic), daemon=True).start()
    def run_pipeline(self, filepath, topic):
        try:
            seed_filename = f"seed_{topic}_auto.json"
            seed_path = os.path.join("seeds", seed_filename)
            ink_filename = f"game_seed_{topic}_auto.ink"
            ink_path = os.path.join("output", ink_filename)

            # Xóa các file cũ của chủ đề này trước để tránh nhận nhầm file cũ nếu có lỗi
            if os.path.exists(seed_path):
                try: os.remove(seed_path)
                except Exception: pass
            if os.path.exists(ink_path):
                try: os.remove(ink_path)
                except Exception: pass

            self.log(f"\n[BƯỚC 1/3] AI Đang đọc đề thi và tách câu hỏi...")
            cmd_extract = [sys.executable, "extract_seed_from_doc.py", filepath, "--topic", topic]
            ret_extract = self.run_command(cmd_extract)
            if ret_extract != 0 or not os.path.exists(seed_path):
                self.log("❌ Lỗi: Bước 1 trích xuất câu hỏi thất bại. Đã dừng tiến trình!")
                self.btn_gen.config(state="normal", bg="green")
                return
            self.log(f" Đã trích xuất xong bộ câu hỏi: {seed_filename}")
            self.log(f"\n[BƯỚC 2/3] AI Đang sáng tác cốt truyện và lập trình game (Quá trình này có thể mất 1-2 phút)...")
            cmd_generate = [sys.executable, "run_single_test.py", "--seed", seed_filename]
            ret_generate = self.run_command(cmd_generate)
            if ret_generate != 0 or not os.path.exists(ink_path):
                self.log("❌ Lỗi: Không tìm thấy file game (.ink) được tạo ra.")
                self.btn_gen.config(state="normal", bg="green")
                return
            self.log(f"\n[BƯỚC 3/3] Đang đóng gói thành bản Game độc lập...")
            export_dir = os.path.join("Game_Export", f"Game_{topic}")
            os.makedirs(export_dir, exist_ok=True)

            # Sao chép file kịch bản ban đầu vào thư mục game
            story_ink_target = os.path.join(export_dir, "story.ink")
            shutil.copy2(ink_path, story_ink_target)

            # Tự động tạo thư mục images
            images_export_dir = os.path.join(export_dir, "images")
            os.makedirs(images_export_dir, exist_ok=True)

            # Tự động minh họa bối cảnh qua AI Story Illustrator
            try:
                from src.story_illustrator import illustrate_exported_game
                illustrate_exported_game(export_dir, topic=topic, progress_callback=self.log)
            except Exception as e_ill:
                self.log(f"⚠️ Cảnh báo tạo ảnh minh họa: {e_ill}. Tiến hành biên dịch kịch bản dự phòng.")
                subprocess.run([os.path.join("tools", "inklecate.exe"), "-o", os.path.join(export_dir, "story.json"), story_ink_target], capture_output=True)

            html_content = r"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>SINE Game</title>
    <!-- Ink Engine -->
    <script src="https://unpkg.com/inkjs/dist/ink.js"></script>
    
    <!-- KaTeX Math Renderer -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a1a1a; color: #f0f0f0; margin: 0; padding: 20px 0; display: flex; flex-direction: column; align-items: center; min-height: 100vh; }
        #game-container { max-width: 800px; width: 92%; background: #2a2a2a; border-radius: 12px; overflow: hidden; box-shadow: 0 6px 20px rgba(0,0,0,0.6); }
        #story { padding: 25px; min-height: 150px; font-size: 19px; line-height: 1.7; }
        .story-img { width: 100%; max-height: 380px; object-fit: cover; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); display: block; }
        .choice { display: block; margin: 12px 25px; padding: 15px 20px; background: #2b4c6f; color: #fff; text-decoration: none; border-radius: 8px; cursor: pointer; transition: all 0.2s ease; font-size: 17px; font-weight: 500; border: 1px solid rgba(255,255,255,0.1); }
        .choice:hover { background: #3b6c9f; transform: translateX(6px); border-color: rgba(255,255,255,0.3); }
        .katex { font-size: 1.12em; }
        .choice .katex { font-size: 1.05em; }
    </style>
</head>
<body>
    <div id="game-container">
        <div id="story"></div>
        <div id="choices"></div>
    </div>
    <script>
        function fixMathTokens(mathStr) {
            var s = mathStr;
            s = s.replace(/(^|[^\\])(frac|sqrt|infty|perp|parallel|approx|simeq|cong|equiv|leq|geq|neq|alpha|beta|gamma|delta|Delta|pi|theta|sigma|omega|Omega|iint|iiint|oint|prod|lim|dot|ddot|overline|underline|partial|nabla)(?=[^a-zA-Z]|$)/g, '$1\\$2');
            s = s.replace(/(^|[^a-zA-Z\\])(int|sum|sin|cos|tan|cot|log|ln|exp|bar|vec|hat|begin|end|subset|supset|in|notin|cup|cap|emptyset|forall|exists|to|iff|cdot|ldots|cdots|pm|mp|times|div|le|ge)(?=[^a-zA-Z]|$)/g, '$1\\$2');
            return s;
        }

        function prepareParagraph(text) {
            if (!text) return "";
            try {
                // Chỉ chuẩn hóa các công thức nằm trong $...$ hoặc \(...\)
                return text.replace(/\$([^$]+)\$/g, function(match, inner) {
                    return '$' + fixMathTokens(inner) + '$';
                }).replace(/\\\(([\s\S]*?)\\\)/g, function(match, inner) {
                    return '\\(' + fixMathTokens(inner) + '\\)';
                });
            } catch(e) {
                return text;
            }
        }

        function prepareChoice(label) {
            if (!label) return "";
            var s = label.trim();
            try {
                if (s.indexOf('$') !== -1 || s.indexOf('\\(') !== -1) {
                    return prepareParagraph(s);
                }
                if (/(frac|sqrt|infty|cases|lim|\\frac|\\sqrt|\^|_)/.test(s)) {
                    return '$' + fixMathTokens(s) + '$';
                }
            } catch(e) {
                return s;
            }
            return s;
        }

        function renderAllMath() {
            try {
                if (window.renderMathInElement) {
                    renderMathInElement(document.getElementById('game-container'), {
                        delimiters: [
                            {left: '$$', right: '$$', display: true},
                            {left: '$', right: '$', display: false},
                            {left: '\\(', right: '\\)', display: false},
                            {left: '\\[', right: '\\]', display: true}
                        ],
                        throwOnError: false
                    });
                }
            } catch(e) {
                console.warn("Lỗi renderMathInElement:", e);
            }
        }

        fetch('story.json').then(response => {
            if (!response.ok) throw new Error("HTTP " + response.status + ": Không thể đọc file story.json");
            return response.text();
        }).then(storyContent => {
            var story = new inkjs.Story(storyContent);
            var storyContainer = document.getElementById('story');
            var choicesContainer = document.getElementById('choices');
            var activeImage = "";
            function continueStory() {
                try {
                    storyContainer.innerHTML = '';
                    choicesContainer.innerHTML = '';
                    var allTags = [];
                    while(story.canContinue) {
                        var paragraphText = story.Continue();
                        if (story.currentTags) {
                            allTags = allTags.concat(story.currentTags);
                        }
                        if(paragraphText.trim() !== '') {
                            var p = document.createElement('p');
                            p.textContent = prepareParagraph(paragraphText);
                            storyContainer.appendChild(p);
                        }
                    }
                    
                    var imageTag = allTags.find(function(tag) { return tag.toLowerCase().indexOf('image:') !== -1; });
                    if (imageTag) {
                        activeImage = imageTag.split(':')[1].trim();
                    }
                    if (activeImage) {
                        var img = document.createElement('img');
                        img.src = 'images/' + activeImage;
                        img.className = 'story-img';
                        img.alt = 'Minh họa';
                        storyContainer.insertBefore(img, storyContainer.firstChild);
                    }

                    if (story.currentChoices.length === 0 && !story.canContinue) {
                        var endP = document.createElement('p');
                        endP.style.textAlign = 'center';
                        endP.style.color = '#4CAF50';
                        endP.style.fontWeight = 'bold';
                        endP.style.fontSize = '22px';
                        endP.style.marginTop = '20px';
                        endP.innerHTML = '🎉 Chúc mừng bạn đã hoàn thành bài học!';
                        storyContainer.appendChild(endP);
                    }

                    story.currentChoices.forEach(function(choice) {
                        var button = document.createElement('a');
                        var label = choice.text.trim();
                        if (!label) {
                            var letters = ['A', 'B', 'C', 'D', 'E', 'F'];
                            label = 'Lựa chọn ' + (letters[choice.index] || (choice.index + 1));
                        }
                        button.textContent = prepareChoice(label);
                        button.className = 'choice';
                        button.onclick = function(e) {
                            e.preventDefault();
                            story.ChooseChoiceIndex(choice.index);
                            continueStory();
                        };
                        choicesContainer.appendChild(button);
                    });

                    renderAllMath();
                } catch(innerErr) {
                    console.error("Lỗi thực thi story:", innerErr);
                    storyContainer.innerHTML += "<p style='color:orange;'>Lỗi hiển thị kịch bản: " + innerErr.message + "</p>";
                }
            }
            continueStory();
        }).catch(err => {
            console.error("Lỗi nạp game:", err);
            document.getElementById('story').innerHTML = "<p style='color:red;'>Lỗi tải game: " + err.message + "<br><br>Vui lòng click đúp vào file Choi_Game_Truc_Quan.bat để chơi.</p>";
        });
    </script>
</body>
</html>"""
            with open(os.path.join(export_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)
            shutil.copy2(os.path.join("tools", "inklecate.exe"), os.path.join(export_dir, "inklecate.exe"))
            bat_path = os.path.join(export_dir, "Choi_Game_Truc_Quan.bat")
            with open(bat_path, "w", encoding="utf-8") as f:
                f.write("@echo off\n")
                f.write("title SINE Game Web Player\n")
                f.write("echo Dang khoi dong may chu ao de choi game...\n")
                f.write("start http://localhost:8000\n")
                f.write("python -m http.server 8000\n")
            self.log(f" ĐÓNG GÓI THÀNH CÔNG!")
            self.log(f"Thư mục game đã được lưu tại: {os.path.abspath(export_dir)}")
            self.log(f"-> Giáo viên chỉ cần mở thư mục này và click đúp vào file 'Choi_Game.bat' để chơi.")
            messagebox.showinfo("Thành công", f"Đã tạo game xong!\nThư mục: {export_dir}")
            os.startfile(export_dir)
        except Exception as e:
            self.log(f" Lỗi hệ thống: {str(e)}")
        finally:
            self.btn_gen.config(state="normal", bg="green")
    def run_command(self, cmd):
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", env=env)
        for line in process.stdout:
            self.log(line.strip())
            self.root.update_idletasks()
        process.wait()
        return process.returncode
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Đang khởi động Giao diện SINE GUI...")
    print("💡 Cửa sổ giao diện đang được hiển thị trên màn hình.")
    print("   (Nếu bị che khuất bởi VS Code, hãy nhìn thanh Taskbar hoặc bấm Alt+Tab).")
    print("=" * 60)
    root = tk.Tk()
    root.lift()
    root.attributes("-topmost", True)
    root.after(500, lambda: root.attributes("-topmost", False))
    root.focus_force()
    app = SINEApp(root)
    root.mainloop()