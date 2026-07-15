# Notes

This is my personal knowledge repository: a capture system around a portable
Open Knowledge Format bundle.

Read [`DESIGN.md`](DESIGN.md) for the repository's mental model, boundaries,
knowledge flow, and invariants.

## Structure

- `inbox/` — agent + human scratchpad (daily capture)
- [`topics/`](topics/index.md) — the OKF 0.1 knowledge bundle and its entry point
- `meetings/` — dated meeting notes
- `refs/` — reference material (papers, links)
- `_meta/` — tags, glossary, conventions
- `scripts/` — ingestion, maintenance, and validation tools

## Conventions

- Use ISO dates: `YYYY-MM-DD.md`
- Prefer short sections + bullets
- Capture first, organize later
- Use ordinary relative Markdown links between related concepts
- Run `uv run --with PyYAML python scripts/validate_okf.py` after changing `topics/`

See [the repository design](DESIGN.md),
[the OKF repository guide](_meta/OPEN_KNOWLEDGE_FORMAT.md), and the
[note format contract](_meta/NOTE_FORMAT_CONTRACT.md) for details.
