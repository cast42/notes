---
title: "GEPA optimize_anything — ‘Let’s take it for a spin’ (SVG optimization demo)"
date: 2026-03-19
type: note
topics:
  - agentic_coding
tags:
  - optimization
  - llm
  - gepa
  - api
  - svg
source: "https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/#lets-take-it-for-a-spin"
---

## TL;DR
GEPA’s `optimize_anything` presents a declarative way to optimize *any text artifact* (code, prompts, configs, policies, agent architectures, SVGs) using an evaluator + feedback loop.

In the “Let’s take it for a spin” demo, they optimize raw SVG code for “a pelican riding a bicycle,” improving from a weak zero-shot image to a much better composition via iterative LLM reflection on visual feedback.

## Key takeaways
- Core abstraction: if something can be represented as text and scored, it can be optimized.
- API is deliberately minimal: provide a candidate/objective + evaluator; search/reflection is handled by the framework.
- Actionable Side Information (ASI) is central: evaluator returns not only score but diagnostics (text, structured fields, even images).
- One API supports three modes:
  - single-task search
  - multi-task search (cross-transfer across related tasks)
  - generalization (train/val setup for transfer to unseen examples)
- “Optimize artifact directly” is emphasized (e.g., SVG code), not only prompt tuning.

## Details (focus: “Let’s take it for a spin”)
- Task: generate high-quality SVG for “a pelican riding a bicycle.”
- Baseline: zero-shot attempt (Claude Opus 4.6).
- Optimization: explore multiple candidates (20 in the demo), evaluate rendered outputs with a vision model, and feed image + critique back as ASI.
- Outcome described: better anatomy, richer composition/background, and more refined visual elements.

### Why this matters
- Shows a practical path from “LLM suggests edits” to a measurable optimization loop.
- Makes artifact evolution less prompt-hack dependent and more evaluator-driven.
- Useful mental model for agentic coding: build strong evaluators/feedback channels first, then let search do the heavy lifting.

## Links
- Source article (anchor): https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/#lets-take-it-for-a-spin
- Main page title: “GEPA: optimize_anything: A Universal API for Optimizing any Text Parameter”
