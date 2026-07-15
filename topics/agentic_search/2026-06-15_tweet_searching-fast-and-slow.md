---
type: tweet
source_url: "https://x.com/i/status/2065423284343050314"
canonical_url: "https://x.com/barrowjoseph/status/2065423284343050314"
title: Searching, Fast and Slow
author: Joe Barrow
handle: barrowjoseph
created_at: 2026-06-15
topics: [agentic_search]
tags:
  - search-agents
  - dual-process-search
  - exploration-exploitation
  - query-planning
  - information-retrieval
date: 2026-06-15
timestamp: 2026-06-15
resource: "https://x.com/barrowjoseph/status/2065423284343050314"
---

# Searching, Fast and Slow

*Joe Barrow — @barrowjoseph*

## TL;DR

- Joe Barrow revisits the old "Slow Search" idea in the context of agentic retrieval, arguing that agents can often benefit from slower, higher-quality search because whole-task performance matters more than per-query latency.
- The post distinguishes per-query latency from throughput and total task time, suggesting that better retrieval can reduce the number of tool calls and LLM steps even if each search is slower.
- A broader implication is that search systems for agents may need to optimize for recall, quality, and throughput rather than copying human-search assumptions about instant responses.

## Highlights

- "Are you willing to wait even longer for better search results? Maybe not. But an agent is, and that can actually speed up agentic search."
- The post frames agentic retrieval as a trade of wall-clock time for recall, then asks why we should not lean further into that trade when the immediate consumer is a model, not a human.
- It contrasts two views: latency matters less because agents can wait, versus latency and scalability still matter because agents will issue many more queries than humans.
- The argument is that for many agentic tasks, both time and cost are dominated more by LLM tool-calling loops than by raw retrieval latency.
- The piece calls for more slow-search research specifically tuned to agent workloads.

## Links

- Permalink: [https://x.com/barrowjoseph/status/2065423284343050314](https://x.com/barrowjoseph/status/2065423284343050314)
- [https://x.com/barrowjoseph/status/2065423284343050314](https://x.com/barrowjoseph/status/2065423284343050314)

## Raw

- Raw text: [topics/agentic_search/raw/2026-06-15_tweet_searching-fast-and-slow.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_search/raw/2026-06-15_tweet_searching-fast-and-slow.raw.md)
- Extractor: fxtwitter

## My notes
-
