"""Parse OCR'd bilingual Mains GS papers into JSON (English text only).

Input: work/ocr/<paper>__pNN.txt (tesseract, eng) ; app/data/mains_sources.json
Question text is OCR output: kept as read (line breaks joined with a space),
never paraphrased. Every question carries source file/page and verification
'ocr-unverified'. Ambiguities are recorded in `flags` for the review queue.
usage: parse_mains.py <ocr_dir> <sources.json> <out.json>
"""
import json, re, sys, glob, os

STOP = set("the of and in to is are be that this it for on with as by which what how can has have from or their its not an these could would should do does you your at was were more between if when whether such any other into than also may will who they there been being those them our us we".split())
NUMMARK = re.compile(r"^(?:Q\s*)?(\d{1,2})\s*[.,)]\s*(.*)$")
# English end-of-question: line ends with the marks figure (10/12.5/15/20/25), optional OCR noise
END = re.compile(r"(?:^|[\s)\].?:;])(10|15|20|25|12\s?[\u00bd%]|12\.5|12\W{0,2}5)\s*[|.]?\s*$")
LONEMARKS = re.compile(r"^\s*(10|15|20|25)\s*$")
NOISE = re.compile(r"^(?:[A-Z]{2,5}-?[A-Z]?-?[A-Z]{2,4}(?:/\d+)?\s*\d*|\d+|SECTION\s+[AB]|P\.?T\.?O\.?)$", re.I)


def _load_words():
    try:
        return {w.strip().lower() for w in open("/usr/share/dict/words", encoding="utf-8", errors="ignore") if len(w.strip()) >= 4}
    except OSError:
        return set()


WORDS = _load_words()


def _is_word(t):
    if t in WORDS:
        return True
    for suf in ("s", "es", "ed", "ing", "ly", "d", "ment", "ments", "ions", "ion", "al"):
        if t.endswith(suf) and t[: -len(suf)] in WORDS:
            return True
    return False


def is_english(line, prev):
    toks = [t.lower() for t in re.findall(r"[A-Za-z]+", line)]
    cand = [t for t in toks if len(t) >= 3 or t in STOP]
    if len(cand) < 2:
        return prev  # too short to judge; inherit
    hits = sum(1 for t in cand if t in STOP or _is_word(t))
    return hits / len(cand) >= 0.6


def read_pages(ocr_dir, base):
    out = []
    for p in sorted(glob.glob(os.path.join(ocr_dir, base + "__p*.txt"))):
        n = int(re.search(r"__p(\d+)\.txt$", p).group(1))
        out.append((n, open(p, encoding="utf-8", errors="replace").read().split("\n")))
    return out


QMARK = re.compile(r"^Q\s*([0-9A-Za-z]{1,2})\s*[.,:]\s*(.*)$")
WORDLIM = re.compile(r"\(?\s*(?:Answer\s+in\s+)?(\d{2,3})\s*words?\s*[)\]}]?\s*[|.,]?\s*(10|15|20|25|12\s?[\u00bd%]|12\.5)?\s*$", re.I)


HINDI_TAIL = re.compile(r"^.{0,160}?\(\s*[^()\d]{0,6}\s*(?:150|250|1\.50|1 50|2\.50|750|7150|J50|\[50|I50)\s+[^()]{2,30}\)\s*")
CODE_PREFIX = re.compile(r"^\S*(?=[^\s]*[0-9])\S*[-/]\S*\s+(?:\d{1,2}\s+)?(?:\[?\s*P\.?T\.?O\.?,?\s*)?")


INSTR_SENT = re.compile(r"^[\s_\W]*Answer[_\s]*all.{0,260}?(equal[_\s]*marks|its[_\s]*length)\.?\s*(All questions carry equal marks\.?)?", re.I)


