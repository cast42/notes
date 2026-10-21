---
title: "Working extraction: How to use decision models for evals"
date: 2026-10-20
type: source
topics:
  - agentic_coding
tags:
  - decision-models
  - threshold-tuning
  - calibration
resource: "https://hamel.dev/blog/posts/decision-model-evals/"
generated:
  by: "process:codex"
  at: "2026-10-21T22:00:00+02:00"
extractor: "FxTwitter API and Hamel's Blog; paraphrased summary"
sources:
  - id: "announcement-post"
    resource: "https://x.com/HamelHusain/status/2112588257104216294"
  - id: "article"
    resource: "https://hamel.dev/blog/posts/decision-model-evals/"
---

# Working extraction

This is a paraphrased source summary, not a verbatim copy of the article.

## Announcement

Hamel Husain announced an article on using decision models for evals. Its central recommendations are to select a decision model for the task, tune its operating threshold rather than assume 0.50, and interpret scores with care.

## Experiment and findings

The article compares Jev 1.13, Perplexity Decider 1.1 27B, Liquid d1 and d1-ultra, Cloudflare Clef Flash, and OpenAI Decisions using apartment-leasing agent traces labeled by humans as passing or failing. The evaluation task asks whether a trace contains at least one substantive assistant or tool-use problem. The authors began with 100 traces, excluded two internal QA examples, and report results on 98: 61 with a labeled failure and 37 without one.

Each system produces a score from 0 to 1. The default classification cutoff is 0.50, but the same scores can produce different precision/recall tradeoffs at other cutoffs. The article uses stratified five-fold cross-validation to choose thresholds on training folds and report on held-out folds. It examines F1, but also illustrates an 80% minimum for both precision and recall. When no threshold met both minimums in a training split, the authors mark the split as infeasible and use unconstrained F1 tuning; those cases remain in validation averages.

On this dataset, tuned Perplexity Decider achieved F1 0.79 at about 0.82 cents per 100 runs. OpenAI Decisions achieved F1 0.87 at about 3.72 cents per 100 runs. The authors omit latency from the main comparison and caution that results vary with the task and dataset.

The article separately checks probability calibration using held-out predictions and Platt scaling. Some systems move closer to observed failure rates, but calibration changes little for some and slightly worsens OpenAI's Brier score under the tested fit. Calibration results use a small number of examples and do not guarantee accurate future probabilities.

The authors recommend defining task-specific failure criteria, setting minimum requirements before choosing a model, selecting thresholds according to operational costs, measuring probability calibration if scores will be used as confidence, and comparing quality against cost and latency. They suggest narrowing judges to individual failure modes and rerunning measurements after prompt or data changes.
