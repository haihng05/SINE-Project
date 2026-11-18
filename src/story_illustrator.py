"""Module tự động minh họa bối cảnh game bằng Trí tuệ nhân tạo (AI Story Illustrator).

Chức năng:
1. Phân tích kịch bản Ink (.ink) để trích xuất các địa điểm (locations) và đoạn văn miêu tả không gian.
2. Dùng AI Director để sinh Image Prompt tiếng Anh chuẩn mỹ thuật Visual Novel 2D anime.
3. Sinh ảnh bối cảnh chất lượng cao (16:9, 640x384) qua mạng lưới Stable Diffusion (AI Horde) hoàn toàn tự động.
4. Cơ chế dự phòng thông minh (Fallback): Tự động gán ảnh theo chủ đề nếu mất kết nối mạng, đảm bảo không bao giờ gián đoạn tiến trình xuất game.
5. Tự động chèn thẻ tag `# image: <ten_anh>.jpg` vào kịch bản Ink và biên dịch lại sang `story.json`.
"""

import re
import os
import sys
import json
import time
import shutil
import hashlib
import urllib.request
import urllib.parse
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class StoryIllustrator:
    """Bộ tạo ảnh minh họa bối cảnh tự động ăn khớp với cốt truyện từng game."""

    def __init__(self, client=None, model_name: str = ""):
        self.client = client
        self.model_name = model_name

    def extract_locations(self, ink_text: str) -> List[Dict[str, str]]:
        """Trích xuất danh sách các địa điểm bối cảnh và câu văn mô tả từ kịch bản Ink."""
        has_locations = bool(re.search(r"===\s*location_[a-zA-Z0-9_]+\s*===", ink_text))
        prefix_pattern = r"location_[a-zA-Z0-9_]+" if has_locations else r"(?:location_|task_)[a-zA-Z0-9_]+"
        pattern = rf"===\s*({prefix_pattern})\s*===\s*\n(.*?)(?=\n\s*\+[\s\[]|\n\s*===|\Z)"
        matches = re.findall(pattern, ink_text, re.DOTALL)
        locations = []
        seen_ids = set()
        for loc_id, body in matches:
            if "_success" in loc_id or "_fail" in loc_id or loc_id in seen_ids:
                continue
            seen_ids.add(loc_id)
            # Lọc bỏ các dòng tag đã có
            lines = [line.strip() for line in body.strip().split("\n") if line.strip() and not line.strip().startswith("#")]
            desc = " ".join(lines[:3]) if lines else "Bối cảnh học tập tương tác"
            locations.append({"id": loc_id, "description": desc})
        return locations

    def generate_image_prompts(self, locations: List[Dict[str, str]], topic: str = "general") -> Dict[str, str]:
        """Tự động phân tích ngữ cảnh mô tả và sinh prompt hình ảnh 2D Visual Novel phong phú."""
        # 1. Thử dùng AI Director (Gemini) để hiểu sâu ngữ cảnh đề bài
        gemini_key = os.environ.get("GEMINI_API_KEY", "")
        if not gemini_key:
            env_file = PROJECT_ROOT / ".env"
            if env_file.exists():
                with open(env_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("GEMINI_API_KEY="):
                            gemini_key = line.split("=", 1)[1].strip().strip('"').strip("'")

        if gemini_key:
            try:
                system_instruction = (
                    "You are a professional visual novel art director for educational games. "
                    "For each problem/location below, create a concise, visually evocative English image prompt (15-20 words). "
                    "Focus on physical objects, laboratory gear, mechanical devices, geometric structures, or architectural environments directly relevant to the problem. "
                    "Style: 2D anime visual novel background, scenic, cinematic lighting, 16:9, clean composition, NO text, NO characters. "
                    "Return ONLY a valid JSON object mapping each location_id to its English prompt."
                )
                input_payload = {loc["id"]: loc["description"] for loc in locations}
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": f"{system_instruction}\n\nSubject: {topic}\nTasks/Locations:\n{json.dumps(input_payload, ensure_ascii=False)}"
                        }]
                    }],
                    "generationConfig": {
                        "temperature": 0.3,
                        "responseMimeType": "application/json"
                    }
                }
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={gemini_key}"
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    cand_text = data.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")
                    prompts_map = json.loads(cand_text)
                    if isinstance(prompts_map, dict) and len(prompts_map) >= len(locations) * 0.7:
                        return prompts_map
            except Exception:
                pass

        # 2. Heuristic fallback phong phú nếu không có mạng
        topic_lower = topic.lower()
        topic_mapping = {
            "toan": "Mathematics & Sacred Geometry",
            "toanhoc": "Mathematics & Sacred Geometry",
            "hoahoc": "Modern Chemistry & Science Laboratory",
            "lichsu": "Ancient Vietnamese Heritage & Historic Architecture",
            "dialy": "Scenic Geography, Mountains & Rivers Landscape",
            "tienganh": "International Academy & Global Library",
            "vatly": "Quantum Physics & Advanced Engineering Chamber",
            "sinhoc": "Botanical Garden & Living Ecosystem"
        }
        topic_context = topic_mapping.get(topic_lower, "Educational Academy")

        prompts_dict = {}
        for loc in locations:
            desc = loc["description"].lower()
            env_keywords = []

            if any(k in desc for k in ["quả cầu", "xanh", "đỏ", "xác suất", "hộp"]):
                env_keywords.append("ancient wooden puzzle altar with glowing glass spheres in red and blue colors, mysterious mechanism")
            elif any(k in desc for k in ["bút chì", "gỗ", "than chì", "lăng trụ", "khối trụ"]):
                env_keywords.append("architectural drafting workshop with hexagonal wooden pencil prism and graphite cylinders, drafting table")
            elif any(k in desc for k in ["chóp", "s.abcd", "hình chữ nhật", "khoảng cách"]):
                env_keywords.append("futuristic holographic geometry chamber with floating glowing pyramid and 3D coordinate planes")
            elif any(k in desc for k in ["chuyển động", "vận tốc", "chất điểm", "đuổi kịp", "gia tốc"]):
                env_keywords.append("high-speed kinematic simulation chamber with glowing vector velocity trails and futuristic instruments")
            elif any(k in desc for k in ["số phức", "thuần ảo", "đường tròn", "mặt phẳng"]):
                env_keywords.append("astronomical observatory with glowing complex plane circular diagrams and celestial coordinate rings")
            elif any(k in desc for k in ["bể cá", "kính", "thể tích", "hộp chữ nhật"]):
                env_keywords.append("aquatic research laboratory with large transparent glass aquariums and sparkling water caustics")
            elif any(k in desc for k in ["phòng thí nghiệm", "ống nghiệm", "hóa chất", "bình tam giác", "hóa sinh"]):
                env_keywords.append("modern chemistry laboratory, glowing glass beakers, test tubes with colorful solutions, scientific instruments")
            elif any(k in desc for k in ["điện phân", "kim loại", "rỉ", "điện cực"]):
                env_keywords.append("high-tech industrial electrolysis chamber, neon copper electrodes, chemical reaction vat, dramatic reflections")
            elif any(k in desc for k in ["polymer", "sợi", "vật liệu", "tổng hợp"]):
                env_keywords.append("advanced materials synthesis laboratory, glowing macromolecular crystal models, futuristic scientific apparatus")
            elif any(k in desc for k in ["thư viện", "bức tường", "sách", "tài liệu", "hồ sơ"]):
                env_keywords.append("grand historic research library, towering mahogany bookshelves, warm lantern lighting, ancient scientific scrolls")
            elif any(k in desc for k in ["kho", "dụng cụ", "chưng cất", "nhiên liệu"]):
                env_keywords.append("scientific storage warehouse, rows of organized distillation glassware, industrial laboratory ambiance")
            elif any(k in desc for k in ["cổng", "sảnh", "khởi đầu", "viện"]):
                env_keywords.append(f"monumental entrance pavilion of {topic_context}, glass facade, cinematic morning sunlight, grand architecture")
            else:
                env_keywords.append(f"breathtaking visual novel scenery, {topic_context} research sanctuary, artistic lighting")

            prompt = (
                f"2D visual novel background concept art, {', '.join(env_keywords)}, "
                f"anime background style, cinematic lighting, 16:9 ratio, rich details, clean composition, no text, no characters"
            )
            prompts_dict[loc["id"]] = prompt

        return prompts_dict

    def generate_horde_image(self, prompt: str, output_path: Path, timeout: int = 120) -> bool:
        """Sinh ảnh qua AI Horde (Stable Diffusion API miễn phí, không cần key, kiên nhẫn đợi hoàn tất)."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Thêm negative prompt rõ ràng để tránh người và tránh false-positive của bộ lọc
        full_prompt = f"{prompt} ### blurry, human, people, face, skin, nude, nsfw, text, watermark"

        payload = {
            "prompt": full_prompt,
            "params": {
                "steps": 20,
                "width": 640,
                "height": 384,
                "sampler_name": "k_euler",
                "cfg_scale": 7.0,
                "n": 1
            },
            "nsfw": False,
            "censor_nsfw": False
        }

        try:
            req = urllib.request.Request(
                "https://stablehorde.net/api/v2/generate/async",
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "apikey": "0000000000",
                    "Content-Type": "application/json",
                    "Client-Agent": "SINE-Project:2.0:edu"
                }
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                job_id = res.get("id")

            if not job_id:
                return False

            start_t = time.time()
            while time.time() - start_t < timeout:
                time.sleep(2.5)
                status_req = urllib.request.Request(
                    f"https://stablehorde.net/api/v2/generate/status/{job_id}",
                    headers={"apikey": "0000000000", "Client-Agent": "SINE-Project:2.0:edu"}
                )
                try:
                    with urllib.request.urlopen(status_req, timeout=10) as s_resp:
                        s_data = json.loads(s_resp.read().decode("utf-8"))
                        if s_data.get("faulted") or s_data.get("is_possible") is False:
                            return False

                        if s_data.get("done"):
                            generations = s_data.get("generations", [])
                            if generations:
                                gen = generations[0]
                                # Nếu bị đánh cờ kiểm duyệt thì từ chối ngay để retry
                                if gen.get("censored"):
                                    return False
                                img_url = gen.get("img")
                                if not img_url:
                                    return False
                                img_req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
                                with urllib.request.urlopen(img_req, timeout=20) as img_resp:
                                    img_bytes = img_resp.read()
                                    # Kiểm tra mã băm và kích thước ảnh chống nhận nhầm banner cảnh báo censor
                                    if len(img_bytes) == 47207 or hashlib.md5(img_bytes).hexdigest() == "67fff27ddf4ca3b4bc3a9919206bd3e6":
                                        return False
                                    # Ghi file tạm để PIL chuyển đổi sang JPEG chuẩn
                                    temp_file = output_path.with_suffix(".tmp")
                                    with open(temp_file, "wb") as f_tmp:
                                        f_tmp.write(img_bytes)
                                    with Image.open(temp_file) as im:
                                        im.convert("RGB").save(output_path, "JPEG", quality=90)
                                    if temp_file.exists():
                                        temp_file.unlink()
                                    return True
                except Exception:
                    pass
        except Exception:
            pass

        return False

    def fallback_image(self, loc_id: str, topic: str, output_path: Path) -> bool:
        """Cơ chế dự phòng: sinh ảnh đồ họa bối cảnh Visual Novel công nghệ cao nếu mất kết nối mạng."""
        try:
            from PIL import ImageDraw, ImageFont
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Bảng màu chủ đề chuẩn phong cách Visual Novel
            topic_colors = {
                "toan": [(15, 30, 60), (40, 85, 140)],
                "toanhoc": [(15, 30, 60), (40, 85, 140)],
                "hoa": [(20, 50, 45), (45, 110, 95)],
                "hoahoc": [(20, 50, 45), (45, 110, 95)],
                "lichsu": [(60, 35, 20), (130, 75, 40)],
                "dialy": [(20, 55, 50), (40, 120, 105)],
                "vatly": [(35, 20, 65), (85, 50, 140)],
                "tienganh": [(25, 40, 65), (70, 95, 145)]
            }
            c1, c2 = topic_colors.get(topic.lower(), [(25, 40, 65), (65, 85, 125)])

            w, h = 640, 384
            img = Image.new("RGB", (w, h))
            pixels = img.load()
            for y in range(h):
                r = int(c1[0] + (c2[0] - c1[0]) * (y / h))
                g = int(c1[1] + (c2[1] - c1[1]) * (y / h))
                b = int(c1[2] + (c2[2] - c1[2]) * (y / h))
                for x in range(w):
                    dx = abs(x - w / 2) / (w / 2)
                    dy = abs(y - h / 2) / (h / 2)
                    vignette = 1.0 - 0.20 * (dx * dx + dy * dy)
                    pixels[x, y] = (int(r * vignette), int(g * vignette), int(b * vignette))

            draw = ImageDraw.Draw(img)
            # Vẽ lưới phối cảnh không gian công nghệ cao
            grid_color = (int(c2[0] * 1.3), int(c2[1] * 1.3), int(c2[2] * 1.3))
            center_x, center_y = w // 2, h // 2
            for i in range(-5, 6):
                x_pos = center_x + i * 55
                draw.line([(center_x, center_y - 40), (x_pos, h)], fill=grid_color, width=1)
            for y_line in range(center_y, h, 28):
                draw.line([(0, y_line), (w, y_line)], fill=grid_color, width=1)

            # Vẽ vòng tròn hologram trung tâm
            for radius in [70, 85, 100]:
                bbox = [center_x - radius, center_y - 40 - radius, center_x + radius, center_y - 40 + radius]
                draw.arc(bbox, start=0, end=360, fill=(180, 220, 255), width=2)

            # Điểm nhấn ánh sáng
            draw.ellipse([center_x - 6, center_y - 46, center_x + 6, center_y - 34], fill=(255, 255, 255))

            # Khung huy hiệu thông tin khu vực
            badge_w, badge_h = 280, 36
            b_x0, b_y0 = (w - badge_w) // 2, 25
            draw.rectangle([b_x0, b_y0, b_x0 + badge_w, b_y0 + badge_h], outline=(150, 210, 255), width=2)
            draw.text((b_x0 + 35, b_y0 + 10), f"SINE SYSTEM - {topic.upper()} ZONE", fill=(230, 245, 255))

            img.save(output_path, "JPEG", quality=90)
            return True
        except Exception:
            return False

    def illustrate_and_tag_story(
        self,
        ink_text: str,
        images_dir: Path,
        topic: str = "general",
        max_workers: int = 2,
        progress_callback: Optional[Callable[[str], None]] = None
    ) -> Tuple[str, List[str]]:
        """Quy trình toàn diện: Trích xuất -> Sinh Prompt -> Sinh ảnh AI -> Đính thẻ # image vào Ink."""
        images_dir = Path(images_dir)
        images_dir.mkdir(parents=True, exist_ok=True)

        locations = self.extract_locations(ink_text)
        if not locations:
            return ink_text, []

        if progress_callback:
            progress_callback(f"🖼️ Phân tích bối cảnh cho {len(locations)} địa điểm của môn {topic.upper()}...")

        # 1. Sinh danh sách prompt
        prompts = self.generate_image_prompts(locations, topic)

        if progress_callback:
            progress_callback(f"🎨 Đang kích hoạt AI vẽ {len(locations)} ảnh bối cảnh phong cách Visual Novel...")

        # 2. Xử lý ảnh tuần tự với độ kiên nhẫn cao, đảm bảo 100% sinh đủ và đúng hình
        downloaded_images = []
        total_locs = len(locations)
        for idx, loc in enumerate(locations, 1):
            loc_id = loc["id"]
            p = prompts.get(loc_id, f"anime visual novel background of {topic} research laboratory, sci-fi")
            img_filename = f"{loc_id}.jpg"
            img_path = images_dir / img_filename

            # Nếu ảnh đã tồn tại hợp lệ và kích thước chuẩn (>15KB) thì giữ nguyên, không cần gen lại
            if img_path.exists() and img_path.stat().st_size >= 15000:
                downloaded_images.append(img_filename)
                if progress_callback:
                    kb = round(img_path.stat().st_size / 1024, 1)
                    progress_callback(f"   ✓ [{idx}/{total_locs}] Ảnh đã sẵn sàng: {img_filename} ({kb} KB)")
                continue

            if progress_callback:
                progress_callback(f"   🎨 [{idx}/{total_locs}] AI đang vẽ bối cảnh {loc_id} theo đề bài...")

            # Thử lần 1: Prompt chi tiết từ Gemini (kiên nhẫn đợi GPU tới 120 giây)
            success = self.generate_horde_image(p, img_path, timeout=120)

            # Nếu lần 1 chưa thành công (lỗi node hoặc false-positive), thử lại lần 2 với prompt tối ưu
            if not success or not img_path.exists() or img_path.stat().st_size < 15000:
                if progress_callback:
                    progress_callback(f"   🔄 [{idx}/{total_locs}] Đang thử lại lần 2 cho {loc_id}...")
                time.sleep(2)
                clean_p = f"anime visual novel scenery, {p.split('###')[0].strip()}, 4k, masterpiece, highly detailed environment"
                success = self.generate_horde_image(clean_p, img_path, timeout=120)

            # Nếu lần 2 vẫn chưa được, thử lần 3 với prompt phòng thí nghiệm/không gian học thuật đặc thù
            if not success or not img_path.exists() or img_path.stat().st_size < 15000:
                if progress_callback:
                    progress_callback(f"   🔄 [{idx}/{total_locs}] Đang thử lại lần 3 cho {loc_id}...")
                time.sleep(2)
                scifi_p = f"anime visual novel background, futuristic {topic} research academy chamber, scientific equipment, 4k"
                success = self.generate_horde_image(scifi_p, img_path, timeout=120)

            if img_path.exists() and img_path.stat().st_size >= 15000:
                downloaded_images.append(img_filename)
                if progress_callback:
                    kb = round(img_path.stat().st_size / 1024, 1)
                    progress_callback(f"   ✓ [{idx}/{total_locs}] Đã hoàn tất ảnh bối cảnh {img_filename} ({kb} KB)")
            else:
                self.fallback_image(loc_id, topic, img_path)
                downloaded_images.append(img_filename)
                if progress_callback:
                    progress_callback(f"   ⚠️ [{idx}/{total_locs}] Sử dụng đồ họa phối cảnh công nghệ cho {img_filename}")

        # 3. Chèn thẻ tag `# image: ...` vào kịch bản Ink
        updated_ink = ink_text
        for loc in locations:
            loc_id = loc["id"]
            img_filename = f"{loc_id}.jpg"
            target_path = images_dir / img_filename
            if target_path.exists():
                # Kiểm tra nếu chưa có tag image thì chèn vào ngay sau === loc_id ===
                if not re.search(rf"===\s*{re.escape(loc_id)}\s*===\s*\n\s*#\s*image:", updated_ink):
                    pattern = rf"(===\s*{re.escape(loc_id)}\s*===\s*\n)"
                    replacement = rf"\1# image: {img_filename}\n"
                    updated_ink = re.sub(pattern, replacement, updated_ink, count=1)

        return updated_ink, downloaded_images


