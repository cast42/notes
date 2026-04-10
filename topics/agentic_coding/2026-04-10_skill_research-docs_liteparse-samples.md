---
title: "research-docs skill in liteparse_samples"
date: 2026-04-10
type: note
topics:
  - agentic_coding
tags: []
---

# research-docs skill in liteparse_samples

## TL;DR
- The `research_docs` sample in `jerryjliu/liteparse_samples` is a Claude-style skill for document Q&A with visual citations.
- It parses documents with LiteParse, has the model answer from parsed text, then generates an HTML report with cited page images and bounding-box highlights.
- The implementation pattern is useful as a reference for agent workflows that need auditable answers from source documents.

## Key takeaways / what stuck
- The skill is named `research-docs` and expects two arguments: a data directory plus a question.
- It uses a bundled Python script, `generate_report.py`, as the single execution path instead of calling LiteParse CLI commands directly.
- The workflow is parse first, read parsed JSON, write an answer JSON with exact-quote citations, then render an HTML report.
- Citation quality is treated as critical: quotes must be exact substrings from parsed text so bounding-box lookup works reliably.
- The generated report is self-contained and includes answer text, citation cards, page screenshots, and highlighted source regions.

## Details

### Repo
- GitHub: <https://github.com/jerryjliu/liteparse_samples>
- Relevant folder: `research_docs/`

### What the skill does
The sample skill is designed for question answering over a directory of documents, with visual verification baked into the output. Instead of only returning a text answer, it produces an HTML report that shows where each cited claim came from on the original page.

### Main workflow shape
1. Parse supported files in a directory into structured JSON.
2. Read the parsed output and reason over the extracted text.
3. Write a machine-readable answer file with:
   - the question
   - an answer in markdown with inline citation markers
   - a citations array containing file, page, exact quote, and relevance
4. Re-run the Python script in report mode to render the final HTML report.

### Constraints and implementation details
- The skill says to always use the bundled Python script and not invoke `lit` or `liteparse` CLI commands directly.
- It supports LiteParse-friendly files like PDFs, Office docs, spreadsheets, and images, plus plaintext formats such as `.txt`, `.md`, and `.rst`.
- It warns that quotes should be short and exact, and should not span table columns, because highlight matching depends on exact string lookup.
- Plaintext citations use `page: 0`, while paginated documents use 1-indexed page numbers.

### Why it is interesting
This is a strong reference design for “research with receipts.” It separates:
- extraction
- reasoning
- citation serialization
- visual rendering

That makes it easier to audit model claims and also suggests a reusable pattern for other agent/reporting skills.

## Links / sources
- <https://github.com/jerryjliu/liteparse_samples>
- <https://github.com/jerryjliu/liteparse_samples/tree/main/research_docs>
