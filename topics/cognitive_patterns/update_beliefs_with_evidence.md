---
type: cognitive_pattern
title: Update beliefs with evidence
date: 2026-07-20
timestamp: 2026-07-20
description: Revise confidence by starting with a prior belief and asking how expected new evidence is under competing explanations.
topics:
  - cognitive_patterns
tags:
  - bayesian-reasoning
  - uncertainty
  - base-rates
  - evidence
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
status: experimental
---

# Update beliefs with evidence

## TL;DR

State what you believed before seeing new evidence. Compare how likely the evidence is under competing explanations, then revise your confidence. Do not invent precise numbers when the evidence cannot support them.

## Use when

- New evidence may cause an overreaction.
- Base rates are available.
- Several explanations remain plausible.
- A decision depends on how likely an uncertain claim is.
- You want to track whether past confidence estimates were calibrated.

Skip the update when direct observation can answer the question, when no defensible prior exists, or when the decision stays the same across all plausible probabilities.

## Procedure

1. State the claim or hypothesis.
2. List the main alternatives.
3. Record the prior confidence before examining the new evidence.
4. Explain the source of the prior, such as a base rate or comparable cases.
5. Ask how likely the evidence would be if each explanation were true.
6. Check whether the evidence is independent of evidence already counted.
7. Update confidence in proportion to how well the evidence separates the explanations.
8. Record the new confidence as a range when a point estimate would imply false precision.
9. State what future evidence would cause another meaningful update.
10. Check whether the revised confidence changes the decision.

When the inputs support calculation, use Bayesian odds:

```text
posterior odds = prior odds × likelihood ratio
```

Use a qualitative update when the inputs are weak. State the direction and size of the update, e.g., small decrease or large increase, and explain why.

## Output template

```text
Hypothesis:
Alternatives:
Prior confidence:
Basis for the prior:
New evidence:
Expected under the hypothesis:
Expected under alternatives:
Evidence already counted:
Updated confidence:
Decision effect:
Next useful evidence:
```

## Failure modes

- Ignoring the base rate.
- Starting with the new evidence and inventing a prior afterward.
- Treating repeated reports from one source as independent evidence.
- Using precise probabilities without defensible inputs.
- Updating only toward a preferred explanation.
- Revising confidence without changing any action or prediction.

## Evaluation

A good belief update should:

- make the prior and its source explicit;
- compare the evidence under at least two explanations;
- avoid counting the same evidence twice;
- match the size of the update to the strength of the evidence;
- state how the update affects the decision or next observation.

Track dated forecasts when possible. If events assigned about 70 percent confidence occur far more or less than 70 percent of the time, revise the estimation process.

## Related patterns

- [Test competing hypotheses](test_competing_hypotheses.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Select cognitive patterns](select_cognitive_patterns.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its Bayesian reasoning skill.
