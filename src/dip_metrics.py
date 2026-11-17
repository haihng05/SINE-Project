"""Module đo lường và đánh giá chất lượng ảnh số (DIP Evaluation Metrics).

Cung cấp đầy đủ các chỉ số toán học chuẩn mực phục vụ Bài tập lớn & Nghiên cứu khoa học:
1. Full-Reference (FR-IQA): MSE, PSNR, SSIM (Khi có ảnh tham chiếu/ảnh đối chứng).
2. No-Reference (NR-IQA):
   - Michelson Contrast (Độ tương phản vùng chữ / nền giấy).
   - RMS Contrast (Độ lệch chuẩn mức xám toàn cục).
   - Tenengrad Gradient Sharpness (Độ sắc nét biên cạnh nét chữ qua toán tử Sobel).
   - Background Uniformity & Noise (Độ sạch và đồng nhất của nền giấy, khử bóng mờ).
3. Đánh giá tự động hiệu quả trước và sau khi qua DIP Processor.
"""

import math
import cv2
import numpy as np
from pathlib import Path
from typing import Tuple, Dict, Any, List, Optional

try:
    from skimage.metrics import structural_similarity as ssim_func
except ImportError:
    ssim_func = None


def compute_mse(img1: np.ndarray, img2: np.ndarray) -> float:
    """Tính Sai số toàn phương trung bình (Mean Squared Error - MSE)."""
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    return float(np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2))


def compute_psnr(img1: np.ndarray, img2: np.ndarray, max_pixel: float = 255.0) -> float:
    """Tính Tỷ số tín hiệu cực đại trên nhiễu (Peak Signal-to-Noise Ratio - PSNR).
    
    Đơn vị: dB. Càng cao càng tốt (> 30 dB là chất lượng rất tốt).
    """
    mse = compute_mse(img1, img2)
    if mse == 0:
        return 100.0
    return float(10.0 * math.log10((max_pixel ** 2) / mse))


def compute_ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    """Tính Chỉ số tương đồng cấu trúc (Structural Similarity Index Measure - SSIM).
    
    Giá trị từ -1.0 đến 1.0 (càng gần 1.0 càng bảo toàn tốt cấu trúc nét chữ).
    """
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    if len(img1.shape) == 3:
        g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    else:
        g1 = img1
    if len(img2.shape) == 3:
        g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    else:
        g2 = img2

    if ssim_func is not None:
        val, _ = ssim_func(g1, g2, full=True)
        return float(val)
    else:
        # Tự tính SSIM xấp xỉ nếu chưa có skimage
        c1 = (0.01 * 255) ** 2
        c2 = (0.03 * 255) ** 2
        mu1 = cv2.GaussianBlur(g1.astype(np.float64), (11, 11), 1.5)
        mu2 = cv2.GaussianBlur(g2.astype(np.float64), (11, 11), 1.5)
        mu1_sq = mu1 ** 2
        mu2_sq = mu2 ** 2
        mu1_mu2 = mu1 * mu2
        sigma1_sq = cv2.GaussianBlur(g1.astype(np.float64) ** 2, (11, 11), 1.5) - mu1_sq
        sigma2_sq = cv2.GaussianBlur(g2.astype(np.float64) ** 2, (11, 11), 1.5) - mu2_sq
        sigma12 = cv2.GaussianBlur(g1.astype(np.float64) * g2.astype(np.float64), (11, 11), 1.5) - mu1_mu2
        ssim_map = ((2 * mu1_mu2 + c1) * (2 * sigma12 + c2)) / ((mu1_sq + mu2_sq + c1) * (sigma1_sq + sigma2_sq + c2))
        return float(np.mean(ssim_map))


def compute_michelson_contrast(gray: np.ndarray) -> float:
    """Tính Độ tương phản Michelson giữa vùng chữ (foreground) và nền giấy (background).
    
    Giá trị từ 0.0 (mờ tịt) đến 1.0 (tương phản hoàn hảo: chữ đen đậm, nền trắng tinh).
    """
    if len(gray.shape) == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    # Phân ngưỡng Otsu để tách vùng mực chữ và vùng nền giấy
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Vùng nền giấy (pixel trắng trong thresh)
    bg_pixels = gray[thresh == 255]
    # Vùng mực chữ (pixel đen trong thresh)
    fg_pixels = gray[thresh == 0]
    
    if len(bg_pixels) == 0 or len(fg_pixels) == 0:
        return 0.0
    
    mu_bg = float(np.mean(bg_pixels))
    mu_fg = float(np.mean(fg_pixels))
    
    if mu_bg + mu_fg == 0:
        return 0.0
    
    return float((mu_bg - mu_fg) / (mu_bg + mu_fg))


