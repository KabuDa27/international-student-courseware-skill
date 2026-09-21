# 留学生课件学习 Skill

**Courseware to Obsidian** is a Codex skill for international students who need to study English PDF/PPTX lecture slides in Chinese and maintain page-linked, tutor-style Obsidian notes. It emphasizes understanding diagrams, mechanisms, formulas, examples, and the limits of each claim rather than dumping a full-page translation.

将 PDF/PPTX 课件整理为可追溯到原页的 Obsidian 精读笔记。每个实质内容页都应像单独提问该页时一样得到讲解，而不是只保留一句摘要。

## What it does / 主要能力

- Reads the whole deck, maps every page, and groups closely related pages into small knowledge units.
- Produces a separate teaching card for each substantive page, with its screenshot and a concise source anchor.
- Explains what a page shows, why its conclusion follows, how to use it, and where the conclusion stops applying.
- Handles diagrams, comparisons, formulas, worked problems, examples, English terminology, agenda, and learning objectives according to page type.
- Maintains one course folder with a homepage, lecture notes, and stable screenshot assets.
- Keeps source statements, visual observations, added context, and inference distinguishable.

The skill instructions are in [SKILL.md](SKILL.md). The supporting note format and completion checks are in [references/](references/).

## Install / 安装

Clone this repository directly into a Codex skills directory:

```bash
git clone <YOUR_REPOSITORY_URL> ~/.codex/skills/courseware-to-obsidian
```

Then invoke `$courseware-to-obsidian` with a lecture PDF/PPTX and the destination course or Obsidian vault. If your Codex installation uses a different skills directory, clone the repository there instead.

## Requirements / 运行条件

- Python 3.10+ for the included extraction helpers.
- For PDF text extraction: `pdfinfo` and `pdftotext` from Poppler.
- For PPTX text extraction: Python standard library only. Convert legacy `.ppt` to `.pptx` or PDF first.
- A PDF/presentation rendering capability for inspecting diagrams and producing page screenshots; extracted text alone is not sufficient.
- An Obsidian vault if you want notes written directly to Obsidian. Otherwise the skill can stage its output elsewhere.

Full-page English–Chinese translation is **optional**, not the default note format. The optional local Argos workflow and its additional installation steps are documented in [references/argos-translation.md](references/argos-translation.md).

## Repository layout / 文件结构

```text
SKILL.md                       Main skill instructions
agents/openai.yaml             Codex UI metadata
references/quality-rubric.md   Per-page and whole-deck completion checks
references/obsidian-note-schema.md
references/argos-translation.md
scripts/                        Optional local extraction/translation helpers
```

## Privacy / 隐私

This repository contains **no lecture files, generated notes, vault contents, accounts, credentials, or personal paths**. Keep courseware and generated artifacts outside the repository; `.gitignore` excludes common private-source and temporary-output patterns. The extractor records a source filename, not an absolute local path, in generated JSON.

Before publishing a fork or examples, check every new file for names, email addresses, API keys, university IDs, local paths, and copyrighted lecture material. Only publish courseware or screenshots when you have the right to do so.

## License / 许可

No open-source license has been selected for this package. Choose and add a license before publicly releasing or inviting reuse of the repository.
