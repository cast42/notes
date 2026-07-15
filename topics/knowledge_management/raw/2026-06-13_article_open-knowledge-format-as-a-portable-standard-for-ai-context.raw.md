---
type: article
source_url: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/"
canonical_url: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing"
title: Open Knowledge Format as a portable standard for AI context
author: Google Cloud
created_at: 2026-06-13
topics: [knowledge_management]
content_hash: 43b72ef3044b84eda28af5d7eb9bb89ea0b4eaca986c063d8d1505a42cebfb83
extracted_at: "2026-06-13T07:57:44"
extractor: summarize+web-fetch
date: 2026-06-13
timestamp: 2026-06-13
resource: "https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing"
---

# Raw content

Source: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing


URL: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
Title: How the Open Knowledge Format can improve data sharing
Author: Google Cloud

Summarize output:
Google is introducing the Open Knowledge Format, or OKF, as an open standard for packaging the internal context that AI agents need but usually struggle to access cleanly. The article's core claim is that the problem is not a lack of knowledge systems, but the lack of a portable format that can move across tools, teams, and vendors. OKF v0.1 is deliberately simple: a directory of Markdown files with YAML frontmatter, where each file represents a concept such as a table, dataset, metric, runbook, or API, and normal Markdown links connect them into a graph. The goal is to standardize the increasingly common "LLM wiki" pattern without introducing a new runtime, SDK, or proprietary platform.
*"What's missing is a format, not another service"*
The motivation is that enterprises store the context models need across many incompatible surfaces: metadata catalogs, wikis, shared drives, code comments, notebooks, and undocumented knowledge in employees' heads. When an agent needs to answer something practical like how to compute a metric or join two systems, it has to reconstruct the answer from scattered sources and vendor-specific schemas. OKF is meant to solve that by making knowledge human-readable, agent-parseable, version-controllable, and portable between producers and consumers. The design is intentionally minimal: the only required field is `type`, while other fields like title, description, resource, tags, and timestamp live in frontmatter, and the rest remains plain Markdown body text.
Google is shipping the spec with reference implementations to make it concrete rather than abstract. These include an enrichment agent that walks a BigQuery dataset and drafts OKF documents for tables and views, a static HTML visualizer that turns any OKF bundle into an interactive graph, and three sample bundles for GA4 e-commerce, Stack Overflow, and Bitcoin public datasets. Google also says its Knowledge Catalog can now ingest OKF and serve it to agents. The broader argument is that the value of a knowledge format grows through adoption and interoperability, so the real contribution is not the tools but the shared contract that lets different systems exchange curated AI context without translation.
*"The format itself is the contribution."*


Additional article details captured via web fetch:
- OKF v0.1 is presented as a vendor-neutral format for packaging AI-relevant knowledge as markdown files with YAML frontmatter.
- The design is intentionally minimal: one file per concept, required `type` field, optional fields like title, description, resource, tags, and timestamp.
- Concepts can link with normal markdown links, with optional index.md and log.md files for navigation and change history.
- Google is shipping reference implementations including a BigQuery enrichment agent, a static HTML visualizer, and sample bundles.
- The main pitch is interoperability: a format for knowledge exchange, not another hosted service or SDK.
