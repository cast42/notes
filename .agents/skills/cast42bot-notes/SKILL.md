---
name: cast42bot-notes
description: Create and maintain notes in the cast42/notes repository with minimal YAML frontmatter, meaningful concept types, progressive disclosure, relative links, and Open Knowledge Format (OKF) 0.1 conformance. Use when capturing or summarizing articles, books, videos, posts, meetings, or references; creating or updating topic notes and indexes; moving notes; or normalizing and validating the knowledge repository.
---

# Notes workflow (cast42/notes)

## Respect the bundle boundary

Treat `topics/` as the OKF 0.1 bundle. Treat `inbox/`, `meetings/`, `refs/`,
`twil/`, `_meta/`, scripts, skills, and agent memory as supporting
infrastructure.

Start topic discovery at `topics/index.md`. Read the relevant nested `index.md`
before loading many concept files.

## Classify the file before writing

Apply these rules in order:

1. Keep `topics/index.md` frontmatter exactly:

   ```yaml
   ---
   okf_version: "0.1"
   ---
   ```

2. Give nested `index.md` and any `log.md` under `topics/` no frontmatter.
   Never create `README.md` as a topic index; use `index.md`.
3. Give every other Markdown file under `topics/`, including `raw/` captures,
   parseable YAML frontmatter with a non-empty `type`.
4. Give notes under `inbox/`, `meetings/`, and `refs/` the repository's minimum
   frontmatter.

## Write concept metadata

Use this minimum shape for ordinary notes and concepts:

```yaml
---
title: "..."
date: YYYY-MM-DD
type: article
topics:
  - knowledge_management
tags: []
---
```

- Derive `title` from the first H1, otherwise from the filename.
- Derive `date` from a leading `YYYY-MM-DD`, otherwise from the source date or
  last Git commit date.
- Infer `topics` from `topics/<topic>/`; use the filename stem for a file
  directly under `topics/`.
- Keep `tags: []` unless specific tags add retrieval value.
- Preserve existing metadata when editing. Do not rewrite notes only to rename
  fields.

Choose the narrowest honest `type`. Prefer source types such as `article`,
`book`, `paper`, `tweet`, and `video`; use `concept` for synthesized evergreen
knowledge, `investigation` for an active research trajectory, `procedure` for a
reusable method, `source` for a raw capture of uncertain kind, and `note` only
when no more meaningful type fits. Outside the bundle, use `inbox`, `meeting`,
or `reference` based on the containing area.

When useful, add OKF-oriented aliases without removing repository-native
fields:

- `resource` for `source`, `source_url`, or `canonical_url`
- `timestamp` for `date` or `created_at`
- `tags` alongside the repository's `topics`

## Structure for progressive disclosure

Write new notes in this order:

1. **TL;DR** in 2–5 lines.
2. **Key takeaways / what stuck** as bullets.
3. **Details** in focused sections, with quotes or timestamps when useful.
4. **Links / sources**.

Keep each concept self-contained enough for an agent to load independently.
Do not over-summarize deeper source material.

## Maintain the knowledge graph

- Use ordinary filesystem-relative Markdown links, not tool-specific wiki
  links.
- Resolve links relative to the file containing them; do not paste a
  repository-root path into a nested note.
- Link a new concept from its nearest topic `index.md` when that index exists.
- When creating a durable new topic directory, add a frontmatter-free
  `index.md` and link it from `topics/index.md`.
- Add cross-topic links only when they express a useful relationship.

## Route and name notes

- Put unprocessed captures in `inbox/`.
- Put durable concepts and curated source notes in `topics/<topic>/`.
- Put meeting notes in `meetings/` and reference lists in `refs/`.
- Use `YYYY-MM-DD_<source>_<author>_<short-title>.md` for date-specific notes.
- Otherwise use a stable, descriptive slug.
- Keep raw source material under `topics/<topic>/raw/` with frontmatter and a
  non-empty type.

For awkward source pages, try `https://r.jina.ai/http://<original-url>` or
`https://defuddle.md/?url=<original-url>` to obtain readable Markdown.

## Validate every topic change

After changing `topics/`, run:

```sh
uv run --with PyYAML python scripts/validate_okf.py
```

Fix all conformance errors. Also fix link warnings introduced by the current
change. CI runs the same validator.

To find legacy notes missing frontmatter, run the bundled normalizer in dry-run
mode; add `--apply` only when the requested task includes normalization:

```sh
python .agents/skills/cast42bot-notes/scripts/normalize_frontmatter.py
```

## Git hygiene

- Use `git mv` when moving notes.
- Keep content rewrites separate from mechanical metadata normalization when
  practical.
- Use short imperative commit messages, such as `Add note on ...` or
  `Normalize frontmatter`.
