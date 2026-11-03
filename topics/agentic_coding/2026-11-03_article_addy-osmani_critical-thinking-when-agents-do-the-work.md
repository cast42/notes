---
title: "Critical thinking when agents do the work"
date: 2026-11-03
type: article
topics:
  - agentic_coding
tags:
  - critical-thinking
  - cognitive-offloading
  - verification
  - human-agency
  - agent-workflows
resource: "https://x.com/i/article/2116367635365695488"
author: "Addy Osmani"
description: "Osmani argues that agentic workflows make it easy to drift from delegation with ownership into unexamined deferral, and offers habits for preserving understanding, verification, and accountability."
sources:
  - id: article
    resource: "https://x.com/i/article/2116367635365695488"
    title: "Critical thinking when agents do the work"
    author: "Addy Osmani"
  - id: announcement
    resource: "https://x.com/addyosmani/status/2117512471930167377"
    title: "Addy Osmani's post linking the article"
generated:
  by: "process:codex"
  at: "2026-11-03T08:22:15+01:00"
---

# Critical thinking when agents do the work

## TL;DR

Addy Osmani argues that agentic tools can make work faster while quietly moving the human from **offloading with ownership**, through **deferral**, to **cognitive surrender**—accepting outputs without understanding or checking them. His answer is not to avoid agents, but to make independent thinking, verification, and accountability deliberate parts of the workflow.

## The central distinction

Osmani describes three modes:

- **Cognitive offloading:** delegate work, but retain ownership of the result.
- **Deferral:** treat the agent's output as the next input rather than as a hypothesis to evaluate.
- **Cognitive surrender:** absorb the output as one's own without feeling a need to check or explain it.

The transition can be gradual. Because agent outputs are increasingly polished and often correct, the absence of obvious errors is a weak reason to stop looking. Parallel agents increase production, but they do not increase the human's review capacity; Osmani calls the resulting gap between generated work and work one can stand behind the “orchestration tax.”

## Practices for keeping judgment engaged

- **Form an initial hypothesis or brief before asking.** It can be wrong; writing it down makes later changes of mind attributable to evidence rather than to the agent's framing.
- **Choose whether the task is for learning or delegation.** Both are legitimate. Make the choice intentionally, especially when abandoning practice would erode a skill you still need.
- **Ask what would make the answer wrong, then test it.** Prefer observable checks over the model's self-reported confidence. For open questions, examine a serious counterargument, potentially from an independent source or model.
- **Define verification before work begins.** A green test establishes only what that test checks. Ask what it proves and what it misses; for code or other consequential deliverables, use tangible evidence such as test output, a trace, screenshot, or source sample.
- **Inspect decisions, not only the summary.** Ask the agent to list assumptions, scope choices, defaults, and trade-offs. Read a few artifacts directly and make sure you can explain what matters.
- **Scale review to stakes and capacity.** Delegate freely where mistakes are cheap and reversible. Slow down, add stronger checks, or reduce agent throughput when work piles up faster than it can be reviewed.
- **Keep the human-owned questions human-owned.** What should be built, why it matters, who it affects, and what trade-offs are acceptable are not settled by technical verification. The agent can help explore them; accountability remains with the person or organization.

## Reading stance and limits

This is a practitioner essay and set of recommendations, not a controlled test of the full checklist. It combines Osmani's experience with concepts and research he cites, including cognitive surrender and supervision risks. Its strongest practical point is a distinction between **delegating execution** and **delegating judgment**. The exact amount of manual review needed depends on the task: codebases and other complex systems need not be held in a person's full memory if understanding can be rebuilt locally, but the person must know when they lack that understanding and be able to retrieve and verify it.

## Related concepts

- [How AI agents shape experts' judgment calls](2026-10-27_paper_anthropic_agents-shape-expert-judgment.md) — experimental evidence that an agent's framing can influence upstream expert choices, even when the human signs off.
- [How the Claude Code team does code review](2026-10-15_article_anthropic_how-claude-code-team-does-code-review.md) — layered verification and risk-scaled human review in one production engineering team.
- [How to Avoid AI Brain Rot — Miles Cranmer](../ai_adoption/2026-10-16_video_miles-cranmer_avoid-ai-brain-rot.md) — preserve the practice needed to understand and evaluate AI-generated work.
- [How to stay smart in the age of AI: the science of critical thinking](../ai_adoption/2026-09-23_article_how-to-stay-smart-in-the-age-of-ai-the-science-of-critical-thinking.md) — distinguishes assisted performance from durable learning and unaided transfer.
- [Critical Thinking: Why Is It So Hard to Teach?](../learning/2008-03-01_article_daniel-willingham_critical-thinking-hard-to-teach.md) — why general prompts need relevant domain knowledge and practice to support reasoning.

## Sources

- [Addy Osmani, “Critical thinking when agents do the work”](https://x.com/i/article/2116367635365695488) [article]
- [X post linking the article](https://x.com/addyosmani/status/2117512471930167377) [announcement]