def clean(text, flags):
    t = text
    t = INSTR_SENT.sub("", t)
    t2 = re.sub(r"\[?\s*P\.?T\.?O\.?\s*[,.]?\s*", " ", t)
    t2 = CODE_PREFIX.sub("", t2)
    m = HINDI_TAIL.match(t2)
    if m and not re.search(r"word", m.group(0), re.I) and len(t2) - m.end() >= 25:
        t2 = t2[m.end():]
    toks = t2.split()
    wl = [(re.sub(r"[^a-z]", "", w.lower()) in STOP) or _is_word(re.sub(r"[^a-z]", "", w.lower())) for w in toks]
    for i in range(0, min(len(toks) - 3, 26)):
        if all(wl[i:i + 4]):
            if i >= 4 and sum(wl[:i]) / i < 0.35:
                t2 = " ".join(toks[i:]); flags.append("hindi-garble-prefix-trimmed")
            break
    if t2 != t and "ocr-noise-prefix-stripped" not in flags:
        flags.append("ocr-noise-prefix-stripped")
    return re.sub(r"\s+", " ", t2).strip()


G4MARK = re.compile(r"^(?:Q\s*)?(\d{1,2})\s*[.,]?\s*(?:\(\s*([a-cA-C0o])\s*\))?\s*[-.]?\s*(.*)$")


def parse_gs4(pages):
    """GS4: one unit per numbered question; parts (a)/(b) and case-study sub-questions stay inside the text."""
    units, cur, cur_n = [], None, 0
    eng_state = False

    def finish(c):
        text = clean(re.sub(r"\s+", " ", " ".join(c["eng"])).strip(), c["flags"])
        units.append({"num": c["num"], "part": None, "page": c["page"], "text": text, "marks": None, "limit": None, "flags": c["flags"]})

    for pno, lines in pages:
        if pno == 1:
            continue
        for raw in lines:
            s = raw.strip()
            if not s:
                continue
            qm = re.match(r"^Q\s*([0-9A-Za-z|]{1,2})\s*[.,:]\s*(?:\(\s*([a-cA-C0o])\s*\))?\s*(.*)$", s)
            dm = None if qm else re.match(r"^(\d{1,2})\s*[.,]?\s*(?:\(\s*([a-cA-C0o])\s*\))?\s*[-.]?\s*(.*)$", s)
            m = qm or dm
            if m:
                g = m.group(1)
                n = int(g) if g.isdigit() else cur_n + 1
                is_start = n == cur_n + 1 and (qm or m.group(2) or not re.match(r"^\d{1,2}\s*[.,]?\s*$", s) or True)
                if is_start and (qm or re.match(r"^\d{1,2}\s*[.,]|^\d{1,2}\s*\(", s)):
                    if cur is not None and cur["eng"]:
                        finish(cur)
                    cur = {"num": n, "page": pno, "eng": [], "flags": [] if g.isdigit() else ["ocr-number-char-uncertain"]}
                    cur_n, eng_state = n, False
                    s = m.group(3).strip()
                    if m.group(2):
                        s = "(" + {"o": "b", "0": "b"}.get(m.group(2).lower(), m.group(2).lower()) + ") " + s if s else s
                    if not s:
                        continue
            if cur is None or NOISE.match(s):
                continue
            eng_state = is_english(s, eng_state)
            if eng_state and not LONEMARKS.match(s):
                cur["eng"].append(s)
    if cur is not None and cur["eng"]:
        finish(cur)
    return units


