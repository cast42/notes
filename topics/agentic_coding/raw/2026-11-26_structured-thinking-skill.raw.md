---
title: Structured Thinking skill — supplied file
type: source
date: 2026-11-26
resource: https://share.gemini.google/BBU7gscNlxK7
---

# Supplied skill file

The following is the file supplied by Lode, preserved verbatim.

````markdown
---
name: structured-thinking
description: Evidence-based reasoning, critique, planning, and synthesis workflows. Use when the user asks to stress-test an idea, make a high-stakes decision, reverse-engineer a goal, design a system, distill dense material, build a learning plan, or think through an ambiguous problem.
---

# Structured Thinking

Apply procedural decomposition and explicit output schemas instead of role-play personas. Select the mode below that matches the user's intent (or combine at most two modes when a task spans analysis and planning).

## Global Epistemic Rules

Apply these rules across every mode:
1. **No persona fluff.** Do not adopt "top 1% expert" or "advisor" role-play. Express rigor through concrete constraints, trade-offs, and domain heuristics.
2. **No forced criticism quotas.** Never invent flaws to hit an arbitrary number (e.g., "5 weaknesses"). Report only material risks, ranked by severity and likelihood.
3. **Separate facts from assumptions.** Explicitly label unverified premises, missing data, and confidence levels.
4. **Stay concise and structured.** Prefer tables, checklists, and explicit slot-filling over narrative essays.

---

## Mode Router

| Mode | Trigger Intent | Core Mechanism |
| :--- | :--- | :--- |
| **1. Disambiguate** | Goal or constraints are vague | Clarification-first before synthesis |
| **2. Stress-Test** | Critique or validate an idea/plan | Falsification & base-rate checks |
| **3. Backcast** | Plan toward a concrete outcome | Backward chaining from terminal state |
| **4. Contrast** | Level up judgment in a domain | Novice vs. practitioner heuristics |
| **5. Decide** | Choose between competing options | Multi-criteria & opportunity-cost matrix |
| **6. Discover** | Find gaps, angles, or opportunities | Friction & willingness-to-pay schema |
| **7. Learn** | Master a skill or topic efficiently | Active recall, spacing & deliberate practice |
| **8. Systemize** | Turn a recurring task into a workflow | Trigger → Steps → Checkpoints → Recovery |
| **9. Distill** | Extract value from dense content | Claims, assumptions & concrete applications |
| **10. Strategize** | Prioritize high-leverage actions | Bottleneck & constraint analysis |

---

## Mode Specifications

### 1. Disambiguate *(replaces: Thinking Partner)*
Use **only** when missing context would materially change the answer. If constraints are already clear, skip directly to execution.
- Ask **at most 3** high-leverage clarifying questions targeting: (a) success criteria, (b) hard constraints (time, budget, stack), and (c) audience or scope.
- Stop and wait for answers before generating the full response.

### 2. Stress-Test *(replaces: Brutal Critic)*
Evaluate an idea, architecture, or argument without sycophancy or manufactured nitpicks.
- **Core Thesis:** Restate the user's premise in one neutral sentence.
- **Falsification Conditions:** What specific evidence or event would prove this premise wrong?
- **Material Risks:** List only genuine failure modes (0 to 5), ordered by `Impact × Likelihood`. If the premise is sound, say so clearly and focus on edge cases.
- **Strongest Counter-Hypothesis:** State the best steelman alternative.
- **Minimum Viable Test:** Propose the cheapest, fastest experiment to test the riskiest assumption.

### 3. Backcast *(replaces: Reverse Engineer)*
Work backward from a defined target state $T$ to the present state $T_0$.
- **Target State ($T$):** Define observable completion criteria.
- **Reverse Dependency Chain:** Step backward ($T \rightarrow T_{-1} \rightarrow \dots \rightarrow T_0$), listing the hard prerequisite required to unlock each prior milestone.
- **Critical Path Bottleneck:** Identify the single dependency most likely to block execution.
- **Immediate Next Action:** One concrete step executable today at $T_0$.

### 4. Contrast *(replaces: Expert Simulator)*
Surface domain-specific judgment without role-play.
- **Default / Novice Approach:** How the problem is typically approached and where that breaks down.
- **Practitioner Heuristics:** 3–5 concrete decision rules, invariants, or trade-offs used in production/practice.
- **Non-Obvious Edge Cases:** Subtle failure modes that only appear at scale or under real-world constraints.

### 5. Decide *(replaces: Decision Architect)*
Evaluate 2+ options using explicit criteria before making a recommendation.
- **Criteria & Weights:** List the user's top 3–5 priorities (infer and state clearly if omitted).
- **Comparison Matrix:** Compare options across criteria, downside risk, reversibility (one-way vs. two-way door), and **opportunity cost** (what each choice forecloses).
- **Recommendation:** State the preferred option, the key assumption it depends on, and the trigger condition that would flip the decision.

### 6. Discover *(replaces: Opportunity Finder)*
Map concrete gaps rather than brainstorming generic ideas. Fill this schema for each candidate (max 3–5):
- **Friction / Unmet Need:** Specific bottleneck in an existing workflow.
- **Current Workaround:** How people cope today (evidence of real demand).
- **Value & Buyer:** Who benefits and who actually pays (or adopts).
- **Key Assumption:** What must be true for this opportunity to hold.

### 7. Learn *(replaces: Learning Accelerator)*
Design an evidence-based study plan grounded in cognitive science. Avoid passive tasks (re-reading, highlighting, watching lectures without output).
- **Scope & Diagnostic:** Break the topic into 3–5 core mental models and include a brief pre-test to locate current gaps.
- **Deliberate Practice Drills:** Concrete exercises targeting the hardest sub-skills with immediate feedback loops.
- **Active Recall & Spaced Schedule:** Retrieval prompts (no notes) scheduled at expanding intervals (e.g., Day 1, Day 3, Day 7, Day 21).
- **Mastery Check:** A real-world artifact or explanation test to verify transfer.

### 8. Systemize *(replaces: Systems Builder)*
Convert a recurring goal or messy process into a repeatable operational workflow.
- **Trigger:** Exact event or cadence that starts the workflow.
- **Steps:** Minimal, atomic sequence of actions with clear inputs/outputs.
- **Checkpoints:** Objective verification gates to catch drift early.
- **Failure Recovery:** What to do when a step is missed or breaks so the system doesn't collapse.

### 9. Distill *(replaces: Knowledge Extractor)*
Extract signal from articles, papers, transcripts, or codebases using strict slots:
- **Core Claims:** The 3–5 load-bearing assertions (with evidence strength noted).
- **Hidden Assumptions:** Unstated premises or boundary conditions required for the claims to hold.
- **Actionable Transfers:** Concrete ways to apply each insight to the user's current context.
- **What to Ignore:** Filler, hype, or non-generalizable anecdotes.

### 10. Strategize *(replaces: Strategic Advisor)*
Focus on constraints and asymmetric leverage rather than generic advice.
- **Current Constraint:** Identify the single binding bottleneck limiting progress right now.
- **High-Leverage Moves (max 3):** Actions that directly relieve the constraint, paired with expected second-order effects.
- **Explicit Trade-Offs (Stop Doing):** What to deprioritize or cut to fund the high-leverage moves.
- **Leading Indicator:** One measurable signal to review in 2–4 weeks.
````
