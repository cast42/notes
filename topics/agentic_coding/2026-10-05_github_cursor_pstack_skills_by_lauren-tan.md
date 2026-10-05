---
title: "pstack: Lauren Tan's engineering skills for coding agents"
date: 2026-10-05
type: software
topics:
  - agentic_coding
tags:
  - coding-agents
  - agent-skills
  - software-verification
  - code-review
  - engineering-workflows
resource: "https://github.com/cursor/plugins/tree/main/pstack"
description: "Lauren Tan's pstack is a Cursor plugin that routes engineering tasks through explicit playbooks and reusable principles, emphasizing verified changes over code volume."
author: "Lauren Tan"
handle: "poteto"
generated:
  by: "process:codex"
  at: "2026-10-05T11:55:00+00:00"
sources:
  - id: "official-pstack-readme"
    resource: "https://github.com/cursor/plugins/blob/main/pstack/README.md"
  - id: "official-pstack-mode-skill"
    resource: "https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md"
  - id: "official-pstack-plugin-manifest"
    resource: "https://github.com/cursor/plugins/blob/main/pstack/.cursor-plugin/plugin.json"
---

# pstack: Lauren Tan's engineering skills for coding agents

*Lauren Tan — @poteto*

## TL;DR

- pstack is a Cursor plugin of reusable engineering workflows, playbooks, and principles. Its stated goal is not to maximize code or agent throughput, but to write less, higher-quality code and make parallel agent work more trustworthy.
- Start with `/setup-pstack` to choose models, then `/poteto-mode` to route a task into an appropriate workflow. The README currently lists 23 playbooks and 24 principle skills; task-specific skills and subagents fill in the steps.
- Its distinctive idea is to make rigor operational: investigate the system, choose a concrete workflow, verify behavior with evidence, and review the result. It is Cursor-specific as published; other-harness ports are independent projects, not the official plugin.

## How the skill stack is organized

### `/poteto-mode` is the entry point

The main skill classifies the request, selects a playbook, lays out the playbook's steps, and calls other skills as needed. For an unfamiliar pstack workflow, `/poteto-help` helps choose a route. A user can also invoke a narrower skill directly.

The official README groups 23 playbooks across several kinds of work:

- **Understand and diagnose:** investigation, bug fixing, performance work, runtime/trace forensics.
- **Design and change:** feature work, refactoring, prototyping, visual parity, multi-phase changes.
- **Improve engineering practice:** authoring a skill, evaluating a skill, and continuous metric improvement (`hillclimb`).
- **Operate and deliver:** babysit a PR, ship a verified stack, autonomous runs, long-running orchestration, autopilot modes, session pickup/pause, worktree cleanup, and opening a PR.

These playbooks give agents a process, not proof that each step succeeded. For example, the verification-oriented principles explicitly call for checking the real behavior rather than relying on an assertion or compilation alone.

### Skills and principles support the playbooks

The skill catalog includes focused actions such as `/how` for a subsystem walkthrough, `/why` for evidence gathering, `/architect` for settling a boundary before implementation, `/arena` and `/swarm` for different kinds of parallel work, `/interrogate` for adversarial review, `/tdd`, `/reflect`, and `/correct` for turning repeated mistakes into structural fixes.

The README lists 24 short principle skills, organized around core engineering choices, architecture, verification, delegation, and meta-level learning. Examples include minimizing changes, modeling the domain, making illegal states unrepresentable, proving behavior, fixing root causes, protecting context, and encoding lessons in enforceable structure. These principles guide the work; they do not replace tests, repository constraints, or human judgment.

The plugin also includes `poteto-agent` and a read-only comment-review subagent. A dormant Benny automation pack can triage Slack issue reports and attempt fixes with UI evidence, but it requires separate setup and is not a slash skill.

## Getting started and boundaries

In Cursor, the README's quick start is:

1. Install with `/add-plugin pstack`.
2. Run `/setup-pstack` to configure reasoning budget and model roles.
3. Use `/poteto-mode` for non-trivial engineering work; ask `/poteto-help` when unsure which workflow fits.

The current plugin manifest identifies version **0.15.10**, Lauren Tan as author, and an MIT license (checked 2026-10-05). The integration depends on Cursor's plugin, model-routing, and subagent mechanisms. Community ports may adapt the content for other agents, but check each port's provenance and license separately rather than treating it as the official Cursor plugin.

The README explicitly invites people to fork, improve, and adapt pstack. That is a useful posture: borrow the workflow that solves a real friction point, then fit it to the repository and its actual verification tools. Don't adopt the entire stack just because it is comprehensive.

## Related concept

- [Lauren Tan on pstack, verification, and agent workflows](2026-09-21_video_lauren-tan-pstack-verification-and-agent-workflows.md) — the talk and interview behind the verification-first engineering context; this note focuses on the published skill stack itself.

## Sources

- [Official pstack plugin](https://github.com/cursor/plugins/tree/main/pstack)
- [pstack README and skill catalog](https://github.com/cursor/plugins/blob/main/pstack/README.md)
- [Plugin manifest](https://github.com/cursor/plugins/blob/main/pstack/.cursor-plugin/plugin.json)
