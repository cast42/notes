---
title: "Papero and Xberg compared on PDF Markdown extraction"
date: 2026-10-02
type: investigation
topics:
  - rag
tags:
  - pdf-extraction
  - document-parsing
  - rag-ingestion
  - layout-analysis
description: "A bounded comparison showing similar prose extraction but different treatment of a diagram in a born-digital book PDF."
sources:
  - id: papero
    resource: "https://github.com/beatrizalmeidaf/papero-pdf-text-extractor"
  - id: xberg
    resource: "https://github.com/xberg-io/xberg"
generated:
  by: "process:codex"
  at: "2026-10-02T07:31:10+02:00"
---

# Papero and Xberg compared on PDF Markdown extraction

## TL;DR

On four selected pages from the user-supplied *Engineering a Safer World* PDF, Papero 3.1.0 and Xberg 1.3.2 produced nearly identical Markdown for ordinary prose. They differed on a systems diagram: Papero emitted a figure with imperfectly ordered labels, while Xberg represented the diagram as two false-positive Markdown tables. Neither preserved the arrows or full relationships. For this PDF, Papero is the safer Markdown starting point, but diagrams should remain available as images when their structure matters.

## Method

- Sample: PDF pages 32, 33, 63, and 115 (printed pages 11, 12, 42, and 94), chosen for prose and a labeled systems diagram.
- Both tools received identical one-page PDF slices. Papero ran with `tika=False`, `ocr="off"`; Xberg used `output_format="markdown"`, `disable_ocr=True`, `use_cache=False`. The document has a usable text layer, so OCR was disabled to compare text/layout extraction rather than OCR engines.
- Runs used isolated `uv run --with ...` environments; the notes repository's dependency files were not changed. Neither run downloaded LLM or OCR model weights.

## Results

- On prose pages 32, 33, and 115, output lengths differed by less than 1% per page and spot inspection found no meaningful content difference. Heading markup differed: Papero generally used Markdown headings while Xberg often bolded the page heading.
- Page 63 contains Figure 2.9, a directed diagram connecting the designer's, operator's, and actual-system mental models. Papero identified one figure and retained its caption; its extracted labels were still partly reordered or conflated. Xberg detected two tables, placing diagram labels into table cells and mixing in surrounding annotations. This representation is misleading for downstream text retrieval even though the Xberg result reported `quality_score=1.0`.
- The diagram's arrows and semantics were not recovered by either Markdown output. Preserve or separately index the source image when those relationships matter.
- This was a four-page spot check, not a general accuracy or speed benchmark. It covered born-digital prose and one diagram—not scans, OCR, dense tables, or the whole book. Xberg's reported quality score is an internal signal, not an independent fidelity measure.

## Takeaway for RAG ingestion

For plain prose indexing, these runs do not justify choosing one tool on extraction quality alone. For the tested diagram, Papero's figure classification is preferable to Xberg's false tables, but neither text output carries enough structure to stand in for the visual. Keep extraction separate from embedding/vector indexing; this extraction path did not require llama.cpp.

## Sources

- [Papero PDF text extractor](https://github.com/beatrizalmeidaf/papero-pdf-text-extractor)
- [Xberg (successor/rebrand of Kreuzberg)](https://github.com/xberg-io/xberg)
