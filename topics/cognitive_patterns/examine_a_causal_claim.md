---
title: "Examine a causal claim"
date: 2026-09-07
type: cognitive_pattern
topics:
  - cognitive_patterns
tags:
  - causal-inference
  - confounding
  - intervention
  - study-design
description: "Define an intervention comparison and inspect the assumptions needed to interpret an observed difference as a causal effect."
maturity: experimental
sources:
  - resource: "https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf"
generated:
  by: "process:codex"
  at: "2026-09-07T13:29:46+00:00"
---

# Examine a causal claim

## TL;DR

Define what would be compared for the same target population under an intervention and an alternative. Then inspect whether the available study supports that comparison. An observed difference can be accurate while its causal interpretation remains unsupported.

## Use when

- Someone claims a policy, product, or practice changed an outcome.
- A before-and-after comparison is being used to predict the effect of adopting a change.
- A decision needs an effect estimate rather than a plausible explanation.

Skip this pattern for a purely descriptive question or an immediate fault already established by direct inspection. Use it as a screening procedure; complex effect estimation needs a suitable study design and domain expertise.

## Procedure

1. State the target population, intervention, alternative, outcome, and follow-up period. Define eligibility and the start of follow-up consistently. Replace vague actions such as "improve management" with a specific change before estimating its effect.
2. Describe the hypothetical comparison that would answer the question. For an intervention study, sketch the trial you would want, including assignment and outcome measurement. A hypothetical trial is a question specification, not evidence that such a trial occurred.
3. Describe how the actual data were obtained. Check who received each option, who was observed, and what changed at the same time.
4. Draw a small causal sketch with time order. Mark the intervention, outcome, and plausible shared causes. Mark assumptions as assumptions. A diagram does not verify its own arrows.
5. Examine the assumptions behind the proposed comparison. For ordinary adjustment of observational data, check that the compared groups could have comparable potential outcomes after accounting for measured differences; that both options are possible within the relevant groups; and that observed actions correspond to the intervention being defined. These are exchangeability, positivity, and consistency. Other designs need their own assumptions.
6. Check selection, measurement error, and spillovers between units. Do not adjust for every available variable. A consequence of treatment can be part of the effect, while conditioning on a shared consequence of two causes can create a misleading association.
7. Identify which design or additional observation could address the main weakness. If no defensible comparison exists, report the observed association and withhold the causal magnitude. Lack of identification is not evidence of no effect.
8. State the supported claim and scope. Report statistical uncertainty separately from uncertainty about the design and assumptions.

Stop when the causal question and its main identification gap are clear, or when a supported design permits the required estimate. Avoid refining a numerical estimate whose interpretation is not justified.

## Output

```text
Population and eligibility:
Intervention and alternative:
Outcome and follow-up:
Comparison needed:
Actual assignment and observation:
Shared causes and selection concerns:
Assumptions and their support:
Main gap and next check:
Supported association or causal claim:
Scope and remaining uncertainty:
```

## Example and transfer

In a hypothetical factory, defect rates fall after new inspection software is introduced, while a supplier also improves its materials. Define whether the intended effect concerns software assignment or actual use, then seek a comparison that separates the changes. The same procedure applies to a tutoring program whose volunteers were already more motivated than nonparticipants.

## Failure modes

- Treating sequence in time as sufficient evidence of causation.
- Treating random assignment as a cure for later missing outcomes or nonadherence.
- Assuming a larger dataset fixes a systematically unsuitable comparison.
- Controlling for every measured variable without considering its causal role.
- Inferring no effect because the available evidence cannot identify one.
- Reporting a narrow confidence interval as if it captured all uncertainty.

## Evaluation

A useful review specifies the comparison, identifies the assumption most likely to change its interpretation, and proposes a relevant next check. It distinguishes an observed difference from a defensible effect estimate without automatically rejecting all observational evidence.

## Related patterns

- [Check evidence quality](check_evidence_quality.md) inspects the observations and their provenance.
- [Test competing hypotheses](test_competing_hypotheses.md) separates possible explanations of an event.
- [Find leverage points](find_leverage_points.md) proposes interventions whose effects may then need investigation.

## Sources

The [What If source note](2026-08-19_book_hernan-robins_causal-inference-what-if.md) identifies the reviewed chapters. This pattern is a local screening procedure inspired by the book, not an implementation of its statistical methods.
