---
title: "Karpathy Guidelines: reduce common LLM coding mistakes"
date: 2026-02-03
type: note
topics:
  - agentic_coding
tags:
  - guidelines
  - llm
  - coding
  - refactoring
source:
  kind: github
  url: https://github.com/forrestchang/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md
---

## TL;DR

A short set of behavioral guardrails for LLM-assisted coding:
- **Think before coding** (surface assumptions + uncertainty)
- **Simplicity first** (minimum code, no speculative abstractions)
- **Surgical changes** (touch only what the request requires)
- **Goal-driven execution** (define success criteria, verify in a loop)

## Key points (as captured in the skill)

### 1) Think before coding
- Don’t assume; **state assumptions**.
- If multiple interpretations exist, present them.
- Push back if there’s a simpler approach.
- If unclear, stop and ask.

### 2) Simplicity first
- Write the **minimum** code that solves what was asked.
- Avoid speculative “flexibility”, premature abstractions, and unnecessary error handling.
- If the solution feels overcomplicated, simplify.

### 3) Surgical changes
- Don’t refactor or “improve” unrelated adjacent code.
- Match existing style.
- If you notice unrelated issues, mention them—don’t change them.
- Clean up only the unused imports/vars/functions **your change** caused.

### 4) Goal-driven execution
- Turn tasks into **verifiable goals** (usually tests + passing).
- For multi-step work: use a short plan with “step → verify” checkpoints.
- Strong success criteria enable independent iteration; weak criteria force constant back-and-forth.

## Source

This note is based on the skill file:
- https://github.com/forrestchang/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md

The skill cites Karpathy’s original thread:
- https://x.com/karpathy/status/2015883857489522876
