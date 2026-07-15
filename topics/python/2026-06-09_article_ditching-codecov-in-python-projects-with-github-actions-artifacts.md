---
type: article
source_url: "https://hynek.me/articles/ditch-codecov-python/"
canonical_url: "https://hynek.me/articles/ditch-codecov-python"
title: Ditching Codecov in Python projects with GitHub Actions artifacts
author: Hynek Schlawack
created_at: 2026-06-09
topics: [python]
tags: []
---

# Ditching Codecov in Python projects with GitHub Actions artifacts

*Hynek Schlawack*

## TL;DR

- Hynek argues that Python projects on GitHub Actions do not need Codecov to enforce coverage across a build matrix, and that removing it simplifies CI and avoids a flaky dependency.
- The replacement pattern is to upload raw coverage files from each matrix job as GitHub Actions artifacts, then use a final coverage job to download, combine, report, and fail the build using Coverage.py itself.
- The broader lesson is that built-in tools already cover the needed workflow: artifacts provide cross-job handoff, and Coverage.py already supports fail-under enforcement and reporting.

## Highlights

- "Not only did I get rid of a flaky dependency, it also simplified my workflow."
- Use actions/upload-artifact in each coverage-producing matrix job to save .coverage.* files.
- Use a final coverage job with if: always() and coverage combine to aggregate matrix results.
- Write coverage report --format=markdown to $GITHUB_STEP_SUMMARY for inline GitHub Actions reporting.
- Only upload the HTML coverage artifact when the fail-under check fails.

## Links

- Permalink: [https://hynek.me/articles/ditch-codecov-python](https://hynek.me/articles/ditch-codecov-python)
- [https://hynek.me/articles/ditch-codecov-python/](https://hynek.me/articles/ditch-codecov-python/)
- [https://coverage.readthedocs.io/](https://coverage.readthedocs.io/)
- [https://github.com/hynek/structlog/blob/main/.github/workflows/ci.yml](https://github.com/hynek/structlog/blob/main/.github/workflows/ci.yml)
- [https://github.com/hynek/setup-cached-uv](https://github.com/hynek/setup-cached-uv)

## Raw

- Raw text: [topics/python/raw/2026-06-09_article_ditching-codecov-in-python-projects-with-github-actions-artifacts.raw.md](https://github.com/cast42/notes/blob/main/topics/python/raw/2026-06-09_article_ditching-codecov-in-python-projects-with-github-actions-artifacts.raw.md)
- Extractor: summarize+web-fetch

## My notes
-
