# Open Knowledge Format in this repository

## TL;DR

`topics/` is the repository's Open Knowledge Format (OKF) 0.2 bundle. The rest
of the repository remains operational infrastructure for capture, meetings,
automation, memory, and agent behavior.

Start at [`topics/index.md`](../topics/index.md). It is the bundle entry point
and offers progressive disclosure: topic map first, concept files second.

## Bundle rules

- `topics/index.md` has exactly `okf_version: "0.2"` in its frontmatter.
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
| `date` / `created_at` / legacy `timestamp` | Source dates, separate from `generated.at` |
| `title` | `title` |

Existing fields do not need to be rewritten in bulk. New writers should keep
the repository's required note fields and may add the OKF aliases.

Common concept types include `article`, `book`, `cognitive_pattern`, `concept`,
`investigation`, `note`, `paper`, `procedure`, `source`, `tweet`, and `video`.
OKF intentionally allows producer-defined types. Add one because it carries
meaning, not to grow a rigid ontology.

New captures record `sources` as a list of materials actually used and
`generated` as the producer and known time of the note's creation or meaningful
revision. The ingestion script identifies its formatting process as
`process:note-ingest`; it does not claim to know who wrote the supplied prose.
It retains `created_at`, writes the source date as `date` for weekly selection,
and does not invent verification events. New captures also include `resource`
and an empty `tags` list for later curation.

Preserve existing source dates and legacy body citations. Do not rename old
`timestamp` fields to `generated.at`: in this repository they often record
publication dates. New structured sources can coexist with readable body links.

The `cognitive_pattern` type identifies a reusable reasoning procedure. Treat
these notes as guidance for reasoning, not as factual evidence. Their
experimental state is recorded as `maturity: experimental`.

## Optional review metadata

- `verified` records actual content checks as a list of `{by, at}` events.
  Readers also accept a single mapping. Format validation does not verify claims.
- Actors use `human:<id>`, `process:<id>`, or `<producer>/<version>`.
- `status` is `draft`, `stable`, or `deprecated`. Missing status means stable;
  it does not imply that a person reviewed the note.
- `stale_after` is an absolute ISO 8601 datetime with an explicit UTC offset.
  A note is stale when the current time is on or after that instant.
- Generation, verification, and source modification timestamps also need
  UTC offsets. Publication dates remain separate local metadata.

Adopt these fields when their values are known and useful. Do not add historical
generation or verification events by guessing. Attested computations are
optional and are not implemented by this repository's tooling.

## Validation

Run:

```sh
uv run --with PyYAML python scripts/validate_okf.py
```

Conformance errors fail. The validator requires a root index as a local policy
and accepts declarations for 0.1 and 0.2. Optional metadata issues and missing
local links are warnings. It checks common source, actor, lifecycle, and date
fields without implementing a trust filter or the full computation contract.
Unknown keys and concept types are preserved and accepted. File-relative and
bundle-root Markdown links are checked; writers continue to use file-relative
links for portability in ordinary Markdown tools.

CI runs validation and focused compatibility tests. Run the tests locally with:

```sh
uv run --with PyYAML python -B -m unittest discover -s tests -v
```

## Specification

The [official OKF 0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
defines the format. This repository's required root declaration and curated
indexes are local conventions. Existing 0.1 concepts remain usable without
optional 0.2 metadata.
