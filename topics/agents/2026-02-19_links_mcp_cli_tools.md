---
type: collection
source_url: https://x.com/RLanceMartin/status/2023824176029761931
canonical_url: https://x.com/RLanceMartin/status/2023824176029761931
title: "MCP vs CLI/tools (Lance Martin + Armin Ronacher)"
author: "(multiple)"
created_at: 2026-02-19
topics:
  - agents
tags:
  - mcp
  - cli
---

# MCP vs CLI/tools (Lance Martin + Armin Ronacher)

## TL;DR
- Lance Martin points at **programmatic tool calling (PTC)** as a way to turn “tools” into runnable functions in a container—**fewer tokens + better performance**.
- Armin Ronacher’s take: today’s **MCP isn’t really composable** and burns context; often **plain code/CLI** gets you there faster and more reliably.
- The practical pattern: use LLMs to **generate code/scripts** you can re-run, test, and iterate on—less inference per step.

## Highlights
- RLanceMartin: “performance boost + token savings from converting tools into functions … (programmatic tool calling / PTC)”
- Armin: MCP composition tends to happen “through inference” + each tool call consumes context; try the same task with `gh` CLI and compare.

## Links
- X post (RLanceMartin): https://x.com/RLanceMartin/status/2023824176029761931
  - Claude docs (PTC): https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
  - Image: https://x.com/RLanceMartin/status/2023824176029761931/photo/1
- Blog post (Armin Ronacher): https://lucumr.pocoo.org/2025/7/3/tools/

Related note:
- <a href="https://github.com/cast42/notes/blob/main/topics/genbi/2026-01-22_blog_vercel_testing_if_bash_is_all_you_need.md">Vercel/testing + “bash is all you need” (cast42/notes)</a>

## Raw
- Raw extract: [2026-02-19_collection_mcp-vs-cli-tools.raw.md](raw/2026-02-19_collection_mcp-vs-cli-tools.raw.md)
- Extractors:
  - X: FxTwitter (`https://api.fxtwitter.com/status/<id>`)
  - Article: readability (web_fetch)

## My notes
- This matches our workflow shift: **CLI-first, scrape only when needed**, and treat MCP-like tool calls as a last resort unless they’re executable/replayable (code).