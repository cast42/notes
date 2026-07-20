---
type: cognitive_pattern
title: Test competing hypotheses
date: 2026-07-20
timestamp: 2026-07-20
description: Compare plausible explanations by stating falsifiers and checking the observation that best separates them.
topics:
  - cognitive_patterns
tags:
  - hypothesis-testing
  - falsification
  - diagnosis
  - evidence
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
status: experimental
---

# Test competing hypotheses

## TL;DR

List several specific explanations before investigating deeply. For each explanation, state what would count against it. Check the cheapest observation that best separates the leading explanations, then update or discard them.

## Use when

- A symptom or event has several plausible causes.
- You can inspect records, code, logs, measurements, or other evidence.
- The cost of testing differs across explanations.
- You need to locate a cause before choosing a response.

Skip the pattern when direct evidence already identifies the cause, only one plausible explanation exists, or no observation is possible yet.

## Procedure

1. Describe the observation that needs explanation.
2. List three to five specific hypotheses.
3. Record why each hypothesis is plausible.
4. State what observation would weaken or rule out each hypothesis.
5. Identify the cheapest observation that separates the leading hypotheses.
6. Rank observations by expected information and cost.
7. Make one observation at a time.
8. Update, narrow, or discard hypotheses after each observation.
9. Stop when direct evidence supports one explanation and important alternatives have been ruled out.
10. State the remaining uncertainty and the next check if uncertainty is still decision relevant.

## Output template

| Hypothesis | Why plausible | Best separating observation | Weakened or ruled out if |
| --- | --- | --- | --- |
| H1 | | | |
| H2 | | | |
| H3 | | | |

```text
Observation order:
Evidence found:
Hypotheses discarded:
Leading explanation:
Remaining uncertainty:
Next check:
```

## Failure modes

- Writing vague hypotheses that cannot be tested.
- Searching only for support for the first explanation.
- Starting with an expensive test when a simple observation can separate the options.
- Treating absence of evidence as proof of absence.
- Stopping at a plausible story without checking alternatives.
- Continuing the investigation after the evidence is sufficient for the decision.

## Evaluation

A good hypothesis test should:

- compare several plausible explanations;
- define evidence against each explanation before inspection;
- choose observations for their ability to separate explanations;
- change the hypothesis set as evidence arrives;
- end with a supported explanation or a clear statement of what remains unknown.

## Related patterns

- [Update beliefs with evidence](update_beliefs_with_evidence.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Reason from first principles](reason_from_first_principles.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its hypothesis differential version of the scientific method skill.
