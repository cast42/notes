---
type: cognitive_pattern
title: Run a pre-mortem
date: 2026-07-20
timestamp: 2026-07-20
description: Assume that a plan has failed, explain the specific causes, and change the plan before committing to it.
topics:
  - cognitive_patterns
tags:
  - pre-mortem
  - risk-analysis
  - planning
  - failure-modes
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
maturity: experimental
sources:
  - resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-pre-mortem/SKILL.md"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Run a pre-mortem

## TL;DR

Imagine that the plan has already failed. Explain the failure in concrete terms and rank the causes. For each serious cause, identify the conditions that allowed failure and turn them into verifiable prevention requirements before changing the plan.

## Use when

- A project, launch, migration, or major decision is about to begin.
- The team appears confident and has discussed few risks.
- Failure would be costly or hard to reverse.
- The plan depends on several assumptions or external parties.

Skip the pattern for small reversible work, during an active incident, or when it would only repeat risks already controlled by tests and rollback systems.

## Procedure

1. State a future date and assume the plan has failed by then.
2. Describe the failure in observable terms.
3. Generate specific causes before judging them.
4. Include technical, operational, human, and external causes when relevant.
5. Ask which assumption the plan most needs to be true.
6. Rank causes by likelihood, impact, and how early they can be detected.
7. Choose the most serious causes that the team can influence.
8. For each serious cause, identify the necessary or enabling conditions and turn them into requirements that prevent or detect failure. State what observation would show that each requirement is met.
9. Bind each requirement to an owner, warning sign, verification checkpoint, and condition for proceeding, pausing, or rolling back. Change the plan, budget, sequence, or scope accordingly.
10. Record accepted risks and who accepts them. Stop when each serious risk has a planned control with an owner and a check, or an explicit acceptance by the responsible owner. Also stop when further reasons only repeat generic risks.

## Output template

```text
Plan:
Future date:
Observed failure:

Failure cause:
Likelihood:
Impact:
Necessary or enabling conditions:
Prevention requirement and verification:
Early warning sign:
Prevention or response:
Owner:
Checkpoint:
Condition for proceeding, pausing, or rolling back:

Changes to the plan:
Accepted risks:
Decision owner for accepted risks:
```

## Failure modes

- Listing generic risks that apply to every project.
- Ranking risks while generating them and stopping at the first plausible cause.
- Focusing only on technical failure.
- Adding mitigations with no owner or checkpoint.
- Naming a warning sign without deciding what to do when it appears.
- Recording risks without changing the plan.
- Treating the exercise as evidence that failure will occur.

## Evaluation

A good pre-mortem should:

- describe failure in observable terms;
- uncover risks that were missing from the plan;
- identify assumptions that carry much of the risk;
- add concrete warning signs and checkpoints;
- connect failure conditions to verifiable prevention requirements and decisions about proceeding;
- cause at least one useful change to the plan or record why no change is needed.

## Related patterns

- [Generate counterexamples](generate_counterexamples.md)
- [Evaluate incentives](evaluate_incentives.md)
- [Combine cognitive patterns](combine_cognitive_patterns.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Pre-mortem in version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills/thinking-pre-mortem/SKILL.md), including the failure reversal procedure from the former inversion skill.
