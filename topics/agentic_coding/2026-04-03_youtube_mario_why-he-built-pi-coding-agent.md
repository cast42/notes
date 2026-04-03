---
title: "Why Mario built Pi: a minimal, extensible coding agent harness"
date: 2026-04-03
type: note
topics:
  - agentic_coding
tags:
  - youtube
  - coding_agents
  - pi
  - open_source
  - context_engineering
source: "https://youtu.be/Dli5slNaJu0?is=wAWHbyCHnyEpDDAd"
---

## TL;DR
Mario explains why he became dissatisfied with existing coding harnesses like Claude Code and OpenCode, then built **Pi** as a deliberately minimal, extensible alternative.

The core thesis: most harnesses are overbuilt, insufficiently observable, and too rigid. Better to strip the system down to a tiny core, expose everything, and let developers customize the rest.

## Key takeaways
- Existing agent harnesses often optimize for feature sprawl rather than control and observability.
- The most important missing primitive is good **context management / compaction**, not more built-in features.
- Many popular built-ins (LSP-on-every-edit, opaque sub-agents, approval spam, server complexity) may actively degrade outcomes.
- Pi’s design philosophy is minimal core + maximum extensibility.
- Open-source coding-agent projects are being strained by low-quality AI-driven PR/issue spam.

## Summary
Mario sketches the recent history of coding agents: copy-paste ChatGPT, early GitHub Copilot, Aider/AutoGPT, then the big step-change with Claude Code’s ad hoc codebase exploration via bash/file tools. He credits Claude Code with making agentic coding actually work at scale, but argues it drifted into a “spaceship” product: too many features, too little observability, unstable workflows, and not enough user control.

He then critiques several alternatives. Claude Code is praised for model quality but criticized for poor context management, UI instability, limited extensibility, and over-evolving behavior that breaks stable workflows. OpenCode is described as pragmatic and grounded, but flawed by bad prompt-cache interactions, over-eager LSP feedback during incomplete edits, architecture decisions that reduce trust, and a server model that introduced security concerns. Commercial tools like Amp are respected, but rejected for limiting model/control choices.

From there he introduces **Pi**, built around a simple principle: adapt the coding agent to your needs, not the other way around. Pi has a small system prompt, only four built-in tools (`read`, `write`, `edit`, `bash`), YOLO-by-default philosophy, and explicit rejection of many mainstream features as defaults: no built-in MCP, sub-agents, plan UI, background bash, or todos. Instead, it expects users to use markdown plans, tmux, extensions, skills, and custom tools.

The main argument is that coding-agent design is still in the “messing around and finding out” phase, and we need systems that are easier to modify than to admire. Pi therefore exposes hooks for custom tools, custom UI, custom compaction, permission gates, provider integrations, SSH-backed file tools, HTML/JSON exports, and tree-structured sessions. This makes it possible to prototype workflows quickly and treat the harness itself as editable infrastructure.

He also uses **Terminal Bench** as evidence that highly capable results can come from extremely minimal interfaces—suggesting that many harness features may be unnecessary for strong performance. Pi is presented as proof that a small, hackable architecture can still benchmark near the top while staying understandable.

The talk closes on a strong open-source warning: AI-assisted spam PRs/issues are degrading OSS collaboration. Mario describes countermeasures like “OSS vacation,” strict human verification, and vouch-style access control before contributions are accepted.

## Memorable arguments
- “We are in the messing around and finding out stage.”
- The right time for linting/type-checking feedback is when the agent believes it is done, not during every intermediate edit.
- Approval prompts are not a real safety model; they mainly train users to hit Enter.
- Containerization is a better base than dialog spam, but still not a full answer to exfiltration/prompt injection.

## Links
- Video: https://youtu.be/Dli5slNaJu0?is=wAWHbyCHnyEpDDAd
- Pi: https://pi.dev
