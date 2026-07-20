---
title: "Human–AI collaboration as the unit of cognition"
date: 2026-07-20
timestamp: 2026-07-20
type: investigation
topics:
  - cognitive_patterns
tags:
  - human-ai-collaboration
  - collective-intelligence
  - skill-design
  - transactive-systems
  - evaluation
resource: "https://doi.org/10.1111/tops.12679"
description: "Investigates whether the cognitive-pattern workflow should evaluate and support the human–AI pair as a collaborative system rather than optimizing the agent's reasoning in isolation."
---

# Human–AI collaboration as the unit of cognition

## TL;DR

Yes, [*A Bigger Prize*](../organisation/2014-02-27_book_margaret-heffernan_a-bigger-prize.md) identifies a meaningful gap in the cognitive-pattern workflow: the current patterns improve how an agent structures reasoning, but they do not explicitly improve how a human and AI coordinate as one problem-solving system.

Do not add a collaboration pattern solely because the analogy is persuasive. First test a lightweight collaboration protocol on real tasks and measure the joint result against ordinary pattern use.

## Question

Could the book's argument—measure the coop rather than the individual chicken—improve the cognitive-pattern workflow for human–AI collaboration?

## Patterns selected

This investigation combines three patterns in sequence:

1. [Reason from first principles](reason_from_first_principles.md) defines what successful human–AI collaboration must accomplish.
2. [Evaluate incentives](evaluate_incentives.md) checks what the current workflow implicitly rewards.
3. [Find leverage points](find_leverage_points.md) identifies the smallest changes likely to improve joint performance.

## Evidence

Heffernan argues that individual competition and narrow scorekeeping can undermine trust, sharing, creativity, and collective output. The superchicken example makes the measurement problem vivid: the apparent productivity of one member may partly consist of costs imposed on the group.

Research on collective human–machine intelligence reaches a compatible conclusion through a different route. The COHUMAIN work treats collective intelligence as a property of a sociotechnical system and highlights functional systems for collective memory, attention, and reasoning. It emphasizes coordination of interdependent action, mutual understanding of cognitive states and resources, shared goals, and trust.

The current cognitive-pattern toolkit already offers strong procedures for selecting and combining reasoning methods. Its index also correctly warns that structured reasoning is not proof of a better conclusion. What it mostly evaluates, however, is whether the agent applied a procedure well—not whether the human and AI coordinated well.

## Findings

### 1. The current unit of improvement is too often the agent

Pattern instructions commonly improve the structure of the AI's analysis. But collaboration can still fail when the human's tacit knowledge, values, constraints, or uncertainty never enter the shared state.

The relevant outcome is not “Did the agent use the pattern correctly?” It is “Did the human–AI system reach a better, inspectable result with an appropriate division of work?”

### 2. More patterns can create a superchicken failure

Adding ever more sophisticated patterns may make the agent look more capable while increasing cognitive load for the human. Long pattern-heavy answers can transfer synthesis and verification work back to the user.

That is the direct analogue of selecting for individual output while ignoring the coop: agent sophistication rises, but joint throughput or decision quality may fall.

### 3. Collaboration requires transactive knowledge

A good pair needs a lightweight model of who knows what and who decides what:

- The human usually owns purpose, values, lived context, and consequential approval.
- The AI contributes retrieval, structured comparison, counterexamples, consistency checks, and execution within authorized scope.
- Both need visibility into assumptions, uncertainty, unresolved disagreement, and the current state of the work.

### 4. Trust should be calibrated through interaction

Trust is neither maximal deference nor constant suspicion. It improves when the AI exposes uncertainty and evidence, the human can correct the shared model cheaply, and corrections persist into subsequent work.

## Candidate improvement: a collaboration wrapper

Before adding a new cognitive pattern, test a short wrapper around existing patterns:

1. **Shared outcome** — state what completed success looks like for the human, including constraints and decision rights.
2. **Contribution map** — state what the human knows or decides and what the AI will retrieve, analyze, or execute.
3. **Smallest useful pattern set** — select only the procedures that fill a real reasoning gap.
4. **Inspectable joint state** — surface assumptions, evidence, uncertainty, and disagreements that could change the result.
5. **Decision handoff** — make clear what the AI completed, what remains a human judgment, and why.
6. **Collaboration retrospective** — record whether the process reduced work, improved the result, and produced reusable knowledge.

This wrapper should stay invisible on routine tasks and become explicit only when the stakes, ambiguity, or coordination burden justify it.

## Evaluation plan

Compare ordinary cognitive-pattern use with the collaboration wrapper on several substantive tasks. Evaluate the whole pair, not just the response:

- quality of the final decision or artifact;
- human correction and verification effort;
- number of important assumptions discovered late;
- calibration of confidence and trust;
- time to useful completion;
- reuse of context and learning in a later task.

The candidate should be revised or rejected if it merely lengthens responses, forces artificial role declarations, or fails to improve these joint outcomes repeatedly.

## Verdict

The book supports a real improvement direction, but not yet a new durable cognitive pattern. The next step should be a small, testable collaboration protocol that wraps pattern selection and combination. Promote it into a reusable skill or pattern only after repeated tasks show that it improves joint outcomes rather than just making the AI's reasoning more elaborate.

## Related concepts

- [A Bigger Prize](../organisation/2014-02-27_book_margaret-heffernan_a-bigger-prize.md)
- [Anthropic's Superchicken Problem](../organisation/2026-07-18_article_anthropic-s-superchicken-problem.md)
- [Select cognitive patterns](select_cognitive_patterns.md)
- [Combine cognitive patterns](combine_cognitive_patterns.md)

## Sources

- Margaret Heffernan, [*A Bigger Prize* publisher preview PDF](https://cdn.waterstones.com/special/pdf/9781471100758.pdf).
- [One-page summary of *A Bigger Prize*](https://static1.squarespace.com/static/5f60f3e1a140d716b34889c5/t/61976c5415797f39f85807af/1637313621185/heffernanabiggerprizestonecourtbriefsummary.pdf).
- Gupta et al., [“Fostering Collective Intelligence in Human–AI Collaboration: Laying the Groundwork for COHUMAIN”](https://pmc.ncbi.nlm.nih.gov/articles/PMC12093911/), open access under CC BY 4.0.
