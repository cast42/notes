---
type: tweet
date: 2026-07-15
timestamp: 2026-07-15
source_url: "https://x.com/i/status/2077498534128218116"
canonical_url: "https://x.com/0xwhrrari/status/2077498534128218116"
resource: "https://www.deeplearning.ai/courses/agent-skills-with-anthropic"
title: Agent Skills with Anthropic — DeepLearning.AI course
author: rari
handle: 0xwhrrari
created_at: 2026-07-15
topics: [agentic_coding]
tags:
  - agent-skills
  - progressive-disclosure
  - claude-code
  - model-context-protocol
  - subagents
description: "A practical course on packaging reusable agent expertise as skills and composing skills with tools, MCP, and subagents."
---

# Agent Skills with Anthropic — DeepLearning.AI course

*rari — @0xwhrrari*

## TL;DR

- Agent Skills package reusable instructions, scripts, reference material, and assets so agents can execute specialized workflows consistently.
- Progressive disclosure is the central design principle: keep only a skill's name and description in context, load `SKILL.md` when triggered, and retrieve supporting files or execute scripts only when needed.
- Skills encode *how to perform a workflow*; tools provide actions, MCP connects external systems and data, and subagents provide isolated context, permissions, and parallelism.
- The course demonstrates this stack across Claude.ai, the Claude API, Claude Code, and the Claude Agent SDK.

## Highlights

- Official title: Agent Skills with Anthropic
- Instructor: Elie Schoppik, Head of Technical Education at Anthropic
- 2h19m, 10 video lessons
- Includes a 24-minute lesson on Skills with Claude Code

## Course outline

- Why use skills: turning general-purpose agents into specialists on demand.
- Skill anatomy: `SKILL.md`, supporting files, and progressive disclosure.
- Boundaries: when to use a skill versus a tool, MCP server, or subagent.
- Practice: pre-built and custom skills for coding, data analysis, and research.
- Deployment surfaces: Claude.ai, Claude Code, Claude API, and Claude Agent SDK.

## Key takeaways from the video

### Start small and design for discovery

- A skill is a folder whose required entry point is `SKILL.md`; it may also contain scripts, detailed references, templates, and other assets.
- The description is operational metadata: it must clearly state what the skill does and when the agent should activate it.
- Begin with plain Markdown instructions. Add structure, scripts, and supporting files only after real usage reveals the need.
- Use the Skill Creator skill to scaffold and improve skills, then observe actual agent behaviour and iterate.

### Treat the context window as a shared scarce resource

- The course calls the context window a “public good”: unnecessary content consumes tokens and increases the risk of context degradation.
- At discovery time, agents see only skill names and descriptions. Full instructions load after selection; deeper files load only when referenced.
- Scripts can run outside the context window, returning only their useful outputs. This makes large skill libraries feasible without loading all their content up front.

### Compose the agent stack deliberately

- **Prompts** are one-off communication and do not scale well across teams.
- **Tools** are low-level capabilities—roughly the hammer, saw, and nails. Their definitions normally occupy context.
- **MCP** supplies external tools, data, and resources; a skill teaches the agent what workflow to execute with them.
- **Skills** bundle repeatable organizational knowledge and procedures into a portable, versionable unit.
- **Subagents** isolate context and permissions and enable parallel work. They can be equipped with specific skills, but do not automatically inherit the parent agent's skills.

### Coding example: separate implementation from review and testing

- In Claude Code, project knowledge that must always be present belongs in `CLAUDE.md`; task-specific procedures belong in skills.
- The demo creates reusable skills for adding CLI commands, reviewing code, and generating tests.
- A main agent implements features while a code-review subagent and test subagent work in separate contexts with narrowly scoped tools and skills.
- The result is a more context-efficient maker/checker workflow: specialized agents return findings and tests instead of filling the main thread with every intermediate step.

### API and SDK lessons

- API-based skills can be versioned, combined with built-in document skills, and used with code execution and file APIs to produce artifacts such as analyses, charts, and Word documents.
- The Agent SDK example combines a coordinating skill, parallel research subagents, web/repository tools, and a Notion MCP server to build and publish a learning guide.
- Tool permissions remain a security boundary. The demo explicitly notes that production systems need confirmation or policy controls around powerful actions such as shell execution and writes.

## Context

The X post describes this as an Andrew Ng course. More precisely, it is published by Andrew Ng's DeepLearning.AI, built with Anthropic, and taught by Elie Schoppik from Anthropic.

## Links

- Permalink: [https://x.com/0xwhrrari/status/2077498534128218116](https://x.com/0xwhrrari/status/2077498534128218116)
- [https://www.deeplearning.ai/courses/agent-skills-with-anthropic](https://www.deeplearning.ai/courses/agent-skills-with-anthropic)
- [https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Raw

- Raw text: [X post capture](raw/2026-07-15_tweet_agent-skills-with-anthropic-deeplearning-ai-course.raw.md)
- Full transcript: [timestamped machine transcript](raw/2026-07-15_video_agent-skills-with-anthropic-transcript.md)
- Extractors: FxTwitter and whisper.cpp (`base.en`)
