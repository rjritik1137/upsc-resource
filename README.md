# UPSC GS Static Study Guide

A static, client-side study-navigation app built from the PRD in `../UPSC_Static_Study_Guide_Product_Requirements.pdf`.
Vite + React + TypeScript, no backend, no accounts, no runtime AI. Data ships as versioned JSON in `data/`.

**Read `COVERAGE.md` before trusting anything.** It is generated from the data and lists what is imported, flagged, missing or unreviewed.

## Status at a glance

| Area | State |
|---|---|
| Prelims GS-I PYQs, 1995–2026 (3,976, from the supplied compilation) | parsed with provenance (file + page). Answers are **as supplied by the third-party compilation; not checked against UPSC keys**. 9 cancelled and 4 unresolved items are marked, not resolved. |
| Mains GS-I..IV PYQs, 2016–2026 (760, UPSC PDFs → OCR) | text is **OCR, unverified**. GS-I..III: 20/20 per paper in every year (2 questions hand-transcribed from page images, flagged). **GS-IV is unreliable**: parts and long case studies are often merged. |
| Mains 2013–2015 | **not available** on UPSC's page or archive; not included. |
| Concepts (see COVERAGE.md for per-subject counts) | **draft-unreviewed**: written by the assistant from general knowledge, not checked against a textbook. History covers Ancient, Medieval, Modern, World and Art & Culture; Ethics/GS-IV has concepts but case-study OCR text is unreliable. |
| PYQ↔concept links (3,481) | **all `proposed`** by keyword/label rules; precision not measured (spot-checks show some wrong matches). |
| Resources (39) | official URLs HTTP-checked 2026-11-13. Books are cited by title/author only; **editions and chapters are not verified and not stated**. NCERT chapter locations unverified. |
| Not built yet | Society, Governance, IR, Science & Technology, Security, Disaster Management, Ethics, Art & Culture, Ancient/Medieval/World History. |
| Official-key check for Prelims answers | not performed. |

## Run

```sh
npm install
npm run dev        # syncs data, then starts Vite
npm run build      # syncs data → type-checks → builds to dist/
npm run preview
npm run validate   # data integrity: ids, dangling links, prerequisite cycles, provenance, per-concept fields
```

`data/*.json` is the source of truth; `public/data/` is a copy made by `npm run sync-data`.

## Free deployment (static hosting)

The build uses relative paths (`base: './'`) and hash routing, so it works from any folder or project sub-path.

- **GitHub Pages:** push `app/`, run `npm run build`, publish `dist/` (e.g. `gh-pages` branch or a Pages workflow uploading `dist`).
- **Cloudflare Pages:** build command `npm run build`, output directory `dist`, root directory `app`.
- Free-tier limits apply (file counts, size, bandwidth). The Prelims data file is ~3 MB (≈0.8 MB gzipped).
- Offline: `public/sw.js` caches same-origin files after first load (optional; bump `VERSION` when data changes).

## Pages (PRD §3)

Home (subjects, start sequences, syllabus-content coverage, search) · Subject Roadmap (prerequisite order, stage/year filters) ·
Concept Detail (What / How / Where / Why) · PYQ Explorer (filters, provenance, backlinks) · Interlinkage Explorer (authored + derived links) ·
Sources & Coverage (resource catalog, audit, review queue) · optional “My saves” (localStorage, JSON export/import).

## Pipeline (reproducible)

`scripts/build_all.sh` rebuilds every derived file. Steps:

1. `parse_prelims.py` — `pdftotext -layout` text → questions, verbatim, with source page.
2. `ocr_pdf.sh` — 300 dpi + tesseract (psm 4) for the scanned Mains PDFs. A psm 6 pass (`ocr_pdf.sh <pdf> <dir> 6` into `../work/ocr_psm6`) was run only for the 14 papers whose first parse did not give 20 questions; it is used as a fallback.
3. `parse_mains.py` — filters out the Hindi text, splits questions, reconciles to the known 20-per-paper structure, flags every uncertainty, and applies `data/mains_manual.json` (hand transcriptions). Unattached fragments go to the review queue.
4. `build_syllabus.py` — splits the supplied syllabus into addressable points.
5. `author_all.py` — merges `author_polity.py` (Polity) and `author_subjects.py` (Economy, Geography, Environment, Modern History) and `author_subjects2.py` (Science & Technology, Art & Culture, Ancient/Medieval History, Society, Governance, IR, Security, Disaster) and emits concepts, resources and concept links. The authored content lives in those two files.
6. `build_data.py` — assembles questions, the review queue and the proposed PYQ links.
7. `audit.py` → `COVERAGE.md` and `data/coverage.json`; `validate.py` checks integrity.

`download_mains.sh <dir>` re-downloads the Mains PDFs from the URLs in `data/mains_sources.json`.
Requires `pdftotext`/`pdftoppm` (poppler), `tesseract`, Python 3, and macOS `/usr/share/dict/words` (used by the English-line filter).

## How to review (next step)

- `data/review_queue.json` / the Sources & Coverage page list flagged questions with the source file and page; compare with the PDF and fix `data/mains_manual.json` or the parser.
- Concepts: `scripts/author_polity.py` and `scripts/author_subjects.py` — check each concept against a textbook, then set `review_status`. Add verified chapters/editions to `RES` only when confirmed.
- Links: confirm or drop entries in `data/question_links.json` (they are regenerated by `build_data.py`; move accepted ones into an override file before re-running).

## Known limitations

- Keyword rules over-link and under-link; mapping is for navigation, not an answer key.
- Prelims subject/topic labels are the compiler's own.
- Concept pages are checklists, not notes; no textbook text is reproduced.


## Phase E: checking Prelims answers against official keys
The UPSC answer-key page (`/examinations/answer-key`) was reachable but its listing did not expose Civil Services Prelims key PDFs to automated fetching (only other examinations appeared), so no official keys were downloaded. Transcribe or download the keys yourself, put them in a JSON file (format in `scripts/check_keys.py`) and run `python3 -I scripts/check_keys.py data <keys.json>`; it writes `data/key_check.json` and never edits answers.
