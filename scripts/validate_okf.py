#!/usr/bin/env python3
"""Validate the Open Knowledge Format bundle rooted at topics/.

Conformance errors fail the command. Missing relative link targets are reported
as warnings so older notes can be repaired incrementally.
"""
from __future__ import annotations

import re
import sys
from collections.abc import Mapping
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print(
        "error: PyYAML is required; run "
        "`uv run --with PyYAML python scripts/validate_okf.py`",
        file=sys.stderr,
    )
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "topics"
ROOT_INDEX = BUNDLE / "index.md"
RESERVED = {"index.md", "log.md"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEMES = {"data", "http", "https", "mailto", "qmd", "tel"}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def frontmatter(text: str) -> tuple[str | None, str | None]:
    """Return (YAML text, error); YAML is None when frontmatter is absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, "frontmatter is not closed with ---"
    return "\n".join(lines[1:end]), None


def validate_frontmatter(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw, framing_error = frontmatter(text)
    label = relative(path)

    if framing_error:
        errors.append(f"{label}: {framing_error}")
        return

    if path == ROOT_INDEX:
        if raw is None:
            errors.append(f"{label}: bundle index requires YAML frontmatter")
            return
        try:
            metadata = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            errors.append(f"{label}: invalid YAML: {exc.problem or exc}")
            return
        if metadata != {"okf_version": "0.1"}:
            errors.append(
                f'{label}: frontmatter must contain only okf_version: "0.1"'
            )
        return

    if path.name in RESERVED:
        if raw is not None:
            errors.append(f"{label}: nested index/log files must not have frontmatter")
        return

    if raw is None:
        errors.append(f"{label}: concept file requires YAML frontmatter")
        return

    try:
        metadata = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        errors.append(f"{label}: invalid YAML: {exc.problem or exc}")
        return
    if not isinstance(metadata, Mapping):
        errors.append(f"{label}: frontmatter must parse to a mapping")
        return
    concept_type = metadata.get("type")
    if concept_type is None or not str(concept_type).strip():
        errors.append(f"{label}: concept frontmatter requires a non-empty type")


def link_warnings(path: Path) -> list[str]:
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for match in LINK_RE.finditer(text):
        raw = match.group(1).strip().strip("<>")
        if not raw or raw.startswith("#"):
            continue
        if " " in raw:
            raw = raw.split(" ", 1)[0]
        parsed = urlsplit(raw)
        if parsed.scheme.lower() in SCHEMES or parsed.netloc or raw.startswith("/"):
            continue
        target = unquote(parsed.path)
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            warnings.append(f"{relative(path)}: relative link target not found: {target}")
    return warnings


def main() -> int:
    if not BUNDLE.is_dir():
        print("error: topics/ bundle not found", file=sys.stderr)
        return 2

    files = sorted(BUNDLE.rglob("*.md"))
    errors: list[str] = []
    warnings: list[str] = []
    for path in files:
        validate_frontmatter(path, errors)
        warnings.extend(link_warnings(path))

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    concepts = sum(path.name not in RESERVED for path in files)
    if errors:
        print(
            f"FAIL: {len(errors)} conformance error(s), "
            f"{len(warnings)} link warning(s) in {len(files)} Markdown files.",
            file=sys.stderr,
        )
        return 1

    print(
        f"OK: OKF 0.1 bundle with {concepts} concept files and "
        f"{len(files) - concepts} reserved files; {len(warnings)} link warning(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
