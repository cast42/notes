#!/usr/bin/env python3
"""Token-efficient note ingestion helpers.

This script does NOT fetch from the internet by itself.
It turns already-extracted content (text/json) into a progressive-disclosure note pair:
- thin primary note
- thick raw note

Use with the OpenClaw agent which performs extraction (FxTwitter, browser, etc.).
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "igshid",
    "ref",
    "s",
    "t",
}


def iso_date_now() -> str:
    return dt.datetime.now().date().isoformat()


def slugify(s: str, max_len: int = 80) -> str:
    s = s.strip().lower()
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    if not s:
        s = "note"
    return s[:max_len].rstrip("-")


def normalize_url(url: str) -> str:
    """Cheap URL normalization for dedupe; not perfect but good enough."""
    url = url.strip()
    url = re.sub(r"^https?://", "https://", url)
    url = url.replace("twitter.com/", "x.com/")
    url = url.replace("www.", "")

    # strip fragments
    url = url.split("#", 1)[0]

    # strip common tracking params
    if "?" in url:
        base, qs = url.split("?", 1)
        kept = []
        for part in qs.split("&"):
            if not part:
                continue
            k = part.split("=", 1)[0]
            if k in TRACKING_PARAMS:
                continue
            kept.append(part)
        url = base + ("?" + "&".join(kept) if kept else "")

    # trim trailing slash
    if url.endswith("/"):
        url = url[:-1]

    return url


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def render_frontmatter(meta: Dict[str, Any]) -> str:
    # simple YAML renderer (strings/arrays only)
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        else:
            # escape quotes minimally
            if isinstance(v, str) and (":" in v or "#" in v):
                v = v.replace('"', "'")
                lines.append(f'{k}: "{v}"')
            else:
                lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def github_blob_url(vault_root: Path, relative_path: Path) -> Optional[str]:
    git_config = vault_root / ".git" / "config"
    if not git_config.exists():
        return None

    text = git_config.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"url\s*=\s*git@github\.com:([^/]+)/([^\s]+?)(?:\.git)?\s*$", text, re.MULTILINE)
    if not m:
        m = re.search(r"url\s*=\s*https://github\.com/([^/]+)/([^\s]+?)(?:\.git)?\s*$", text, re.MULTILINE)
    if not m:
        return None

    owner, repo = m.group(1), m.group(2)
    return f"https://github.com/{owner}/{repo}/blob/main/{relative_path.as_posix()}"


def write_note_pair(
    *,
    vault_root: Path,
    topic: str,
    date: str,
    source: str,
    title: str,
    author: Optional[str],
    handle: Optional[str],
    source_url: str,
    canonical_url: Optional[str],
    primary_links: list[str],
    tldr_bullets: list[str],
    highlights: list[str],
    raw_text: str,
    extractor: str,
) -> Tuple[Path, Path]:
    topic_dir = vault_root / "topics" / topic
    raw_dir = topic_dir / "raw"
    ensure_dir(topic_dir)
    ensure_dir(raw_dir)

    slug = slugify(title)
    base = f"{date}_{source}_{slug}"

    primary_path = topic_dir / f"{base}.md"
    raw_path = raw_dir / f"{base}.raw.md"

    canon = normalize_url(canonical_url or source_url)

    meta_primary: Dict[str, Any] = {
        "type": source,
        "source_url": source_url,
        "canonical_url": canon,
        "title": title,
        "author": author,
        "handle": handle,
        "created_at": date,
        "topics": [topic],
    }

    meta_raw = dict(meta_primary)
    meta_raw.update(
        {
            "content_hash": sha256_text(raw_text),
            "extracted_at": dt.datetime.now().isoformat(timespec="seconds"),
            "extractor": extractor,
        }
    )

    primary = []
    primary.append(render_frontmatter(meta_primary))
    primary.append(f"# {title}\n")
    if author or handle:
        who = " — ".join([x for x in [(author or ""), (f"@{handle}" if handle else "")] if x])
        primary.append(f"*{who}*\n")
    primary.append("## TL;DR\n")
    primary.extend([f"- {b}" for b in (tldr_bullets or [])] or ["- (TODO)"])
    primary.append("\n## Highlights\n")
    primary.extend([f"- {h}" for h in (highlights or [])] or ["- (TODO)"])
    primary.append("\n## Links\n")
    primary.append(f"- Permalink: {md_link(canon, canon)}")
    for link in primary_links:
        primary.append(f"- {md_link(link, link)}")
    primary.append("\n## Raw\n")
    raw_rel_vault = raw_path.relative_to(vault_root)
    raw_blob = github_blob_url(vault_root, raw_rel_vault)
    if raw_blob:
        primary.append(f"- Raw text: {md_link(str(raw_rel_vault), raw_blob)}")
    else:
        primary.append(
            f"- Raw text: {md_link(str(raw_rel_vault), raw_path.relative_to(topic_dir).as_posix())}"
        )
    primary.append(f"- Extractor: {extractor}")
    primary.append("\n## My notes\n- ")

    raw = []
    raw.append(render_frontmatter(meta_raw))
    raw.append(f"# Raw content\n\nSource: {canon}\n\n")
    raw.append(raw_text.strip() + "\n")

    primary_path.write_text("\n".join(primary).rstrip() + "\n", encoding="utf-8")
    raw_path.write_text("\n".join(raw).rstrip() + "\n", encoding="utf-8")

    return primary_path, raw_path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(Path.cwd()), help="Path that contains topics/")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--source", required=True, help="tweet|article|video|pdf|text|other")
    ap.add_argument("--title", required=True)
    ap.add_argument("--author")
    ap.add_argument("--handle")
    ap.add_argument("--url", required=True)
    ap.add_argument("--canonical-url")
    ap.add_argument("--links", default="[]", help="JSON array of extra links")
    ap.add_argument("--tldr", default="[]", help="JSON array of TL;DR bullets")
    ap.add_argument("--highlights", default="[]", help="JSON array of highlights")
    ap.add_argument("--raw-file", required=True, help="Path to file containing raw extracted text")
    ap.add_argument("--extractor", default="manual")
    ap.add_argument("--date", default=iso_date_now())

    args = ap.parse_args()

    vault_root = Path(args.vault).expanduser().resolve()
    raw_text = Path(args.raw_file).expanduser().read_text(encoding="utf-8")

    primary, raw = write_note_pair(
        vault_root=vault_root,
        topic=args.topic,
        date=args.date,
        source=args.source,
        title=args.title,
        author=args.author,
        handle=args.handle,
        source_url=args.url,
        canonical_url=args.canonical_url,
        primary_links=json.loads(args.links),
        tldr_bullets=json.loads(args.tldr),
        highlights=json.loads(args.highlights),
        raw_text=raw_text,
        extractor=args.extractor,
    )

    print(str(primary))
    print(str(raw))


if __name__ == "__main__":
    main()
