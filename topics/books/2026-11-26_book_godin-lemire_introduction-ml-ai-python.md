---
title: "Introduction to Machine Learning and Artificial Intelligence with Python"
date: 2026-11-26
type: book
topics:
  - books
tags:
  - machine-learning
  - python
  - deep-learning
  - transformers
  - reinforcement-learning
resource: "https://lemire.github.io/python_book_md/en/"
description: "An implementation-oriented introductory textbook that builds from Python data tools and classical machine learning to neural networks, modern language models and deployment."
authors:
  - Robert Godin
  - Daniel Lemire
sources:
  - resource: "https://lemire.github.io/python_book_md/en/"
  - resource: "https://lemire.me/blog/2026/11/26/our-textbook-on-machine-learning-and-artificial-intelligence-is-out/"
  - resource: "https://x.com/lemire/status/2126300012149879134"
---

# Introduction to Machine Learning and Artificial Intelligence with Python

## TL;DR

Robert Godin and Daniel Lemire's 741-page textbook is an implementation-oriented introduction to machine learning and AI for Python programmers. It moves from NumPy, Pandas and classical models through neural networks and PyTorch to transformers, modern language models, reinforcement learning and deployment. The authors say the exercises have solutions.

**Read online:** [English textbook](https://lemire.github.io/python_book_md/en/). Lemire also links to [paperback](https://www.amazon.com/dp/B0HT2JWXQ5/) and [Kindle](https://www.amazon.com/dp/B0GX32CJ74) editions.

## Who it is for

The preface targets first-course college or university students, curious beginners and working programmers. Basic Python is required; probability, statistics and differential calculus help, but the authors emphasize intuition and use rather than comprehensive mathematical derivations. NumPy and Pandas are introduced in the book.

## Learning path

1. **Data and classical ML:** NumPy and Pandas, linear and multivariate regression, classification and time series. Lemire describes both normal-equation and gradient-descent approaches to linear regression.
2. **Neural-network foundations:** build a network step by step, including forward propagation, backpropagation, minibatches, nonlinearities and classification loss; then move to PyTorch.
3. **Sequences and language models:** recurrent networks, attention and transformers, pretrained models and applications such as embeddings, classification and fine-tuning.
4. **Modern LLM mechanisms:** the announcement highlights key-value caching, grouped-query attention, mixture of experts and quantization, connecting the transformer foundation to contemporary models.
5. **Reinforcement learning and deployment:** reinforcement-learning concepts and a final chapter on performance and serving a model, including a containerized sentiment-analysis example and `torch.compile`.

## How to use it

For a hands-on route, work through the code and exercises rather than only reading: implement a small network before relying on PyTorch abstractions, then follow the LLM and deployment chapters relevant to your projects. The breadth is a useful map, but implementation-focused coverage should not be mistaken for a full mathematical treatment or a substitute for checking current library documentation.

## Sources and reading scope

- [Online textbook and preface](https://lemire.github.io/python_book_md/en/).
- [Lemire's announcement](https://lemire.me/blog/2026/11/26/our-textbook-on-machine-learning-and-artificial-intelligence-is-out/) and [original post](https://x.com/lemire/status/2126300012149879134).

This note is based on the preface, table of contents and author announcements; the complete book and exercises were not independently reviewed or run.
