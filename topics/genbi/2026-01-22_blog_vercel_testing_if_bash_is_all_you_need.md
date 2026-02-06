---
title: "Testing if 'bash is all you need' (Vercel / Braintrust)"
date: 2026-01-22
type: note
topics:
  - genbi
tags:
  - agents
  - evals
  - sql
  - bash
  - structured_data
people:
  - Ankur Goyal
source:
  kind: blog
  url: https://vercel.com/blog/testing-if-bash-is-all-you-need
---

# Testing if “bash is all you need” (Vercel / Braintrust)

## TL;DR
Vercel + Braintrust tested the hypothesis that giving agents a filesystem + bash (“**bash is all you need**”) is the best abstraction.
On a benchmark of querying semi-structured GitHub issues/PRs, **SQL beat bash** on accuracy, cost, and latency — but a **hybrid** approach (bash + SQLite) ended up most reliable because the agent used bash to *verify* SQL answers.

## Takeaways
- For **structured data with clear schema**, SQL is the straight-line tool: fewer tokens, faster, more accurate.
- Shell access can produce impressive command chains, but that doesn’t automatically translate into correctness.
- **Hybrid = best reliability**: use SQL for the query, then use filesystem tools to spot-check/verify.
- Evals matter: traces + harnesses surfaced benchmark bugs and tool bottlenecks; without that, you’d argue abstractions based on flawed data.

## Details

### Setup
Task: answer questions over a dataset of GitHub issues + pull requests.
Question types ranged from simple counts (“open issues mentioning security”) to relationship queries (“bug report later fixed by PR”).

Compared agents:
- **SQL agent** (SQLite)
- **Bash agent** (JSON files + `just-bash`)
- **Filesystem agent** (search/read tools, no full shell)

### Initial results (as reported)
- SQL: **100%** accuracy, **155k** tokens, **$0.51**, **45s**
- Bash: **52.7%** accuracy, **1.06M** tokens, **$3.34**, **401s**
- Filesystem: **63.0%** accuracy, **1.28M** tokens, **$3.89**, **126s**

### Why bash underperformed (diagnosis)
- Performance bottlenecks (e.g., expensive `stat()` across ~68k files)
- Missing schema context (agent didn’t know JSON structure)
- Eval/scoring issues (expected answers wrong/ambiguous)

### The hybrid approach
Give the agent both:
- bash/filesystem for exploration + verification
- SQLite for direct querying

Observed behavior: run SQL, then validate by grepping the filesystem.
Tradeoff: about **2× tokens** vs pure SQL, but more consistent correctness.

## Links
- Post: <https://vercel.com/blog/testing-if-bash-is-all-you-need>
- Eval harness (open source): <https://github.com/braintrustdata/bash-agent-evals>
