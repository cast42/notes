# Note Format Contract (v1)

Purpose: keep notes machine-findable across agent/tool changes without forcing one rigid source schema.

## Scope
Applies to content notes under:
- `inbox/**`
- `topics/**` (except OKF-reserved `index.md` and `log.md`; raw files may use
  looser metadata but still require a non-empty `type`)
- `meetings/**`
- `refs/**`

## Canonical required keys (normalized view)

Every source, concept, and investigation note must resolve to these fields:

- `title` (string)
- `date` (YYYY-MM-DD)
- `type` (`note` | `inbox` | `meeting` | `reference` | `tweet` | `article` | `cognitive_pattern`)
- `topics` (list of slugs)
- `tags` (list; allow empty `[]`)

Cognitive patterns follow a smaller contract because they are reusable
procedures rather than dated records. They require `title`,
`type: cognitive_pattern`, `description`, and `tags`. They may include `maturity`
when the procedure is still being tested.

## Accepted source/provenance keys (optional)
- `source` or `source_url`
- `canonical_url`
- `author`
- `handle`
- `created_at` (date or datetime)
- `people` (list)

## Compatibility mapping (future-proof)
When reading notes, agents should normalize with this precedence:

1. `date`:
   - frontmatter `date` if valid YYYY-MM-DD
   - else first `YYYY-MM-DD` prefix in filename
   - else first 10 chars of `created_at` if ISO-like
2. `source`:
   - `source`
   - else `source_url`
3. `topics`:
   - frontmatter list
   - else infer from `topics/<topic>/...` folder name
4. `type`:
   - frontmatter `type`
   - else infer by path (`inbox/`, `meetings/`, `refs/`, default `note`)

For interchange through the OKF bundle, readers should also recognize:

- `resource` as an alias for `source`, `source_url`, or `canonical_url`
- `tags` as the OKF-oriented equivalent of `topics`
- legacy `timestamp` as source metadata, often duplicating `date` or `created_at`

OKF 0.2 `generated.at` records the note's last meaningful content change.
It must not replace the source date or become a TWIL selection date. Do not
convert legacy `timestamp` values into generation events without evidence.

For new notes, record known provenance in `sources` and `generated`. Each
source entry has a `resource`; each generation event has `by` and, when known,
`at`. Use an actor in the form `human:<id>`, `process:<id>`, or
`<producer>/<version>` and datetimes with an explicit UTC offset.

Optional `verified` events record actual checks against sources. Accept a
single mapping or a list. Preserve absent verification rather than inventing
it. Lifecycle `status` uses `draft`, `stable`, or `deprecated`; absence means
stable, not verified. Pattern maturity uses `maturity: experimental`.
`stale_after` is an optional datetime with a UTC offset, inclusive at the
deadline. See the [OKF guide](OPEN_KNOWLEDGE_FORMAT.md).

Writers may include both repository-native and OKF-oriented fields. Do not
rewrite historical notes solely to add aliases.

## OKF bundle rules

`topics/` is an OKF 0.2 bundle:

- the root `topics/index.md` declares only `okf_version: "0.2"`
- nested `index.md` and `log.md` files have no frontmatter
- all other Markdown files have parseable frontmatter and a non-empty `type`
- links between concepts use ordinary relative Markdown links

Run `uv run --with PyYAML python scripts/validate_okf.py` after editing the
bundle.

## TWIL selection rule
To avoid misses, weekly inclusion should be based on normalized `date` (mapping above), not on a single raw key.

## Writer rule
When creating/updating normal notes, write the minimum frontmatter shape:

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

Additional keys are allowed, but this minimum must stay intact.

When creating a cognitive pattern, use:

```yaml
---
title: "..."
type: cognitive_pattern
description: "..."
tags:
  - ...
---
```

Do not add a date or source field unless it describes the pattern itself.
