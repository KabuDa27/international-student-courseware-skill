#!/usr/bin/env python3
"""Extract page-preserving text from PDF or PPTX courseware into JSON."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


DRAWING_NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def run_checked(command: list[str]) -> str:
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"Required command is not installed: {command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "unknown error").strip()
        raise RuntimeError(f"Command failed ({command[0]}): {detail}") from exc
    return result.stdout


def normalize_text(text: str) -> str:
    lines = [re.sub(r"[ \t]+$", "", line) for line in text.replace("\r\n", "\n").split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def extract_pdf(path: Path) -> list[dict[str, object]]:
    info = run_checked(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)\s*$", info, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("Could not determine PDF page count with pdfinfo")
    page_count = int(match.group(1))
    pages: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="courseware-extract-") as temp_dir:
        temp_root = Path(temp_dir)
        for page_number in range(1, page_count + 1):
            output_path = temp_root / f"p{page_number:04d}.txt"
            run_checked(
                [
                    "pdftotext",
                    "-f",
                    str(page_number),
                    "-l",
                    str(page_number),
                    "-layout",
                    "-nopgbrk",
                    str(path),
                    str(output_path),
                ]
            )
            text = normalize_text(output_path.read_text(encoding="utf-8", errors="replace"))
            pages.append({"page": page_number, "text": text})
    return pages


def slide_sort_key(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else sys.maxsize


def extract_pptx(path: Path) -> list[dict[str, object]]:
    pages: list[dict[str, object]] = []
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile as exc:
        raise RuntimeError("The PPTX file is not a valid Office archive") from exc
    with archive:
        slide_names = sorted(
            (
                name
                for name in archive.namelist()
                if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
            ),
            key=slide_sort_key,
        )
        for page_number, name in enumerate(slide_names, start=1):
            root = ET.fromstring(archive.read(name))
            text_runs = [node.text or "" for node in root.findall(".//a:t", DRAWING_NS)]
            pages.append({"page": page_number, "text": normalize_text("\n".join(text_runs))})
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract each PDF page or PPTX slide into a stable JSON record."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.is_file():
        parser.error(f"source file does not exist: {source}")

    suffix = source.suffix.lower()
    if suffix == ".pdf":
        pages = extract_pdf(source)
        engine = "pdftotext-layout"
    elif suffix == ".pptx":
        pages = extract_pptx(source)
        engine = "pptx-xml"
    elif suffix == ".ppt":
        parser.error("legacy .ppt must be converted to .pptx or PDF before extraction")
    else:
        parser.error("supported source formats are PDF and PPTX")

    payload = {
        "schema_version": 1,
        "source_file": source.name,
        "source_name": source.name,
        "extraction_engine": engine,
        "page_count": len(pages),
        "pages": pages,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    nonempty = sum(bool(str(page["text"]).strip()) for page in pages)
    print(f"Extracted {len(pages)} pages ({nonempty} with text) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
