---
type: tweet
source_url: "https://x.com/i/status/2049169905186910307"
canonical_url: "https://x.com/subramanya/status/2049169905186910307"
title: markdownfs, an open source in-memory filesystem for agents
author: Subramanya N
handle: subramanya
created_at: 2026-04-30
topics: [agentic_coding]
content_hash: 950259e4970f956b2e92a790a7f2abf96898916416dfc6ffe8e1dbf2cd840dd2
extracted_at: "2026-04-30T07:35:34"
extractor: fxtwitter+github-readme
---

# Raw content

Source: https://x.com/subramanya/status/2049169905186910307


Post: @olvrgln https://github.com/subramanya1997/markdownfs opensource version for it
Author: Subramanya N (@subramanya)
URL: https://x.com/subramanya/status/2049169905186910307
Original ask URL: https://x.com/i/status/2049169905186910307
Created: Tue Apr 28 16:52:31 +0000 2026
Engagement at capture: 128 likes, 3 reposts, 1 quote, 302 bookmarks, 14,284 views

Referenced repo:
- https://github.com/subramanya1997/markdownfs
- Title: markdownfs
- Repo description: A high-performance, concurrent markdown database built in Rust. Supports Unix-like commands, Git-style versioning with content-addressable storage, disk persistence, multi-user permissioning, HTTP/REST API, and MCP for AI agents.

What the repo claims:
- In-memory virtual filesystem specifically for Markdown files.
- Multiple interfaces: CLI/REPL, HTTP server, MCP server for agent tooling.
- Shared concurrent core with multi-reader/single-writer access.
- Built-in version control semantics: commit, log, revert, status.
- Search and filesystem primitives: grep, find, tree, mkdir, write, move, delete.
- Multi-user and permission model with users, groups, chmod/chown-style controls.
- Positioned explicitly as an agent workspace layer with durable markdown memory, inspectable artifacts, rollback, and shared surfaces.

Why it matters for agents:
- It is trying to turn agent memory/workspace into a first-class markdown-native system instead of an opaque database.
- MCP exposure makes it directly usable from agent clients like Cursor or Claude.
- The combination of durable markdown artifacts, search, permissions, and version history is a strong fit for multi-agent or human+agent collaboration.
- The design is notable because it treats Markdown not just as output format but as the storage substrate.

Caveats:
- The X post itself is very short and mostly just points to the repo as an open-source version.
- Most substance here comes from the linked GitHub repository description and docs-visible README content.
