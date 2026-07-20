# Notes

This is my personal knowledge repository: a capture system around a portable
Open Knowledge Format bundle.

Read [`DESIGN.md`](DESIGN.md) for the repository's mental model, boundaries,
knowledge flow, and invariants.

## Structure

- `inbox/` contains the agent and human scratchpad for daily capture.
- [`topics/`](topics/index.md) contains the OKF 0.1 knowledge bundle and its entry point.
- `meetings/` contains dated meeting notes.
- `refs/` contains reference material such as papers and links.
- `_meta/` contains tags, the glossary, and conventions.
- `scripts/` contains ingestion, maintenance, and validation tools.

## Knowledge Objects

The bundle contains four complementary knowledge objects:

- Sources capture information from a specific origin.
- Concepts consolidate knowledge about an idea.
- Investigations document reasoning about a specific question.
- [Cognitive Patterns](topics/cognitive_patterns/index.md) capture reusable ways of thinking.

Each object serves a different purpose. Cognitive patterns guide how humans and agents reason with concepts and sources. They do not replace evidence or duplicate factual content.

## Conventions

- Use ISO dates: `YYYY-MM-DD.md`
- Prefer short sections + bullets
- Capture first, organize later
- Use ordinary relative Markdown links between related concepts
- Run `uv run --with PyYAML python scripts/validate_okf.py` after changing `topics/`

See [the repository design](DESIGN.md),
[the OKF repository guide](_meta/OPEN_KNOWLEDGE_FORMAT.md), and the
[note format contract](_meta/NOTE_FORMAT_CONTRACT.md) for details.

## Sources and influences

The [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills)
repository informed the selection, combination, belief updating, pre-mortem,
and hypothesis testing procedures in the cognitive patterns. The
[local source note](topics/cognitive_patterns/2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
explains what changed and why patterns remain reasoning guidance rather than
proof that an answer is correct.

Sanjoy Mahajan's
[*The Art of Insight in Science and Engineering*](topics/cognitive_patterns/2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md)
informed the decomposition, abstraction, approximation, easy case, and
independent verification procedures in the cognitive patterns.
