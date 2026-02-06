---
title: "LLM style tips (Python): guidelines for agentic coding"
date: 2026-02-06
type: note
topics:
  - agentic_coding
tags:
  - python
  - typing
  - pyright
  - testing
  - complexity
source:
  kind: blog
  url: https://honnibal.dev/blog/llm-style-tips
---

## TL;DR

LLMs make it easy to generate lots of code quickly — which increases the risk of **complexity creep** and **debugging spirals**. The core advice is to adopt a **slow-and-steady** mindset and design the codebase so correctness is easy to *check*: strict typing, strong interfaces/invariants, disciplined exception handling, pure-ish functions, and tests with good input coverage.

## The mindset shift: slow and steady

Key idea: with LLM speed available, you should spend your budget on **reducing risk**.

- Don’t “move fast and break things” by default; that slogan is an over-correction, not wisdom.
- If you write the wrong thing quickly, you just bounce between failures.
- The north star: aim for a codebase that looks like what an expert team would produce.

## Guidelines that map well to agentic coding

### 1) Types are a safety rail (and a loop-closer)

- **Use types as strictly as possible.** Type checking catches propagation errors (LLMs are especially bad at updating all call-sites/fields).
- LLMs thrive when the task is a “one-way function”: generate output → verify cheaply.
- **Type all the things** so you can verify changes quickly.

### 2) Use Pyright + IDE type-linting

- Run **Pyright** (author recommends it over mypy: faster, better narrowing rules, better ergonomics with untyped dependencies).
- Ensure type errors are **visible inline in the IDE**.
- The agent should check types before tests (even if not on every intermediate draft).

### 3) Ask: “should the types have caught this?”

During debugging:
- If the LLM proposes a diagnosis that would imply a type error, call it out.
- Watch for “gradual typing holes” where missing annotations silently become `Any`.

### 4) Annotate attributes correctly

Common pitfall: forgetting class attribute annotations, causing type-checkers to miss invalid assignments.

Pattern:

```python
class Foo:
    bar: str

    def __init__(self, bar: str) -> None:
        self.bar = bar
```

### 5) Prefer dataclasses / Pydantic over dicts

- LLMs love passing around `dict` and accessing `record["field"]`.
- That’s brittle: changes don’t propagate, different functions drift on schema, and the LLM often tries to support both variants instead of fixing the inconsistency.
- Use structured types so you get:
  - field access (`record.name`)
  - type checking
  - schema consistency

### 6) Scrutinize `Optional` / unions and “broadening” changes

- Don’t let the LLM make things `str | None` “just because”. Demand a reason.
- Be wary when debugging suggestions **broaden inputs/outputs** (it’s often a mistake and just makes the boundary leak more complexity).
- Prefer overloads when return types depend on inputs.

### 7) Control complexity at the interface (the boundary)

- Handle variations at the input boundary (web requests, files, env vars).
- Normalize early; pass one canonical shape through the rest of the program.
- Otherwise variation combinations explode (3×3 → 9), and the system gets harder to evolve.

### 8) Define invariants + demand valid inputs

- Every function should define what valid inputs are (including multi-argument invariants like “two lists must be the same length”).
- If inputs are invalid: **raise**.
- Don’t “cover up” errors; early failure makes debugging local and prevents LLMs from patching the wrong layer.

### 9) Crack down on exception handlers

- LLMs tend to add broad `try/except` blocks.
- Prefer:
  - minimal `try` blocks (one statement)
  - specific exceptions
  - handling “catch-all” only high in the stack (e.g., request handler)

### 10) Prefer pure functions (reduce side effects)

- Pure-ish functions are easier to test in isolation.
- Side effects make it easier to assemble failure out of “individually correct” parts.

### 11) Testing: prioritize input coverage, but use coverage tooling

- Good unit tests: parametrized, multiple inputs.
- Line coverage is imperfect, but can be useful in LLM-driven codebases to spot untested regions.
- Add tests for **invalid inputs**: LLMs are prone to hiding exceptions.
- Avoid the “reverse centaur” anti-pattern: don’t become the LLM’s error-pasting assistant.

## Source

- https://honnibal.dev/blog/llm-style-tips
