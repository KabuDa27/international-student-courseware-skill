"""Smoke tests for the public, privacy-safe skill package."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicPackageTests(unittest.TestCase):
    def test_packaged_text_has_no_local_home_path_or_email(self) -> None:
        email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
        for file in ROOT.rglob("*"):
            if not file.is_file() or "__pycache__" in file.parts:
                continue
            if file.suffix not in {".md", ".py", ".yaml"}:
                continue
            text = file.read_text(encoding="utf-8")
            with self.subTest(file=file.relative_to(ROOT)):
                self.assertNotIn("/" + "Users/", text)
                self.assertNotIn("/private/" + "var/folders/", text)
                self.assertNotIn("C:\\" + "Users\\", text)
                self.assertIsNone(email_pattern.search(text))

    def test_pptx_extraction_keeps_only_source_basename(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            private_dir = Path(temp_dir) / "private-user-folder"
            private_dir.mkdir()
            source = private_dir / "example-lecture.pptx"
            with zipfile.ZipFile(source, "w") as archive:
                archive.writestr(
                    "ppt/slides/slide1.xml",
                    '<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
                    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                    "<a:t>Satellite link</a:t></p:sld>",
                )
            output = Path(temp_dir) / "pages.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "extract_courseware_pages.py"),
                    str(source),
                    "--output",
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertIn("Extracted 1 pages", result.stdout)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["source_file"], "example-lecture.pptx")
            self.assertEqual(payload["source_name"], "example-lecture.pptx")
            self.assertEqual(payload["pages"], [{"page": 1, "text": "Satellite link"}])
            self.assertNotIn(str(private_dir), output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
