# Argos offline translation pipeline

Use this reference for the token-efficient English-Chinese translation layer when the learner prefers a completely local, no-quota workflow.

## Runtime

Argos Translate is open-source and runs locally. Install the runtime and the English-to-Chinese model once:

```bash
uv tool install argostranslate
argospm update
argospm install translate-en_zh
```

The language-model download is the only required network step. Subsequent translation must run offline and requires no account, API key, cloud endpoint, or billing configuration. The bundled adapter locates the `uv tool` Python runtime automatically; `ARGOS_PYTHON` may override it when needed.

Official project: <https://github.com/argosopentech/argos-translate>

## Workflow

Extract pages while retaining source page numbers:

```bash
python3 scripts/extract_courseware_pages.py lecture.pdf \
  --output .work/lecture-pages.json
```

Verify the local model and planned workload:

```bash
python3 scripts/argos_translate_pages.py .work/lecture-pages.json \
  --output .work/lecture-translated.json \
  --dry-run
```

Translate and render the deterministic bilingual layer:

```bash
python3 scripts/argos_translate_pages.py .work/lecture-pages.json \
  --output .work/lecture-translated.json \
  --markdown-output .work/lecture-bilingual.md
```

The adapter keeps blank lines and common bullet prefixes, preserves numeric/formula-only lines, caches each page by source text, language pair, and Argos version, and records pages that need selective review.

For direct note insertion, put exactly one marker for each page inside its matching one-to-three-page unit:

```markdown
<!-- BILINGUAL_PAGE:1 -->

> [!tip] 本页拓展知识（非课件原文）
> ...
```

Then inject without routing the complete translation through Codex:

```bash
python3 scripts/inject_bilingual_blocks.py note-skeleton.md \
  .work/lecture-translated.json \
  --output final-note.md
```

The injector rejects missing, duplicate, and unknown markers. Codex writes the teaching explanations and page extensions; the script inserts the full bilingual blocks.

## Known quality boundary

Argos is suitable as a first-pass translation of headings, bullets, definitions, and ordinary prose. It is less reliable on:

- multi-column diagrams and flow labels extracted without spatial relationships;
- formulas mixed with prose, mathematical variables, and coordinate notation;
- long sentences broken across PDF extraction lines;
- specialized terminology, acronyms, standards, names, and ambiguous short labels;
- OCR noise or text whose reading order is unclear.

The adapter adds `review_reasons` such as `multi-column-or-diagram-layout`, `formula-or-symbol-heavy`, `mostly-numeric`, and `line-structure-changed`. Review every flagged page and a small sample from the beginning, middle, and end. Compare against the rendered slide, not only extracted text.

Do not ask Codex to rewrite all machine translations. Correct only confirmed errors and record the review. For diagrams, use the screenshot plus `图表读取` to restore relationships that plain text cannot represent. For core terms, prefer the course glossary consistently even when Argos chooses a plausible general-language synonym.

## Extraction boundary

`extract_courseware_pages.py` uses `pdftotext -layout` for PDF and Office XML for PPTX. Convert legacy `.ppt` to PPTX or PDF first. MarkItDown may be used as a secondary whole-document extraction check when already installed, but its flattened output is not the sole evidence source for numbered pages.

Extraction and translation never replace rendered-slide inspection. Empty, incomplete, or suspicious page records remain `待核对` until checked visually.
