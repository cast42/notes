---
title: "Working extraction: How to write and test agent skills with evals"
date: 2026-10-19
type: source
topics:
  - agentic_coding
tags:
  - agent-skills
  - evaluation
resource: "https://x.com/i/article/2112186374052802560"
generated:
  by: "process:codex"
  at: "2026-10-19T22:37:00+02:00"
extractor: "FxTwitter API; paraphrased for copyright-conscious source capture"
sources:
  - id: "announcement-post"
    resource: "https://x.com/sermakarevich/status/2112198653469241856"
  - id: "article"
    resource: "https://x.com/i/article/2112186374052802560"
---

# Working extraction

This is a paraphrased outline, not a verbatim transcript or complete copy of the article.

## Announcement post

Sergii Makarevych asks how to create skills and determine whether third-party skills help. He argues that many shared skills have not been evaluated and links to his article on writing and testing skills with evals.

## Article argument and method

The article describes a skill as text added to an agent's context to encourage a repeatable behavior. It argues that formatting or publishing a skill does not establish that it works, and that results from one agent setup may not transfer to another.

The proposed method starts from a measurable objective. The author recommends extracting a short list of points from the skill, each with a testable explanation for why the behavior should help. Points grounded in repeated failures observed in a no-skill baseline are treated as stronger starting hypotheses than unsupported doctrine. The instruction text should implement those points; secondary points, persuasive language, and loading hooks should be tracked separately.

Two metric families are required:

- **Adherence:** determine from the run log whether the agent followed each applicable point and whether the skill was loaded.
- **Effect:** determine whether task outcomes improved using hidden checks or quality ratings of the actual work. Do not assume that more activity or more generated tests means better work.

The proposed comparisons include a no-skill baseline, the skill, and an unrelated text of similar length to control for extra context. Add comparisons for an alternative procedure or a routing hook when those factors matter. Use real tasks, the target model and environment, multiple fresh runs, and include time and token costs.

Interpret the metrics together. Low adherence means the instructions may need to be shortened, clarified, or triggered more reliably; it does not test whether the underlying idea helps. High adherence without improved outcomes means the instruction was followed but the idea did not help in the tested setup. Retain only points whose effects survive comparison with baseline and the length control, at an acceptable cost.

The article recommends preserving the skill, extracted points, hypotheses, eval set, graders, results, and model/version information as one bundle. Rerun evaluations when the model or the tools and libraries relevant to the skill change. It also argues for reviewing third-party skills, including any scripts or tool permissions they introduce.

## Limits

The article cites published studies and vendor claims about skills, evaluation results, security, and costs. This capture does not independently verify those sources or reproduce the article's experiments. Its experimental design recommendations should be evaluated for the task and context where they are used.
