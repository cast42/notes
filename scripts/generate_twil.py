#!/usr/bin/env python3
"""Generate a weekly summary of curated topic notes added to Git.

Selection is based on the commit date when a concept file was first added, not
the publication date stored in the note. Raw captures and OKF-reserved files are
excluded so each curated concept appears once.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS_DIR = ROOT / "topics"
TWIL_DIR = ROOT / "twil"
RESERVED = {"index.md", "log.md"}
COMMIT_MARKER = "@@@"


@dataclass(frozen=True)
class AddedNote:
    added_on: dt.date
    path: Path
    title: str
    content_date: str | None
    topics: tuple[str, ...]
    summary: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", help="YYYY-MM-DD")
    parser.add_argument("--end", help="YYYY-MM-DD")
    parser.add_argument("--previous-week", action="store_true")
    return parser.parse_args()


def week_bounds(day: dt.date) -> tuple[dt.date, dt.date]:
    start = day - dt.timedelta(days=day.weekday())
    return start, start + dt.timedelta(days=6)


def previous_week_bounds(today: dt.date) -> tuple[dt.date, dt.date]:
    this_monday, _ = week_bounds(today)
    start = this_monday - dt.timedelta(days=7)
    return start, start + dt.timedelta(days=6)


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end >= 0 else ""


def scalar(metadata: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", metadata, flags=re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith(("'", '"')) and value.endswith(value[0]):
        value = value[1:-1]
    return value or None


def extract_topics(path: Path, metadata: str) -> tuple[str, ...]:
    inline = scalar(metadata, "topics")
    if inline and inline.startswith("[") and inline.endswith("]"):
        values = [value.strip().strip("'\"") for value in inline[1:-1].split(",")]
        values = [value for value in values if value]
        if values:
            return tuple(values)

    block = re.search(r"^topics:\s*\n((?:\s+-\s*.+\n?)+)", metadata, flags=re.M)
    if block:
        values = []
        for line in block.group(1).splitlines():
            match = re.match(r"\s*-\s*(.+?)\s*$", line)
            if match:
                values.append(match.group(1).strip("'\""))
        if values:
            return tuple(values)

    relative = path.relative_to(ROOT)
    if len(relative.parts) >= 3:
        return (relative.parts[1],)
    return ("unknown",)


def extract_title(path: Path, text: str, metadata: str) -> str:
    title = scalar(metadata, "title")
    if title:
        return title
    heading = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
    if heading:
        return heading.group(1)
    return path.stem.replace("_", " ").replace("-", " ").strip().title()


def compact_markdown(value: str) -> str:
    value = re.sub(r"^[-*]\s+", "", value.strip())
    value = re.sub(r"[*_`]", "", value)
    value = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", value)
    return re.sub(r"\s+", " ", value).strip()


def extract_summary(text: str, title: str) -> str:
    match = re.search(r"^## TL;DR\s*\n(.+?)(?=\n##\s|\Z)", text, flags=re.M | re.S)
    if not match:
        return title
    lines = [line for line in match.group(1).strip().splitlines()]
    if not lines:
        return title

    selected: list[str] = []
    first = next((index for index, line in enumerate(lines) if line.strip()), None)
    if first is None:
        return title
    if re.match(r"\s*[-*]\s+", lines[first]):
        selected.append(lines[first])
        for line in lines[first + 1 :]:
            if not line.strip() or re.match(r"\s*[-*]\s+", line):
                break
            selected.append(line)
    else:
        for line in lines[first:]:
            if not line.strip():
                break
            selected.append(line)

    summary = compact_markdown(" ".join(selected)) or title
    if len(summary) > 280:
        summary = summary[:277].rsplit(" ", 1)[0] + "…"
    return summary


def is_curated_concept(path: Path) -> bool:
    try:
        relative = path.relative_to(TOPICS_DIR)
    except ValueError:
        return False
    return (
        path.suffix == ".md"
        and path.name not in RESERVED
        and "raw" not in relative.parts
        and not path.name.endswith(".raw.md")
    )


def git_added_paths(start: dt.date, end: dt.date) -> list[tuple[dt.date, Path]]:
    command = [
        "git",
        "log",
        f"--since={start.isoformat()} 00:00:00",
        f"--until={end.isoformat()} 23:59:59",
        "--diff-filter=A",
        "--date=short",
        f"--pretty=format:{COMMIT_MARKER}%ad",
        "--name-only",
        "--",
        "topics",
    ]
    output = subprocess.check_output(command, cwd=ROOT, text=True)
    current_date: dt.date | None = None
    additions: dict[Path, dt.date] = {}

    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(COMMIT_MARKER):
            current_date = dt.date.fromisoformat(line[len(COMMIT_MARKER) :])
            continue
        if current_date is None:
            continue
        path = ROOT / line
        if path.exists() and is_curated_concept(path):
            additions[path] = current_date

    return sorted(((added, path) for path, added in additions.items()), key=lambda x: (x[0], str(x[1]).lower()))


def load_notes(start: dt.date, end: dt.date) -> list[AddedNote]:
    notes = []
    for added_on, path in git_added_paths(start, end):
        text = path.read_text(encoding="utf-8", errors="replace")
        metadata = frontmatter(text)
        title = extract_title(path, text, metadata)
        notes.append(
            AddedNote(
                added_on=added_on,
                path=path,
                title=title,
                content_date=scalar(metadata, "date") or scalar(metadata, "created_at"),
                topics=extract_topics(path, metadata),
                summary=extract_summary(text, title),
            )
        )
    return notes


def render(start: dt.date, end: dt.date, notes: list[AddedNote]) -> str:
    iso_year, iso_week, _ = start.isocalendar()
    topic_counter = Counter(topic for note in notes for topic in note.topics)
    primary_counter = Counter(note.topics[0] for note in notes if note.topics)
    leaders = primary_counter.most_common()
    if not leaders:
        main_topic = "weekly"
    elif len(leaders) > 1 and leaders[0][1] == leaders[1][1]:
        main_topic = "mixed"
    else:
        main_topic = leaders[0][0]
    top_topics = ", ".join(f"{topic} ×{count}" for topic, count in topic_counter.most_common(3)) or "none"
    today = dt.date.today()
    status = "complete" if end < today else "in_progress"
    note_date = min(end, today)
    generated_at = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()

    out = [
        "---",
        f'title: "TWIL {iso_year} week {iso_week}: {main_topic}"',
        f"date: {note_date.isoformat()}",
        "type: twil",
        "topics:",
        "  - twil",
        f"  - {main_topic}",
        "tags: []",
        f"week: {iso_year}-W{iso_week:02d}",
        "period:",
        f"  start: {start.isoformat()}",
        f"  end: {end.isoformat()}",
        f"status: {status}",
        f"main_topic: {main_topic}",
        "source_scope: curated topic concepts added in Git",
        f"generated_at: {generated_at}",
        "---",
        f"# TWIL {iso_year} week {iso_week}: {main_topic}",
        "",
        f"- **Period:** {start.isoformat()} → {end.isoformat()}",
        f"- **Status:** `{status}`",
        f"- **Signal:** {len(notes)} notes, top topics: {top_topics}",
        "",
        "## TL;DR",
    ]

    if notes:
        if main_topic == "mixed":
            out.append(
                f"This week added {len(notes)} curated notes with no single dominant "
                f"topic. The collection ranged across "
                f"{', '.join(topic for topic, _ in topic_counter.most_common(3))}."
            )
        else:
            out.append(
                f"This week added {len(notes)} curated notes. The strongest thread was "
                f"**{main_topic}**, with the collection also touching "
                f"{', '.join(topic for topic, _ in topic_counter.most_common(3) if topic != main_topic) or 'adjacent ideas in the same area'}."
            )
    else:
        out.append("No curated topic notes were added in this ISO week; this entry preserves weekly continuity.")

    out.extend(["", "## Highlights"])
    if notes:
        for note in notes:
            relative = note.path.relative_to(ROOT)
            link = f"../{relative.as_posix()}"
            source_date = f"; source date {note.content_date}" if note.content_date and note.content_date != note.added_on.isoformat() else ""
            out.append(f"- [{note.title}]({link}) — {note.summary} _(added {note.added_on.isoformat()}{source_date})_")
    else:
        out.append("- No eligible notes found in this week.")

    out.extend(["", "## This happened → so that happened → which led to…"])
    if notes:
        signal = (
            "no single topic dominated the primary classification"
            if main_topic == "mixed"
            else (
                f"`{main_topic}` became the week's strongest primary signal "
                f"({primary_counter[main_topic]} "
                f"{'note' if primary_counter[main_topic] == 1 else 'notes'})"
            )
        )
        out.extend(
            [
                f"- **This happened:** {len(notes)} durable notes were added across {len(topic_counter)} topic areas.",
                f"- **So that happened:** {signal}.",
                "- **Which led to…** a compact map of the week's additions that can be revisited without scanning the Git history.",
            ]
        )
    else:
        out.extend(
            [
                "- **This happened:** no curated topic concepts were added.",
                "- **So that happened:** there was no content topic to compact.",
                "- **Which led to…** a continuity-only weekly entry.",
            ]
        )

    out.extend(["", "## Topic signal"])
    if topic_counter:
        out.extend(f"- `{topic}` ×{count}" for topic, count in topic_counter.most_common())
    else:
        out.append("- none")

    out.extend(["", "## Links"])
    if notes:
        for note in notes:
            relative = note.path.relative_to(ROOT)
            out.append(f"- [{note.title}](../{relative.as_posix()})")
    else:
        out.append("- none")

    return "\n".join(out) + "\n"


def main() -> int:
    args = parse_args()
    today = dt.date.today()
    if args.previous_week:
        start, end = previous_week_bounds(today)
    elif args.start and args.end:
        start = dt.date.fromisoformat(args.start)
        end = dt.date.fromisoformat(args.end)
    else:
        raise SystemExit("Provide --previous-week or --start/--end")
    if end < start:
        raise SystemExit("--end must be on or after --start")

    notes = load_notes(start, end)
    iso_year, iso_week, _ = start.isocalendar()
    target = TWIL_DIR / f"{iso_year}_week_{iso_week:02d}_weekly.md"
    target.write_text(render(start, end, notes), encoding="utf-8")
    print(f"{target.relative_to(ROOT)}: {len(notes)} curated notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
