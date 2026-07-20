---
title: "Claude Code Thinking Skills and this notes repo"
date: 2026-07-20
timestamp: 2026-07-20
type: source
topics:
  - cognitive_patterns
tags:
  - mental-models
  - reasoning-procedures
  - skill-design
  - evaluation
resource: "https://github.com/tjboudreaux/cc-thinking-skills"
author: "TJ Boudreaux"
source_revision: "0313ee0d476bf9db2c38ad8bd11d9933a61350d4"
description: "A collection of reasoning skills that informed new cognitive patterns, clearer pattern selection, and stronger evaluation rules in this notes repo."
---

# Claude Code Thinking Skills and this notes repo

## TL;DR

[Claude Code Thinking Skills](https://github.com/tjboudreaux/cc-thinking-skills) is a collection of 39 reasoning frameworks packaged as skills for Claude Code. The review led to five new cognitive patterns in this notes repo and a clearer way to select, combine, and evaluate patterns.

The source also reports that none of its skills has shown a reliable and repeated accuracy gain. The notes repo therefore treats cognitive patterns as reasoning guidance rather than proof that an answer is correct.

## What the source contains

The repository turns established reasoning frameworks into instructions that an agent can apply. Its collection covers decisions, uncertainty, systems, risk, diagnosis, strategy, and product work.

Most skills follow a common structure:

- They state the pattern's purpose.
- They explain when to use and skip the pattern.
- They give a step by step procedure.
- They provide examples and an output template.
- They list common mistakes.
- They end with a checklist and key questions.

The repository also includes skills for choosing and combining patterns. A model router maps the type of problem to suitable procedures. A separate combination skill explains how to use procedures in sequence, in parallel, or in opposition.

## What changed in this notes repo

The review exposed gaps in the original cognitive pattern set. The original set was strongest on systems, incentives, and capability. It offered less guidance for choosing a pattern, handling uncertainty, reviewing plans before execution, and testing several explanations.

Five patterns were added:

- [Select cognitive patterns](select_cognitive_patterns.md) chooses the smallest useful set for a question.
- [Combine cognitive patterns](combine_cognitive_patterns.md) gives each selected pattern a distinct role and resolves disagreements between their outputs.
- [Update beliefs with evidence](update_beliefs_with_evidence.md) starts with a prior belief, compares explanations, and updates confidence without false precision.
- [Run a pre-mortem](run_a_pre_mortem.md) assumes that a plan has failed and turns likely causes into changes, owners, and checkpoints.
- [Test competing hypotheses](test_competing_hypotheses.md) states several falsifiable explanations and checks the observation that best separates them.

The [cognitive pattern index](index.md) was also reorganized by reasoning need. It now tells agents to choose the smallest useful set, state what each pattern should add, and combine patterns only when each one covers a distinct gap.

## What was adapted

The notes repo adopted the source's practical structure rather than copying its skills as a package. The new patterns use the local cognitive pattern contract, which focuses on a reusable procedure, failure modes, evaluation criteria, and links to related knowledge.

The review led to six design choices:

- Route from the problem to the procedure.
- State when a pattern should be skipped.
- Give every combined pattern a separate job.
- Use output templates so a reader can inspect the reasoning.
- End with checks that show whether the procedure was followed.
- Test whether a pattern improves results before claiming that it does.

## What was not adopted

The notes repo did not import all 39 skills. Many overlap with existing patterns, address narrow coding tasks, or need evidence from repeated use before they belong in the durable knowledge set.

Claude Code installation steps and invocation rules were also left out. The notes repo stores portable reasoning procedures, not instructions tied to one agent product.

The source's evaluation claims were treated with care. Its published summary says that no skill currently has a reliable and repeated accuracy improvement. One revised scientific method skill showed promising results, but its main test did not pass the stated significance threshold. The source therefore supports experimentation and evaluation, not a general claim that adding a named framework makes an agent more accurate.

## How to use the source in future updates

Use the external collection as a source of candidates, structure, and test ideas. Do not add a pattern because it appears in the collection.

Before adding another pattern:

1. Name the reasoning gap in the current set.
2. Check whether an existing pattern can cover the gap with a small change.
3. Adapt only the procedure that remains useful outside Claude Code.
4. Add local links, failure modes, and evaluation criteria.
5. Apply the pattern to a real investigation.
6. Revise or remove it when repeated use does not improve the work.

## Related concepts

- [Generate counterexamples](generate_counterexamples.md)
- [Reason from first principles](reason_from_first_principles.md)
- [Repository design](../../DESIGN.md)

## Sources

- [tjboudreaux/cc-thinking-skills at the inspected revision](https://github.com/tjboudreaux/cc-thinking-skills/tree/0313ee0d476bf9db2c38ad8bd11d9933a61350d4).
- [Elevate or Kill scorecard](https://github.com/tjboudreaux/cc-thinking-skills/blob/0313ee0d476bf9db2c38ad8bd11d9933a61350d4/analysis/ELEVATE-OR-KILL-SCORECARD.md), the repository's evaluation summary.
