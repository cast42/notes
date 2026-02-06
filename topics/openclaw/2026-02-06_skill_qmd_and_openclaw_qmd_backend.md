---
title: "QMD skill for OpenClaw (and when QMD became built-in)"
date: 2026-02-06
type: note
topics:
  - openclaw
tags:
  - qmd
  - skills
  - search
  - memory
source:
  kind: github
  url: https://github.com/levineam/qmd-skill
---

## TL;DR

- **qmd-skill** is an OpenClaw/Codex skill wrapper around **QMD** (Tobi’s local hybrid search tool for Markdown notes).
- OpenClaw added an **opt-in QMD backend for workspace memory** in **OpenClaw 2026.2.2**.

## Links

- Skill repo: https://github.com/levineam/qmd-skill
- Skill file (raw): https://raw.githubusercontent.com/levineam/qmd-skill/main/SKILL.md
- QMD (by Tobi): https://github.com/tobi/qmd
- X: Tobi noting “QMD based memory built right in” (OpenClaw 2026.2.2): https://x.com/tobi/status/2018881321313997151

## What the skill does

The skill’s intent is: “Local hybrid search for markdown notes and docs” using the `qmd` binary.

Key behavioral guidance from the skill:
- Prefer **`qmd search`** (BM25) by default (fast).
- Use **`qmd vsearch`** only when keyword search fails (can be slow on cold start).
- Avoid **`qmd query`** unless you explicitly want best-quality hybrid + rerank (often slow / can timeout).

It also includes setup snippets:
- `qmd collection add ... --mask "**/*.md"`
- `qmd context add ...` (optional)
- `qmd embed` (for semantic/hybrid)
- Maintenance: `qmd update`, `qmd embed`, `qmd status`

## When did OpenClaw get QMD “out of the box”?

OpenClaw **2026.2.2** release notes include:
- “Memory: implement the opt-in QMD backend for workspace memory.”

Source (release notes): https://github.com/openclaw/openclaw/releases

Note: the wording is **opt-in** — it’s built in, but not necessarily enabled by default for everyone.
