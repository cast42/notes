---
type: article
source_url: "https://www.aihero.dev/getting-started-with-ralph"
canonical_url: "https://aihero.dev/getting-started-with-ralph"
title: Getting Started With Ralph
author: AI Hero
created_at: 2026-04-13
topics: [agentic_coding]
content_hash: 32f4bd4d3d32659d676d2e524a606153c6006faddaaf635663c3681e88ae0440
extracted_at: "2026-04-13T11:41:29"
extractor: web_fetch
---

# Raw content

Source: https://aihero.dev/getting-started-with-ralph


Source URL: https://www.aihero.dev/getting-started-with-ralph
Title: Getting Started With Ralph
Description: Learn to run AI coding agents in a loop. Set up Claude Code, create a PRD, and let the AI ship features while you're AFK. Step-by-step guide included.
Updated: 2026-01-08

Extracted article content:
Ralph is a technique for running AI coding agents in a loop. You run the same prompt repeatedly. The AI picks its own tasks from a PRD. It commits after each feature. You come back later to working code.

This guide walks through building a first Ralph loop using Claude Code and Docker Desktop.

Key setup:
- Install Claude Code and authenticate.
- Install Docker Desktop to run Claude in an isolated sandbox.
- Create a PRD.md plan file and an empty progress.txt file.

Human-in-the-loop version:
- Create ralph-once.sh
- Run Claude with PRD.md and progress.txt
- Ask it to read both files, find the next incomplete task, implement one task only, commit changes, and update progress.txt
- Use permission mode acceptEdits to avoid stalling on file edit prompts

AFK version:
- Create afk-ralph.sh
- Wrap Claude in a shell loop with a max iteration count
- Use print mode to capture output
- Have the agent run tests and type checks, update PRD and progress, commit changes, and emit <promise>COMPLETE</promise> when done
- Stop the loop when the completion marker appears

Why it works:
- The PRD defines the target state.
- progress.txt stores short-term execution state across iterations.
- "Only do one task" keeps commits small and inspectable.
- A hard iteration cap limits runaway cost.

Customization ideas from the article:
- Pull tasks from GitHub Issues, Linear, or beads instead of a local PRD
- Open branches/PRs instead of committing directly to main
- Use the same loop for test coverage, lint fixing, duplication reduction, or code-smell cleanup

Important examples mentioned:
- ralph-once.sh for supervised repetition
- afk-ralph.sh for unattended iterations
- docker sandbox run claude for isolated execution

Notes:
- This article is specifically about a simple repeatable control loop around an agent, not a complex orchestration system.
- The main conceptual pieces are: task source, loop runner, progress memory, and completion signal.
