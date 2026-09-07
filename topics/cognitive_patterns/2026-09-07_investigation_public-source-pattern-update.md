---
title: "Updating cognitive patterns from public sources"
date: 2026-09-07
type: investigation
topics:
  - cognitive_patterns
tags:
  - source-review
  - reasoning-procedures
  - evaluation
  - human-ai-collaboration
description: "Records the source decisions, bounded checks, and limitations of the September cognitive pattern update."
sources:
  - id: cia
    resource: "https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf"
  - id: futures
    resource: "https://www.gov.uk/government/publications/futures-toolkit-for-policy-makers-and-analysts/the-futures-toolkit-html"
  - id: causal
    resource: "https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf"
  - id: nist-design
    resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm"
  - id: nist-randomization
    resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm"
  - id: nist-blocking
    resource: "https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm"
  - id: double-crux
    resource: "https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-mutual-understanding"
  - id: meadows
    resource: "https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/"
  - id: proactive-writing
    resource: "https://arxiv.org/html/2609.01588v1"
generated:
  by: "process:codex"
  at: "2026-09-07T13:29:46+00:00"
---

# Updating cognitive patterns from public sources

## TL;DR

The update starts from notes commit `66b333a`, which includes the completed v1 review at `7feac3c` and a newly captured post about proactive writing partners. All 15 existing patterns remain available. Three additions cover evidence quality, scenario comparison, and causal claims. Five existing patterns receive focused changes, and the collection now has 18 experimental patterns.

The checks found clearer instructions and one stopping-rule inconsistency in the existing hypothesis pattern. They did not demonstrate better answers than direct reasoning. No controlled model experiment or human outcome study was run.

## Key takeaways

- Preserve the difference between inspecting evidence, comparing explanations, and estimating an intervention effect.
- Compare options across the same futures without inventing probabilities.
- Preserve independent estimates before discussing a decisive assumption.
- Treat the writing study as design inspiration with explicit transfer limits.

## Evaluation protocol recorded before pattern edits

The following five synthetic cases and checks were written before changing pattern procedures in this update. They are small editorial checks, not observations of real projects. The author has already read the proposed sources and knows the intended changes. Neither baseline reasoning nor later review is blind or independent.

For each case, record a direct answer first, inspect the baseline guidance at `66b333a`, then apply revised guidance to the same facts. The same Codex session at the user-selected High effort performs the comparison. There are no separate model trials or measured time savings. Record concrete omissions, justified changes, and extra steps instead of numerical quality scores. Keep a final transfer case out of the pattern examples; select it after the first drafts and report its limited independence.

| Case and fixed facts | Check specified in advance |
| --- | --- |
| Evidence. Three articles repeat one vendor's claim of 30 percent less energy use. The underlying test is a selected sample of ten vehicles, with no stated comparison group. A city wants a fleet-wide forecast. | Trace one underlying origin, preserve the restricted population, and refuse to infer a city-wide causal saving. |
| Planning. A depot must choose fixed charging capacity or staged installation. Demand may be low or high; the grid upgrade may arrive on time or two years late. Staging costs more per installed unit but can defer unused capacity. No probabilities or cost figures are available. | Examine all four combinations, separate external conditions from available actions, and avoid an invented probability or numerical optimum. |
| Causality. Volunteer depots adopt route software and report 12 percent lower energy use afterward. Non-adopters do not report comparable data. Season and routes also changed. | Define the comparison that is needed, identify selection and concurrent changes, and withhold a causal percentage. |
| Disagreement. A human expects 10 MWh of daily charging, while an AI estimates 16 MWh. The human assumes 60 active trucks and the AI assumes 100. Both use 160 kWh per truck per day. The human also values spare capacity more. | Reconcile 9.6 and 16 MWh by the fleet-count assumption, seek an activity record, and keep the reserve preference separate from the factual estimate. |
| Routine work. The user authorizes correcting a typo in a paragraph. No substantive claim changes. | Make the correction without a pattern exercise, speculative monitoring, or another approval question. |

## Direct answers and baseline inspection

- Evidence. Direct reasoning already identifies one vendor sample and insufficient support for a causal fleet forecast. Baseline independent verification warns about shared evidence, and hypothesis testing warns about stale records. Source provenance, measurement context, and permissible claim scope are not collected in one dedicated procedure.
- Planning. Direct reasoning identifies demand and grid timing as separate uncertainties and cannot rank costs without figures. The baseline pre-mortem finds ways a choice could fail, while leverage analysis considers feasibility. Neither requires comparing every option across the same external conditions.
- Causality. Direct reasoning identifies self-selection and seasonal change. Baseline hypothesis testing can compare those explanations but does not require a defined intervention, alternative, population, and outcome period before interpreting an effect estimate.
- Disagreement. Direct calculation gives 9.6 and 16 MWh. Baseline independent verification already requires matching definitions and explaining disagreement before averaging. A change should preserve that procedure rather than claim to invent it.
- Routine work. Direct reasoning and the baseline selection pattern both support correcting the typo immediately. Any revision that adds a confirmation loop fails this check.

## Source decisions and final checks

### What each source changed

| Source and reviewed material | Evidence type and limits | Applied decision |
| --- | --- | --- |
| [CIA primer](2009-03_source_cia_tradecraft-primer.md), March 2009, printed pages 7 to 11 | Professional analytic guidance, not an AI effectiveness study. | Add [Check evidence quality](check_evidence_quality.md). Preserve source qualifications and name the assumption connecting evidence to its use. Existing first-principles guidance already challenges assumptions, so no separate assumption pattern is added. |
| [Futures Toolkit](2024-08-29_source_go-science_futures-toolkit.md), August 29, 2024 HTML, Scenarios and Policy Stress-Testing | Facilitated foresight methods; a short solo application has less diversity of experience. | Add [Test a plan across plausible futures](test_a_plan_across_plausible_futures.md). Keep it separate from failure-path analysis in a pre-mortem. |
| [What If](2026-08-19_book_hernan-robins_causal-inference-what-if.md), August 19, 2026 PDF, chapter 3 and sections 6.4 and 7.3 | Formal causal methods depend on substantive assumptions. A checklist cannot verify them. | Add [Examine a causal claim](examine_a_causal_claim.md) as a screening procedure. Do not implement an effect estimator. |
| [NIST design selection](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm), sections 5.3, [5.3.3.1](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm), and [5.3.3.2](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm), accessed September 7, 2026 | Engineering experimental-design guidance, not a tested model-evaluation package. | Add a conditional experiment branch to [Test competing hypotheses](test_competing_hypotheses.md) and a supporting [evaluation procedure](evaluate_pattern_changes.md), not another cognitive pattern. |
| [Double Crux](https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-mutual-understanding), Duncan Sabien, January 2, 2017, "How to play" | Practitioner method for human disagreement. | Add a bounded disagreement procedure to [Combine cognitive patterns](combine_cognitive_patterns.md). Link to it after independent estimation. Do not equate an AI output with an independent human belief. |
| [Meadows' Leverage Points](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/), introduction, revised list, and parameter discussion, accessed September 7, 2026 | Systems guidance with explicit limits on generalization. | Clarify the local grouping and add the missing feedback category to [Find leverage points](find_leverage_points.md). Require a mechanism check and a stopping condition. |
| [Designing Proactive Thought Partners for Writing](https://arxiv.org/html/2609.01588v1), September 1, 2026 v1, sections 4, 6, 7, and 9 | Exploratory one-week study with 16 participants. It does not establish causal gains in writing quality or productivity. | Extend [Select cognitive patterns](select_cognitive_patterns.md) and usage guidance. Reuse the existing [post and paper note](../agents/2026-09-07_tweet_omar-sar_proactive-thought-partners-for-writing.md). No new agent, monitoring feature, or approval loop is introduced. |

The three new patterns have different outputs. Evidence review produces a defensible claim scope. Scenario comparison produces conditional choices. Causal review specifies a comparison and its identification limits. Their overlap is handled by links instead of merging the procedures.

### Worked results under the revised guidance

| Case | Result of applying the revised procedure | Difference from baseline and cost |
| --- | --- | --- |
| Evidence | The three reports have one underlying vendor source. The selected ten-vehicle test has an unspecified comparator. A fleet-wide 30 percent saving is unsupported. Request the test protocol and comparison before using it in a forecast. | The direct conclusion is unchanged. The new procedure provides one record for origin, sample, comparison, and claim scope. It adds a source-tracing step rather than three separate corroboration searches. |
| Planning | Under low demand and an on-time grid upgrade, fixed capacity risks idle investment while staging carries its unit-cost premium. Under high demand and an on-time upgrade, fixed capacity may meet demand sooner; staging must allow timely expansion. Under low demand and a late upgrade, staging may reduce idle commitment, but usable interim capacity still needs checking. Under high demand and a late upgrade, neither option alone solves the supply constraint; investigate feasible interim operation or a changed schedule. | The matrix makes the four combinations explicit. No cost optimum is established. Additional work is four comparisons and a request for capacity, cost, and lead-time data. Staging is not assumed to solve grid delay. |
| Causality | Define assignment to a specified software version versus existing routing, among eligible depots over the same follow-up period, with comparable energy measurements. Volunteer selection, route changes, and season prevent attributing the reported 12 percent decline to software. Seek a defensible contemporaneous comparison and assignment strategy. | Direct reasoning already withholds the percentage. The revision makes population, treatment, outcome period, and study-design gaps explicit. It requires more specification before estimation. |
| Disagreement | Sixty trucks at 160 kWh gives 9.6 MWh; 100 trucks gives 16 MWh. Ten MWh is a rounded estimate. Reconcile the number active on the planning day using scheduling records. Decide the desired reserve separately. | Baseline verification already exposes the count difference. The extension names the disputed assumption and separates the reserve preference. No additional independent evidence is created by agreement. |
| Routine work | Correct the authorized typo immediately. | The revision preserves baseline behavior. No pattern exercise or new approval question is needed. |

For the planning case, a review trigger must arrive before the installation decision becomes irreversible. A proposed quarterly check is inadequate if equipment must be ordered six months ahead. The owner should schedule the check before that ordering deadline and use confirmed grid capacity and the fleet schedule as inputs. No actual owner or operational monitoring task is assigned by this synthetic example.

### Transfer and counterexample checks after drafting

A fresh author-selected case concerns a library. A report says extended opening hours increased borrowing by 20 percent. The earlier count excludes renewals, while the later count includes them. No comparable count is supplied. The revised evidence procedure identifies the changed outcome definition before attempting a causal review. Request consistently defined counts; neither the 20 percent comparison nor an effect of opening hours is established. The case is outside the new patterns' worked examples, but it was selected by the same author and is not a blind held-out test.

Three boundary checks were also applied:

- A trustworthy association does not automatically support causation. Keep a causal claim unresolved when the necessary comparison is missing; do not infer that the effect is zero.
- A small parameter adjustment near a capacity threshold can be more useful than an infeasible goal change. The revised leverage guidance passes this counterexample to choosing by hierarchy alone.
- Two hypotheses may remain indistinguishable after every affordable observation. Baseline step 9 required a supported single explanation to stop, despite its output allowing uncertainty. The revised stopping rule explicitly permits ending with unresolved alternatives when further discrimination is unavailable at a justified cost. The evaluation wording also no longer requires several alternatives when only one is serious.

The source and stopping checks support retaining the revisions as experimental guidance. They do not support a claim that the revised collection improves accuracy, saves time, or reduces interruptions in practice. Actual human verification burden was not measured.

## Changes deliberately excluded

- The completed v1 migration is not repeated. The earlier review remains a historical record.
- Decomposition and approximation procedures from Mahajan remain unchanged. Independent estimation retains its method and only gains a link to the later disagreement step plus explicit provenance metadata.
- No separate generic assumptions, disagreement, experimental-design, or proactive-agent pattern is added. The supporting evaluation document has type `procedure` and is not counted among the 18 patterns.
- No upstream skill package, agent configuration, background observation, or scheduled task is installed.
- No source claims are converted into a guarantee of human or AI improvement.

## Validation and publication record

The OKF validator passed with 293 concept files, 18 reserved files, and zero warnings. The collection contains exactly 18 cognitive patterns. The decomposition and approximation files are byte-for-byte unchanged from the baseline. The working diff passes the whitespace check.

The follow-up article, [Updating my cognitive patterns with clearer evidence checks](https://cast42.github.io/blog/2026/09/07/updating-my-cognitive-patterns-with-clearer-evidence-checks/), was prepared in an isolated checkout of `cast42/blog`. A strict MkDocs build passed, and the local browser preview showed the article, navigation, and comparison table correctly. The post links back to the July introduction and attributes each source near the relevant contribution. It uses original synthetic examples and reproduces no source figures or extended quotations.

The earlier v1 review and this investigation provide the change history. Controlled model trials, an independent reviewer, and measured human outcomes remain unrun. The [evaluation procedure](evaluate_pattern_changes.md) records how to run those studies if an effectiveness claim is needed.

## Related concepts

- [Cognitive pattern index](index.md)
- [Earlier v1 review](2026-09-07_investigation_cc-thinking-skills-v1-review.md)
- [Evaluate changes to cognitive patterns](evaluate_pattern_changes.md)

## Sources

The source decision table links the exact material used. Source metadata records provenance; no `verified` event is inferred from successful format validation. The examples and case judgments above are local synthetic work, not outcomes reported by the source authors.
