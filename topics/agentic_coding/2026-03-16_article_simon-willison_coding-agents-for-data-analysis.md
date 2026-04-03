---
title: "Coding agents for data analysis (Simon Willison / NICAR 2026)"
date: 2026-03-16
type: note
topics:
  - agentic_coding
  - data_analysis
tags:
  - simon_willison
  - codex
  - claude_code
  - sqlite
  - datasette
source: "https://simonwillison.net/2026/Mar/16/coding-agents-for-data-analysis/"
---

## TL;DR
Simon Willison published the handout for his NICAR 2026 workshop on using coding agents for data analysis.

The material is aimed at data journalists, but the workflow generalizes well: use Claude Code or Codex to explore databases, clean data, generate visualizations, and scrape data, with Python/SQLite/Datasette as the working substrate.

## Key takeaways
- Workshop covers data exploration, cleaning, visualization, and scraping with coding agents.
- Simon used **GitHub Codespaces + OpenAI Codex** for easy participant setup and cost control.
- The stack was mostly **Python + SQLite + Datasette**.
- One highlight: using Claude Code to vibe-code interactive visualizations directly into a served folder.
- The handout is designed to stand alone even for people who didn’t attend.

## Summary
The post links to a full workshop handout from NICAR 2026, where Simon Willison taught a three-hour session on how coding agents can support real data-analysis workflows. Rather than treating agents as a novelty, the workshop frames them as practical tools for asking questions against databases, cleaning messy data, creating visualizations, and scraping additional inputs.

A useful implementation detail is the delivery mechanism: GitHub Codespaces plus budget-restricted Codex access, which made the workshop easy to distribute and control. The examples were grounded in approachable tools—Python, SQLite, and Datasette—showing how agent workflows can plug into familiar data stacks rather than requiring a brand-new environment.

The visualizations example is especially notable: Claude Code was used to generate interactive visualizations directly into a folder served by Datasette, demonstrating how agents can move beyond analysis into output production. The broader message is that agentic coding is becoming a usable workflow for exploratory data work, not just software engineering.

## Links
- Source: https://simonwillison.net/2026/Mar/16/coding-agents-for-data-analysis/
- Workshop handout: https://simonw.github.io/nicar-2026-coding-agents/
