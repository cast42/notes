---
title: "Ethan Mollick on AI factual search and verification"
date: 2026-11-07
type: tweet
topics:
  - agentic_coding
tags:
  - factuality
  - fact-checking
  - benchmark-interpretation
  - human-ai-evaluation
resource: "https://x.com/emollick/status/2119140502746308674"
author: "Ethan Mollick"
description: "Mollick questions whether everyday AI factual errors receive too much verification concern, citing browsing and scientific claim-checking benchmarks."
sources:
  - id: post
    resource: "https://x.com/emollick/status/2119140502746308674"
  - id: browsecomp
    resource: "https://openai.com/index/browsecomp/"
  - id: deepfact
    resource: "https://aclanthology.org/2026.acl-long.1586/"
---

# Ethan Mollick on AI factual search and verification

## TL;DR

Mollick argues that concern about factual errors in everyday AI work is excessive, pointing to results where AI agents outperform human comparison groups on factual search and checking scientific claims. His post usefully challenges the assumption that unaided human verification is automatically superior. The cited benchmarks show capabilities on particular tasks, however, not that verification is unnecessary in ordinary work or that AI is universally more reliable than experts.

## What the post presents

- **BrowseComp:** its image compares human searchers with later AI-agent results. The chart reports 25.3% reference matches for humans and roughly 90–92% for selected agents. These are not a controlled head-to-head comparison with identical budgets or setups; the chart itself notes that they differ. OpenAI describes the benchmark as 1,266 deliberately difficult, short-answer web questions and cautions that its relationship to real, open-ended user queries is unclear. In the human study, 317 of 1,255 answers matched the reference; many questions were marked unsolvable after roughly two hours. [browsecomp]
- **DeepFact:** the image reports 60.8% for PhD-level specialists working unaided, about 89% for a GPT-5 agent, 90.9% for humans auditing agent-raised disagreements, and 93.0% for the best agent-auditor pairing. These refer to specific conditions and rounds, not a universal ranking of people and AI. The image notes the comparison uses 143 known-answer claims, 120 deliberately unsupported; always answering unsupported would score 83.9%. [post] [deepfact]
- **Audit-then-score:** DeepFact lets challengers submit evidence against benchmark labels and has auditors adjudicate before updating them. The authors report experts’ hidden known-answer accuracy improving from 60.8% initially to 90.9% after additional audit rounds. Their abstract separately reports 83.4% for DeepFact-Eval on the frozen benchmark; do not confuse that full benchmark result with the image’s selected micro-gold comparisons. [deepfact]

## Interpretation and limits

Finding a hard-to-locate fact, checking a scientific claim, auditing supplied evidence, and reviewing an everyday AI-generated answer are different tasks. The DeepFact human and agent conditions also provide different inputs and opportunities for revision. The error-heavy test’s class imbalance means raw accuracy alone conceals how well a method identifies supported versus unsupported claims. The cited figures cannot establish a general everyday error rate.

The practical question is not simply “AI or human?” but **which combination of search, checks and judgment is worth its cost for this claim?** AI may help gather evidence or challenge a conclusion; a human can inspect consequential uncertainties and the quality and relevance of sources. The appropriate amount of checking depends on stakes, error costs, and evidence about the workflow—not a blanket rule to verify everything or trust everything.

## Related concepts

- [Check evidence quality](../cognitive_patterns/check_evidence_quality.md) — connect a claim to its actual evidence and limits.
- [Critical thinking when agents do the work](2026-11-03_article_addy-osmani_critical-thinking-when-agents-do-the-work.md) — preserve judgment and adapt verification to stakes.
- [Ironies of Automation](1983-01-01_paper_lisanne-bainbridge_ironies-of-automation.md) — a distinct warning about unsupported human supervision in industrial control, not evidence that human checking always beats AI.

## Sources

- [Mollick’s post and three images](https://x.com/emollick/status/2119140502746308674) [post].
- [OpenAI, BrowseComp](https://openai.com/index/browsecomp/) [browsecomp].
- [Huang et al., DeepFact, ACL 2026](https://aclanthology.org/2026.acl-long.1586/) [deepfact].
