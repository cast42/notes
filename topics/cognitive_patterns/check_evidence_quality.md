---
title: "Check evidence quality"
date: 2026-09-07
type: cognitive_pattern
topics:
  - cognitive_patterns
tags:
  - source-reliability
  - provenance
  - measurement
  - evidence
description: "Check what a consequential claim's evidence can support before using it to explain, predict, or decide."
maturity: experimental
sources:
  - resource: "https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf"
generated:
  by: "process:codex"
  at: "2026-09-07T13:29:46+00:00"
---

# Check evidence quality

## TL;DR

Trace the evidence behind a consequential claim and check whether its collection and interpretation support the intended use. Several reports can repeat one observation. Record the claim you can support, the uncertainty, and the next useful check.

## Use when

- A recommendation depends on a report, measurement, or quotation whose basis is unclear.
- Sources appear to agree but may share an origin.
- A result is being transferred to another population or period.

Skip a full review for a routine fact with a current, directly inspectable source. Limit the review to evidence that could change the decision.

## Procedure

1. Write the exact claim, intended use, and required precision. Separate what was observed from what someone inferred.
2. Locate the underlying observation, dataset, or original statement. Record its date and version. Mark an unavailable original as unavailable rather than treating a summary as a direct observation.
3. Check who collected the information, their access, and relevant incentives. Reputation alone neither establishes nor refutes the claim.
4. Inspect the collection method. Check the population, comparison, missing observations, units, and measurement conditions that affect this use.
5. Trace dependencies between reports. Count shared observations once when assessing corroboration, even if several authors interpret them differently.
6. Check that the cited passage supports the claim and retains its qualifications. Look for corrections, withdrawals, and changes since collection.
7. Identify the assumption connecting the observation to the intended decision. State how a plausible failure of that assumption would change the conclusion.
8. Classify the claim as supported within a stated scope, usable with a named limitation, or unsupported for this use. Name one check that could change the classification.

Stop when the important claim has a defensible scope or when unavailable evidence prevents further progress. State the limitation instead of accumulating more summaries. Reopen the review when the source changes or the intended use expands.

## Output

| Claim and use | Original evidence and date | Collection limits | Shared origins | Supported scope | Next check |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Do not compress different weaknesses into a precise numerical reliability score without a validated scoring method.

## Example and transfer

In a hypothetical procurement review, a supplier cites a laboratory throughput test to support an annual production commitment. Check whether the test included maintenance downtime and the proposed material mix before using its rate in a capacity estimate. The same procedure applies to an education claim based on a selected class that excluded absent pupils.

## Failure modes

- Treating repeated reporting as independent corroboration.
- Rejecting all evidence from an interested source instead of examining its method.
- Treating an unavailable source as proof that its claim is false.
- Preserving a statistic while dropping its population or comparison.
- Assuming a trustworthy measurement establishes causation.
- Reviewing every minor citation after the decision is already supported.

## Evaluation

The review should identify the underlying evidence, preserve its scope, and explain any dependency between sources. It should narrow an unsupported claim or justify using it without inventing missing facts. The next check must address a limitation that could change the decision.

## Related patterns

- [Test competing hypotheses](test_competing_hypotheses.md) compares explanations after checking the observations.
- [Examine a causal claim](examine_a_causal_claim.md) checks whether a comparison supports an intervention effect.
- [Verify with independent estimates](verify_with_independent_estimates.md) checks a conclusion through different routes.

## Sources

The [CIA primer source note](2009-03_source_cia_tradecraft-primer.md) identifies the relevant sections. The primer informs the source and assumption checks. The stopping rule, output categories, and transfer examples are local adaptations and have not been shown to improve model accuracy.
