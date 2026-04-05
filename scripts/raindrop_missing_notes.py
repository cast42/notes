#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path('/Users/lode/.openclaw/workspace')
SCAN_DIRS = ['topics', 'refs', 'inbox', 'meetings', 'twil']


def raindrop_items(limit: int = 50):
    cmd = ['raindrop', 'search', '--limit', str(limit), '--format', 'json']
    data = subprocess.check_output(cmd, text=True)
    payload = json.loads(data)
    return payload.get('items', [])


def repo_has_url(url: str) -> bool:
    cmd = ['rg', '-n', '-F', url, *SCAN_DIRS]
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode == 0


def topic_guess(item: dict) -> str:
    text = ' '.join([
        item.get('title', ''),
        item.get('excerpt', '') or '',
        ' '.join(item.get('tags', []) if isinstance(item.get('tags'), list) else [])
    ]).lower()
    if 'copilot' in text or 'microsoft' in text:
        return 'MAGMA/microsoft/copilot'
    if 'anthropic' in text or 'openai' in text or 'deepmind' in text or 'ai' in text or 'agent' in text:
        return 'AGI'
    return 'inbox'


def main():
    items = raindrop_items()
    missing = []
    for item in items:
        url = item.get('link', '')
        if not url:
            continue
        if not repo_has_url(url):
            missing.append({
                'title': item.get('title', ''),
                'url': url,
                'topic_guess': topic_guess(item),
            })

    print('# Missing Raindrop URLs not yet in notes\n')
    for i, m in enumerate(missing, 1):
        print(f"{i}. {m['title']}\n   {m['url']}\n   topic_guess: {m['topic_guess']}\n")


if __name__ == '__main__':
    main()
