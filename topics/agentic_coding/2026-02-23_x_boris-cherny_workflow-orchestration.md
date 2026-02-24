---
title: "Boris Cherny — Workflow orchestration notes (image transcript)"
date: 2026-02-23
type: note
topics:
  - agentic_coding
tags:
  - x
  - claude_code
  - workflow
  - boris_cherny
---

# Boris Cherny — Workflow orchestration notes (image transcript)

## TL;DR
A compact playbook for agentic coding: always plan first, use subagents for parallelism, codify lessons after corrections, verify before declaring done, and optimize for elegant minimal-impact changes.

## Key takeaways
- Use plan mode for non-trivial work and re-plan early when things drift.
- Delegate aggressively to subagents to keep main context clean.
- Maintain a lessons loop (`tasks/lessons.md`) to reduce repeated mistakes.
- Never mark done without proof (tests/logs/diff + review standard).
- Favor simple, elegant fixes over hacky patches.

## Transcribed text from image (lightly cleaned)

### Workflow Orchestration

#### 1) Plan Mode Default
- Enter plan mode for any non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, stop and re-plan immediately; don’t keep pushing.
- Use plan mode for verification steps, not just building.
- Write detailed specs up front to reduce ambiguity.

#### 2) Subagent Strategy
- Use subagents liberally to keep the main context window clean.
- Offload research, exploration, and parallel analysis to subagents.
- For complex problems, throw more compute at it via subagents.
- One task/track per subagent for focused execution.

#### 3) Self-Improvement Loop
- After any correction from the user, update `tasks/lessons.md` with the pattern.
- Write rules for yourself that prevent the same mistake.
- Ruthlessly iterate on these lessons until mistake rate drops.
- Review lessons at session start for the relevant project.

#### 4) Verification Before Done
- Never mark a task complete without proving it works.
- Diff behavior between main and your changes when relevant.
- Ask yourself: “Would a staff engineer approve this?”
- Run tests, check logs, demonstrate correctness.

#### 5) Demand Elegance (Balanced)
- For non-trivial changes, pause and ask: “Is there a more elegant way?”
- If a fix feels hacky: “Knowing everything I know now, implement the elegant solution.”
- Skip this for simple, obvious fixes; don’t over-engineer.
- Challenge your own work before presenting it.

#### 6) Autonomous Bug Fixing
- When given a bug report: just fix it; don’t ask for hand-holding.
- Point at logs, errors, failing tests, then resolve them.
- Zero context switching required from the user.
- Go fix failing CI tests without being told how.

### Task Management
1. **Plan First**: Write plan to `tasks/todo.md` with checkable items.
2. **Verify Plan**: Check in before starting implementation.
3. **Track Progress**: Mark items complete as you go.
4. **Explain Changes**: High-level summary at each step.
5. **Document Results**: Add a review section to `tasks/todo.md`.
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections.

### Core Principles
- **Simplicity First**: Make every change as simple as possible; impact minimal code.
- **No Laziness**: Find root causes; no temporary fixes; senior-engineer standards.
- **Minimal Impact**: Touch only what’s necessary; avoid introducing bugs.

## Source
- Post URL: https://x.com/Eljaboom/status/2025905043447459983
- Author requested for note context: Boris Cherny
- Note: source post is by @Eljaboom and contains an image quoting Boris Cherny workflow guidance.
