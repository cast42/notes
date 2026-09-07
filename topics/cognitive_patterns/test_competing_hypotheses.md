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
maturity: experimental
sources:
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-scientific-method/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Test competing hypotheses

## TL;DR

List the serious competing explanations before investigating deeply. For each explanation, state what would count against it. Check the cheapest observation that best separates the leading explanations. Among explanations that still fit the evidence, prefer the one with fewer unsupported assumptions as a working explanation.

## Use when

- A symptom or event has several plausible causes.
- You can inspect records, code, logs, measurements, or other evidence.
- The cost of testing differs across explanations.
- You need to locate a cause before choosing a response.

Skip the pattern when direct evidence already identifies the cause, only one plausible explanation exists, or no observation is possible yet.

If only one serious explanation remains, test it directly. Do not invent alternatives to fill a table. If an observation comes from a document or dashboard that may be stale, check the underlying records or current behaviour first.

## Procedure

1. Describe the observation, scope, and timing without treating an interpretation as an observed fact.
2. List two to five specific hypotheses when serious alternatives exist.
3. Record why each hypothesis is plausible.
4. State what observation would weaken or rule out each hypothesis.
5. Identify the cheapest observation that separates the leading hypotheses.
6. Rank observations by expected information and cost.
7. Make one observation at a time.
8. Update, narrow, or discard hypotheses after each observation. Among survivors that fit the evidence, prefer the explanation with fewer independent unsupported assumptions. Never keep a simpler explanation that contradicts the evidence.
9. Stop when direct evidence supports one explanation and important alternatives have been ruled out.
10. State the supported cause or location, remaining uncertainty, and the next useful action. Further study of systemic causes is a separate question once the immediate cause is known.

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
Unsupported assumptions in surviving explanations:
Evidence supporting the cause or location:
Remaining uncertainty:
Next check:
Next action:
```

## Failure modes

- Writing vague hypotheses that cannot be tested.
- Searching only for support for the first explanation.
- Inventing weak alternatives to reach a fixed number of hypotheses.
- Choosing the simplest story before checking whether it fits the observations.
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
- use simplicity only to rank explanations that still fit the evidence;
- end with a supported explanation or a clear statement of what remains unknown.

## Related patterns

- [Update beliefs with evidence](update_beliefs_with_evidence.md)
- [Generate counterexamples](generate_counterexamples.md)
- [Reason from first principles](reason_from_first_principles.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Scientific method in version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-scientific-method/SKILL.md), including the former Occam's razor skill. The local pattern remains usable for observable causes outside software diagnosis.
