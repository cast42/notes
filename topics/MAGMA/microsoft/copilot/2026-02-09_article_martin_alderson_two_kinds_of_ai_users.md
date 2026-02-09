---
title: "Two kinds of AI users are emerging (and why M365 Copilot is a problem)"
date: 2026-02-09
type: note
topics:
  - MAGMA
tags:
  - microsoft
  - copilot
  - enterprise
  - productivity
  - agents
source:
  kind: article
  url: https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/
---

# Two kinds of AI users are emerging (and why M365 Copilot is a problem)

## TL;DR
Martin Alderson describes a widening gap between **“power users”** (agentic tooling, CLI agents, scripts, APIs) and **“chat users”** (mostly ChatGPT-style chat). He argues **M365 Copilot** is often the only allowed enterprise AI tool, but is *so underpowered* that it risks making leadership conclude “AI doesn’t work”.

## Takeaways
- **Two user archetypes**
  - *Power users*: use agentic tooling (Claude Code, skills/MCP, scripting). Often *not* traditional engineers; e.g. finance roles getting huge leverage once they can use Python.
  - *Chat-only users*: mostly prompt/response in a chat UI.

- **Copilot as an enterprise bottleneck**
  - Bundling → huge footprint, but (author claims) the experience resembles a weak chat UI.
  - If Copilot is the only approved tool, it sets the ceiling for what employees can do.

- **Why enterprises are vulnerable**
  - Locked-down endpoints: can’t run scripts/tools locally.
  - Legacy systems: no internal APIs, so agents have nothing to connect to.
  - Siloed/outsourced engineering: little capability to build safe agent infrastructure.

- **The emerging advantage of smaller companies**
  - Fewer constraints + more API-first tooling → small teams can build AI-assisted workflows quickly.

- **Security framing**
  - The author acknowledges real risk of “YOLO agents” on production systems.
  - Suggestion: a **hosted VM / sandboxed environment** with thoughtful restrictions, especially for read-only/reporting workflows.

## Why this matters for coaching
If you’re coaching teams/leaders:
- Diagnose whether the org is *actually* enabling “power user” workflows (scripts + APIs + sandboxes), or only permitting chat.
- Don’t let a weak tooling rollout poison the broader judgment about AI capability.
- Treat “internal APIs + safe sandboxes” as a core enabler, not an afterthought.

## Links
- Article: <https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/>
