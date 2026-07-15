---
type: cognitive_pattern
title: Reason From First Principles
description: Reconstruct an argument from basic constraints, mechanisms, and objectives rather than analogy or convention.
tags:
  - reasoning
  - first-principles
  - design
  - engineering
status: experimental
---

# Reason From First Principles

## Purpose

Use this pattern when conventional assumptions may be outdated, copied, or poorly matched to the problem.

## Use when

- A field relies heavily on inherited rules of thumb.
- New technology changes old constraints.
- Competing solutions are discussed mainly through analogy.
- You need to separate physical, economic, and institutional constraints.

## Procedure

1. Define the objective precisely.
2. List non-negotiable constraints.
3. Separate physical laws from current conventions.
4. Identify the relevant units and quantities.
5. Derive the minimum requirements for a viable solution.
6. Generate multiple architectures that satisfy them.
7. Add economic and operational constraints.
8. Compare the architectures under realistic scenarios.
9. Test sensitivity to uncertain assumptions.
10. Reintroduce historical evidence and practical knowledge.

## Constraint categories

- Physical
- Economic
- Temporal
- Operational
- Regulatory
- Human
- Strategic

## Failure modes

- Pretending assumptions do not exist.
- Ignoring tacit operational knowledge.
- Re-deriving well-known facts badly.
- Using "first principles" as rhetoric.
- Omitting institutional and behavioural constraints.
- Treating a mathematically elegant solution as deployable.

## Example

### Truck charging versus battery swapping

Start with:

- required daily energy;
- acceptable downtime;
- payload impact;
- station utilization;
- grid connection capacity;
- battery degradation;
- route predictability.

Then derive which architecture is viable under which operating profile instead of asking which technology is fashionable.

## Evaluation

A good first-principles analysis should:

- distinguish laws from conventions;
- expose key assumptions;
- quantify the main constraints;
- generate more than one solution;
- reconnect the result to empirical evidence.

## Related Patterns

- [Generate Counterexamples](generate_counterexamples.md)
- [Compare Ecosystems](compare_ecosystems.md)
- [Evaluate Incentives](evaluate_incentives.md)
