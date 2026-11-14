---
title: "How Complex Systems Fail"
date: 2000-04-21
type: article
author: "Richard I. Cook"
topics:
  - system_thinking
tags:
  - resilience-engineering
  - complex-systems
  - incident-investigation
  - safety
  - human-factors
resource: "https://gwern.net/doc/technology/2000-cook.pdf"
description: "Cook’s 18 propositions explain safety as an ongoing system accomplishment shaped by interacting faults, adaptation, expertise, and hindsight."
sources:
  - id: essay
    resource: "https://gwern.net/doc/technology/2000-cook.pdf"
    title: "How Complex Systems Fail, revision D"
  - id: post
    resource: "https://x.com/emollick/status/1761504126897103190"
    title: "Ethan Mollick on How Complex Systems Fail"
---

# How Complex Systems Fail

## TL;DR

Richard I. Cook’s short treatise argues that safety in hazardous, complex operations is an ongoing accomplishment, not a property of one reliable component. Multiple imperfect defenses and the adaptations of practitioners keep systems working; an accident can arise when vulnerabilities interact. Investigations should understand that context instead of stopping at a person or a single root cause.

The essay presents **18 propositions**, not a statistical study or a universal theorem about every complex system. The cited revision is dated 21 April 2000; the document also carries copyright dates from 1998–2000. [Ethan Mollick’s post](https://x.com/emollick/status/1761504126897103190) highlights it as a recurring reread.

## The 18 propositions, in brief

1. **Hazards are inherent:** useful activities such as healthcare, energy and transport involve hazards that must be managed.
2. **Defenses are layered:** technical, human, organizational and regulatory measures usually prevent those hazards from producing catastrophe.
3. **Failures interact:** Cook argues catastrophic accidents in well-defended systems emerge from combinations of faults rather than an isolated defect.
4. **Latent faults change:** minor-seeming weaknesses coexist, evolve and can become consequential in combination.
5. **Operations are often degraded:** systems keep working despite flaws, through redundancy and human adjustment.
6. **Catastrophic potential persists:** successful routine operation does not mean the potential for serious failure has vanished.
7. **A single root cause can mislead:** tracing an incident to one factor obscures interacting contributors and defenses.
8. **Hindsight distorts judgment:** once the outcome is known, warning signs and decisions can appear clearer than they were at the time.
9. **Practitioners have two roles:** they produce the desired service and simultaneously defend against failure.
10. **Actions involve uncertainty:** operational choices are made without knowing their outcomes; successful decisions also involve uncertainty.
11. **The sharp end resolves ambiguity:** frontline actions reconcile competing pressures for production, efficiency and safety.
12. **People adapt:** practitioners and frontline managers adjust resources, detect changes and create recovery routes as conditions evolve.
13. **Expertise evolves:** technological change, turnover and training continually alter the skills available to the system.
14. **Change creates new failure paths:** a fix or technology may eliminate familiar problems while introducing less visible ones.
15. **Narrow causal stories limit remedies:** reacting only to the final human action can miss conditions and make the system more complex.
16. **Safety is systemic:** it emerges from how people, equipment and organizations interact rather than residing in a single part.
17. **People create safety continuously:** everyday adjustments and practiced responses keep performance within tolerable limits.
18. **Experience with failure matters:** operators need calibrated ways to recognize hazards and system boundaries, including opportunities to learn from failures and near misses.

## Implications for incidents and automation

- Reconstruct what people knew, what pressures they faced, which safeguards were available, and how conditions combined—not just who made the last mistake.
- Study successful recoveries and ordinary work as well as accidents; ask what expertise and adaptations are keeping the system safe.
- Test changes for new interactions and preserve ways to detect degradation, retreat and recover. Simulations and exercises can build experience without deliberately creating unsafe conditions.
- For AI agents or automated operations, **an application of Cook’s argument**, not a claim tested in the essay: consider whether automation improves detection while weakening human visibility, practice or the ability to intervene.

**Boundary:** Cook’s absolute wording—especially that catastrophe always requires multiple failures—should be read as his systems-safety perspective, not as proof that a single identifiable defect can never precipitate a serious incident. Systemic context and actionable proximate causes can both matter.

## Related concepts

- [Engineering a Safer World](2012-01-13_book_nancy-leveson_engineering-a-safer-world.md) — systems safety and the constraints needed to control hazards.
- [Ironies of Automation](../agentic_coding/1983-01-01_paper_lisanne-bainbridge_ironies-of-automation.md) — automation can leave people responsible for interventions while reducing their practice and situational awareness.

## Sources

- [How Complex Systems Fail](https://how.complexsystems.fail/) — readable web edition.
- Richard I. Cook, [*How Complex Systems Fail*, revision D](https://gwern.net/doc/technology/2000-cook.pdf), 21 April 2000.
- [Ethan Mollick’s post](https://x.com/emollick/status/1761504126897103190), 24 February 2024; links to a [ResearchGate copy](https://www.researchgate.net/publication/228797158_How_complex_systems_fail).
