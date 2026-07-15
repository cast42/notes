---
type: article
source_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles"
canonical_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles"
title: Write a coding agent from first principles
author: mathspp
created_at: 2026-06-22
topics: [agentic_coding]
tags: []
---

# Write a coding agent from first principles

*mathspp*

## TL;DR

- This tutorial is a clear from-first-principles walkthrough of how a coding agent actually works: an LLM, a running conversation context, and host-side tools that let the model interact with files and other parts of its environment.
- Its biggest value is pedagogical clarity: it decomposes agent behavior into understandable mechanics like context replay, command handling, tool-call syntax, tool execution, and reinserting results into the conversation.
- The result is a useful mental model for understanding more advanced coding harnesses, even if the example agent itself is intentionally simple.

## Highlights

- A coding agent is framed as an LLM extended with tools that let it interact with its environment.
- The tutorial makes the usually hidden mechanics visible: full context replay, assistant/user role separation, command interception, and tool-call parsing.
- The file-reading tool is the key conceptual bridge from plain chatbot to actual agent.
- Context management is treated as central rather than incidental.
- The post is best read as a systems-clarity piece, not just a coding recipe.

## Links

- Permalink: [https://mathspp.com/blog/write-a-coding-agent-from-first-principles](https://mathspp.com/blog/write-a-coding-agent-from-first-principles)
- [https://mathspp.com/blog/write-a-coding-agent-from-first-principles](https://mathspp.com/blog/write-a-coding-agent-from-first-principles)
- [https://github.com/mathspp/coding-agent-tutorial](https://github.com/mathspp/coding-agent-tutorial)

## Raw

- Raw text: [topics/agentic_coding/raw/2026-06-22_article_write-a-coding-agent-from-first-principles.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-06-22_article_write-a-coding-agent-from-first-principles.raw.md)
- Extractor: web-fetch+manual-focus

## My notes
-
