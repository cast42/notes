---
title: "Gemini deep-research skill for Antigravity"
date: 2026-11-27
type: tweet
topics:
  - agentic_coding
tags:
  - agent-skills
  - deep-research
  - multi-agent-research
  - source-verification
  - antigravity
resource: "https://x.com/_philschmid/status/2126312943520243885"
description: "An experimental Gemini research skill coordinates bounded parallel investigations and synthesizes source-grounded reports."
author: Philipp Schmid
sources:
  - resource: "https://x.com/_philschmid/status/2126312943520243885"
  - resource: "https://github.com/google-gemini/demolab/tree/main/skills/deep-research"
---

# Gemini deep-research skill for Antigravity

## TL;DR

Philipp Schmid describes an experimental **deep-research** skill for Gemini 4 Neon that turns a broad research question into bounded parallel investigations and a sourced synthesis. It is available in [google-gemini/demolab](https://github.com/google-gemini/demolab/tree/main/skills/deep-research), with instructions for using it in Antigravity.

## Workflow

1. **Orient and scope:** clarify only consequential ambiguity; answer narrow lookups directly or use at most two subagents. Split broad questions into three to five distinct angles, fewer for slower models.
2. **Investigate in parallel:** give workers different angles, timeframes and source scopes; use browser-capable workers for full or authenticated pages. Limit each track to roughly 8–12 searches or tool steps. If subagents are unavailable, conduct the tracks directly.
3. **Ground claims:** favor primary sources and full documents over search snippets. Workers should provide evidence for key figures and return verified partial findings and gaps when their budget ends.
4. **Manage gaps and delays:** collect results as they arrive; the skill advises cancelling a stalled worker after most finish, allowing one targeted follow-up for important gaps, and using a fresh verifier for high-stakes or data-heavy reports.
5. **Synthesize:** produce a two-sentence top line, inline links and an unresolved section for conflicts or missing evidence. Use the session's artifact directory if available; otherwise respond directly.

## Antigravity and installation

Schmid's reply suggests:

```sh
npx skills add google-gemini/demolab --skill deep-research
```

This runs an external installer; review the repository and installer before use. **The skill was not installed or tested for this note.** The repository lists it under Apache-2.0.

## Evidence and limits

Schmid reports that the skill was preferred over a no-skill baseline more than 90% of the time across hundreds of blind evaluations. This is the author's claim; the post does not provide enough details here to assess the task distribution, judging criteria, statistical uncertainty or generalization to other models and harnesses. A preference score alone does not prove factual accuracy.

The speed limits are heuristics: cancelling a slow track may discard valuable contrary evidence. Subagents and browser access also depend on the host's capabilities and permissions; the file is guidance, not a guarantee that a particular Antigravity configuration has them.

## Related

- [Gemini frontend-design skill](2026-11-24_tweet_philipp-schmid_gemini-frontend-design-skill.md) — another experimental skill from the same repository.
- [AI factual search and verification](2026-11-07_tweet_ethan-mollick_ai-factual-verification.md) — interpreting evidence on automated research and verification.

## Sources

- [Schmid's post](https://x.com/_philschmid/status/2126312943520243885).
- [Skill directory and SKILL.md](https://github.com/google-gemini/demolab/tree/main/skills/deep-research).
