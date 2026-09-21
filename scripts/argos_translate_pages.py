#!/usr/bin/env python3
"""Translate page-preserving courseware JSON locally with Argos Translate."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any


def ensure_argos_runtime() -> None:
    try:
        import argostranslate.translate  # noqa: F401
        return
    except ImportError:
        pass

    candidates: list[Path] = []
    configured = os.getenv("ARGOS_PYTHON")
    if configured:
        candidates.append(Path(configured).expanduser())
    executable = shutil.which("argos-translate")
    if executable:
        candidates.append(Path(executable).resolve().parent / "python")
    candidates.append(Path.home() / ".local/share/uv/tools/argostranslate/bin/python")

    current = Path(sys.executable).resolve()
    for candidate in candidates:
        if candidate.is_file() and candidate.resolve() != current:
            environment = dict(os.environ)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            os.execve(
                str(candidate),
                [str(candidate), str(Path(__file__).resolve()), *sys.argv[1:]],
                environment,
            )
    raise RuntimeError(
        "Argos Translate is not installed. Install it with `uv tool install argostranslate`, "
        "then install the en→zh model with `argospm install translate-en_zh`."
    )


try:
    ensure_argos_runtime()
except RuntimeError as exc:
    print(f"error: {exc}", file=sys.stderr)
    raise SystemExit(2)
import argostranslate.translate  # type: ignore  # noqa: E402
from bilingual_blocks import render_markdown  # noqa: E402


class TranslationError(RuntimeError):
    pass


def load_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TranslationError(f"Cannot read input JSON: {exc}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("pages"), list):
        raise TranslationError("Input must be an object containing a pages array")
    seen: set[int] = set()
    for item in payload["pages"]:
        if not isinstance(item, dict) or not isinstance(item.get("page"), int):
            raise TranslationError("Every page must be an object with an integer page field")
        if item["page"] in seen:
            raise TranslationError(f"Duplicate page number: {item['page']}")
        seen.add(item["page"])
        if not isinstance(item.get("text", ""), str):
            raise TranslationError(f"Page {item['page']} text must be a string")
    return payload


def cache_key(engine_version: str, source: str, target: str, text: str) -> str:
    raw = json.dumps(
        ["argos", engine_version, source, target, text],
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def read_cache(cache_dir: Path, key: str) -> str | None:
    path = cache_dir / f"{key}.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    translation = data.get("translation") if isinstance(data, dict) else None
    return translation if isinstance(translation, str) else None


def write_cache(cache_dir: Path, key: str, translation: str) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / f"{key}.json").write_text(
        json.dumps({"translation": translation}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def should_preserve(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith(("http://", "https://", "www.")):
        return True
    letters = len(re.findall(r"[A-Za-z]", stripped))
    return letters == 0


def translate_page(translator: Any, text: str) -> str:
    translated_lines: list[str] = []
    for line in text.splitlines():
        if should_preserve(line):
            translated_lines.append(line)
            continue
        match = re.match(r"^(\s*(?:(?:[-*•▪◦])|(?:\d+[.)]))?\s*)(.*)$", line)
        prefix, content = match.groups() if match else ("", line)
        if not content.strip():
            translated_lines.append(line)
            continue
        translated_lines.append(prefix + translator.translate(content).strip())
    return "\n".join(translated_lines).strip()


def review_reasons(source: str, translation: str) -> list[str]:
    reasons: list[str] = []
    nonempty = [line for line in source.splitlines() if line.strip()]
    if any(re.search(r"\S\s{6,}\S", line) for line in nonempty):
        reasons.append("multi-column-or-diagram-layout")
    if re.search(r"[𝑓𝑥𝑦∑∫√≈≤≥]|\b[A-Za-z]\s*[=<>]\s*", source):
        reasons.append("formula-or-symbol-heavy")
    visible = [char for char in source if not char.isspace()]
    if visible and sum(char.isdigit() for char in visible) / len(visible) > 0.35:
        reasons.append("mostly-numeric")
    if len(source.splitlines()) != len(translation.splitlines()):
        reasons.append("line-structure-changed")
    return reasons


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Translate page JSON locally with Argos and render bilingual Markdown."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--source", default="en")
    parser.add_argument("--target", default="zh")
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--max-source-chars", type=int, default=0)
    parser.add_argument(
        "--pages",
        help="Optional comma-separated page numbers for a review sample, for example 13,79,105",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--mock", action="store_true", help="Test only: do not load a model")
    args = parser.parse_args()

    payload = load_payload(args.input)
    if args.pages:
        try:
            selected = {int(value.strip()) for value in args.pages.split(",") if value.strip()}
        except ValueError as exc:
            raise TranslationError("--pages must contain comma-separated integers") from exc
        available = {page["page"] for page in payload["pages"]}
        unknown = sorted(selected - available)
        if unknown:
            raise TranslationError(f"Requested pages are not present: {unknown}")
        payload = dict(payload)
        payload["pages"] = [page for page in payload["pages"] if page["page"] in selected]
        payload["page_count"] = len(payload["pages"])
        payload["sampled_from_page_count"] = len(available)
    source_chars = sum(len(page.get("text", "")) for page in payload["pages"])
    translatable_pages = sum(bool(page.get("text", "").strip()) for page in payload["pages"])
    if args.max_source_chars > 0 and source_chars > args.max_source_chars:
        raise TranslationError(
            f"Source contains {source_chars} characters, exceeding the per-run cap "
            f"of {args.max_source_chars}."
        )

    try:
        engine_version = importlib.metadata.version("argostranslate")
    except importlib.metadata.PackageNotFoundError:
        engine_version = "unknown"
    cache_dir = args.cache_dir or args.output.parent / ".translation-cache/argos"
    keys = [
        cache_key(engine_version, args.source, args.target, page.get("text", "").strip())
        for page in payload["pages"]
        if page.get("text", "").strip()
    ]
    cached_pages = sum(read_cache(cache_dir, key) is not None for key in keys)
    likely_review = [
        {"page": page["page"], "reasons": review_reasons(page.get("text", ""), page.get("text", ""))}
        for page in payload["pages"]
        if review_reasons(page.get("text", ""), page.get("text", ""))
    ]

    if args.dry_run:
        requested_model_installed = (
            argostranslate.translate.get_translation_from_codes(args.source, args.target) is not None
        )
        print(
            json.dumps(
                {
                    "pages": len(payload["pages"]),
                    "translatable_pages": translatable_pages,
                    "source_characters": source_chars,
                    "cached_pages": cached_pages,
                    "pages_to_translate": translatable_pages - cached_pages,
                    "likely_review_page_count": len(likely_review),
                    "likely_review_pages": likely_review,
                    "engine": "argos-translate",
                    "engine_version": engine_version,
                    "requested_pair": f"{args.source}->{args.target}",
                    "requested_model_installed": requested_model_installed,
                    "network_required": False,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    translator = None
    if not args.mock:
        translator = argostranslate.translate.get_translation_from_codes(args.source, args.target)
        if translator is None:
            raise TranslationError(
                f"Argos model {args.source}->{args.target} is not installed. "
                f"Install it with `argospm install translate_{args.source}_{args.target}`."
            )

    output_pages: list[dict[str, Any]] = []
    for index, page in enumerate(payload["pages"], start=1):
        text = page.get("text", "").strip()
        output_page = dict(page)
        if not text:
            output_page.update({"translation": "", "translation_status": "no-text"})
            output_pages.append(output_page)
            continue
        key = cache_key(engine_version, args.source, args.target, text)
        cached = read_cache(cache_dir, key)
        if cached is not None:
            translation, status = cached, "cached"
        elif args.mock:
            translation, status = f"[模拟译文 Slide {page['page']}]\n{text}", "mock"
        else:
            translation, status = translate_page(translator, text), "translated"
            write_cache(cache_dir, key, translation)
        output_page.update(
            {
                "translation": translation,
                "translation_status": status,
                "translation_cache_key": key,
                "review_reasons": review_reasons(text, translation),
            }
        )
        output_pages.append(output_page)
        print(f"[{index}/{len(payload['pages'])}] Slide {page['page']}: {status}", file=sys.stderr)

    result = dict(payload)
    result["pages"] = output_pages
    result["translation"] = {
        "provider": "local-argos-translate",
        "engine_version": engine_version,
        "source": args.source,
        "target": args.target,
        "source_characters": source_chars,
        "network_required": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(render_markdown(result), encoding="utf-8")
    print(f"Translated {translatable_pages} pages locally to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (TranslationError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
