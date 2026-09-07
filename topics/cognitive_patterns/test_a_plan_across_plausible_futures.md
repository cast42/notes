---
title: "Test a plan across plausible futures"
date: 2026-09-07
type: cognitive_pattern
topics:
  - cognitive_patterns
tags:
  - scenario-planning
  - uncertainty
  - policy-testing
  - contingency-planning
description: "Compare the same options across plausible external conditions and identify adaptations and review triggers."
maturity: experimental
sources:
  - resource: "https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts/the-futures-toolkit-html"
generated:
  by: "process:codex"
  at: "2026-09-07T13:29:46+00:00"
---

# Test a plan across plausible futures

## TL;DR

Compare a plan and its alternatives across the same plausible external conditions. Identify what remains useful, what depends on a condition, and what should change if that condition appears. Scenarios do not establish probabilities.

## Use when

- A commitment lasts longer than confidence in one forecast.
- External changes could reverse the preferred option.
- A staged or reversible choice may be useful.

Skip scenario construction for a routine, reversible action or a question with an adequate direct forecast. A brief comparison can use existing scenarios if their scope fits.

## Procedure

1. Define the decision, planning horizon, and alternatives, including postponement when feasible. Record the decision owner's success criteria and minimum acceptable conditions before comparing options.
2. Separate actions the decision maker controls from external uncertainties. Identify the few uncertainties that could reverse a choice.
3. Use source evidence to describe plausible ranges and dependencies. If two uncertainties are sufficiently distinct, a two by two matrix is one useful starting point. Do not force dependent uncertainties into impossible combinations.
4. Describe a small set of coherent futures that challenge different assumptions. Include an adverse condition that could defeat the preferred plan. State what the set leaves out.
5. Evaluate every option against every future using the same criteria. For each judgment, explain the mechanism and record missing information. A label such as "works" needs conditions and evidence.
6. Separate actions suitable across the tested futures from actions that depend on a condition. Compare feasible modifications, costs of delay, and reversibility. Do not average scenarios using invented probabilities.
7. For a contingent action, name an observable sign, a review owner, and enough lead time to act. A sign starts a reassessment; it does not prove that an entire scenario is happening.
8. Report the preferred action or unresolved tradeoff, the conditions under which it changes, and the most useful next observation.

Stop when the tested futures distinguish the options or identify the information needed to choose. More scenarios are useful only when they expose a materially different vulnerability. Do not claim coverage of every possible future.

## Output

| Option | Future A | Future B | Future C | Future D | Adaptation and review trigger |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Record the success criteria, scenario assumptions, omitted conditions, and unresolved tradeoffs alongside the table.

## Example and transfer

A hypothetical training provider compares permanent classrooms with rented space. Enrollment and remote attendance may change independently. Compare each option under the same enrollment and attendance conditions, including the possibility that both reduce room use. The procedure also applies to a data service choosing owned hardware or rented computing capacity when demand and delivery dates are uncertain.

## Failure modes

- Treating a scenario as a forecast or giving each scenario equal probability by default.
- Choosing futures that make the preferred option win.
- Mixing a controllable response with an external condition.
- Using inconsistent success criteria across options.
- Recommending flexibility without checking its price or lead time.
- Defining a warning sign that appears too late to permit action.

## Evaluation

A useful comparison exposes a condition that changes an option's performance, or explains why the choice survives the tested variation. It produces an actionable contingency and preserves unresolved tradeoffs. Any numerical ranking must be supported by stated inputs.

## Related patterns

- [Run a pre-mortem](run_a_pre_mortem.md) investigates failure paths for a particular plan.
- [Find leverage points](find_leverage_points.md) selects the system changes to consider.
- [Approximate and check easy cases](approximate_and_check_easy_cases.md) tests numerical models used inside scenarios.

## Sources

The [Futures Toolkit source note](2024-08-29_source_go-science_futures-toolkit.md) covers scenario construction and policy stress-testing. The shorter procedure and examples here are local adaptations, not a substitute for a facilitated foresight exercise or evidence of improved AI decisions.
