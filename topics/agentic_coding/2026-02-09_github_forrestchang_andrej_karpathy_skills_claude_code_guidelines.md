---
title: "Karpathy-inspired Claude Code guidelines (forrestchang/andrej-karpathy-skills)"
date: 2026-02-09
type: note
topics:
  - agentic_coding
tags:
  - claude
  - prompting
  - guidelines
  - tooling
people:
  - Andrej Karpathy
source:
  kind: github
  url: https://github.com/forrestchang/andrej-karpathy-skills
---

# Karpathy-inspired Claude Code guidelines (forrestchang/andrej-karpathy-skills)

## TL;DR
A single `CLAUDE.md` (and installable Claude Code plugin) that turns Andrej Karpathy’s observations about LLM coding pitfalls into four operational rules: **think before coding**, **simplicity first**, **surgical changes**, and **goal-driven execution**.

## Takeaways
- Useful when you want Claude Code to:
  - ask clarifying questions instead of guessing
  - avoid abstraction bloat / overengineering
  - keep diffs minimal (no drive-by refactors)
  - loop until verifiable success criteria are met

## The 4 principles (as described)
1. **Think Before Coding** — state assumptions; surface ambiguity; ask; push back when simpler.
2. **Simplicity First** — minimum code; no speculative flexibility.
3. **Surgical Changes** — touch only what’s required; clean up only what you made unused.
4. **Goal-Driven Execution** — convert tasks into success criteria + verification loops.

## Links
- Repo: <https://github.com/forrestchang/andrej-karpathy-skills>
- Karpathy post referenced in the repo: <https://x.com/karpathy/status/2015883857489522876>
