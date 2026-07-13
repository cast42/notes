# Repository design

## Purpose

This repository is a filesystem-native knowledge system shared by humans and
agents. It is designed to capture material quickly, turn selected material into
durable concepts, and make those concepts easy to discover without loading the
entire repository into context.

The repository controls the ideas behind the knowledge system—its boundaries,
invariants, and information flow—while leaving individual tools and agents free
to implement those ideas in different ways.

## Design principles

1. **Markdown is the durable interface.** Knowledge should remain readable and
   editable without a particular application, database, model, or agent.
2. **Capture and curation are different modes.** Fast capture should not be
   blocked by the standards required for durable knowledge.
3. **Progressive disclosure protects attention.** Start with topic maps and
   summaries; load detailed concepts and raw sources only when needed.
4. **Paths identify concepts.** Stable, descriptive paths are the portable
   identity layer. Renames should be deliberate and performed with `git mv`.
5. **Links form the graph.** Ordinary relative Markdown links express useful
   relationships without introducing a proprietary graph syntax.
6. **Metadata supports interchange, not ontology theater.** Require only what
   tools need, preserve useful source metadata, and avoid elaborate schemas
   that do not improve retrieval or reasoning.
7. **Automation enforces invariants, not taste.** Validators should reject
   malformed knowledge while leaving room for human judgment about structure,
   prose, and significance.
8. **Raw material and synthesis remain distinguishable.** Preserve provenance
   while allowing curated notes to become independent, reusable concepts.

## System boundaries

The repository has five cooperating layers.

### 1. Human and agent operating context

- `AGENTS.md` defines how agents work in the repository.
- `SOUL.md`, `USER.md`, and memory files preserve relationship and session
  context. They are private operating context, not portable knowledge.
- `.agents/skills/` and `skills/` contain reusable workflows.

This layer guides behavior but does not belong to the OKF bundle.

### 2. Capture and working material

- `inbox/` holds unprocessed captures and incomplete thinking.
- `meetings/` holds dated interaction records and action context.
- `refs/` holds reference lists and supporting collections.

Material may remain here indefinitely. Promotion is valuable only when a note
has durable meaning or repeated usefulness.

### 3. Durable knowledge bundle

`topics/` is the Open Knowledge Format 0.1 bundle and the repository's portable
knowledge surface.

- `topics/index.md` is the entry point.
- Nested `index.md` files provide topic-level progressive disclosure.
- Concept files contain one reasonably self-contained idea, source, procedure,
  investigation, person, or other meaningful unit.
- `raw/` directories preserve source captures separately from curated notes.
- `log.md` records significant changes to the bundle structure.

Only this layer claims OKF conformance. Operational files elsewhere in the
repository do not need to behave like concepts.

### 4. Derived views

`twil/` and other generated summaries are views over knowledge, not canonical
sources. They may select, compress, and reorganize notes, but corrections
should normally be made in the source concept and regenerated downstream.

### 5. Maintenance and validation

`scripts/` contains ingestion, promotion, export, link checking, and validation
tools. `.github/workflows/` runs repository checks in CI.

Tools may change. The Markdown contracts and design invariants should remain
stable enough that a replacement tool can reconstruct the system.

## Knowledge flow

The normal path is:

```text
source or thought
  -> capture
  -> normalize metadata
  -> curate into a self-contained concept
  -> link from the nearest topic map
  -> connect related concepts
  -> validate
  -> surface through searches and derived views
```

Not every capture must complete the flow. The system compounds knowledge when
curated concepts are revisited, corrected, linked, and synthesized—not merely
when more files are accumulated.

## Concept contract

Every Markdown file under `topics/`, except reserved `index.md` and `log.md`
files, must have parseable YAML frontmatter with a non-empty `type`.

Repository-native fields support local workflows:

- `title`
- `date`
- `type`
- `topics`
- `tags`

OKF-oriented fields improve interchange when useful:

- `resource`
- `timestamp`
- `description`

Source-specific provenance such as `author`, `source_url`, `canonical_url`,
`created_at`, `content_hash`, and `extractor` may remain as extensions.

Choose types for meaning, not storage location. Examples include `article`,
`book`, `concept`, `investigation`, `paper`, `procedure`, `source`, `tweet`,
and `video`. Organize durable notes primarily by subject; express media format
through `type`.

## Navigation and graph design

Topic indexes are deliberately small maps, not generated file listings. They
should identify the most useful concepts, describe why each matters, and link
to related areas.

Concept files should link to local related concepts when the relationship will
help a future reader or agent. Links must resolve relative to the containing
file. External sources belong in a source section, while local relationships
belong in a related section or the relevant prose.

This design allows an agent to:

1. Read `topics/index.md`.
2. Select one topic index.
3. Load a few relevant concepts.
4. Follow explicit relationships only when more context is needed.

## Agent write protocol

When adding durable knowledge, an agent should:

1. Read this file, the relevant skill, and the nearest topic index.
2. Search for an existing concept before creating another file.
3. Decide whether the material belongs in capture, durable knowledge, or a
   derived view.
4. Write progressive-disclosure content: TL;DR, takeaways, details, sources.
5. Preserve provenance and choose the narrowest honest concept type.
6. Add ordinary relative links in both directions when two concepts materially
   inform each other.
7. Update the nearest index when the new concept improves topic navigation.
8. Run the OKF validator and repair errors and newly introduced link warnings.

The repository-specific implementation lives in
`.agents/skills/cast42bot-notes/SKILL.md`.

## Validation invariants

The validator checks the ideas that tools must agree on:

- the bundle root declares OKF 0.1 and nothing else;
- reserved nested indexes and logs have no frontmatter;
- concept frontmatter parses to a mapping and has a non-empty type;
- relative Markdown targets exist.

Run:

```sh
uv run --with PyYAML python scripts/validate_okf.py
```

CI runs the same validation when the bundle or validator changes.

## Intentional tradeoffs

- Date-prefixed filenames are retained for provenance and stable capture even
  though purely semantic filenames can be easier to read.
- Topic folders are producer-defined and may evolve; no global ontology is
  imposed.
- Raw captures remain inside the bundle and therefore require a type, but they
  may carry looser metadata and less polished content.
- Link warnings are reported separately from conformance errors so historical
  repairs can be incremental. New changes should not introduce warnings.
- Indexes are curated by humans and agents rather than generated, because their
  purpose is selection and explanation rather than completeness.

## Non-goals

This repository is not intended to become:

- a graph database;
- a mirror of every source consumed;
- a rigid universal taxonomy;
- a requirement that every capture become evergreen;
- a proprietary agent-memory format;
- a substitute for tests, source code, or operational systems of record.

## Evolution

Change this design when repeated use exposes a real limitation. Prefer a small
explicit contract change plus migration and validation over silent convention
drift. Record structural changes in `topics/log.md`, and keep old readers in
mind when renaming fields or paths.

This file applies the design-document principle described in
[Antirez's "Control the ideas, not the code"](topics/agentic_coding/2026-07-13_article_control-the-ideas-not-the-code.md): preserve the mental model and constraints that future humans and agents need to understand and extend the system.
