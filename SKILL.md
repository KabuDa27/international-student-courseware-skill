---
name: courseware-to-obsidian
description: Deeply interpret user-provided PPT, PPTX, or PDF courseware slide by slide, explain each substantive page like an expert tutor, extract examinable knowledge, and maintain evidence-linked course notes in Obsidian Markdown. Use for lecture-slide explanation, courseware study notes, revision notes, or importing teaching materials into an Obsidian vault; do not use merely to redesign or create a presentation.
---

# Courseware to Obsidian

Turn courseware into detailed, reviewable teaching notes whose explanations can always be traced to the source slides. The default product is **page-by-page teaching**, not page-by-page translation.

## Required inputs

Identify the source file, course name, and lecture/week when available. Before the first Obsidian write, resolve the vault path, canonical course folder, course homepage, and target week/lecture note. Never guess a vault path or silently overwrite a note. If the vault is unavailable, create a staging course folder beside the task output and report its path.

Accept `.pptx`, `.ppt`, and `.pdf`. Use the available presentation- or PDF-specific capability to inspect the file. Combine structural extraction with rendered-page inspection: text extraction alone is insufficient for diagrams, formulas, spatial relationships, annotations, and screenshots. Treat speaker notes as a distinct source when present.

## Evidence contract

Every substantive explanation must cite a slide or page number. Use these labels consistently:

- **课件原文** — an exact, short excerpt, formula, label, or data value. Preserve its language and notation; never put a paraphrase here.
- **图表读取** — a direct account of visible axes, legends, arrows, regions, tables, or relationships.
- **详细讲解** — the teaching layer grounded in cited evidence.
- **补充知识** — useful context not stated on the slide. Keep the boundary explicit.
- **推断** — an interpretation such as likely emphasis or exam relevance. State the reason and confidence; never present it as the teacher's claim.

Do not invent unreadable text, missing definitions, citations, or speaker intent. Mark uncertain content `待核对` and state what is unclear. Use the minimum quotation needed to anchor an explanation while preserving complete formulas, variable definitions, thresholds, and table values when correctness requires them.

## Agenda and learning-objective closure

Treat opening roadmap slides as teaching content. Detect close variants of `Agenda`, `Outline`, `Objectives`, `Learning Outcomes`, `Goals`, `本讲安排`, and `学习目标`.

- Near the beginning, add `Agenda / 本讲路线` and `Objectives / 学习目标回应` when present. Pair the slide screenshot with concise exact wording and citations.
- Turn every agenda item into a study question, explain why it appears, link it to the detailed section, and cite its coverage pages. Do not merely copy or translate bullets.
- For every objective, retain the concise English original, explain the expected capability in Chinese, give a substantive overview answer, link to the detailed section, and assign one honest status: `已覆盖`, `部分覆盖`, `仅预告`, or `待后续课程`.
- When no explicit roadmap exists, create only `本讲路线（推断）` and label its basis.
- End with `学习目标回收（Objective Check）`, revisiting each objective with a final answer, self-check question, status, and detailed-section link.

## Granularity

Write a teaching document, not a compressed executive summary.

- Default to knowledge units spanning **one to three content pages**. Allow four to six only for one incremental diagram build or an indivisible worked example. Administrative pages may be grouped more broadly.
- Give each distinct definition, mechanism, comparison, formula, algorithm, diagram, or worked example its own heading or clearly separated subsection.
- Build a fine-grained coverage map that states each page's contribution. Do not hide content under broad ranges such as `Pages 10–25: concepts`.
- Each substantive page receives its own `单页精讲卡`. Closely related cards are followed by a unit synthesis that connects them.
- Length is not a reason to omit explanation. Split a large result by lecture, part, or chapter instead of reducing teaching depth.

## Slide-by-slide teaching contract

Respond to every substantive page with the same reasoning quality used when a learner sends that page alone and asks “这页讲了什么?”. First reconstruct the page's intent, then teach it; do not merely translate, transcribe, or rephrase visible bullets.

For each substantive page, first make a private **page knowledge inventory** from both extracted text and the rendered page: list every distinct claim, definition, mechanism, formula, diagram relationship, condition, comparison, and example. Match every material inventory item to an explanation in that page's card. A page containing several ideas needs several explained subpoints or subheadings; do not compress it into one umbrella sentence. The screenshot and evidence anchor support the teaching but do not substitute for it.

Write the card as a self-contained tutor response. Its minimum teaching core is: **the page's question and conclusion; how to read any meaningful visual or notation; a step-by-step explanation of each material idea and why it follows; one page-specific concrete example or worked application; the key misconception or boundary; and a learner check that requires using the idea**. Include prerequisites, adjacent-page connections, and source-language cues where relevant. If a minimum-core element truly does not apply, say why in the page inventory or coverage map instead of silently dropping it. Do not manufacture examples for purely administrative pages.

