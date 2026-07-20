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
status: experimental
---

# Run a pre-mortem

## TL;DR

Imagine that the plan has already failed. Explain the failure in concrete terms, rank the causes, and change the plan to prevent or detect the most serious causes.

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
8. Add a prevention step, warning sign, owner, and checkpoint for each one.
9. Change the plan, budget, sequence, or scope based on the findings.
10. Record any accepted risk that remains.

## Output template

```text
Plan:
Future date:
Observed failure:

Failure cause:
Likelihood:
Impact:
Early warning sign:
Prevention or response:
Owner:
Checkpoint:

Changes to the plan:
Accepted risks:
```

## Failure modes

- Listing generic risks that apply to every project.
- Ranking risks while generating them and stopping at the first plausible cause.
- Focusing only on technical failure.
- Adding mitigations with no owner or checkpoint.
- Recording risks without changing the plan.
- Treating the exercise as evidence that failure will occur.

## Evaluation

A good pre-mortem should:

- describe failure in observable terms;
- uncover risks that were missing from the plan;
- identify assumptions that carry much of the risk;
- add concrete warning signs and checkpoints;
- cause at least one useful change to the plan or record why no change is needed.

## Related patterns

- [Generate counterexamples](generate_counterexamples.md)
- [Evaluate incentives](evaluate_incentives.md)
- [Combine cognitive patterns](combine_cognitive_patterns.md)

## Sources

- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
- [Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills), especially its pre-mortem skill.
