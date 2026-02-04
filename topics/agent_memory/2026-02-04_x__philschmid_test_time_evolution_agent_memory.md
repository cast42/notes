---
title: "Test-time evolution for agent memory (TAME)"
date: 2026-02-04
type: note
topics:
  - agent_memory
tags:
  - memory
  - rag
  - agents
  - test_time
  - evaluation
people:
  - Philipp Schmid
source:
  kind: x
  url: https://x.com/_philschmid/status/2019081772189823239
---

## TL;DR

Static “store everything” memory (and static RAG) tends to accumulate noise. The proposed idea is to **evolve/refine memory at test-time**: actively **search**, **synthesize**, and **evolve** what the agent remembers after each interaction — including the ability to **refine and delete** irrelevant experiences.

## What the X post claims (verbatim-ish)

Philipp’s summary:

- Static RAG is insufficient for agent memory; naive accumulation creates noise.
- A Google DeepMind paper proposes **“Test-Time Evolution”** where agents actively **Search**, **Synthesize**, and **Evolve** memory after every interaction.
- Key findings mentioned:
  - Active memory refinement reduced task steps by ~50% (22.6 → 11.5 on AlfWorld).
  - Smaller models saw disproportionately larger gains, sometimes rivaling larger static models.
  - Success depends on the ability to refine + delete irrelevant experiences, not just store them.

![figure](https://pbs.twimg.com/media/HAU4IiqXAAAx9Ce?format=jpg&name=large)

## Paper (arXiv)

Using the arXiv API query for “Test-Time Evolution agent memory”, the most directly matching result is:

- **TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking**
  - arXiv (abs): https://arxiv.org/abs/2602.03224
  - PDF: https://arxiv.org/pdf/2602.03224

If you want, I can double-check this is exactly the paper referenced in the tweet once browser control is stable again (t.co card link extraction was flaky).

## Why I care (agent memory design)

- “Memory” is not just storage; it’s an **editing process**.
- The killer capability is **forgetting and distilling** (turning episodes into reusable procedures / heuristics).
- Benchmarks that measure both **utility** and **trust/safety drift** during memory evolution are likely going to matter.
