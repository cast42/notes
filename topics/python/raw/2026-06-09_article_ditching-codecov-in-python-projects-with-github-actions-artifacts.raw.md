---
type: article
source_url: "https://hynek.me/articles/ditch-codecov-python/"
canonical_url: "https://hynek.me/articles/ditch-codecov-python"
title: Ditching Codecov in Python projects with GitHub Actions artifacts
author: Hynek Schlawack
created_at: 2026-06-09
topics: [python]
content_hash: 5ba12529a6040afa8a0869254b628f048966fe119357475bfcb6a1a7d053456b
extracted_at: "2026-06-09T14:31:02"
extractor: summarize+web-fetch
date: 2026-06-09
timestamp: 2026-06-09
tags:
  - test-coverage
  - github-actions
  - ci-artifacts
  - python-tooling
  - codecov
resource: "https://hynek.me/articles/ditch-codecov-python"
---

# Raw content

Source: https://hynek.me/articles/ditch-codecov-python


URL: https://hynek.me/articles/ditch-codecov-python/
Title: How to Ditch Codecov for Python Projects
Author: Hynek Schlawack

Summarize output:
Hynek Schlawack's argument is simple: Python projects on GitHub Actions do not need Codecov to enforce coverage across a build matrix, and removing it makes CI both more reliable and simpler. The problem he is solving is that coverage data is produced in separate matrix jobs, often across different Python versions and containers, so a single local `coverage combine` is not enough during the test jobs themselves. His fix is to use GitHub Actions artifacts as the handoff layer: each test job uploads its `.coverage.*` files, then a final coverage job downloads them all, combines them, generates reports, and fails the build if total coverage is below the chosen threshold.
*"I have lost any confidence"*
The workflow has two key steps. First, every matrix job that runs tests under coverage uploads its raw coverage files as an artifact, with a name that includes all relevant matrix dimensions. Second, a dedicated `coverage` job runs after the tests, downloads all those artifacts, runs `coverage combine`, writes both HTML and Markdown reports, adds the Markdown output to the GitHub Actions job summary, and finally enforces the threshold with `coverage report --fail-under=100`. He also uses `if: always()` so the coverage job still runs even if one test job fails, and only uploads the HTML artifact when the coverage check itself fails.
The broader point is that this approach replaces a flaky external dependency with built-in tools that already do the job. Coverage.py already knows how to enforce minimum coverage, and GitHub Actions artifacts already provide the cross-job storage layer needed for matrix builds. The result is fewer false failures, less time wasted restarting builds or inspecting stale status reports, and a cleaner CI setup. He uses `uv` to install Coverage.py because it is fast, but notes that plain `pip` works too, so the technique is not tied to any specific packaging workflow.
*"Not only did I get rid of a flaky dependency, it also simplified my workflow."*


Additional article details captured via web fetch:
- Uses GitHub Actions artifacts to collect .coverage.* files from matrix jobs.
- Final coverage job downloads artifacts, runs coverage combine, emits HTML and Markdown reports, and enforces fail-under in Coverage.py.
- Suggests using if: always() so coverage still runs even when one matrix job fails.
- Uses uv for installing Coverage.py, but notes pip works too.
- Motivating problem: unreliable Codecov status reporting and CI flakiness.
