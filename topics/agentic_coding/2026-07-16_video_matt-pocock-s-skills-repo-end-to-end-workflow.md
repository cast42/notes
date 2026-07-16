---
type: video
date: 2026-07-16
timestamp: 2026-07-16
source_url: "https://youtu.be/M6mYodf0dJM"
canonical_url: "https://youtube.com/watch?v=M6mYodf0dJM"
resource: "https://youtube.com/watch?v=M6mYodf0dJM"
title: Matt Pocock’s skills repo — end-to-end workflow
author: Matt Pocock
handle: mattpocockuk
created_at: 2026-07-16
topics: [agentic_coding]
tags:
  - agent-skills
  - context-engineering
  - specification-driven-development
  - code-review
  - subagents
description: "Matt Pocock's workflow turns vague coding ideas into durable specs and context-sized tickets before implementation and independent review."
---

# Matt Pocock’s skills repo — end-to-end workflow

*Matt Pocock — @mattpocockuk*

## TL;DR

- Matt Pocock demonstrates the core workflow of his skills repository: install, configure, interview, specify, ticket, implement, and review.
- The workflow treats the context window as a limited smart zone and persists decisions in specs and tickets before clearing context between implementation slices.
- Fresh review subagents compare the result against both the original specification and repository standards.

## Highlights

- Install with `npx skills@latest add mattpocock/skills`.
- Start with `grill-with-docs` to turn a vague idea into shared understanding.
- Use `to-spec` and `to-tickets` when work spans multiple context windows.
- Implement one ticket per fresh context, then run code review against the spec.

## The main flow

1. **Install:** select the stable, public skills from [`mattpocock/skills`](https://github.com/mattpocock/skills), choose the target agent, and prefer project scope for teams or global scope for solo use.
2. **Configure:** run `setup-matt-pocock-skills` to choose an issue tracker, triage conventions, and single- or multi-context domain documentation. Local Markdown, GitHub, Jira, Linear, and other trackers can be adapted through configuration.
3. **Orient:** invoke `ask-matt` for guidance on which skill and sequence fit the work.
4. **Interview:** `grill-with-docs` explores the repository and asks questions until the human and agent share a concrete understanding of the change. It records durable context and architectural decisions.
5. **Choose the short or long path:** implement directly if the job fits comfortably in the remaining context window; otherwise persist the result with `to-spec`, then decompose it with `to-tickets`.
6. **Implement in slices:** each ticket should fit one fresh context window. Clear context between tickets instead of dragging a long, degraded conversation through the whole project.
7. **Verify independently:** the implementation flow runs builds and checks, then fresh review subagents compare the code against both the original acceptance criteria and repository standards.

## Why the workflow matters

### Context is an engineering budget

Pocock describes the useful portion of a context window as the model's “smart zone.” The exact threshold is model-dependent, but the design consequence is general: decompose work around coherent context-sized units, not arbitrary project-management granularity.

Specs preserve **where the project is going**; tickets preserve **how to get there**. This lets a new agent session regain intent without replaying the entire discovery conversation.

### Interview before planning

The workflow does not treat a vague prompt as a sufficient specification. `grill-with-docs` inspects the codebase and forces unresolved decisions into the open. A prototype is optional when discussion cannot settle a question with confidence.

### Review needs fresh eyes

The reviewing agent should not be the same context that authored the code. Pocock argues that agents tend to rationalize their own recent output. Fresh subagents reduce that bias and can check two separate dimensions:

- Did the implementation satisfy every requirement in the spec?
- Does it conform to the repository's coding standards and avoid common code smells?

## Practical caveats

- Most skills are deliberately user-invoked and have short descriptions; the complete installed set reportedly contributes only about 660 discovery tokens in the demonstrated setup.
- Project-level installation makes the skill set versionable and shared across a team; global installation is convenient for a solo developer.
- The video demonstrates the core flow, not every experimental skill in the repository.

## Links

- Permalink: [https://youtube.com/watch?v=M6mYodf0dJM](https://youtube.com/watch?v=M6mYodf0dJM)
- [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)
- [https://aihero.dev/s/4arzG4](https://aihero.dev/s/4arzG4)

## Raw

- Raw text: [timestamped YouTube transcript](raw/2026-07-16_video_matt-pocock-s-skills-repo-end-to-end-workflow.raw.md)
- Extractor: youtube-auto-captions
