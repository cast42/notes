---
title: "Review of cc-thinking-skills version 1.0"
date: 2026-09-07
type: investigation
topics:
  - cognitive_patterns
tags:
  - mental-models
  - reasoning-procedures
  - evaluation
  - source-review
resource: "https://github.com/tjboudreaux/cc-thinking-skills/releases/tag/v1.0.0"
description: "Compares version 1.0 with the earlier source snapshot and all 15 local patterns, adopts seven targeted refinements, and preserves separate book-derived methods."
source_revision: "32f612605ae79bb8fd5a343605d7b7b7806b6bed"
compared_source_revision: "0313ee0d476bf9db2c38ad8bd11d9933a61350d4"
sources:
  - id: release
    resource: "https://github.com/tjboudreaux/cc-thinking-skills/releases/tag/v1.0.0"
  - id: audit
    resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/analysis/AUDIT.md"
  - id: evidence
    resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/analysis/evidence.json"
  - id: procedures
    resource: "https://github.com/tjboudreaux/cc-thinking-skills/tree/32f612605ae79bb8fd5a343605d7b7b7806b6bed/skills"
  - id: later-study
    resource: "https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/evals/studies/scientific-method-vnext/tool-v1-disposition.json"
generated:
  by: "process:codex"
  at: "2026-09-07T10:50:21+00:00"
---

# Review of cc-thinking-skills version 1.0

## TL;DR

Version 1.0 contains useful refinements for the notes repo. Seven existing patterns were updated, all 15 were retained, and no new standalone pattern was needed. The three patterns added from *The Art of Insight* remain unchanged.

The upstream catalog has 28 skills, compared with 39 at our earlier source snapshot. Its authors shortened the procedures and consolidated overlapping skills. They still report no skill approved for automatic invocation under their evaluation policy. The local patterns remain experimental.

## Key takeaways

- Choose no pattern when direct reasoning is sufficient, and define when to stop or reconsider a poor fit.
- Before combining patterns, state each pattern's unique question and how disagreements will be resolved.
- Prefer simpler hypotheses only among explanations that still fit the evidence.
- Turn serious pre-mortem failure conditions into verifiable prevention requirements and conditions for proceeding.
- Separate statistical significance, practical usefulness, evidence quality, and studies that were never run.

## What was compared

The comparison starts from the exact revision recorded in the [original source note](2026-07-20_github_tjboudreaux_cc-thinking-skills.md), `0313ee0d476bf9db2c38ad8bd11d9933a61350d4`, and ends at the version 1.0 tag, `32f612605ae79bb8fd5a343605d7b7b7806b6bed`. The release was published on August 4, 2026.[^release]

The original note is dated July 20, but its source revision is from June 8. Several changes included in version 1.0 were committed in July. The findings cover all changes since the saved June 8 revision.

The current main revision inspected was `7b8fece345dfaa11773be7152ccd194589cb5437`, dated August 7. Only `README.md` differs between that revision and the release tag. The skill bodies and audit evidence inspected are therefore the release versions. The later README describes broader distribution and the current catalog; those documentation changes do not require changes to the local reasoning procedures.

## Decisions for all 15 local patterns

The five patterns introduced in the original upstream review all receive small updates. First principles and feedback loops receive useful checks from overlapping upstream procedures. Each changed pattern links to its exact release source.

| Local pattern | Decision | Reason or applied change |
| --- | --- | --- |
| [Select cognitive patterns](select_cognitive_patterns.md) | Updated. | Make no pattern an explicit result, compare input and time needs, and limit repeated attempts to find a fit. |
| [Combine cognitive patterns](combine_cognitive_patterns.md) | Updated. | Choose a disagreement rule in advance, state unique questions, and retain checks that affect confidence or risk even when the recommendation stays the same. |
| [Test competing hypotheses](test_competing_hypotheses.md) | Updated. | Allow two serious alternatives, avoid invented rivals, check stale observations, and rank simpler explanations only after evidence fit. |
| [Update beliefs with evidence](update_beliefs_with_evidence.md) | Updated. | Challenge the prior, make forecasts checkable, stop when the decision is stable, and link to existing estimation procedures. |
| [Run a pre-mortem](run_a_pre_mortem.md) | Updated. | Identify enabling conditions for failure and turn them into verifiable prevention requirements with owners and decisions about proceeding. |
| [Reason from first principles](reason_from_first_principles.md) | Updated. | Require support for claimed constraints, preserve binding obligations, add skip conditions, and define a cheap disconfirming check. |
| [Identify feedback loops](identify_feedback_loops.md) | Updated. | Define the boundary, distinguish accumulated quantities from rates, check loop signs and delays, and state a disconfirming observation. |
| [Find leverage points](find_leverage_points.md) | Retained unchanged. | Already compares intervention levels, feasibility, reversibility, and side effects. Choosing an intervention remains a separate task from explaining loops. |
| [Decompose and abstract](decompose_and_abstract.md) | Retained unchanged. | Already covers factor decomposition, interactions, and transfer to a different problem. |
| [Approximate and check easy cases](approximate_and_check_easy_cases.md) | Retained unchanged. | Already covers bounds, needed precision, units, sensitivity, and when to replace an approximation. |
| [Verify with independent estimates](verify_with_independent_estimates.md) | Retained unchanged. | Its independent evidence routes and human-first estimate protocol add checks beyond upstream combination rules. |
| [Generate counterexamples](generate_counterexamples.md) | Retained unchanged. | It already tests scope conditions and challenges unsupported generalization. |
| [Evaluate incentives](evaluate_incentives.md) | Retained unchanged. | Its actor responses, gaming checks, and persistent effects cover the relevant overlap with systems and second-order reasoning. |
| [Compare ecosystems](compare_ecosystems.md) | Retained unchanged. | Its cross-domain comparison and transfer limits have a distinct local purpose. |
| [Analyze capability accumulation](analyze_capability_accumulation.md) | Retained unchanged. | Its learning, tacit knowledge, and capability decay questions have a distinct local purpose. |

