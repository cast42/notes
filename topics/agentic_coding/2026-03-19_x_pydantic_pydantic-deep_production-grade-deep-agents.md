---
title: "Pydantic announces pydantic-deep for production-grade deep agents"
date: 2026-03-19
type: note
topics:
  - agentic_coding
tags:
  - x
  - pydantic
  - agents
  - framework
source: "https://x.com/pydantic/status/2034277533236015441"
---

## TL;DR
Pydantic announced **pydantic-deep**, described as an open-source framework for building production-grade “deep agents” on top of Pydantic AI.

The post positions it as an extension layer around Pydantic AI, with an accompanying article and demo video.

## Key takeaways
- New project name: **pydantic-deep**.
- Positioning: production-grade “deep agents” built on **Pydantic AI**.
- Framing: open-source extension by Vstorm around deeper agent architecture patterns.
- Linked assets include:
  - pydantic.dev article,
  - YouTube demo: “pydantic-deep: Production-Grade Deep Agents for Pydantic AI”.

## Post text
“Meet pydantic-deep, an open-source framework for building production-grade \"deep agents\" on Pydantic AI.”

## Article summary (pydantic.dev)
The linked article presents **pydantic-deep** (guest post by Vstorm) as a production-focused extension to Pydantic AI that implements “deep agent” patterns: multi-step planning, progress tracking, file operations, task delegation, sandboxed code execution, context management, and human approval workflows.

It emphasizes:
- type safety end-to-end (Pydantic models),
- async-first architecture,
- Docker-isolated execution for risky actions,
- HITL approval flow for dangerous tools,
- and a full demo app with multi-user session isolation, WebSocket streaming, uploads, custom tools, and sub-agent delegation.

The positioning is explicitly “same class of capabilities as LangChain deepagents, but in the Pydantic ecosystem with simpler mental models.”

## Links
- Post: https://x.com/pydantic/status/2034277533236015441
- Correct article link: https://pydantic.dev/articles/pydantic-deep-agents
- Demo video (from post): https://www.youtube.com/watch?v=AhV5DqiHn7E
