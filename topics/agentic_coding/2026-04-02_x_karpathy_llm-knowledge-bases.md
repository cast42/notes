---
title: "LLM Knowledge Bases (Andrej Karpathy)"
date: 2026-04-02
type: note
topics:
  - agentic_coding
tags:
  - x
  - andrej_karpathy
  - knowledge_management
  - obsidian
  - llm_workflow
source: "https://x.com/i/status/2039805659525644595"
---

## TL;DR
Karpathy describes a personal workflow where LLMs ingest raw research materials into a structured markdown wiki, maintain it, answer questions against it, and progressively enhance it.

The core idea is to shift token spend from writing code toward manipulating knowledge: collecting sources, compiling them into a wiki, querying that wiki, and feeding the outputs back into the system.

## Key takeaways
- Raw materials go into a `raw/` directory; an LLM incrementally compiles them into a markdown wiki.
- The wiki contains summaries, backlinks, concept pages, and cross-links.
- Obsidian acts as the frontend/IDE for viewing raw inputs, compiled wiki pages, and derived outputs.
- The LLM maintains the wiki directly; Karpathy rarely edits it by hand.
- Instead of terminal-only answers, the LLM emits markdown notes, slides, plots, and other files that are then viewed in Obsidian.
- Health-check passes can lint the wiki for inconsistency, missing data, and candidate article ideas.
- The workflow suggests room for a better product than a pile of custom scripts.

## Summary
Karpathy says a large share of his recent LLM usage has shifted away from coding and toward building personal research knowledge bases. His pattern starts with collecting source materials—articles, papers, repositories, datasets, and images—into a `raw/` folder. He then uses an LLM to incrementally compile these into a markdown wiki with summaries, backlinks, concept pages, and structured cross-references.

He uses Obsidian as the frontend for the whole system: raw materials, compiled wiki articles, and generated outputs all live in one place. The important twist is that the LLM writes and maintains the wiki; he rarely edits it himself. Once the wiki gets large enough (his example: ~100 articles and ~400K words), the agent can answer substantial research questions by exploring the wiki and its index-like summaries without requiring sophisticated RAG.

Outputs are not limited to plain text. Karpathy prefers having the agent render markdown documents, Marp slide decks, and matplotlib visualizations, which he then reviews in Obsidian. These outputs often get filed back into the wiki, meaning every query leaves a durable trace and improves the knowledge base for future work.

He also runs “health checks” over the wiki to detect inconsistent or missing information, pull in extra facts with web search, and propose new article candidates. Beyond that, he has started building auxiliary tools like a simple search engine over the wiki that both he and the LLM can use. Longer term, he sees a path from context-window-based systems toward synthetic data generation and fine-tuning, where the model begins to internalize more of the knowledge base in its weights.

## Useful workflow pieces mentioned
- Obsidian Web Clipper to convert web articles to markdown.
- Hotkey-driven local download of related images so the LLM can reference them.
- Obsidian plugins for alternate views (e.g. Marp for slides).
- CLI tools over the wiki for larger queries and maintenance tasks.

## Why this matters
This is a concrete pattern for research augmentation: not just “chat with documents,” but continuously compiling a living markdown knowledge system that the LLM can maintain, query, and extend.

## Links
- Post: https://x.com/i/status/2039805659525644595
