---
type: "tweet"
source_url: "https://x.com/JnBrymn/status/2099606852942143647"
canonical_url: "https://x.com/JnBrymn/status/2099606852942143647"
title: "AI model frontier skill for adaptive agent routing"
author: "John Berryman"
handle: "JnBrymn"
created_at: "2026-09-14"
date: "2026-09-14"
topics: ["agentic_coding"]
tags: [agent-skills, model-routing, pareto-frontier, model-selection, context-windows]
resource: "https://x.com/JnBrymn/status/2099606852942143647"
generated: {"by": "process:note-ingest", "at": "2026-09-15T05:28:49+00:00"}
sources: [{"id": "original", "resource": "https://x.com/JnBrymn/status/2099606852942143647"}, {"id": "skill", "resource": "https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier"}, {"id": "artificial-analysis-api", "resource": "https://artificialanalysis.ai/data-api/docs"}]
description: "A reusable skill that turns live model quality and price data into auditable Pareto frontiers for adaptive agent-model routing."
---

# AI model frontier skill for adaptive agent routing

*John Berryman — @JnBrymn*

## TL;DR

- Turn a complete Artificial Analysis model snapshot into company and combined cost-versus-quality Pareto frontiers.
- Use current frontier data to inform Pi or Oh My Pi model choices when a route reaches a context-window limit.
- Keep benchmark proxies, prices, provider IDs, cache age, and harness changes explicit so model routing remains auditable.

## Highlights

- The skill computes quality from the Artificial Analysis Intelligence Index and cost from a fixed 3:1 input/output token-price blend.
- It produces Markdown, CSV, JSON, PNG, and SVG reports, including thinking-level variants and a combined frontier.
- Pi and Oh My Pi configuration changes are an authorized follow-up, not an automatic consequence of a report-only run.
- The X post illustrates a scheduled deployment that jumps to frontier models when Codex reaches a window limit.

## What the skill does

The skill turns model selection into a small, repeatable control loop:

1. Retrieve or reuse one complete Artificial Analysis snapshot, with pagination and index-version checks.
2. Compute each model's quality from the Artificial Analysis Intelligence Index and its cost from a fixed 3:1 input/output token-price blend.
3. Remove dominated choices and produce company, combined-watchlist, and entire-catalogue Pareto frontiers.
4. Preserve measured thinking-level variants and generate Markdown, CSV, JSON, PNG, and SVG outputs.
5. Optionally translate selected frontiers into Pi or Oh My Pi configuration after an explicitly authorized follow-up.

## Why it matters

The interesting move is to make the model catalogue an operational routing layer rather than a static list. A scheduled run can discover which models currently offer a better quality/cost trade-off; an agent that reaches a context-window limit can then switch to a strong alternative instead of stopping. The post describes this deployment pattern, while the skill itself keeps report generation separate from harness mutation.

## Boundaries

- The AA Intelligence Index is a benchmark proxy, not a guarantee of performance on a particular task.
- The blended token price is not cost per task: it excludes caching, tool charges, human time, and variable reasoning-token use.
- Prices, model names, provider IDs, benchmark versions, and availability change; cached snapshots and historical comparisons need dates and version labels.
- The free endpoint does not establish licensing or self-hosting status, so the skill records self-hosting as unknown rather than inferring it.
- Configuration updates need verified provider/model mappings and live checks; a frontier plot alone is not evidence that a route is authenticated or usable.

## Links

- Permalink: [https://x.com/JnBrymn/status/2099606852942143647](https://x.com/JnBrymn/status/2099606852942143647)
- [https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier](https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier)
- [https://raw.githubusercontent.com/arcturus-labs/agent-skills/main/skills/update-ai-model-frontier/SKILL.md](https://raw.githubusercontent.com/arcturus-labs/agent-skills/main/skills/update-ai-model-frontier/SKILL.md)
- [https://artificialanalysis.ai/data-api/docs](https://artificialanalysis.ai/data-api/docs)
- [https://pbs.twimg.com/media/HSNL_HrXwAA8C7Y.jpg?name=orig](https://pbs.twimg.com/media/HSNL_HrXwAA8C7Y.jpg?name=orig)

## Raw

- Raw text: [topics/agentic_coding/raw/2026-09-14_tweet_ai-model-frontier-skill-for-adaptive-agent-routing.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-09-14_tweet_ai-model-frontier-skill-for-adaptive-agent-routing.raw.md)
- Extractor: fxtwitter+github-skill

## My notes

- This is a useful example of **adaptive agent routing**: external model-market observations feed a report, a human-authorized configuration step, and a fallback path for long-running work.