def compute_rms_contrast(gray: np.ndarray) -> float:
    """Tính Độ tương phản RMS (Root Mean Square Contrast).
    
    Đo độ lệch chuẩn phân bố mức xám trên toàn ảnh.
    """
    if len(gray.shape) == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    return float(np.std(gray) / 255.0)


def compute_tenengrad_sharpness(gray: np.ndarray) -> float:
    """Tính Độ sắc nét mép nét chữ qua toán tử Tenengrad Gradient (Sobel).
    
    Càng cao thì mép cạnh chữ càng sắc nét, không bị nhòe mờ.
    """
    if len(gray.shape) == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude_sq = gx ** 2 + gy ** 2
    return float(np.mean(gradient_magnitude_sq))


def compute_background_uniformity(gray: np.ndarray) -> float:
    """Tính Độ phân tán của nền giấy (Background Noise / Standard Deviation).
    
    Lấy 30% pixel sáng nhất đại diện cho nền giấy và tính độ lệch chuẩn mức xám.
    Giá trị CÀNG THẤP chứng minh nền giấy CÀNG SẠCH ĐỒNG NHẤT, bóng đổ đã bị triệt tiêu hoàn toàn.
    """
    if len(gray.shape) == 3:
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    
    # Lấy phân vị 70% trở lên (vùng nền giấy)
    threshold_val = np.percentile(gray, 70)
    bg_pixels = gray[gray >= threshold_val]
    
    if len(bg_pixels) == 0:
        return 0.0
    return float(np.std(bg_pixels))


class DIPQualityEvaluator:
    """Bộ công cụ đánh giá khoa học chất lượng xử lý ảnh số."""

    def __init__(self):
        pass

    def evaluate_image_enhancement(
        self,
        raw_image: np.ndarray,
        processed_image: np.ndarray,
        reference_image: Optional[np.ndarray] = None
    ) -> Dict[str, Any]:
        """So sánh định lượng chất lượng giữa ảnh gốc thô và ảnh đã qua DIP."""
        if len(raw_image.shape) == 3:
            raw_gray = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
        else:
            raw_gray = raw_image.copy()

        if len(processed_image.shape) == 3:
            proc_gray = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
        else:
            proc_gray = processed_image.copy()

        # 1. Đo độ tương phản chữ / nền (Michelson Contrast)
        c_raw = compute_michelson_contrast(raw_gray)
        c_proc = compute_michelson_contrast(proc_gray)
        contrast_gain = ((c_proc - c_raw) / (c_raw + 1e-6)) * 100.0

        # 2. Đo độ tương phản RMS
        rms_raw = compute_rms_contrast(raw_gray)
        rms_proc = compute_rms_contrast(proc_gray)

        # 3. Đo độ sắc nét nét chữ (Tenengrad Sharpness)
        # Resize proc_gray về cùng kích thước raw_gray để so sánh gradient công bằng
        proc_resized = cv2.resize(proc_gray, (raw_gray.shape[1], raw_gray.shape[0]))
        s_raw = compute_tenengrad_sharpness(raw_gray)
        s_proc = compute_tenengrad_sharpness(proc_resized)
        sharpness_gain = ((s_proc - s_raw) / (s_raw + 1e-6)) * 100.0

        # 4. Đo độ sạch nền giấy (Background Noise)
        bg_noise_raw = compute_background_uniformity(raw_gray)
        bg_noise_proc = compute_background_uniformity(proc_resized)
        bg_noise_reduction = ((bg_noise_raw - bg_noise_proc) / (bg_noise_raw + 1e-6)) * 100.0

        # 5. Full-Reference metrics (nếu có ảnh tham chiếu chuẩn)
        psnr_val = None
        ssim_val = None
        if reference_image is not None:
            psnr_val = compute_psnr(reference_image, proc_gray)
            ssim_val = compute_ssim(reference_image, proc_gray)
        else:
            # So sánh độ trung thực cấu trúc giữa ảnh trước và sau xử lý (Structural Preservation)
            psnr_val = compute_psnr(raw_gray, proc_resized)
            ssim_val = compute_ssim(raw_gray, proc_resized)

        return {
            "contrast_raw": round(c_raw, 4),
            "contrast_proc": round(c_proc, 4),
            "contrast_gain_pct": round(contrast_gain, 2),
            "rms_contrast_raw": round(rms_raw, 4),
            "rms_contrast_proc": round(rms_proc, 4),
            "sharpness_raw": round(s_raw, 1),
            "sharpness_proc": round(s_proc, 1),
            "sharpness_gain_pct": round(sharpness_gain, 2),
            "bg_noise_raw": round(bg_noise_raw, 2),
            "bg_noise_proc": round(bg_noise_proc, 2),
            "bg_noise_reduction_pct": round(bg_noise_reduction, 2),
            "psnr_db": round(psnr_val, 2) if psnr_val is not None else None,
            "ssim": round(ssim_val, 4) if ssim_val is not None else None,
        }
