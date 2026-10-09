---
type: "github_project"
source_url: "https://github.com/nashsu/llm_wiki"
canonical_url: "https://github.com/nashsu/llm_wiki"
title: "LLM Wiki: a desktop app for building a persistent knowledge wiki"
author: "nash_su"
date: "2026-10-09"
topics: ["agent_memory"]
tags:
  - llm-wiki
  - knowledge-graph
  - rag
  - personal-knowledge-management
resource: "https://github.com/nashsu/llm_wiki"
description: "A cross-platform desktop application that incrementally turns imported documents into a linked, source-traceable wiki for retrieval and agent use."
generated: {"by": "process:note-ingest", "at": "2026-10-09T16:59:12Z"}
sources:
  - id: repository-readme
    resource: "https://github.com/nashsu/llm_wiki#readme"
  - id: karpathy-llm-wiki-pattern
    resource: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
---

# LLM Wiki: a desktop app for building a persistent knowledge wiki

## TL;DR

[`nashsu/llm_wiki`](https://github.com/nashsu/llm_wiki) is a Tauri desktop implementation of Andrej Karpathy's LLM-Wiki pattern. It ingests documents into a persistent, interlinked Markdown wiki, then answers questions by retrieving from that evolving wiki rather than rebuilding context from scratch each time. It combines source-grounded summaries, graph expansion, optional vector search, review queues, and a local API/MCP integration. The project README describes the implementation; its quality and benchmark claims have not been independently tested here. The repository states that it is GPL-3.0 licensed.

## How it works

The project preserves the original pattern's three layers—immutable raw sources, an LLM-maintained wiki, and schema/rules—and its core `ingest`, `query`, and `lint` operations. Wiki pages use YAML frontmatter and `[[wikilinks]]`; `wiki/index.md` is the catalog and `wiki/log.md` records operations. The wiki can also be opened as an Obsidian vault.

Ingestion uses two LLM calls: first analyze the new source and its relationship to existing pages; then generate or update source summaries, entity/concept pages, links, indexes, and items for human review. The README describes SHA-256 incremental caching, a persistent/retryable queue, source traceability, and optional watching of the source folder. `purpose.md` supplies project-specific goals and questions to guide both ingestion and queries.

Queries combine tokenized search over wiki and raw sources, optional embedding search via LanceDB, and graph expansion from matching pages. The graph ranks links using direct links, shared sources, Adamic–Adar, and page-type affinity. Vector search is optional and disabled by default. The README reports recall improving from 58.2% to 71.4% when vector search is enabled; treat that as a project-reported benchmark, not an independently reproduced result.

## What makes this implementation notable

- It turns the wiki pattern into a cross-platform desktop application, with project settings, persistent chats, document import, graph visualization, linting, and an asynchronous human-review queue.
- It supports multiple document formats and optional local or cloud MinerU processing for complex PDFs.
- A local, token-protected HTTP API and bundled MCP server expose wiki search, file access, graph traversal, and source rescanning to external agents. The project also publishes a companion agent skill.
- The README says the app supports OpenAI, Anthropic, Google, Ollama, and custom model providers. This is a client application: model use depends on configuring a provider/model, and optional web search or cloud parsing has its own service requirements.

## Relation to other LLM-Wiki and memory work

This repository is a practical software implementation and extension of Karpathy's design pattern. It is distinct from the [WFM paper note](2026-09-23_tweet_wfm-wiki-foundation-model-for-complex-agentic-reasoning.md): WFM studies wiki-structured memory and reasoning as a research model, while this project builds a usable app and retrieval pipeline. It is also distinct from [Cognition's Agent Memory Repo and dreaming](2026-10-06_cognition_agent-memory-repo-and-dreaming.md), which focuses on git-backed agent memory and periodic consolidation rather than a document-ingestion desktop product.

The design choice worth evaluating is whether maintaining generated pages, links, and provenance makes repeat queries more useful than plain source search for a given corpus. The trade-off is extra ingest-time model work and the need to inspect/update generated knowledge; its review queue, source links, linting, and deletion cleanup are intended to help manage that maintenance burden.

## Links

- [Repository and current README](https://github.com/nashsu/llm_wiki)
- [Karpathy's original LLM-Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Companion agent skill](https://github.com/nashsu/llm_wiki_skill)
- [WFM: Wiki Foundation Model for Complex Agentic Reasoning](2026-09-23_tweet_wfm-wiki-foundation-model-for-complex-agentic-reasoning.md)
- [Agent Memory Repo and dreaming](2026-10-06_cognition_agent-memory-repo-and-dreaming.md)
