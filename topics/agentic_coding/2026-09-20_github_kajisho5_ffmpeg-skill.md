---
type: "skill"
source_url: "https://github.com/kajisho5/ffmpeg-skill"
canonical_url: "https://github.com/kajisho5/ffmpeg-skill"
title: "ffmpeg-skill: local, verified video editing for agents"
author: "kajisho5"
date: "2026-09-20"
topics: ["agentic_coding"]
tags: [video-editing, audio-editing, ffmpeg, agent-skill, verification, mcp]
resource: "https://github.com/kajisho5/ffmpeg-skill"
generated: {"by": "process:note-ingest", "at": "2026-09-20T11:26:28+02:00"}
verified: [{"by": "process:codex", "at": "2026-09-20T11:26:28+02:00"}]
sources:
  - {"id": "repository", "resource": "https://github.com/kajisho5/ffmpeg-skill"}
  - {"id": "skill-file", "resource": "https://raw.githubusercontent.com/kajisho5/ffmpeg-skill/main/SKILL.md"}
description: "An offline Agent Skill that routes video and audio edits through typed local FFmpeg tools, capability checks, dry runs, output probes, and visual verification."
maturity: "experimental"
---

# ffmpeg-skill: local, verified video editing for agents

## TL;DR

[`ffmpeg-skill`](https://github.com/kajisho5/ffmpeg-skill) gives coding agents a local video and audio editing engine built around FFmpeg and Python's standard library. It exposes 42 typed command-line tools, optional MCP access, machine-readable contracts, and a fixed workflow:

**probe → plan → edit → check → verify → inspect**

The central design choice is to make media operations measurable and repeatable. The skill does not decide what a good edit is or which moments are interesting; it executes explicit parameters and reports what the resulting file contains.

## What it provides

The repository covers:

- inspection: media probing, scene changes, audio peaks, shot measurements, motion-centre reports, and contact sheets;
- editing: cuts, joins, silence and filler removal, speed changes, reframing, crops, denoising, stabilization, overlays, graphics, redaction, reverse, loops, B-roll, and multicam;
- captions and audio: SRT/text captions, animated or karaoke captions, transcription when a local Whisper installation exists, voice cleanup, compression, limiting, music ducking, sync, and loudness normalization;
- delivery: platform templates and exports for YouTube, Reels, TikTok, Shorts, X, LinkedIn, Facebook, and podcasts;
- projects and automation: multi-step render projects, caching, batch jobs, reports, and a machine-readable contract for agents and MCP clients.

The repository is standalone: it uses local `ffmpeg`/`ffprobe`, needs no cloud service or API key, and keeps source footage on the machine.

## The workflow

1. **Probe real inputs.** Measure duration, frame rate, resolution, codecs, audio layout, HDR/colour information, and variable-frame-rate risk. Do not infer media properties from filenames.
2. **Prefer lossless operations.** Use stream copying for operations such as keyframe cuts or remuxing when possible; re-encode only when the requested transformation requires it.
3. **Plan before rendering.** Use `--dry-run --json` for writing steps and use plans with input fingerprints when a job will be executed later.
4. **Chain in a deliberate order.** The documented order is colour conversion/LUTs, cut, join, silence removal, fit/reframe, captions/overlays, sync, audio, loudness, and export. For three or more stages, use a render project.
5. **Check the deliverable.** Run platform checks for codec, dimensions, colour, frame rate, loudness, and other destination requirements. Distinguish mechanical failures from choices that require human judgment, such as whether a crop removes important content.
6. **Verify the output.** Require a successful command, a non-empty output, and a probe whose measurements match the request. Report actual duration, dimensions, frame rate, codecs, and audio properties.
7. **Keep originals.** Outputs are new files by default. Replacement requires explicit overwrite consent.
8. **Look at changed pictures.** When captions, overlays, crops, colour, or transitions alter the picture, render a contact sheet and inspect it. A media probe cannot tell whether text covers a face or whether a crop is aesthetically acceptable.

## Design principles

The skill separates execution from judgment:

- **Typed tools instead of shell strings:** each operation has explicit arguments and does not accept an arbitrary filter graph from the caller.
- **Capability-aware execution:** `doctor` and the contract report available FFmpeg encoders, filters, and other components. Unknown capability is not silently treated as available.
- **Contract-derived MCP:** tool schemas are generated from the same `argparse` definitions that drive the CLI, reducing drift between the command-line and MCP surfaces.
- **Dry-run and JSON reporting:** tools can show planned commands and return structured output, probes, verification results, and errors.
- **No silent overwrite:** originals are preserved and output replacement is explicit.
- **Mechanical versus aesthetic checks:** the skill verifies requested properties, while the calling agent or human decides whether content, composition, colour, or a chosen highlight is actually good.
- **Deterministic boundaries:** the same input and explicit parameters should produce the same verifiable operation; taste and interpretation remain outside the execution layer.

## Why this is useful for agents

An agent that only knows FFmpeg syntax can still make unsafe or uncheckable choices: assume a frame rate, select an incompatible codec, re-encode unnecessarily, or report success without opening the output. This skill turns media editing into a sequence of inspectable contracts:

- input facts are measured before planning;
- operations expose typed parameters and capabilities;
- outputs carry structured probes;
- visual changes receive a separate image-level check;
- failures identify missing tools, FFmpeg errors, timeouts, interruptions, or verification failures.

This is a strong pattern for tool design generally: the tool should report what it did and what it can verify, while leaving semantic approval to the agent or user who understands the goal.

## Limits and failure modes

The skill is an execution and verification layer, not a complete video-production director. It does not decide:

- which part of a recording is the best highlight;
- whether a deliverable is publishable or aesthetically successful;
- what a video is about;
- which subject should be kept when a crop is ambiguous;
- what caption words should say or how they should be rewritten;
- how to choose creative colour, branding, thumbnail, or composition decisions.

Some operations also depend on the local FFmpeg build. A tool can be installed while a required filter or encoder is unavailable, so per-tool capability data matters. The skill recommends reporting warnings instead of silently “fixing” subjective or destination-dependent choices.

## Relation to the existing agentic-coding notes

This skill is a concrete media-tool layer for the minimal harness described in [Omar Sar's minimal agent harness guide](2026-09-14_tweet_omar-sar-s-minimal-agent-harness-guide.md). It complements the [agent-native video-analysis skill](2026-09-06_skill_agentnative_video-analysis.md): that skill gathers timestamped evidence about a video, while `ffmpeg-skill` performs local transformations and verifies the resulting file.

## Assessment

The most reusable idea is not the list of 42 media commands. It is the **probe–plan–execute–verify–inspect** contract. It prevents the agent from confusing a successful process exit with a successful media result and keeps subjective decisions visible instead of hiding them inside a generic “video editing” tool.

## Sources

- [Repository and README](https://github.com/kajisho5/ffmpeg-skill)
- [Skill instructions](https://raw.githubusercontent.com/kajisho5/ffmpeg-skill/main/SKILL.md)

## Raw capture

- [Repository and skill capture](raw/2026-09-20_github_kajisho5_ffmpeg-skill.raw.md)
