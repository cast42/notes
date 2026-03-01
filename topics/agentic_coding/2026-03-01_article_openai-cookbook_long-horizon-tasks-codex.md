---
title: "Long horizon tasks with Codex (OpenAI Cookbook)"
date: 2026-03-01
type: note
topics:
  - agentic_coding
tags:
  - openai
  - codex
  - agents
  - long_horizon
---

# Long horizon tasks with Codex (OpenAI Cookbook)

## TL;DR
The core shift is from “single clever prompt” to a **long-running agent loop** with explicit guardrails. The OpenAI Cookbook example frames long-horizon coding as a reliability problem over time: keep the agent coherent, verify at milestones, repair failures, and preserve durable project memory.

## Key takeaways
- **Time horizon is the key capability axis** for agentic coding, not just one-shot intelligence.
- Long runs work better with a disciplined loop: **plan → implement → validate → repair → document → repeat**.
- Durable memory in repo docs (spec, plan, runbook, status) reduces drift and keeps “done” stable.
- Milestone-level validation (tests/lint/typecheck/build) is a practical reliability multiplier.
- Better outcomes come from steerability mid-flight, not from restarting with new prompts.

## Practical pattern from the Cookbook
Use a four-file operating stack for long tasks:
1. **Prompt/spec file** (goals, constraints, deliverables, done criteria)
2. **Plan file** (milestones, acceptance checks, stop-and-fix rule)
3. **Implementation runbook** (how to execute each loop)
4. **Live documentation/status log** (decisions, progress, known issues)

This externalized state lets humans step away and still resume control without losing context.

## Why this matters
This model of work turns coding agents into “delegatable teammates” instead of fragile assistants. Human leverage increases when supervision happens at checkpoints and architecture level rather than per-line micromanagement.

## Related benchmark framing (METR)
METR’s long-task research provides a useful external lens: evaluate agents by the **task length (human-time equivalent)** they can complete reliably. Their reported trend suggests rapidly increasing long-task capability over time, with strong implications for planning automation.

Reference:
- https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

## Sources
- OpenAI Cookbook: https://developers.openai.com/cookbook/examples/codex/long_horizon_tasks/
- METR: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
