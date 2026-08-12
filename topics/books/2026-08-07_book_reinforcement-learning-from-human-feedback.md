---
type: book
source_url: "https://rlhfbook.com/"
canonical_url: "https://rlhfbook.com/"
resource: "https://rlhfbook.com/"
title: Reinforcement Learning from Human Feedback
author: Nathan Lambert
date: 2026-08-07
timestamp: 2026-08-07
created_at: 2026-08-07
topics: [books]
tags: [rlhf, llm-post-training, preference-learning, reward-modeling, reinforcement-learning, model-evaluation]
description: A practical map of modern language-model post-training, from instruction tuning and preference data through reward models, online RL, direct alignment, evaluation, and model character.
---

# Reinforcement Learning from Human Feedback

*Nathan Lambert*

## TL;DR

- RLHF is best understood as one part of a broader post-training stack: instruction tuning establishes behavior, preference tuning shapes hard-to-specify qualities, and RL with verifiable rewards strengthens capabilities in domains with checkable answers.
- The practical core is a loop over data, reward or judgment signals, and optimization. The decisive choices are often data quality, on-policy versus offline sampling, regularization, and evaluation—not the headline optimizer alone.
- Modern post-training spans reward models, PPO-style policy gradients, GRPO and related methods, DPO-style direct alignment, rejection sampling, synthetic feedback, and distillation; each trades implementation complexity against data freshness, stability, and control.
- Optimization relentlessly exploits proxy weaknesses. Reward hacking, over-refusal, verbosity, evaluator bias, contamination, and brittle benchmarks make regularization and evaluation part of the training system rather than final checks.

## Highlights

- The canonical RLHF recipe has three stages: instruction fine-tuning, preference-data collection plus reward-model training, and policy optimization against that reward signal.
- Preference fine-tuning handles qualities that are difficult to specify directly; RLVR instead uses verifiable rewards and is central to reasoning-oriented models.
- Reward models may score whole outcomes, intermediate processes, or generate critiques and judgments; their usefulness depends on data design and resistance to exploitation.
- Online RL trains on current-policy samples and can generalize beyond demonstrations, while offline methods such as DPO are simpler but inherit the limitations of a fixed preference dataset.
- Tool use, model character, and product behavior are post-training problems: formatting, multi-step interaction, refusal style, and persona must be represented in data and evaluation.

## The book's argument

The book reframes RLHF from a single algorithm into a family of post-training systems. The original recipe—supervised instruction tuning, a reward model learned from human comparisons, then reinforcement learning against that model—still supplies the organizing logic. Modern systems, however, mix and match several sources of supervision and several optimization methods.

Its central distinction is between three jobs:

1. **Instruction tuning** teaches the model to follow prompts, use chat formats, and reproduce desired response structures.
2. **Preference fine-tuning** shapes subjective or hard-to-formalize qualities such as helpfulness, tone, refusal behavior, and style.
3. **Reinforcement learning with verifiable rewards (RLVR)** improves performance where answers can be checked automatically, especially reasoning, mathematics, and code.

This makes post-training an engineering system rather than a fixed recipe. The data distribution, feedback mechanism, sampling policy, loss, regularization, and evaluation suite all interact.

## Methods covered

- **Reward modeling:** Bradley–Terry pairwise preference models, outcome and process reward models, value functions, and generative judges. Reward models compress judgments into a training signal, but also create a proxy that the policy can exploit.
- **Online reinforcement learning:** policy-gradient methods including REINFORCE, RLOO, PPO, GRPO, GSPO, and CISPO. Their differences concern baselines, clipping, importance sampling, value models, and how token- or sequence-level losses are aggregated.
- **Direct alignment:** DPO and related objectives optimize from a fixed set of preferred and rejected responses without a separate online RL loop. They are operationally simpler, but depend heavily on the coverage and provenance of offline data.
- **Rejection sampling and best-of-N:** generate several responses, score them, then use the best responses for inference or further supervised training. This is simple and effective when generation and scoring are affordable.
- **Synthetic data and distillation:** stronger models, AI judges, constitutional rules, and prompt-specific rubrics can generate supervision. On-policy teacher–student distillation reduces the mismatch between a fixed synthetic dataset and the student's current behavior.

## Practical lessons

- Preference data is a product and measurement problem. Interface design, ranking versus rating, annotator instructions, multi-turn context, sourcing, and systematic bias determine what the model actually learns.
- Fresh, on-policy data is powerful because it targets the current model's errors. Offline data is easier to reuse, but becomes stale as the policy changes.
- Regularization is essential. KL penalties, reference models, pretraining gradients, and conservative objectives limit drift and protect capabilities while optimizing a noisy proxy.
- Evaluation must mirror the intended deployment. Prompt templates, chain-of-thought settings, judge models, contamination, evaluator variance, and agentic tool environments can change apparent performance substantially.
- Model character is trained behavior, not cosmetic prompting. Persona, verbosity, uncertainty, refusal boundaries, and tool etiquette emerge from repeated choices in data and optimization.

## Failure modes and open questions

The recurring danger is over-optimization: a model learns to maximize the measured reward rather than the underlying human goal. Symptoms include verbosity, sycophancy, over-refusal, stylistic homogenization, reward hacking, and benchmark-specific behavior. The book therefore treats evaluation and regularization as continuous controls around optimization.

Open problems include combining heterogeneous feedback signals, building robust judges, deciding when human feedback remains necessary, training reliable multi-step tool use, evaluating agentic systems, preserving useful diversity and character, and understanding why online RL can generalize differently from supervised imitation.

## Links

- Canonical book page: [https://rlhfbook.com/](https://rlhfbook.com/)
- [https://rlhfbook.com/book.pdf](https://rlhfbook.com/book.pdf)
- [https://github.com/natolambert/rlhf-book](https://github.com/natolambert/rlhf-book)
- [https://arxiv.org/abs/2504.12501](https://arxiv.org/abs/2504.12501)

## Raw

- [Extracted PDF text](raw/2026-08-07_book_reinforcement-learning-from-human-feedback.raw.md)
- Extractor: pypdf 6.1.0 text extraction from https://rlhfbook.com/book.pdf
