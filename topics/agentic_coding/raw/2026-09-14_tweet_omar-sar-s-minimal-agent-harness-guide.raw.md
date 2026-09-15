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
content_hash: "789c38f1b1aa1599306e608aa3c7787d8ec1a94c19e20d5b2cf671bced957478"
extracted_at: "2026-09-15T06:35:29+00:00"
extractor: "fxtwitter+arxiv-api"
---

# Raw content

Source: https://x.com/omarsar0/status/2099545598156288292


## X post capture

URL: https://x.com/omarsar0/status/2099545598156288292
Author: Omar Sar (@omarsar0)
Published: 2026-09-14T17:07:32Z

Post text:
On building an agent harness from scratch.

Got so many questions about where to get started.

My short guide (feed it to your agent):

If you really want to learn harnesses well, it's worth building one from scratch using a programming language (TypeScript or Python) of your choice.

When I got started, I implemented my first harness using ReAct from Google: https://academy.dair.ai/papers/react-synergizing-reasoning-and-acting-in-language-models-2210.03629

At the time, I built this from scratch, but you can easily prompt your agent to consume the paper and produce a minimal implementation you can inspect and understand.

You want to target having three parts:

- an LLM module for all things inference, and it should ideally support several models. I used OpenRouter when I got started. This can include the system prompt, but you can also separate it out if you plan to explore context-engineering ideas more deeply.

- a tools module (I recommend building them as MCP tools for interoperability, but you can design functions from scratch if you have experience).

- an agent loop that encapsulates the tools and LLM. ReAct is one of the more basic loops you can implement.

Primarily, aim to understand the main components and how they work with each other.

Pro tips:

- try to keep your system prompt minimal and experiment with different models; a mini version of all frontier lab models should be good enough to get you started.

- look at the code and log things as you experiment with different tasks. You want to log inputs/outputs to the loop, inputs/outputs from LLMs, and inputs/outputs from tool calls as a starting point.  Set up a simple set of diverse tasks to test your agent loop on. So with every change, you can run the tasks and inspect the results manually.

Once you have a good grasp of this, you can easily add other things like skills, memory, etc., once you have a good idea of how to tune them. It helps to keep things modular if you are planning for this. I would recommend playing with memory, skill, and subagent as good next steps.

If you don't want to build the components or want to start building a more serious agent harness, I recommend using the Pi SDK or LangChain harness tools. I am also going to release something soon to help with this.

Let me know if you have questions. I am planning a longer write-up on this, but this should be enough to give you something to experiment with.

Media:
- photo: https://pbs.twimg.com/media/HSMVlsrWcAAHc0Z.jpg?name=orig (2546x1684)

## Linked ReAct paper metadata capture

URL: https://arxiv.org/abs/2210.03629
Title: ReAct: Synergizing Reasoning and Acting in Language Models
Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao
Version checked: arXiv v3, revised 2023-03-10; the paper is the ICLR 2023 camera-ready version.

Abstract, transcribed from the arXiv abstract page:

While large language models have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (for example, chain-of-thought prompting) and acting (for example, action plan generation) have primarily been studied as separate topics. ReAct explores generating reasoning traces and task-specific actions in an interleaved manner. Reasoning traces help the model induce, track, and update action plans and handle exceptions, while actions allow it to interface with external sources such as knowledge bases or environments to gather additional information. The paper reports results across language and decision-making tasks, including improvements over baselines and improved human interpretability and trustworthiness over methods without reasoning or acting components.
