---
type: video
source_url: "https://x.com/poteto/status/2102050467505430555"
canonical_url: "https://x.com/poteto/status/2102050467505430555"
title: "Lauren Tan: pstack, verification, and agent workflows"
author: "Lauren Tan"
handle: "poteto"
created_at: "2026-09-21"
date: "2026-09-21"
topics:
  - agentic_coding
tags:
  - agentic-engineering
  - coding-agents
  - verification
  - pstack
  - feature-maps
resource: "https://x.com/poteto/status/2102050467505430555"
description: "Lauren Tan and Matt Pocock describe how verification, agent-friendly environments, and feedback loops can support higher-throughput engineering while retaining quality controls."
generated:
  by: "process:codex"
  at: "2026-10-05T09:41:26+00:00"
sources:
  - id: "original-talk-post"
    resource: "https://x.com/poteto/status/2102050467505430555"
  - id: "lauren-interview-post"
    resource: "https://x.com/poteto/status/2106134336705843554"
  - id: "requested-follow-up"
    resource: "https://x.com/thecsguy/status/2106398397506916410"
  - id: "matt-pocock-summary"
    resource: "https://x.com/mattpocockuk/status/2103431302527508886"
  - id: "interview"
    resource: "https://www.youtube.com/watch?v=MN9dGgmLyso"
  - id: "official-pstack-plugin"
    resource: "https://github.com/cursor/plugins/tree/main/pstack"
  - id: "lauren-noodle-repository"
    resource: "https://github.com/poteto/noodle"
---

# Lauren Tan: pstack, verification, and agent workflows

*Lauren Tan — @poteto*

## TL;DR

- Lauren Tan presents high-volume agentic coding as a trust-and-environment problem, not a prompt trick: make the safe, correct path easy, and let agents gather evidence about their work.
- Her talk describes a verification CLI that runs the product and collects traces, paired with an automatically maintained feature map. The interview adds event-driven “outer loops” that gather bugs and context, plus coordinator agents that route work into coding “inner loops.”
- Her reported 2,500-PR month is not an audited quality metric. She says the work includes gardening and maintenance, advocates sampling landed code and fixing recurring failure patterns in the environment, and notes that autonomous merging depends on how well a domain can be verified.
- The videos’ machine-generated transcripts do not consistently resolve the PR count: the talk transcript hears “2,000,” while the interview discusses “2,500” and later “2,000 or however many.” Keep the headline figure attributed to her post, not as a precise independently verified count.

## What the talk and follow-up emphasize

### Build trust in layers

At the close of the talk, Lauren says this is the one takeaway she most wants viewers to remember: when correcting an agent, decide which layer should absorb the lesson (about 36:09–37:25). Her five-step sequence is:

- **Codebase:** Fix the example the agent will imitate. Prefer a clear paved path and refactor recurring bad patterns out of the code; architecture and data structures can make some mistakes impossible.
- **Static analysis:** Turn repeatable constraints into lint rules, compiler diagnostics, or CI checks. This is more reliable than asking the agent to remember a correction.
- **Rules / Bugbot:** Add explicit guidance and automated review for issues that static checks do not cover. These can still be missed or ignored, so they are not hard guarantees.
- **Skills:** Encode the team’s reusable workflow—how to investigate, implement, and verify—so the agent can apply the process in context. Treat skills as guidance, not enforcement.
- **Style guide:** Use human review for judgment and conventions that are not yet encoded elsewhere. Lauren cautions against relying on humans to catch every issue line by line at high PR volume.

The practical ordering is to fix the example or make a recurring mistake impossible first, then add increasingly softer enforcement and guidance. She calls the agent-oriented framework Dune: it favors one paved path, tight boundaries, and conventions that make the easy route the right one. A codebase is also memory: existing workarounds can spread as readily as good patterns. She gives banning comments in one framework as a project-specific example, after finding that agents used comments to justify band-aids instead of addressing underlying problems (about 19:00–26:20). This is her team’s design choice, not a general recommendation to ban comments.

