"""Parse the supplied Prelims compilation (pdftotext -layout output) into JSON.

Preserves question text verbatim (line breaks kept, per-line whitespace trimmed),
records source file/page, and flags anything ambiguous for manual review.
usage: parse_prelims.py <prelims.txt> <out.json>
"""
import json, re, sys

SRC = "upsc-prelims-complete.pdf"
HDR = re.compile(r"^UPSC (\d{4})\s+(.+?)\s*(?:›\s*(.+))?$")
QRE = re.compile(r"^Q(\d+)\.\s*(.*)$")
OPT = re.compile(r"^\(([a-d])\)\s*(.*)$")
ANS = re.compile(r"^Answer:\s*(.*)$")
FOOT = re.compile(r"^UnlockIAS\b")


def main(src, out):
    raw = open(src, encoding="utf-8", errors="replace").read()
    pages = raw.split("\f")
    items, cur, hdr = [], None, None
    for pno, ptxt in enumerate(pages, start=1):
        for line in ptxt.split("\n"):
            s = line.strip()
            if not s or FOOT.match(s):
                continue
            m = HDR.match(s)
            if m:
                hdr = {"year": int(m.group(1)), "subject_label": m.group(2).strip(), "topic_label": (m.group(3) or "").strip()}
                continue
            m = QRE.match(s)
            if m:
                cur = {"number": int(m.group(1)), "page": pno, "hdr": hdr, "text": [m.group(2)], "options": [], "answer_raw": None, "_mode": "q"}
                hdr = None if hdr is None else hdr
                items.append(cur)
                continue
            if cur is None:
                continue
            m = ANS.match(s)
            if m:
                cur["answer_raw"] = m.group(1).strip(); cur["_mode"] = "done"; continue
            if cur["_mode"] == "done":
                continue
            m = OPT.match(s)
            if m:
                cur["options"].append([m.group(1), m.group(2)]); cur["_mode"] = "o"; continue
            if cur["_mode"] == "o":
                cur["options"][-1][1] += " " + s
            else:
                cur["text"].append(s)
    result, year_counter = [], {}
    for it in items:
        h = it["hdr"] or {}
        year = h.get("year")
        flags = []
        if year is None:
            flags.append("no-header")
        a = it["answer_raw"] or ""
        m = re.fullmatch(r"\(([a-d])\)", a)
        if m:
            ans, status = m.group(1), "supplied"
        elif a.lower().startswith("cancelled"):
            ans, status = None, "cancelled"; flags.append("cancelled-by-upsc")
        else:
            ans, status = None, "unresolved"; flags.append("answer-note:" + a[:80])
        if len(it["options"]) != 4:
            flags.append(f"options={len(it['options'])}")
        result.append({
            "stage": "Prelims", "paper": "GS-I", "year": year, "number": it["number"],
            "subject_label": h.get("subject_label"), "topic_label": h.get("topic_label"),
            "text": "\n".join(it["text"]).strip(),
            "options": [{"key": k, "text": t.strip()} for k, t in it["options"]],
            "answer": ans, "answer_status": status, "answer_note": a if status != "supplied" else None,
            "source_file": SRC, "source_page": it["page"],
            "verification": "parsed-unverified", "flags": flags,
        })
    for r in result:
        r["id"] = f"P-{r['year']}-{r['number']:03d}" if r["year"] else f"P-NOYEAR-{r['source_page']}-{r['number']}"
    json.dump(result, open(out, "w"), ensure_ascii=False, indent=1)
    print(len(result), "questions;", sum(1 for r in result if r["flags"]), "flagged")


main(sys.argv[1], sys.argv[2])
