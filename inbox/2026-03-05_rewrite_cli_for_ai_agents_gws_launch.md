---
title: "Rewrite your CLI for AI agents (Google Workspace CLI launch + reactions)"
date: 2026-03-05
type: inbox
topics:
  - ai-agents
  - cli
tags: []
---

# Rewrite your CLI for AI agents (Google Workspace CLI launch + reactions)

## TL;DR
Justin Poehnelt argues that CLIs should be designed agent-first (or dual-path), not just retrofitted for humans.
Core design themes: raw JSON payloads, runtime schema introspection, strict input validation, context-window-aware output, and safety rails like dry-run/sanitization.
The post is paired with Gabor Cselle’s launch post for `@googleworkspace/cli` and commentary from Peter Steinberger and Guillermo Rauch comparing/endorsing implementation trade-offs.

## Key takeaways / what stuck
- Agent DX and human DX are orthogonal: keep human-friendly UX, but make machine paths first-class.
- Raw payload input (`--json` / `--params`) reduces translation loss and maps directly to API schemas.
- Runtime introspection (`schema`/`describe`) is better than stale prompt-packed docs.
- Safety must assume hallucinated/adversarial inputs (path traversal, encoded garbage, malformed IDs).
- Output discipline matters for agents: field masks and stream-friendly formats (e.g., NDJSON).
- A practical migration path exists for existing CLIs (JSON output, validation, schema, fields, dry-run, skills, MCP).

## Details

### Article summary (Justin Poehnelt)
The article frames AI agents as a distinct CLI user class with different needs from humans:
- **Predictable IO** over convenience abstractions
- **Machine-readable structure** over prose/tables
- **Introspection at runtime** over static docs
- **Defensive validation** against hallucinated inputs
- **Token/context optimization** via selective fields and incremental processing

The Google Workspace CLI (`gws`) is presented as a reference implementation with:
- raw JSON payload support
- schema discovery from API discovery docs
- field-mask guidance
- input hardening
- dry-run mode
- optional response sanitization
- multi-surface support (CLI/MCP/extensions/env)

### X announcement (Gabor Cselle)
> “We shipped a CLI for all of Google Workspace. For humans and AI Agents. Drive, Gmail, Calendar, and every Workspace API. npm install -g @googleworkspace/cli”

### X comment (Peter Steinberger)
Peter notes this is impressive and compares it to his motivation for building `gog`; he questions whether heavier JSON command structure is always better and mentions running evaluations to compare what works best for agents.

### X comment (Guillermo Rauch)
Rauch calls the CLI “very well implemented” and “thorough,” highlighting dynamic command registration, agent-oriented setup automation, and MCP daemon support, while also linking Justin’s article.

## Links / sources
- Article: https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/
- X announcement: https://x.com/i/status/2029428483974459843
- X comment (Peter Steinberger): https://x.com/i/status/2029363714642837806
- X comment (Guillermo Rauch): https://x.com/i/status/2029371455012773978
- oEmbed (announcement capture): https://publish.twitter.com/oembed?url=https://x.com/i/status/2029428483974459843
- oEmbed (comment capture, Peter): https://publish.twitter.com/oembed?url=https://x.com/i/status/2029363714642837806
- oEmbed (comment capture, Rauch): https://publish.twitter.com/oembed?url=https://x.com/i/status/2029371455012773978
