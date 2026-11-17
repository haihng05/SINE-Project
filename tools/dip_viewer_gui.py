"""Giao diện xem trước kết quả Xử lý ảnh (DIP Studio Viewer).

Cho phép giáo viên/sinh viên:
1. Bấm nút chọn ảnh bất kỳ từ máy tính (.jpg, .png, .jpeg).
2. Tự động xử lý qua 4 bước: Ảnh gốc -> Nắn thẳng & CLAHE -> Nhị phân hóa -> Bóc tách Bounding Box.
3. Hiển thị trực quan trực tiếp trên giao diện để phục vụ báo cáo/demo.
"""

import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import cv2
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "src"))

from dip_processor import ImageDIPProcessor
from dip_metrics import DIPQualityEvaluator

try:
    from PIL import Image, ImageTk
except ImportError:
    # Cài pillow nếu chưa có
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageTk


class DIPViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SINE - DIP Studio (Kiểm tra thuật toán Xử lý ảnh)")
        self.root.geometry("1180x780")
        self.root.configure(bg="#222")

        self.dip = ImageDIPProcessor()
        self.evaluator = DIPQualityEvaluator()

        # Tiêu đề
        title_frame = tk.Frame(root, bg="#222")
        title_frame.pack(fill="x", pady=8)
        tk.Label(
            title_frame,
            text="HỆ THỐNG TRỰC QUAN HÓA THUẬT TOÁN XỬ LÝ ẢNH (DIP)",
            font=("Arial", 14, "bold"),
            fg="#4CAF50",
            bg="#222"
        ).pack()

        # Thanh công cụ
        toolbar = tk.Frame(root, bg="#333", padx=10, pady=8)
        toolbar.pack(fill="x", padx=15, pady=5)

        tk.Button(
            toolbar,
            text="📁 1. Chọn ảnh từ máy tính...",
            font=("Arial", 10, "bold"),
            bg="#1976D2",
            fg="white",
            padx=10,
            pady=4,
            command=self.browse_and_process
        ).pack(side="left")

        tk.Button(
            toolbar,
            text="📊 2. Chạy Benchmark & Biểu đồ...",
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=4,
            command=self.run_benchmark_popup
        ).pack(side="left", padx=8)

        self.lbl_path = tk.Label(
            toolbar,
            text="Chưa chọn ảnh (Hãy bấm nút bên trái)",
            font=("Arial", 10, "italic"),
            fg="#ddd",
            bg="#333"
        )
        self.lbl_path.pack(side="left", padx=10)

        self.lbl_info = tk.Label(
            toolbar,
            text="",
            font=("Arial", 10, "bold"),
            fg="#FFC107",
            bg="#333"
        )
        self.lbl_info.pack(side="right", padx=10)

        # Khung hiển thị 4 ảnh
        grid_frame = tk.Frame(root, bg="#222")
        grid_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # Khởi tạo 4 ô ảnh
        self.panels = []
        titles = [
            "[1] Ảnh gốc chụp thực tế",
            "[2] Cân bằng sáng CLAHE & Nắn thẳng 0°",
            "[3] Nhị phân hóa & Giãn nở hình thái học",
            "[4] Phân đoạn câu hỏi (ROI Bounding Boxes)"
        ]

        for i in range(2):
            for j in range(2):
                idx = i * 2 + j
                box = tk.LabelFrame(
                    grid_frame,
                    text=titles[idx],
                    font=("Arial", 10, "bold"),
                    fg="#4CAF50",
                    bg="#2b2b2b",
                    labelanchor="nw"
                )
                box.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")
                grid_frame.grid_rowconfigure(i, weight=1)
                grid_frame.grid_columnconfigure(j, weight=1)

                lbl = tk.Label(box, bg="#1e1e1e", text="Chưa có dữ liệu", fg="#888")
                lbl.pack(fill="both", expand=True, padx=5, pady=5)
                self.panels.append(lbl)

    def browse_and_process(self):
        filepath = filedialog.askopenfilename(
            title="Chọn ảnh đề thi",
            filetypes=[
                ("File ảnh hỗ trợ", "*.jpg *.jpeg *.png *.bmp *.webp"),
                ("Tất cả tập tin", "*.*")
            ]
        )
        if not filepath:
            return

        self.lbl_path.config(text=os.path.basename(filepath))
        self.lbl_info.config(text="Đang xử lý thuật toán DIP...")
        self.root.update_idletasks()

        try:
            import time
            t0 = time.time()
            res = self.dip.process_stage2(filepath)
            elapsed = (time.time() - t0) * 1000

            angle = res["skew_angle"]
            boxes_count = len(res["boxes"])

            # Đo đạc chất lượng DIP metrics
            m = self.evaluator.evaluate_image_enhancement(res["deskewed_gray"], res["enhanced"])
            self.lbl_info.config(
                text=f"{elapsed:.0f}ms | Góc: {angle:+.2f}° | Tương phản: {m['contrast_gain_pct']:+.1f}% | Sắc nét: {m['sharpness_gain_pct']:+.1f}% | SSIM: {m['ssim']:.3f} | ROIs: {boxes_count}"
            )

            # Chuyển đổi và hiển thị lên 4 ô
            # 1. Ảnh gốc
            img1 = self.cv2_to_tk(res["original"], target_size=(500, 320))
            self.panels[0].config(image=img1, text="")
            self.panels[0].image = img1

            # 2. Cân bằng sáng & Nắn thẳng
            img2 = self.cv2_to_tk(res["deskewed_gray"], target_size=(500, 320))
            self.panels[1].config(image=img2, text="")
            self.panels[1].image = img2

            # 3. Nhị phân hóa & Giãn nở
            img3 = self.cv2_to_tk(res["dilated_mask"], target_size=(500, 320))
            self.panels[2].config(image=img3, text="")
            self.panels[2].image = img3

            # 4. Phân đoạn Bounding Boxes
            img4 = self.cv2_to_tk(res["annotated"], target_size=(500, 320))
            self.panels[3].config(image=img4, text="")
            self.panels[3].image = img4

        except Exception as e:
            messagebox.showerror("Lỗi xử lý", f"Không thể xử lý ảnh này:\n{str(e)}")
            self.lbl_info.config(text="Lỗi!")

    def run_benchmark_popup(self):
        """Chạy toàn bộ benchmark trên thư mục test_images và thông báo."""
        from evaluate_dip_metrics import run_evaluation
        self.lbl_info.config(text="Đang đo đạc toàn bộ bộ dữ liệu Benchmark...")
        self.root.update_idletasks()
        try:
            run_evaluation()
            chart_path = PROJECT_ROOT / "output" / "dip_metrics_chart.png"
            rep_path = PROJECT_ROOT / "output" / "dip_evaluation_report.md"
            msg = f"Đã hoàn thành đo lường định lượng!\n\n1. Biểu đồ khoa học: {chart_path.name}\n2. Báo cáo Markdown: {rep_path.name}\n3. Bảng số liệu CSV: dip_evaluation_report.csv\n\nTất cả đã được lưu vào thư mục: output/"
            messagebox.showinfo("Thành công", msg)
            self.lbl_info.config(text="Đã xuất Báo cáo & Biểu đồ Benchmark thành công!")
            # Mở file ảnh biểu đồ
            if chart_path.exists():
                os.startfile(str(chart_path))
        except Exception as e:
            messagebox.showerror("Lỗi Benchmark", str(e))

    def cv2_to_tk(self, cv_img, target_size=(500, 320)):
        if len(cv_img.shape) == 2:
            rgb = cv2.cvtColor(cv_img, cv2.COLOR_GRAY2RGB)
        else:
            rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

        h, w = rgb.shape[:2]
        max_w, max_h = target_size
        scale = min(max_w / w, max_h / h)
        new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))

        resized = cv2.resize(rgb, (new_w, new_h), interpolation=cv2.INTER_AREA)
        pil_img = Image.fromarray(resized)
        return ImageTk.PhotoImage(pil_img)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", default="")
    args, _ = parser.parse_known_args()

    root = tk.Tk()
    root.lift()
    root.attributes("-topmost", True)
    root.after(500, lambda: root.attributes("-topmost", False))
    root.focus_force()
    app = DIPViewerApp(root)
    if args.image and os.path.exists(args.image):
        root.after(200, lambda: app.process_file(args.image))
    root.mainloop()
