---
title: "pstack-claude: porting pstack across coding-agent harnesses"
date: 2026-10-15
type: software
topics:
  - agentic_coding
tags:
  - agent-skills
  - coding-agent-harnesses
  - workflow-routing
  - software-verification
resource: "https://github.com/michael-denyer/pstack-claude"
description: "Michael Denyer's pstack-claude adapts Lauren Tan's Cursor workflow stack for several agent harnesses, illustrating both the portability of skill content and the harness-specific work needed for routing and tools."
author: "Michael Denyer"
generated:
  by: "process:codex"
  at: "2026-10-16T18:49:00+02:00"
sources:
  - id: "x-post"
    resource: "https://x.com/LLMpsycho/status/2110637801272439262"
  - id: "pstack-claude-repository"
    resource: "https://github.com/michael-denyer/pstack-claude"
  - id: "upstream-pstack"
    resource: "https://github.com/cursor/plugins/tree/main/pstack"
---

# pstack-claude: porting pstack across coding-agent harnesses

## TL;DR

- [Michael Denyer's pstack-claude](https://github.com/michael-denyer/pstack-claude) adapts Lauren Tan's pstack playbooks and principle skills for Claude Code, Codex, Pi, GitHub Copilot, OpenCode, Gemini CLI, and Prime Agent.
- The project presents itself as an upstream-tracking port, with named policy forks. Its central promise is to carry workflow content across harnesses while adding integration-specific routing, setup, and tools where supported.
- The useful distinction is **portable workflow vs. harness integration**: skills can be shared, but routing hooks, model setup, subagent APIs, and install paths differ by runtime. This is a separate community project, not the official Cursor plugin.

## Highlights

- In the linked post, Bessi S describes the project as a port of poteto's pstack and says it brings the principle skills and `poteto-mode` workflows from Cursor to several other coding-agent environments.
- The repository README says the port tracks upstream and keeps named policy forks. Its stated purpose is to help agents route a goal to a suitable workflow and keep changes concise and verified.
- Integration is not uniform. The README documents routing hooks for Claude Code, Codex, and GitHub Copilot; Pi injects a routing instruction through an extension. Some other environments use shared skill files without a routing hook, so users must invoke `poteto-mode` or add a standing instruction.
- Pi's package includes an extension supplying subagent, question, and wake-up tools used by the skills. The README also documents runtime-specific setup, model selection, and version caveats—for example, a Copilot CLI behavior observed on versions 1.0.87–1.0.92.
- The project says it has no server or telemetry; however, content the skills ask an agent to read (including transcripts) is still sent to that agent's model provider. That is an important data-flow distinction.

## What to take from it

This is a concrete portability experiment around the original pstack: the reusable part is the playbook and principle content, while reliable operation depends on adapters for each harness's hooks, commands, tools, and model configuration. When evaluating or borrowing it, inspect the target harness's integration path and current compatibility notes rather than assuming that installing a skill directory reproduces the full Cursor experience.

The README describes intended behavior and supported setup paths; this note does not independently test the integrations or verify the post's engagement figures. Check the live repository documentation before installing because support and version constraints can change.

## Related concepts

- [pstack: Lauren Tan's engineering skills for coding agents](2026-10-05_github_cursor_pstack_skills_by_lauren-tan.md) — the upstream Cursor stack this project adapts.
- [Lauren Tan on pstack, verification, and agent workflows](2026-09-21_video_lauren-tan-pstack-verification-and-agent-workflows.md) — broader context on the workflow principles.

## Sources

- [Bessi S's X post](https://x.com/LLMpsycho/status/2110637801272439262)
- [pstack-claude repository and installation documentation](https://github.com/michael-denyer/pstack-claude)
- [Original Cursor pstack plugin](https://github.com/cursor/plugins/tree/main/pstack)

Raw capture: [post and repository page text](raw/2026-10-15_github_michael-denyer_pstack-across-harnesses.raw.md).
