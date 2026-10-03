---
type: cognitive_pattern
title: Find leverage points
description: Identify interventions that change system behaviour with disproportionate effect.
tags:
  - systems-thinking
  - intervention
  - policy
  - design
maturity: experimental
topics:
  - cognitive_patterns
resource: "https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/"
sources:
  - resource: "https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/"
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-opportunity-cost/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-10-03T17:51:28+00:00"
---

# Find leverage points

## TL;DR

Use this pattern to select interventions that alter the structure or behaviour of a system rather than merely treating symptoms.

## Use when

- Many interventions are possible.
- Current measures produce weak or temporary effects.
- A system resists change.
- Resources are limited and prioritization matters.

## Intervention levels

The following is a local grouping of intervention types. It is not a numbered reproduction of Meadows' twelve-item list:

1. Parameters and subsidies
2. Buffer sizes and inventories
3. Physical stocks and flows
4. Delays
5. Corrective and reinforcing feedback
6. Information flows
7. Rules and incentives
8. Ability to self-organize
9. Goals
10. Mental models and the ability to reconsider them

Meadows presents a hierarchy while warning that it is not a recipe for locating effective interventions. A goal or rule change can fail if people lack the power or capacity to implement it. A parameter change can be decisive near a threshold. Compare the mechanism, feasibility, and risk in the actual system instead of selecting an intervention by rank.

## Procedure

1. Define the undesirable system behaviour.
2. Identify the dominant feedback loops.
3. List current interventions and their level.
4. Find bottlenecks, delays, missing information, and rigid rules.
5. Ask whether the system can experiment and self-organize.
6. Identify who controls goals and incentives.
7. Generate candidate interventions at several levels.
8. Estimate impact, feasibility, reversibility, and risk.
   When choices use scarce resources, also name the best feasible alternative those resources would otherwise support. Compare the options over the same horizon and keep the alternative's foregone benefit distinct from the chosen intervention's direct cost. Skip this check only when compliance leaves no feasible alternative or the resource has no real alternative use.
9. Prefer portfolios when one intervention cannot unlock the system alone.
10. Define measurements that reveal whether the intervention changed the loop.

For each candidate, state an observation that would weaken the proposed mechanism and a condition for revising or stopping the intervention. If the feedback model is too uncertain to choose, investigate the uncertain link first. Use [Examine a causal claim](examine_a_causal_claim.md) before treating an observed change as an intervention effect. Use [Test a plan across plausible futures](test_a_plan_across_plausible_futures.md) when external conditions could reverse the choice.

Stop when the comparison supports a feasible action or identifies the specific missing evidence. Adding more intervention levels is not useful unless it changes the available choices.

## Decision table

| Candidate | Expected impact | Feasibility | Risk and reversibility | Best forgone use | Learning value |
|---|---:|---:|---:|---|---:|
| Intervention A | High | Medium | Low risk, high reversibility | Intervention B | High |
| Intervention B | Medium | High | Medium risk, medium reversibility | Intervention A | Medium |

## Failure modes

- Assuming the deepest intervention is automatically best.
- Ignoring political power and implementation capacity.
- Choosing an intervention without mapping feedback loops.
- Focusing only on price signals.
- Treating leverage points as isolated rather than interacting.
- Failing to create a feedback mechanism for policy learning.
- Comparing an intervention only with doing nothing when another feasible intervention would use the same scarce resources.

## Example

For electric freight transport:

- Purchase subsidy: parameter change.
- Faster grid-connection information: information-flow change.
- Standardized charging interfaces: rule change.
- Shared industrial charging hubs: structural change.
- Competitive experimentation among charging models: self-organization.

## Evaluation

A strong leverage-point analysis should:

- compare interventions at multiple system levels;
- explain which loop each intervention changes;
- include implementation constraints;
- identify second-order effects;
- define how to learn from the intervention.
- when scarce resources constrain the choice, identify the best feasible forgone use or explain why none exists.

## Related patterns

- [Identify Feedback Loops](identify_feedback_loops.md)
- [Evaluate Incentives](evaluate_incentives.md)
- [Analyze Capability Accumulation](analyze_capability_accumulation.md)

## Sources

- [Donella Meadows, Leverage Points: Places to Intervene in a System](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/), especially the introduction, revised list, and discussion of parameters. The local procedure and examples are adaptations, not evidence that a particular intervention will work.
- [Thinking in Systems](../system_thinking/2008-12-05_book_donella-meadows_thinking-in-systems.md) provides the wider systems context already used in this repository.
- [Opportunity cost in Claude Code Thinking Skills, version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-opportunity-cost/SKILL.md) motivates the optional comparison with the best feasible use of scarce resources. This local adaptation does not adopt its numerical value-delta formula or its permanent-loss decision rule.
