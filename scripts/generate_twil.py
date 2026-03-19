#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/lode/.openclaw/workspace')
TOPICS_DIR = ROOT / 'topics'
TWIL_DIR = ROOT / 'twil'

DATE_RE = re.compile(r'(\d{4}-\d{2}-\d{2})_')


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--start', help='YYYY-MM-DD')
    p.add_argument('--end', help='YYYY-MM-DD')
    p.add_argument('--previous-week', action='store_true')
    return p.parse_args()


def week_bounds_for_previous(today: dt.date):
    # previous ISO week (Mon-Sun)
    this_monday = today - dt.timedelta(days=today.weekday())
    start = this_monday - dt.timedelta(days=7)
    end = start + dt.timedelta(days=6)
    return start, end


def infer_note_date(path: Path, text: str | None = None) -> str | None:
    m = DATE_RE.search(path.name)
    if m:
        return m.group(1)
    if text:
        m2 = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})\s*$', text, flags=re.M)
        if m2:
            return m2.group(1)
        m3 = re.search(r'^created_at:\s*(\d{4}-\d{2}-\d{2})', text, flags=re.M)
        if m3:
            return m3.group(1)
    return None


def extract_topics(path: Path, text: str) -> list[str]:
    m = re.search(r'^topics:\s*\n((?:\s*-\s*.+\n)+)', text, flags=re.M)
    if m:
        vals = []
        for line in m.group(1).splitlines():
            mm = re.match(r'\s*-\s*(.+?)\s*$', line)
            if mm:
                vals.append(mm.group(1))
        if vals:
            return vals
    # fallback from folder path topics/<topic>/...
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if len(parts) >= 3 and parts[0] == 'topics':
        return [parts[1]]
    return ['unknown']


def main():
    args = parse_args()
    today = dt.date.today()

    if args.previous_week:
        start_d, end_d = week_bounds_for_previous(today)
    elif args.start and args.end:
        start_d = dt.date.fromisoformat(args.start)
        end_d = dt.date.fromisoformat(args.end)
    else:
        raise SystemExit('Provide --previous-week or --start/--end')

    start, end = start_d.isoformat(), end_d.isoformat()
    iso_year, iso_week, _ = start_d.isocalendar()

    notes = []
    for p in TOPICS_DIR.rglob('*.md'):
        text = p.read_text(encoding='utf-8', errors='ignore')
        d = infer_note_date(p, text)
        if not d:
            continue
        if start <= d <= end:
            topics = extract_topics(p, text)
            rel = p.relative_to(ROOT)
            notes.append((d, rel, topics))

    notes.sort(key=lambda x: (x[0], str(x[1]).lower()))

    topic_counter = Counter()
    for _, _, tps in notes:
        for t in tps:
            topic_counter[t] += 1
    main_topic = topic_counter.most_common(1)[0][0] if topic_counter else 'none'

    out = []
    out.append('---')
    out.append('type: twil')
    out.append(f'year: {iso_year}')
    out.append(f'iso_week: {iso_week}')
    out.append(f'week_start: {start}')
    out.append(f'week_end: {end}')
    out.append(f'main_topic: {main_topic}')
    out.append('source_scope: topics/**/*.md')
    out.append(f'generated_at: {dt.datetime.now().replace(microsecond=0).isoformat()}')
    out.append('---\n')

    out.append(f'# TWIL — {iso_year} Week {iso_week} ({start} → {end})\n')

    out.append('## TL;DR')
    out.append(f'Main thread: **{main_topic}**. {len(notes)} notes captured this week ({start} → {end}).\n')

    out.append('## Highlights')
    for d, rel, tps in notes:
        label = rel.stem
        link = f'../{rel.as_posix()}'
        out.append(f'- {d}: [{label}]({link}) · topics: {", ".join(tps)}')
    if not notes:
        out.append('- No notes captured in this week range.')
    out.append('')

    out.append('## Topic signal')
    if topic_counter:
        for t, c in topic_counter.most_common():
            out.append(f'- `{t}` ×{c}')
    else:
        out.append('- none')
    out.append('')

    out.append('## Links')
    for d, rel, _ in notes:
        label = rel.stem
        link = f'../{rel.as_posix()}'
        out.append(f'- {d}: [{label}]({link})')
    if not notes:
        out.append('- none')

    TWIL_DIR.mkdir(parents=True, exist_ok=True)
    target = TWIL_DIR / f'{iso_year}_week_{iso_week:02d}_{main_topic.lower().replace(" ","_")}.md'
    target.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
