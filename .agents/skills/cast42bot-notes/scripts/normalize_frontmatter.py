#!/usr/bin/env python3
"""Normalize notes in this repo to include minimal YAML frontmatter.

Rules live in .agents/skills/cast42bot-notes/SKILL.md.

Usage:
  python .agents/skills/cast42bot-notes/scripts/normalize_frontmatter.py [--apply]

Default is dry-run.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

RE_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n\n?", re.DOTALL)
RE_DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:[_-].*|\..*|$)")

EXCLUDE = {
    Path("README.md"),
    Path("_meta/glossary.md"),
    Path("_meta/tags.md"),
    Path("topics/coaching/README.md"),
    Path("topics/learning/README.md"),
}


@dataclass
class Plan:
    path: Path
    title: str
    date: str
    type_: str
    topics: list[str]


def sh(cmd: list[str], cwd: Path) -> str:
    return subprocess.check_output(cmd, cwd=str(cwd), text=True).strip()


def git_last_date(repo: Path, file: Path) -> str:
    # ISO short date, fall back to today if file not committed yet.
    try:
        out = sh(["git", "log", "-1", "--format=%cs", "--", str(file)], cwd=repo)
        return out.split()[0] if out else "1970-01-01"
    except Exception:
        return "1970-01-01"


def _strip_wrapping_md(s: str) -> str:
    s = s.strip()
    # Common cases where the whole title line is wrapped in emphasis.
    for wrapper in ("**", "*", "`"):
        if s.startswith(wrapper) and s.endswith(wrapper) and len(s) >= 2 * len(wrapper) + 1:
            s = s[len(wrapper) : -len(wrapper)].strip()
    return s


def derive_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return _strip_wrapping_md(line[2:].strip())
    return path.stem.replace("_", " ").replace("-", " ").strip().title()


def derive_date(repo: Path, path: Path) -> str:
    m = RE_DATE_PREFIX.match(path.name)
    if m:
        return m.group(1)
    return git_last_date(repo, path)


def derive_type(path: Path) -> str:
    if path.parts[0] == "inbox":
        return "inbox"
    if path.parts[0] == "meetings":
        return "meeting"
    if path.parts[0] == "refs":
        return "reference"
    return "note"


def derive_topics(path: Path) -> list[str]:
    if path.parts[0] != "topics":
        return [path.parts[0]]
    # topics/<topic>/file.md
    if len(path.parts) >= 3:
        return [path.parts[1]]
    # topics/file.md
    return [path.stem]


def build_frontmatter(p: Plan) -> str:
    topics_yaml = "\n".join([f"  - {t}" for t in p.topics])
    return (
        "---\n"
        f"title: \"{p.title.replace('\\"', '\\"')}\"\n"
        f"date: {p.date}\n"
        f"type: {p.type_}\n"
        "topics:\n"
        f"{topics_yaml}\n"
        "tags: []\n"
        "---\n\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes")
    args = ap.parse_args()

    repo = Path.cwd()
    files = sorted(Path(".").glob("**/*.md"))
    changed = 0

    for path in files:
        path = Path(os.path.normpath(path))
        if path in EXCLUDE:
            continue
        if any(part.startswith(".git") for part in path.parts):
            continue
        if path.parts and path.parts[0].startswith(".") and path.parts[0] != ".agents":
            continue
        # Only normalize the actual notes areas.
        if path.parts[0] not in {"inbox", "meetings", "refs", "topics"}:
            continue

        text = path.read_text(encoding="utf-8")
        if RE_FRONTMATTER.search(text):
            continue

        plan = Plan(
            path=path,
            title=derive_title(text, path),
            date=derive_date(repo, path),
            type_=derive_type(path),
            topics=derive_topics(path),
        )
        fm = build_frontmatter(plan)
        new_text = fm + text

        changed += 1
        print(f"MISSING FRONTMATTER: {path} -> add title={plan.title!r} date={plan.date} type={plan.type_} topics={plan.topics}")

        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    print(f"\nFiles updated: {changed}" + (" (applied)" if args.apply else " (dry-run)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
