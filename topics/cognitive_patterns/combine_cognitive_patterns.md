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

Combine patterns only when one pattern leaves an important gap. Give each pattern a distinct role, decide how their outputs relate, and resolve disagreements instead of hiding them in a long summary. When parallel patterns are used for verification, their evidence, assumptions, or representations must differ.

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

Parallel routes provide a stronger check when they can fail for different reasons. Record their different evidence, assumptions, or representations. Also record any shared assumption that could make both routes wrong.

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
7. For parallel verification, state why the routes are independent enough to add information.
8. Record assumptions that the routes share.
9. Compare where the results agree and disagree.
10. Resolve disagreements with evidence, scope conditions, or a decision rule.
11. State the combined conclusion and its uncertainty.

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

Basis for independence:
Shared assumptions:
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
- Repeating the same prompt and calling the second answer an independent check.
- Averaging conflicting results before explaining the difference.
- Reporting every output without producing a combined conclusion.
- Continuing to add patterns after the decision is already clear.

## Evaluation

A good combination should:

- answer a question that one pattern could not answer alone;
- give every pattern a distinct role;
- explain why parallel routes can fail for different reasons;
- identify assumptions shared by the routes;
- preserve disagreements that affect the conclusion;
- show how evidence resolved a disagreement;
- remain shorter and clearer than separate full analyses.

## Related patterns

- [Select cognitive patterns](select_cognitive_patterns.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Update beliefs with evidence](update_beliefs_with_evidence.md)
- [Verify with independent estimates](verify_with_independent_estimates.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its model combination skill.
- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md), especially its principle of intelligent redundancy.
