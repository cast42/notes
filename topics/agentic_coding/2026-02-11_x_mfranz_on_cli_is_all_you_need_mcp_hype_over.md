---
title: "Marco Franzon: CLI Is All You Need (the MCP hype is over)"
date: 2026-02-11
type: note
topics:
  - agentic_coding
tags:
  - mcp
  - cli
  - bash
  - tooling
  - agentic_coding
people:
  - Marco Franzon
source:
  kind: x
  url: https://x.com/mfranz_on/article/2021364017147818434
---

# Marco Franzon: CLI Is All You Need (the MCP hype is over)

## TL;DR
Claim: for most day-to-day agentic coding, **MCP-style tool servers are unnecessary overhead**. The winning setup is a strong model + **direct shell access** to the boring, battle-tested tools: `bash`, `git`, `rg`, `grep`, `curl`, `jq`, `docker`, etc.

## Key points (as argued)
- **MCP adds token/context overhead** via verbose tool catalogs + schemas.
- It often **reinvents what official CLIs already do**, but less reliably.
- It hurts **composability**: you lose pipes/chaining/one-off Unix hacks.
- Models are already strongly **trained on shell usage** (flags, pipes, man-page patterns).

> “Drop the agent into your project directory, grant shell execution (with safeguards), and describe the task.”

## Practical examples mentioned
- Monorepo refactor with `rg` + targeted edits + `git diff` + tests.
- Debugging via logs + `curl -v` + `grep` + `docker-compose`.
- Scaffolding services via native toolchains (e.g. `cargo` + `curl` health check).

## Links
- X Article: <https://x.com/mfranz_on/article/2021364017147818434>
- Status link: <https://x.com/i/status/2021364017147818434>
