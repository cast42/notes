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

# The Sunday agent job may already have created this week's TWIL. Do not
# overwrite its curated content or create a second file with another topic.
WEEK_PREFIX="$(python3 -c 'import datetime as d; x=d.date.today()-d.timedelta(days=d.date.today().weekday()+1); y,w,_=x.isocalendar(); print(f"{y}_week_{w:02d}_")')"
EXISTING_TWIL="$(find "$WORKSPACE/twil" -maxdepth 1 -name "${WEEK_PREFIX}*.md" -print -quit)"
if [[ -n "$EXISTING_TWIL" ]]; then
  log "TWIL already exists for ${WEEK_PREFIX%_}; leaving it unchanged"
  exit 0
fi

GENERATOR_OUTPUT="$(python3 "$WORKSPACE/scripts/generate_twil.py" --previous-week --activity | tee -a "$LOG_FILE" | tail -n 1)"
TARGET_FILE="${GENERATOR_OUTPUT%%:*}"

# validate only the generated twil file
python3 "$WORKSPACE/scripts/check_markdown_links.py" "$TARGET_FILE" >> "$LOG_FILE" 2>&1

if [[ -f "$TARGET_FILE" ]] && ! grep -q '^main_topic: none$' "$TARGET_FILE"; then
  if [[ -n "$(git status --porcelain -- "$TARGET_FILE")" ]]; then
    git add -- "$TARGET_FILE"
    git commit -m "Generate weekly TWIL (auto)" -- "$TARGET_FILE" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1 || log "git push failed"
    log "twil changes committed"
  else
    log "no twil changes"
  fi
else
  log "generated empty week; not committing"
fi

log "twil weekly done"
