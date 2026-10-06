---
title: "Agent Memory Repo: Git-backed memory and periodic dreaming"
date: 2026-10-06
type: concept
topics:
  - agent_memory
tags:
  - persistent-memory
  - git
  - knowledge-maintenance
  - provenance
  - agent-swarms
resource: "https://cognition.com/agent-memory-repo"
description: "Cognition's Agent Memory Repo spec uses Git and linked files for persistent agent memory, with periodic dreaming to distill patterns and maintain stale or conflicting knowledge."
generated:
  by: "process:codex"
  at: "2026-10-06T05:09:49+00:00"
sources:
  - id: "cognition-agent-memory-repo"
    resource: "https://cognition.com/agent-memory-repo"
  - id: "agent-memory-repo-spec"
    resource: "https://github.com/AgentMemoryRepo/agentmemoryrepo"
---

# Agent Memory Repo: Git-backed memory and periodic dreaming

## TL;DR

- Cognition's Agent Memory Repo treats long-lived agent memory as a Git repository of linked files. Each session retrieves what it needs, updates memory as it learns, and commits or pushes the change.
- A short `MEMORY.md` acts as the always-loaded entry point; linked notes, queries, scripts, and other artifacts hold details. Git supplies history, ownership boundaries, and conflict signals for shared or parallel work.
- “Dreaming” is a separate periodic maintenance agent: it distills patterns across sessions, adds useful memories, merges duplicates, retires outdated entries, and checks sources when claims conflict.
- Important distinction: the spec describes the broader loop, but the current local trial skill does not automatically start sessions or schedule Dreaming. Its trial is local unless the owner connects a private remote.

## How the memory loop works

The proposal makes memory a maintained shared artifact rather than a transcript dump:

1. Clone or retrieve the latest memory repository.
2. Search for the task's relevant context, or navigate by links.
3. Update entries when the agent learns something useful.
4. Commit or push after edits so later sessions and collaborators can see them.

Keep the root `MEMORY.md` short because every session loads it. Put details in linked files and attach source links and dates to individual claims. The format is intentionally flexible: Markdown can coexist with SQL, scripts, and other useful project artifacts.

The same structure can serve personal memory, team knowledge, and parallel-agent investigations. Separate user repositories preserve who owns which facts; a session can load more than one repository when its participants choose to share them. Swarms can coordinate through shared folders such as findings, questions, and reproducible scripts. Git merges non-overlapping edits and surfaces conflicting writes, but it does not resolve semantic contradictions automatically.

## What Dreaming adds

Dreaming is not another retrieval step inside every task. It is a periodic curation pass over accumulated sessions and memory. Its two jobs are to:

- detect repeated or connected lessons and save reusable entries;
- improve the memory base by merging duplicates, removing stale claims, and checking sources to resolve disagreements.

This is a concrete memory-maintenance loop: retrieve and write during work, then periodically consolidate and prune. It echoes the broader test-time-evolution idea that useful memory needs search, synthesis, refinement, and forgetting—not just accumulation. Dreaming will only be trustworthy if it preserves provenance and treats uncertainty carefully; an incorrect merge or deletion can contaminate future sessions just as easily as an incorrect new memory.

## Try it, with the scope clear

The project documents a skill installer:

```sh
npx skills add AgentMemoryRepo/agentmemoryrepo --skill agent-memory-repo
```

It also documents `devin plugins install AgentMemoryRepo/agentmemoryrepo` for Devin. The website's simple local trial asks the agent to create a separate repository without a remote, then checks retrieval in another session on the same machine and project. The page explicitly says that automatic startup and scheduled Dreaming are not included in this trial. To use memory on another machine, connect a private remote and clone it there; do not assume a local trial has become synchronized memory.

## Practical read

Git is a useful substrate because it makes edits inspectable, attributable, reversible, and shareable. The main risk is granting an agent a frictionless path to rewrite and publish its own long-term context: bad inferences can become durable and repeatedly retrieved. For high-impact preferences, policy, or disputed facts, retain source links and review the change rather than relying on “Dreaming” to guarantee correctness.

The specification is published as an open standard and the repository declares an MIT license. This note describes the proposal and documented trial; it is not an evaluation of a deployed memory system's recall quality or safety.

## Related concepts

- [Test-time evolution for agent memory](2026-02-04_x__philschmid_test_time_evolution_agent_memory.md) — active search, synthesis, refinement, and deletion as a memory loop.
- [WFM: Wiki Foundation Model for Complex Agentic Reasoning](2026-09-23_tweet_wfm-wiki-foundation-model-for-complex-agentic-reasoning.md) — linked Markdown as both semantic context and navigable graph structure.

## Sources

- [Cognition: Agent Memory Repo](https://cognition.com/agent-memory-repo)
- [AgentMemoryRepo specification and skill](https://github.com/AgentMemoryRepo/agentmemoryrepo)
- [MIT license](https://github.com/AgentMemoryRepo/agentmemoryrepo/blob/main/LICENSE)
- Raw source summary: [timestamp-free extraction notes](raw/2026-10-06_cognition_agent-memory-repo-and-dreaming.raw.md)
