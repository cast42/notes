---
title: "Raw source: Boris Cherny's steps of AI adoption"
date: 2026-07-17
timestamp: 2026-07-17T01:32:24Z
type: source
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
extractor: fxtwitter+claude-artifact-browser+bird
description: "Source metadata and structured capture of Boris Cherny's post, linked adoption framework, and authored follow-up reply."
---

# Raw source

## Post metadata

- Author: Boris Cherny (`@bcherny`)
- Published: 2026-07-17 01:32:24 UTC
- Canonical URL: https://x.com/bcherny/status/2077929379661844559
- Linked artifact: https://claude.ai/code/artifact/bfdfaef9-bc62-4dfe-ba9e-c58a26c9accf
- Artifact title: *Steps of AI Adoption*
- Artifact author/date: Boris Cherny, 2026-07-16

## Main post

Boris says he repeatedly sees a mismatch inside engineering organizations: one person dramatically increases output with Claude while the rest of the organization has not adapted. He links a framework mapping the recurring stages he sees as teams adopt AI.

## Linked artifact structure

The document compares five states—numbered 0 through 4—across six dimensions:

- the adoption step and the human's role;
- approximate number of agents;
- the observable workflow;
- the current bottleneck;
- products that support that stage;
- required guardrails.

The states are:

1. `0: Gated` — zero agents; access and approval infrastructure are the constraint.
2. `1: Assisted` — a person pairs with about one closely supervised agent; attention is the constraint.
3. `2: Parallel` — one orchestrator coordinates about ten self-checking agents; review and steering are the constraint.
4. `3: Supervised autonomy` — a manager-of-managers oversees an agent tree of about one hundred; trust, decision throughput, and token efficiency are the constraints.
5. `4: AI-native` — a VP-like human steers one thousand or more agents by intent; identifying valuable automation and assigning suitable controls are the constraints.

The document recommends progressively stronger controls: identity and budget governance at the gated stage; centrally managed policy and observability during assisted use; automated quality, security checks, worktree isolation, and pre-approved safe commands during parallel work; then sandboxing, encoded standards, model selection, and tuned permission classifiers as autonomy grows.

## Boris-authored reply

- Published: 2026-07-17 01:32:26 UTC
- URL: https://x.com/bcherny/status/2077929386146169269

Boris clarifies that teams do not have to follow one universal path. Tokens alone cannot advance a team from one stage to the next; each transition requires breaking down the next bottlenecks and building the next guardrails.

## Extraction notes

- The public post and metadata were retrieved through FxTwitter.
- The linked Claude Artifact was read in a browser, including its stage, bottleneck, transition, product, and guardrail columns.
- X replies were fetched through the authenticated `bird` CLI. Of 107 replies returned for the conversation at capture time, one was authored by Boris Cherny; unrelated replies were excluded.
