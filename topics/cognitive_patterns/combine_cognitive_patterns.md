---
type: cognitive_pattern
title: Combine cognitive patterns
date: 2026-07-20
timestamp: 2026-07-20
description: Combine a small number of reasoning procedures when each one covers a distinct part of a complex question.
topics:
  - cognitive_patterns
tags:
  - model-combination
  - synthesis
  - reasoning
  - decision-making
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
status: experimental
---

# Combine cognitive patterns

## TL;DR

Combine patterns only when one pattern leaves an important gap. Give each pattern a distinct role, decide how their outputs relate, and resolve disagreements instead of hiding them in a long summary.

## Use when

- The question spans several kinds of reasoning.
- The stakes justify checking a conclusion from another angle.
- One pattern finds the problem and another can guide the response.
- Two plausible approaches make different assumptions.

Use one pattern when it already answers the question.

## Ways to combine patterns

### In sequence

Use the output of one pattern as the input to the next.

Example: use [Identify feedback loops](identify_feedback_loops.md) to explain behaviour, then [Find leverage points](find_leverage_points.md) to choose an intervention.

### In parallel

Apply patterns independently and compare their conclusions.

Example: use [Evaluate incentives](evaluate_incentives.md) and [Generate counterexamples](generate_counterexamples.md) to review the same policy proposal.

### In opposition

Use one pattern to build a case and another to challenge it.

Example: use [Reason from first principles](reason_from_first_principles.md) to design an option, then [Run a pre-mortem](run_a_pre_mortem.md) to find how it could fail.

## Procedure

1. State the main question.
2. Apply the best fitting pattern first.
3. Name the remaining gap.
4. Choose a second pattern that addresses only that gap.
5. Decide whether the patterns will run in sequence, in parallel, or in opposition.
6. Record what each pattern contributes.
7. Compare where the results agree and disagree.
8. Resolve disagreements with evidence, scope conditions, or a decision rule.
9. State the combined conclusion and its uncertainty.

Use at most three patterns unless the task has separate parts that clearly require more.

## Output template

```text
Question:
Combination type:

Pattern 1:
Role:
Finding:

Pattern 2:
Role:
Finding:

Agreement:
Disagreement:
How the disagreement was resolved:
Combined conclusion:
Remaining uncertainty:
```

## Failure modes

- Adding patterns without naming their roles.
- Using several patterns that ask the same question.
- Blending incompatible assumptions without noticing.
- Counting agreement between similar patterns as independent support.
- Reporting every output without producing a combined conclusion.
- Continuing to add patterns after the decision is already clear.

## Evaluation

A good combination should:

- answer a question that one pattern could not answer alone;
- give every pattern a distinct role;
- preserve disagreements that affect the conclusion;
- show how evidence resolved a disagreement;
- remain shorter and clearer than separate full analyses.

## Related patterns

- [Select cognitive patterns](select_cognitive_patterns.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Update beliefs with evidence](update_beliefs_with_evidence.md)

## Sources

- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its model combination skill.
