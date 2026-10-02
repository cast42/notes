---
type: "tweet"
source_url: "https://x.com/karpathy/status/2105819303471976479?s=20"
canonical_url: "https://x.com/karpathy/status/2105819303471976479"
title: "Better Formats for Understanding LLM Outputs"
author: "Andrej Karpathy"
handle: "karpathy"
created_at: "2026-10-02"
date: "2026-10-02"
topics: ["agents"]
tags: [llm-outputs, information-design, human-ai-interaction, agent-skills]
description: "As language models take on more work, well-chosen written, visual, interactive, and video formats can make their outputs easier to understand and oversee."
resource: "https://x.com/karpathy/status/2105819303471976479"
generated: {"by": "process:note-ingest", "at": "2026-10-02T15:32:19+00:00"}
sources: [{"id": "karpathy_post", "resource": "https://x.com/karpathy/status/2105819303471976479"}, {"id": "alik_reply", "resource": "https://x.com/alik_huseyn0v/status/2105989790017454106"}, {"id": "asd_ste100_skill", "resource": "https://github.com/danyuchn/asd-ste100-skill"}]
---

# Better Formats for Understanding LLM Outputs

*Andrej Karpathy — @karpathy*

## TL;DR

- As language models take on more legwork, human work shifts toward oversight and understanding; choose output formats that make that work easier.
- Karpathy suggests constrained prose (ASD-STE100), diagrams, interactive HTML pages, and bespoke explainer videos as increasingly rich ways to explain model outputs.
- A reply links an MIT-licensed ASD-STE100 Claude Code skill that operationalizes the writing suggestion, while explicitly limiting its scope and not reproducing the protected official dictionary.

## Highlights

- Try asking for prose written about 80% of the way to ASD-STE100 when the full standard feels too strict.
- Use diagrams for relationships, interactive web pages for exploration, and custom explainer videos for topics that benefit from narration and animation.
- The related skill defines Strict and STE-flavored modes and includes a deterministic linter for some structural rules.

## Links

- Permalink: [https://x.com/karpathy/status/2105819303471976479](https://x.com/karpathy/status/2105819303471976479)
- [https://x.com/karpathy/status/2105819303471976479/photo/1](https://x.com/karpathy/status/2105819303471976479/photo/1)
- [https://x.com/alik_huseyn0v/status/2105989790017454106](https://x.com/alik_huseyn0v/status/2105989790017454106)
- [https://github.com/danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)
- [Installed ASD-STE100 skill](../../skills/asd-ste100/SKILL.md)

## Raw

- Raw text: [topics/agents/raw/2026-10-02_tweet_better-formats-for-understanding-llm-outputs.raw.md](https://github.com/cast42/notes/blob/main/topics/agents/raw/2026-10-02_tweet_better-formats-for-understanding-llm-outputs.raw.md)
- Extractor: fxtwitter API; image inspected visually

## My notes

- The key move is to choose an output format for the user's understanding task, rather than defaulting to chat prose. Each step can make the result easier to inspect, but richer media can also cost more to produce and verify.
- The linked skill adapts ASD-STE100 rules for agent-facing English. It is not an official ASD implementation and deliberately omits the protected approved-word dictionary, so it must not be treated as certified STE compliance.
