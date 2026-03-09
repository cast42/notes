---
title: "Karpathy autoresearch + Tobi’s qmd experiment: autonomous ML research loops in practice"
date: 2026-03-09
type: note
topics:
  - agentic_coding
tags:
  - x
  - autoresearch
  - qmd
  - llm_training
  - agents
source: "https://x.com/i/status/2030371219518931079"
---

## TL;DR
Karpathy shared **autoresearch**, a minimal repo for autonomous LLM-training experimentation: human iterates on prompt/spec, agent iterates on training code, repeatedly running short experiments and committing improvements.

Tobi then reported applying this pattern to qmd model work overnight and seeing a **~19% score gain** on a smaller 0.8B model (surpassing prior 1.6B baseline), after 37 experiments in ~8 hours.

## Key takeaways
- The pattern is a practical template for **agentic research loops**:
  - human defines goal/constraints in prompt/docs
  - agent proposes code changes + runs experiments
  - results are tracked over many short runs
- Core mechanism is not one “smart prompt,” but **high iteration throughput** + automatic experiment logging.
- Tobi’s qmd result suggests this can transfer from a generic training harness to **domain-specific model optimization** (query expansion + reranking quality/speed tradeoffs).
- This is an early but concrete signal that small teams can run continuous ML improvement loops with low manual overhead.

## What Karpathy posted (summary)
- Packaged `autoresearch` as a self-contained minimal repo.
- Described setup as:
  - human iterates on a prompt file (`.md`)
  - agent iterates on training code (`.py`)
- Goal: maximize research progress with minimal human intervention.
- Experiment style: many fixed-length runs (5 minutes each), agent looping autonomously on a git feature branch and committing improvements.

## What Tobi reported (qmd-specific)
- Before sleep, he asked his pi/agent to adapt the approach for qmd query-expansion model work using qmd repo data.
- Overnight result: **+19% score** on a 0.8B model, above previous 1.6B score baseline, after 37 experiments in ~8 hours.
- He also reported early gains on a new reranker baseline.
- Emphasis: value was not only the metric bump, but visibility into the agent’s reasoning and experiment chain.

## Practical implications for qmd / local note search workflows
- Agentic research loops can be used to optimize:
  - query expansion quality
  - reranker quality/latency balance
  - model size vs quality operating point
- Important operational ingredients:
  - short deterministic runs
  - clear scoring function
  - strict experiment tracking (commits/metrics)
  - branch isolation for safe iterative changes

## Links
- Karpathy post: https://x.com/i/status/2030371219518931079
- Repo: https://github.com/karpathy/autoresearch
- Tobi post (qmd results): https://x.com/i/status/2030771823151853938
