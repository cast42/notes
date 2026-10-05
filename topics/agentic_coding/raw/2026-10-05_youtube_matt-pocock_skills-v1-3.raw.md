---
type: source
date: 2026-10-05
source_url: "https://youtu.be/BsJGo1wFTvQ?is=kEM87RGi8AGC9hSK"
canonical_url: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
resource: "https://www.youtube.com/watch?v=BsJGo1wFTvQ"
title: "Matt Pocock — Skills v1.3 walkthrough"
author: Matt Pocock
handle: mattpocockuk
created_at: 2026-10-05
topics: [agentic_coding]
tags:
  - agent-skills
  - specification-driven-development
  - code-review
  - retrospectives
description: "Paraphrased, timestamped source notes from Matt Pocock's walkthrough of three new skills in v1.3."
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
content_hash: "2a7ae03a4cfb465eb03c8cdd6895fd564a1af8891dc05de73e843c313d6b8edf"
extracted_at: "2026-10-05T11:34:31+00:00"
extractor: "yt-dlp audio download + whisper.cpp base.en local ASR; YouTube subtitles unavailable. Transcript used for analysis, not reproduced; paraphrases below."
---

# Raw source notes

Video: https://www.youtube.com/watch?v=BsJGo1wFTvQ
Title: New Skills! v1.3 brings /pr, /implement-spec, and /retro
Duration: 14:34
Channel: Matt Pocock

## Transcript-derived notes

These are concise paraphrases, not a verbatim transcript. Times refer to the supplied YouTube video.

### `/implement-spec` (0:27–4:45)

- A spec is the destination; tickets decompose it into separate coding sessions. Trying to do a large spec in one agent context risks degraded reasoning or compaction.
- Manual ticket-by-ticket prompting works but makes the human the loop controller.
- A deterministic script can read tickets and run the same implementation loop reliably and cheaply; building and tuning that automation takes effort.
- The new middle ground is an orchestrator agent that reads a ticket dependency graph, delegates ready work to implementer subagents, and integrates as dependencies clear.
- In the video, Matt describes exploration, an integration branch, implementer subagents in worktrees using TDD, merges back to the integration branch, then code review and a review-ready PR. He calls this useful for AFK work but less deterministic than a script loop.

### `/pr` (4:55–8:05)

- Pull-request review is a bottleneck, so the skill structures a PR body for quick human comprehension.
- It uses a compact visual explanation (inspired by Dex Horthy's Show Me), before/after evidence, a merge-danger assessment (one-way or two-way door), and blast radius.
- Evidence may require an extra test or screenshot; a model's claim based only on reading its own code is weak evidence.

### Repository/domain-file update (8:10–9:30)

- Matt says the skills now use `GLOSSARY.md` rather than `CONTEXT.md` for domain language because “context” was too vague and the file had effectively become a glossary.
- Repository v1.3.1 release notes further standardize the names to `GLOSSARY.md` / `GLOSSARY-MAP.md`.

### `/retro` (9:35–13:55)

- Retro reviews agent session history for environment-level improvements, including navigation, missing automated checks, coding standards, agent instructions, tool efficiency, and access to context.
- Demonstrated findings include an agent taking a public release action without waiting for a choice, a missing CI guardrail, context lost in long sessions, and inefficient or unavailable tooling.
- Matt recommends human judgment and sampling sessions, including ones that went wrong. The point is to learn from repeated friction; blindly automating every suggested fix can create false-positive loops and damage the setup.
- In the video, Matt reports that regular use improved token efficiency and work quality. Treat this as his experience, not an independently measured result.

## Provenance and limitations

- YouTube did not provide captions for this video, so audio was downloaded with `yt-dlp` and transcribed locally using `whisper.cpp` with the `base.en` model.
- Automatic speech recognition may mishear names or commands. The official [skills repository](https://github.com/mattpocock/skills) and [release notes](https://github.com/mattpocock/skills/releases) were checked for project/version details.
- The v1.3.1 release marks `/implement-spec` and `/retro` user-invoked, and `/pr` model-invoked.
- Full transcript is not included here; only paraphrase and navigation timestamps are retained.
