---
title: "OpenClaw upgrade troubleshooting note"
date: 2026-04-13
type: note
topics:
  - openclaw
tags: []
---

# OpenClaw upgrade troubleshooting note

## TL;DR
- The 2026.4.11 upgrade mostly went fine, but one recovery step had to be run manually on the Mac instead of fully from chat.
- Main failure mode was a permissions issue during global npm install, followed by temporary gateway reachability confusion after restart.
- Practical recovery path: update, restart gateway, probe gateway, and only escalate to local terminal commands if the service does not come back cleanly.

## Key takeaways / what stuck
- A plain `npm install -g openclaw@latest` failed with `EACCES` on `/usr/local/lib/node_modules/openclaw`.
- Running the install with `sudo` fixed the package update.
- After restart, `openclaw status` briefly showed `Gateway ... unreachable (timeout)` even though the service process was running.
- `openclaw gateway probe` was the decisive verification step and confirmed the gateway was reachable and updated to 2026.4.11.
- Codex auth appears to have survived this upgrade, so `openclaw configure --section model` was not needed this time, though it remains a good fallback check after updates.

## Details

### Observed sequence
1. Tried upgrading OpenClaw from chat.
2. Global npm update failed because of permissions under `/usr/local/lib/node_modules/`.
3. Manual fix on the Mac:
   - `sudo npm install -g openclaw@latest`
4. CLI showed the new version correctly.
5. After `openclaw gateway restart`, `openclaw status` temporarily reported the gateway as unreachable.
6. `openclaw gateway probe` then showed the gateway was actually reachable and on app version 2026.4.11.
7. Final conclusion: installation and gateway were healthy again.

### Recommended next-time checklist
```bash
sudo npm install -g openclaw@latest
openclaw --version
openclaw gateway restart
openclaw gateway probe
openclaw status
```

### If status still looks bad
Try:
```bash
openclaw gateway stop
openclaw gateway start
openclaw gateway probe
openclaw status
```

### If package install fails again
Likely cause:
- permissions on `/usr/local/lib/node_modules/openclaw`

Practical fix:
- rerun with `sudo`

### If gateway shows unreachable after restart
Do not panic immediately. Use:
```bash
openclaw gateway probe
```
That gave the clearest signal and may succeed even when `openclaw status` still shows a temporary timeout.

## Links / sources
- Local command sequence and outputs captured from the 2026-04-13 upgrade session.
