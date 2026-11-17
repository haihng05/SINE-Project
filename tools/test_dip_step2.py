"""Script kiểm thử Giai đoạn 2 của Module Xử lý ảnh (DIP).

Chức năng:
1. Nhị phân hóa thích nghi (Adaptive Gaussian Thresholding).
2. Phân đoạn hình thái học (Morphological Dilation) và Contours.
3. Trích xuất Bounding Boxes bao quanh từng câu hỏi trắc nghiệm.
4. Xuất ảnh so sánh 4 bước hoàn chỉnh của toàn bộ DIP Pipeline.
"""

import sys
import os
import argparse
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "src"))

from dip_processor import ImageDIPProcessor


def main():
    parser = argparse.ArgumentParser(description="Chạy thử nghiệm Giai đoạn 2 Module DIP")
    parser.add_argument("--image", default="", help="Đường dẫn file ảnh đề thi cần test")
    args = parser.parse_args()

    input_img_path = args.image
    if input_img_path:
        if not os.path.exists(input_img_path):
            print(f"⚠️ CẢNH BÁO: Không tìm thấy file ảnh '{input_img_path}'!")
            print(f"-> Vui lòng kiểm tra lại tên file hoặc đường dẫn.")
            print(f"-> Hệ thống tạm thời chuyển sang ảnh mẫu để demo...")
            input_img_path = str(PROJECT_ROOT / "test_images" / "sample_exam_tilted.jpg")
    else:
        input_img_path = str(PROJECT_ROOT / "test_images" / "sample_exam_tilted.jpg")

    print(f"\n BẮT ĐẦU CHẠY THỬ NGHIỆM GIAI ĐOẠN 2 (DIP PIPELINE)")
    print(f" File ảnh kiểm thử: {input_img_path}")

    dip = ImageDIPProcessor()
    t0 = time.time()
    res = dip.process_stage2(input_img_path)
    elapsed = time.time() - t0

    boxes = res["boxes"]
    print(f"\n[KẾT QUẢ PHÂN ĐOẠN]")
    print(f"  • Tổng thời gian xử lý: {elapsed * 1000:.1f} ms")
    print(f"  • Góc nghiêng đã nắn: {res['skew_angle']:+.2f}°")
    print(f"  • Số khối câu hỏi/tiêu đề phân đoạn được: {len(boxes)}")
    for idx, (x, y, w, h) in enumerate(boxes):
        print(f"    - Khối #{idx+1}: Tọa độ (x={x}, y={y}, w={w}, h={h})")

    # Lưu các ảnh kết quả
    out_dir = PROJECT_ROOT / "output" / "dip_test"
    out_dir.mkdir(parents=True, exist_ok=True)

    path_binary = out_dir / "step2_1_binary.png"
    path_dilated = out_dir / "step2_2_dilated_morphology.png"
    path_annotated = out_dir / "step2_3_segmented_boxes.png"

    dip.save_image(res["binary_inv"], str(path_binary))
    dip.save_image(res["dilated_mask"], str(path_dilated))
    dip.save_image(res["annotated"], str(path_annotated))

    # Vẽ bảng đối sánh 4 bước trực quan phục vụ báo cáo / thuyết minh
    try:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 2, figsize=(14, 14))

        axes[0, 0].imshow(res["original"], cmap="gray" if len(res["original"].shape) == 2 else None)
        axes[0, 0].set_title(f"[1] Ảnh gốc chụp nghiêng ({res['skew_angle']:.1f}°)", fontsize=11, fontweight="bold")
        axes[0, 0].axis("off")

        axes[0, 1].imshow(res["deskewed_gray"], cmap="gray")
        axes[0, 1].set_title("[2] Cân bằng sáng CLAHE & Nắn thẳng 0°", fontsize=11, fontweight="bold")
        axes[0, 1].axis("off")

        axes[1, 0].imshow(res["dilated_mask"], cmap="gray")
        axes[1, 0].set_title("[3] Nhị phân hóa & Giãn nở hình thái học", fontsize=11, fontweight="bold")
        axes[1, 0].axis("off")

        # OpenCV BGR sang RGB cho Matplotlib
        import cv2
        rgb_annotated = cv2.cvtColor(res["annotated"], cv2.COLOR_BGR2RGB)
        axes[1, 1].imshow(rgb_annotated)
        axes[1, 1].set_title(f"[4] Phân đoạn câu hỏi ({len(boxes)} Bounding Boxes)", fontsize=11, fontweight="bold")
        axes[1, 1].axis("off")

        plt.tight_layout()
        comparison_path = out_dir / "step2_full_pipeline_dashboard.png"
        try:
            plt.savefig(str(comparison_path), dpi=150)
        except OSError:
            # Nếu file đang bị Windows Photo Viewer mở và khóa, lưu vào file mới
            comparison_path = out_dir / "step2_dashboard_latest.png"
            plt.savefig(str(comparison_path), dpi=150)
        plt.close()
        print(f"\n Đã xuất Dashboard đối sánh 4 bước tại: {comparison_path}")

        # Tự động mở ảnh kết quả trên màn hình Windows
        try:
            os.startfile(str(comparison_path))
            print("🚀 Đã tự động mở ảnh kết quả trên màn hình của bạn!")
        except Exception:
            pass
    except Exception as e:
        print(f" Lưu ý khi vẽ Dashboard: {e}")

    print(f"\n HOÀN THÀNH GIAI ĐOẠN 2!")


if __name__ == "__main__":
    main()