### Verification is the core feedback loop

The original talk starts with manual Chrome performance tracing and heap snapshots becoming a bottleneck. Lauren’s first verification skill taught an agent to run the app through Chrome DevTools Protocol, collect traces and performance evidence, and iteratively improve hotspots (about 2:55–9:55). Its reusable CLI avoids having each agent recreate bespoke scripts; the feature map records what the product does and how users reach features, including UI paths, and is kept current by automation (about 10:15–12:20). Together, the map helps interpret vague reports while the CLI lets the agent reproduce behavior and gather evidence.

She distinguishes checking functional correctness from assessing performance or code quality. Product-specific verification skills provide empirical feedback; engineering playbooks and skills encode how the team wants work done. Her emphasis is to make the agent exercise the application itself, not merely assert that its code is correct.

### Scale context and work, not just agents

In the interview, Lauren describes an “outer loop” that pulls signals and context from sources such as bug reports, Slack, and monitoring into work, and an “inner loop” where agents investigate, implement, and verify changes (about 34:00–46:50). Coordinator or “chief of staff” agents can route and contextualize tasks; the aim is to teach agents to answer more of their own questions rather than make the human relay every detail. Matt’s “context, not control” framing captures this: invest in clear intent and a capable environment rather than continuous micromanagement.

She also describes sampling rather than inspecting every landed change: inspect code regularly and rigorously, look for recurring shortcuts, then improve constraints, linting, types, or skills in the environment (about 50:25–55:20). If several agents repeat a failure, treat it as evidence of an environmental gap, not just an individual agent mistake. She explicitly says the setup takes significant work and is not an easy switch to “dark factory” automation.

### pstack and the throughput claim

Lauren’s X post reports 2,500 PRs shipped in a month. The interview clarifies that these were not 2,500 features: she mentions bug fixing, gardening, and other maintenance, and describes work triggered by external signals as well as product development. The interview discusses PRs being merged after the verification loop, with review sampling afterward. The recordings do not independently establish the denominator, defect/revert rate, review burden, or durable user impact. The talk’s automatic-verification claim should therefore be understood as her account of one verifiable software context, not proof that the same autonomy is safe in every domain. She says one-way-door changes are harder to automate when they cannot be made effectively verifiable (about 57:00–60:40).

In their interview, Lauren and Matt treat skills as workflows distilled into language. Lauren recommends reviewing one’s own agent transcripts for repeated corrections and interventions, then turning useful lessons into reusable skills or lint rules. She describes her Recall skill as a way to mine earlier conversations for relevant context when beginning a new chat (about 61:00–65:25). She sees the two skill collections as complementary and encourages adapting them, not adopting them wholesale. The official [pstack plugin](https://github.com/cursor/plugins/tree/main/pstack) is one implementation; its existence does not validate the throughput claim.

## Links

- [Lauren Tan’s original X video post](https://x.com/poteto/status/2102050467505430555)
- [Lauren’s interview announcement and link](https://x.com/poteto/status/2106134336705843554) · [YouTube interview with Matt Pocock](https://www.youtube.com/watch?v=MN9dGgmLyso)
- [Thecsguy’s follow-up post](https://x.com/thecsguy/status/2106398397506916410)
- [Matt Pocock’s written recap](https://x.com/mattpocockuk/status/2103431302527508886)
- [Official pstack plugin and documentation](https://github.com/cursor/plugins/tree/main/pstack)
- [Noodle, Lauren’s public agent-orchestration repository mentioned in the interview](https://github.com/poteto/noodle)

## Raw

- Transcript notes: [timestamped paraphrases and extraction provenance](https://github.com/cast42/notes/blob/main/topics/agentic_coding/raw/2026-09-21_video_lauren-tan-pstack-verification-and-agent-workflows.raw.md)
- Extractor: local `whisper.cpp` `base.en` model on audio from both linked videos; timestamps are approximate, and automated speech recognition can mishear names or numbers. The full transcripts were used for this summary but are not included in the public note.
