---
type: tweet
source_url: "https://x.com/rasbt/status/2095141254958858496"
canonical_url: "https://x.com/rasbt/status/2095141254958858496"
title: Sebastian Raschka on OpenAI Astra and looped Transformers
author: Sebastian Raschka
handle: rasbt
created_at: 2026-09-02
topics: [agi]
tags: [openai-astra, looped-transformer, recursive-computation, parameter-sharing, chain-of-thought]
timestamp: 2026-09-02
resource: "https://x.com/rasbt/status/2095141254958858496"
description: "Sebastian Raschka explains the parameter, memory, compute, and reasoning-visibility trade-offs behind the rumored looped Transformer approach associated with OpenAI Astra."
---

# Sebastian Raschka on OpenAI Astra and looped Transformers

*Sebastian Raschka — @rasbt*

## TL;DR

- The rumored Astra technique is described as a looped or recurrent Transformer: reuse the same layer stack for another pass instead of adding a second set of weights.
- Weight sharing can increase effective depth and reduce storage and RAM, but it nearly doubles compute when the text is processed through the stack again.
- The post separates looped computation from chain-of-thought visibility: hidden-state computation may be less legible, but layer reuse alone does not suppress textual reasoning.

## Highlights

- Nanbeige4.2 is presented as a concrete open-weight example: a shared 22-layer stack is run twice, giving roughly 44 effective layers without duplicating weights.
- The reported trade-off is about 75% of the token efficiency of a standard architecture for two passes; more passes added little while increasing training cost.
- Mixture-of-Recursions adds a learned router so tokens can receive different numbers of recursive passes, allowing easy tokens to exit earlier.
- Raschka argues that any reduction in visible chain of thought would more plausibly come from shifting work into latent activations, not from looped Transformers inherently hiding reasoning.

## Context

- The post appeared amid hype about the upcoming, rumored OpenAI Astra release. It responds to a report attributed to *The Information*; Astra’s actual architecture is not confirmed by an OpenAI technical disclosure here.

## My notes

- The key distinction is **parameter efficiency versus compute efficiency**: reusing a layer stack keeps the model smaller to store and load, but repeated passes still cost roughly proportional extra inference compute.
- The useful question for Astra is therefore not simply whether it “loops,” but how many passes it uses, whether routing is token-adaptive, and how quality, latency, memory, and cost compare with a conventional model of similar effective depth.
- Layer reuse alone does not hide chain of thought. It can move more computation into latent activations, but the same visibility trade-off can also come from larger models or other inference-time computation. The 75% efficiency figure is a claim relayed by Raschka and should be read against the Nanbeige report’s exact metric.

## Related concepts

- [What Is Intelligence?](2025-09-23_book_blaise-aguera-y-arcas_what-is-intelligence.md) — broader context on Transformers, learning, and intelligence.

## Links

- Permalink: [https://x.com/rasbt/status/2095141254958858496](https://x.com/rasbt/status/2095141254958858496)
- [https://www.theinformation.com/articles/secret-technique-behind-openais-astra-model-sparks-security-concerns](https://www.theinformation.com/articles/secret-technique-behind-openais-astra-model-sparks-security-concerns)
- [https://arxiv.org/abs/2607.22083](https://arxiv.org/abs/2607.22083)
- [https://arxiv.org/abs/2507.10524](https://arxiv.org/abs/2507.10524)
- [https://x.com/rasbt/status/2095141254958858496/photo/1](https://x.com/rasbt/status/2095141254958858496/photo/1)

## Raw

- Raw text: [topics/agi/raw/2026-09-02_tweet_sebastian-raschka-on-openai-astra-and-looped-transformers.raw.md](https://github.com/cast42/notes/blob/main/topics/agi/raw/2026-09-02_tweet_sebastian-raschka-on-openai-astra-and-looped-transformers.raw.md)
- Extractor: fxtwitter
