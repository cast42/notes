#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/Users/lode/.openclaw/workspace"
COLLECTION="cast42-notes"
MASK="{inbox,meetings,refs,topics,twil}/**/*.md"
LOG_DIR="$WORKSPACE/_tmp/logs"
LOG_FILE="$LOG_DIR/qmd-maintenance.log"
LOCK_DIR="$WORKSPACE/_tmp/locks"
LOCK_FILE="$LOCK_DIR/qmd-maintenance.pid"

mkdir -p "$LOG_DIR" "$LOCK_DIR"

# lock (pid-file, macOS-safe)
if [[ -f "$LOCK_FILE" ]]; then
  EXISTING_PID="$(cat "$LOCK_FILE" 2>/dev/null || true)"
  if [[ -n "$EXISTING_PID" ]] && kill -0 "$EXISTING_PID" 2>/dev/null; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] another run is in progress (pid $EXISTING_PID), skipping" >> "$LOG_FILE"
    exit 0
  fi
fi

echo $$ > "$LOCK_FILE"
cleanup_lock() { rm -f "$LOCK_FILE"; }
trap cleanup_lock EXIT

export PATH="$HOME/.bun/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

cd "$WORKSPACE"
log "qmd maintenance start"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git pull --ff-only origin main >> "$LOG_FILE" 2>&1; then
    log "git pull ok"
  else
    log "git pull failed (continuing)"
  fi
fi

if qmd collection list 2>/dev/null | grep -q "^${COLLECTION} "; then
  log "recreating qmd collection ${COLLECTION}"
  qmd collection remove "$COLLECTION" >> "$LOG_FILE" 2>&1 || true
fi

log "adding qmd collection ${COLLECTION}"
qmd collection add "$WORKSPACE" --name "$COLLECTION" --mask "$MASK" >> "$LOG_FILE" 2>&1

log "qmd update"
qmd update >> "$LOG_FILE" 2>&1

# Run embeddings at night only (01:00-06:59 local time), or force with --embed
HOUR=$(date +%H)
if [[ "${1:-}" == "--embed" || ( "$HOUR" -ge 1 && "$HOUR" -le 6 ) ]]; then
  log "qmd embed"
  qmd embed >> "$LOG_FILE" 2>&1 || log "qmd embed failed"
else
  log "skip embed (outside night window)"
fi

log "qmd status snapshot"
qmd status >> "$LOG_FILE" 2>&1 || true

log "qmd maintenance done"
