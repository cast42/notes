---
title: "Modern Web Guidance: web-platform skills for coding agents"
date: 2026-11-25
type: tweet
topics:
  - agentic_coding
tags:
  - agent-skills
  - web-platform
  - browser-compatibility
  - accessibility
  - frontend-development
resource: "https://x.com/Saboo_Shubham_/status/2125490308788162704"
description: "A searchable collection of expert-curated web-platform guidance helps coding agents find modern APIs, browser support information and appropriate fallbacks."
sources:
  - resource: "https://x.com/Saboo_Shubham_/status/2125490308788162704"
  - resource: "https://github.com/GoogleChrome/modern-web-guidance"
---

# Modern Web Guidance: web-platform skills for coding agents

## TL;DR

Shubham Saboo highlights [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance), an Apache-2.0-licensed collection of web-development guidance for coding agents. Its aim is to make current platform techniques and compatibility information available at implementation time, rather than relying only on a model's potentially outdated training data.

## How it works

The skill instructs an agent to search for a specific UI or web-platform capability, retrieve relevant guides, apply them with appropriate fallbacks, and check the implementation against the guidance. For a broad modernization request it also offers a legacy-pattern scan; the skill notes that the scan covers only a subset of its guidance and that findings need review.

The repository covers CSS and layout, interaction and motion, native UI and forms, performance, accessibility and browser APIs. Examples include container queries, dialogs and popovers, view transitions and keyboard accessibility. The repository describes stewardship by Chrome, Edge, Firefox and MDN teams alongside the web community.

## Try it

The repository documents an interactive installer (`npx modern-web-guidance@latest install`) and commands to search or retrieve guides without installing the skill. Its README states Node.js 22 or later is required. These commands fetch and run a package: review and pin the version as appropriate for your environment. **Not installed or tested for this note.**

## Judgment and related notes

Compatibility data and native APIs help, but they do not replace checking the project's actual browser-support policy, accessibility and rendered behavior. The project's evaluation dashboard reports its own tests; this note does not independently validate the claimed improvement. Saboo suggests trying it with Gemini 4 Neon, but the repository describes a set of skills for coding agents, not an exclusively Gemini tool.

This complements the [Gemini frontend design skill](2026-11-24_tweet_philipp-schmid_gemini-frontend-design-skill.md): that skill emphasizes art direction and visual composition; Modern Web Guidance focuses on platform implementation, compatibility and fallbacks.

## Sources

- [Shubham Saboo's post](https://x.com/Saboo_Shubham_/status/2125490308788162704).
- [GitHub repository](https://github.com/GoogleChrome/modern-web-guidance) and [skill instructions](https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/SKILL.md).
