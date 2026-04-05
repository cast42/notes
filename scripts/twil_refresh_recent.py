#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import subprocess
from pathlib import Path

ROOT = Path('/Users/lode/.openclaw/workspace')


def week_bounds(d: dt.date):
    start = d - dt.timedelta(days=d.weekday())
    end = start + dt.timedelta(days=6)
    return start, end


def note_dates_from_paths(paths):
    dates = set()
    for p in paths:
        name = Path(p).name
        if len(name) >= 10 and name[:10].count('-') == 2:
            try:
                dates.add(dt.date.fromisoformat(name[:10]))
            except Exception:
                pass
    return sorted(dates)


def main():
    out = subprocess.check_output(['git', '-C', str(ROOT), 'diff', '--name-only', 'HEAD~1..HEAD'], text=True)
    files = [line.strip() for line in out.splitlines() if line.strip().startswith('topics/')]
    dates = note_dates_from_paths(files)
    seen = set()
    for d in dates:
        start, end = week_bounds(d)
        key = (start, end)
        if key in seen:
            continue
        seen.add(key)
        subprocess.check_call(['python3', str(ROOT / 'scripts/generate_twil.py'), '--start', start.isoformat(), '--end', end.isoformat()])
        print(f'refreshed {start}..{end}')


if __name__ == '__main__':
    main()
