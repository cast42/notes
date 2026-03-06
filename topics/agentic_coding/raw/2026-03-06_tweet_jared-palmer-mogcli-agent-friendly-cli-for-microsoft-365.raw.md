---
type: tweet
source_url: "https://x.com/i/status/2029643407606563140"
canonical_url: "https://x.com/jaredpalmer/status/2029643407606563140"
title: Jared Palmer — mogcli (agent-friendly CLI for Microsoft 365)
author: Jared Palmer
handle: jaredpalmer
created_at: 2026-03-06
topics: [agentic_coding]
content_hash: 2c0aef002183b42782e9225a0cf6dc8df697250d72c9349411265c4954a08407
extracted_at: "2026-03-06T08:31:38"
extractor: browser-relay+x-readme
---

# Raw content

Source: https://x.com/jaredpalmer/status/2029643407606563140


Tweet:
"mogcli: an unofficial agent-friendly CLI for Microsoft M365 (h/t to @steipete’s for gogcli)"
Author: Jared Palmer (@jaredpalmer)
Date: 2026-03-05
URL: https://x.com/jaredpalmer/status/2029643407606563140

Linked repository:
https://github.com/jaredpalmer/mogcli

Extracted repo notes (README snapshot):
- mogcli is an unofficial Microsoft Graph CLI for Microsoft 365.
- Supports personal Microsoft accounts (MSA) and enterprise Entra ID accounts.
- Workloads: Mail, Calendar, Contacts, Groups, Tasks (Microsoft To Do), OneDrive.
- Auth modes: delegated user auth + enterprise app-only auth.
- Multi-profile support with one active profile, plus per-command profile override.
- Script-friendly output via --json and --plain.
- Includes interactive auth flows, non-interactive login, profile settings update.
- Progressive consent for scopes in delegated mode.
- --dry-run support for write operations in Mail, Calendar, and OneDrive.
- Install options: build from source, go install, Homebrew tap.
- Includes command groups for auth, mail, calendar, contacts, groups, tasks, onedrive, config, completion.

Repository positioning summary:
mogcli aims to make Microsoft 365 automation agent-friendly and shell-friendly, with stable output, explicit profile/auth handling, and enough breadth to script core personal/work workflows through Microsoft Graph.
