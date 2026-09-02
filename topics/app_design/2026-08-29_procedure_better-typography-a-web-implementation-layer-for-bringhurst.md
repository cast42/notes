---
title: "Better Typography — a web implementation layer for Bringhurst"
date: 2026-08-29
timestamp: 2026-08-29
type: procedure
topics:
  - app_design
tags:
  - typography
  - web-design
  - css
  - design-systems
  - accessibility
resource: "https://ui-skills.com/skills/jakubkrehel/better-typography"
description: "A practical web-typography review procedure that operationalizes many of Bringhurst's principles while leaving editorial judgment, page composition, and typographic history to the deeper reference."
source_url: "https://www.ui-skills.com/skills/jakubkrehel/better-typography"
canonical_url: "https://ui-skills.com/skills/jakubkrehel/better-typography"
author: Jakub Krehel
handle: jakubkrehel
created_at: 2026-08-29
---

# Better Typography — a web implementation layer for Bringhurst

*Jakub Krehel — @jakubkrehel*

## TL;DR

- A practical web-typography review skill covering type systems, spacing, font technology, wrapping, overflow, accessibility, and verification.
- It operationalizes many Bringhurst principles—restraint, measure, hierarchy, spacing, genuine font forms—but does not replace his reader-first judgment or historical depth.
- Best used as an implementation checklist under Bringhurst’s governing question: does the typography clarify and honor the content?

## Key takeaways

- Use a small semantic type scale and descending visual hierarchy.
- Cap long-form measure at roughly 60–75 characters and tune line-height by role.
- Prefer real font forms and CSS properties over synthesized faces or raw OpenType axis tags.
- Inspect rendered pages at realistic lengths; wrapping and truncation failures are not visible from code alone.

## Comparison with Bringhurst

The closest book in these notes is Robert Bringhurst's [*The Elements of Typographic Style*](../designing_things_people_love/1992-01-01_book_robert-bringhurst_the-elements-of-typographic-style.md). They fit together as two layers: Bringhurst supplies the governing philosophy and trained judgment; `better-typography` turns part of that craft into repeatable checks for web interfaces.

| Area | `better-typography` | Bringhurst | Assessment |
| --- | --- | --- | --- |
| Purpose | Make text render, wrap, and behave well in products | Interpret the text and serve the reader | Strong alignment, but the skill starts after content and structure are mostly decided |
| Restraint and hierarchy | Few fonts, sizes, and weights; semantic scale; descending headings | Consistent, distinct, harmonious levels derived from the text's inner logic | The skill makes Bringhurst operational for design systems, but a scale cannot decide which distinctions the content needs |
| Measure | Roughly 60–75 characters for long-form text | Common book measure of roughly 60–66 characters, adjusted with leading and page shape | Compatible ranges, not a universal constant; Bringhurst treats measure, face, size, and leading as one system |
| Leading | Role-based defaults: about 1.1 for headings and 1.5–1.6 for body | Leading follows measure, typeface, size, language, and desired page color | Useful web defaults, but less contextual than the book |
| Letterforms and features | Load real styles; use optical sizing, small caps, and numeric variants correctly | Respect genuine italics, small caps, figures, ligatures, kerning, and the character of the face | Direct translation from typographic craft to browser capabilities |
| Spacing and rhythm | Type scales, letter-spacing guidance, wrapping controls, nonbreaking spaces | Proportional rhythm across letters, words, lines, paragraphs, and the page | The skill covers local rendering well; the book offers the stronger model of the whole composition |
| Widows, orphans, wrapping | CSS `pretty` and `balance`, plus realistic browser testing | Detailed editorial handling and more precise widow/orphan terminology | CSS helps but does not replace inspection or copy/layout judgment |
| Accessibility and interaction | Mobile input sizes, recoverable truncation, language/direction, selectable text | Reader-first legibility and respect for language, primarily in print | The skill productively extends the book into responsive, interactive, bidirectional contexts |
| Verification | Severity levels, computed-style checks, viewport resizing, explicit unverified items | Case-by-case craft judgment informed by history and close reading | The review protocol is the skill's clearest contribution beyond the book |

## What the skill adds

- Current browser mechanics: WOFF2, variable fonts, OpenType CSS properties, font synthesis, and font smoothing.
- Responsive failure modes: overflow, line clamping, mobile input zoom, changing numeric values, and realistic-content testing.
- International and accessible implementation: `lang`, `dir`, `<bdi>`, selection behavior, and recoverable truncation.
- A concrete audit format with severity, locations, before/after values, verification, and a block/approve decision.

## What Bringhurst still adds

- A first principle: read and understand the text before assigning it typographic form.
- A relational model in which measure, leading, face, size, spacing, page shape, and typographic color are tuned together.
- Editorial and historical judgment: why conventions exist, when exceptions are warranted, and how type participates in a cultural tradition.
- Attention to the whole page and long-form reading, beyond individual components and CSS declarations.

## Practical synthesis

Use Bringhurst to decide what the typography should communicate, then use `better-typography` to inspect whether the web implementation actually delivers it. Treat the skill's numeric floors and ranges as review defaults, not proofs of quality. A page can pass every checklist item and still fail if its hierarchy misreads the content or its typography calls more attention to itself than to the text.

## Sources

- Permalink: [https://ui-skills.com/skills/jakubkrehel/better-typography](https://ui-skills.com/skills/jakubkrehel/better-typography)
- [https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/SKILL.md](https://github.com/jakubkrehel/skills/blob/main/skills/better-typography/SKILL.md)
- [https://github.com/jakubkrehel/skills/tree/main/skills/better-typography](https://github.com/jakubkrehel/skills/tree/main/skills/better-typography)

## Raw

- [Raw skill files](raw/2026-08-29_procedure_better-typography-a-web-implementation-layer-for-bringhurst.raw.md)
- Extractor: ui-skills-page+raw-github
