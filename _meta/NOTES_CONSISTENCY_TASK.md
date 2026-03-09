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

## 4) Drift watch
- If new metadata shapes appear, update `_meta/NOTE_FORMAT_CONTRACT.md` mapping.
- Keep canonical minimum stable; evolve via compatibility layer, not breaking changes.
