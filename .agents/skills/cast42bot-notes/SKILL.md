---
name: "cast42bot-notes"
description: "Maintain cast42/notes with meaningful OKF metadata, links, validation, and safe Git hygiene."
---

# Notes workflow (cast42/notes)

## Respect the bundle boundary

Treat `topics/` as the OKF 0.1 bundle. Treat `inbox/`, `meetings/`, `refs/`,
`twil/`, `_meta/`, scripts, skills, and agent memory as supporting
infrastructure.

Before changing durable knowledge:
1. Read `DESIGN.md`.
2. Read `_meta/OPEN_KNOWLEDGE_FORMAT.md`.
3. Start discovery at `topics/index.md`.
4. Read the relevant nested `index.md`.
5. Search for an existing concept or canonical source URL before creating a file.

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
4. Give notes under `inbox/`, `meetings/`, and `refs/` the repository's
   minimum frontmatter.

## Write meaningful concept metadata

Use this shape for new durable concepts:

```yaml
---
title: "..."
date: YYYY-MM-DD
timestamp: YYYY-MM-DD
type: article
topics:
  - knowledge_management
tags:
  - progressive-disclosure
  - knowledge-graphs
resource: "https://canonical.example/source"
description: "One sentence explaining the durable idea and why it matters."
---
```

Metadata rules:

- Derive `title` from the first H1, otherwise from the filename.
- Derive `date` from a leading `YYYY-MM-DD`, otherwise from the source date.
- Set `timestamp` to the same value for new notes unless a more precise source
  timestamp is useful.
- Infer `topics` from `topics/<topic>/`; topics are broad repository
  placement categories.
- Add 2–6 concise `tags` that improve retrieval. Tags should name the concepts,
  mechanisms, practices, or entities a future reader would search for.
- Do not merely duplicate the topic name as the only tag.
- Avoid generic tags such as `article`, `notes`, `interesting`, `ai`, or
  `technology` unless they carry genuine discriminating value.
- Use lowercase kebab-case for tags.
- Empty `tags: []` is acceptable only when no honest retrieval tag can be
  inferred; this should be uncommon for curated durable concepts.
- Set `resource` to the canonical source URL for source-based notes.
- Add a one-sentence `description` that states the durable idea, not merely the
  media format.
- Preserve useful provenance extensions such as `author`, `source_url`,
  `canonical_url`, `created_at`, `content_hash`, and `extractor`.
- Preserve existing metadata when editing unless the task explicitly includes
  normalization or the edited concept is missing metadata required by the
  current contract.

Choose the narrowest honest `type`. Prefer source types such as `article`,
`book`, `paper`, `tweet`, and `video`; use `concept` for synthesized
evergreen knowledge, `investigation` for active research, `procedure` for a
reusable method, and `source` for a raw capture.

## Structure for progressive disclosure

Write curated notes in this order:

1. `# Title`
2. `## TL;DR` in 2–5 lines or bullets.
3. `## Key takeaways` / `## What stuck`.
4. Focused detail sections.
5. `## Related concepts` when local relationships materially help.
6. `## Sources` or `## Links`.
7. A relative link to the raw capture when one exists.

Keep each concept self-contained enough for an agent to load independently.
Do not over-summarize deeper source material. Keep source capture and synthesis
distinguishable.

## Maintain the knowledge graph

- Use ordinary filesystem-relative Markdown links, not tool-specific wiki links.
- Resolve links relative to the file containing them.
- Link a new concept from its nearest topic `index.md` when it improves
  navigation; indexes are curated maps, not exhaustive listings.
- Add reciprocal links when two concepts materially inform each other.
- When creating a durable topic directory, add a frontmatter-free `index.md`
  and link it from `topics/index.md`.
- Put local conceptual relationships in prose or a related section; keep
  external provenance in the sources section.

## Route and name notes

- Put unprocessed captures in `inbox/`.
- Put durable concepts and curated source notes in `topics/<topic>/`.
- Put meeting notes in `meetings/` and reference lists in `refs/`.
- Use `YYYY-MM-DD_<source>_<author>_<short-title>.md` for date-specific notes.
- Otherwise use a stable, descriptive slug.
- Keep raw source material under `topics/<topic>/raw/` with frontmatter and a
  non-empty type.
- For awkward pages, try Jina Reader or Defuddle to obtain readable Markdown.

## Validate every topic change

After changing `topics/`, run:

```sh
uv run --with PyYAML python scripts/validate_okf.py
```

Fix all conformance errors and all link warnings introduced by the change.
Run `git diff --check`. Inspect the exact staged paths before committing.

For legacy frontmatter discovery, run:

```sh
python .agents/skills/cast42bot-notes/scripts/normalize_frontmatter.py
```

Use `--apply` only when normalization is explicitly in scope.

## Git hygiene

- Pull or fetch the relevant branch before writing when remote changes are
  expected.
- Preserve unrelated worktree changes.
- Use `git mv` for moves.
- Stage explicit paths only; never use broad `git add .` in a dirty worktree.
- Keep content rewrites separate from mechanical normalization when practical.
- Use short imperative commit messages.
- For Lode's notes workflow, commit and push completed new notes without asking
  for extra confirmation.
