#!/usr/bin/env python3
"""Inject machine-generated bilingual page blocks into a lecture-note skeleton."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from bilingual_blocks import render_page_markdown


MARKER = re.compile(r"<!--\s*BILINGUAL_PAGE:(\d+)\s*-->")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replace BILINGUAL_PAGE markers without sending translation text through a model."
    )
    parser.add_argument("note_template", type=Path)
    parser.add_argument("translated_json", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    args = parser.parse_args()

    template = args.note_template.read_text(encoding="utf-8")
    payload = json.loads(args.translated_json.read_text(encoding="utf-8"))
    pages = payload.get("pages") if isinstance(payload, dict) else None
    if not isinstance(pages, list):
        parser.error("translated JSON must contain a pages array")

    page_map: dict[int, dict[str, Any]] = {}
    for page in pages:
        if not isinstance(page, dict) or not isinstance(page.get("page"), int):
            parser.error("every translated page must have an integer page number")
        number = page["page"]
        if number in page_map:
            parser.error(f"duplicate translated page: {number}")
        if "translation" not in page:
            parser.error(f"page {number} has no translation field")
        page_map[number] = page

    marker_numbers = [int(value) for value in MARKER.findall(template)]
    duplicates = sorted(number for number in set(marker_numbers) if marker_numbers.count(number) > 1)
    if duplicates:
        parser.error(f"duplicate markers in note template: {duplicates}")
    missing_markers = sorted(set(page_map) - set(marker_numbers))
    unknown_markers = sorted(set(marker_numbers) - set(page_map))
    if missing_markers or unknown_markers:
        parser.error(
            f"marker mismatch; missing markers={missing_markers}, unknown markers={unknown_markers}"
        )

    def replace(match: re.Match[str]) -> str:
        number = int(match.group(1))
        return render_page_markdown(page_map[number]).rstrip()

    rendered = MARKER.sub(replace, template)
    if MARKER.search(rendered):
        parser.error("unresolved bilingual markers remain after injection")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"Injected {len(page_map)} bilingual page blocks into {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
