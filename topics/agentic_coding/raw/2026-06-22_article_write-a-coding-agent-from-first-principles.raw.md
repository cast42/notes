---
type: article
source_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles"
canonical_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles"
title: Write a coding agent from first principles
author: mathspp
created_at: 2026-06-22
topics: [agentic_coding]
content_hash: 2d39cca3decf28ad4224fd8463fcbdbd853e58635be64a02c2e782d0e7c299a0
extracted_at: "2026-07-15T14:50:32"
extractor: web-fetch+manual-focus
date: 2026-06-22
timestamp: 2026-06-22
resource: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles"
---

# Raw content

Source: https://mathspp.com/blog/write-a-coding-agent-from-first-principles


URL: https://mathspp.com/blog/write-a-coding-agent-from-first-principles
Title: Write a coding agent from first principles
Author: mathspp
Requested note date: 2026-06-22

Focused extraction:
- The tutorial explains a coding agent from first principles by building one step by step in Python.
- It frames an agent as an LLM plus extra functionality that lets it interact with its environment.
- Early sections cover basic message sending, conversation context, user commands, and why the full transcript must be resent on each request.
- The core conceptual move is that tools turn a plain chat loop into an agent: the model is instructed to emit tool-call syntax, the host program executes the tool, and the result is fed back into context.
- The tutorial uses a simple file-reading tool to show the full loop: tool instructions, tool-call detection, parsing, execution, and reinsertion of results as user messages.
- It is useful not because it is the most production-grade coding agent design, but because it exposes the mechanics cleanly enough that the abstractions in more advanced harnesses become legible.

Notable details:
- Uses Python, uv, python-dotenv, and the Anthropic SDK.
- Emphasizes context management as half the battle in getting good results from agents.
- Shows how custom user commands like /help and /exit can be intercepted before model calls.
- Treats tools as explicit host-side functions rather than magic model capabilities.
