---
title: "Raw capture: pstack-claude across agent harnesses"
date: 2026-10-15
type: source
topics:
  - agentic_coding
tags:
  - pstack
  - coding-agent-harnesses
resource: "https://github.com/michael-denyer/pstack-claude"
sources:
  - id: "x-post"
    resource: "https://x.com/LLMpsycho/status/2110637801272439262"
  - id: "repository-readme"
    resource: "https://github.com/michael-denyer/pstack-claude"
generated:
  by: "process:codex"
  at: "2026-10-16T18:49:00+02:00"
extractor: "FxTwitter API and GitHub page text extraction"
---

# Raw content

## X post by Bessi S (@LLMpsycho)

Published 2026-10-15.

> pstack-claude is a port of poteto's pstack for Claude Code, Codex, Pi, Copilot and OpenCode. It brings the principle skills and poteto-mode workflows over from Cursor. 2,027 stars.
>
> https://github.com/michael-denyer/pstack-claude

The post's link card described the repository as agent versions of Poteto's pstack, with rigorous workflows translating Cursor primitives for other harnesses. The post's star count is time-specific and not a current count.

## Repository page text captured 2026-10-16

The README describes Lauren Tan's pstack as an opinionated Cursor skill stack and this repository as a port for Claude Code, Codex, Pi, GitHub Copilot, and other agent harnesses. It says the port tracks upstream and carries named policy forks declared in `tools/forks.json`.

It says `poteto-mode` accepts a goal and selects an appropriate workflow, with the goal of concise, simple, verified code. Installation instructions are provided for Claude Code, Codex, Pi, and Copilot. For OpenCode, Gemini CLI, Prime Agent, and skills-only Codex use, it describes linking skills into `~/.agents/skills/`; these installations have no routing hook, so the user must request `poteto-mode` by name or add a standing instruction.

The README describes runtime-specific behavior:

- Claude Code, Codex, and GitHub Copilot have a routing hook; Codex asks the user to trust it through `/hooks` before it runs.
- On Pi, an extension injects the routing instruction and adds subagent, question, and wake-up tools used by the skills, along with `/loop` and the routing instruction.
- Copilot setup includes model selection and reuse of that choice across sessions. The README documents tested Copilot CLI versions 1.0.87–1.0.92 and a session-listing/skill-discovery issue in version 1.0.92, while saying interactive sessions, hooks, and agents are unaffected.
- `setup-pstack` can configure model defaults, reasoning effort by role, and automatic routing.

The README describes playbooks for bugs, planning, features, refactoring, performance, investigations, prototypes, PR maintenance, shipping, and longer projects. Its bug-fix example reproduces a failure, investigates, delegates a fix, and reruns the failing case; it says architect is consulted when a fix crosses a function boundary.

The repository states that pstack has no server or telemetry. It also notes that material its skills ask the agent to read—including session transcripts—is sent to the model provider, scripts run locally, and PR tools use the user's GitHub CLI login.

The page identifies the port as MIT-licensed and distinguishes it from upstream Cursor material, which has separate license files and notices. It invites bug reports, documentation fixes, and runtime improvements.
