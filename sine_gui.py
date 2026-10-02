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
        self.root.title("SINE - AI Game Generator cho Giáo Viên")
        self.root.geometry("700x550")
        tk.Label(root, text="HỆ THỐNG TẠO GAME GIÁO DỤC TỰ ĐỘNG", font=("Arial", 14, "bold")).pack(pady=10)
        frame_file = tk.Frame(root)
        frame_file.pack(fill="x", padx=20, pady=5)
        tk.Label(frame_file, text="1. Chọn Đề Thi (PDF/Word):", font=("Arial", 10)).pack(side="left")
        self.lbl_file = tk.Label(frame_file, text="Chưa chọn file", fg="blue", font=("Arial", 10, "italic"))
        self.lbl_file.pack(side="left", padx=10)
        tk.Button(frame_file, text="Duyệt...", command=self.browse_file).pack(side="right")
        self.selected_file = ""
        frame_topic = tk.Frame(root)
        frame_topic.pack(fill="x", padx=20, pady=5)
        tk.Label(frame_topic, text="2. Chủ đề / Tên bài học:", font=("Arial", 10)).pack(side="left")
        self.entry_topic = tk.Entry(frame_topic, width=30)
        self.entry_topic.insert(0, "toanhoc")
        self.entry_topic.pack(side="left", padx=10)
        self.btn_gen = tk.Button(root, text="3.  TỰ ĐỘNG TẠO VÀ ĐÓNG GÓI GAME", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.start_generation)
        self.btn_gen.pack(pady=15)
        tk.Label(root, text="Trạng thái hệ thống:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20)
        self.log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, font=("Consolas", 9))
        self.log_area.pack(fill="both", expand=True, padx=20, pady=5)
    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Documents", "*.pdf *.docx *.doc *.txt")])
        if filename:
            self.selected_file = filename
            self.lbl_file.config(text=os.path.basename(filename))
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
            self.log(f"\n[BƯỚC 1/3] AI Đang đọc đề thi và tách câu hỏi...")
            cmd_extract = [sys.executable, "extract_seed_from_doc.py", filepath, "--topic", topic]
            self.run_command(cmd_extract)
            seed_filename = f"seed_{topic}_auto.json"
            seed_path = os.path.join("seeds", seed_filename)
            if not os.path.exists(seed_path):
                self.log(" Lỗi: Không tìm thấy file seed được tạo ra. Quá trình thất bại.")
                self.btn_gen.config(state="normal", bg="green")
                return
            self.log(f" Đã trích xuất xong bộ câu hỏi: {seed_filename}")
            self.log(f"\n[BƯỚC 2/3] AI Đang sáng tác cốt truyện và lập trình game (Quá trình này có thể mất 1-2 phút)...")
            cmd_generate = [sys.executable, "run_single_test.py", "--seed", seed_filename]
            self.run_command(cmd_generate)
            ink_filename = f"game_seed_{topic}_auto.ink"
            ink_path = os.path.join("output", ink_filename)
            if not os.path.exists(ink_path):
                self.log(" Lỗi: Không tìm thấy file game (.ink) được tạo ra.")
                self.btn_gen.config(state="normal", bg="green")
                return
            self.log(f"\n[BƯỚC 3/3] Đang đóng gói thành bản Game độc lập...")
            export_dir = os.path.join("Game_Export", f"Game_{topic}")
            os.makedirs(export_dir, exist_ok=True)
            self.log(" Đang biên dịch kịch bản sang định dạng Web (JSON)...")
            subprocess.run([os.path.join("tools", "inklecate.exe"), "-o", os.path.join(export_dir, "story.json"), ink_path], capture_output=True)
            html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>SINE Game</title>
    <script src="https://unpkg.com/inkjs/dist/ink.js"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a1a1a; color: #f0f0f0; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; }
        #game-container { max-width: 800px; width: 100%; margin-top: 20px; background: #2a2a2a; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        #story { padding: 20px; min-height: 150px; font-size: 18px; line-height: 1.6; }
        .choice { display: block; margin: 10px 20px; padding: 15px; background: #3a5a7a; color: #fff; text-decoration: none; border-radius: 8px; cursor: pointer; transition: 0.2s; font-weight: bold; }
        .choice:hover { background: #4a7a9a; transform: translateX(5px); }
        .math-tex { font-family: 'Courier New', Courier, monospace; background: #333; padding: 2px 5px; border-radius: 3px; }
    </style>
</head>
<body>
    <div id="game-container">
                <div id="story"></div>
        <div id="choices"></div>
    </div>
    <script>
        fetch('story.json').then(response => response.text()).then(storyContent => {
            var story = new inkjs.Story(storyContent);
            var storyContainer = document.getElementById('story');
            var choicesContainer = document.getElementById('choices');
            function continueStory() {
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
                        p.innerHTML = paragraphText.replace(/\$([^$]+)\$/g, '<span class="math-tex">$1</span>');
                        storyContainer.appendChild(p);
                    }
                }
                story.currentChoices.forEach(function(choice) {
                    var button = document.createElement('a');
                    button.innerHTML = choice.text.replace(/\$([^$]+)\$/g, '<span class="math-tex">$1</span>');
                    button.className = 'choice';
                    button.onclick = function(e) {
                        e.preventDefault();
                        story.ChooseChoiceIndex(choice.index);
                        continueStory();
                    };
                    choicesContainer.appendChild(button);
                });
            }
            continueStory();
        }).catch(err => {
            document.getElementById('story').innerHTML = "<p style='color:red;'>Lỗi tải game: Vui lòng click đúp vào file Choi_Game_Truc_Quan.bat để chơi.</p>";
        });
    </script>
</body>
</html>"""
            with open(os.path.join(export_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)
            shutil.copy2(ink_path, os.path.join(export_dir, "story.ink"))
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
if __name__ == "__main__":
    root = tk.Tk()
    app = SINEApp(root)
    root.mainloop()