---
title: "Boris Cherny's steps of AI adoption"
date: 2026-07-17
timestamp: 2026-07-17T01:32:24Z
type: tweet
topics:
  - ai_adoption
tags:
  - organizational-adoption
  - agent-orchestration
  - verification-loops
  - guardrails
  - bottleneck-removal
author: Boris Cherny
handle: bcherny
source_url: "https://x.com/i/status/2077929379661844559"
canonical_url: "https://x.com/bcherny/status/2077929379661844559"
resource: "https://x.com/bcherny/status/2077929379661844559"
description: "Boris Cherny frames AI adoption as a progression from gated access to intent-driven agent fleets, where each advance depends on removing a new bottleneck and installing stronger verification and governance loops."
---

# Boris Cherny's steps of AI adoption

## TL;DR

Boris Cherny describes organizational AI adoption as a progression from restricted access, through supervised pairing and parallel orchestration, to increasingly autonomous agent systems. The durable idea is not the agent counts but the changing constraint: access, human attention, review throughput, organizational context and trust, then selecting work that is safe and valuable to automate at scale.

His follow-up supplies the most important qualification: there is no single correct route. More tokens alone do not move a team forward; progress comes from breaking the next bottleneck while building the guardrails required for the next level of autonomy.

## The adoption ladder

### 0. Gated — no agents

AI access is slow, restricted, or limited to weaker models. Security, procurement, authentication, MCP governance, and deployment approvals dominate. The organization optimizes token cost before it has established useful outcomes.

**Move forward by:** aligning executives, buyers, security, and technical leaders around a secure launch path.

### 1. Assisted — one person paired with roughly one agent

The engineer runs one session at a time and reviews nearly every response and edit. Work accelerates, but it remains synchronous because low trust keeps the human watching the agent.

**Bottleneck:** human attention and the need to inspect everything.

**Move forward by:** running multiple agents, building trusted self-verification with tests, builds, linting, and end-to-end checks, reducing routine permission prompts, and automating code review.

### 2. Parallel — one orchestrator with roughly ten agents

An engineer coordinates several isolated agents at once. Agents test and review their own work before presenting final diffs, so the human reviews outcomes instead of keystrokes.

**Bottleneck:** review and steering throughput across many concurrent streams.

**Move forward by:** giving agents access to code, documentation, and discussions; increasing cross-team agency and review speed; turning work into loops and routines; and allowing agents to launch other agents.

### 3. Supervised autonomy — manager of an agent tree of roughly one hundred

Agents write nearly all code and increasingly initiate recurring maintenance and cleanup. When work fails, the question shifts from whether the agent read the code to which context or verification capability was missing.

**Bottleneck:** trust, decision throughput, and efficient use of rapidly growing compute. Scaling the tree before the verification loop earns trust is the central trap.

**Move forward by:** closing domain-specific loops for repeatable work such as migrations, fuzzing, feature building, and feedback remediation.

### 4. AI-native — intent-driven fleets of roughly one thousand or more agents

Most work is initiated by agents. People steer by intent and monitor exceptions rather than manually dispatching every task.

**Bottleneck:** finding work worth automating at scale and applying guardrails appropriate to each class of work.

## What the framework really measures

The numbers are illustrative, not maturity targets. Each stage changes the scarce resource:

1. **Access** — can people use capable models in a governed environment?
2. **Attention** — can the agent verify enough work that the person can look away?
3. **Review capacity** — can a person judge several completed streams without becoming the queue?
4. **Organizational trust and context** — can agents retrieve what they need, work across ownership boundaries, and initiate bounded tasks?
5. **Portfolio judgment** — which loops deserve full automation, and which controls must remain?

This makes adoption a systems problem rather than a licensing problem. Buying more tokens increases potential throughput, but it can worsen the current bottleneck when verification, review, context, or governance has not caught up.

## Boris's reply

Boris says teams and companies need not follow one identical route. At every stage, token availability is insufficient by itself: the team must identify and remove the next bottleneck and construct the next layer of guardrails.

That reply turns the table from a prescriptive ladder into a diagnostic model. A useful adoption plan therefore begins by locating the current constraint, not by copying the tooling or agent count of a more advanced team.

## Reasoning lens

Using [Analyze Capability Accumulation](../cognitive_patterns/analyze_capability_accumulation.md), the stages describe a compounding organizational capability: action generates failures, failures reveal missing context or checks, and teams encode those lessons into verification, skills, policies, and routines. Progress compounds only when those improvements shorten the feedback loop and allow more work to proceed without consuming proportional human attention.

## Sources

- [Boris Cherny's post](https://x.com/bcherny/status/2077929379661844559)
- [Steps of AI Adoption artifact](https://claude.ai/code/artifact/bfdfaef9-bc62-4dfe-ba9e-c58a26c9accf)
- [Boris's follow-up reply](https://x.com/bcherny/status/2077929386146169269)
- [Raw source capture](raw/2026-07-17_tweet_boris-cherny_steps-of-ai-adoption.raw.md)
