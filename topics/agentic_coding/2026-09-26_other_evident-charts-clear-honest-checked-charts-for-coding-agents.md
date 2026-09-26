---
type: "skill"
source_url: "https://github.com/rhiever/evident-charts"
canonical_url: "https://github.com/rhiever/evident-charts"
title: "evident-charts: clear, honest, checked charts for coding agents"
author: "Randy Olson"
handle: "rhiever"
created_at: "2026-09-26"
date: "2026-09-26"
topics: ["agentic_coding"]
tags:
  - data-visualization
  - chart-integrity
  - agent-skill
  - matplotlib
  - visual-review
resource: "https://github.com/rhiever/evident-charts"
description: "An agent skill that turns chart creation into an evidence-aware workflow with data checks, deterministic linting, and rendered-image review."
generated: {"by": "process:note-ingest", "at": "2026-09-26T17:08:42+00:00"}
verified: [{"by": "process:codex", "at": "2026-09-26T17:08:42+00:00"}]
sources:
  - id: repository
    resource: "https://github.com/rhiever/evident-charts"
  - id: skill-file
    resource: "https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/SKILL.md"
  - id: rule-sources
    resource: "https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/references/sources.md"
maturity: "experimental"
---

# evident-charts: clear, honest, checked charts for coding agents

*Randy Olson — @rhiever*

## TL;DR

- Treat charting as an agent workflow: analyze, state the takeaway, choose the form, build, check, review the PNG, and deliver with provenance.
- Combine data-integrity checks with deterministic linting and fresh-context image review.
- Separate evidence-backed integrity rules from practitioner consensus and taste, while leaving project style in control of non-integrity choices.

## Highlights

- The chart title should state what the data shows, not merely name the topic.
- A successful plotting script is not enough: inspect the rendered image and fix P0/P1 issues.
- The skill checks totals, duplicates, preliminary periods, axes, palettes, labels, clipping, contrast, and source attribution.

## Links

- Permalink: [https://github.com/rhiever/evident-charts](https://github.com/rhiever/evident-charts)
- [https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/SKILL.md](https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/SKILL.md)
- [https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/references/sources.md](https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/references/sources.md)

## Raw

- Raw text: [topics/agentic_coding/raw/2026-09-26_other_evident-charts-clear-honest-checked-charts-for-coding-agents.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-09-26_other_evident-charts-clear-honest-checked-charts-for-coding-agents.raw.md)
- Extractor: github-readme+skill-md+github-api

## My notes

The strongest idea is the separation of **data integrity**, **visual rendering
checks**, and **reader judgment**. An agent should not equate “the plotting
script ran” with “the chart communicates honestly.” The explicit takeaway and
fresh-image review are especially useful safeguards against charts that are
technically valid but misleading or unreadable.

The evidence tags are also a good boundary: integrity rules need stronger
justification than house style. The repository is new, however, so its claims
about effectiveness are maintainer claims rather than an independent
evaluation.

## Related concepts

- [Coding agents for data analysis](2026-03-16_article_simon-willison_coding-agents-for-data-analysis.md)
- [Open Knowledge Format as a portable standard for AI context](../knowledge_management/2026-06-13_article_open-knowledge-format-as-a-portable-standard-for-ai-context.md)