Depth follows information density and difficulty, not a fixed word count. A multi-idea page may require several paragraphs, a diagram walkthrough, or separate subsections. If the explanation would be as short as a caption or executive-summary bullet, it is not a completed teaching card. Split long lectures into parts instead of shortening cards to fit a length or token target.

For each substantive page, cover the applicable parts below. Omit only genuinely irrelevant headings rather than generating filler.

1. **这页在讲什么** — state the page's real question and conclusion.
2. **怎么阅读这页** — identify reading order and the role of text, diagram, table, formula, color, axis, or annotation.
3. **详细讲解** — explain the mechanism step by step, including prerequisites and why the result follows.
4. **公式与推导** — when present, define symbols, state assumptions, derive or justify key steps, preserve notation, and interpret the result.
5. **具体例子** — give a numerical, physical, or everyday example that instantiates the exact concept. Label outside material `补充知识`.
6. **重点与易错点** — distinguish the key idea from common confusions and boundary conditions.
7. **与前后页的关系** — state what this page inherits and enables next.
8. **英文识别线索** — retain essential English terms, definitions, commands, and question cues.
9. **自测** — ask at least one application or explanation question, not heading recall.

### Route by page type

Choose the dominant page type and apply its required reasoning:

- **概念/定义页** — plain-language meaning, purpose, positive example, counterexample, and distinction from a nearby concept.
- **对比页** — comparison dimensions, both mechanisms on the same example, trade-offs, and visual oversimplifications.
- **图示/流程页** — axes, legends, arrows, regions, direction, reading order, relationships, and what cannot be concluded.
- **公式/定理页** — problem solved, symbols, assumptions, derivation, intuition, parameter sensitivity, miniature application, and common error.
- **例题/习题页** — `已知条件 → 求解目标 → 选择公式 → 逐步代入 → 中间结果 → 最终答案 → 实际解释`; include units and limitations where applicable.
- **表格/数据图页** — rows, columns, units, trends, anomalies, supported conclusions, and unsupported conclusions.
- **应用/案例页** — scenario, inputs, outputs, decision, assumptions, failure modes, and transfer to a second scenario.
- **Agenda/Objectives** — learning questions, coverage links, and closure checks.
- **标题/过渡/版权/纯行政页** — record briefly in the coverage map. Do not manufacture a full card unless it adds instructional meaning.

When a page combines types, apply every materially relevant rule without duplicating prose.

## Bilingual study policy

Chinese is the default teaching language for English courseware, while source-language vocabulary needed for lectures and examinations remains visible. **Do not produce complete page-by-page parallel translation unless the user explicitly requests it.**

- On first use in each independently readable unit, write core terms as `中文名称（English term, abbreviation）`.
- Preserve formulas, symbols, variable names, proper names, standards, labels, and source abbreviations exactly.
- Keep short exact source excerpts that anchor the explanation. Add `中文直译` only when a difficult or examinable sentence benefits from it.
- Use `中文理解` for interpretation; never disguise it as a quotation.
- Preserve command words such as `define`, `explain`, `compare`, `derive`, `calculate`, and `justify`, explaining the expected response when relevant.
- Add concise `英文识别线索` grounded in actual slide wording; do not invent exam wording.
- Maintain a consistent bilingual glossary using the English term as the stable key.

Full-page translation is an optional mode only. If explicitly requested, read [references/argos-translation.md](references/argos-translation.md) and treat local machine translation as an untrusted draft. It must not replace teaching cards, and translation completeness is not a default completion criterion.

## Screenshot evidence

Place a rendered screenshot beside each page's concise evidence anchor by default. Images preserve layout and diagrams; excerpts keep evidence searchable.

- Render the cited page itself. Use a full page unless one clearly labelled crop is additionally needed.
- Store assets under `<course-folder>/assets/<course-code>/<source-stem>-<fingerprint>/pNNN.png`; never embed temporary paths.
- Use a two-column Obsidian table headed `课件截图` and `课件证据`, with a normal text page label in the evidence cell.
- Every substantive page should have its own screenshot when pages contain distinct content. Near-duplicate builds may use one representative screenshot only if every page's distinct contribution is recorded.
- If rendering fails, retain text evidence, mark `待补充`, and report the missing page.

## Workflow

