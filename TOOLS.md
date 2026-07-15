# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Local environment
- Shell: fish

## OpenClaw / Codex
- After OpenClaw updates, reauthenticate OpenAI Codex by running `openclaw configure --section model`.

## Git / GitHub SSH
- (Operational notes live here: host-specific SSH config, key names, troubleshooting.)
- Migrated pointer from MEMORY.md on 2026-02-22.
- Re-confirmed as tooling-only (kept in TOOLS.md) on 2026-03-11.

## Raindrop.io
- (CLI commands/auth/safety notes live here.)

## summarize (@steipete/summarize)
- Preferred usage: run via `npx` (no global install required).
- Basic URL summary:
  - `npx -y @steipete/summarize "https://example.com" --length medium --plain`
- YouTube summary:
  - `npx -y @steipete/summarize "https://youtu.be/<id>" --length medium --plain`
- PDF summary:
  - `npx -y @steipete/summarize "https://example.com/file.pdf" --length medium --plain`
- If X/Twitter fetch fails in summarize, use Browser Relay to capture post text and then summarize from stdin:
  - `cat note.txt | npx -y @steipete/summarize - --length short --plain`

Add whatever helps you do your job. This is your cheat sheet.
