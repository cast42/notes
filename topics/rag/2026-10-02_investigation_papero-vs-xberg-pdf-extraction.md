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
description: "A bounded comparison of Papero and Xberg on prose, a diagram, multi-column academic pages, tables, and equations in born-digital PDFs."
sources:
  - id: papero
    resource: "https://github.com/beatrizalmeidaf/papero-pdf-text-extractor"
  - id: xberg
    resource: "https://github.com/xberg-io/xberg"
  - id: tesseract
    resource: "https://github.com/tesseract-ocr/tesseract"
  - id: attention_is_all_you_need
    resource: "https://arxiv.org/abs/1706.03762"
generated:
  by: "process:codex"
  at: "2026-10-02T07:53:42+02:00"
---

# Papero and Xberg compared on PDF Markdown extraction

## TL;DR

On four selected pages from the user-supplied *Engineering a Safer World* PDF, Papero 3.1.0 and Xberg 1.3.2 produced nearly identical Markdown for ordinary prose. They differed on a systems diagram: Papero emitted a figure with imperfectly ordered labels, while Xberg represented the diagram as two false-positive Markdown tables. Neither preserved the arrows or full relationships. For this PDF, Papero is the safer Markdown starting point, but diagrams should remain available as images when their structure matters.

## Method

- Sample: PDF pages 32, 33, 63, and 115 (printed pages 11, 12, 42, and 94), chosen for prose and a labeled systems diagram.
- Both tools received identical one-page PDF slices. Papero ran with `tika=False`, `ocr="off"`; Xberg used `output_format="markdown"`, `disable_ocr=True`, `use_cache=False`. The document has a usable text layer, so OCR was disabled to compare text/layout extraction rather than OCR engines.
- Runs used isolated `uv run --with ...` environments; the notes repository's dependency files were not changed. Neither run downloaded LLM or OCR model weights.

## Papero implementation and CLI

Papero combines a geometry/layout engine built on PDFium with Apache Tika. PDFium reads glyphs and their positions to reconstruct reading order, tables, formulas, and figures; Tika adds metadata, tagged-PDF headings, OCR, and support for other formats. The OCR path uses the open-source Tesseract engine, which runs on CPU with language traineddata. Papero's Docker Compose setup includes Tika and Tesseract. Its main layout reconstruction requires no heavyweight ML/PyTorch model, but Tesseract OCR is a separate optional path. Papero is MIT licensed. ([architecture and setup](https://github.com/beatrizalmeidaf/papero-pdf-text-extractor#how-it-works), [license](https://github.com/beatrizalmeidaf/papero-pdf-text-extractor/blob/main/LICENSE), [Tesseract](https://github.com/tesseract-ocr/tesseract))

For text-layer PDFs, run the CLI without Java/Tika or OCR:

```sh
uv run --with papero-extract papero-extract extract paper.pdf \
  -p 1-3,5 --no-tika --ocr off -o paper.md
```

This command was checked against the supplied PDF with page 63. For scanned PDFs, use the Tika/Tesseract-backed setup instead; `uv --with` installs Papero's Python CLI, not those external services.

## Results

- On prose pages 32, 33, and 115, output lengths differed by less than 1% per page and spot inspection found no meaningful content difference. Heading markup differed: Papero generally used Markdown headings while Xberg often bolded the page heading.
- Page 63 contains Figure 2.9, a directed diagram connecting the designer's, operator's, and actual-system mental models. Papero identified one figure and retained its caption; its extracted labels were still partly reordered or conflated. Xberg detected two tables, placing diagram labels into table cells and mixing in surrounding annotations. This representation is misleading for downstream text retrieval even though the Xberg result reported `quality_score=1.0`.
- The diagram's arrows and semantics were not recovered by either Markdown output. Preserve or separately index the source image when those relationships matter.
- This was a four-page spot check, not a general accuracy or speed benchmark. It covered born-digital prose and one diagram—not scans, OCR, dense tables, or the whole book. Xberg's reported quality score is an internal signal, not an independent fidelity measure.

## Multi-column paper test

To exercise a denser academic layout, I used pages 6–8 of Vaswani et al., [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762). These pages use a two-column layout and include Table 1 (a four-column comparison), Table 2 (nested column headings and grouped BLEU/training-cost values), and displayed equations. Both tools received the same three-page PDF slice; OCR was disabled because the paper is born-digital and has a text layer.

Recreate the slice from the public PDF with `qpdf`, then run Papero and Xberg:

```sh
curl -L https://arxiv.org/pdf/1706.03762 -o attention.pdf
qpdf --empty --pages attention.pdf 6-8 -- pages-6-8.pdf

uv run --with papero-extract papero-extract extract pages-6-8.pdf \
  --no-tika --ocr off --page-breaks -o papero.md

xberg extract pages-6-8.pdf --no-config-discovery \
  --content-format markdown --disable-ocr true --no-cache true \
  --page-markers true -f json > xberg.json
```

The Papero command used Papero 3.1.0 via its `uv` CLI. Xberg was v1.3.2's official macOS CLI release binary (the `xberg` Python package does not provide this CLI entry point); it emitted Markdown in a JSON result, so its `content` field is the Markdown to compare. Runs were native/text-layer extraction, not OCR. Papero reported 2 tables and 5 formulas; Xberg reported 2 tables and `quality_score=1.0`.

- **Table 1:** Papero preserved the four semantic columns and aligned the rows. Xberg generated a spurious fifth, blank column and shifted some maximum-path-length values into it.
- **Table 2:** Both struggled with its grouped headers. Papero kept a recognizable table, but combined paired EN-DE/EN-FR scores and FLOP values into single cells, losing which value belongs to which subcolumn. Xberg was worse: it treated header/caption fragments as table rows and merged or shifted the paired values across cells.
- **Equations:** Papero represented equations as display-math blocks, but joined the two positional-encoding equations on one line and did not preserve all subscript formatting cleanly. Xberg split the equation into prose-like fragments and lost the equation's clear symbolic structure.
- **Surrounding prose:** Both returned readable two-column body text in this small sample, though neither output should be treated as a proof of perfect reading order or content fidelity.

For this particular PDF sample, Papero is the better starting point for tables and formulas, but its Table 2 still needs checking against the PDF. Xberg's perfect self-reported quality score did not catch the visible structural errors. This is one paper and three pages—not a broad benchmark—and the extraction times and scores are not directly comparable quality measures.

## Takeaway for RAG ingestion

For plain prose indexing, these runs do not justify choosing one tool on extraction quality alone. For the tested diagram, Papero's figure classification is preferable to Xberg's false tables, but neither text output carries enough structure to stand in for the visual. Keep extraction separate from embedding/vector indexing; this extraction path did not require llama.cpp.

## Sources

- [Papero PDF text extractor](https://github.com/beatrizalmeidaf/papero-pdf-text-extractor)
- [Xberg (successor/rebrand of Kreuzberg)](https://github.com/xberg-io/xberg)
