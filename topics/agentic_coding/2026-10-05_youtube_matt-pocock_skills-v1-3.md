---
type: video
date: 2026-10-05
source_url: "https://youtu.be/BsJGo1wFTvQ?is=kEM87RGi8AGC9hSK"
canonical_url: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
resource: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
title: "Matt Pocock: Skills v1.3 — implement-spec, pr, and retro"
author: Matt Pocock
handle: mattpocockuk
created_at: 2026-10-05
topics: [agentic_coding]
tags:
  - agent-skills
  - specification-driven-development
  - code-review
  - retrospectives
description: "Matt Pocock's v1.3 skill walkthrough turns spec execution, review evidence, and agent-session retrospectives into reusable engineering workflows."
generated:
  by: "process:codex"
  at: "2026-10-05T11:37:05+00:00"
sources:
  - id: "youtube-video"
    resource: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
  - id: "mattpocock-skills-repository"
    resource: "https://github.com/mattpocock/skills"
  - id: "mattpocock-skills-v1.3.1-release"
    resource: "https://github.com/mattpocock/skills/releases"
---

# Matt Pocock: Skills v1.3 — implement-spec, pr, and retro

*Matt Pocock — @mattpocockuk*

## TL;DR

- The video introduces three workflows in Matt Pocock's skills repo: `/implement-spec` orchestrates a spec's ticket graph, `/pr` makes changes easier to review, and `/retro` learns from an agent session to improve the working environment.
- `/implement-spec` is a convenient away-from-keyboard middle ground: subagents work on ready tickets and integrate their results. Matt says a deterministic script loop is more reliable and cheaper when a team can build one.
- `/pr` asks for a small visual summary, before/after evidence, merge danger, and blast radius. `/retro` is a human-reviewed retrospective, not an instruction to let an agent autonomously rewrite its setup.
- The video announces v1.3; the repository's latest release on 2026-10-05 is v1.3.1, which promotes all three into its Engineering skill set and clarifies the glossary-file rename.

## Highlights

### `/implement-spec`: orchestrate a spec's ticket graph

A spec describes the destination; tickets break it into context-sized implementation sessions. `/implement-spec` reads the tickets as a dependency graph and delegates ready work to implementer subagents, using separate worktrees, then integrates and reviews the result. The v1.3 video presents one reviewable change for a large spec (about 0:27–4:45).

Matt compares three ways to run the ticket loop: manually prompting each ticket, a deterministic script loop, and an orchestrator agent that manages subagents. He considers the deterministic loop the most repeatable and cost-efficient, but harder to set up; `/implement-spec` is an accessible AFK option, though less deterministic.

### `/pr`: make human review cheaper

The PR skill shapes the body around four questions: what changed (shown with the smallest useful visual), what evidence demonstrates it works (before/after), how dangerous it is to merge (one-way or two-way door), and what its blast radius is (about 4:55–8:05). The intent is to help a reviewer direct attention, not to claim the PR is correct just because an agent wrote evidence.

### `/retro`: convert session failures into environment improvements

Retro looks back over one or more agent sessions and suggests changes to the repository or agent setup: navigation, checks and guardrails, coding standards, steering files, tools, and access to needed information (about 9:35–13:55). Matt's example surfaced a release action taken before he chose a fix, a missing CI guardrail, context loss, and token-wasting tools.

He recommends sampling sessions and applying human judgment to the suggestions. The skill should propose improvements, not continuously auto-fix its own findings: false positives can otherwise push the repo or agent setup in the wrong direction.

### Version note

The video announces v1.3. As of 2026-10-05, the [latest repository release is v1.3.1](https://github.com/mattpocock/skills/releases): it promotes `/implement-spec`, `/pr`, and `/retro` into the Engineering set, with docs and routing. The release marks `/implement-spec` and `/retro` user-invoked, while `/pr` is model-invoked. It also renames `CONTEXT.md` / `CONTEXT-MAP.md` to `GLOSSARY.md` / `GLOSSARY-MAP.md`; existing files need to be renamed for the skills to find them.

## Links

- [YouTube video](https://youtu.be/BsJGo1wFTvQ?is=kEM87RGi8AGC9hSK)
- [Matt Pocock's skills repository](https://github.com/mattpocock/skills)
- [Skills releases](https://github.com/mattpocock/skills/releases)
- Related: [Matt's earlier end-to-end skills workflow](2026-07-16_video_matt-pocock-s-skills-repo-end-to-end-workflow.md)

## Raw

- [Transcript-derived notes with timestamps and extraction details](raw/2026-10-05_youtube_matt-pocock_skills-v1-3.raw.md)
- Extractor: local `whisper.cpp` `base.en` speech recognition on audio downloaded from YouTube with `yt-dlp`. YouTube captions were unavailable. Full transcript not published; raw companion contains paraphrased notes only.
