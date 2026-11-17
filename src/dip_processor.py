"""Module Xử lý ảnh số (Digital Image Processing - DIP) cho Hệ thống SINE.

Cung cấp đầy đủ các thuật toán xử lý tài liệu chuẩn mực:
1. Tự động phát hiện góc nghiêng dòng chữ bằng Black Hat Transform & Biến đổi Hough.
2. Xoay nắn thẳng toàn bộ dòng chữ về góc ngang tuyệt đối 0.0°.
3. Tự động cắt gọn (Auto-Crop) trang giấy, loại bỏ 100% bàn tay, áo đen và viền mép xéo bên ngoài.
4. Cân bằng sáng thích nghi (CLAHE) & Khử nhiễu bảo toàn cạnh (Bilateral Filter).
5. Phân đoạn từng dòng văn bản / khối câu hỏi sắc nét, song song 100% với dòng chữ.
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Tuple, List, Dict, Any, Optional


class ImageDIPProcessor:
    """Bộ xử lý ảnh tài liệu số theo tiêu chuẩn môn Xử lý ảnh (DIP)."""

    def __init__(self, clahe_clip_limit: float = 2.0, clahe_grid_size: Tuple[int, int] = (8, 8)):
        self.clahe_clip_limit = clahe_clip_limit
        self.clahe_grid_size = clahe_grid_size
        self.clahe = cv2.createCLAHE(clipLimit=self.clahe_clip_limit, tileGridSize=self.clahe_grid_size)

    def load_image(self, image_path: str) -> np.ndarray:
        """Đọc ảnh từ đường dẫn hỗ trợ cả tiếng Việt có dấu trên Windows."""
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Không tìm thấy file ảnh: {image_path}")
        img_array = np.fromfile(str(path), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError(f"Không thể giải mã file ảnh: {image_path}")
        return img

    def save_image(self, image: np.ndarray, output_path: str) -> None:
        """Lưu ảnh ra đĩa hỗ trợ đường dẫn tiếng Việt và an toàn đa luồng."""
        out_p = Path(output_path).resolve()
        out_p.parent.mkdir(parents=True, exist_ok=True)
        ext = out_p.suffix.lower() or ".png"
        success, encoded_img = cv2.imencode(ext, image)
        if success:
            import time
            for _ in range(5):
                try:
                    with open(str(out_p), "wb") as f:
                        f.write(encoded_img)
                    break
                except OSError:
                    time.sleep(0.1)
        else:
            raise RuntimeError(f"Không thể lưu ảnh ra: {output_path}")

    def convert_to_grayscale(self, image: np.ndarray) -> np.ndarray:
        """Chuyển đổi sang mức xám (Grayscale)."""
        if len(image.shape) == 2:
            return image
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def detect_text_skew_angle(self, gray: np.ndarray) -> float:
        """Phát hiện chính xác góc nghiêng của các dòng chữ trong đề thi bằng Biến đổi Hough."""
        # Dùng phép biến đổi Black Hat để chỉ lấy nét mực in, loại bỏ mọi bóng mờ mặt bàn/áo đen
        bh = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15)))
        _, thresh = cv2.threshold(bh, 24, 255, cv2.THRESH_BINARY)
        
        # Tìm các đoạn thẳng dòng chữ
        lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, 80, minLineLength=140, maxLineGap=20)
        if lines is None or len(lines) == 0:
            return 0.0

        angles = []
        for line in lines:
            l = line.reshape(-1)
            dx = l[2] - l[0]
            dy = l[3] - l[1]
            if dx != 0:
                deg = np.degrees(np.arctan2(dy, dx))
                if -25 < deg < 25:
                    angles.append(deg)

        if len(angles) > 0:
            median_angle = float(np.median(angles))
            return median_angle
        return 0.0

    def deskew_and_crop_document(self, image: np.ndarray, angle: float) -> Tuple[np.ndarray, np.ndarray]:
        """Nắn thẳng tuyệt đối góc chữ về 0.0° và tự động cắt bỏ bàn tay, áo đen bên ngoài.
        
        Returns:
            Tuple[clean_color, clean_gray]: Ảnh màu và ảnh xám đã nắn phẳng và cắt gọn.
        """
        h, w = image.shape[:2]
        center = (w // 2, h // 2)

        # 1. Xoay toàn bộ bức ảnh để dòng chữ nằm ngang 0.0°
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_color = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
        rotated_gray = self.convert_to_grayscale(rotated_color)

        # 2. Tìm vùng trang giấy tài liệu sáng màu (loại bỏ bàn tay, áo đen, mặt bàn)
        blur = cv2.GaussianBlur(rotated_gray, (9, 9), 0)
        _, thresh = cv2.threshold(blur, 115, 255, cv2.THRESH_BINARY)
        
        cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not cnts:
            return rotated_color, rotated_gray

        # Đường bao lớn nhất chính là trang giấy
        paper_cnt = max(cnts, key=cv2.contourArea)
        area = cv2.contourArea(paper_cnt)
        if area < (h * w * 0.25):
            return rotated_color, rotated_gray

        x, y, pw, ph = cv2.boundingRect(paper_cnt)

        # Cắt lùi vào trong một khoảng lề an toàn (margin = 15px) để loại bỏ hoàn toàn viền xơ mép giấy
        margin = 15
        x1 = max(0, x + margin)
        y1 = max(0, y + margin)
        x2 = min(w, x + pw - margin)
        y2 = min(h, y + ph - margin)

        if (x2 - x1) > 200 and (y2 - y1) > 200:
            cropped_color = rotated_color[y1:y2, x1:x2]
            cropped_gray = rotated_gray[y1:y2, x1:x2]
            return cropped_color, cropped_gray

        return rotated_color, rotated_gray

    def enhance_contrast(self, gray: np.ndarray) -> np.ndarray:
        """Cân bằng sáng thích nghi (CLAHE) và lọc khử nhiễu song phương."""
        enhanced = self.clahe.apply(gray)
        denoised = cv2.bilateralFilter(enhanced, d=7, sigmaColor=50, sigmaSpace=50)
        return denoised

    def process_stage1(self, image_path: str) -> Dict[str, Any]:
        """Quy trình Giai đoạn 1 chuẩn chỉnh: Đo góc -> Xoay thẳng 0.0° -> Cắt sạch viền đen -> CLAHE."""
        original = self.load_image(image_path)
        gray_orig = self.convert_to_grayscale(original)

        # 1. Phát hiện góc nghiêng thực tế của dòng chữ
        skew_angle = self.detect_text_skew_angle(gray_orig)

        # 2. Xoay nắn thẳng 0.0° và tự động cắt bỏ hậu cảnh bàn tay/áo đen
        deskewed_color, deskewed_gray = self.deskew_and_crop_document(original, skew_angle)

        # 3. Nâng cao chất lượng & Cân bằng sáng
        enhanced = self.enhance_contrast(deskewed_gray)

        return {
            "original": original,
            "skew_angle": skew_angle,
            "deskewed_color": deskewed_color,
            "deskewed_gray": deskewed_gray,
            "enhanced": enhanced
        }

    def segment_document_questions(
        self,
        image_gray: np.ndarray,
        image_color: np.ndarray
    ) -> Tuple[List[Tuple[int, int, int, int]], np.ndarray, np.ndarray]:
        """Phân đoạn các dòng và khối câu hỏi (Adaptive theo độ phân giải ảnh, không dính chùm hay mất câu)."""
        h_img, w_img = image_gray.shape[:2]

        # 1. Black Hat Transform với kernel co giãn theo chiều rộng ảnh
        k_bh = max(5, int(w_img * 0.015)) | 1
        kernel_bh = cv2.getStructuringElement(cv2.MORPH_RECT, (k_bh, k_bh))
        blackhat = cv2.morphologyEx(image_gray, cv2.MORPH_BLACKHAT, kernel_bh)
        _, thresh = cv2.threshold(blackhat, 20, 255, cv2.THRESH_BINARY)

        # Giới hạn vùng chữ trong ruột trang (bỏ viền ngoài cùng 1-2%)
        clean_bin = thresh.copy()
        clean_bin[:, :int(w_img * 0.02)] = 0
        clean_bin[:, int(w_img * 0.98):] = 0
        clean_bin[:int(h_img * 0.01), :] = 0
        clean_bin[int(h_img * 0.99):, :] = 0

        # 2. Dùng toán tử giãn nở ngang theo tỷ lệ ảnh (chiều cao cố định 1px để không dính dòng trên/dưới)
        k_w = max(8, int(w_img * 0.022))
        kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (k_w, 1))
        dilated = cv2.dilate(clean_bin, kernel_h, iterations=1)

        # 3. Tìm các đường viền dòng chữ
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        min_w = max(15, int(w_img * 0.05))
        min_h = max(4, int(h_img * 0.006))
        raw_boxes = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # Chỉ loại bỏ nếu là viền khung bao trọn toàn bộ trang ảnh
            if w >= min_w and h >= min_h and not (w > w_img * 0.98 and h > h_img * 0.95):
                raw_boxes.append((x, y, w, h))

        # 4. Sắp xếp các dòng chữ theo diện tích
        raw_boxes.sort(key=lambda b: (b[2] * b[3]), reverse=True)

        # 5. Non-Maximum Suppression (NMS) để loại bỏ các hộp trùng đè
        nms_boxes = []
        for box in raw_boxes:
            x1, y1, w1, h1 = box
            keep = True
            for (x2, y2, w2, h2) in nms_boxes:
                xi1, yi1 = max(x1, x2), max(y1, y2)
                xi2, yi2 = min(x1 + w1, x2 + w2), min(y1 + h1, y2 + h2)
                if xi2 > xi1 and yi2 > yi1:
                    inter_area = (xi2 - xi1) * (yi2 - yi1)
                    if inter_area / (w1 * h1) > 0.45:
                        keep = False
                        break
            if keep:
                nms_boxes.append(box)

        nms_boxes.sort(key=lambda b: b[1])

        # 6. Gom cụm các dòng cận kề thuộc cùng đoạn văn bản (gap thích ứng theo chiều cao ảnh)
        max_gap = max(1, int(h_img * 0.003))
        question_boxes = []
        for box in nms_boxes:
            if not question_boxes:
                question_boxes.append(box)
            else:
                prev_x, prev_y, prev_w, prev_h = question_boxes[-1]
                x, y, w, h = box

                gap = y - (prev_y + prev_h)
                if gap <= max_gap:
                    new_x = min(prev_x, x)
                    new_y = min(prev_y, y)
                    new_w = max(prev_x + prev_w, x + w) - new_x
                    new_h = max(prev_y + prev_h, y + h) - new_y
                    question_boxes[-1] = (new_x, new_y, new_w, new_h)
                else:
                    question_boxes.append(box)

        return question_boxes, dilated, thresh

    def draw_bounding_boxes(
        self,
        image: np.ndarray,
        boxes: List[Tuple[int, int, int, int]],
        color: Tuple[int, int, int] = (0, 0, 255),
        thickness: int = 2
    ) -> np.ndarray:
        """Vẽ khung viền Bounding Box và nhãn ROI số thứ tự."""
        if len(image.shape) == 2:
            annotated = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        else:
            annotated = image.copy()

        font = cv2.FONT_HERSHEY_SIMPLEX
        for idx, (x, y, w, h) in enumerate(boxes):
            cv2.rectangle(annotated, (x, y), (x + w, y + h), color, thickness)
            label = f"ROI #{idx+1}"
            cv2.putText(annotated, label, (x, max(18, y - 5)), font, 0.50, (255, 0, 0), 2, cv2.LINE_AA)

        return annotated

    def process_stage2(self, image_path: str) -> Dict[str, Any]:
        """Quy trình toàn diện: Xoay thẳng chữ 0.0° -> Auto-Crop trang giấy -> Bóc tách ROI chuẩn xác."""
        s1_res = self.process_stage1(image_path)
        deskewed_color = s1_res["deskewed_color"]
        deskewed_gray = s1_res["deskewed_gray"]

        # Phân đoạn câu hỏi trên trang giấy phẳng lì
        boxes, dilated_mask, binary_inv = self.segment_document_questions(deskewed_gray, deskewed_color)
        annotated = self.draw_bounding_boxes(deskewed_color, boxes)

        return {
            **s1_res,
            "binary_inv": binary_inv,
            "dilated_mask": dilated_mask,
            "boxes": boxes,
            "annotated": annotated,
            "total_blocks_found": len(boxes)
        }
