---
type: "source"
source_url: "https://x.com/theo/status/2113424203345265053"
canonical_url: "https://x.com/i/article/2113408019619028992"
title: "What is a harness?"
author: "Theo"
handle: "theo"
created_at: "2026-10-23"
date: "2026-10-23"
topics: ["agentic_coding"]
tags: [agent-harness, tool-calling, runtime-architecture]
resource: "https://x.com/i/article/2113408019619028992"
generated: {"by": "process:note-ingest", "at": "2026-10-23T07:13:31+00:00"}
sources:
  - id: "announcement-post"
    resource: "https://x.com/theo/status/2113424203345265053"
  - id: "article"
    resource: "https://x.com/i/article/2113408019619028992"
  - id: "mcp-server-primitives"
    resource: "https://py.sdk.modelcontextprotocol.io/servers/"
content_hash: "75723a3e9691906d15b804f73d7cb131de6a89549256b6ec4926ad6d5d02c241"
extracted_at: "2026-10-23T07:13:31+00:00"
extractor: "FxTwitter API article payload; paraphrased, checked against official MCP docs"
---

# Raw content

Source: https://x.com/i/article/2113408019619028992


This is a paraphrased extraction of Theo's X article, not a verbatim transcript.

## Basic model

People use computers through interfaces such as terminals, websites, or apps. An LLM, by contrast, produces text. To make it act on a computer, a runtime must expose available tools and their descriptions, give the model a format for requesting them, recognize those requests, execute the corresponding operations, and return results to the model. Theo calls that execution system the harness.

## Interface and harness

The human-facing interface and the agent runtime are conceptually different, even when one product packages them together. Theo describes the Claude Code and Codex products as including both a UI and an underlying SDK/server runtime. Other applications can embed those runtimes; the post gives Grok Bot using Cursor's harness and T3 Code using Anthropic's Agent SDK or Codex App Server as examples. Pi is given as an example of a runtime used within OpenClaw.

## Tools and MCP

The harness owns or connects to tools and mediates their availability to both the model and the interface. MCP provides a standard client-server protocol for connecting an application to external capabilities. The article's kitchen analogy treats direct tools as kitchen equipment and MCP integrations as recipes or remote services that a harness can invoke. MCP's actual protocol has more structure: its servers can expose tools, resources, and prompts, so it is not merely a generic API URL.

## T3 Code analogy

Theo says T3 Code is not itself a harness: it is more like a restaurant whose users bring a kitchen/runtime. It can provide extra capabilities through MCP while leaving the chosen harness in control. The model is the chef, the harness the kitchen, and T3 Code the restaurant/cookbook.

## Definition and limits

Theo's concise formula is that an agent is an LLM combined with a harness. This is useful as an operational model for tool-using agents, but terminology is not universal: authors may use “harness” more broadly to include orchestration, context management, instructions, permissions, and user experience. The interface/runtime boundary is often a packaging boundary, not a strict product boundary.
