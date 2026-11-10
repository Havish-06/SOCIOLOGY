#!/usr/bin/env bash
# Fetch original-language YouTube captions for every case video into data/transcripts/ (git-ignored).
REPO=$(cd "$(dirname "$0")/../.." && pwd)
YTDLP=${YTDLP:-yt-dlp}
OUT=$REPO/data/transcripts/raw
mkdir -p "$OUT"
while read -r cid vid; do
  [ -z "$cid" ] && continue
  if ls "$OUT/${cid}__${vid}".*.vtt >/dev/null 2>&1; then echo "skip $cid $vid"; continue; fi
  "$YTDLP" --skip-download --write-auto-subs --write-subs --sub-langs ".*-orig" --sub-format vtt \
     --sleep-requests 2 -o "$OUT/${cid}__${vid}.%(ext)s" "https://www.youtube.com/watch?v=$vid" >/dev/null 2>&1
  if ! ls "$OUT/${cid}__${vid}".*.vtt >/dev/null 2>&1; then
    "$YTDLP" --skip-download --write-auto-subs --write-subs --sub-langs "hi,en,te,ta,mr,pa" --sub-format vtt \
       --sleep-requests 2 -o "$OUT/${cid}__${vid}.%(ext)s" "https://www.youtube.com/watch?v=$vid" >/dev/null 2>&1
  fi
  n=$(ls "$OUT/${cid}__${vid}".*.vtt 2>/dev/null | head -1)
  echo "$cid $vid -> ${n:-NONE}"
  sleep 4
done < "$1"
