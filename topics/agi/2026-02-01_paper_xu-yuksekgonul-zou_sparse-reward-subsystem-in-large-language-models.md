---
title: "Sparse Reward Subsystem in Large Language Models"
date: 2026-02-01
timestamp: 2026-02-01
type: paper
topics:
  - agi
tags:
  - mechanistic-interpretability
  - reward-modeling
  - reasoning
  - temporal-difference-learning
  - process-reward-models
resource: "https://arxiv.org/abs/2602.00986"
source_url: "https://arxiv.org/abs/2602.00986"
canonical_url: "https://arxiv.org/abs/2602.00986"
author: "Guowei Xu, Mert Yuksekgonul, and James Zou"
paper_version: "v2, revised 2026-05-11"
description: "The paper reports that reward-related information in LLM hidden states is concentrated in sparse value and dopamine neurons, enabling confidence prediction and process reward modeling."
sources:
  - id: arxiv-abstract
    resource: "https://arxiv.org/abs/2602.00986"
    title: "arXiv abstract"
  - id: arxiv-paper
    resource: "https://arxiv.org/pdf/2602.00986"
    title: "Paper PDF"
  - id: x-post
    resource: "https://x.com/HowToPrompt__/status/2096074597674500503"
    title: "How To Prompt post about the paper"
generated:
  by: "process:codex"
  at: "2026-09-06T10:27:00+02:00"
verified:
  - by: "process:codex"
    at: "2026-09-06T10:27:00+02:00"
---

# Sparse Reward Subsystem in Large Language Models

*Guowei Xu, Mert Yuksekgonul, and James Zou*

## TL;DR

- Xu, Yuksekgonul, and Zou report that reward-related information in several LLMs is concentrated in a small subset of hidden-state neurons rather than being uniformly distributed across the representation.
- They distinguish **value neurons**, which predict the expected success of a partial reasoning state, from **dopamine neurons**, which encode step-level temporal-difference (TD) or reward-prediction errors.
- The result suggests that models contain sparse, reusable signals for evaluating reasoning progress. It does **not** show that LLMs have biological dopamine systems, human-like motivation, or consciousness: the terminology is explicitly an analogy.

## Key takeaways

- Less than 1% of neurons were sufficient for value probes to retain predictive power in the reported pruning experiments. The authors find similar sparse value-neuron patterns across several models, layers, and task families.
- In a Qwen-2.5-7B-SimpleRL-Zoo intervention on MATH500, zeroing the identified 1% subset reduced average accuracy from 75.2% to 20.3%, a 54.9-point drop. This is strong model- and task-specific causal evidence, not a universal claim that removing 1% of neurons breaks every LLM.
- The value-neuron signal can predict model confidence before generation and during reasoning. The dopamine-neuron signal can act as an internal process-reward model for selecting promising reasoning steps during inference-time search.
- In the paper's MATH500 search experiment, dopamine-neuron guidance reached 77.8% accuracy, compared with 72.2% for greedy and random baselines and 75.0% for the paper's implicit PRM baseline.

## The proposed subsystem

The paper treats an autoregressive LLM as a policy operating over partial reasoning trajectories. A partial state has an implicit **value**: the expected probability that continuing from it will eventually produce a correct answer. A newly generated step also has a TD error: whether that step made the expected outcome better or worse than predicted.

The authors use two probe-defined neuron groups:

1. **Value neurons** encode information about the expected value of the current state. Their activations can be used to estimate correctness or confidence.
2. **Dopamine neurons** encode step-level TD errors. Their activations tend to peak when reasoning makes unexpected progress and dip when the model encounters an error.

The “value” and “dopamine” labels are borrowed from neuroscience because the computational roles resemble value representation and reward-prediction error. They are not evidence that the neurons are biological counterparts of dopamine neurons.

## Why this matters

The most useful idea is architectural and functional: an LLM may carry a sparse internal evaluation layer alongside its token-generation machinery. That creates a possible bridge between mechanistic interpretability and inference control:

- confidence could be estimated from a small targeted set of activations;
- internal TD-error signals could guide search without a separately trained external process-reward model;
- interventions on those neurons may reveal how long-horizon reasoning is monitored and corrected;
- sparse signals could make monitoring cheaper and more portable across tasks and models.

This is a more concrete proposal than saying merely that “hidden states contain confidence.” It asks where the signal lives, whether it is causally involved, and whether it can be reused to steer computation.

## What the result does—and does not—mean

The evidence supports the narrower claim that reward-related quantities are decodable from, and in some interventions functionally connected to, sparse neuron subsets in the tested LLMs. It does not establish that models experience reward, possess intrinsic goals, or reproduce the human brain's reward circuitry.

The paper's explanation for why such a subsystem might emerge—an autoregressive policy benefits from tracking the value of partial trajectories, and superposition can make frequently useful low-dimensional features sparse—is presented by the authors as **motivation, not rigorous proof**. Probe success also does not by itself prove that the model internally computes the same concepts in the way a human does.

The work is an arXiv preprint. Its strongest claims are therefore the specific probing, pruning, intervention, transfer, and search results reported in the paper. Generality beyond the evaluated architectures, layers, tasks, and probe choices remains an open question.

## Relation to the X post

The [How To Prompt post](https://x.com/HowToPrompt__/status/2096074597674500503) presents the finding as an “exact” biological equivalent of dopamine neurons and says Stanford “proved” that LLMs built the same system. That is rhetorically effective but stronger than the paper. A calibrated summary is: **the authors found sparse neural representations with computational roles analogous to value and reward-prediction-error signals, and demonstrated useful causal and applied effects in selected models and tasks.**

## Related concepts

- [The most cited paper of the century is a brilliant hack](2026-09-03_video_the-most-cited-paper-of-the-century-is-a-brilliant-hack.md) — the residual stream as a persistent workspace in which sparse functional signals may be represented.
- [Sebastian Raschka on OpenAI Astra and looped Transformers](2026-09-02_tweet_sebastian-raschka-on-openai-astra-and-looped-transformers.md) — latent computation and the difficulty of inferring reasoning from visible text.
- [Reinforcement Learning from Human Feedback](../books/2026-08-07_book_reinforcement-learning-from-human-feedback.md) — process rewards, reward models, and the risks of optimizing proxies.

## Sources

- [arXiv abstract](https://arxiv.org/abs/2602.00986) [arxiv-abstract]
- [Paper PDF](https://arxiv.org/pdf/2602.00986) [arxiv-paper]
- [How To Prompt post](https://x.com/HowToPrompt__/status/2096074597674500503) [x-post]

The post and paper research capture are preserved in [the raw source note](raw/2026-02-01_paper_xu-yuksekgonul-zou_sparse-reward-subsystem-in-large-language-models.raw.md).