def illustrate_exported_game(export_dir: str, topic: str = "general", progress_callback=print):
    """Hàm tiện ích minh họa trực tiếp cho thư mục game đã xuất (Game_Export/Game_<topic>)."""
    p_export = Path(export_dir)
    ink_file = p_export / "story.ink"
    if not ink_file.exists():
        if progress_callback:
            progress_callback(f"❌ Không tìm thấy story.ink tại: {export_dir}")
        return

    images_dir = p_export / "images"
    ink_text = ink_file.read_text(encoding="utf-8")

    illustrator = StoryIllustrator()
    if progress_callback:
        progress_callback(f"🎨 Bắt đầu minh họa ảnh bối cảnh tự động cho: {p_export.name}...")

    updated_ink, imgs = illustrator.illustrate_and_tag_story(
        ink_text=ink_text,
        images_dir=images_dir,
        topic=topic,
        max_workers=3,
        progress_callback=progress_callback
    )

    # Ghi lại story.ink với đầy đủ tags
    ink_file.write_text(updated_ink, encoding="utf-8")
    if progress_callback:
        progress_callback(f"💾 Đã chèn thẻ # image: vào {ink_file.name}")

    # Biên dịch lại sang story.json
    inklecate_path = PROJECT_ROOT / "tools" / "inklecate.exe"
    if inklecate_path.exists():
        import subprocess
        json_path = p_export / "story.json"
        cmd = [str(inklecate_path), "-o", str(json_path), str(ink_file)]
        subprocess.run(cmd, check=True, capture_output=True)
        if progress_callback:
            progress_callback(f"🚀 Đã biên dịch lại kịch bản Web: {json_path.name} thành công!")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AI Story Illustrator")
    parser.add_argument("--export-dir", required=True, help="Thư mục game cần minh họa (ví dụ: Game_Export/Game_hoahoc)")
    parser.add_argument("--topic", default="general", help="Chủ đề môn học")
    args = parser.parse_args()

    illustrate_exported_game(args.export_dir, args.topic)
