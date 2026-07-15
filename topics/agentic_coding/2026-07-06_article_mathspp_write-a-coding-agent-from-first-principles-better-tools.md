---
title: "Write a coding agent from first principles: better tools"
date: 2026-07-06
type: article
source_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools"
canonical_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools"
author: Rodrigo Girão Serrão
topics:
  - agentic_coding
tags: []
---

# Write a coding agent from first principles: better tools

## TL;DR

- This sequel upgrades the minimal coding agent from the [first tutorial](2026-06-22_article_write-a-coding-agent-from-first-principles.md) with Anthropic's native text-editor and Bash tool interfaces.
- The central lesson is that a tool is more than a function: reliability depends on the model knowing its schema, while the host remains responsible for execution, state, error handling, security, and bounded output.
- A capable coding harness can remain understandable and compact—roughly 300 lines—while supporting precise edits, a persistent shell, timeouts, backups, workspace boundaries, and command approvals.

## Key takeaways

- **Prefer familiar tool contracts.** Models call tool schemas more consistently when those schemas match interfaces used during training.
- **Keep execution client-side.** The model requests an operation; trusted host code validates it, runs it, and returns a structured success or error result.
- **Make edits precise and reversible.** Exact-string replacement should fail when the target occurs zero or multiple times, and destructive edits can create timestamped backups first.
- **Constrain filesystem scope.** Write operations should resolve paths and reject access outside the current working directory.
- **Shell state matters.** A persistent Bash subprocess preserves state such as the working directory and environment across commands, making the tool substantially more useful than isolated subprocess calls.
- **Bound every open-ended operation.** Commands need timeouts, output truncation, restart semantics, and graceful process cleanup.
- **Permissions belong in the harness.** The agent should receive explicit authorization results and adapt when a command is denied; executable-level allowlists must account for pipes and chained commands.

## From functions to a dependable harness

The first tutorial established the minimal agent loop: maintain conversation context, expose host functions as tools, execute requested operations, and feed results back to the model. This second part shows what turns that proof of concept into a more dependable coding harness.

Anthropic's native text-editor tool combines viewing, file creation, exact replacement, and insertion behind one versioned interface. The implementation remains local, but the model no longer needs a bespoke schema invented by each developer. That alignment between training and runtime reduces malformed or inconsistent tool calls.

The Bash tool adds a second important property: persistence. Instead of launching an unrelated process for every command, the harness keeps one shell alive, reads its output asynchronously, detects completion with a sentinel, and exposes explicit restart and close operations. A manager layer then adds timeouts, output limits, lazy startup, command approval, and session lifecycle management.

## Relation to established agentic coding practice

This tutorial supports the broader pattern found throughout the agentic-coding notes: keep the model-facing tool surface small and familiar, but make the machinery underneath explicit and rigorous. Capability comes from closing the loop; trust comes from guardrails, observability, reversible edits, and machine-readable results.

It also sharpens the idea that skills and tools are harness extensions rather than prompt prose. The model may choose the action, but dependable behavior comes from deterministic code around that choice.

## Links

- [Original article](https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools)
- [First tutorial: Write a coding agent from first principles](2026-06-22_article_write-a-coding-agent-from-first-principles.md)
- [Companion repository](https://github.com/mathspp/coding-agent-tutorial)
- [Anthropic tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
- [Anthropic text editor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)
- [Anthropic Bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)

## Raw

- [Detailed source capture](raw/2026-07-06_article_mathspp_write-a-coding-agent-from-first-principles-better-tools.raw.md)

