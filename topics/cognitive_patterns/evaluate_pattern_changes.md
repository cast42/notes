---
title: "Evaluate changes to cognitive patterns"
date: 2026-09-07
type: procedure
topics:
  - cognitive_patterns
tags:
  - evaluation
  - experimental-design
  - comparison
  - reproducibility
description: "Separate editorial checks from outcome comparisons when deciding whether a pattern revision helps."
sources:
  - resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm"
  - resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm"
  - resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm"
generated:
  by: "process:codex"
  at: "2026-09-07T13:29:46+00:00"
---

# Evaluate changes to cognitive patterns

## TL;DR

An editorial review can find unclear instructions and missing checks. An outcome comparison is needed to learn whether users obtain better answers or decisions. Label which kind of review was actually performed.

## Key takeaways

- Define cases and criteria before revising a procedure.
- Compare the current pattern, the revision, and direct reasoning under comparable conditions.
- Preserve unsuccessful cases, extra work, and unrun tests in the record.

## Editorial review

1. Pin the baseline revision and state the problem a change should address.
2. Select representative cases and a case where no pattern is useful. Write the relevant facts and acceptable outcomes before editing.
3. Inspect current guidance, apply the proposed revision, and record any different action or missing check. Name any prior exposure that prevents an independent comparison.
4. Test the revision on a fresh case outside its worked examples. If the author chooses and reviews that case, call it an author transfer check rather than an independent validation.
5. Record remaining ambiguities and whether they require an edit. A clearer procedure is an editorial finding, not a measured accuracy gain.

## Outcome comparison

Use this stage when a claim about effectiveness is needed. It is a study to run, not a condition automatically satisfied by editing Markdown.

1. Specify the outcome and a practically useful difference in advance. Include factual correctness and verification burden. Record interruption cost separately from whether suggestions were accepted.
2. Preserve the exact prompts, pattern revisions, source packets, and scoring criteria. Use the same model version, effort setting, tools, and task budget across conditions.
3. Compare direct reasoning, baseline guidance, and revised guidance in separate sessions. Prevent answers from one condition entering another condition's context. Keep distinct tasks for development and evaluation.
4. Randomize condition order where possible. Group comparisons by relevant task characteristics so that a change in task difficulty is not mistaken for a treatment effect. Record any deviations.
5. Plan enough repeated trials to assess variability. When people participate, account for learning and order effects; do not present repeated exposures as independent experience.
6. Use an answer key or a reviewer unaware of the condition when feasible. Preserve raw outputs and failures. Human verification time and usefulness judgments require actual human observations.
7. Report the comparison and its uncertainty. Check practical benefit separately from statistical significance, and repeat a promising result on different cases before generalizing.

Separate sessions reduce answer contamination. They do not make models independent sources of factual evidence. A comparison of whole collections estimates the effect of that package; it does not identify which individual edit caused a difference.

## Record

```text
Question and intended benefit:
Baseline and revised commits:
Cases, evidence packets, and selection date:
Editorial check or outcome study:
Model, effort, tools, and budgets:
Conditions, order, and repetitions:
Scoring rule and practical threshold:
Raw outputs or worked case record:
Observed changes, failures, and additional effort:
Prior exposure and other limitations:
Tests not run:
Retain, revise, or remove:
```

## Related concepts

- [September source review and worked checks](2026-09-07_investigation_public-source-pattern-update.md)
- [Test competing hypotheses](test_competing_hypotheses.md)
- [Cognitive pattern index](index.md)

## Sources

NIST/SEMATECH's engineering statistics handbook informs the distinction between selecting a design, randomizing runs, and grouping runs by known sources of variation. The application to model prompts and human verification is a local adaptation.

- [Choosing an experimental design, section 5.3](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm)
- [Completely randomized designs, section 5.3.3.1](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm)
- [Randomized block designs, section 5.3.3.2](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)
