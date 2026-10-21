---
title: "How to write and test agent skills with evals"
date: 2026-10-19
type: article
topics:
  - agentic_coding
tags:
  - agent-skills
  - evaluation
  - ablation
  - prompt-engineering
  - reliability
resource: "https://x.com/i/article/2112186374052802560"
description: "Sergii Makarevych proposes treating agent skills as testable behavioral hypotheses, separating whether agents follow the instructions from whether following them improves task outcomes."
author: "Sergii Makarevych"
handle: "sermakarevich"
generated:
  by: "process:codex"
  at: "2026-10-19T22:37:00+02:00"
sources:
  - id: "announcement-post"
    resource: "https://x.com/sermakarevich/status/2112198653469241856"
  - id: "article"
    resource: "https://x.com/i/article/2112186374052802560"
  - id: "agent-skills-specification"
    resource: "https://agentskills.io/specification"
---

# How to write and test agent skills with evals

## TL;DR

- Treat a skill as text intended to change agent behavior—not as a model upgrade. A published file is only a hypothesis about what the agent will do and whether that behavior will help.
- Start with one measurable objective. Break the skill into a short list of actionable points, each with a reasoned hypothesis for why it should improve the objective.
- Evaluate two separate questions: **adherence** (did the agent follow each point?) and **effect** (did following it improve the work?). Control for the skill's extra tokens with an equally long, unrelated-text arm.
- Test on real tasks in the target model, tools, repository, and context. Keep results and costs with the skill, and rerun when the model or relevant environment changes.

## A practical creation loop

1. **Define the objective.** State in one sentence what must improve and how you will measure it. If the outcome cannot be measured, the skill remains an untested preference.
2. **Find candidate ideas.** Run the agent without the skill on representative tasks. Look for repeated failures; Makarevych gives these more weight than generic doctrine. For each proposed point, write a claim of the form: *the agent should do X because it is expected to improve Y through Z*. Mark expert advice without supporting evidence as untested.
3. **Write only the instructions that deliver those points.** Keep core ideas distinct from secondary guidance, examples, persuasion text, and routing/loading hooks. Use examples and terminology that match the target agent's actual environment.
4. **Measure adherence from the run log.** Define an observable check for each point, such as whether the agent opened a skill, ran a command, or made a required change. Report how often applicable points were followed. Adherence shows whether the text worked as instructions; it does not show that the instructions were useful.
5. **Measure effect on task quality.** Use realistic tasks with outcomes the agent cannot see, hidden checks where appropriate, and human-calibrated quality labels for generated artifacts. Count quality, not just visible effort such as number of tests or lines written.
6. **Compare controlled arms.** At minimum compare no skill, the skill, and a sensible unrelated text of similar token length. Where relevant, add a competing procedure and compare the skill body with and without a routing hook. Run several fresh sessions per task and report results by model, including tokens, time, and monetary cost.
7. **Decide from both metrics.** Low adherence points to unclear, overlong, or poorly triggered instructions—revise the wording and retest. High adherence with no improvement means the idea did not help in this setting—remove or change it. Keep a point only when measured gains beat both baseline and the length control and justify their cost.
8. **Ship an evaluation bundle, not just a prompt.** Keep the skill text, its points and hypotheses, eval tasks, graders, results, model/environment versions, and known limits together. Rerun after changes to the model, tools, libraries, or relevant context.

## Why the controls matter

The article separates two failure modes that an outcome score alone cannot diagnose: an agent may fail to follow an instruction, or follow it faithfully without producing better work. A length-matched control also distinguishes the skill's ideas from the generic effect of adding more context. If installation adds a hook or the skill is not reliably selected, loading is another factor to measure rather than silently mixing into the result.

The author's example is a test-driven-development skill. He extracts individual testable claims from its instructions, proposes behavioral graders using tool logs, and compares multiple evaluation arms. The design is transferable; the numerical claims in the article are not universal guarantees.

## Limits and cautions

- Results are specific to a model, task distribution, tools, and surrounding instructions. “Worked for me” is not evidence of transfer to a different setup.
- Adherence graders can reward superficial compliance; evaluate the checks together and make sure each corresponds to the intended behavior.
- A hidden benchmark is only useful if its checks represent the real objective. For subjective artifacts, quality labels need a rubric and calibration against human judgments.
- The article surveys external studies and reports substantial costs or regressions for some skills. This note captures the proposed method; it does not independently audit those studies or reproduce the article's measurements.
- External skills may include scripts or ask agents to use powerful tools. Review their contents, permissions, and data flows before installing them.

## Related concepts

- [SkillOpt and training agent skills without touching model weights](2026-06-11_article_skillopt-and-training-agent-skills-without-touching-model-weights.md) — a related optimization approach using bounded edits and held-out validation.
- [Agent Skills with Anthropic course](2026-07-15_tweet_agent-skills-with-anthropic-deeplearning-ai-course.md) — skill anatomy, progressive disclosure, and how skills compose with tools and subagents.
- [Matt Pocock: Skills v1.3 — implement-spec, pr, and retro](2026-10-05_youtube_matt-pocock_skills-v1-3.md) — turn recurring agent-session failures into reusable improvements.
- [How to use decision models for evals](2026-10-20_article_hamel-husain_decision-model-evals.md) — a concrete case of choosing metrics, thresholds, and calibration for an automated evaluator.

## Sources

- [Sergii Makarevych's announcement](https://x.com/sermakarevich/status/2112198653469241856)
- [How to write and test agent skills with evals](https://x.com/i/article/2112186374052802560)
- [Agent Skills specification](https://agentskills.io/specification)

Raw capture: [article outline and paraphrased extraction](raw/2026-10-19_article_sergii-makarevych_agent-skill-evals.raw.md).
