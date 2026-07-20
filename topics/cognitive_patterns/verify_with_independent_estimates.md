---
type: cognitive_pattern
title: Verify with independent estimates
date: 2026-07-20
timestamp: 2026-07-20
description: Check a conclusion through different evidence, assumptions, or representations and use disagreement to find hidden errors.
topics:
  - cognitive_patterns
tags:
  - independent-estimates
  - cross-checking
  - human-ai-collaboration
  - verification
resource: "https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/3bca850386a3005c22134fa62fb3bad5_MITRES_6-011F14_art_insfin.pdf"
status: experimental
---

# Verify with independent estimates

## TL;DR

Estimate the same quantity or conclusion through different routes. The routes should use different evidence, assumptions, or representations. Investigate disagreement before averaging or choosing an answer.

## Use when

- A mistake would be costly.
- A result depends on several uncertain assumptions.
- A human and an AI can contribute different knowledge.
- A second route is cheaper than full verification.
- Agreement would narrow a useful range.

Skip the second estimate when the decision is easy to reverse, the first result is directly observable, or every available route depends on the same uncertain input.

## Independence test

Two estimates are usefully independent when a mistake in one route is unlikely to appear in the other route for the same reason.

Seek differences in at least one of these areas:

- Use different source data.
- Use a whole problem estimate and a sum of parts estimate.
- Use an empirical base rate and a model based on a mechanism.
- Use different units, representations, or boundary conditions.
- Use separate human experience and evidence the AI can access.

Repeated prompts to the same model are not independent when they preserve the same framing and evidence.

## Procedure

1. State the quantity, claim, or decision to verify.
2. Record the first estimate, range, method, and assumptions.
3. Choose a second route with different evidence, assumptions, or representation.
4. Keep the second route separate from the first result when anchoring is a risk.
5. Record the second estimate, range, method, and assumptions.
6. Put both results on the same scale and use the same definitions.
7. List shared assumptions that could make both routes wrong.
8. Explain agreement or disagreement before combining the results.
9. Identify the cheapest observation that can resolve an important difference.
10. Report the supported range, remaining disagreement, and decision effect.

## Human and AI protocol

1. The human records a rough expectation, range, or causal sketch before seeing the AI answer.
2. The AI uses a route based on different evidence or decomposition.
3. Both sides reveal their assumptions.
4. The human and AI investigate divergence before changing either estimate.
5. The final result preserves unresolved disagreement when the evidence cannot settle it.

Use the protocol only when the human has relevant knowledge and the cost of a shared mistake justifies the extra step.

## Output template

```text
Question or quantity:

Estimate 1:
Method:
Evidence:
Assumptions:

Estimate 2:
Method:
Evidence:
Assumptions:

Basis for independence:
Shared assumptions:
Agreement:
Disagreement:
Resolving observation:
Supported range:
Decision effect:
```

## Example

Estimate the annual electricity demand of an electric truck fleet through two routes. The first route multiplies the number of trucks by average annual distance and energy use per kilometre. The second route starts from charging station records and adjusts for the share of charging that happens elsewhere. Compare the ranges, list any shared assumptions about fleet activity, and investigate a large difference before using either estimate for grid planning.

## Failure modes

- Repeating the same method with different wording.
- Letting the first answer anchor the second estimate.
- Treating agreement as proof when both routes share an assumption.
- Averaging disagreement before explaining it.
- Choosing the preferred estimate without a decision rule.
- Paying for a second estimate when it cannot change the decision.

## Evaluation

A good independent check should:

- state how the routes differ;
- expose assumptions shared by both routes;
- use disagreement to guide the next observation;
- narrow uncertainty or reveal an error that affects the decision;
- justify the extra verification effort.

## Related patterns

- [Combine cognitive patterns](combine_cognitive_patterns.md)
- [Decompose and abstract](decompose_and_abstract.md)
- [Approximate and check easy cases](approximate_and_check_easy_cases.md)
- [Update beliefs with evidence](update_beliefs_with_evidence.md)

## Sources

- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md), especially its principle of intelligent redundancy.
