---
type: article
source_url: "https://www.xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design/"
canonical_url: "https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design"
title: Zaya1-8B and why its design may matter more than its benchmark numbers
author: Adam Conway
created_at: 2026-05-23
topics: [local_models]
---

# Zaya1-8B and why its design may matter more than its benchmark numbers

*Adam Conway*

## TL;DR

- Adam Conway argues that Zyphra’s Zaya1-8B is interesting less because it is another small reasoning model and more because it combines several substantive architectural ideas in one local model stack.
- The note highlights three main ideas: compressed attention for a much smaller KV cache, co-trained Markovian RSA for bounded-context multi-trace reasoning, and a PID-style MoE router to avoid expert collapse.
- The hands-on takeaway is that local deployment was messy on ROCm hardware but much smoother on an Apple Silicon setup with quantization, where the model appeared strong on tested reasoning tasks.

## Highlights

- The article frames the design, not just the benchmark score, as the important shift.
- Compressed Convolutional Attention reportedly compresses KV cache by 8x with no measured quality loss in Zyphra’s tests.
- Markovian RSA is co-trained into the model instead of being added later as an inference-only scaffold.
- The MoE router uses an MLP gate with PID-style bias balancing to stabilize expert usage.
- The local test reportedly failed on a 7900 XTX ROCm setup but ran far better on an M4 Pro MacBook using vMLX and an MXFP4 quant.

## Links

- Permalink: [https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design](https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design)
- [https://www.xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design/](https://www.xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design/)
- [https://arxiv.org/abs/2510.04476](https://arxiv.org/abs/2510.04476)
- [https://arxiv.org/pdf/2605.05365](https://arxiv.org/pdf/2605.05365)

## Raw

- Raw text: [topics/local_models/raw/2026-05-23_article_zaya1-8b-and-why-its-design-may-matter-more-than-its-benchmark-numbers.raw.md](https://github.com/cast42/notes/blob/main/topics/local_models/raw/2026-05-23_article_zaya1-8b-and-why-its-design-may-matter-more-than-its-benchmark-numbers.raw.md)
- Extractor: summarize+web-fetch

## My notes
-
