---
type: "video"
source_url: "https://x.com/poteto/status/2102050467505430555"
canonical_url: "https://x.com/poteto/status/2102050467505430555"
title: "Lauren Tan: pstack, verification, and agent workflows"
author: "Lauren Tan"
handle: "poteto"
created_at: "2026-09-21"
date: "2026-09-21"
topics: ["agentic_coding"]
tags: ["agentic-engineering", "coding-agents", "verification", "pstack", "feature-maps"]
description: "Transcript-derived source notes on verification, agent-friendly environments, and feedback loops in higher-throughput engineering."
resource: "https://x.com/poteto/status/2102050467505430555"
generated: {"by": "process:codex", "at": "2026-10-05T09:33:13+00:00"}
sources:
  - {"id": "original-talk-post", "resource": "https://x.com/poteto/status/2102050467505430555"}
  - {"id": "lauren-interview-post", "resource": "https://x.com/poteto/status/2106134336705843554"}
  - {"id": "requested-follow-up", "resource": "https://x.com/thecsguy/status/2106398397506916410"}
  - {"id": "matt-pocock-summary", "resource": "https://x.com/mattpocockuk/status/2103431302527508886"}
  - {"id": "interview", "resource": "https://www.youtube.com/watch?v=MN9dGgmLyso"}
  - {"id": "official-pstack-plugin", "resource": "https://github.com/cursor/plugins/tree/main/pstack"}
  - {"id": "lauren-noodle-repository", "resource": "https://github.com/poteto/noodle"}
content_hash: "10a1f8fbe3e92f944f461ea2722ef5e6af87252a2a32ee540cd15376d04d2999"
extracted_at: "2026-10-05T09:33:13+00:00"
extractor: "whisper.cpp base.en run locally on audio from both recordings, plus source-post metadata. Full transcripts used for analysis but not published; paraphrases below are timestamped navigation aids, not verbatim transcript."
---

# Raw content

Source: https://x.com/poteto/status/2102050467505430555


# Brief source excerpts

## Lauren Tan's original talk post
Date: 2026-09-21
URL: https://x.com/poteto/status/2102050467505430555
Excerpt: “here's how i shipped 2,500 PRs last month to production”

## Follow-up post by thecsguy
Date: 2026-10-03
URL: https://x.com/thecsguy/status/2106398397506916410
Excerpt: “Probably the best interview of 2026. @poteto and Matt are both awesome”

## Lauren Tan's interview announcement
Date: 2026-10-02
URL: https://x.com/poteto/status/2106134336705843554
Excerpt: “i had a lot of fun chatting with @mattpocockuk today about how i was able to land 2,500 PRs last month!”
YouTube: https://www.youtube.com/watch?v=MN9dGgmLyso

## Transcript-based notes (paraphrased; timestamps approximate)

### Lauren Tan's original talk — 38:01

- 00:13 — ASR hears “2,000 pull requests to production”; this differs from the 2,500 figure in her X post. Treat either number as an attributed claim, not an audited metric.
- 00:19–06:45 — She frames scale as trust: moving from a few agents to many without confidence creates bugs and regressions. She began by automating performance investigation that had made her the manual bottleneck.
- 07:00–12:30 — Verification ranges from running the product and collecting empirical evidence to harder formal methods. Her first verification skill used Chrome DevTools Protocol; a reusable CLI collects repeatable traces, and an automatically maintained feature map gives agents product/UI context for vague reports.
- 12:40–18:55 — Correctness, performance, and code quality need distinct evidence. She lays out a trust-building progression: good codebase patterns; structural constraints; static analysis/CI; rules, review bots, and skills; then human style-guide review. Human-only review does not scale as the sole safeguard.
- 19:00–26:35 — Dune encodes paved paths and tight boundaries. Existing anti-patterns can propagate through agent imitation; her examples include preventing bad patterns structurally, writing lint rules to stop regressions, and assigning ongoing “gardening” to clean the codebase.
- 32:30–36:45 — Product/event integrations can trigger agents, while environment, rules, and skills compound. She closes by urging teams to turn repeated corrections into the strongest suitable safeguard in that progression.

### Lauren Tan and Matt Pocock interview — approximately 66 minutes

- 05:10–09:30 — Lauren describes skills as a way to externalize her own workflows. Matt and Lauren argue domain expertise remains valuable: stating intent and goals clearly is a key bottleneck.
- 10:00–11:10 — They discuss language as a compressed carrier of intent; Matt highlights avoiding tautological/useless tests as a memorable example of precise guidance.
- 15:00–19:55 — The Michelin-kitchen metaphor keeps human accountability for the final product while agents take on work. Lauren calls verification the most important skill: give agents “hands and eyes” to run the application, inspect results, debug, and iterate; the loop depends on that feedback.
- 20:00–24:45 — A skill-specific CLI makes deterministic steps repeatable and leaves judgment to the model, instead of having every agent rebuild scripts. Verification skills become shared, maintained team infrastructure.
- 25:00–34:00 — They return to environment design, Dune, constraints, and context. Lauren describes app-specific architecture and clear boundaries as ways to make correct behavior the default.
- 34:00–46:50 — She explains outer and inner loops: gather external context (bug reports, Slack, monitoring) and feed it into coding/verification work. Coordinator agents route tasks and help agents answer their own questions; not every task should be parallelized just for its own sake.
- 47:00–50:00 — PRs include gardening and maintenance, not just features. One recurring-pattern workflow buffers findings in a document for periodic synthesis rather than immediately spawning fixes for every issue.
- 50:25–56:55 — Review shifts from inspecting every output to rigorous sampling and correcting the environment when multiple agents repeat a failure. Lauren says full automation takes substantial investment; she describes verifier agents that exercise the product, find regressions, and iterate before merge, while she reviews landed changes later and reverts or adjusts as needed.
- 57:00–60:40 — Reversibility and verifiability set the boundary: software may be automatable when evidence is strong, but hard-to-verify domains and one-way-door changes need more caution.
- 61:00–66:15 — They recommend mining prior agent transcripts for recurring interventions and turning them into skills, checks, or rules. Skills are adaptable workflows, not magic packages to adopt unchanged.

### Extraction caveat

These notes derive from automatic speech recognition (`whisper.cpp`, `base.en`) on the two recordings; verify exact quotations, names, and numbers against the linked videos. The complete generated transcripts are kept out of this public repository; only concise paraphrases and timestamps are retained.
