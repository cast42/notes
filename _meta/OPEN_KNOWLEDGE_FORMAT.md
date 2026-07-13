# Open Knowledge Format in this repository

## TL;DR

`topics/` is the repository's Open Knowledge Format (OKF) 0.1 bundle. The rest
of the repository remains operational infrastructure for capture, meetings,
automation, memory, and agent behavior.

Start at [`topics/index.md`](../topics/index.md). It is the bundle entry point
and offers progressive disclosure: topic map first, concept files second.

## Bundle rules

- `topics/index.md` has exactly `okf_version: "0.1"` in its frontmatter.
- Nested `index.md` and any `log.md` are reserved navigation/history files and
  have no frontmatter.
- Every other Markdown file under `topics/`, including raw source captures, has
  parseable YAML frontmatter with a non-empty `type`.
- Ordinary relative Markdown links express relationships between concepts.
- A concept should be self-contained enough to load into an agent context on
  its own.

## Metadata compatibility

The existing note contract remains valid. These OKF-oriented fields improve
interoperability and may be added when useful:

| Existing field | OKF-oriented field |
| --- | --- |
| `source` / `source_url` / `canonical_url` | `resource` |
| `topics` | `tags` |
| `date` / `created_at` | `timestamp` |
| `title` | `title` |

Existing fields do not need to be rewritten in bulk. New writers should keep
the repository's required note fields and may add the OKF aliases.

Common concept types include `article`, `book`, `concept`, `investigation`,
`note`, `paper`, `procedure`, `source`, `tweet`, and `video`. OKF intentionally
allows producer-defined types; add one because it carries meaning, not to grow
a rigid ontology.

## Validation

Run:

```sh
uv run --with PyYAML python scripts/validate_okf.py
```

Conformance errors fail. Missing relative links are warnings so historical
notes can be repaired incrementally. CI runs the same validator when bundle
files change.
