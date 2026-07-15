---
type: cognitive_pattern
title: Evaluate Incentives
description: Analyze how rules, rewards, penalties, and constraints shape actor behaviour and system outcomes.
tags:
  - incentives
  - economics
  - governance
  - policy
status: experimental
---

# Evaluate Incentives

## Purpose

Use this pattern to determine whether an intervention changes behaviour in the intended direction and whether it creates gaming, leakage, dependency, or unintended effects.

## Use when

- Designing subsidies, taxes, procurement, targets, or regulation.
- Actors appear to optimize a metric rather than the real objective.
- A policy creates compliance without capability.
- Incentives affect multiple actors differently.

## Core questions

1. Who receives the reward or bears the cost?
2. What behaviour becomes locally rational?
3. What can be gamed?
4. What externalities remain?
5. Does the incentive build capability or only change short-term behaviour?
6. What happens when the incentive ends?
7. How does the incentive interact with infrastructure and constraints?
8. Who has better information than the policy designer?

## Procedure

1. Define the desired system outcome.
2. Identify all affected actors.
3. Map each actor's objective, constraints, and information.
4. Describe the behaviour encouraged by the intervention.
5. Generate plausible gaming strategies.
6. Identify externalities and distributional effects.
7. Test whether infrastructure allows the desired response.
8. Compare temporary and persistent effects.
9. Add feedback, auditing, and adaptation mechanisms.
10. Evaluate alternative incentive designs.

## Example

A purchase subsidy for electric trucks may lower upfront cost, but if charging access is unreliable, fleet operators still avoid adoption. The policy changes price but not feasibility.

A better package may combine:

- temporary purchase support;
- guaranteed grid access;
- charging availability standards;
- utilization-based infrastructure support.

## Failure modes

- Assuming actors follow policy intent.
- Ignoring constraints that prevent response.
- Ignoring timing and cash-flow effects.
- Rewarding outputs without learning or capability.
- Creating cliff effects when support ends.
- Measuring activity rather than outcomes.

## Evaluation

A strong incentive analysis should:

- predict actor responses;
- identify gaming opportunities;
- include infrastructure constraints;
- distinguish short-term behaviour from capability-building;
- propose adaptive monitoring.

## Related Patterns

- [Identify Feedback Loops](identify_feedback_loops.md)
- [Find Leverage Points](find_leverage_points.md)
- [Generate Counterexamples](generate_counterexamples.md)
