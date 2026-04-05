# Compiled knowledge workflow

Small Karpathy-inspired layer on top of dated source notes.

## Scripts

### 1) Find Raindrop links not yet in notes
```bash
python3 scripts/raindrop_missing_notes.py
```

### 2) Promote source notes into an evergreen synthesis note
```bash
python3 scripts/promote_to_evergreen.py refs/enterprise_ai_adoption.md \
  topics/AGI/2026-03-11_article_ramp_ai-index-march-2026_anthropic-adoption.md \
  topics/MAGMA/microsoft/copilot/2026-03-19_x_aakashgupta_copilot_suleyman_copilot-reorg.md
```

### 3) Refresh TWILs for recently-added notes
```bash
python3 scripts/twil_refresh_recent.py
```

## Principle
- `topics/**` = dated source notes
- `refs/**` = evergreen synthesis notes
- TWIL should summarize both new source notes and important synthesis changes over time
