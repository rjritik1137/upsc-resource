"""Split the supplied official syllabus text into addressable items (S-<paper>-NN).
usage: build_syllabus.py <syllabus.txt> <out.json>"""
import json, re, sys

lines = [re.sub(r"[ \t]+", " ", l).rstrip() for l in open(sys.argv[1], encoding="utf-8", errors="replace").read().replace("\f", "\n").split("\n")]
SECTIONS = [  # (key, stage, paper label, start regex, end regex)
    ("P1", "Prelims", "GS-I", r"^Paper I - \(200 marks\)", r"^Paper II-\(200 marks\)"),
    ("GS1", "Mains", "GS-I", r"^General Studies-\s*I:", r"^PAPER-III"),
    ("GS2", "Mains", "GS-II", r"^General Studies-\s*II:", r"^PAPER-IV"),
    ("GS3", "Mains", "GS-III", r"^General Studies-\s*III:", r"^PAPER-V"),
    ("GS4", "Mains", "GS-IV", r"^General Studies-\s*IV:", r"^\Z"),
]
BUL = re.compile(r"^\s*[••]\s*(.*)$")
out = []
for key, stage, paper, a, b in SECTIONS:
    i = next(i for i, l in enumerate(lines) if re.match(a, l.strip()))
    title = lines[i].strip()
    items, cur = [], None
    for l in lines[i + 1:]:
        s = l.strip()
        if re.match(b, s) and s:
            break
        if not s or re.fullmatch(r"\d{1,3}", s):
            continue
        m = BUL.match(l)
        if m:
            cur = [m.group(1).strip()]; items.append(cur)
        elif cur is not None:
            cur.append(s)
        elif key in ("GS4",):
            cur = [s]; items.append(cur)
    for n, it in enumerate(items, 1):
        out.append({"id": f"S-{key}-{n:02d}", "stage": stage, "paper": paper, "section_title": title,
                    "text": re.sub(r"\s+", " ", " ".join(it)).strip(), "source": "syllabus.pdf (supplied)"})
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(o["id"].rsplit("-", 1)[0] for o in out))
