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
description: "Source capture for the X post and its linked WFM paper about agent memory over linked Markdown wikis."
generated: {"by": "process:note-ingest", "at": "2026-09-26T13:23:55+00:00"}
sources:
  - id: original-post
    resource: "https://x.com/omarsar0/status/2102579964436680959"
  - id: primary-paper
    resource: "https://arxiv.org/abs/2609.18182"
  - id: shared-figure
    resource: "https://pbs.twimg.com/media/HS3dVYGbkAAYv2a.jpg?name=orig"
content_hash: "9a49276c9b25dee04445bb406c65cdad8362c7bd967bcc2fa0436a77a31b92b1"
extracted_at: "2026-09-26T13:23:55+00:00"
extractor: "fxtwitter+arxiv+image-inspection"
---

# Raw content

## X post — extracted text

Interesting paper on agent memory stored as a linked markdown wiki.

Lots of great ideas and insights if you work with LLM Wikis.

Wikis are useful for agents because each page holds dense text and the links between pages hold structure. WFM is a Wiki Foundation Model trained to use both at once.

It turns an LLM Wiki into a graph and retrieves from it with message passing conditioned on the query, so the text of each page and the link structure shape the result together.

The team also built a GPU-to-GPU training protocol that trains 10.5x faster, and reports strong results on five agent memory and multi-hop reasoning benchmarks.

If your agent's long-term memory is a folder of linked markdown files, WFM is designed for that format.

Paper: https://arxiv.org/abs/2609.18182

Chat with Paper: https://academy.dair.ai/papers/wfm-wiki-foundation-model-for-complex-agentic-reasoning-2609.18182

## Source metadata

- Post: https://x.com/omarsar0/status/2102579964436680959
- Author: elvis (`@omarsar0`)
- Published: 2026-09-23
- Linked paper: *WFM: Wiki Foundation Model for Complex Agentic Reasoning*
- Paper authors: Junnan Dong, Linhao Luo, Senlei Zhang, Gong Chen, Taian Guo, Yifei Yu, Rong Tao, Tao Guo, Qian-Wen Zhang, Siyu An, Ruizhi Qiao, Xing Sun
- arXiv submission: 2026-09-16, version 1

## Shared image

The image is the first page of the linked paper. Its overview figure contrasts three representations:

1. Classic chunk-based RAG: text is split into fragments and retrieved fragments can lose contextual links.
2. GraphRAG: graph construction exposes connections for structured reasoning, but sparse structures can strip away dense textual semantics.
3. LLM-Wiki: an agent-native representation combining macro Markdown structures, dense text sources, and fine-grained entity topologies.

The page also shows the paper's abstract and identifies the proposed Wiki Foundation Model, query-conditioned attentive aggregation for wiki message passing, and an NCCL GPU-to-GPU boundary-exchange protocol.

## Primary-source notes

The arXiv abstract describes WFM as a model for persistent non-parametric knowledge used in long-term memory and retrieval-augmented generation. The paper claims evaluations on five long-term agent-memory and multi-hop-reasoning benchmarks, together with a reported 10.5x training acceleration on distributed clusters. These are paper-reported results, not independent validation.

Primary source: https://arxiv.org/abs/2609.18182
Image source: https://pbs.twimg.com/media/HS3dVYGbkAAYv2a.jpg?name=orig
