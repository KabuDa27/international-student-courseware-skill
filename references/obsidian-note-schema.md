# Obsidian course-note schema

Use this schema for the canonical course folder. Adapt labels to the course language while preserving page evidence and teaching-card structure.

## Canonical location

```text
<vault>/<course-root>/<course-code> - <course-name>/
├── 00 - 课程主页.md
├── Week 01 - Lecture 01 - <lecture-title>.md
└── assets/<course-code>/<source-stem>-<fingerprint>/p014.png
```

Use one folder per course and one note per teaching week/lecture. Reuse a corresponding course folder and preserve user content.

## Course homepage

`00 - 课程主页.md` is the stable navigation entry. Keep it concise: metadata, completion state, lecture index, and cross-week concept links.

```markdown
---
type: course-index
course: "<course name>"
course_code: "<course code>"
term: "<term>"
tags: [course, course-index]
updated: YYYY-MM-DD
---

# <Course code> · <Course name>

## 课程进度

- 已导入：2 / 12 周

## 周次与课件

| 周次 | 课次 | 主题 | 状态 | 笔记 |
|---|---|---|---|---|
| Week 01 | Lecture 01 | Introduction | 已完成 | [[Week 01 - Lecture 01 - Introduction]] |
```

Preserve user-added sections. Update only affected rows, progress, and concept links.

## Lecture-note properties

```yaml
---
type: lecture-notes
course: "<course name>"
course_code: "<course code>"
term: "<term>"
week: 1
lecture: 1
teachers: []
tags: [course, lecture-notes]
updated: YYYY-MM-DD
---
```

Preserve user-defined properties.

## Lecture-note structure

```markdown
# <Course code> · Week 01 · <Lecture title>

> [[00 - 课程主页|返回课程主页]]

## 本讲知识地图

- [[#Concept A]] → [[#Concept B]]

## 课件导入记录

| 文件 | 课次 | 版本/指纹 | 页数 | 导入时间 | 状态 |
|---|---|---|---:|---|---|
| `<source filename>` | Week 01 | `<fingerprint>` | 36 | YYYY-MM-DD HH:mm | complete |

> [!info] 来源
> 文件：`<source filename>`<br>
> 覆盖：Slides 1–36<br>
> 版本：`<fingerprint>`
```

## Agenda / 本讲路线

