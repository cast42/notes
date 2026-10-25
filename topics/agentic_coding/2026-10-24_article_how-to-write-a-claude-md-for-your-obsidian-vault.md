---
type: "article"
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
description: "Cyril offers a section-by-section template and test plan for vault-specific Claude Code instructions; current docs and safe testing practices qualify several claims."
generated: {"by": "process:note-ingest", "at": "2026-10-25T07:42:06+00:00"}
sources:
  - id: "announcement-post"
    resource: "https://x.com/cyrilXBT/status/2114057378001747980"
  - id: "article"
    resource: "https://x.com/i/article/2106438046602141696"
  - id: "claude-code-memory-docs"
    resource: "https://code.claude.com/docs/en/memory"
---

# How to Write a CLAUDE.md for Your Obsidian Vault

*Cyril — @cyrilXBT*

## TL;DR

- Use CLAUDE.md as a concise onboarding document for a vault: identity and purpose, folder map, note conventions, safety boundaries, answer preferences, and current focus.
- Test the instructions incrementally on a sandboxed copy before trusting them on a real vault; instructions do not replace backups or enforced controls.
- The linked course is practical advice, not an evaluated method. Its test asking Claude to delete a note must only use disposable test data.

## Highlights

- The article recommends a controlled note format, explicit folder destinations, preserving the owner’s voice, and scoped folder rules.
- Its test ladder moves from explaining the rules, to one capture, a batch, safety checks, and an answerability check.
- Current Claude Code docs clarify that instructions are context rather than enforcement, and distinguish startup-loaded files from nested files loaded when their subtree is accessed.

## The proposed instruction file

The course treats CLAUDE.md as an onboarding brief that makes implicit vault conventions explicit. Its seven sections cover:

1. Who the owner is and what the vault is for.
2. The folder map, including where new notes go and which areas are read-only.
3. Note conventions: one idea per note, naming, summaries, a controlled tag set, links, and preserving the owner's wording.
4. Safety boundaries for deletion, edits, moves, and renames.
5. Preferred answer format and how to cite vault notes.
6. Current priorities, refreshed periodically.

The sample includes separate templates for writing, founder, student, and research vaults. It also recommends folder-level instructions for rules that apply only within one part of the vault, keeping the root file short (its rule of thumb is 50–100 lines), and revising it when recurring mistakes expose a missing or unclear rule.

## Test it safely

The suggested sequence is to ask Claude to restate the rules and flag ambiguity; try one capture; try a small batch; check that an answer unsupported by the vault is acknowledged as unknown; and verify safety behavior. Do not perform destructive tests on valuable notes: use a disposable copy and synthetic files. Make a backup before experiments.

CLAUDE.md is instruction context, not a permission boundary. The current Claude Code docs say files in the working directory and its parents load at launch, while nested instruction files are loaded when Claude accesses files within their subtree. The docs also suggest staying under 200 lines per file; the article's lower line target is an author recommendation. For hard restrictions, use permission settings or hooks rather than relying on prose instructions alone.

## Limits

The linked article is a promotional course with a useful template, not a controlled evaluation. It does not demonstrate that the proposed structure prevents accidental edits or improves organization across vaults. Adapt its examples to the vault's actual folders and conventions, and verify behavior on a safe copy before trusting it with real data.

## Links

- Permalink: [https://x.com/i/article/2106438046602141696](https://x.com/i/article/2106438046602141696)
- [https://x.com/cyrilXBT/status/2114057378001747980](https://x.com/cyrilXBT/status/2114057378001747980)
- [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- [2026-10-19_article_sergii-makarevych_agent-skill-evals.md](2026-10-19_article_sergii-makarevych_agent-skill-evals.md)
- [2026-08-16_tweet_the-elements-of-style-as-a-source-for-the-plain-writing-skill.md](2026-08-16_tweet_the-elements-of-style-as-a-source-for-the-plain-writing-skill.md)
- [Boris Cherny's Claude Code tips](2026-02-03_x_bcherny_how_to_use_claude_code.md) — also recommends evolving CLAUDE.md after corrections, while this course focuses on vault-specific structure and safety.

## Raw

- Raw text: [topics/agentic_coding/raw/2026-10-24_article_how-to-write-a-claude-md-for-your-obsidian-vault.raw.md](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-10-24_article_how-to-write-a-claude-md-for-your-obsidian-vault.raw.md)
- Extractor: FxTwitter API article payload and official Claude Code memory docs; paraphrased

## My notes

The strongest pattern here is not the particular folder taxonomy. It is making ownership boundaries explicit: tell the agent what it may organize, what must remain untouched, when to stop and ask, and how to preserve provenance and the owner's voice. Then test those instructions before scaling up.
