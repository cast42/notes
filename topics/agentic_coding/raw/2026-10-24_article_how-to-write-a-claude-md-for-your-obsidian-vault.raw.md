---
type: "source"
source_url: "https://x.com/cyrilXBT/status/2114057378001747980"
canonical_url: "https://x.com/i/article/2106438046602141696"
title: "How to Write a CLAUDE.md for Your Obsidian Vault"
author: "Cyril"
handle: "cyrilXBT"
created_at: "2026-10-24"
date: "2026-10-24"
topics: ["agentic_coding"]
tags: [claude-code, obsidian, agent-instructions, vault-safety]
resource: "https://x.com/i/article/2106438046602141696"
generated: {"by": "process:note-ingest", "at": "2026-10-25T07:42:06+00:00"}
sources:
  - id: "announcement-post"
    resource: "https://x.com/cyrilXBT/status/2114057378001747980"
  - id: "article"
    resource: "https://x.com/i/article/2106438046602141696"
  - id: "claude-code-memory-docs"
    resource: "https://code.claude.com/docs/en/memory"
content_hash: "7afa52a3669186a490aaea725b45a35b44fb45ce0991d070f48e3726dbb041cf"
extracted_at: "2026-10-25T07:42:06+00:00"
extractor: "FxTwitter API article payload and official Claude Code memory docs; paraphrased"
---

# Raw content

Source: https://x.com/i/article/2106438046602141696


Paraphrased extraction of Cyril's X article, not a verbatim reproduction of its course or full template.

## Purpose and structure

The article proposes using a root CLAUDE.md as an onboarding and instruction file for Claude Code working in an Obsidian vault. Its seven core questions are: who the owner is; what the vault is for; how folders are organized; how notes are written; what must not be changed; how answers should be presented; and what the current priorities are.

The author recommends describing folders and default destinations explicitly, using consistent filenames and a controlled tag list, preserving the owner's wording and opinions, linking related notes, protecting sensitive or read-only areas, and putting frequently changing priorities in a short section. Examples are offered for writing, founder, student, and research vaults. Folder-specific instruction files can hold local rules; the root file should remain concise.

## Suggested testing and maintenance

Before broad use, ask Claude to restate the vault rules and identify ambiguity; then test a single capture, a small batch, safety behavior, and a question whose answer is absent from the vault. Update instructions when recurring mistakes reveal a missing or unclear rule, and review priorities and obsolete rules periodically. The author also recommends keeping a backup.

## Cautions and current documentation

CLAUDE.md instructions guide behavior but do not enforce permissions. The article's proposed test that asks the agent to delete a note should only be performed on a disposable copy or synthetic test file—not on a real vault. A backup and authorization controls remain important.

The article says a root file is loaded each session and that folder-level files apply when work enters those folders. Current Claude Code docs clarify that files in the working directory and its parent directories load at launch, while nested CLAUDE.md files are discovered and loaded when Claude accesses files in their subtree. The docs also describe CLAUDE.md as context rather than enforced configuration, and currently recommend keeping each file under 200 lines; the article's 50–100-line target is a tighter rule of thumb, not an official limit.

The article is a practical course/promotional piece. It provides a template and test ideas, but no controlled results demonstrating that its template prevents damage or reliably improves vault organization.
