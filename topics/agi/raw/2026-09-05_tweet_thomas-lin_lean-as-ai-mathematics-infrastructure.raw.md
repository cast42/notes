---
title: "Research capture: Thomas Lin on Lean as infrastructure for AI-assisted mathematics"
date: 2026-09-05
type: source
topics:
  - agi
tags:
  - lean
  - autoformalization
  - formal-verification
resource: "https://x.com/7homaslin/status/2096283512810684418"
description: "Capture of Thomas Lin's recommendation of Anthropic's Fermat formalization report and Kevin Hartnett's history of Lean, with source-checked context."
sources:
  - id: x-post
    resource: "https://x.com/7homaslin/status/2096283512810684418"
    title: "Thomas Lin's post"
  - id: anthropic-flt
    resource: "https://www.anthropic.com/research/formalizing-fermats-last-theorem"
    title: "Anthropic: Formalizing Fermat's Last Theorem"
  - id: proof-in-code
    resource: "https://us.macmillan.com/books/9781250493941/theproofinthecode/"
    title: "Kevin Hartnett: The Proof in the Code"
generated:
  by: "process:codex"
  at: "2026-09-06T10:49:00+02:00"
---

# Research capture: Thomas Lin on Lean as infrastructure for AI-assisted mathematics

## X post

The [post](https://x.com/7homaslin/status/2096283512810684418) is by Thomas
Lin (@7homaslin), dated 5 September 2026. It says that Lean is mentioned in
nearly every paragraph of Anthropic's writeup about its formalization of
Fermat's Last Theorem. It calls Kevin Hartnett's new book *The Proof in the
Code* the first item on the recommended-reading list and strongly recommends
it.

The post links to Anthropic's report and to the book page at Quanta Books /
Macmillan. It is a recommendation and framing comment rather than a technical
claim of its own.

## Anthropic source

In [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem), Anthropic reports that Claude worked largely autonomously for 11 days to produce an end-to-end, computer-checked proof in Lean. The report says the system produced 13 million lines of Lean and proved 29,500 intermediate theorems used in the final proof.

Anthropic describes a multi-agent workflow with Prove2Me, an open collaborative
platform. The platform maintained a directed acyclic graph of theorem
statements, separated theorem statements from proofs for faster compilation,
and attached natural-language descriptions to theorem statements to support
search and reuse.

The report distinguishes this achievement from AI discovering a new proof of
FLT. The underlying theorem and mathematical strategy draw on existing work,
including Wiles's proof. The notable result is the rapid, large-scale
formalization and computer verification of the argument.

Anthropic's broader claim is that formalization may reduce the burden of
checking new mathematical work and make it easier to trust AI-generated
mathematics. It also says formalized proofs should complement, not replace,
human-understandable exposition.

## Book source

[The Proof in the Code](https://us.macmillan.com/books/9781250493941/theproofinthecode/)
is by journalist Kevin Hartnett. Its subtitle is *How a Truth Machine Is
Transforming Math and AI*. The publisher describes it as the story of Lean's
development, its adoption by mathematicians, and the wider movement toward
machine-checked mathematics.

## Interpretation

The combined signal is that Lean is becoming a possible trust, memory, and
coordination layer for AI-assisted mathematics. Models can search and generate
candidate proof steps, while Lean checks the formal derivation and libraries
preserve results in a composable format. This changes the role of AI in math
from producing plausible prose to operating inside an executable system of
definitions, lemmas, and verification.

That interpretation should not be inflated into “AI understands mathematics”
or “formalization solves mathematical trust.” A checked term establishes a
formal consequence of specified assumptions. Human judgment is still needed for
the choice of formalization, the mathematical strategy, the quality of the
library, and the explanatory connection to the informal problem.

## Source links

- [Thomas Lin's X post](https://x.com/7homaslin/status/2096283512810684418)
- [Anthropic: Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
- [Kevin Hartnett: The Proof in the Code](https://us.macmillan.com/books/9781250493941/theproofinthecode/)
