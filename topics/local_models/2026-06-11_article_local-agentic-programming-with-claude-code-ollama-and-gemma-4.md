---
type: article
source_url: "https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4"
canonical_url: "https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4"
title: Local agentic programming with Claude Code, Ollama, and Gemma 4
author: KDnuggets
created_at: 2026-06-11
topics: [local_models]
tags: []
date: 2026-06-11
timestamp: 2026-06-11
resource: "https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4"
---

# Local agentic programming with Claude Code, Ollama, and Gemma 4

*KDnuggets*

## TL;DR

- The article argues that local agentic coding is now practical and cheap if you combine Claude Code with Ollama and Gemma 4 26B MoE, but only if you configure the stack carefully.
- Its biggest operational point is that Ollama’s default 4K context is unusable for agentic coding, so a custom Modelfile with a much larger context window and stricter decoding settings is required.
- The broader claim is that this setup can serve as a private, zero-per-token-cost coding agent for many day-to-day programming tasks, even if frontier cloud models still win on the biggest reasoning jobs.

## Highlights

- "The Modelfile is not optional."
- Gemma 4 26B MoE is presented as a major jump over Gemma 3 for agentic tool use.
- The article recommends a custom Ollama model variant with 64K context and low temperature for tool-call reliability.
- It stresses that Claude Code should talk to Ollama’s Anthropic-compatible endpoint at http://localhost:11434, not /v1.
- A verification script is included to confirm tool_use output before trusting the stack on real code.

## Links

- Permalink: [https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4](https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4)
- [https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4](https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4)
- [https://ollama.com/](https://ollama.com/)
- [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)

## Raw

- Raw text: [topics/local_models/raw/2026-06-11_article_local-agentic-programming-with-claude-code-ollama-and-gemma-4.raw.md](https://github.com/cast42/notes/blob/main/topics/local_models/raw/2026-06-11_article_local-agentic-programming-with-claude-code-ollama-and-gemma-4.raw.md)
- Extractor: summarize+web-fetch

## My notes
-
