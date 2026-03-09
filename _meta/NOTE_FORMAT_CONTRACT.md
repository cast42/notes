# Note Format Contract (v1)

Purpose: keep notes machine-findable across agent/tool changes without forcing one rigid source schema.

## Scope
Applies to content notes under:
- `inbox/**`
- `topics/**` (except `README.md`, `_meta/**`, `raw/**` where raw has looser metadata)
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
