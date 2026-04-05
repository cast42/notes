#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path('/Users/lode/.openclaw/workspace')
DEFAULT_INPUTS = [ROOT / 'refs' / '_index.md']

LINK_RE = re.compile(r'\[(.*?)\]\((.*?)\)')


def extract_links(md_path: Path):
    text = md_path.read_text(encoding='utf-8', errors='ignore')
    links = []
    for label, target in LINK_RE.findall(text):
        if target.endswith('.md'):
            p = (md_path.parent / target).resolve()
            if p.exists():
                links.append((label, p))
    return links


def extract_tldr(text: str):
    m = re.search(r'## TL;DR\n(.+?)(?:\n## |\Z)', text, re.S)
    return m.group(1).strip() if m else ''


def build_examples(note_paths):
    examples = []
    for p in note_paths:
        text = p.read_text(encoding='utf-8', errors='ignore')
        title_m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        title = title_m.group(1) if title_m else p.stem
        tldr = extract_tldr(text)
        topic = p.parts[p.parts.index('topics') + 1] if 'topics' in p.parts else 'refs'
        if tldr:
            examples.append({
                'question': f'What is this note about: {title}?',
                'answer': tldr,
                'sources': [str(p.relative_to(ROOT))],
                'type': 'single_note_summary',
                'topic': topic,
            })
    return examples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ROOT / 'refs' / 'eval_dataset.jsonl'))
    args = ap.parse_args()

    note_paths = []
    for idx in DEFAULT_INPUTS:
        for _, p in extract_links(idx):
            note_paths.append(p)

    examples = build_examples(note_paths)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + '\n')
    print(out)
    print(f'{len(examples)} examples')


if __name__ == '__main__':
    main()
