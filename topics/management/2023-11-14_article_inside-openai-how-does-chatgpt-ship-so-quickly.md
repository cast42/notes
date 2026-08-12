---
type: article
source_url: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship?hide_intro_popup=true"
canonical_url: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship"
resource: "https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship"
title: "Inside OpenAI: How Does ChatGPT Ship So Quickly?"
author: Gergely Orosz, interviewing Evan Morikawa
date: 2023-11-14
timestamp: 2023-11-14
created_at: 2023-11-14
topics: [management]
tags: [organizational-design, product-engineering, research-engineering, team-autonomy, shipping-velocity, openai]
description: OpenAI's early ChatGPT team increased delivery speed through startup-like autonomy, greenfield boundaries, embedded research, and a shared strategic mission.
---

# Inside OpenAI: How Does ChatGPT Ship So Quickly?

*Gergely Orosz, interviewing Evan Morikawa*

## TL;DR

- OpenAI gave ChatGPT the autonomy and greenfield infrastructure of an early-stage startup: a small colocated team, its own repository and cluster, and direct ownership of product iteration.
- The team was vertically integrated across design, engineering, research, and product (DERP). This mattered because many apparent product features—accuracy, concision, browsing, code execution, and multimodality—also required model research.
- A long-term mission acted as a prioritization filter: it helped the team decide both what to pursue and what not to build, reducing coordination and strategy drift.
- The interview attributes speed to organizational boundaries and feedback-loop design, not a single process trick: autonomous teams, research embedded in delivery, incremental releases, high talent density, and accumulated daily habits.

## Highlights

- The ChatGPT group was deliberately structured as a fractal startup inside the larger Applied organization.
- Fresh code and compute boundaries reduced inherited coupling while colocated, cross-functional ownership accelerated iteration toward product-market fit.
- Research was not a supplier handing models over a wall; researchers prototyped and ran experiments within the product loop.
- The accessible source preview ends partway through the long-term planning section; later sections named by the article are not present in the captured text.

## Organizational design behind the speed

The ChatGPT team was intentionally treated as a startup nested inside OpenAI's Applied organization. In summer 2022, a small group of applied engineers, designers, researchers, and leadership began iterating in one room. Unlike existing Applied products, which shared a codebase, cluster, and build pipelines, ChatGPT received a fresh repository and cluster. The aim was to preserve autonomy and the rapid learning cadence needed to find product–market fit.

As the product grew, the team remained vertically integrated. Engineering, product, design, and key researchers worked as one unit rather than as functional departments coordinating through handoffs. OpenAI had used a similar greenfield structure when launching its API; Evan Morikawa calls the repeatable pattern a **fractal startup**.

## Why research sat inside the product loop

The usual engineering–product–design trio became **design–engineering–research–product (DERP)**. This was more than adding another stakeholder: product questions such as making responses more concise or accurate, connecting ChatGPT to new data sources, or enabling browsing and code execution depended on research experiments and post-training techniques.

Embedding researchers avoided the classic model handoff from research to product. Researchers remained hands-on, wrote production-adjacent code, ran A/B experiments, and helped turn prototypes into shipped features. The relevant feedback loop therefore ran directly from user-facing behavior to product and research changes.

## Mission as a coordination mechanism

OpenAI's AGI mission served as a recurring decision filter. Asking which option moved the organization closer to that mission reportedly helped teams reject work as well as select it. The useful management lesson is not the mission's specific content, but that a sufficiently shared direction can reduce local prioritization debates and keep autonomous teams aligned.

## Transferable lessons

- Give a new product category a boundary it can control: team, repository, infrastructure, and release path.
- Keep the disciplines needed to solve the whole problem inside one feedback loop; don't mistake handoffs for specialization.
- Colocation and direct communication can be high-leverage during early ambiguity, though the article does not establish that they are universally required.
- Use a stable mission to constrain choices while allowing teams autonomy over implementation.
- Shipping velocity is an outcome of system design. Greenfield freedom helps early, but its future integration and operational costs still need deliberate management.

## Source limitation

This note summarizes the publicly accessible preview captured on 2026-08-12. The page is subscriber-only and the captured text stops during section 4. The article advertises later sections on uncoupled incremental releases, talent density, daily habits, and the road ahead; their detailed arguments are not available in the raw capture and are therefore not reconstructed here.

## Links

- Permalink: [https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship](https://newsletter.pragmaticengineer.com/p/inside-openai-how-does-chatgpt-ship)

## Raw

- [Captured public article preview](raw/2023-11-14_article_inside-openai-how-does-chatgpt-ship-so-quickly.raw.md)
- Extractor: Jina Reader public article preview
