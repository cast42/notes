---
type: "source_capture"
source_url: "https://github.com/kajisho5/ffmpeg-skill"
canonical_url: "https://github.com/kajisho5/ffmpeg-skill"
title: "Raw capture: kajisho5/ffmpeg-skill"
date: "2026-09-20"
topics: ["agentic_coding"]
generated: {"by": "process:note-ingest", "at": "2026-09-20T11:26:28+02:00"}
sources:
  - {"id": "repository", "resource": "https://github.com/kajisho5/ffmpeg-skill"}
  - {"id": "skill-file", "resource": "https://raw.githubusercontent.com/kajisho5/ffmpeg-skill/main/SKILL.md"}
---

# Source capture

## Repository

- Repository: https://github.com/kajisho5/ffmpeg-skill
- Maintainer: `kajisho5`
- Public repository description: “Give your coding agent a video editor.”
- The repository presents itself as an Agent Skill for Claude Code, Cursor, Codex, and agents that read `SKILL.md`.
- License shown by GitHub: MIT.
- Runtime premise: local FFmpeg and Python 3.9 standard library; no cloud service or API key is required.
- Installation shown by the repository: `npx ffmpeg-skill`, with `--cursor`, `--codex`, or `--all` variants.
- The repository reports 42 tools, each callable from the CLI and reachable through MCP. MCP lists a core subset by default; `contract --json` describes the full surface.

## README design claims

The repository says its fixed workflow is:

1. probe the real input;
2. prefer lossless operations where possible;
3. plan with `--dry-run --json` before rendering;
4. chain transformations in a sensible order;
5. check the destination requirements;
6. verify output measurements;
7. keep originals and require explicit overwrite;
8. inspect a contact sheet whenever the picture changes.

It explicitly separates mechanical verification from judgment. For example, the skill can verify that captions exist at requested times and that dimensions are correct, but the calling agent or human must decide whether a face was cropped, a caption covers an important subject, or a selected highlight is interesting.

## Tool inventory captured from the repository

Analysis and inspection include `probe.py`, `scenes.py`, `look.py`, `cropdetect.py`, `report.py`, and `verify.py`. Editing includes `cut.py`, `join.py`, `silence.py`, `fit.py`, `crop.py`, `denoise.py`, `redact.py`, `stabilize.py`, `overlay.py`, `graphics.py`, `broll.py`, `multicam.py`, and related tools. Audio and delivery tools include `audio.py`, `sync.py`, `loudness.py`, `caption.py`, `export.py`, `render.py`, `check.py`, `batch.py`, and `metadata.py`.

The repository documents common flags including `--dry-run`, `--json`, `--json-brief`, `--fast`, `--progress`, `--timeout`, `--overwrite`, and `--plan`. Re-encoding tools expose codec and quality choices. Output reports include probes and verification data.

## SKILL.md capture

The linked `SKILL.md` instructs the agent to probe each input, plan from measured values rather than assumptions, use stream copy when the request permits it, avoid overwriting originals, and report failures honestly. It also says that when the picture changes, the agent should create and inspect a `look.py` contact sheet; if no vision capability is available, it must say that pixels were not inspected rather than claiming visual verification.

The skill distinguishes operations from decisions. It executes cuts, joins, captions, reframes, audio processing, exports, and checks, but does not decide which cut is right, what a video means, what looks good, which crop preserves the subject, or what caption wording should be.

## Interpretation boundary

The repository's capability and tool-count descriptions are maintainer claims from the repository and `SKILL.md`, not an independent benchmark. The note treats the workflow and design principles as the durable contribution; individual FFmpeg capabilities remain dependent on the local installation and build.
