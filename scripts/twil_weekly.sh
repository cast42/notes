#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/Users/lode/.openclaw/workspace"
LOG_DIR="$WORKSPACE/_tmp/logs"
LOG_FILE="$LOG_DIR/twil-weekly.log"
LOCK_DIR="$WORKSPACE/_tmp/locks"
LOCK_FILE="$LOCK_DIR/twil-weekly.pid"

mkdir -p "$LOG_DIR" "$LOCK_DIR"

if [[ -f "$LOCK_FILE" ]]; then
  EXISTING_PID="$(cat "$LOCK_FILE" 2>/dev/null || true)"
  if [[ -n "$EXISTING_PID" ]] && kill -0 "$EXISTING_PID" 2>/dev/null; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] run already in progress (pid $EXISTING_PID), skipping" >> "$LOG_FILE"
    exit 0
  fi
fi

echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

export PATH="$HOME/.bun/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

cd "$WORKSPACE"
log "twil weekly start"

git pull --ff-only origin main >> "$LOG_FILE" 2>&1 || log "git pull failed (continuing)"

python3 "$WORKSPACE/scripts/generate_twil.py" --previous-week | tee -a "$LOG_FILE"

# validate links in twil files
python3 "$WORKSPACE/scripts/check_markdown_links.py" twil >> "$LOG_FILE" 2>&1

if ! git diff --quiet -- twil; then
  git add twil/*.md
  git commit -m "Generate weekly TWIL (auto)" >> "$LOG_FILE" 2>&1 || true
  git push origin main >> "$LOG_FILE" 2>&1 || log "git push failed"
  log "twil changes committed"
else
  log "no twil changes"
fi

log "twil weekly done"
