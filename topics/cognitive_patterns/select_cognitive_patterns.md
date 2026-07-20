---
type: cognitive_pattern
title: Select cognitive patterns
date: 2026-07-20
timestamp: 2026-07-20
description: Choose the smallest reasoning procedure that fits the question, available evidence, stakes, and time.
topics:
  - cognitive_patterns
tags:
  - model-selection
  - problem-framing
  - reasoning
  - decision-making
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
status: experimental
---

# Select cognitive patterns

## TL;DR

Classify the question before choosing a cognitive pattern. Use one pattern when it covers the main need. Add another only when it answers a distinct question that the first pattern cannot answer.

## Use when

- The right reasoning procedure is unclear.
- A familiar pattern has stopped helping.
- The question spans several kinds of reasoning.
- The cost of choosing a poor method is high.

Skip this pattern when the fit is obvious or when direct reasoning is enough.

## Procedure

1. State the question and the decision or output it must support.
2. Classify the main need.
3. List the evidence and observations that are available now.
4. Note the stakes, time limit, and cost of a wrong answer.
5. Choose the pattern that best addresses the main need.
6. State what useful output the pattern should produce.
7. Check whether the pattern has a blind spot that changes the decision.
8. Add one complementary pattern only when it covers that blind spot.
9. Stop using a pattern when its questions no longer change the analysis.

## Problem map

| Need | Start with |
| --- | --- |
| Challenge an assumption | [Reason from first principles](reason_from_first_principles.md) |
| Check a broad claim | [Generate counterexamples](generate_counterexamples.md) |
| Separate plausible causes | [Test competing hypotheses](test_competing_hypotheses.md) |
| Revise confidence after new evidence | [Update beliefs with evidence](update_beliefs_with_evidence.md) |
| Explain recurring system behaviour | [Identify feedback loops](identify_feedback_loops.md) |
| Choose an intervention | [Find leverage points](find_leverage_points.md) |
| Predict responses to a rule or reward | [Evaluate incentives](evaluate_incentives.md) |
| Compare connected environments | [Compare ecosystems](compare_ecosystems.md) |
| Explain how practical skill grows | [Analyze capability accumulation](analyze_capability_accumulation.md) |
| Find risks before execution | [Run a pre-mortem](run_a_pre_mortem.md) |

## Output template

```text
Question:
Main need:
Available evidence:
Constraints:
Selected pattern:
Expected output:
Known blind spot:
Optional second pattern:
Reason for adding it:
```

## Failure modes

- Choosing a favourite pattern by habit.
- Using a pattern because its name appears in the question.
- Applying several patterns to appear thorough.
- Forcing a pattern onto a routine question.
- Keeping a pattern after it stops producing new information.
- Confusing a clear procedure with a correct conclusion.

## Evaluation

A good selection should:

- fit the main reasoning need;
- work with the evidence that is available;
- produce an output that supports the decision;
- use no more patterns than needed;
- make each added pattern's role clear.

## Related patterns

- [Combine cognitive patterns](combine_cognitive_patterns.md)
- [Generate counterexamples](generate_counterexamples.md)

## Sources

- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its model router and model selection skills.
