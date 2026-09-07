---
type: cognitive_pattern
title: Reason From First Principles
description: Reconstruct an argument from basic constraints, mechanisms, and objectives rather than analogy or convention.
tags:
  - reasoning
  - first-principles
  - design
  - engineering
maturity: experimental
sources:
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-first-principles/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Reason From First Principles

## Purpose

Use this pattern when conventional assumptions may be outdated, copied, or poorly matched to the problem.

## Use when

- A field relies heavily on inherited rules of thumb.
- New technology changes old constraints.
- Competing solutions are discussed mainly through analogy.
- You need to separate physical, economic, and institutional constraints.

Skip a full reconstruction when a standard solution already satisfies verified constraints or when an urgent incident requires immediate action.

## Procedure

1. Define the objective precisely.
2. List claimed constraints and their supporting evidence. Distinguish physical laws, binding rules or agreements, measured limits, and conventions.
3. Separate supported constraints from conventions. For each convention you propose to drop, state how it can be checked and who can change it. Preserve obligations until the responsible person changes them.
4. Identify the relevant units and quantities.
5. Derive the minimum requirements for a viable solution.
6. Generate multiple architectures that satisfy them.
7. Add economic and operational constraints.
8. Compare the architectures under realistic scenarios.
9. Test sensitivity to uncertain assumptions.
10. Reintroduce historical evidence and practical knowledge. Define the cheapest check that could disprove the proposed solution. Stop when the solution and its test are clear, or when only verified constraints remain.

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
- Treating an unsupported constraint as permission to disregard a binding agreement.
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
- reconnect the result to empirical evidence;
- identify a practical check that could disprove the proposed solution.

## Related Patterns

- [Decompose and Abstract](decompose_and_abstract.md)
- [Approximate and Check Easy Cases](approximate_and_check_easy_cases.md)
- [Generate Counterexamples](generate_counterexamples.md)
- [Compare Ecosystems](compare_ecosystems.md)
- [Evaluate Incentives](evaluate_incentives.md)

## Sources

- [First principles in version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-first-principles/SKILL.md) informed the added constraint evidence, skip conditions, and disconfirming check. The local pattern predates this adaptation.
