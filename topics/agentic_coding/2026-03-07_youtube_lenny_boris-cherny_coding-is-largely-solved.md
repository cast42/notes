---
title: "Boris Cherny on ‘coding is largely solved’ — implications"
date: 2026-03-07
type: note
topics:
  - agentic_coding
tags:
  - youtube
  - x
  - boris_cherny
  - anthropic
  - claude_code
---

# Boris Cherny on ‘coding is largely solved’ — implications

## TL;DR
Boris’ claim is not “software is done,” but that **manual coding is becoming the bottleneck-free part** for many workflows. The scarce resource shifts to **problem framing, product taste, verification, and cross-functional execution**.

If this trend holds, teams optimize less for “who can type code fastest” and more for “who can define, steer, and validate high-leverage outcomes.”

## Key takeaways / implications
- **Role shift:** software engineer work moves toward builder/operator behavior (planning, orchestration, review, prioritization).
- **Generalists gain leverage:** PM/design/data/ops roles increasingly execute directly through agents.
- **Planning and verification become core skills:** plan mode, explicit acceptance criteria, and proof-before-done matter more than syntax fluency.
- **Org design impact:** underfunded/smaller teams + high token budgets can outperform larger teams with slower loops.
- **Education signal:** “learn to code” becomes “learn to build with code + models + tools,” with stronger emphasis on systems/product judgment.
- **Risk:** displacement and transition pain are real; the upside is broad software creation access if safety/governance keep pace.

## Notes from the interview
- Boris says he has not hand-edited code since November and ships many PRs/day via Claude Code.
- He frames coding as “largely solved” for his workflows; next frontier is idea generation + non-coding computer tasks.
- He expects role boundaries (engineer/PM/designer) to blur further, with everyone increasingly “building.”
- Recommended usage patterns: most-capable model, plan mode first, parallel agents, and minimal over-scaffolding.

## Added X post (URL + extracted text)
- URL: https://x.com/i/status/2030015356383691121
- Extraction note: direct fetch from X was blocked in this environment; text below was extracted from a local image capture (`boris-cherny-post.jpg`) via OCR.

### Extracted text (OCR, lightly cleaned)
## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: “Would a staff engineer approve this?”
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask “is there a more elegant way?”
- If a fix feels hacky: “Knowing everything I know now, implement the elegant solution”
- Skip this for simple, obvious fixes — don’t over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don’t ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management
1. Plan first: write plan to `tasks/todo.md` with checkable items
2. Verify plan: check in before starting implementation
3. Track progress: mark items complete as you go
4. Explain changes: high-level summary at each step
5. Document results: add review section to `tasks/todo.md`
6. Capture lessons: update `tasks/lessons.md` after corrections

## Core Principles
- Simplicity first: make every change as simple as possible, touching minimal code
- No laziness: find root causes, no temporary fixes, senior-engineer standards
- Minimal impact: only touch what’s necessary, avoid introducing bugs

## Sources
- YouTube: https://youtu.be/We7BZVKbCVw?is=7m_s6oA8Q5jBeNby
- X post: https://x.com/i/status/2030015356383691121
