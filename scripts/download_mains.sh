#!/bin/zsh
# usage: download_mains.sh <out_dir>   -- downloads every Mains GS paper listed in data/mains_sources.json from upsc.gov.in
out=${1:?out dir}; here=${0:A:h}; mkdir -p "$out"
python3 -I -c "
import json,sys
for r in json.load(open('$here/../data/mains_sources.json')): print(r['file'],r['url'],sep='\t')" | while IFS=$'\t' read -r f u; do
  curl -sL -m 120 -A "Mozilla/5.0" -o "$out/$f" "$u" && head -c4 "$out/$f" | grep -q '%PDF' || echo "FAILED $f"
done
