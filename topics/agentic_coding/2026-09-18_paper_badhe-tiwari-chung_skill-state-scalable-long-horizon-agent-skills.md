---
type: "paper"
source_url: "https://arxiv.org/abs/2608.26263"
canonical_url: "https://arxiv.org/abs/2608.26263"
title: "SKILL.state: Scalable Long-Horizon Agent Skills"
author: "Sanket Badhe, Priyanka Tiwari, Jonghyun Chung"
date: "2026-09-18"
topics: ["agentic_coding"]
tags: [long-horizon, agent-runtime, structured-state, context-management, tool-use]
resource: "https://arxiv.org/abs/2608.26263"
generated: {"by": "process:note-ingest", "at": "2026-09-20T11:26:28+02:00"}
verified: [{"by": "process:codex", "at": "2026-09-20T11:26:28+02:00"}]
sources:
  - {"id": "paper", "resource": "https://arxiv.org/abs/2608.26263"}
  - {"id": "paper-html", "resource": "https://arxiv.org/html/2608.26263"}
  - {"id": "x-post", "resource": "https://x.com/beamnxw/status/2101018409802580300"}
  - {"id": "quoted-article", "resource": "https://x.com/i/article/2100322887253348352"}
description: "A runtime architecture that replaces replayed agent transcripts with validated structured execution state, keeping prompts bounded across long-horizon skill execution."
maturity: "experimental"
---

# SKILL.state: scalable long-horizon agent skills

## TL;DR

The paper proposes replacing an agent's append-only conversation history with an explicit, structured execution state. At each step, the model receives the immutable skill specification, the latest validated state, and the newest observation. It proposes an action and a state update; a runtime validator applies the update, while the intermediate reasoning trace is discarded.

This changes the problem from replaying everything that happened to maintaining the smaller set of facts needed for the next decision. In the paper's experiments, this keeps prompt growth bounded and improves long-horizon performance, but only when the state schema captures what future steps need.

## The core procedure

For step `t`, the runtime gives the model:

1. the immutable skill specification `P`;
2. the structured execution state `Σ_t`; and
3. the latest external observation `O_t`.

The model returns a reasoning trace, an action, and a proposed state patch. A deterministic validator checks and applies the patch to produce `Σ_{t+1}`. The reasoning trace is not replayed into the next prompt.

The state schema is task-specific. In the paper's simulated CTF example, it includes discovered flags, tested hypotheses, active files, the working directory, and a command summary. The design therefore requires an explicit answer to: *which facts must survive from one step to the next?*

## Why it matters

Replay-based agents repeatedly pay for old context and can be distracted by irrelevant or misleading history. A validated state gives the model a compact operational view instead:

- **Bounded prompts:** if the skill, state, and observation remain bounded, each step has an `O(1)` prompt footprint and a run has `O(T)` cumulative prompt cost rather than the `O(T²)` growth of full-history replay.
- **Less context poisoning:** irrelevant, contradictory, or injected material need not remain in the active state once it has been filtered by the runtime.
- **Explicit memory semantics:** state fields make persistence inspectable. A harness can validate, audit, roll back, or compare updates instead of treating the entire transcript as memory.
- **A recovery boundary:** after external drift, the agent can update state from the latest observation rather than reasoning from a stale narrative.

This is more specific than summarization. A summary compresses history into prose; `SKILL.state` asks the designer to define a structured sufficient state for the task and to validate changes to it.

## Evidence reported by the paper

The authors evaluate warehouse tasks, InterCode CTF, and Sierra τ-Bench Retail and Airline tasks. Their reported results include:

- In a 100-step warehouse comparison, `SKILL.state` used 65,408 cumulative tokens versus 1,062,387 for the stateful baseline—about 16.2× fewer in that setup—and reached 0.94 accuracy.
- On the reported Gemini-3-Flash public-benchmark runs, `SKILL.state` scored 54.2% on InterCode CTF, 58.3% on τ-Bench Retail, and 32.4% on τ-Bench Airline. These are task- and model-specific results, not a general guarantee.
- In the paper's noise and external-drift tests, structured state was more robust than history-based baselines. The reported recovery test also found that history baselines could spend several turns recovering from drift, while `SKILL.state` recovered immediately in the tested scenarios.
- In an open-weight error analysis, most observed failures came from premature state overwrite or deletion, followed by schema/type errors and JSON-format errors. The state mechanism reduces context cost but creates a new state-management failure surface.

The 16× number shared in the X post is therefore best read as a result from one 100-step warehouse comparison, not as a universal property of the architecture.

## Design implications for a harness

The proposal fits naturally after the minimal LLM–tools–loop core described in [Omar Sar's minimal agent harness guide](2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.md):

1. Define the durable facts required by a skill before choosing a memory mechanism.
2. Keep the skill specification immutable and keep execution state separate from observations and actions.
3. Make state updates typed, minimal, validated, and reversible where possible.
4. Treat external observations as the source for refreshing state after drift; do not silently preserve stale assumptions.
5. Log state patches, validator decisions, and failures so that the harness remains inspectable.
6. Test long runs with injected noise, changed external conditions, missing observations, and incorrect proposed updates.

The useful shift is from “How much transcript can the context window hold?” to “What state is sufficient for the next decision, and how do we know it is valid?”

## Limits and failure modes

The paper's approach depends on a schema being sufficient for future execution. It is weaker when:

- the relevant state cannot be specified in advance and must be discovered dynamically;
- an important observation is never recognized and committed to state;
- the objective requires the historical trajectory, provenance, or an audit trail rather than only the current operational state;
- multiple agents write shared state and need conflict-resolution semantics; or
- the model proposes invalid, destructive, or premature patches.

Runtime validation and rollback help, but they do not solve a badly chosen schema. The paper evaluates single-agent settings; multi-agent shared state remains an open design problem.

## Assessment

`SKILL.state` is a strong candidate for the durable-state layer of long-horizon skills. Its main contribution is not simply shorter prompts; it makes the memory contract explicit and gives the runtime a place to enforce that contract. The central engineering risk moves from context-window overflow to state-schema design and update validation.

The reported gains are promising but bounded by the paper's tasks, models, schemas, and implementation. A practical harness should retain the full event log for debugging and provenance while exposing only validated task state to the model.

## Sources

- [Paper abstract and metadata](https://arxiv.org/abs/2608.26263)
- [Paper HTML](https://arxiv.org/html/2608.26263)
- [X post by beamnxw](https://x.com/beamnxw/status/2101018409802580300)
- [Quoted X article](https://x.com/i/article/2100322887253348352)

## Raw capture

- [Raw paper and X capture](raw/2026-09-18_paper_badhe-tiwari-chung_skill-state-scalable-long-horizon-agent-skills.raw.md)
