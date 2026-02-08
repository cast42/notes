---
title: "Claude Code: agentic search > RAG + local vector DB (Boris Cherny)"
date: 2026-02-01
type: note
topics:
  - agentic_coding
tags:
  - rag
  - search
  - claude
  - security
  - privacy
people:
  - Boris Cherny
source:
  kind: x
  url: https://x.com/bcherny/status/2017824286489383315
---

# Claude Code: agentic search > RAG + local vector DB (Boris Cherny)

## TL;DR
Boris Cherny says early Claude Code versions used **RAG + a local vector database**, but they quickly found **agentic search** works better.
He highlights the pragmatic benefits: simpler, and fewer issues around **security, privacy, staleness, and reliability**.

## Takeaways
- “RAG + local vector DB” isn’t automatically the best default for coding agents.
- Agentic search can be better because it:
  - stays closer to the live repo state (less staleness)
  - reduces a whole class of vector-store lifecycle problems (indexing, sync, corruption)
  - avoids sensitive-data questions around storing embeddings/derived data
- This matches a pattern we’ve seen elsewhere: for code, **the filesystem + deterministic tools** often beat fancy retrieval.

## Details (verbatim)
> 👋 Early versions of Claude Code used RAG + a local vector db, but we found pretty quickly that agentic search generally works better. It is also simpler and doesn’t have the same issues around security, privacy, staleness, and reliability.

## Figure
Screenshot to add (pending your next message).

## Links
- X post: <https://x.com/bcherny/status/2017824286489383315>
