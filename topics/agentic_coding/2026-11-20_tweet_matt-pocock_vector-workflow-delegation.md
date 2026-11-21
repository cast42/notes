---
title: "VECTOR: mapping a workflow onto an agent"
date: 2026-11-20
type: tweet
author: Matt Pocock
topics:
  - agentic_coding
tags:
  - agent-workflows
  - delegation
  - verification
  - agent-memory
resource: "https://x.com/mattpocockuk/status/2123810087361810663"
description: "A six-question method for redesigning existing knowledge work as a verifiable human–agent workflow."
sources:
  - id: pocock-post
    resource: "https://x.com/mattpocockuk/status/2123810087361810663"
generated:
  by: openai/gpt-6
  at: 2026-11-21T09:50:00+01:00
---

# VECTOR: mapping a workflow onto an agent

## TL;DR

Matt Pocock proposes **VECTOR**, a six-question exercise to map an existing piece of knowledge work onto an AI agent. Start with how the outcome can be verified, then examine the current process, necessary context, delegated authority, workflow order, and what should be remembered. The result is a workflow map that makes human and agent responsibilities explicit.

## The six questions

The image in [Pocock's post](https://x.com/mattpocockuk/status/2123810087361810663) recommends choosing a real workflow that takes at least 20 minutes and addressing these in order:

1. **Verification:** How will we check the work was done?
2. **Existing process:** What happens today?
3. **Context:** What does the agent need to know or access?
4. **Trust:** Which actions can the agent be trusted to perform?
5. **Order:** How should the redesigned workflow be sequenced, including human–agent handoffs?
6. **Remember:** What should carry over between runs?

The map should specify the definition of done and its checks, the steps and their inputs, delegated authority, handoffs, and retained memory. Starting with verification makes the desired outcome and its evidence visible before redesigning the work.

## Practical interpretation

For a weekly notes summary, for example, define completion as a summary covering the qualifying notes with working links; map how notes are selected today; give the agent the repository, date range, and selection rules; set boundaries for edits and publication; then order collection, drafting, validation, and review. Record corrections to selection rules for the next run. This is an application of the questions, not an example from the post.

Verification and trust deserve distinct answers: a task can be easy to check yet still require approval before an external action. Likewise, memory should capture useful corrections without storing unnecessary sensitive material.

## Status and limits

On 20 November 2026, Pocock described `/vector` and supporting documentation as **forthcoming**. The post and accompanying image outline the method, not a validated study or a complete implementation. Its promised improvement in trust and workflow quality is a proposal, not an established outcome.

## Related concepts

- [Matt Pocock's skills repo workflow](2026-07-16_video_matt-pocock-s-skills-repo-end-to-end-workflow.md) — a related, coding-focused workflow for specification and review.
- [Skills v1.3 — implement-spec, pr, and retro](2026-10-05_youtube_matt-pocock_skills-v1-3.md) — includes learning from sessions to improve subsequent work.
- [Critical thinking when agents do the work](2026-11-03_article_addy-osmani_critical-thinking-when-agents-do-the-work.md) — retaining human judgment and meaningful checks.

## Source

- [Matt Pocock's post and VECTOR diagram](https://x.com/mattpocockuk/status/2123810087361810663), 20 November 2026.
- [Paraphrased source capture](raw/2026-11-20_tweet_matt-pocock_vector-workflow-delegation.raw.md).
