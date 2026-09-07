---
type: cognitive_pattern
title: Identify Feedback Loops
description: Find reinforcing and balancing loops that explain how a system changes over time.
tags:
  - systems-thinking
  - feedback
  - dynamics
maturity: experimental
sources:
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-systems/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Identify Feedback Loops

## Purpose

Use this pattern to explain recurring system behaviour such as growth, decline, oscillation, lock-in, resistance, or unintended consequences.

## Use when

- Outcomes repeat despite interventions.
- A change produces secondary effects.
- The system appears self-reinforcing or self-correcting.
- Linear cause-and-effect explanations are inadequate.

Skip a full loop analysis when one directly observed cause explains the problem and a local correction is sufficient.

## Core concepts

- **Reinforcing loop:** change amplifies further change.
- **Balancing loop:** change triggers forces that resist or offset it.
- **Delay:** consequences appear later than the action that caused them.
- **Nonlinearity:** effects are not proportional to causes.

## Procedure

1. Define the outcome that changes over time, the system boundary, and the period being examined.
2. List the main variables influencing that outcome. Distinguish quantities that accumulate, such as a queue or inventory, from the rates that increase or decrease them.
3. Draw causal links with direction: increase or decrease.
4. Close the chains into loops.
5. Label each loop reinforcing or balancing. When the link directions stay stable, an even number of opposite-direction links indicates a reinforcing loop and an odd number indicates a balancing loop.
6. Identify delays and check whether a strong corrective response arrives so late that it causes overshoot.
7. Look for loops that dominate at different stages.
8. Test the loop against historical behaviour.
9. Identify where an intervention may trigger a counter-loop.
10. State which loop must change for the outcome to change sustainably and which observation would challenge that explanation. Stop adding loops when more detail no longer changes the explanation or next observation.

## Template

```text
Variable A
  ↓
Variable B
  ↓
Variable C
  ↘
   Variable A
```

For every link ask:

> If the first variable increases, all else equal, what happens to the second?

## Failure modes

- Drawing only one-way causal chains.
- Using vague variables such as "success" or "culture."
- Mixing correlation with causation.
- Ignoring delays.
- Confusing an accumulated quantity with the rate at which it changes.
- Applying the link-count check across conditions where a causal link reverses direction.
- Treating all loops as equally important.
- Failing to test whether the loop explains actual behaviour.

## Example

### Electric-truck charging infrastructure

```text
More charging stations
→ lower operational risk
→ more electric trucks
→ higher station utilization
→ stronger business case
→ more charging stations
```

This is a reinforcing loop.

A balancing loop may be:

```text
More charging demand
→ grid congestion
→ longer connection delays
→ slower station deployment
```

## Evaluation

A useful feedback-loop analysis should:

- contain at least one closed loop;
- distinguish reinforcing from balancing dynamics;
- identify delays;
- state the system boundary and distinguish accumulated quantities from rates;
- explain observed behaviour over time;
- reveal at least one intervention risk or leverage point.

## Related Patterns

- [Analyze Capability Accumulation](analyze_capability_accumulation.md)
- [Find Leverage Points](find_leverage_points.md)
- [Evaluate Incentives](evaluate_incentives.md)

## Sources

- [Systems mapping in version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-systems/SKILL.md) informed the added boundary, stock and flow, and loop checks. The local pattern remains separate from [Find leverage points](find_leverage_points.md) because explaining behaviour and choosing an intervention are different tasks.
