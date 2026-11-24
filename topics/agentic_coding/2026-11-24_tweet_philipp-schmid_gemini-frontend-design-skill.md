---
title: "Gemini frontend design skill for distinctive web pages"
date: 2026-11-24
type: tweet
topics:
  - agentic_coding
tags:
  - agent-skills
  - frontend-design
  - visual-design
  - gemini
  - antigravity
resource: "https://x.com/_philschmid/status/2125206633722601572"
description: "An experimental Gemini frontend-design skill uses subject-led art direction, disciplined typography, and visual review to counter generic agent-generated interfaces."
author: Philipp Schmid
sources:
  - resource: "https://x.com/_philschmid/status/2125206633722601572"
  - resource: "https://github.com/google-gemini/demolab/tree/main/skills/gemini-frontend-design"
---

# Gemini frontend design skill for distinctive web pages

## TL;DR

Philipp Schmid presents an experimental frontend skill for Gemini 4 Neon, designed to steer agent-built pages away from repetitive AI-generated layouts. The [skill in Google's demolab repository](https://github.com/google-gemini/demolab/tree/main/skills/gemini-frontend-design) is a reusable `SKILL.md` containing art-direction rules and a visual verification checklist.

## What the skill does

- **Start with the brief:** derive typography, palette, imagery and layout from the subject and audience; honor explicit style requests and existing design systems.
- **Choose the opening to fit the job:** where a hero is appropriate, favor strong, full-width type or imagery over the familiar half-text/half-image split. Blogs, dashboards, documentation and utilities should instead open directly into content or controls.
- **Constrain typography:** at most two font families and three body-size steps, with exceptions for hero display type and specified dense interfaces. Avoid text below 13 px above the fold.
- **Make color and imagery intentional:** avoid reflexive beige or dark-purple palettes unless the brief calls for them. Use generated or bespoke imagery where it earns its place, with sufficient contrast.
- **Reduce decorative clutter:** avoid noninteractive badges, eyebrow labels, nested cards and fake telemetry. Use plain hierarchy and space to group content.
- **Inspect the result:** review desktop and mobile renders, including below the fold; check overflow, collisions, contrast and reduced-motion behavior.

Schmid's example prompt requests an illustrated long-form field essay about Dolomites alpine wildflowers. The post calls the skill **experimental**; its strict preferences are design heuristics, not evidence of universally better usability. Its detailed rules allow exceptions, including user-requested styles and formats that should skip a hero.

## Antigravity context

The user identified this as a skill for Antigravity. The public post describes a Gemini frontend skill; the linked skill file specifies its design instructions but does not itself establish an Antigravity-specific installation procedure. No installation or compatibility test was performed.

## Sources

- [Philipp Schmid's post](https://x.com/_philschmid/status/2125206633722601572).
- [GitHub: google-gemini/demolab — gemini-frontend-design](https://github.com/google-gemini/demolab/tree/main/skills/gemini-frontend-design) (the repository link supplied in his reply).
- [Skill instructions](https://github.com/google-gemini/demolab/blob/main/skills/gemini-frontend-design/SKILL.md).