## What the upstream mergers mean here

The authors reduced the catalog from 39 skills to 28. Most removed procedures were incorporated into retained skills. The dual-process skill was removed without a named replacement.[^audit]

| Earlier upstream skills | Version 1.0 destination | Local implication |
| --- | --- | --- |
| Model selection | Model router | Update the source link and strengthen selection. |
| Bayesian reasoning and Fermi estimation | Probabilistic thinking | Keep belief updating separate from the existing decomposition and approximation notes, with links between them. |
| Inversion | Pre-mortem | Add the failure-condition reversal step to the existing pre-mortem. |
| Occam's razor | Scientific method | Rank the hypotheses that survive evidence checks by unsupported assumptions. |
| Archetypes, feedback loops, and leverage points | Systems | Keep the two focused local patterns and improve loop checks. A generic archetype catalog is not required by the current notes. |
| Debiasing | Probabilistic thinking and steel-manning | Add a serious challenge to the prior instead of creating a general bias checklist. |
| Regret minimization | Reversibility and opportunity cost | No matching local pattern needs migration. Reconsider only if a concrete investigation exposes a gap. |
| Dual process | No named replacement | No local counterpart needs action. |

An upstream packaging decision does not by itself justify merging local concepts. I used [Generate counterexamples](generate_counterexamples.md) to test that inference. Feedback analysis and intervention selection provide a concrete counterexample because a reader can need either procedure separately. The local distinction remains useful even though both are packaged together upstream.

## Evaluation claims that needed correction

The version 1.0 registry contains a later historical scientific-method test with 426 scored cases. Reported accuracy was 92.5 percent with the skill and 88.5 percent with an active placebo, a difference of 4.0 percentage points. The reported continuity-corrected significance test gives approximately `p = 0.00048`. The result is statistically significant, but it is below the authors' 5 percentage point usefulness threshold.[^evidence]

The authors still classify the result as provisional. Their recorded defects include permissive filename scoring and missing raw responses. The comparator also contains advice, so it is not a clean measure against ordinary use without a skill. The result does not establish a gain for the rewritten version 1.0 procedures or for our local adaptations.[^evidence]

The planned `portfolio-v1` evaluation made zero model calls. It remains unmeasured. All 28 active skills have `disable-model-invocation: true`, and none meets the authors' conditions for automatic retention. An unrun study and a measured absence of improvement are different findings.[^evidence]

A later experiment using repository tools also does not establish improvement. Its calibration failed the required completion checks. Confirmation and replication were skipped, and the recorded disposition says that no skill edit was applied. Experimental candidate prompts were therefore not imported into the notes.[^later-study]

For future local evaluation, record the exact pattern revision and compare it with direct reasoning on relevant tasks. Check useful changes to the answer or decision, human verification effort, and added interaction cost. Preserve evidence that permits review, and repeat a successful test before making a general accuracy claim.

## What was deliberately not adopted

- The upstream installation instructions and plugin settings are distribution details. No skills were installed and no agent settings were changed.
- The upstream manual-invocation policy does not override Lode's instruction to use local cognitive patterns when useful. It limits what we can claim about measured effectiveness.
- Fixed router weights and numerical probability bands were not adopted because their apparent precision is not established for this local workflow.
- The probabilistic skill's stronger preference for numbers does not justify invented base rates or calibrated intervals. Qualitative updates remain appropriate when inputs are weak.
- The book-derived approximation record, easy-case checks, and independent human estimate protocol remain intact. The [book investigation](2026-07-20_investigation_art-of-insight-for-human-ai-cognitive-patterns.md) remains a record of their original rationale.

## Sources

[^release]: [Version 1.0 release](https://github.com/tjboudreaux/cc-thinking-skills/releases/tag/v1.0.0). Commit history and the tree comparison were checked in a local clone.
[^audit]: [Catalog audit at version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/analysis/AUDIT.md), especially the catalog consolidation table. Procedure links are in the seven updated local patterns.
[^evidence]: [Evidence registry at version 1.0](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/analysis/evidence.json) and the [historical scientific-method aggregate](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/evals/studies/legacy-july-sci-method-larger-n/aggregate.json).
[^later-study]: [Scientific-method experiment disposition](https://github.com/tjboudreaux/cc-thinking-skills/blob/32f612605ae79bb8fd5a343605d7b7b7806b6bed/evals/studies/scientific-method-vnext/tool-v1-disposition.json).
