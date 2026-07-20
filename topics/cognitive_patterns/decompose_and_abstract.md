---
type: cognitive_pattern
title: Decompose and abstract
date: 2026-07-20
timestamp: 2026-07-20
description: Break a complex problem into manageable parts, recombine the results, and extract the operation that transfers to other problems.
topics:
  - cognitive_patterns
tags:
  - decomposition
  - abstraction
  - problem-framing
  - transfer
resource: "https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/3bca850386a3005c22134fa62fb3bad5_MITRES_6-011F14_art_insfin.pdf"
status: experimental
---

# Decompose and abstract

## TL;DR

Split a difficult problem into parts that can be understood or estimated separately. Recombine the parts without gaps or double counting. After the method works, name the operation that made it work and test whether the operation transfers to another domain.

## Use when

- The question is too large to reason about as one unit.
- Different parts need different evidence or methods.
- One part may dominate the answer.
- A successful solution may contain a reusable procedure.

Skip decomposition when the parts interact so strongly that separating them removes the behaviour being studied.

## Ways to divide a problem

- Divide a total by source, actor, place, process, or time.
- Divide a mechanism into inputs, transformations, outputs, and feedback.
- Divide a decision into objectives, constraints, options, and consequences.
- Divide an estimate into factors that can be measured or bounded separately.

## Procedure

1. State the output or decision the analysis must support.
2. Choose a way to divide the problem that matches how the system works.
3. Check that the parts cover the whole question without overlap.
4. Note important interactions between the parts.
5. Solve or estimate the easiest and most influential parts first.
6. Keep units, time periods, and definitions consistent.
7. Recombine the parts and identify which ones dominate the result.
8. Compare the combined result with a rough whole problem estimate.
9. Name the operation that made the decomposition useful.
10. Test the operation on a different example before treating it as a reusable pattern.

## Output template

```text
Question:
Required output:
Division rule:

Part:
Method or evidence:
Result or range:
Important interactions:

Recombined result:
Dominant part:
Whole problem check:
Transferable operation:
Different test case:
```

## Example

To estimate daily electricity demand from a truck fleet, divide the total into the number of active trucks, the average distance per truck, and the energy used per kilometre. Estimate each part from a suitable source, multiply the ranges, and compare the result with measured depot use. The transferable operation is to express a total as a count multiplied by use per item. Test the operation on a different problem, such as daily water use in a building, before treating it as general guidance.

## Failure modes

- Dividing the problem according to available data rather than its mechanism.
- Leaving gaps between the parts.
- Counting the same quantity in more than one part.
- Ignoring interactions that change the result.
- Spending equal effort on parts with very different effects.
- Naming an abstraction before the concrete method has worked.
- Assuming that a method transfers without testing another domain.

## Evaluation

A good decomposition should:

- make each part easier to examine;
- preserve the interactions that affect the conclusion;
- recombine without gaps or double counting;
- identify the parts that dominate the result;
- produce an operation that works on at least one different example.

## Related patterns

- [Select cognitive patterns](select_cognitive_patterns.md)
- [Approximate and check easy cases](approximate_and_check_easy_cases.md)
- [Reason from first principles](reason_from_first_principles.md)
- [Verify with independent estimates](verify_with_independent_estimates.md)

## Sources

- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md), especially its divide and conquer and abstraction methods.
