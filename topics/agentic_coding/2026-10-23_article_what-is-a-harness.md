---
type: "article"
source_url: "https://x.com/theo/status/2113424203345265053"
canonical_url: "https://x.com/i/article/2113408019619028992"
title: "What is a harness?"
author: "Theo"
handle: "theo"
created_at: "2026-10-23"
date: "2026-10-23"
topics: ["agentic_coding"]
tags: [agent-harness, tool-calling, runtime-architecture, model-context-protocol]
resource: "https://x.com/i/article/2113408019619028992"
description: "Theo explains an agent harness as the runtime that connects an LLM to tools, executes model requests, and returns observations, while distinguishing that runtime from the user interface that may package it."
generated: {"by": "process:note-ingest", "at": "2026-10-23T07:13:31+00:00"}
sources:
  - id: "announcement-post"
    resource: "https://x.com/theo/status/2113424203345265053"
  - id: "article"
    resource: "https://x.com/i/article/2113408019619028992"
  - id: "mcp-server-primitives"
    resource: "https://py.sdk.modelcontextprotocol.io/servers/"
---

# What is a harness?

*Theo — @theo*

## TL;DR

- A harness is the runtime around an LLM that exposes tools, interprets tool calls, executes them, and feeds results back.
- Separate the human-facing interface from the runtime conceptually, even when a product bundles them together.
- Treat the chef/kitchen/restaurant metaphor as a useful model, not a universal definition; MCP is a protocol with tools, resources, and prompts.

## Highlights

- **LLM:** generates text, including structured requests for actions.
- **Harness:** makes tools and their descriptions available, interprets tool requests, executes them, and returns results for the next model turn.
- **Interface:** the terminal, app, or website through which a person interacts. Products often bundle interface and harness, even though they are distinct roles in the architecture.
- **Agent:** Theo’s shorthand is an LLM combined with a harness; changing tools, instructions, or other runtime configuration can change the resulting agent.
- **T3 Code:** presented as an application that can provide extra capabilities to a harness rather than replacing it.

## The kitchen analogy—and where it stops

Think of the LLM as the chef and the harness as the kitchen: the chef can propose an action, but the kitchen supplies the equipment and translates that request into an operation. In Theo’s analogy, T3 Code is more like a restaurant or cookbook that can supply extra capabilities to kitchens people choose to use.

This is a compact teaching model, not a universal taxonomy. “Harness” is also used more broadly for orchestration, context management, permissions, and other runtime behavior; in shipped products, interface and harness boundaries can be embedded together.

MCP is one way for an application to connect to external capabilities. Theo compresses it into an analogy of recipes or remote services, but MCP servers can expose tools, resources, and prompts through a client-server protocol; it is more than a generic API URL. [The MCP server overview](https://py.sdk.modelcontextprotocol.io/servers/) documents these primitives.

## Links

- Permalink: [https://x.com/i/article/2113408019619028992](https://x.com/i/article/2113408019619028992)
- [https://modelcontextprotocol.io/specification/draft/server/index](https://modelcontextprotocol.io/specification/draft/server/index)
- [https://github.com/pingdotgg/t3code](https://github.com/pingdotgg/t3code)
- [2026-06-22_article_write-a-coding-agent-from-first-principles.md](2026-06-22_article_write-a-coding-agent-from-first-principles.md)
- [2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.md](2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.md)
- [MCP server primitives: tools, resources, and prompts](https://py.sdk.modelcontextprotocol.io/servers/)

## Raw

- Raw text: [topics/agentic_coding/raw/2026-10-23_article_what-is-a-harness.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-10-23_article_what-is-a-harness.raw.md)
- Extractor: FxTwitter API article payload; paraphrased, checked against official MCP docs

## My notes

The most useful distinction is between **the model’s ability to request an action** and **the host runtime’s responsibility to make it happen**. A product label such as “coding agent” can hide both the model and harness, so comparing agents is clearer when you name the model, runtime, available tools, and configuration separately.
