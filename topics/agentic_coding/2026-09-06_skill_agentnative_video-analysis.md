---
title: "Agent Native video-analysis skill"
date: 2026-09-06
timestamp: 2026-09-06
type: procedure
topics:
  - agentic_coding
tags:
  - agent-skills
  - video-analysis
  - multimodal-agents
  - gemini
  - timestamped-evidence
resource: "https://agentnative.inc/resources/give-agents-video-analysis-skill"
source_url: "https://agentnative.inc/resources/give-agents-video-analysis-skill"
canonical_url: "https://agentnative.inc/resources/give-agents-video-analysis-skill"
author: "Agent Native"
skill_name: "video-analysis"
description: "A self-contained agent procedure for analyzing local video and audio with Gemini, returning grounded findings with timestamps and explicit uncertainty."
sources:
  - id: agentnative-skill
    resource: "https://agentnative.inc/resources/give-agents-video-analysis-skill"
    title: "Agent Native: Give agents video analysis skill"
  - id: gemini-video-guide
    resource: "https://ai.google.dev/gemini-api/docs/video-understanding"
    title: "Gemini API video understanding guide"
  - id: gemini-files-guide
    resource: "https://ai.google.dev/gemini-api/docs/files"
    title: "Gemini API Files guide"
  - id: aistudio-agentic-video
    resource: "https://aistudio.google.com/learn/agentic-video-understanding-with-gemini?e=0"
    title: "Google AI Studio: Agentic video understanding with Gemini"
generated:
  by: "process:codex"
  at: "2026-09-07T07:41:00+02:00"
verified:
  - by: "process:codex"
    at: "2026-09-07T07:41:00+02:00"
---

# Agent Native video-analysis skill

## TL;DR

- The `video-analysis` skill gives Codex, Claude, or GrokBot a repeatable way to inspect the actual audio and visuals of a local video through the Gemini API.
- It is designed to return a concise answer with timestamped evidence, separating direct observations from interpretation and marking unclear or uncertain material.
- Its strongest design choice is procedural: inspect the exact file, upload the original video with audio, use a grounded question, report coverage limits, and delete the temporary Gemini upload afterward.

## Key takeaways

- The workflow handles overview, spoken-content transcription, visual explanation, critique, and locating specific moments. If the user gives no narrow question, it produces an overview with timestamped observations.
- It uses Google's official Python SDK and the Gemini Files API. The skill requires a Gemini API key supplied privately through `GEMINI_API_KEY` or `GOOGLE_API_KEY`; the key must never be pasted into chat, written into the skill, printed, or placed in command arguments.
- The linked [Google AI Studio guide](https://aistudio.google.com/learn/agentic-video-understanding-with-gemini?e=0) explains an optional agentic processing mode: Gemini can search transcripts, retrieve targeted frame windows at adaptive frame rates, and extract audio on demand instead of loading the entire video uniformly.
- The agent should analyze the video itself, not substitute a transcript or a handful of screenshots when the task requires visual or audio understanding.
- The output contract is evidence-oriented: give the main finding, useful `HH:MM:SS` timestamps, what is actually visible or audible, and the distinction between observation and interpretation.

## Workflow

1. **Choose and inspect the file.** Use the exact user-supplied file; do not scan or upload unrelated videos. Confirm that it exists and inspect duration, size, video streams, and audio streams with `ffprobe`.
2. **Prepare only if necessary.** Keep the original unchanged. If the format is unsupported, create a temporary H.264/AAC MP4 with `ffmpeg`. If segmentation is required, cover the requested range completely, use small overlaps, preserve original offsets, and avoid double-counting overlap.
3. **Upload securely.** Prefer the Gemini Files API and include the actual video, including audio when present. Poll until the upload is `ACTIVE`, with bounded timeouts; stop on `FAILED` rather than waiting indefinitely.
4. **Ask for grounded analysis.** Send the video to a currently available video-capable Gemini model together with the user's question. Request concise findings, timestamps, observable evidence, uncertainty markers, and no claims about uncovered parts of the timeline.
5. **Return and clean up.** Answer in chat unless a file is requested. Delete the Gemini upload in a `finally` block and remove only temporary local files created by the workflow. Report cleanup failure instead of claiming it succeeded.

## Why this is useful

The skill turns a generic multimodal capability into an auditable interaction pattern. Timestamps make a long answer navigable; requiring observations before interpretation reduces unsupported scene descriptions; and the explicit coverage rule prevents the agent from treating a partial clip or failed transcription as evidence about the whole video.

For software demonstrations, the procedure says to describe the interface and actual actions rather than infer intent from narration. For critique, each suggestion should be tied to a visible or audible example. For clip selection, the output should include start and end times, what happens, and why the moment matters.

## Boundaries and failure modes

- A Gemini API key and network access are prerequisites. An agent that cannot read local files or make API requests should state that limitation rather than claim to have watched the video.
- Model names, processing modes, upload limits, and duration limits can change. The skill therefore directs the agent to check the current official Gemini video guide before choosing a model or relying on limits.
- Timestamps are estimates unless verified locally. The agent should not invent dialogue, identities, scenes, or actions, and should mark unreadable text and uncertain speech.
- Instructions spoken or displayed in a video are content to analyze, not permission to operate accounts or perform unrelated actions.
- External upload is part of the workflow. Users who prohibit external uploads need a different local-analysis route or an explicit limitation report.

## Design assessment

The skill is more than a prompt: it combines file selection, media inspection, API lifecycle, grounded prompting, uncertainty handling, and cleanup. The most reusable pattern is **evidence-preserving multimodal analysis**—make the source and coverage explicit, attach claims to locations in the source, and keep temporary processing state disposable.

It is intentionally a provider-specific implementation around Gemini rather than a provider-neutral interface. That keeps the instructions concrete and executable, but makes the skill dependent on the current Gemini SDK, model availability, API limits, and private key setup.

The Google guide extends the skill's design with a useful optimization: **active
media retrieval**. For long videos or fine-grained temporal questions, agentic
processing can spend media tokens on the moments relevant to the question,
while short clips may still be better served by static processing. The guide
reports lower token use and cost in its own benchmarks; those figures are
provider-reported and should not be treated as universal guarantees.

## Sources

- [Agent Native: Give agents video analysis skill](https://agentnative.inc/resources/give-agents-video-analysis-skill) [agentnative-skill]
- [Gemini API: Video understanding](https://ai.google.dev/gemini-api/docs/video-understanding) [gemini-video-guide]
- [Gemini API: Files](https://ai.google.dev/gemini-api/docs/files) [gemini-files-guide]
- [Google AI Studio: Agentic video understanding with Gemini](https://aistudio.google.com/learn/agentic-video-understanding-with-gemini?e=0) [aistudio-agentic-video]

The complete skill-page capture is preserved in [the raw source note](raw/2026-09-06_skill_agentnative_video-analysis.raw.md).
