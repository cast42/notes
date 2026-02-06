---
title: "Microsoft and Software Survival (Stratechery)"
date: 2026-02-06
type: note
topics:
  - agentic_coding
tags:
  - microsoft
  - economy
  - copilot
  - saas
  - agents
people:
  - Ben Thompson
  - Ryan Singer
source:
  kind: article
  url: https://stratechery.com/2026/microsoft-and-software-survival/
---

# Microsoft and Software Survival (Stratechery)

## TL;DR
Ben Thompson argues Microsoft has moved from “big AI winner” to “under pressure” because AI changes software economics in two directions at once:
1) **code gets cheaper** (AI writes more of it), which increases competition, and
2) **agents** threaten the *per-seat* licensing model as work becomes less tied to individual human users.

Microsoft’s immediate issue: scarce GPU capacity and the choice to allocate it to its own Copilot products/R&D rather than maximizing Azure growth.

## Takeaways
- **AI-written code benefits software vendors first** (they can ship/iterate faster), but it also lets *every vendor* do the same → competition intensifies.
- The bigger risk for SaaS is not “customers will build everything themselves” but “**software abundance** makes the SaaS pie harder to grow; vendors start fighting for it.”
- **Agents** shift the unit of value away from “a human seat” toward “work done”; per-seat pricing becomes fragile.
- Microsoft’s natural agent advantage is **identity + artifacts** (Active Directory/M365 data) → “Work IQ” as the substrate.
- Cloud is becoming a **token foundry** business; hyperscalers will prioritize their own products first, pushing some demand toward more neutral capacity providers.

## Details

### Why code getting cheaper doesn’t mean software is free
Thompson is skeptical that businesses will stop buying software just because AI can write code:
- most companies want to focus on core competency
- shipping an app is the start of a long tail: maintenance, security patches, integrations, compliance, support

### The real competitive shock: abundance
Analogy to media:
- when distribution went to ~0, publishing became “infinite” → competition exploded
- in software, the input changing is the **cost of code** trending toward ~0 → everyone can build more, so everyone attacks adjacencies

### Microsoft’s “Work IQ” and the per-seat problem
- Work IQ is framed as reasoning over people/roles/artifacts/communications/history **inside an org security boundary**.
- But if agents reduce the number of *human identities* doing the work, Microsoft’s per-seat model (M365) is pressured.

### GPU allocation and Azure’s miss
Thompson interprets Microsoft’s choice to allocate scarce GPU capacity to:
- first-party Copilot products (M365, GitHub, etc.)
- R&D / building more software with AI
…as strategically rational, even if it hurts near-term Azure growth.

## Links
- Stratechery: <https://stratechery.com/2026/microsoft-and-software-survival/>
- X post (Ryan Singer pointing to the article): <https://x.com/rjs/status/2019719077866901528>
