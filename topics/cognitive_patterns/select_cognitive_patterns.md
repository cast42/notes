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
maturity: experimental
sources:
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-model-router/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Select cognitive patterns

## TL;DR

Use direct reasoning when no cognitive pattern would improve the work. Otherwise, classify the question and choose one pattern for the main need. Add another only when it answers a distinct question that the first pattern cannot answer.

## Use when

- The right reasoning procedure is unclear.
- A familiar pattern has stopped helping.
- The question spans several kinds of reasoning.
- The cost of choosing a poor method is high.

Skip this pattern when the fit is obvious or when direct reasoning is enough.

## Procedure

1. State the question and the decision or output it must support.
2. Classify the main need.
3. Check whether the question must be decomposed before choosing a specialized pattern.
4. List the evidence and observations that are available now.
5. Note the stakes, time limit, and cost of a wrong answer.
6. Choose the pattern that best addresses the main need, or choose none when direct reasoning is enough.
7. State what useful output the pattern should produce.
8. Check whether the pattern has a blind spot that changes the decision.
9. Add one complementary pattern only when it covers that blind spot.
10. State when to abandon the pattern. If it forces a poor fit or adds no useful information, reconsider the choice once, then use direct reasoning if no better fit exists.

When two candidates seem equally suitable, compare the evidence they need, the time available, and your ability to apply them correctly. Prefer the simpler adequate procedure. Treat a pattern's name appearing in the question as a clue, not sufficient reason to use it.

## Problem map

| Need | Start with |
| --- | --- |
| Answer a routine question or carry out an agreed next step | Use direct reasoning without a named pattern. |
| Break a complex question into parts | [Decompose and abstract](decompose_and_abstract.md) |
| Simplify while recording what is lost | [Approximate and check easy cases](approximate_and_check_easy_cases.md) |
| Check a result through a different route | [Verify with independent estimates](verify_with_independent_estimates.md) |
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
Selected pattern or none:
Expected output:
Known blind spot:
Optional second pattern:
Reason for adding it:
Abandon or reconsider when:
```

## Failure modes

- Choosing a favourite pattern by habit.
- Using a pattern because its name appears in the question.
- Applying several patterns to appear thorough.
- Forcing a pattern onto a routine question.
- Keeping a pattern after it stops producing new information.
- Repeatedly selecting new patterns instead of taking the next supported action.
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
- [Decompose and abstract](decompose_and_abstract.md)
- [Generate counterexamples](generate_counterexamples.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Model router in version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-model-router/SKILL.md). The former model selection skill is now included in the router.
- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md), especially its divide and conquer and abstraction methods.
