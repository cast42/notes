---
type: cognitive_pattern
title: Approximate and check easy cases
date: 2026-07-20
timestamp: 2026-07-20
description: Build a simple model, state what it leaves out, and test it against units, boundaries, and easy cases before trusting it.
topics:
  - cognitive_patterns
tags:
  - approximation
  - dimensional-analysis
  - easy-cases
  - sensitivity-analysis
resource: "https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/3bca850386a3005c22134fa62fb3bad5_MITRES_6-011F14_art_insfin.pdf"
status: experimental
---

# Approximate and check easy cases

## TL;DR

Keep the structure that drives the answer and leave out details that are unlikely to change the decision. Record what was left out, where the approximation may fail, and which cheap check would reveal failure. Test the model in easy cases before adding detail.

## Use when

- An exact answer is expensive or hides the main mechanism.
- A rough range is enough for the decision.
- The problem contains many details with unequal effects.
- You need to check a formula, model, or general claim quickly.

Skip approximation when a discarded detail can cause irreversible harm, when the decision sits near a hard threshold, or when an exact answer is cheap.

## Procedure

1. State the question and the precision needed for the decision.
2. Identify the variables and relationships that are likely to dominate.
3. Check that the units of the proposed relationships are consistent.
4. Replace secondary variation with simple values, shapes, or bounds.
5. Record every important detail that was discarded.
6. Explain why each discarded detail is probably secondary in this case.
7. Estimate the size or direction of the error when possible.
8. Derive the approximate answer or range.
9. Test zero, one, symmetry, boundary, and extreme cases that fit the problem.
10. Vary the uncertain inputs and discarded details.
11. Add precision only where the conclusion is sensitive.

## Approximation record

```text
Question:
Precision needed:
Dominant structure retained:
Details discarded:
Why they are secondary:
Expected error or direction of bias:
Boundary where the approximation fails:
Cheap check that would reveal failure:
Approximate answer or range:
Decision supported:
```

## Easy case checks

- Set a quantity to zero or one.
- Compare very small and very large values.
- Test a symmetric or balanced case.
- Remove a constraint, then make the constraint binding.
- Remove feedback, then make feedback dominant.
- Check whether the answer changes in the expected direction.

Use only checks that fit the mechanism. Passing an unrelated easy case adds no confidence.

## Example

Estimate charging time as required energy divided by charging power. Keep the energy need and average usable power. Leave out charging losses and power reduction near a full battery, but record both omissions. The estimate should approach zero when required energy approaches zero, and it should grow when usable power falls. If losses or power reduction can move the result across a scheduling limit, replace the simple model with a more detailed one.

## Failure modes

- Starting with exact calculation before identifying the dominant structure.
- Discarding a term because it is inconvenient rather than small.
- Mixing units, definitions, or time periods.
- Hiding discarded information from the final result.
- Reporting more digits than the assumptions support.
- Choosing easy cases that the model was designed to pass.
- Keeping an approximation after sensitivity checks change the decision.

## Evaluation

A good approximation should:

- state the precision needed for the decision;
- preserve the structure that controls the answer;
- list the important information that was discarded;
- identify where the approximation can fail;
- pass relevant unit, boundary, and easy case checks;
- remain stable across plausible changes to secondary details.

## Related patterns

- [Decompose and abstract](decompose_and_abstract.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Reason from first principles](reason_from_first_principles.md)
- [Verify with independent estimates](verify_with_independent_estimates.md)

## Sources

- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md), especially its methods for dimensions, lumping, scaling, and easy cases.
