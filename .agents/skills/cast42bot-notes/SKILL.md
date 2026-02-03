---
name: cast42bot-notes
description: Create and maintain notes in the cast42/notes repo with minimal YAML frontmatter, consistent filenames, and progressive disclosure structure (TL;DR first). Use when asked to capture content (videos, articles, posts), add summaries/takeaways, move notes to the right topic folder, or normalize existing notes to the repo’s minimum format.
---

# Notes workflow (cast42/notes)

## Minimum note format

For any *note* file (anything under `inbox/`, `meetings/`, `refs/`, `topics/` except README/_meta), ensure it has YAML frontmatter **at the very top**:

```yaml
---
title: "..."
date: YYYY-MM-DD
type: note
topics:
  - ...
tags: []
---
```

Guidance:
- Keep edits minimal: add frontmatter without rewriting content.
- Prefer `title` from the first `# H1` heading; otherwise derive from filename.
- Prefer `date` from a leading `YYYY-MM-DD` in the filename; otherwise use the last git commit date for that file.
- `type`:
  - `inbox` for `inbox/**`
  - `meeting` for `meetings/**`
  - `reference` for `refs/**`
  - `note` for `topics/**`
- `topics`:
  - For `topics/<topic>/...` → include `<topic>`
  - For `topics/<file>.md` → include the filename stem (e.g., `duckdb`)
- Keep `tags: []` unless you have strong confidence in specific tags.

## Progressive disclosure (structure)

When writing new notes, follow this order:

1. **TL;DR** (2–5 lines)
2. **Key takeaways / what stuck** (bullets)
3. **Details** (sections with headings; include quotes/timestamps when available)
4. **Links / sources**

Don’t over-summarize; the goal is skimmable top sections with deeper detail below.

## Where to put new notes

- Quick capture / unprocessed: `inbox/`
- Topic notes: `topics/<topic>/` if a subtopic exists, otherwise `topics/`
- Meeting notes: `meetings/`
- Reference lists: `refs/`

## Filenames

Prefer stable, descriptive slugs.
- If date-specific: `YYYY-MM-DD_<source>_<author>_<short-title>.md`
- Otherwise: `<topic>.md` or `<short-title>.md` within the topic folder.

## Git hygiene

- Use `git mv` when moving notes.
- Commit messages: imperative, short (e.g., “Add note on …”, “Normalize frontmatter”).
