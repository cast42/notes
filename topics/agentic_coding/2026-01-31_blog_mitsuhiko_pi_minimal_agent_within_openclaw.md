---
title: "Pi: the minimal agent within OpenClaw (and why it matters)"
date: 2026-01-31
type: note
topics:
  - agentic_coding
tags:
  - openclaw
  - pi
  - minimalism
  - extensions
  - tools
  - sessions
  - tui
source:
  kind: blog
  url: https://lucumr.pocoo.org/2026/1/31/pi/
---

## TL;DR

OpenClaw’s “coding agent” core is **Pi** (by Mario Zechner): a deliberately minimal agent (short system prompt, only 4 tools: **Read/Write/Edit/Bash**) that stays powerful via an **extension system** with persistent state + hot reload + a terminal UI. The blog post argues this architecture makes agents *malleable like clay*: the agent can extend itself by writing code rather than requiring a huge built-in tool surface.

> openclaw is an agent connected to a communication channel of your choice that [just runs code](https://lucumr.pocoo.org/2025/7/3/tools/).

(Also captured as its own note under the OpenClaw topic: `topics/openclaw/2026-02-06_blog_mitsuhiko_openclaw_just_runs_code.md`.)

## What Pi is (according to the post)

Pi is a coding agent the author uses almost exclusively. It’s notable for:

- **Tiny core**: shortest system prompt the author has seen; only four tools.
- **Extension system** that can persist state into sessions (powerful).
- **Reliability**: low resource usage; doesn’t flicker/break; carefully engineered.
- **Composable components**: you can build your own agent on top (OpenClaw is built this way).

## What’s intentionally *not* in Pi

- No built-in **MCP** support.
- This is philosophical: instead of “download an extension/skill for everything”, you **ask the agent to extend itself**.
- If you really want MCP, you can bridge via tools like **mcporter** (CLI/TS bindings) and have the agent use that.

## Architecture details that matter for agentic coding

### Sessions as trees (branching workflows)

- Sessions are **trees**: you can branch, navigate, rewind.
- This supports side-quests (e.g., fix a broken tool) without polluting the main context.
- After a side branch, Pi can summarize what happened.

### Persistent extension state + hot reload

- Extensions can store state (custom messages in session files / extension state on disk).
- Built-in **hot reloading** supports a tight loop: agent writes extension code → reloads → tests → iterates.

### “Tools outside the context”

- Pi *can* register new tools callable by the model, but the author mostly prefers:
  - slash commands
  - TUI extensions
  - skills that use CLI/normal workflows

The idea: avoid bloating the always-loaded tool context.

## Examples of extensions (good inspiration)

The post highlights a few extensions (all in TypeScript):

- `/answer`: turns the agent’s last response into a clean question list UI
- `/todos`: local markdown todo tracking in `.pi/todos`
- `/review`: branch into a review context, then bring fixes back; UI modeled after Codex (diffs/commits/PRs)
- `/control`: one Pi agent can prompt another (simple multi-agent)
- `/files`: lists files changed/referenced and offers actions (reveal/diff/quicklook)

## Why this is a useful lens for “agentic coding”

- **Minimal core + extensibility** is a strong strategy to avoid fragile mega-agents.
- Session trees + branching match how real work happens (explore, fix tool, return).
- The post makes a case for “software building software”: the agent maintains its own capabilities over time.

## Source

- Blog post: https://lucumr.pocoo.org/2026/1/31/pi/
- Pi: https://github.com/badlogic/pi-mono/
