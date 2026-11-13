#!/bin/zsh
# Rebuild every derived data file. Run from the app/ directory. Inputs live one level up (../upsc-prelims-complete.pdf, ../syllabus.pdf, ../pyq/*.pdf).
set -e
W=../work; mkdir -p $W/text $W/ocr $W/ocr_psm6 data
pdftotext -layout ../upsc-prelims-complete.pdf $W/text/upsc-prelims-complete.txt 2>/dev/null
pdftotext -layout ../syllabus.pdf $W/text/syllabus.txt
[ "$(ls $W/ocr | wc -l)" -gt 0 ] || ls ../pyq/*.pdf | xargs -P 6 -I{} scripts/ocr_pdf.sh {} $W/ocr 4      # slow: ~15 min
python3 -I scripts/parse_prelims.py $W/text/upsc-prelims-complete.txt $W/prelims_raw.json
python3 -I scripts/build_syllabus.py $W/text/syllabus.txt data/syllabus.json
python3 scripts/author_all.py data
python3 -I scripts/parse_mains.py $W/ocr data/mains_sources.json $W/mains_raw.json $W/ocr_psm6   # psm6 dir is an optional fallback (see README)
python3 -I scripts/build_data.py $W data
python3 -I scripts/audit.py data data/inventory.json COVERAGE.md
python3 -I scripts/validate.py
