"""Script kiểm thử Giai đoạn 1 của Module Xử lý ảnh (DIP).

Chức năng:
1. Nạp ảnh đề thi (hoặc tự động tạo ảnh mẫu mô phỏng đề thi chụp nghiêng + thiếu sáng nếu chưa có ảnh).
2. Chạy thuật toán lọc nhiễu, cân bằng sáng CLAHE, nắn thẳng góc nghiêng.
3. Xuất ảnh đối sánh trực quan 4 bước để kiểm tra kết quả.
"""

import sys
import os
import argparse
import time
from pathlib import Path
import cv2
import numpy as np

# Thiết lập đường dẫn import
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "src"))

from dip_processor import ImageDIPProcessor


def generate_mock_tilted_exam(output_path: str, tilt_angle: float = -8.5) -> str:
    """Tạo một ảnh đề thi giả lập bị chụp nghiêng góc và bị bóng tối loang lổ."""
    h, w = 1200, 900
    canvas = np.ones((h, w), dtype=np.uint8) * 245  # Nền giấy hơi ngà

    # Thêm bóng tối loang lổ (Gradient shadow mô phỏng bóng điện thoại/ngón tay)
    X, Y = np.meshgrid(np.linspace(0, 1, w), np.linspace(0, 1, h))
    shadow = np.sin(X * np.pi * 0.8) * np.cos(Y * np.pi * 0.5) * 80
    noisy_paper = np.clip(canvas - shadow, 60, 255).astype(np.uint8)

    # Thêm nhiễu hạt (Gaussian noise nhẹ)
    noise = np.random.normal(0, 8, (h, w)).astype(np.int16)
    noisy_paper = np.clip(noisy_paper.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    # Viết chữ đề thi mô phỏng
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(noisy_paper, "DE THI KIEM TRA MON XU LY ANH SO", (140, 100), font, 1.0, (20,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "Thoi gian lam bai: 45 phut - He dao tao CNTT", (180, 150), font, 0.7, (40,), 2, cv2.LINE_AA)
    cv2.line(noisy_paper, (100, 180), (800, 180), (30,), 2)

    # Câu 1
    cv2.putText(noisy_paper, "Cau 1: He mau nao thuong duoc dung trong thiet bi in an?", (100, 260), font, 0.75, (20,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "A. RGB", (130, 310), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "B. CMYK", (130, 360), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "C. HSV", (130, 410), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "D. YUV", (130, 460), font, 0.7, (30,), 2, cv2.LINE_AA)

    # Câu 2
    cv2.putText(noisy_paper, "Cau 2: Thuat toan CLAHE thuoc nhom xu ly nao duoi day?", (100, 560), font, 0.75, (20,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "A. Can bang luoc do muc xam thich nghi", (130, 610), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "B. Bien doi hinh hoc 3D", (130, 660), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "C. Ma hoa nen video H.264", (130, 710), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "D. Phan doan anh bang K-Means", (130, 760), font, 0.7, (30,), 2, cv2.LINE_AA)

    # Câu 3
    cv2.putText(noisy_paper, "Cau 3: Phep toan hinh thai hoc Dilation co tac dung gi?", (100, 860), font, 0.75, (20,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "A. Gian no va lam day vung diem anh trang", (130, 910), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "B. Xoa bo cac canh sac net", (130, 960), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "C. Thu hep kich thuoc vat the", (130, 1010), font, 0.7, (30,), 2, cv2.LINE_AA)
    cv2.putText(noisy_paper, "D. Triet tieu hoan toan kenh mau do", (130, 1060), font, 0.7, (30,), 2, cv2.LINE_AA)

    # Xoay ảnh mô phỏng việc chụp nghiêng
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, tilt_angle, 1.0)
    tilted = cv2.warpAffine(noisy_paper, M, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=200)

    # Lưu ra đĩa bằng imencode để hỗ trợ đường dẫn tiếng Việt
    out_dir = Path(output_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    ext = Path(output_path).suffix or ".jpg"
    success, enc = cv2.imencode(ext, tilted)
    if success:
        with open(output_path, "wb") as f:
            f.write(enc)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Chạy thử nghiệm Giai đoạn 1 Module DIP")
    parser.add_argument("--image", default="", help="Đường dẫn file ảnh đề thi cần test")
    args = parser.parse_args()

    input_img_path = args.image
    if not input_img_path or not os.path.exists(input_img_path):
        print("💡 Chưa cung cấp ảnh đề thi thực tế, tự động sinh ảnh mẫu mô phỏng đề thi chụp nghiêng...")
        test_dir = PROJECT_ROOT / "test_images"
        input_img_path = str(test_dir / "sample_exam_tilted.jpg")
        generate_mock_tilted_exam(input_img_path, tilt_angle=-7.5)
        print(f" Đã tạo ảnh mẫu tại: {input_img_path}")

    print(f"\n BẮT ĐẦU CHẠY THỬ NGHIỆM GIAI ĐOẠN 1 (DIP PIPELINE)")
    print(f" File ảnh kiểm thử: {input_img_path}")

    dip = ImageDIPProcessor()
    t0 = time.time()
    res = dip.process_stage1(input_img_path)
    elapsed = time.time() - t0

    skew_angle = res["skew_angle"]
    print(f"\n[KẾT QUẢ PHÂN TÍCH]")
    print(f"  • Thời gian xử lý: {elapsed * 1000:.1f} ms")
    print(f"  • Góc nghiêng phát hiện được: {skew_angle:+.2f}°")
    print(f"  • Kích thước ảnh gốc: {res['original'].shape[1]}x{res['original'].shape[0]}")
    print(f"  • Kích thước ảnh sau nắn: {res['deskewed_gray'].shape[1]}x{res['deskewed_gray'].shape[0]}")

    # Xuất các ảnh kết quả
    out_dir = PROJECT_ROOT / "output" / "dip_test"
    out_dir.mkdir(parents=True, exist_ok=True)

    path_enhanced = out_dir / "step1_1_enhanced_clahe.png"
    path_deskewed = out_dir / "step1_2_deskewed.png"
    dip.save_image(res["enhanced_clahe"], str(path_enhanced))
    dip.save_image(res["deskewed_gray"], str(path_deskewed))

    # Vẽ bảng đối sánh 4 bước trực quan bằng Matplotlib
    try:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 3, figsize=(15, 6))

        axes[0].imshow(res["original"], cmap="gray" if len(res["original"].shape) == 2 else None)
        axes[0].set_title(f"[1] Ảnh gốc (Nghiêng ~ {skew_angle:.1f}°)", fontsize=11, fontweight="bold")
        axes[0].axis("off")

        axes[1].imshow(res["enhanced_clahe"], cmap="gray")
        axes[1].set_title("[2] Cân bằng sáng CLAHE & Khử nhiễu", fontsize=11, fontweight="bold")
        axes[1].axis("off")

        axes[2].imshow(res["deskewed_gray"], cmap="gray")
        axes[2].set_title("[3] Nắn thẳng về 0° (Deskewed)", fontsize=11, fontweight="bold")
        axes[2].axis("off")

        plt.tight_layout()
        comparison_path = out_dir / "step1_comparison.png"
        plt.savefig(str(comparison_path), dpi=150)
        plt.close()
        print(f" Đã lưu ảnh đối sánh trực quan tại: {comparison_path}")
    except Exception as e:
        print(f" Lưu ý khi vẽ biểu đồ: {e}")

    print(f"\n HOÀN THÀNH GIAI ĐOẠN 1!")
    print(f" Các ảnh kết quả đã được lưu trong thư mục: {out_dir}")


if __name__ == "__main__":
    main()