| Agenda item（原文） | 中文理解 | 本讲要解决的问题 | 精读位置 | 来源 |
|---|---|---|---|---|
| `<short exact item>` | <interpretation> | <study question> | [[#<heading>]] | Slide 2; Slides 6–9 |

If no agenda exists, use `本讲路线（推断）` and state the inference basis.

## Objectives / 学习目标回应

| Objective 原文 | 中文理解 | 本讲如何回答 | 详细位置 | 状态 / 来源 |
|---|---|---|---|---|
| `<short exact objective>` | <expected capability> | <substantive overview> | [[#<heading>]] | 已覆盖 · Slide 3; Slides 10–14 |

Only use `已覆盖`, `部分覆盖`, `仅预告`, or `待后续课程`.

## 逐页覆盖地图

| 页面 | 页面类型 | 本页贡献 | 精讲位置 | 状态 |
|---|---|---|---|---|
| Slide 1 | 标题/行政 | 课程与章节信息 | [[#Slides 1–2]] | 简要记录 |
| Slide 2 | Agenda | 建立本讲路线 | [[#Slides 1–2]] | 已精讲 |
| Slides 3–4 | 定义 + 对比 | Slide 3 定义 A；Slide 4 比较 A 与 B | [[#Slides 3–4]] | 已精讲 |

Every page must appear. State individual contributions even when pages share a unit.

## Slides 3–4 · <small knowledge unit>

Place evidence first, then one card for each substantive page, then a unit synthesis.

| 课件截图 | 课件证据 |
|---|---|
| ![[assets/<course-code>/<source-stem>-<fingerprint>/p003.png\|480]] | **Slide 3**<br>“<minimum exact excerpt, formula, label, or values>” |

### Slide 3 · <page title>

> [!note] 本页知识点
> <list each distinct material claim, mechanism, formula, visual relationship, condition, comparison, or example found on this page; use this list to ensure none is merely named and left unexplained>

#### 这页在讲什么

<state the page's question, purpose, and conclusion>

#### 怎么阅读这页

<explain reading order and the role of its elements; omit when unnecessary>

> [!abstract] 图表读取
> <direct visual observations only; cite Slide 3>

#### 详细讲解

<teach every material point in the inventory, step by step in Chinese, explaining prerequisites, causal links, and why the conclusion follows; split a dense page into subheadings instead of collapsing it into one paragraph; retain essential English terms>

#### 公式与推导

<symbols, assumptions, derivation, substitutions, units, and interpretation; include only when applicable>

> [!example] 具体例子
> <instantiate this page's exact concept or mechanism with a concrete application or calculation; label outside knowledge clearly>

> [!warning] 重点与易错点
> - **重点：** ...
> - **易错点：** ...
> - **边界条件：** ...

#### 与前后页的关系

<what this page inherits and enables>

#### 英文识别线索

- `<short source-grounded phrase or term>` → <how to recognize or answer it>

#### 自测

1. <application or explanation question that cannot be answered by repeating the page heading>

### Slide 4 · <page title>

<repeat only applicable teaching-card fields>

### 单元串联

<connect the pages into one argument, method, or problem-solving sequence>

Do not force empty headings, but do not silently omit the substantive teaching core. A definition page may need a counterexample; a formula page needs assumptions and derivation; a diagram page needs axes and visual relations; a worked example needs the full calculation path. Before marking the card complete, compare it with `本页知识点` and apply the closed-slide test: the learner should be able to explain and use the page without reopening the screenshot. If the page has several ideas, expand them into separate explained subpoints; if an element is genuinely inapplicable, state why in the card or coverage map.

For a title, divider, copyright, or purely administrative page, use a concise record instead of a full card:

```markdown
### Slide 1 · 标题页

- **页面作用：** 标识课程、章节和版本。
- **关键证据：** “<title>”（Slide 1）
```

## 本讲总结

Summarize the conceptual chain, not the order of headings.

## 学习目标回收（Objective Check）

| Objective | 学完后的回答 | 自检问题 | 状态 / 回看 |
|---|---|---|---|
| `<original wording>` | <final answer> | <understanding check> | 已覆盖 · [[#<heading>]] |

## 双语术语表

| English term | 中文对应 | Abbreviation | Recognition cue | 中文理解 | 来源 |
|---|---|---|---|---|---|
| Sampling | 采样 | — | Digitizing x-y coordinate values | 将连续空间坐标离散化 | Slide 8 |

## 考试指令词

| Command word | 作答要求 | 课件实例/来源 |
|---|---|---|
| Explain | 说明原理、步骤及因果关系 | Slide 12 |

## 待核对

- Slide 14: <uncertainty and reason>

## Merge behavior

- Locate imports by filename and fingerprint; do not duplicate unchanged imports.
- For changed content under the same filename, add a new import row and concise `版本变化` subsection.
- Preserve manual text and user-defined YAML.
- Keep screenshots in fingerprinted asset directories and verify every embed.
- Update the homepage lecture row, progress, and relevant concept links.
- Verify that every page occurs in the coverage map and every substantive page has one primary teaching card.
- Preserve older translation-heavy content until migration is requested. During migration, convert page by page and avoid duplicate teaching blocks.

## Screenshot pairing

Use the two-column table above. Escape the pipe in sized Obsidian embeds as `\|`. Keep a normal text page label and a minimal exact excerpt in the evidence cell. Do not rely on text inside the image as the only evidence.

Translation is optional. For English courseware taught in Chinese, keep core terms bilingual and add a short `中文直译` only for difficult or examinable source sentences. Never insert a full-page translation dump by default.
