#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path('/Users/lode/.openclaw/workspace')


def extract_title(text: str, fallback: str) -> str:
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
    return m.group(1) if m else fallback


def extract_tldr(text: str) -> str:
    m = re.search(r'## TL;DR\n(.+?)(?:\n## |\Z)', text, re.S)
    return m.group(1).strip() if m else ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('sources', nargs='+')
    args = ap.parse_args()

    target = Path(args.target)
    if not target.is_absolute():
        target = ROOT / target

    sections = []
    links = []
    for src in args.sources:
        p = Path(src)
        if not p.is_absolute():
            p = ROOT / p
        text = p.read_text(encoding='utf-8', errors='ignore')
        title = extract_title(text, p.stem)
        tldr = extract_tldr(text)
        rel = p.relative_to(ROOT).as_posix()
        sections.append((title, tldr, rel))
        links.append(f'- [{title}](../{rel})')

    title_slug = target.stem.replace('_', ' ')
    content = f"---\ntitle: \"{title_slug}\"\ndate: 2026-04-05\ntype: reference\ntopics:\n  - refs\ntags:\n  - evergreen\n---\n\n# {title_slug}\n\n## TL;DR\nCompiled evergreen note generated from multiple source notes.\n\n## Source note summaries\n"
    for title, tldr, rel in sections:
        content += f"\n### {title}\n{tldr or 'No TL;DR found.'}\nSource: `{rel}`\n"
    content += "\n## Source links\n" + '\n'.join(links) + '\n'

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
