# Notes Consistency Task (burned-in checklist)

Use this before saying a note set is done or before generating TWIL.

## 1) Validate frontmatter coverage
- Check note files have YAML frontmatter.
- Ensure canonical keys resolve: `title`, `date`, `type`, `topics`, `tags`.

## 2) Normalize by compatibility mapping
- Accept legacy keys (`source_url`, `created_at`, path-inferred topic/type).
- Do not silently drop notes because `date` is missing if filename/created_at can resolve it.

## 3) Weekly/TWIL guardrail
- For target week range, list all files whose normalized date falls in range.
- Compare included count vs generated TWIL highlights count.
- If mismatch: stop and report missing files before publishing TWIL.
- TWIL links must be repo-relative from `twil/` to notes, e.g. `../topics/...` (never `topics/...`).

## 4) Link integrity test (required before publish)
- Run link check on files created/updated in the run:
  - `scripts/check_markdown_links.py twil/<week-file>.md <new-or-updated-note>.md ...`
- If any dangling local link appears, fix links before commit.

## 5) Drift watch
- If new metadata shapes appear, update `_meta/NOTE_FORMAT_CONTRACT.md` mapping.
- Keep canonical minimum stable; evolve via compatibility layer, not breaking changes.
