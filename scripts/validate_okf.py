#!/usr/bin/env python3
"""Validate the Open Knowledge Format bundle rooted at topics/.

Conformance errors fail the command. Optional metadata and missing local links
are reported as warnings so older notes can be repaired incrementally.
"""
from __future__ import annotations

import re
import sys
from collections.abc import Mapping
from datetime import datetime
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
SUPPORTED_VERSIONS = ("0.1", "0.2")


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


def metadata_warnings(metadata: Mapping) -> list[str]:
    """Check adopted 0.2 fields without making them conformance requirements."""
    warnings: list[str] = []

    def timestamp(value: object, field: str) -> None:
        try:
            parsed = (
                value if isinstance(value, datetime)
                else datetime.fromisoformat(str(value))
            )
            if parsed.utcoffset() is None:
                raise ValueError
        except (TypeError, ValueError):
            warnings.append(f"{field} should be an ISO 8601 datetime with a UTC offset")

    def event(value: object, field: str, require_at: bool) -> None:
        if not isinstance(value, Mapping):
            warnings.append(f"{field} should be a mapping")
            return
        actor = value.get("by")
        if not isinstance(actor, str) or not re.fullmatch(
            r"(?:human:[^\s]+|process:[^\s]+|[^\s/]+/[^\s/]+)", actor
        ):
            warnings.append(f"{field}.by should identify a human, process, or producer/version")
        if require_at or "at" in value:
            timestamp(value.get("at"), f"{field}.at")

    if "generated" in metadata:
        event(metadata["generated"], "generated", False)
    if "verified" in metadata:
        verified = metadata["verified"]
        if isinstance(verified, Mapping):
            verified = [verified]
        if not isinstance(verified, list):
            warnings.append("verified should be a mapping or a list of mappings")
        else:
            for index, value in enumerate(verified):
                event(value, f"verified[{index}]", True)
    if "sources" in metadata:
        sources = metadata["sources"]
        if not isinstance(sources, list):
            warnings.append("sources should be a list of mappings")
        else:
            for index, source in enumerate(sources):
                if (
                    not isinstance(source, Mapping)
                    or not isinstance(source.get("resource"), str)
                    or not source["resource"].strip()
                ):
                    warnings.append(f"sources[{index}] should have a non-empty resource string")
                elif "last_modified" in source:
                    timestamp(source["last_modified"], f"sources[{index}].last_modified")
    if "status" in metadata and metadata["status"] not in ("draft", "stable", "deprecated"):
        warnings.append("status should be draft, stable, or deprecated; use maturity for experimental")
    if "stale_after" in metadata:
        timestamp(metadata["stale_after"], "stale_after")
    return warnings


def validate_frontmatter(
    path: Path, errors: list[str], warnings: list[str] | None = None
) -> None:
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
        if not any(metadata == {"okf_version": version} for version in SUPPORTED_VERSIONS):
            errors.append(
                f'{label}: frontmatter must contain only okf_version: "0.1" or "0.2"'
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
    if not isinstance(concept_type, str) or not concept_type.strip():
        errors.append(f"{label}: concept frontmatter requires a non-empty string type")
    if warnings is not None:
        warnings.extend(f"{label}: {warning}" for warning in metadata_warnings(metadata))


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
        if parsed.scheme.lower() in SCHEMES or parsed.netloc:
            continue
        target = unquote(parsed.path)
        if not target:
            continue
        resolved = (
            BUNDLE / target.lstrip("/") if target.startswith("/")
            else path.parent / target
        ).resolve()
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
    if not ROOT_INDEX.is_file():
        errors.append("topics/index.md: repository bundle requires a root index")
    for path in files:
        validate_frontmatter(path, errors, warnings)
        warnings.extend(link_warnings(path))

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    concepts = sum(path.name not in RESERVED for path in files)
    if errors:
        print(
            f"FAIL: {len(errors)} conformance error(s), "
            f"{len(warnings)} warning(s) in {len(files)} Markdown files.",
            file=sys.stderr,
        )
        return 1

    print(
        f"OK: OKF bundle (supported versions: {', '.join(SUPPORTED_VERSIONS)}) "
        f"with {concepts} concept files and "
        f"{len(files) - concepts} reserved files; {len(warnings)} warning(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
