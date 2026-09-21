# Courseware analysis quality rubric

Run this check before writing the final note.

## 1. Coverage and granularity

- Every page appears in the coverage map with its type, contribution, location, and status.
- Content units normally span one to three pages; longer units are reserved for a single build sequence or indivisible example.
- Different concepts, formulas, comparisons, algorithms, diagrams, and examples are not collapsed into one generic section.
- Every substantive page has exactly one primary `单页精讲卡`.
- Title, divider, bibliography, and administrative pages are recorded but not padded with filler.
- Hidden pages and speaker notes are identified when exposed by the source.

## 2. Page teaching quality

For every substantive page, compare its knowledge inventory with the finished card. Each material definition, claim, mechanism, formula, visual relationship, condition, comparison, and example must be taught or explicitly marked unreadable/uncertain. A card that names all the topics but explains none of their causal links fails. Several ideas on one page require several explained subpoints, not one summary sentence.

Confirm the applicable questions are answered:

- What question is this page answering, and what is its conclusion?
- How should the learner read the page?
- Why does the mechanism or result follow?
- What prerequisite, assumption, or operating condition applies?
- What concrete example makes it understandable?
- What misconception or boundary condition matters?
- How does it connect to adjacent pages?
- Which English terms or source phrases must the learner recognize?
- Can the learner answer a transfer or explanation question afterward?

The minimum core is a clear question/conclusion, visual or notation reading when relevant, step-by-step causal explanation of all material ideas, a page-specific example/application, a key misconception or boundary, and an application-level learner check. Record why a core element is genuinely inapplicable; do not silently omit it. The card must teach rather than translate, transcribe, paraphrase bullets, or state only conclusions. Omit inapplicable headings; do not use formulaic filler or a fixed word-count proxy.

Run the **closed-slide test**: after reading only the card, could a learner explain what the page shows, why its conclusion holds, and use the idea in a nearby example? If not, expand or rewrite it. A screenshot plus a short caption or one broad paragraph cannot pass merely because the page is counted.

## 3. Page-type routing

- **Definition:** plain-language meaning, purpose, example, counterexample, and distinction from a nearby concept.
- **Comparison:** shared comparison dimensions, both mechanisms on the same example, trade-offs, and visual simplifications.
- **Diagram/process:** axes, legends, arrows, colors, regions, direction, reading order, relationships, and limits of inference.
- **Formula/theorem:** problem solved, symbols, assumptions, derivation, intuition, parameter sensitivity, application, and common error.
- **Worked example/problem:** known values, target, formula, substitutions, units, intermediate steps, answer, interpretation, and limitations.
- **Table/data chart:** rows, columns, units, trends, anomalies, supported conclusions, and unsupported conclusions.
- **Application/case:** scenario, inputs, outputs, decision, assumptions, failure modes, and transfer to another scenario.
- **Agenda/objectives:** study questions, coverage links, statuses, and closure checks.

If a page mixes types, all materially relevant checks apply.

## 4. Attribution

- Every source-grounded claim has a page citation; outside context is labelled `补充知识`.
- `课件原文` contains only exact source material.
- `图表读取` stays with visible relationships and does not smuggle in interpretation.
- Inferences are labelled and justified.
- Formulas preserve operators, subscripts, superscripts, units, and variable meanings.
- Data retain their row, column, axis, or chart context.
- Unreadable content is marked `待核对`, never guessed.

## 5. Visual interpretation and screenshots

- Rendered pages were inspected when layout or imagery carries meaning.
- Every substantive page has its own screenshot, or a representative build-sequence screenshot is explicitly justified.
- Screenshot embeds resolve inside the vault and use stable fingerprinted paths.
- Page identity matches neighboring evidence.
- Axes, legends, arrows, color encodings, table headings, and diagram direction are explained.
- Decorative elements are not treated as evidence.
- Failed renders are marked `待补充` and reported.

## 6. Formula and example depth

- Variable meanings, assumptions, units, and notation are explicit.
- Derivations show the key reasoning rather than jumping to the result.
- Numerical examples show substitutions and intermediate results.
- Final answers are interpreted in the course context.
- Limitations, edge cases, or decision-boundary implications are stated when relevant.
- Reasoning is not shortened merely to control document length.

## 7. Bilingual exam readiness

When source and learner languages differ:

- Core terms retain their source-language form and a consistent learner-language equivalent.
- The first occurrence in each independent unit uses `中文（English, abbreviation）`.
- Exact excerpts remain separate from `中文直译` and `中文理解`.
- Only difficult, defining, or examinable source sentences are translated by default; there is no compulsory full-page parallel translation.
- English recognition cues are grounded in actual slide wording, definitions, formulas, contrasts, or commands.
- Relevant command words are preserved and their response expectations are explained.
- The glossary includes source term, translation, abbreviation, recognition cue, explanation, and citation.

If the user explicitly requested full translation, validate that optional deliverable separately; it does not replace teaching-card quality.

## 8. Agenda and objective closure

- Explicit agenda and objectives are identified with exact wording, screenshots, and citations.
- Every agenda item becomes a useful study route and links to the detailed note.
- Every objective has a Chinese interpretation, overview answer, detailed link, evidence pages, and honest status.
- Inferred roadmaps are labelled as inference.
- The closing `Objective Check` agrees with opening statuses and actual coverage.

## 9. Study value

- Unit synthesis explains how neighboring pages form one conceptual or problem-solving chain.
- Key points and misconceptions are specific and traceable.
- Examples clarify the exact page rather than drifting into an unrelated tutorial.
- Review questions test explanation, calculation, comparison, or transfer—not heading recall.
- The deck-level summary reflects the entire deck.
- Exam relevance is labelled `推断` unless explicitly stated by the source.

## 10. Obsidian integrity

- YAML, headings, anchors, and wikilinks are valid.
- The course has one canonical folder, a homepage, and separate lecture notes.
- Existing user notes and properties are preserved.
- Source filename, fingerprint, page count, and import time are recorded.
- The homepage index and completion state match imported notes.
- The output note and every referenced screenshot exist.

## Completion gate

Do not mark an import complete unless:

1. page coverage equals source page count;
2. teaching-card count equals substantive-page count;
3. every substantive card passes inventory-to-card coverage and the closed-slide test, and every diagram, formula, table, and worked example passes its type-specific checks;
4. agenda/objective closure is honest;
5. screenshots and note paths resolve;
6. all uncertainties and non-substantive exemptions are documented.
