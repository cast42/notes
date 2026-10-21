---
title: "How to use decision models for evals"
date: 2026-10-20
type: article
topics:
  - agentic_coding
tags:
  - automated-evaluation
  - decision-models
  - threshold-tuning
  - calibration
  - precision-recall
resource: "https://hamel.dev/blog/posts/decision-model-evals/"
description: "Hamel Husain and Antaripa Saha show that automated eval classifiers must be measured on task-specific labels, with deliberate thresholds and separate checks for score calibration, cost, and performance."
author:
  - Hamel Husain
  - Antaripa Saha
generated:
  by: "process:codex"
  at: "2026-10-21T22:00:00+02:00"
sources:
  - id: "announcement-post"
    resource: "https://x.com/HamelHusain/status/2112588257104216294"
  - id: "article"
    resource: "https://hamel.dev/blog/posts/decision-model-evals/"
---

# How to use decision models for evals

## TL;DR

- A decision model's score and the threshold used to turn that score into a pass/fail decision are separate choices. The default 0.50 threshold is not automatically right for your eval.
- Choose operating thresholds against labeled examples and the real cost of false positives versus false negatives. Tune on training data and report performance on held-out data.
- A model's ranking quality, its thresholded classification quality, and its probability calibration answer different questions. Check each separately; calibration can help or hurt.
- The authors' apartment-leasing comparison is a useful worked example, not a general leaderboard: it uses 98 labeled traces for one broad failure-finding task, and the authors note that performance varies by task and dataset.

## The method

1. **Define a concrete binary decision.** The study labels a trace as pass or fail for whether an assistant made a substantive error. Clear criteria make the model's output comparable with human labels.
2. **Build labeled examples for your task.** The authors begin with 100 apartment-leasing-agent traces and exclude two internal QA examples, leaving 98 for performance analysis. The set contains 61 traces labeled with failures and 37 without labeled failures.
3. **Select an operating objective.** Precision asks how many flagged examples are genuine failures; recall asks how many known failures are caught. Choose minimum acceptable values and a tradeoff that reflects the consequences of missed failures and false alarms. F1 is one choice when precision and recall deserve equal weight, not a universal default.
4. **Tune thresholds without peeking at validation data.** Using the saved model scores, the authors use stratified five-fold cross-validation: choose a threshold on each training fold and measure it on the held-out fold, using shared splits when comparing models. They compare tuned thresholds with 0.50.
5. **Check constraints, not only the headline score.** The example seeks at least 80% precision and recall when possible. Some training folds had no threshold meeting both limits; the paper reports these cases and includes fallback results, so the minimums are not guarantees of held-out performance.
6. **Compare quality and operating cost.** On this dataset, Perplexity reached F1 0.79 at about 0.82 cents per 100 evaluations; OpenAI Decisions reached 0.87 at about 3.72 cents per 100 evaluations. Latency was omitted from the main comparison, so this is not a complete operational ranking.
7. **Calibrate probabilities only if you need confidence estimates.** A score of 0.8 should correspond to about an 80% observed failure rate among examples with similar scores. The authors test Platt scaling with cross-validation and find that it helps some models slightly, has little effect on others, and worsens OpenAI's Brier score with the tested fit. A threshold for classification is not itself a calibrated probability.
8. **Iterate the evaluator too.** The authors recommend narrower judges for distinct failure modes and note that better prompts may change thresholds and model comparisons. Re-run the measurement after prompt or data changes.

## What generalizes

The most reusable lesson is experimental, not model-specific: choose an eval objective and acceptable error tradeoff first; compare against human-labeled examples; separate training-time threshold selection from held-out measurement; and report cost alongside performance. When confidence estimates drive downstream decisions, measure calibration on representative, held-out examples rather than interpreting raw scores literally.

The article's scores describe one prompt, six named decision-model versions, and a small, domain-specific dataset collected in 2026. The results do not establish that decision models always beat LLM judges, that one vendor is best generally, or that these model versions remain available or competitive. The authors explicitly say task and dataset change performance. Their calibration plots use small groups of traces, so they are diagnostic examples rather than precise estimates of future failure rates.

## Related concepts

- [How to write and test agent skills with evals](2026-10-19_article_sergii-makarevych_agent-skill-evals.md) — also separates evaluator behavior from outcome and emphasizes task-specific validation.
- [Building agentic applications with PydanticAI](2026-02-06_article_pydantic_building_agentic_application.md) — background on eval datasets and LLM judges.

## Sources

- [Hamel Husain's announcement](https://x.com/HamelHusain/status/2112588257104216294)
- [Full article with interactive charts, appendices, and linked data](https://hamel.dev/blog/posts/decision-model-evals/)

Raw capture: [paraphrased article extraction](raw/2026-10-20_article_hamel-husain_decision-model-evals.raw.md).
