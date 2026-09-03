---
type: video
source_url: "https://youtu.be/QgH9sr7G13Q?is=HRwIgmb_8kYsW704"
canonical_url: "https://youtube.com/watch?v=QgH9sr7G13Q"
title: The most cited paper of the century is a brilliant hack
author: Welch Labs
created_at: 2026-09-03
topics: [agi]
tags: [resnet, residual-stream, neural-network-architecture, deep-learning]
timestamp: 2026-09-03
resource: "https://youtube.com/watch?v=QgH9sr7G13Q"
description: "Welch Labs explains how ResNet skip connections stabilized deep learning and helped establish the residual stream as a central pattern in modern AI architectures."
---

# The most cited paper of the century is a brilliant hack

*Welch Labs*

## TL;DR

- ResNet solved the degradation problem in very deep neural networks by adding simple skip connections that let information and gradients flow directly through the model.
- The residual stream reframes deep networks as iterative refinement of a persistent state, a pattern carried into Transformers and modern AI systems.
- The video connects ResNet to later evidence about register tokens: without dedicated storage, vision models can repurpose unimportant image positions as working memory.

## Highlights

- [25–59s] The motivating puzzle: adding layers eventually made ImageNet models perform worse, even when a deeper model could represent the shallower model.
- [973–995s] As depth increases, gradients can become unreliable— the “shattered gradients” problem.
- [1041–1108s] A skip connection adds the input around a block, allowing the block to learn residual behavior; the resulting architecture is ResNet.
- [1586–1605s] The residual stream is described as information passed from input to output and iteratively refined by layers.
- [1760–1925s] Register-token experiments support the view of the residual stream as a working memory.

## My notes

- The key design move is an escape hatch for identity: instead of forcing every layer to relearn the whole representation, let it add a residual update to a signal that can travel unchanged. This is a compact example of architectural leverage—make the easy behavior easy, then spend capacity on the difference.
- The video’s line from ResNet to Transformers and register tokens is a useful explanatory synthesis. The ResNet paper establishes the skip-connection architecture; the later residual-stream and register-token interpretations are subsequent developments, not claims tested by that original paper.

## Related concepts

- [What Is Intelligence?](2025-09-23_book_blaise-aguera-y-arcas_what-is-intelligence.md) — a broader treatment of learning, Transformers, and intelligence that provides conceptual context for this architectural history.

## Links

- Permalink: [https://youtube.com/watch?v=QgH9sr7G13Q](https://youtube.com/watch?v=QgH9sr7G13Q)
- [https://arxiv.org/abs/1512.03385](https://arxiv.org/abs/1512.03385)
- [https://www.youtube.com/@WelchLabs](https://www.youtube.com/@WelchLabs)

## Raw

- Raw text: [topics/agi/raw/2026-09-03_video_the-most-cited-paper-of-the-century-is-a-brilliant-hack.raw.md](https://github.com/cast42/notes/blob/main/topics/agi/raw/2026-09-03_video_the-most-cited-paper-of-the-century-is-a-brilliant-hack.raw.md)
- Extractor: youtube-transcript-api+oembed

## My notes
-
