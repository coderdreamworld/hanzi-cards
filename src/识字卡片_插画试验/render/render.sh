#!/bin/sh
# SVG -> PNG，2x。用法: render.sh in.svg out.png
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR=$(cd "$(dirname "$1")" && pwd)
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --screenshot="$2" --window-size=760,480 --force-device-scale-factor=2 \
  "file://$DIR/$(basename "$1")" 2>/dev/null
