---
type: "source_capture"
source_url: "https://arxiv.org/abs/2608.26263"
canonical_url: "https://arxiv.org/abs/2608.26263"
title: "Raw capture: SKILL.state: Scalable Long-Horizon Agent Skills"
date: "2026-09-18"
topics: ["agentic_coding"]
generated: {"by": "process:note-ingest", "at": "2026-09-20T11:26:28+02:00"}
sources:
  - {"id": "paper", "resource": "https://arxiv.org/abs/2608.26263"}
  - {"id": "paper-html", "resource": "https://arxiv.org/html/2608.26263"}
  - {"id": "x-post", "resource": "https://x.com/beamnxw/status/2101018409802580300"}
---

# Source capture

## X post

- Author: `beamnxw ./` (`@beamnxw`)
- Published: 2026-09-18 18:39:58 UTC
- URL: https://x.com/beamnxw/status/2101018409802580300
- The post recommends a Google paper proposing `SKILL.state` for long-horizon agent skills. It describes replacing append-only conversation history with explicit state updates, reducing cumulative tokens by 16× at 100 turns in the reported comparison, and addressing context poisoning by giving the model the skill specification, current structured state, and latest observation.
- The post quotes an X article at https://x.com/i/article/2100322887253348352 and a related post at https://x.com/beamnxw/status/2100486325564477856.
- An image was attached to the post. The note uses the linked paper as the primary technical source rather than treating the image as independent evidence.

## Primary paper

- Title: `SKILL.state: Scalable Long-Horizon Agent Skills`
- Authors: Sanket Badhe, Priyanka Tiwari, Jonghyun Chung
- arXiv: https://arxiv.org/abs/2608.26263
- HTML: https://arxiv.org/html/2608.26263
- Submitted 2026-08-26; revised version 3 on 2026-09-02; arXiv metadata states acceptance at EMNLP.

### Abstract-level capture

The paper presents `SKILL.state`, a runtime architecture for long-horizon agent skills. Instead of replaying an ever-growing dialogue, each step provides an immutable skill specification, a structured execution state, and the latest observation. The model proposes an action and a state update; validated state persists while the reasoning trace is discarded. The paper reports improved accuracy, substantially lower cumulative token use, and better robustness to noisy or adversarial context in its evaluated tasks.

### Technical capture

- Runtime input at step `t`: `A_t = (P, Σ_t, O_t)`, where `P` is the immutable skill specification, `Σ_t` is structured state, and `O_t` is the latest observation.
- The model emits a reasoning trace `R_t`, a state patch `ΔΣ_t`, and an action `a_t`.
- A deterministic validator applies the patch: `Σ_{t+1} = Σ_t ⊕ ΔΣ_t`.
- The reasoning trace is discarded after the validated update. The complete event history can still be retained by the runtime for logging and audit.
- If skill, state, and observation are bounded, per-step prompt footprint is `O(1)` and cumulative prompt complexity is `O(T)`; full-history replay grows as `O(T²)`.
- The InterCode CTF example uses fields such as discovered flags, tested hypotheses, active files, working directory, and command summary.

### Evaluation capture

The evaluated environments are SkillExecBench warehouse and simulated software-repository tasks, InterCode CTF, and Sierra τ-Bench Retail and Airline. Baselines include full Prompt/ReAct history, memory summaries, stateful/LangGraph-style execution, truncation, summary-capped history, and ReAct with LLMLingua compression.

Reported results include:

- Warehouse, 100 steps: `SKILL.state` 0.94 accuracy and 65,408 cumulative tokens versus 1,062,387 for the stateful baseline, a 16.2× reduction in that comparison.
- Warehouse, 200 steps: `SKILL.state` 0.94 accuracy and 122,384 cumulative tokens.
- Gemini-3-Flash public benchmarks: InterCode CTF 54.2% pass@1; τ-Bench Retail 58.3%; τ-Bench Airline 32.4%.
- Noise tests report stronger robustness for structured state than standard history-based prompts.
- External-drift tests report several recovery turns for history baselines and zero recovery steps for `SKILL.state` in the tested scenarios; a canceled-order scenario failed across runtimes.
- A budget-matched warehouse comparison reports `SKILL.state` at 0.94 accuracy with an approximately 1,800-token budget, while truncation, summary, and LLMLingua variants perform lower in that setup.
- In the Gemma-4-31B open-weight error taxonomy, failures were attributed mainly to premature state overwrite/deletion (68%), schema comprehension/type coercion (20%), and JSON syntax/format (12%).

The paper describes synthetic experiments with five generator seeds and reports extended-horizon differences at `p < 0.01`. These are paper-reported results, not an independent replication.

### Limitations capture

The paper identifies several boundaries:

- structured state must be a sufficient statistic for future execution;
- dynamic schema discovery is difficult;
- information not recognized as relevant may never be committed;
- current state is insufficient when historical trajectory, provenance, or audit detail is the task objective;
- multi-agent shared-state writes and merge conflicts are not evaluated;
- the runtime relies on the model proposing valid patches, so validation, rollback, and possibly grammar-constrained decoding are important.

## Interpretation boundary

The X post's 16× claim refers to the paper's 100-step warehouse comparison. It should not be generalized to every skill, model, horizon, schema, or workload. `SKILL.state` is best understood as explicit, validated task memory—not as a replacement for event logs, provenance records, or all forms of conversational context.
