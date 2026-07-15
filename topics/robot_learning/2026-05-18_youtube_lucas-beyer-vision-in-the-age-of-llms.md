---
type: youtube
source_url: "https://www.youtube.com/watch?v=0XB7fNS_ONg"
canonical_url: "https://youtube.com/watch?v=0XB7fNS_ONg"
title: "Lucas Beyer: Vision in the Age of LLMs"
author: Oier Mees
handle: oier.m
created_at: 2026-05-18
topics: [robot_learning]
tags:
  - computer-vision
  - vision-language-models
  - representation-learning
  - visual-foundation-models
  - robot-perception
date: 2026-05-18
timestamp: 2026-05-18
resource: "https://youtube.com/watch?v=0XB7fNS_ONg"
---

# Lucas Beyer: Vision in the Age of LLMs

*Oier Mees — @oier.m*

## TL;DR

- Lucas Beyer argues that modern vision is close to being "solved" for many perception tasks, mainly through a reliable recipe of large-scale pre-training, targeted mid-training, and small-task fine-tuning.
- He says web-scale image-text training removed the bottleneck of narrow class labels, but contrastive training like CLIP often learns object identity better than relationships, which is why he prefers captioning-style next-token training for richer visual understanding.
- He emphasizes that filtering datasets toward English or North American distributions can improve standard benchmarks while hurting global coverage and real-world robustness.
- His practical advice is strikingly direct: start from a strong pre-trained VLM, collect a few hundred examples for your task, fine-tune, and you will often get something useful very quickly.
- The real frontier is no longer basic perception, but reasoning, planning, action, streaming efficiency, and generalization to new tasks from instructions alone.

## Highlights

- YouTube title: Lucas Beyer: Vision in the Age of LLMs [ETHZ Robot Learning 2026].
- Course context: Week 11, Frontier & Open Problem.
- Guest spotlight: Lucas Beyer, Meta Superintelligence Labs.
- Beyer’s framing: performance jumped when vision scaled model size, dataset size, and training time together, not by merely stretching older ImageNet-era recipes.
- He argues captioning-style training captures relationships better than contrastive-only training, especially spatial or relational concepts like "left of" or "sitting".
- He warns that benchmark-oriented filtering can create blind spots for non-Western objects, landmarks, and language distributions.
- Mid-training is presented as the place to add reusable skills like OCR, localization, segmentation, higher-resolution understanding, and object-centric Q&A.
- Practical recipe: take a strong VLM, gather a few hundred task-specific examples, fine-tune, and test quickly.
- Remaining frontier: reasoning, planning, action, streaming, and instruction-following generalization rather than raw perception.

## Links

- Permalink: [https://youtube.com/watch?v=0XB7fNS_ONg](https://youtube.com/watch?v=0XB7fNS_ONg)
- [https://cvg.ethz.ch/lectures/Robot-Learning/](https://cvg.ethz.ch/lectures/Robot-Learning/)
- [https://github.com/mees-robot-learning-course/ethz-course-2026](https://github.com/mees-robot-learning-course/ethz-course-2026)
- [https://lucasb.eyer.be/](https://lucasb.eyer.be/)

## Raw

- Raw text: [topics/robot_learning/raw/2026-05-18_youtube_lucas-beyer-vision-in-the-age-of-llms.raw.md](https://github.com/cast42/notes/blob/main/topics/robot_learning/raw/2026-05-18_youtube_lucas-beyer-vision-in-the-age-of-llms.raw.md)
- Extractor: youtube-oembed+course-page-web-fetch

## My notes
-
