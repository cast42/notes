---
title: "Cognition Agent Memory Repo — source notes"
date: 2026-10-06
type: source
topics:
  - agent_memory
tags:
  - persistent-memory
  - git
  - dreaming
resource: "https://cognition.com/agent-memory-repo"
description: "Paraphrased source outline of Cognition's Agent Memory Repo page and linked open specification."
generated:
  by: "process:codex"
  at: "2026-10-06T05:09:49+00:00"
sources:
  - id: "cognition-agent-memory-repo"
    resource: "https://cognition.com/agent-memory-repo"
  - id: "agent-memory-repo-spec"
    resource: "https://github.com/AgentMemoryRepo/agentmemoryrepo"
---

# Source notes: Agent Memory Repo

These are concise paraphrases of Cognition's project page and linked GitHub specification, checked 2026-10-06. They are not a verbatim copy.

## Product idea and loop

- Agent memory persists in a Git repository across sessions and is linked like a wiki.
- Session loop: clone latest memory, search or follow links, update entries as the agent learns, commit/push each edit.
- The open spec presents Git as providing history, merging, and permissions; the use cases include personal memory, agent swarms, shared team knowledge, and composable memories for multiple users.

## Format

- Keep `MEMORY.md` short because it is the entry point loaded at each session start; include universal facts and links to detail files.
- Store entries as concise Markdown bullets with optional metadata. Recommended metadata includes a source session URL and date added.
- Use root-relative `[[path]]` links between notes and files. A repository may also hold SQL, scripts, and other artifacts.
- Keep distinct users' memory repositories separate, and only load another user's repository when they choose to share it. Ask if a new fact's destination is unclear.

## Dreaming

- A periodically running, dedicated agent adds memories by detecting patterns across sessions.
- It also maintains the corpus: merge duplicates, remove outdated memories, and check sources to resolve contradictory claims.

## Skill trial and caveat

- The project documents `npx skills add AgentMemoryRepo/agentmemoryrepo --skill agent-memory-repo`, and a Devin plugin installation route.
- The website's manual trial creates a separate local memory repository without a remote, then has a later session on the same machine/project retrieve a saved preference.
- The site distinguishes this trial from the full proposal: the trial does not configure automatic startup or scheduled Dreaming. A local repository is absent on a different cloud machine until a private remote is connected and cloned.
- The spec is described as originally developed by Cognition, released as an open standard, and licensed MIT.

## Sources

- https://cognition.com/agent-memory-repo
- https://github.com/AgentMemoryRepo/agentmemoryrepo
- https://github.com/AgentMemoryRepo/agentmemoryrepo/blob/main/SPEC.md
- https://github.com/AgentMemoryRepo/agentmemoryrepo/blob/main/LICENSE
