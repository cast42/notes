---
type: article
source_url: "https://www.xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design/"
canonical_url: "https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design"
title: Zaya1-8B and why its design may matter more than its benchmark numbers
author: Adam Conway
created_at: 2026-05-23
topics: [local_models]
content_hash: 9c6cabdf833792c6160ed2c1307ef996c1b876a00de0915fff8c01cf2d624fa3
extracted_at: "2026-05-23T06:58:12"
extractor: summarize+web-fetch
date: 2026-05-23
timestamp: 2026-05-23
tags:
  - zaya1-8b
  - small-language-models
  - model-architecture
  - benchmark-evaluation
  - local-inference
resource: "https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design"
---

# Raw content

Source: https://xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design


URL: https://www.xda-developers.com/tried-new-8b-local-llm-deepseek-r1-design/
Title: I tried a new 8B local LLM, and its design might be the biggest shift since DeepSeek R1
Author: Adam Conway
Published: 2026-05-22

Summarize output:
Zyphra's Zaya1-8B stands out because it is not just another small reasoning model with a familiar transformer plus reinforcement learning stack. The article argues that its real significance is architectural: Compressed Convolutional Attention shrinks queries, keys, and values into a shared latent space, cutting KV-cache size by 8x with no measured quality loss, while also speeding prefill by 1.7x and backprop by 1.3x in Zyphra's tests. On top of that, the model uses a custom MoE router with an MLP gate and PID-style bias balancing to keep experts from collapsing into a few overused paths, which helps explain how a model with only about 760 million active parameters per token can perform near much larger systems on math and coding tasks.
*"The design is the bigger deal."*
The second major idea is Markovian RSA, a reasoning method that generates several parallel reasoning traces, keeps only their tail segments, and repeatedly merges them into a better answer. The key point is that this format is not added at inference time as a hack. Zyphra co-trained the model on it during supervised fine-tuning and later reinforcement-learning stages, so the model "expects" this multi-trace aggregation process. Zyphra reports that this setup reaches 91.9% on AIME 2025 and 89.6% on HMMT 2025 Feb with RSA enabled, approaching much larger frontier reasoning systems. The article treats those benchmark claims cautiously because they are vendor-reported, but sees the training design as unusually substantive and portable.
The hands-on local test is where the piece gets more concrete. The author failed to get the model running cleanly on a Radeon 7900 XTX because of ROCm and kernel issues, then switched to an M4 Pro MacBook. There, full BF16 ran at about 7 tokens per second, but an MXFP4 quantized run through vMLX reached roughly 42 tok/s with no visible loss in output quality on tested prompts. On a custom logarithm problem, Zaya1 repeatedly found the correct answer, 272, after about 7,400 reasoning tokens and even verified it using a second method, while several much larger hosted models reportedly answered incorrectly or inconsistently. The big limitation is that local users cannot yet run the full RSA scaffold, so long multi-part tasks can still hit token-budget ceilings before finishing.
*"The weights know how to reason their way to a multi-part answer."*


Additional article details captured via web fetch:
- Model discussed: Zyphra Zaya1-8B
- Key architectural ideas highlighted: Compressed Convolutional Attention (CCA / CCGQA), Markovian RSA, PID-style MoE routing bias balancing
- Reported claims include 8x KV-cache compression, 1.7x faster prefill, and strong math/coding benchmark performance with RSA enabled
- Hands-on notes include ROCm issues on Radeon 7900 XTX and a more successful run on an M4 Pro MacBook using vMLX and an MXFP4 quant
