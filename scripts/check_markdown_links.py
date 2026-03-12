#!/usr/bin/env python3
"""Check local markdown links resolve for selected files/directories.

Usage:
  scripts/check_markdown_links.py <file-or-dir> [<file-or-dir> ...]

Only local links are validated; external URLs are ignored.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def should_skip(url: str) -> bool:
    u = url.strip()
    return (
        not u
        or u.startswith("#")
        or u.startswith(("http://", "https://", "mailto:", "tel:", "qmd://", "data:", "/"))
    )


def clean_target(url: str) -> str:
    u = url.strip()
    if " " in u and not u.startswith("<"):
        u = u.split(" ", 1)[0]
    u = u.strip("<>")
    if "#" in u:
        u = u.split("#", 1)[0]
    return unquote(u)


def expand_targets(args: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in args:
        p = (ROOT / raw).resolve() if not raw.startswith("/") else Path(raw).resolve()
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file() and p.suffix.lower() == ".md":
            files.append(p)
        else:
            print(f"warning: not a markdown file/dir, skipping: {raw}")
    return files


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: scripts/check_markdown_links.py <file-or-dir> [<file-or-dir> ...]")
        return 2

    files = expand_targets(sys.argv[1:])
    missing: list[str] = []

    for md in files:
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            raw = m.group(1)
            if should_skip(raw):
                continue
            target = clean_target(raw)
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                try:
                    rel_file = md.relative_to(ROOT)
                except ValueError:
                    rel_file = md
                missing.append(f"{rel_file}: {raw}")

    if missing:
        print("Dangling markdown links found:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("OK: no dangling local markdown links found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
