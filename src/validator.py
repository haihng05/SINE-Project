import re
import json
import subprocess
import unicodedata
from pathlib import Path
from collections import deque

def normalize_text(text: str) -> str:
    """Chuẩn hóa chuỗi văn bản (Unicode NFC, lowercase, loại bỏ khoảng trắng thừa)."""
    if not text:
        return ""
    text = unicodedata.normalize("NFC", str(text))
    return " ".join(text.strip().lower().split())

class SINEValidator:
    def __init__(self, inklecate_path: Path):
        self.inklecate_path = inklecate_path

    def compile_check(self, ink_text: str, temp_path: Path) -> tuple[bool, str]:
        """Tiêu chí C (Compilation): Biên dịch cú pháp qua inklecate."""
        temp_path.write_text(ink_text, encoding="utf-8")
        try:
            res = subprocess.run(
                [str(self.inklecate_path), "-j", str(temp_path)],
                capture_output=True,
                text=True,
                encoding="utf-8"
            )
            if res.returncode == 0:
                return True, ""
            else:
                error_msg = res.stderr or res.stdout
                return False, f"Compile Error: {error_msg.strip()}"
        except Exception as e:
            return False, f"Execution Error: {str(e)}"

    def playability_check(self, ink_text: str) -> tuple[bool, str]:
        """Tiêu chí P (Playability): Tìm đường đi từ Knot đầu đến END bằng BFS."""
        # 1. Tìm start knot
        start_match = re.search(r"->\s*([a-zA-Z0-9_]+)", ink_text)
        if not start_match:
            return False, "Playability Error: Không tìm thấy điểm bắt đầu (thiếu '-> start_knot')."
        start_knot = start_match.group(1).strip()

        # 2. Tách các Knot và đồ thị chuyển nhánh
        knots = re.split(r"===\s*([a-zA-Z0-9_]+)\s*===", ink_text)
        graph = {}
        if len(knots) > 1:
            for i in range(1, len(knots), 2):
                knot_name = knots[i].strip()
                body = knots[i+1]
                # Tìm các target chuyển tiếp (-> target hoặc * [...] -> target)
                targets = re.findall(r"->\s*([a-zA-Z0-9_]+|END|DONE)", body)
                graph[knot_name] = set(targets)

        # 3. BFS tìm đường tới END
        if start_knot not in graph:
            return False, f"Playability Error: Knot bắt đầu '{start_knot}' không tồn tại trong kịch bản."

        queue = deque([start_knot])
        visited = set([start_knot])
        has_path_to_end = False

        while queue:
            curr = queue.popleft()
            for nxt in graph.get(curr, []):
                if nxt == "END" or nxt == "DONE":
                    has_path_to_end = True
                    break
                if nxt in graph and nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
            if has_path_to_end:
                break

        if has_path_to_end:
            return True, ""
        return False, "Playability Error: Không tìm thấy đường đi nào từ điểm bắt đầu tới điểm kết thúc ('-> END')."

    def fidelity_check(self, ink_text: str, seed: dict) -> tuple[bool, str]:
        """Tiêu chí Q (Fidelity): Kiểm tra sự toàn vẹn của câu hỏi và đáp án từ Seed."""
        norm_script = normalize_text(ink_text)
        missing_errors = []

        for task in seed.get("tasks", []):
            task_id = task.get("id", "unknown_task")
            stem = task["question"]["stem"]
            norm_stem = normalize_text(stem)

            # Kiểm tra câu hỏi có trong kịch bản không
            if norm_stem not in norm_script:
                missing_errors.append(f"Task '{task_id}': Thiếu nội dung câu hỏi ('{stem}').")

            # Kiểm tra các đáp án
            for opt in task["question"]["options"]:
                norm_opt = normalize_text(opt)
                if norm_opt not in norm_script:
                    missing_errors.append(f"Task '{task_id}': Thiếu lựa chọn đáp án ('{opt}').")

        if not missing_errors:
            return True, ""
        return False, "Fidelity Error:\n" + "\n".join(f"- {e}" for e in missing_errors)

    def validate_all(self, ink_text: str, seed: dict, temp_path: Path) -> dict:
        """Thực hiện toàn bộ bộ kiểm tra tự động."""
        c_ok, c_err = self.compile_check(ink_text, temp_path)
        p_ok, p_err = (False, "Chưa biên dịch được") if not c_ok else self.playability_check(ink_text)
        q_ok, q_err = self.fidelity_check(ink_text, seed)

        success = c_ok and p_ok and q_ok
        error_logs = [err for err in [c_err, p_err, q_err] if err]

        return {
            "success": success,
            "compilation": c_ok,
            "playability": p_ok,
            "fidelity": q_ok,
            "error_log": "\n".join(error_logs)
        }