def parse_paper(pages, paper):
    if paper == "GS-4":
        return parse_gs4(pages)
    is4 = False
    qs, cur, expected = [], None, 1
    pending = []  # numbers seen in marker groups whose English text comes later, unnumbered
    eng_state = False

    def new(num, page, flags=()):
        return {"num": num, "page": page, "eng": [], "marks": None, "limit": None, "flags": list(flags)}

    def finish(c, why=None):
        if why:
            c["flags"].append(why)
        text = re.sub(r"\s+", " ", " ".join(c["eng"])).strip()
        text = clean(text, c["flags"])
        qs.append({"num": c["num"], "page": c["page"], "text": text, "marks": c["marks"], "limit": c["limit"], "flags": c["flags"]})

    for pno, lines in pages:
        if pno == 1:
            continue  # cover / instructions page
        for raw in lines:
            s = raw.strip()
            if not s:
                continue
            qm, nm = QMARK.match(s), NUMMARK.match(s)
            rest = None
            if qm:
                rest, n = qm.group(2), (int(qm.group(1)) if qm.group(1).isdigit() else expected)
            elif nm and int(nm.group(1)) == expected:
                rest, n = nm.group(2), expected
            if rest is not None:
                if cur is not None and cur["eng"]:
                    finish(cur, "closed-by-next-number")
                elif cur is not None:
                    pending.append(cur["num"])
                cur = new(n, pno, [] if n == expected else [f"number-mismatch(expected {expected})"])
                expected = n + 1
                eng_state = False
                s = rest.strip()
                if not s:
                    continue
            if NOISE.match(s):
                continue
            eng_state = is_english(s, eng_state)
            if not eng_state:
                continue
            if cur is None and qs and re.fullmatch(r"\(?\s*Answer\s+in\s+\d{2,3}\s*words?\s*\)?\s*", s, re.I):
                qs[-1]["limit"] = int(re.search(r"\d{2,3}", s).group(0))
                qs[-1]["text"] += " " + s
                continue
            if cur is None:
                if pending:
                    cur = new(pending.pop(0), pno, ["number-from-marker-group"])
                else:
                    cur = new(expected, pno, ["number-inferred"])
                    expected += 1
            elif not cur["eng"] and pending:
                pending.append(cur["num"]); pending.sort()
                cur["num"] = pending.pop(0); cur["flags"].append("number-from-marker-group")
            lm = LONEMARKS.match(s)
            if lm:
                if cur["eng"] and cur["marks"] is None:
                    cur["marks"] = int(lm.group(1))
                continue
            cur["eng"].append(s)
            if is4:
                continue
            wl, em = WORDLIM.search(s), END.search(s)
            if wl:
                cur["limit"] = int(wl.group(1))
                if wl.group(2):
                    cur["marks"] = 12.5 if wl.group(2).startswith("12") else int(wl.group(2))
                finish(cur); cur = None
            elif em:
                mk = em.group(1)
                cur["marks"] = 12.5 if mk.startswith("12") else int(mk)
                finish(cur); cur = None
    if cur is not None and cur["eng"]:
        finish(cur, "unterminated")
    return qs


INSTR = re.compile(r"(All questions carry|questions? (are )?compulsory|NOT MORE THAN \d+ words each|equal marks)", re.I)


def looks_like_question(text):
    toks = re.findall(r"[A-Za-z]+", text)
    return len(toks) >= 8 and sum(1 for t in toks if len(t) > 2) / max(len(toks), 1) > 0.6


def _key(t):
    return re.sub(r"[^a-z]", "", t.lower())[:50]


def _dedupe(qs):
    seen, out = set(), []
    for q in qs:
        k = _key(q["text"])
        if k in seen:
            continue
        seen.add(k); out.append(q)
    return out


def reconcile(primary, alt_pages, paper, frags, src):
    """GS1-3 have exactly 20 questions in order. Prefer the parse (primary psm4, else alt psm6) that yields
    exactly 20 distinct questions and number them by order of appearance; otherwise merge by marker number."""
    P = _dedupe([q for q in primary if looks_like_question(q["text"])])
    A = _dedupe([q for q in parse_paper(alt_pages, paper) if looks_like_question(q["text"])]) if alt_pages else []
    pick = None
    if len(P) == 20:
        pick, tag = P, None
    elif len(A) == 20:
        pick, tag = A, "text-from-alt-ocr-psm6"
    if pick:
        for i, q in enumerate(pick, 1):
            if q["num"] != i:
                q["flags"].append(f"renumbered-by-order(was {q['num']})")
            if tag:
                q["flags"].append(tag)
            q["num"] = i
        return pick
    have = {q["num"] for q in P if 1 <= q["num"] <= 20}
    for aq in A:
        if aq["num"] not in have and 1 <= aq["num"] <= 20:
            aq["flags"].append("recovered-from-alt-ocr-psm6"); P.append(aq); have.add(aq["num"])
    gaps = [n for n in range(1, 21) if n not in have]
    for q in sorted((q for q in P if q["num"] > 20), key=lambda q: q["num"]):
        if gaps:
            q["flags"].append(f"number-reassigned-to-fill-gap(was {q['num']})"); q["num"] = gaps.pop(0)
    return P


