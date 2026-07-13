#!/usr/bin/env python3
"""Refresh the current and recent TWIL summaries."""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_twil.py"


def week_bounds(day: dt.date) -> tuple[dt.date, dt.date]:
    start = day - dt.timedelta(days=day.weekday())
    return start, start + dt.timedelta(days=6)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--weeks", type=int, default=2, help="Number of ISO weeks to refresh")
    args = parser.parse_args()
    if args.weeks < 1:
        raise SystemExit("--weeks must be at least 1")

    current_start, _ = week_bounds(dt.date.today())
    for offset in reversed(range(args.weeks)):
        start = current_start - dt.timedelta(days=7 * offset)
        end = start + dt.timedelta(days=6)
        subprocess.check_call(
            [
                sys.executable,
                str(GENERATOR),
                "--start",
                start.isoformat(),
                "--end",
                end.isoformat(),
            ],
            cwd=ROOT,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
