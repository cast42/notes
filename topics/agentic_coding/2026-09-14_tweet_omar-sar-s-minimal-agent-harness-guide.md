---
type: "tweet"
source_url: "https://x.com/omarsar0/status/2099545598156288292"
canonical_url: "https://x.com/omarsar0/status/2099545598156288292"
title: "Omar Sar’s minimal agent harness guide"
author: "Omar Sar"
handle: "omarsar0"
created_at: "2026-09-14"
date: "2026-09-14"
topics: ["agentic_coding"]
tags: [agent-harness, react-loop, tool-use, observability, modular-design]
resource: "https://x.com/omarsar0/status/2099545598156288292"
generated: {"by": "process:note-ingest", "at": "2026-09-15T06:35:29+00:00"}
sources: [{"id": "original", "resource": "https://x.com/omarsar0/status/2099545598156288292"}, {"id": "react-paper", "resource": "https://arxiv.org/abs/2210.03629"}]
description: "Omar Sar’s minimal learning path for building an agent harness from an LLM module, tools, and an observable ReAct-style loop."
---

# Omar Sar’s minimal agent harness guide

*Omar Sar — @omarsar0*

## TL;DR

- Build a small harness from scratch in Python or TypeScript to understand the architecture before adopting a larger framework.
- Start with three modules: multi-model LLM access, interoperable tools, and an agent loop such as ReAct.
- Make the loop observable with input/output logs and a diverse task set, then add skills, memory, and subagents incrementally.
- The guide is a learning path and experimental scaffold, not a complete production harness specification.

## Highlights

- The LLM module should ideally support several models; the post mentions OpenRouter as one starting point.
- The tools module can use MCP for interoperability, while the loop coordinates the LLM and tools.
- ReAct interleaves thought, action, and observation so external results update the next reasoning step.
- Manual inspection of logs across repeated, diverse tasks provides the first evaluation loop for changes to the harness.
- Pi SDK or LangChain are suggested once the goal shifts from learning the components to building a more serious harness.

## A minimal harness architecture

Sar’s advice is to build the smallest understandable system first, using Python or TypeScript:

1. **LLM module:** isolate inference and support several model providers or models. Keep the system prompt separable if experimenting with context engineering.
2. **Tools module:** expose actions the model can invoke. MCP is recommended for interoperability, although ordinary functions are enough for a first implementation.
3. **Agent loop:** coordinate the LLM and tools. A ReAct loop interleaves a thought, an action, and an observation, using the returned observation as context for the next step.

The learning objective is architectural understanding: see how the three pieces exchange inputs and outputs before adding abstractions. Sar recommends a minimal system prompt, experiments across several models, logs for loop/LLM/tool inputs and outputs, and a small diverse task set that can be rerun after every change.

## Build outward in stages

Once the loop is understood and observable, add skills, memory, and subagents as modular extensions. This sequence keeps the source of a behaviour visible: first the model, tools, and loop; later the durable context, reusable procedures, and delegated work. For a more serious application, Sar points to the Pi SDK or LangChain rather than treating a hand-built prototype as production infrastructure.

## Limits and interpretation

This is a learning path, not a complete production-harness design. It does not specify authentication, permissions, retries, cancellation, concurrency, context compaction, persistence, cost controls, or automated evaluation in depth. “Manual inspection” is a useful first feedback loop, but dependable systems need stronger repeatable tests and explicit safety boundaries as their capabilities grow.

The attached screenshot presents the ReAct loop as thought → action → observation → new context. The underlying ReAct paper reports that interleaving reasoning traces with actions can help update plans, handle exceptions, and gather information from external environments; the screenshot and the post are an accessible entry point, not a substitute for the paper’s task-specific evidence.

## Related concepts

- [Write a coding agent from first principles](2026-06-22_article_write-a-coding-agent-from-first-principles.md) — Minimal agent mechanics and the controls that make a harness dependable.
- [Why Mario built Pi](2026-04-03_youtube_mario_why-he-built-pi-coding-agent.md) — A minimal, extensible coding-agent harness as a practical counterpoint.
- [Agent Skills with Anthropic course](2026-07-15_tweet_agent-skills-with-anthropic-deeplearning-ai-course.md) — Skills as modular procedure bundles added after the core agent loop.

## Links

- Permalink: [https://x.com/omarsar0/status/2099545598156288292](https://x.com/omarsar0/status/2099545598156288292)
- [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
- [https://github.com/cast42/notes/blob/main/topics/agentic_coding/2026-06-22_article_write-a-coding-agent-from-first-principles.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/2026-06-22_article_write-a-coding-agent-from-first-principles.md)
- [https://github.com/cast42/notes/blob/main/topics/agentic_coding/2026-04-03_youtube_mario_why-he-built-pi-coding-agent.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/2026-04-03_youtube_mario_why-he-built-pi-coding-agent.md)
- [https://pbs.twimg.com/media/HSMVlsrWcAAHc0Z.jpg?name=orig](https://pbs.twimg.com/media/HSMVlsrWcAAHc0Z.jpg?name=orig)

## Raw

- Raw text: [topics/agentic_coding/raw/2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.raw.md)
- Extractor: fxtwitter+arxiv-api

## My notes

- The most useful design principle is **make the loop legible before making it powerful**: observability and a small rerunnable task set turn architecture changes into inspectable experiments.
