---
title: "Working extraction: Evaluating agents on highly subjective tasks"
date: 2026-10-21
type: source
topics:
  - agentic_coding
tags:
  - agent-evaluation
  - subjective-evaluation
  - llm-as-a-judge
  - uncertainty
resource: "https://cameronrwolfe.substack.com/p/subjective-evals"
generated:
  by: "process:codex"
  at: "2026-10-22T08:05:00+02:00"
extractor: "Substack article; paraphrased extraction"
sources:
  - id: "announcement-post"
    resource: "https://x.com/cwolferesearch/status/2112915508148232571"
  - id: "article"
    resource: "https://cameronrwolfe.substack.com/p/subjective-evals"
---

# Working extraction

This is a paraphrased source summary, not a verbatim copy of the article.

## Problem

Agent evaluations are hard to interpret because agents cover many kinds of work, realistic tasks can be long and costly, outputs vary across runs, and subjective work often lacks deterministic pass/fail checks. Human ratings and LLM judges both add disagreement and uncertainty.

## Evaluation tools

- **LLM judges and rubrics:** A judge applies defined quality criteria; a rubric breaks quality into task-specific checks. Both can scale evaluation but can be biased or inaccurate. Compare judge predictions with human-labeled examples and, where possible, meaningful production outcomes.
- **Power analysis:** Estimate how many task samples are needed based on the effect worth detecting, expected variability, and chosen statistical error rates.
- **Confidence intervals:** Report uncertainty around estimated performance. Account for dependent tasks when relevant; comparing systems on shared tasks and analyzing paired differences can control some variation due to task difficulty.
- **Repeated runs:** Repeat agent executions and, if needed, judge evaluations to estimate and reduce within-task randomness. Repeated scoring does not remove task-sampling uncertainty or guarantee narrower intervals in every setup.
- **Task curation:** Aim for broad coverage, realistic tasks, adequate difficulty, useful discrimination among candidates, and accurate task/grader specifications. Taxonomies, human or model-based difficulty assessments, IRT, and failure audits are possible aids.

## Three-part roadmap

1. Human evaluation provides the reference definition of quality. Experts help make criteria and scoring examples clear. Multiple ratings of shared examples expose disagreement; agreement metrics and continuing calibration can guide improvements. If a criterion remains unreliable, simplify, subdivide, or drop it.
2. Offline evaluation uses validated LLM judges or rubrics to screen and compare candidates efficiently. The automatic evaluator should be checked against human-scored “golden” examples, and benchmark tasks should be refreshed to limit saturation and noise.
3. Production monitoring tracks explicit user feedback and implicit signals such as session abandonment. A/B tests compare promising agents on actual traffic before full rollout. Monitoring can reveal new tasks and failures to add to the evaluation set.

The workflow is iterative: use offline results to select candidates for human review, then test the strongest candidates in production; feed observations back into the benchmark and its criteria.

## Caution

Scores are estimates over selected tasks and graders, not direct measures of general capability. A benchmark can be unrepresentative, saturated, incorrectly specified, or noisy. Statistical intervals and more runs clarify uncertainty only under suitable design and assumptions; they cannot correct a bad construct or biased sample. Production signals are additional evidence, not perfect measures of quality.
