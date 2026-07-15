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
Every note must resolve to these fields:
- `title` (string)
- `date` (YYYY-MM-DD)
- `type` (`note` | `inbox` | `meeting` | `reference` | `tweet` | `article`)
- `topics` (list of slugs)
- `tags` (list; allow empty `[]`)

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
- `timestamp` as an alias for `date` or `created_at`

Writers may include both repository-native and OKF-oriented fields. Do not
rewrite historical notes solely to add aliases.

## OKF bundle rules

`topics/` is an OKF 0.1 bundle:

- the root `topics/index.md` declares only `okf_version: "0.1"`
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
