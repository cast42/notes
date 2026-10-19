---
title: "/hypothesis-grid: a competing-explanations skill for AI product managers"
date: 2026-10-16
type: skill
topics:
  - agentic_coding
tags:
  - product-management
  - hypothesis-testing
  - confirmation-bias
  - analytical-workflows
resource: "https://x.com/i/article/2111214907563954176"
description: "George Nurijanian's /hypothesis-grid packages Analysis of Competing Hypotheses as an AI workflow to help product managers challenge the first plausible diagnosis before directing agents to build a fix."
author: "George Nurijanian"
handle: "nurijanian"
generated:
  by: "process:codex"
  at: "2026-10-19T17:21:00+02:00"
sources:
  - id: "announcement-post"
    resource: "https://x.com/nurijanian/status/2111225382187991447"
  - id: "article"
    resource: "https://x.com/i/article/2111214907563954176"
  - id: "heuer-psychology-of-intelligence-analysis"
    resource: "https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf"
  - id: "public-skill-collection"
    resource: "https://github.com/gnurio/nurijanian-skills"
---

# /hypothesis-grid: a competing-explanations skill for AI product managers

## TL;DR

- George Nurijanian describes `/hypothesis-grid` as an AI skill that applies Richards Heuer's Analysis of Competing Hypotheses (ACH) to product-management diagnosis.
- The core move is to resist anchoring on the first plausible explanation: generate reasonable alternatives, compare them against the evidence together, and look for evidence that weakens each one before choosing what to investigate or build.
- This is especially useful when an AI agent can quickly turn a PM's diagnosis into a specification and implementation. Faster execution makes choosing the right problem more important, not less.
- The announcement describes the skill, but the full `/hypothesis-grid` implementation was not available in the public skill repository I inspected. The details below summarize the announced method rather than review the implementation.

## What the skill is for

The post uses a familiar product failure—activation falls or a launch underperforms—to show how a team can settle too quickly on the first story. Once that explanation becomes the shared narrative, doubts sound obstructive and new charts get interpreted to support it. With an agent able to draft a spec and build a fix, a mistaken diagnosis can be operationalized faster.

The announced `/hypothesis-grid` skill packages Heuer's ACH for Claude Code and Codex. In outline:

1. Write down the plausible explanations before committing to one.
2. Examine each item of evidence against all candidate explanations, rather than evaluating only the current favorite.
3. Pay special attention to evidence that contradicts a hypothesis or distinguishes it from the alternatives.
4. Keep the explanation that survives the evidence best, then choose a useful next test or action.

The article's shorthand—prefer the hypothesis with the least evidence against it over the one with the most evidence for it—captures ACH's anti-confirmation-bias intent. It should not be read as a complete replacement for Heuer's procedure: the CIA chapter describes an eight-step process involving hypothesis generation, evidence assessment, diagnosticity, assumptions, collection, sensitivity, and reporting. A grid structures judgment; it does not mechanically establish which explanation is true.

## Practical use

For a weak launch, a PM might compare explanations such as poor audience fit, confusing onboarding, a technical failure, or a measurement change. Before asking an agent to implement a fix, ask what observation would differ across those explanations and which evidence would count against the leading story. Then gather that evidence or run a focused test.

The PM still owns the framing: the skill can help compare explanations, but it cannot guarantee that the hypothesis set is complete, that the evidence is reliable, or that the chosen test is diagnostic. For a more general procedure, see [Test competing hypotheses](../cognitive_patterns/test_competing_hypotheses.md), which emphasizes separating observations from interpretations, defining falsifiers, checking evidence quality, and avoiding invented alternatives.

## Availability and evidence boundary

The article says the skill is part of AI PM OS 3.0 and runs in Claude Code and Codex. The linked public `nurijanian-skills` repository offers a separate collection of PM skills, but its current file tree did not contain `/hypothesis-grid`; therefore I could not inspect the actual prompt or test it. Treat the product's descriptions of the skill as the author's claims, not independent evidence that it improves PM decisions.

## Related concepts

- [Test competing hypotheses](../cognitive_patterns/test_competing_hypotheses.md) — a reusable local reasoning procedure with explicit failure modes and evaluation criteria.
- [pstack: Lauren Tan's engineering skills for coding agents](2026-10-05_github_cursor_pstack_skills_by_lauren-tan.md) — another example of encoding engineering workflows as agent skills.

## Sources

- [Nurijanian's announcement](https://x.com/nurijanian/status/2111225382187991447)
- [The article describing `/hypothesis-grid`](https://x.com/i/article/2111214907563954176)
- Richards J. Heuer Jr., [*Psychology of Intelligence Analysis*, Chapter 8: Analysis of Competing Hypotheses](https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf)
- [Public `nurijanian-skills` repository](https://github.com/gnurio/nurijanian-skills)

Raw capture: [announcement and article summary](raw/2026-10-16_skill_nurijanian_hypothesis-grid.raw.md).