def main(ocr_dir, srcs, out, alt_dir=None):
    sources = json.load(open(srcs))
    res, frags = [], []
    seen_ids = {}
    for s in sources:
        base = s["file"][:-4]
        pages = read_pages(ocr_dir, base)
        qs = parse_paper(pages, s["paper"])
        if s["paper"] != "GS-4":
            qs = reconcile(qs, read_pages(alt_dir, base) if alt_dir else [], s["paper"], frags, s)
        for q in qs:
            flags = list(q["flags"])
            if not looks_like_question(q["text"]):
                frags.append({"source_file": s["file"], "year": s["year"], "paper": s["paper"], "source_page": q["page"],
                              "number_guess": q["num"], "text": q["text"], "reason": "too-short-or-noisy-to-be-a-question"})
                continue
            head = q["text"][:70]
            toks = [t.lower() for t in re.findall(r"[A-Za-z]+", head) if len(t) >= 3 or t.lower() in STOP]
            if toks and sum(1 for t in toks if t in STOP or _is_word(t)) / len(toks) < 0.5:
                flags.append("possible-hindi-garble-prefix")
            if s["paper"] == "GS-4":
                flags.append("gs4-layout-manual-review")
                if len(q["text"]) > 2500:
                    flags.append("likely-multiple-case-studies-merged")
            marks, mflag = q["marks"], None
            lim = q["limit"]
            if s["paper"] != "GS-4":
                if marks is None:
                    if lim in (150, 250):
                        marks, mflag = {150: 10, 250: 15}[lim], "marks-derived-from-word-limit"
                    else:
                        mflag = "marks-missing"
                if marks in (10, 15) and lim not in (150, 250) and "ocr-wordlimit-normalised" not in flags:
                    lim = {10: 150, 15: 250}[marks]; flags.append("ocr-wordlimit-normalised")
            if mflag:
                flags.append(mflag)
            qid = f"M-{s['year']}-{s['paper'][-1]}-{q['num']:02d}" + (q.get("part") or "")
            k = seen_ids.get(qid, 0)
            seen_ids[qid] = k + 1
            if k:
                flags.append(f"duplicate-number-{k+1}"); qid += "-" + "abcdefg"[k]
            res.append({
                "id": qid, "stage": "Mains", "paper": s["paper"], "year": s["year"], "number": q["num"],
                "text": q["text"], "marks": marks, "word_limit": lim,
                "source_file": s["file"], "source_page": q["page"], "source_url": s["url"],
                "verification": "ocr-unverified", "flags": flags,
            })
    manual_path = os.path.join(os.path.dirname(srcs), "mains_manual.json")
    if os.path.exists(manual_path):
        srcmap = {(x["year"], x["paper"]): x for x in sources}
        for m in json.load(open(manual_path)):
            s = srcmap[(m["year"], m["paper"])]
            qid = f"M-{m['year']}-{m['paper'][-1]}-{m['number']:02d}"
            res = [r for r in res if r["id"] != qid]  # a hand transcription from the page image replaces a partial/missing OCR parse
            res.append({"id": qid, "stage": "Mains", "paper": m["paper"], "year": m["year"], "number": m["number"],
                        "text": m["text"], "marks": m["marks"], "word_limit": m["word_limit"],
                        "source_file": s["file"], "source_page": m["source_page"], "source_url": s["url"],
                        "verification": "manually-transcribed-unverified", "flags": ["manually-transcribed-from-image"], "note": m["note"]})
    res.sort(key=lambda r: (r["year"], r["paper"], r["number"]))
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    json.dump(frags, open(out.replace(".json", "_fragments.json"), "w"), ensure_ascii=False, indent=1)
    print(len(res), "questions;", sum(1 for r in res if r["flags"]), "flagged;", len(frags), "fragments")


main(*sys.argv[1:5])
