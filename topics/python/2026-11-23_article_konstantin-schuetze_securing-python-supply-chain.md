---
title: "Securing Python projects from supply-chain attacks"
date: 2026-11-23
type: article
topics:
  - python
tags:
  - supply-chain-security
  - dependency-locking
  - github-actions
  - trusted-publishing
  - uv
resource: "https://astral.sh/blog/securing-from-supply-chain-attacks"
description: "Layer dependency and CI pinning, trusted publishing, release controls, and cooldowns to reduce Python supply-chain exposure."
author: Konstantin Schütze
sources:
  - resource: "https://astral.sh/blog/securing-from-supply-chain-attacks"
---

# Securing Python projects from supply-chain attacks

## TL;DR

Astral recommends layered defenses for Python dependencies and GitHub CI: lock versions and verify artifact hashes, pin Actions and downloaded binaries, protect publishing, and delay adoption of new releases. The article assumes the dependency versions you start with are already trusted; pinning does not make malicious code safe.

## Threat model

The focus is a malicious new release after a maintainer or CI compromise, and replacement or tampering of artifacts on a distribution server. **Version pinning** prevents automatically taking a newer release; **hash pinning** checks the exact downloaded artifact, including where a version or tag can point to changed content. A lockfile is only as trustworthy as its creation, review and update process.

## Practical defenses

1. **Lock and hash dependencies, including transitive ones.** Astral says `uv.lock` includes hashes where the index supplies them. Enforce the existing lock in CI using `--locked` or `UV_LOCKED=1`; otherwise uv may resolve when the lock is out of date.
2. **Pin GitHub Actions to full commit SHAs**, not mutable tags, and review automated pin updates. Tools such as pinact, Dependabot or Renovate can help maintain them. Check binaries downloaded by those actions too; pinning the action itself does not pin an external download.
3. **Verify downloaded executables and archives before running them.** Compare SHA-256 against an independently trusted expected value; downloading both a file and its expected hash from the same compromised source does not establish authenticity.
4. **Use PyPI Trusted Publishing.** Configure the authorized repository, workflow and environment and use OIDC instead of a long-lived PyPI upload token. Protect release environments with approvals where appropriate.
5. **Lint workflows with zizmor.** It flags CI security concerns including mutable Action references and risky trigger patterns. A finding requires context, not automatic proof of exploitation.
6. **Apply a dependency cooldown.** For example, `exclude-newer = "3d"` in `[tool.uv]` delays newly published files; uv supports package-specific exceptions. Dependabot and Renovate have analogous controls. This buys detection time, not a guarantee, and can delay urgent security fixes.
7. **Lock CI tools too.** Replace unpinned `uvx` invocations with tools in a locked dependency group, e.g. `uv run --locked --only-group nox --isolated nox -s mylintcommand`. Lock standalone PEP 723 scripts with `uv lock --script foo.py` and enforce the lock when running them.
8. **Consider disabling source builds** with `[tool.uv] no-build = true` where suitable wheels exist. This reduces exposure to build-backend execution and unpinned build dependencies, but may break platforms or packages without suitable wheels. It does not make wheel contents safe.

## Limitations

These controls are defense in depth, not vulnerability detection or a substitute for reviewing dependencies and updates. Protect the repository, CI permissions and lockfiles themselves; an attacker who can alter trusted hashes or publishing workflows can undermine the checks. Cooldowns trade freshness for detection time, and restricting source builds trades compatibility for reduced build-time exposure.

## Sources

- [Konstantin Schütze, Astral, 23 November 2026](https://astral.sh/blog/securing-from-supply-chain-attacks), including examples and links to the relevant documentation.
