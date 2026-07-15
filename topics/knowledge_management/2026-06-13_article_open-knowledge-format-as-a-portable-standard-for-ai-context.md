---
type: article
source_url: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/"
canonical_url: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing"
title: Open Knowledge Format as a portable standard for AI context
description: Google's proposal for portable, agent-readable knowledge bundles.
resource: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/"
author: Google Cloud
created_at: 2026-06-13
topics: [knowledge_management]
tags:
  - knowledge-management
  - open-knowledge-format
  - portable-knowledge
  - agent-context
timestamp: 2026-06-13
date: 2026-06-13
---

# Open Knowledge Format as a portable standard for AI context

*Google Cloud*

## TL;DR

- Google introduces the Open Knowledge Format, or OKF, as a portable, vendor-neutral way to package the contextual knowledge AI agents need across tools, teams, and systems.
- The format is deliberately minimal: markdown files with YAML frontmatter, one file per concept, normal markdown links between concepts, and only a small interoperability surface.
- The article’s real thesis is that AI knowledge sharing needs a common format more than another proprietary service, so the value comes from portability and ecosystem adoption.

## Highlights

- "What's missing is a format, not another service."
- OKF formalizes the LLM-wiki pattern into a simple directory of markdown files with YAML frontmatter.
- Each concept is a file with a required type field and optional metadata like title, description, resource, tags, and timestamp.
- Google ships reference implementations including a BigQuery enrichment agent, a static HTML visualizer, and sample OKF bundles.
- The contribution is framed as the format itself, not a runtime, SDK, or hosted platform.

## Links

- Permalink: [https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
- [https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)
- [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Raw

- Raw text: [topics/knowledge_management/raw/2026-06-13_article_open-knowledge-format-as-a-portable-standard-for-ai-context.raw.md](https://github.com/cast42/notes/blob/main/topics/knowledge_management/raw/2026-06-13_article_open-knowledge-format-as-a-portable-standard-for-ai-context.raw.md)
- Extractor: summarize+web-fetch

## My notes
-