1. Inspect the entire deck. Record page count, structure, languages, speaker notes, extraction problems, explicit roadmap/objectives, and page types.
2. Build a page-complete coverage map. Use one-to-three-page units and record the contribution and type of every page.
3. Build one unit at a time: evidence → one `单页精讲卡` per substantive page → unit synthesis → revision support. Administrative pages receive concise coverage entries.
4. Teach each substantive page as though the learner had sent that slide alone and asked “这页讲什么？”. Use the following full **read → explain → apply → check** procedure. It is a teaching sequence, not a requirement to print identical headings on every page.

   - **Read and inventory the page before writing.** Inspect both extracted text and the rendered slide. Record every material concept, claim, relationship, arrow, formula, value, example, and condition. Identify the question the page answers. Do not infer its content solely from its title. Match every material inventory item to an explanation in the finished card; if the page contains several independent ideas, give each an explained subpoint or subsection rather than one umbrella sentence.
   - **Keep three knowledge layers distinct.** First state what the slide literally says or visibly depicts (`课件原文` / `图表读取`). Next explain what those observations mean and why the conclusion follows (`详细讲解`). Finally show how to use the idea and where it stops applying; mark context not on the slide as `补充知识` and interpretations as `推断`. Never present added teaching context as a claim made by the lecturer.
   - **Write in a natural tutor-response order.** Open with the page's central question and answer. Walk the learner through the visual or notation in reading order. Explain each knowledge point from prerequisite → mechanism → result, including the causal steps omitted by terse bullets. Work through one concrete example or application tied to this exact page. Clarify the key misconception, assumption, boundary, or unsupported conclusion. Connect the page to its neighbors and retain the English terms the learner needs to recognize. End with an explanation, comparison, calculation, or transfer question—not a request to repeat the heading. Combine headings when this reads naturally, but do not drop the underlying reasoning.
   - **Let information density determine depth.** Multiple concepts require separate explanations and their relationship; a process diagram requires an end-to-end walkthrough of modules and arrows; a comparison requires both approaches applied to the same scenario and their trade-offs; a formula requires symbols, assumptions, derivation or justification, substitution, and interpretation; a worked problem requires intermediate steps and units; an emphatic equation or claim requires its conditions and a case where it should not be generalized. A sparse page may be short if fully explained, while a dense page may need several paragraphs or subsections. Do not pad administrative pages or use a fixed word count, and do not shorten later pages to fit a length or token target—split the lecture note instead.
   - **Maintain full-deck consistency.** Complete and check one 1–3-page knowledge unit at a time, but keep a separate teaching card for each substantive page. After the cards, explain how those pages form one argument; the unit synthesis must not replace any page card. On a second pass, look especially for later cards that have collapsed into captions or one-sentence summaries.
   - **Apply a per-page completion gate.** Compare the card with its page inventory: every material item needs an explanation, not just a mention. Then perform the closed-slide test: reading only the note, could the learner describe the page, explain why its conclusion holds, and use it in a nearby example or changed scenario? Check that evidence, interpretation, and outside knowledge remain distinguishable. If any test fails, expand/rewrite the card or mark that page `待扩写` / `待核对`; do not count it as complete merely because its heading, screenshot, excerpt, or page number exists. Exempt purely administrative pages explicitly.
5. Work formulas and examples line by line. Keep source claims, direct visual reading, inference, and outside knowledge visibly separate.
6. Produce deck-level synthesis: agenda roadmap, objective responses and final check, concept dependencies, core argument, glossary, and revision checklist.
7. Validate coverage, attribution, **each page inventory against its teaching card**, visual interpretation, and Obsidian integrity using [references/quality-rubric.md](references/quality-rubric.md). A failed substantive card remains incomplete even when its screenshot and page number are present.
8. Merge into the canonical course folder using [references/obsidian-note-schema.md](references/obsidian-note-schema.md). Preserve manual notes and previous imports.

## Obsidian update rules

Use one canonical folder per course:

```text
<course-code> - <course-name>/
├── 00 - 课程主页.md
├── Week NN - Lecture NN - <lecture-title>.md
└── assets/<course-code>/<source-stem>-<fingerprint>/pNNN.png
```

The homepage is the navigation entry; page-level teaching belongs in lecture notes. Identify imports by filename plus fingerprint. Do not duplicate unchanged imports. Retain earlier import records when content changes.

Use ordinary Obsidian Markdown, YAML, `[[wikilinks]]`, callouts, headings, and stable anchors. Do not require community plugins. Preserve user-authored notes and properties. Keep assets stable across re-imports and verify embeds before reporting success.

When upgrading an older note, do not automatically delete existing `逐页中英对照` content. Preserve it until the user requests migration. During migration, retain screenshots and manual annotations, replace translation-heavy generated blocks with teaching cards page by page, and avoid duplicate explanations.

## Completion report

Report source and fingerprint, page coverage, substantive-page count versus completed teaching-card count, non-substantive exemptions, output note and asset paths/counts, agenda/objective closure, type-specific checks for formulas/diagrams/tables/examples, uncertainties, and sections updated.

Do not claim completion until every page is represented in the coverage map, every substantive page has passed the inventory-to-card and learner-comprehension checks, required evidence/assets exist, and the canonical note has been written successfully. Report substantive pages that remain insufficiently explained as incomplete, not as completed coverage.
