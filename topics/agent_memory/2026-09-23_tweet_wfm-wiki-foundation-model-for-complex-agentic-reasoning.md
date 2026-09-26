---
type: "tweet"
source_url: "https://x.com/omarsar0/status/2102579964436680959"
canonical_url: "https://x.com/omarsar0/status/2102579964436680959"
title: "WFM: Wiki Foundation Model for Complex Agentic Reasoning"
author: "elvis"
handle: "omarsar0"
created_at: "2026-09-23"
date: "2026-09-23"
topics: ["agent_memory"]
tags:
  - agent-memory
  - linked-markdown
  - graph-retrieval
  - multi-hop-reasoning
  - rag
resource: "https://x.com/omarsar0/status/2102579964436680959"
description: "A Wiki Foundation Model treats linked Markdown pages as both dense semantic context and explicit graph structure for agent memory and retrieval."
generated: {"by": "process:note-ingest", "at": "2026-09-26T13:23:55+00:00"}
sources:
  - id: original-post
    resource: "https://x.com/omarsar0/status/2102579964436680959"
  - id: primary-paper
    resource: "https://arxiv.org/abs/2609.18182"
  - id: shared-figure
    resource: "https://pbs.twimg.com/media/HS3dVYGbkAAYv2a.jpg?name=orig"
---

# WFM: Wiki Foundation Model for Complex Agentic Reasoning

*elvis — @omarsar0*

## TL;DR

- LLM-Wiki treats linked Markdown pages as both dense text and graph structure for agent memory and retrieval.
- WFM uses query-conditioned wiki message passing and reports results on five long-term-memory and multi-hop-reasoning benchmarks.
- The paper also reports a 10.5x distributed-training acceleration; these are author-reported results, not independent validation.

## Highlights

- Paradigm shift from chunk-based RAG and sparse GraphRAG toward an agent-native LLM-Wiki.
- A linked Markdown folder is the target representation for persistent non-parametric agent memory.
- Reported systems contribution: fixed-shape GPU-to-GPU/NCCL boundary exchange to reduce distributed-training overhead.

## Links

- Permalink: [https://x.com/omarsar0/status/2102579964436680959](https://x.com/omarsar0/status/2102579964436680959)
- [https://arxiv.org/abs/2609.18182](https://arxiv.org/abs/2609.18182)
- [https://academy.dair.ai/papers/wfm-wiki-foundation-model-for-complex-agentic-reasoning-2609.18182](https://academy.dair.ai/papers/wfm-wiki-foundation-model-for-complex-agentic-reasoning-2609.18182)
- [https://pbs.twimg.com/media/HS3dVYGbkAAYv2a.jpg?name=orig](https://pbs.twimg.com/media/HS3dVYGbkAAYv2a.jpg?name=orig)

## Raw

- Raw text: [topics/agent_memory/raw/2026-09-23_tweet_wfm-wiki-foundation-model-for-complex-agentic-reasoning.raw.md](https://github.com/cast42/notes/blob/main/topics/agent_memory/raw/2026-09-23_tweet_wfm-wiki-foundation-model-for-complex-agentic-reasoning.raw.md)
- Extractor: fxtwitter+arxiv+image-inspection

## My notes

The useful design claim is representational: a linked Markdown corpus carries
both readable local context and navigable topology. That makes it a plausible
middle ground between chunk-only RAG and sparse graph representations. The
paper's benchmark and systems results still need independent reproduction.

## Related concepts

- [Test-time evolution for agent memory](2026-02-04_x__philschmid_test_time_evolution_agent_memory.md)
- [Awesome AI memory](2026-02-07_github_awesome_ai_memory.md)
