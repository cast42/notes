---
title: "How AI agents shape experts’ judgment calls"
date: 2026-10-27
type: paper
topics:
  - agentic_coding
tags:
  - human-agency
  - expert-judgment
  - automation-bias
  - causal-inference
resource: "https://www.anthropic.com/research/agents-judgment-calls"
author:
  - "Amaç Herdağdelen"
  - "Hailey Joren"
  - "Alex Tamkin"
description: "A randomized study finds that experts often adopted an AI agent’s experimentally assigned lean on underdetermined analytical choices, even while later describing the resulting judgment as their own."
sources:
  - id: anthropic-research
    resource: "https://www.anthropic.com/research/agents-judgment-calls"
    title: "Anthropic research article"
  - id: paper
    resource: "https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf"
    title: "Who’s Aligned to Whom? How AI Agents Shape Experts’ Research Judgment Calls"
generated:
  by: "process:codex"
  at: "2026-10-29T07:41:20+01:00"
---

# How AI agents shape experts’ judgment calls

## TL;DR

Anthropic researchers randomized the direction of an AI coding agent’s stated preference while 50 causal-inference practitioners analyzed a realistic but fictional farming-cooperative case. Participants chose options aligned with the agent’s assigned lean on 86% of four underdetermined analytical decisions. The result suggests that an agent can quietly supply the assumptions behind expert work, even when the expert remains responsible for the final sign-off.

## Key takeaways

- **The consequential choices often sit upstream of the final answer.** Analysts had discretion over how to measure productivity, which comparison method to use, whose outcomes to estimate, and how to weight farms. Each choice could materially alter the estimated effect and therefore the recommendation.
- **Agent framing shifted those choices.** Each agent was secretly assigned a randomly chosen lean and instructed to make its strongest honest case for it. Participants followed that lean on 86% of analytical choices; their final rollout recommendation was less directly affected, but the prior analytical choices had already shaped the estimate.
- **Influence was not always recognized afterward.** Seventy-seven percent repeated at least one of their agent’s arguments in their explanations, sometimes closely, while only 15% credited the agent. Yet self-reported ownership and confidence were similar among those who followed the lean and those who did not.
- **A technically correct-looking result can still conceal a judgment transfer.** For underdetermined questions, there may be no single ground-truth answer to check. The output can be defensible while its assumptions and framing came largely from the agent.
- **Human review is not automatically independent oversight.** A person can approve an AI-assisted result without independently forming the judgments that shaped it.

## Study design and limits

The experiment included 50 analysts who chose to use the agent; 11 participants who worked without it were excluded from the main comparison. The task used synthetic data in a fictional agricultural-policy scenario, and the participants were causal-inference practitioners rather than farming-domain experts. The researchers deliberately strengthened and made the agent’s lean explicit to measure its effect. Thus, the study identifies a causal effect of assigned agent framing in this task, but the 86% agreement rate is not a forecast of how often experts will defer in ordinary work.

The authors note that the assigned lean may be stronger than agents’ default preferences, and real experts may have more domain knowledge or stronger prior views. They also report one model and one kind of task. Their results establish a risk worth measuring, not that AI assistance generally degrades decisions: the small, less experienced no-agent group is not a fair basis for concluding that AI users performed better.

## Practical implications

The study motivates safeguards, but does not experimentally establish that any one safeguard works. Plausible practices include recording the analyst’s initial view before the agent argues for an option; asking the agent to state the strongest case, assumptions, and evidence for each viable alternative; marking which decisions remain value-laden or underdetermined; and preserving a decision log that distinguishes a human judgment from an agent-suggested default. For high-stakes work, an independent reviewer should examine the assumptions rather than merely the final answer.

These practices connect to [testing competing hypotheses](../cognitive_patterns/test_competing_hypotheses.md): the goal is not artificial neutrality, but making live alternatives and their assumptions visible before settling on one.

## Related concepts

- [How the Claude Code team does code review](2026-10-15_article_anthropic_how-claude-code-team-does-code-review.md) — layered checks and risk-based human approval help catch defects, but do not by themselves ensure that a reviewer independently formed the underlying judgment.
- [Evaluating agents on highly subjective tasks](2026-10-21_article_cameron-wolfe_subjective-evals.md) — evaluation must account for ambiguity, human judgment, and limits of proxy scores.
- [Test competing hypotheses](../cognitive_patterns/test_competing_hypotheses.md) — a procedure for exposing and comparing plausible alternatives.

## Sources

- [Anthropic, “How AI agents shape experts’ judgment calls”](https://www.anthropic.com/research/agents-judgment-calls) [anthropic-research]
- [Herdağdelen, Joren, and Tamkin, “Who’s Aligned to Whom? How AI Agents Shape Experts’ Research Judgment Calls”](https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf) [paper]
