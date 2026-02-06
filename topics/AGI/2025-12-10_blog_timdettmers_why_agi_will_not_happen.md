---
title: "Why AGI Will Not Happen (Tim Dettmers)"
date: 2025-12-10
type: note
topics:
  - AGI
tags:
  - skepticism
  - compute
  - hardware
  - scaling
  - robotics
people:
  - Tim Dettmers
source:
  kind: blog
  url: https://timdettmers.com/2025/12/10/why-agi-will-not-happen/
---

# Why AGI Will Not Happen (Tim Dettmers)

## TL;DR
Dettmers argues that common AGI/superintelligence narratives ignore a core constraint: **computation is physical**.
As hardware progress slows and scaling becomes exponentially more expensive, “just scale it” won’t get us to AGI as commonly imagined—especially if AGI implies **economically meaningful physical work** (robotics).

## Takeaways
- **Computation is physical**: data movement/memory hierarchies impose hard constraints; FLOPS without memory bandwidth are “useless FLOPS”.
- **Linear progress needs exponential resources**: diminishing returns bite both in physics (bigger experiments) and in “idea space” (incremental refinements).
- **GPU progress has largely plateaued** (in perf/$ since ~2018, per the author): remaining gains were “one-off” features (precision, tensor cores, HBM, etc.) and are near exhaustion.
- **Scaling isn’t magic when hardware tailwinds stop**: if compute efficiency stops improving, scaling becomes an exponential cost curve with a near-term ceiling.
- **AGI as ‘do all things humans do’ implies robotics**: physical-world data collection is expensive; many remaining robotics tasks are either already solved in controlled environments or not economically meaningful.
- **Superintelligence runaway is a category error**: recursive self-improvement is still bounded by resource constraints and diminishing returns; it fills gaps rather than extends an unbounded frontier.
- The future is framed as **economic diffusion** (usefulness + adoption) rather than a single winner racing to a mythical threshold.

## Details

### Computation is physical
Dettmers’ foundation is that AI architectures (especially transformers) are physical optimizations:
- compute is cheap relative to **memory movement**, which scales badly with distance
- cache hierarchy illustrates why bigger/farther memory is slower

### Hardware + scaling arguments
- Claims we’re near the end of meaningful GPU efficiency improvements.
- As a result, scaling laws still hold but become **financially/physically infeasible** quickly.
- Rack/datacenter optimizations matter, but are also bounded and may hit walls around 2026–2027 (author’s estimate).

### “AGI will never happen” definition used
A key move: define AGI as including **physical tasks** in the economy.
- Specialized robotics already dominates in factories (“dark factories”).
- Household/general robotics faces expensive data collection + high environment complexity.

### Meta-claim about discourse
The author is explicitly attacking “idea-space” thinking (Bay Area rationalist/EA narratives) as insufficiently grounded in physical/economic constraints.

## Links
- Post: <https://timdettmers.com/2025/12/10/why-agi-will-not-happen/>
