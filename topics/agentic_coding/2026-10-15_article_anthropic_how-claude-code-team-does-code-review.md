---
title: "How the Claude Code team does code review"
date: 2026-10-15
type: article
topics:
  - agentic_coding
tags:
  - ai-code-review
  - risk-based-approval
  - software-quality
  - human-oversight
resource: "https://claude.dev/blog/solving-code-review-at-anthropic/"
author:
  - "Addy Osmani"
  - "Morgan Westlee Lunt"
  - "Qing Wang"
description: "Anthropic’s Claude Code team describes a layered review system that automates routine checks, scales human approval to risk, and uses reversibility and incident data to protect quality as change volume rises."
sources:
  - id: anthropic-article
    resource: "https://claude.dev/blog/solving-code-review-at-anthropic/"
    title: "How the Claude Code team does code review"
  - id: addy-post
    resource: "https://x.com/addyosmani/status/2114604912520921136"
    title: "Addy Osmani’s X post sharing the article"
generated:
  by: "process:codex"
  at: "2026-10-27T07:25:08+01:00"
---

# How the Claude Code team does code review

## TL;DR

Anthropic’s Claude Code team says merged PRs more than doubled between June and September while the share later reverted fell by over 40%. Their reported approach is not “remove review”: it shifts routine reading and checking to automated layers, routes human attention according to risk, and treats rollback and incident rates as quality guardrails. These are results from one team’s own account, not a universal benchmark.

## Key takeaways

- **Review the risk, not the ritual.** Replace “did a person read every line?” with “what could fail here, and which automated or human check is suited to catch it?”
- **Move feedback earlier.** Before a PR, agents run available tests/builds or compare screenshots, then a fresh-context reviewer inspects the diff. Automated review runs on each PR before human review.
- **Use independent layers.** The described pipeline includes AI bug review, a separate security review, blocking CI, human approval scaled by risk, a merge queue, staged releases, monitoring, and rollback. Each layer catches different failures; no single reviewer is treated as sufficient.
- **Make approval risk-based and accountable.** Low-risk changes may need no additional human approval for trusted authors after checks pass; medium-risk changes need one person; high-risk or designated sensitive paths need two. The person directing an agent remains accountable, and an agent’s approval does not substitute for required human approval.
- **Tune review against outcomes.** The team turns incidents and reverts into a recurring evaluation set, measures false-positive burden as well as findings, and caps review rounds to prevent agent-review cycles from continuing without convergence.
- **Separate defect detection from shared understanding.** The team says it has no formal mechanism ensuring everyone learns the codebase through review. Instead, people ask Claude for focused explainers or visual artifacts when they need to understand a slice. This is convenient, but is not the same as review automatically building shared context.

## What may transfer

The transferable design principle is to optimize the whole change system, not simply maximize review volume: make changes small and reversible, spend deeper human attention where failure is costly, require evidence that checks actually ran, and feed escaped failures back into tests or reviewer instructions. Start with one repository and tune the process before widening it.

The reported throughput and revert improvements are Anthropic’s own measurements over a particular period and codebase. Other teams should establish their baseline and watch both human time and quality outcomes; reducing approvals alone can simply move costs into incidents and rework. The article itself also notes that context-sharing remains largely on-demand rather than formally solved.

## Related concepts

- [pstack: Lauren Tan's engineering skills for coding agents](2026-10-05_github_cursor_pstack_skills_by_lauren-tan.md) — a related verification-oriented workflow for delegating implementation while retaining review and evidence.
- [How a harness connects a model to tools](2026-10-23_article_what-is-a-harness.md) — useful for separating the coding-agent runtime from the surrounding review and delivery system.

## Sources

- [Anthropic, “How the Claude Code team does code review” (15 October 2026)](https://claude.dev/blog/solving-code-review-at-anthropic/) [anthropic-article]
- [Addy Osmani’s X post](https://x.com/addyosmani/status/2114604912520921136) [addy-post]
