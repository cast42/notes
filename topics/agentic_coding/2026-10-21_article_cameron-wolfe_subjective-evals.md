---
title: "Evaluating agents on highly subjective tasks"
date: 2026-10-21
type: article
topics:
  - agentic_coding
tags:
  - agent-evaluation
  - subjective-evaluation
  - llm-as-a-judge
  - uncertainty
  - benchmark-design
resource: "https://cameronrwolfe.substack.com/p/subjective-evals"
description: "Cameron R. Wolfe outlines a human-calibrated, statistical, and production-grounded process for evaluating agents when task quality is subjective and outcomes are noisy."
author: "Cameron R. Wolfe"
generated:
  by: "process:codex"
  at: "2026-10-22T08:05:00+02:00"
sources:
  - id: "announcement-post"
    resource: "https://x.com/cwolferesearch/status/2112915508148232571"
  - id: "article"
    resource: "https://cameronrwolfe.substack.com/p/subjective-evals"
---

# Evaluating agents on highly subjective tasks

## TL;DR

- Treat human judgments as the quality reference, but make them more consistent with clear criteria, examples, expert input, and repeated calibration.
- Use LLM judges and task-specific rubrics to scale offline testing only after checking them against a human-rated “golden” set. An automated judge is a proxy, not ground truth.
- Report uncertainty, not just a benchmark score: plan sample size with power analysis, use confidence intervals, and repeat agent or judge runs to estimate run-to-run noise.
- Build evaluations from diverse, realistic, sufficiently difficult, discriminative, and audited tasks. A hard task that every model fails may still be uninformative.
- Advance promising candidates from offline evaluation to human review and then production A/B tests. Production signals and failure cases should feed back into future eval sets.

## The proposed evaluation loop

Wolfe’s roadmap has three linked layers:

1. **Human evaluation defines quality.** Work with subject-matter experts to specify a small set of meaningful criteria, scoring instructions, and examples. Have multiple raters score some of the same outputs; measure agreement, investigate disagreement, revise the guidance, and keep monitoring for drift. If a criterion remains impossible to score consistently, narrow or remove it rather than pretending its score is reliable.
2. **Offline evaluation enables iteration.** Use calibrated LLM judges or criterion-by-criterion rubrics to compare many candidate agents cheaply. Check judge agreement against human-labeled examples and relevant user outcomes. Use power analysis to plan evaluation size, confidence intervals to express uncertainty, and repeated runs to estimate non-determinism in agents and judges. Where appropriate, compare candidates on the same tasks and analyze paired differences.
3. **Production monitoring checks real use.** Track implicit signals such as abandonment and explicit feedback such as ratings. Test promising candidates with A/B experiments before full rollout. Add newly observed use cases and failure modes back into human and offline evaluations.

The intended progression is offline screening → human evaluation → production A/B test → broader rollout, with monitoring continuing after deployment.

## Designing useful task sets

The article recommends checking evaluation tasks for:

- **Diversity and coverage:** organize expected uses into a taxonomy so gaps and domain-specific performance are visible.
- **Realism:** source tasks from actual use where possible, rather than relying only on convenient synthetic examples.
- **Difficulty:** avoid tasks so easy that systems saturate; inspect failures to distinguish genuine model limits from bad task specifications or graders.
- **Discriminative value:** prefer tasks that distinguish capability levels. A task that all candidates fail can be difficult but not useful for ranking them.
- **Accuracy:** audit task statements and grading rules, using automated checks for scale and human review for ambiguous or consequential cases.

## Interpretation and limits

A higher score alone does not establish a real capability gain. The result can reflect task sampling, agent randomness, rater disagreement, judge bias, or a mismatch between the benchmark and actual use. The statistical tools help characterize some of these uncertainties; they do not repair a biased task set or a poor definition of quality. Repeated runs mainly estimate within-task randomness, and confidence intervals require suitable sampling assumptions. Production behavior is also not reducible to proxy metrics such as session length or thumbs-up rates, so use multiple signals and retain human review where the decision warrants it.

This is Wolfe’s practical roadmap, accompanying an AI Engineer conference presentation—not a comparative study demonstrating that every component works equally well for every agent or domain.

## Related concepts

- [How to write and test agent skills with evals](2026-10-19_article_sergii-makarevych_agent-skill-evals.md) — separates instruction adherence from whether the skill improves outcomes; subjective artifact quality still needs calibrated human labels.
- [How to use decision models for evals](2026-10-20_article_hamel-husain_decision-model-evals.md) — a specific example of evaluating automated judges against human-labeled data and separating thresholds, calibration, performance, and cost.

## Sources

- [Cameron R. Wolfe’s announcement](https://x.com/cwolferesearch/status/2112915508148232571)
- [Evaluating Agents on Highly Subjective Tasks](https://cameronrwolfe.substack.com/p/subjective-evals)

Raw capture: [paraphrased article extraction](raw/2026-10-21_article_cameron-wolfe_subjective-evals.raw.md).
