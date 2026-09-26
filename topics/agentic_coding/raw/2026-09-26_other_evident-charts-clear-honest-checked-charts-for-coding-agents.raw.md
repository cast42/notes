---
type: "source_capture"
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
description: "Source capture of the evident-charts repository, its skill workflow, and its evidence-tagged chart rules."
generated: {"by": "process:note-ingest", "at": "2026-09-26T17:08:42+00:00"}
sources:
  - id: repository
    resource: "https://github.com/rhiever/evident-charts"
  - id: skill-file
    resource: "https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/SKILL.md"
  - id: rule-sources
    resource: "https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/references/sources.md"
content_hash: "fce86c287bce18f57f32f95f8d9eaea712750c2199c2cd07dd9e9cb548732ffd"
extracted_at: "2026-09-26T17:08:42+00:00"
extractor: "github-readme+skill-md+github-api"
---

# Source capture

## Repository metadata

- Repository: https://github.com/rhiever/evident-charts
- Maintainer: Randy Olson (`rhiever`)
- License: MIT
- Repository description: “Teaches AI coding agents to make clear, honest charts, and checks each one before you see it.”
- Repository created: 2026-09-25
- Latest repository activity checked: 2026-09-26
- Skill version in `skills/evident-charts/SKILL.md`: 0.1.0
- Supported agent surfaces named by the repository: Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, and other Agent Skills-compatible agents.

## README capture

The repository asks users to request charts normally, for example a chart from a CSV, a slide about a budget, or a critique of an existing PNG and script. The skill is intended to load when an agent creates, revises, restyles, or reviews a chart, plot, graph, or figure.

Its stated checks include:

- checking the data for mixed totals and parts, duplicate rows, placeholder codes, and preliminary periods;
- choosing a chart form from the takeaway and data shape;
- writing the takeaway as the title and naming the real publisher as the source;
- linting rendered charts for overlaps, clipping, baselines, dual axes, color-blind confusability, and contrast;
- reviewing the rendered image with a fresh reviewer that sees only the PNG, then fixing problems for up to three rounds.

The repository supports matplotlib, seaborn, pandas `.plot`, ggplot2, Plotly, Vega-Lite, Altair, and D3. It provides presets for blog, mobile, social, social portrait, slide, and report destinations.

## SKILL.md capture

The skill's workflow is:

1. Analyze the data, print summary statistics, confirm units and scope, and run integrity checks.
2. Write a one-line brief: `Takeaway | Audience | Destination`.
3. Choose the chart form from the takeaway and the data shape; consult the decision references when the form is ambiguous.
4. Build in the project's stack, or use Python/matplotlib and the included helper when no stack is specified.
5. Run deterministic checks, including the chart checker for matplotlib or the palette checker for other stacks.
6. Reopen and review the rendered PNG rather than judging only the code. Use a fresh-context reviewer when available; fix P0/P1 problems for at most three rounds.
7. Deliver the image and script together with the brief, analysis choices, source identification, confidence, unconfirmed details, alt text, rule exceptions, and a short review log.

The rules separate three kinds of guidance:

- `[E]` experimental evidence: integrity rules should only be broken with a stated reason;
- `[P]` practitioner consensus: break only for a clear reason;
- `[T]` taste or convention: bend freely when the project's style requires it.

Examples of the default rules are: bars start at zero; avoid dual axes, 3D, inverted value axes, and rainbow colormaps; use direct labels where practical; show units; use one accent when one element is the story; and make the title state what the data shows rather than merely naming the topic.

## Interpretation

The durable contribution is a procedural quality gate for agent-generated charts. It combines data-integrity checks, an explicit takeaway, deterministic code checks, and image-level review. It treats a successful script run as insufficient evidence that a chart is clear or honest.

The repository's rule evidence and implementation are maintainer-provided. The repository itself is new and small; its claims about chart quality, supported libraries, and review workflow should not be read as an independent benchmark of the skill's effectiveness.

## Primary sources

- Repository and README: https://github.com/rhiever/evident-charts
- Skill instructions: https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/SKILL.md
- Rule citations: https://raw.githubusercontent.com/rhiever/evident-charts/main/skills/evident-charts/references/sources.md
