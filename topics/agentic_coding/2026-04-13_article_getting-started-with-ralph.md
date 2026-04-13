---
type: article
source_url: "https://www.aihero.dev/getting-started-with-ralph"
canonical_url: "https://aihero.dev/getting-started-with-ralph"
title: Getting Started With Ralph
author: AI Hero
created_at: 2026-04-13
topics: [agentic_coding]
---

# Getting Started With Ralph

*AI Hero*

## TL;DR

- Ralph is a simple agent loop: repeatedly run the same coding prompt against a PRD and progress file, commit one task at a time, and stop when complete.
- The article shows both a supervised one-shot loop and an unattended AFK loop using Claude Code plus Docker sandboxes.
- The useful pattern is not the exact tooling but the structure: explicit task source, persistent progress memory, iteration cap, and completion signal.

## Highlights

- Start with a human-in-the-loop script before going fully AFK.
- Use a PRD plus progress.txt so the agent can pick the next task and preserve state between iterations.
- The AFK loop adds print-mode output capture, a completion marker, test/type-check steps, and a hard iteration limit to control cost and drift.

## Links

- Permalink: https://aihero.dev/getting-started-with-ralph
- https://ghuntley.com/ralph/
- https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum

## Raw

- Raw text: topics/agentic_coding/raw/2026-04-13_article_getting-started-with-ralph.raw.md
- Extractor: web_fetch

## My notes
-
