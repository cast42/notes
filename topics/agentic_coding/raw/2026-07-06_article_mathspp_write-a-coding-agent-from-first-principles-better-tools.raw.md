---
title: "Raw capture: Write a coding agent from first principles: better tools"
date: 2026-07-06
timestamp: 2026-07-06
type: source
source_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools"
canonical_url: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools"
resource: "https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools"
description: "Detailed source capture of the mathspp tutorial implementing Anthropic-compatible text editing and persistent Bash tools with safety controls."
author: Rodrigo Girão Serrão
topics:
  - agentic_coding
tags:
  - coding-agents
  - agent-harnesses
  - tool-use
  - persistent-shells
  - filesystem-safety
  - command-approval
extractor: web
extracted_at: 2026-07-15
---

# Raw capture: Write a coding agent from first principles: better tools

## Source metadata

- Published: 6 July 2026
- Author: Rodrigo Girão Serrão / mathspp
- Article: https://mathspp.com/blog/write-a-coding-agent-from-first-principles-better-tools
- Companion repository: https://github.com/mathspp/coding-agent-tutorial
- Series predecessor: https://mathspp.com/blog/write-a-coding-agent-from-first-principles

## Detailed source outline

### Why use Anthropic's native tools?

The tutorial replaces bespoke read, write, replace, insert, and Bash definitions with Anthropic's versioned native tool interfaces. These operations still execute in client code, but Claude already understands their expected schemas because the models are trained to use them. The stated benefit is more consistent and accurate tool requests.

### Native text editor

The text-editor interface dispatches four commands:

- `create`: create a file with supplied text, optionally refusing to overwrite an existing path;
- `str_replace`: replace one exact text fragment, rejecting ambiguous cases where the old text occurs zero or multiple times;
- `view`: read a file or list a directory, with optional one-based line ranges and `-1` meaning through the end;
- `insert`: add supplied text at a specified line boundary while preserving newline characters.

The implementation returns an error flag plus a result string, keeping tool failures inside the agent loop instead of crashing the program.

### Filesystem safeguards

The tutorial adds decorators around mutating operations:

- a workspace-boundary check resolves paths and blocks writes outside the current working directory;
- a backup wrapper creates a timestamped copy before replacement or insertion.

Decorator order is meaningful: authorization must happen before creating a backup, otherwise a denied external edit can still leave an unwanted file behind.

### Persistent Bash tool

The Bash implementation keeps a `/bin/bash` subprocess alive using `subprocess.Popen`. Standard input and output are connected through pipes, standard error is redirected into standard output, and a daemon thread transfers output lines into a queue.

For each command, the harness writes the command followed by a unique completion marker. It consumes queued lines until that marker appears. A monotonic deadline and queue timeout prevent the agent from waiting forever. A close method first requests a graceful shell exit and terminates the process if necessary.

### Bash management and safety

A manager layer separates agent-tool policy from the lower-level persistent shell. It is responsible for:

- lazy creation and explicit restart of the Bash session;
- timeouts;
- truncating very large command output;
- closing the process cleanly;
- asking the user to allow a command once, always, or not at all;
- remembering commands that were permanently approved.

The article warns that executable-level approval is subtle: approving an apparently harmless prefix can unintentionally authorize pipes or chained commands that execute something else.

### Result and follow-up work

The finished agent is described as roughly 300 lines: about one third for the core loop and commands, one third for text editing, and one third for the shell and manager. Suggested extensions include response streaming, a richer terminal interface, commands for context/model/token management, and packaging the agent as a CLI so it can later participate in sub-agent workflows.

## References from the article

- https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool
