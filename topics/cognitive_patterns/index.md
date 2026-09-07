# Cognitive patterns

A cognitive pattern is a reusable reasoning procedure that can be applied across domains.

Cognitive patterns capture how to think about a problem. Each pattern contains reusable questions, reasoning steps, failure modes, evaluation criteria, and an example of how the procedure can transfer between domains.

## Why they exist

Concepts and source notes provide knowledge and evidence. They do not always show how to examine a new problem. Cognitive patterns make useful reasoning procedures easy to find, apply, test, and improve.

Patterns guide reasoning. They are not evidence, and they should not determine a conclusion before the evidence has been examined.

## How agents should use patterns

1. Retrieve the relevant concepts and source material.
2. Name the problem type and choose the smallest useful set of patterns.
3. State what each pattern is expected to add.
4. Apply the questions and procedure to the available evidence.
5. Check the failure modes and evaluation criteria.
6. Name the patterns used in the answer or investigation.

Use direct reasoning for routine questions and agreed execution steps. Otherwise, use one pattern when it can answer the question. Combine patterns only when each one covers a distinct gap, and decide how to resolve disagreements before applying them. Agents should treat patterns as reasoning guidance. Claims still need support from concepts, sources, or direct evidence.

An intervention during shared work should address a current gap and fit the user's goals and working preferences. Offer optional ideas briefly, allow them to be ignored, and carry out agreed actions without another approval loop. The [selection guidance](select_cognitive_patterns.md#when-to-contribute-during-shared-work) distinguishes an opportunity to contribute from a reason to interrupt.

## How humans should use patterns

Use a pattern as a checklist when framing a question, reviewing an argument, or planning an investigation. Adapt the steps to the problem. Record where the pattern helped, where it failed, and which conditions limited its use.

## How patterns differ from other notes

- A source note captures information from a specific source.
- A concept note consolidates knowledge about one idea.
- An investigation records reasoning about a specific question.
- A cognitive pattern provides a reusable procedure for reasoning across many questions and domains.

A cognitive pattern should not repeat factual content from a concept. Its value comes from the questions, steps, checks, and failure modes that can be reused elsewhere.

## Choose and combine patterns

- [Select cognitive patterns](select_cognitive_patterns.md) when the right procedure is unclear.
- [Decompose and abstract](decompose_and_abstract.md) when a question must be divided into manageable parts or a successful method should transfer to another domain.
- [Combine cognitive patterns](combine_cognitive_patterns.md) when one procedure leaves an important gap.

## Examine claims and uncertainty

- [Check evidence quality](check_evidence_quality.md) to trace a consequential claim to its observations and preserve the limits of what they support.
- [Examine a causal claim](examine_a_causal_claim.md) to define an intervention comparison and inspect the assumptions needed for an effect estimate.
- [Generate counterexamples](generate_counterexamples.md) to find where a claim fails.
- [Approximate and check easy cases](approximate_and_check_easy_cases.md) to simplify a model, record what was discarded, and test units and boundaries.
- [Reason from first principles](reason_from_first_principles.md) to rebuild an argument from constraints and mechanisms.
- [Test competing hypotheses](test_competing_hypotheses.md) to separate plausible explanations with useful observations.
- [Update beliefs with evidence](update_beliefs_with_evidence.md) to revise confidence from a prior belief and new evidence.
- [Verify with independent estimates](verify_with_independent_estimates.md) to check a result through routes that can fail for different reasons.

## Examine systems and interventions

- [Analyze capability accumulation](analyze_capability_accumulation.md) to explain how practical capability grows or decays.
- [Compare ecosystems](compare_ecosystems.md) to compare actors, flows, feedback, and learning.
- [Evaluate incentives](evaluate_incentives.md) to predict how rules, rewards, and constraints change behaviour.
- [Find leverage points](find_leverage_points.md) to choose interventions that change system behaviour.
- [Identify feedback loops](identify_feedback_loops.md) to explain change, resistance, growth, and decline over time.

## Examine plans and risks

- [Run a pre-mortem](run_a_pre_mortem.md) to find specific failure paths before committing to a plan.
- [Test a plan across plausible futures](test_a_plan_across_plausible_futures.md) to compare options under the same uncertain external conditions and define adaptations.

## Evidence and evaluation

A pattern can improve the structure of an analysis without improving its conclusion. Evaluate patterns against outcomes when possible. Compare the result with direct reasoning, use tasks with enough room for improvement, and repeat tests before claiming that a pattern improves accuracy.

Record the exact procedure and comparison used in a test. Distinguish tests that were never run from tests that found no useful gain. Check practical benefit, added effort, and evidence quality separately from statistical significance. Upstream version 1.0 has no skill approved for automatic invocation under its evaluation policy. Our patterns remain experimental, and deliberate use here follows Lode's instructions rather than an upstream accuracy claim.

Use [Evaluate changes to cognitive patterns](evaluate_pattern_changes.md) to distinguish editorial checks from controlled outcome comparisons. An author's worked examples can expose gaps without establishing improved accuracy or reduced human effort.

## Investigations

- [September public source update](2026-09-07_investigation_public-source-pattern-update.md) records the source decisions, three additions, and bounded editorial checks for the 18-pattern collection.
- [Review of cc-thinking-skills version 1.0](2026-09-07_investigation_cc-thinking-skills-v1-review.md) compares all 15 local patterns with the release, updates seven procedures, and explains which upstream changes were not adopted.
- [Applying *The Art of Insight* to human–AI cognitive patterns](2026-07-20_investigation_art-of-insight-for-human-ai-cognitive-patterns.md) identifies improvements for decomposition, independent verification, controlled simplification, and easy-case testing.

## Pattern lifecycle

1. Select a pattern.
2. Apply it to an investigation.
3. Record whether it was useful.
4. When it succeeds repeatedly, use [Decompose and abstract](decompose_and_abstract.md) to name the operation that made it work.
5. Test that operation outside the original domain before generalizing it.
6. Add examples, failure modes, or scope conditions when repeated use supports the change.
7. Revise or retire the pattern when it stops helping.

## Sources

- [CIA Tradecraft Primer](2009-03_source_cia_tradecraft-primer.md) informs evidence quality and assumption checks.
- [GO-Science Futures Toolkit](2024-08-29_source_go-science_futures-toolkit.md) informs scenario comparison.
- [Causal Inference: What If](2026-08-19_book_hernan-robins_causal-inference-what-if.md) informs intervention comparisons and causal assumptions.
- [Proactive thought partners for writing](../agents/2026-09-07_tweet_omar-sar_proactive-thought-partners-for-writing.md) informs the timing and form of contributions during shared work.
- [The Art of Insight in Science and Engineering](2014-01-01_book_sanjoy-mahajan_the-art-of-insight-in-science-and-engineering.md) provides a practical toolkit for organizing or carefully discarding complexity.
- [Claude Code Thinking Skills and this notes repo](2026-07-20_github_tjboudreaux_cc-thinking-skills.md)
  explains which ideas were adopted, what changed, and why patterns are still
  treated as guidance rather than proof.
