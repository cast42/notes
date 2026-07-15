#!/usr/bin/env python3
"""Add repository-compatible frontmatter to note files that lack it.

Rules live in .agents/skills/cast42bot-notes/SKILL.md. OKF-reserved index.md
and log.md files under topics/ are deliberately skipped.

Usage:
  python .agents/skills/cast42bot-notes/scripts/normalize_frontmatter.py [--apply]

Default is dry-run.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path

RE_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n\n?", re.DOTALL)
RE_DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:[_-].*|\..*|$)")
NOTE_AREAS = {"inbox", "meetings", "refs", "topics"}
OKF_RESERVED = {"index.md", "log.md"}


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
    """Return the last commit date, falling back to today for new files."""
    try:
        out = sh(["git", "log", "-1", "--format=%cs", "--", str(file)], cwd=repo)
        return out.split()[0] if out else date.today().isoformat()
    except Exception:
        return date.today().isoformat()


def strip_wrapping_markdown(value: str) -> str:
    value = value.strip()
    for wrapper in ("**", "*", "`"):
        if (
            value.startswith(wrapper)
            and value.endswith(wrapper)
            and len(value) >= 2 * len(wrapper) + 1
        ):
            value = value[len(wrapper) : -len(wrapper)].strip()
    return value


def derive_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return strip_wrapping_markdown(line[2:].strip())
    return path.stem.replace("_", " ").replace("-", " ").strip().title()


def derive_date(repo: Path, path: Path) -> str:
    match = RE_DATE_PREFIX.match(path.name)
    if match:
        return match.group(1)
    return git_last_date(repo, path)


def derive_type(path: Path) -> str:
    if path.parts[0] == "inbox":
        return "inbox"
    if path.parts[0] == "meetings":
        return "meeting"
    if path.parts[0] == "refs":
        return "reference"
    if "raw" in path.parts:
        return "source"

    tokens = set(re.split(r"[_-]", path.stem.lower()))
    if "book" in tokens:
        return "book"
    if tokens & {"tweet", "x"}:
        return "tweet"
    if tokens & {"youtube", "video"}:
        return "video"
    if "paper" in tokens:
        return "paper"
    if tokens & {"article", "blog", "newsletter"}:
        return "article"
    return "note"


def derive_topics(path: Path) -> list[str]:
    if path.parts[0] != "topics":
        return [path.parts[0]]
    if len(path.parts) >= 3:
        return [path.parts[1]]
    return [path.stem]


def build_frontmatter(plan: Plan) -> str:
    topics_yaml = "\n".join(f"  - {topic}" for topic in plan.topics)
    return (
        "---\n"
        f"title: {json.dumps(plan.title, ensure_ascii=False)}\n"
        f"date: {plan.date}\n"
        f"type: {plan.type_}\n"
        "topics:\n"
        f"{topics_yaml}\n"
        "tags: []\n"
        "---\n\n"
    )


def is_reserved_okf_file(path: Path) -> bool:
    return path.parts[0] == "topics" and path.name in OKF_RESERVED


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write changes")
    args = parser.parse_args()

    repo = Path.cwd()
    files = sorted(Path(".").glob("**/*.md"))
    changed = 0

    for path in files:
        path = Path(os.path.normpath(path))
        if any(part.startswith(".git") for part in path.parts):
            continue
        if path.parts and path.parts[0].startswith(".") and path.parts[0] != ".agents":
            continue
        if path.parts[0] not in NOTE_AREAS or is_reserved_okf_file(path):
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
        frontmatter = build_frontmatter(plan)
        changed += 1
        print(
            f"MISSING FRONTMATTER: {path} -> add title={plan.title!r} "
            f"date={plan.date} type={plan.type_} topics={plan.topics}"
        )

        if args.apply:
            path.write_text(frontmatter + text, encoding="utf-8")

    mode = "applied" if args.apply else "dry-run"
    print(f"\nFiles updated: {changed} ({mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
