#!/usr/bin/env python3
"""Generate a weekly summary of topic notes dated within an ISO week."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS_DIR = ROOT / "topics"
TWIL_DIR = ROOT / "twil"
RESERVED = {"index.md", "log.md"}


@dataclass(frozen=True)
class WeekNote:
    path: Path
    title: str
    note_date: dt.date
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
    current_start, _ = week_bounds(today)
    return current_start - dt.timedelta(days=7), current_start - dt.timedelta(days=1)


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
        summary = summary[:277].rsplit(" ", 1)[0] + "..."
    return summary


def load_notes(start: dt.date, end: dt.date) -> list[WeekNote]:
    notes: list[WeekNote] = []
    for path in sorted(TOPICS_DIR.rglob("*.md")):
        if path.name in RESERVED:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        metadata = frontmatter(text)
        note_date = scalar(metadata, "date")
        if not note_date:
            continue
        try:
            parsed_date = dt.date.fromisoformat(note_date)
        except ValueError:
            continue
        if not (start <= parsed_date <= end):
            continue
        title = extract_title(path, text, metadata)
        notes.append(
            WeekNote(
                path=path,
                title=title,
                note_date=parsed_date,
                topics=extract_topics(path, metadata),
                summary=extract_summary(text, title),
            )
        )
    return notes


def topic_signal(notes: list[WeekNote]) -> tuple[str, Counter[str], Counter[str]]:
    total_counter: Counter[str] = Counter()
    file_counter: Counter[str] = Counter()

    for note in notes:
        note_topics = [topic for topic in note.topics if topic != "twil"]
        total_counter.update(note_topics)
        file_counter.update(set(note_topics))

    if not total_counter:
        return "weekly", total_counter, file_counter

    main_topic = min(
        total_counter,
        key=lambda topic: (-total_counter[topic], -file_counter[topic], topic),
    )
    return main_topic, total_counter, file_counter


def sorted_topics(total_counter: Counter[str], file_counter: Counter[str]) -> list[tuple[str, int]]:
    return sorted(
        total_counter.items(),
        key=lambda item: (-item[1], -file_counter[item[0]], item[0]),
    )


def slugify_topic(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", topic.lower()).strip("_")
    return slug or "weekly"


def render(start: dt.date, end: dt.date, notes: list[WeekNote], main_topic: str) -> str:
    iso_year, iso_week, _ = start.isocalendar()
    total_counter, file_counter = topic_signal(notes)[1:]
    ranked_topics = sorted_topics(total_counter, file_counter)
    top_topics = ", ".join(f"{topic} x{count}" for topic, count in ranked_topics[:3]) or "none"
    today = dt.date.today()
    status = "complete" if end <= today else "in_progress"
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
        "source_scope: topics/**/*.md with frontmatter date in range",
        f"generated_at: {generated_at}",
        "---",
        f"# TWIL {iso_year} week {iso_week}: {main_topic}",
        "",
        f"- **Period:** {start.isoformat()} -> {end.isoformat()}",
        f"- **Main topic:** `{main_topic}`",
        f"- **Signal:** {len(notes)} notes, top topics: {top_topics}",
        "",
        "## TL;DR",
    ]

    if notes:
        adjacent_topics = ", ".join(topic for topic, _ in ranked_topics if topic != main_topic) or "adjacent ideas in the same area"
        out.append(
            f"This week touched {len(notes)} dated topic notes. The strongest thread was **{main_topic}**, "
            f"with the rest clustering around {adjacent_topics}."
        )
    else:
        out.append(
            f"No `topics/**/*.md` notes with frontmatter `date:` fell inside ISO week {iso_week:02d}, "
            "so there was no dominant topic to compact. I still created the weekly note to preserve the chain and make the quiet week explicit."
        )

    out.extend(["", "## Highlights"])
    if notes:
        for note in notes:
            relative = note.path.relative_to(ROOT)
            out.append(
                f"- [{note.title}](../{relative.as_posix()}) — {note.summary} _(dated {note.note_date.isoformat()})_"
            )
    else:
        out.append(f"- No eligible notes found in range `{start.isoformat()} -> {end.isoformat()}`.")

    out.extend(["", "## This happened -> so that happened -> which led to..."])
    if notes:
        out.extend(
            [
                f"- **This happened:** {len(notes)} notes landed in `topics/` with dates between `{start.isoformat()}` and `{end.isoformat()}`.",
                f"- **So that happened:** `{main_topic}` became the top-of-mind topic at `{total_counter[main_topic]}` mentions across `{file_counter[main_topic]}` files.",
                "- **Which led to...** a compact weekly map you can revisit without re-scanning the whole knowledge base.",
            ]
        )
    else:
        out.extend(
            [
                f"- **This happened:** no dated topic notes matched `{start.isoformat()} -> {end.isoformat()}`.",
                "- **So that happened:** the topic tally stayed empty after excluding `twil`.",
                "- **Which led to...** a continuity-only TWIL entry with `main_topic: weekly`.",
            ]
        )

    out.extend(["", "## Links"])
    if notes:
        for note in notes:
            relative = note.path.relative_to(ROOT)
            out.append(f"- [{note.title}](../{relative.as_posix()})")
    else:
        out.append("- No in-range note links to include.")

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

    TWIL_DIR.mkdir(parents=True, exist_ok=True)
    notes = load_notes(start, end)
    iso_year, iso_week, _ = start.isocalendar()
    main_topic, _, _ = topic_signal(notes)
    target = TWIL_DIR / f"{iso_year}_week_{iso_week:02d}_{slugify_topic(main_topic)}.md"
    target.write_text(render(start, end, notes, main_topic), encoding="utf-8")
    print(f"{target.relative_to(ROOT)}: {len(notes)} dated notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
