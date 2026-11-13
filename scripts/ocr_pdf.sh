#!/bin/zsh
# usage: ocr_pdf.sh <file.pdf> <out_dir> [psm=4]   -- 300 dpi render + tesseract (eng), one text file per page
pdf=$1; out=$2; psm=${3:-4}; b=$(basename "$pdf" .pdf)
mkdir -p "$out"; tmp=$(mktemp -d); pdftoppm -r 300 -gray -png "$pdf" "$tmp/p" 2>/dev/null
for img in $tmp/p-*.png; do n=${${img:t:r}#p-}; OMP_THREAD_LIMIT=1 tesseract "$img" stdout -l eng --psm $psm 2>/dev/null > "$out/${b}__p${n}.txt"; done
rm -rf "$tmp"
