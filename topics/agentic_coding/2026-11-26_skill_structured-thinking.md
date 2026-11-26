---
title: "Structured Thinking: ten reasoning workflows"
date: 2026-11-26
type: skill
topics:
  - agentic_coding
tags:
  - agent-skills
  - structured-reasoning
  - decision-making
  - critical-thinking
resource: "https://share.gemini.google/BBU7gscNlxK7"
description: "A ten-mode reasoning skill turns general-purpose AI prompts into structured procedures with epistemic safeguards and explicit output slots."
sources:
  - resource: "https://share.gemini.google/BBU7gscNlxK7"
---

# Structured Thinking: ten reasoning workflows

## TL;DR

This skill turns the [ten Luna Tech prompts](2026-11-26_tweet_luna-tech_ten-thinking-prompts.md) into a mode-routed procedure for analysis, planning and synthesis. Instead of asking an agent to play an expert persona or invent a fixed number of criticisms, it specifies reasoning steps, output slots and epistemic safeguards.

Lode supplied the skill file and described it as an improved version developed with Gemini 4 Neo. The shared Gemini page could not be inspected; this note is based on the attached file, not a verified account of how it was generated. “Improved” is the intended design, not an independently tested outcome.

## Modes

1. **Disambiguate:** ask up to three consequential questions when missing context changes the answer; otherwise proceed.
2. **Stress-test:** state the thesis, falsification conditions, material risks, strongest alternative and cheapest useful test.
3. **Backcast:** define a target state, trace prerequisites backward, identify the bottleneck and name the next action.
4. **Contrast:** compare a novice default with practitioner heuristics and edge cases, without claiming an expert persona.
5. **Decide:** compare options against priorities, risks, reversibility and opportunity costs; state what would change the recommendation.
6. **Discover:** describe a concrete friction, current workaround, beneficiary and buyer, and a key assumption for each opportunity.
7. **Learn:** diagnose gaps, design practice with feedback, schedule retrieval and check transfer with an artifact or explanation.
8. **Systemize:** specify trigger, steps, checkpoints and recovery for a repeatable workflow.
9. **Distill:** extract core claims, assumptions, applications and material to ignore.
10. **Strategize:** identify the current constraint, up to three leverage moves, explicit trade-offs and a leading indicator.

## Guardrails and judgment

Across modes, the file asks the agent to distinguish facts from assumptions, avoid role-play and fabricated criticism quotas, and keep the output structured. It allows combining at most two modes. In practice, fixed schemas and numeric limits are aids rather than evidence of quality: adapt the depth to the task, verify substantive claims, and avoid turning every simple request into a framework exercise. The learning schedule is an example, not a universally validated timetable.

## Source and artifact

- [Shared Gemini conversation](https://share.gemini.google/BBU7gscNlxK7) — inaccessible to the note's author at capture time.
- [Attached skill file, preserved verbatim](raw/2026-11-26_structured-thinking-skill.raw.md) — reference copy, not installed as an agent skill.
