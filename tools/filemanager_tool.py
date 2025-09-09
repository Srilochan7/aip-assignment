"""
File Manager Tool
"""

from crewai.tools import BaseTool
import os
from datetime import datetime

class FileManagerTool(BaseTool):
    name: str = "File Manager Tool"
    description: str = "Save outputs to markdown files"
    out_dir: str = "outputs"   # ✅ Declare field here so Pydantic knows about it

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ensure directory exists
        os.makedirs(self.out_dir, exist_ok=True)

    def _run(self, content: str, filename: str = "output", ext="md") -> str:
        path = os.path.join(self.out_dir, f"{filename}.{ext}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    # convenience helpers
    def save_report(self, content: str, prefix: str, suffix: str) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{suffix}_{timestamp}"
        return self._run(content, filename, "md")

file_manager_tool = FileManagerTool()