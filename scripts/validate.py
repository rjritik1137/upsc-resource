"""Validate the shipped data. Exit code 1 on any hard failure. usage: validate.py [data_dir]"""
import json, sys, os, collections
d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "data")
L = lambda n: json.load(open(os.path.join(d, n + ".json"), encoding="utf-8"))
P, M, C, R = L("questions_prelims"), L("questions_mains"), L("concepts"), L("resources")
CL, QL, S, ST = L("concept_links"), L("question_links"), L("syllabus"), L("concept_stubs")
errs, warns = [], []
def chk(c, m): (errs if not c else []).append(m) if not c else None
ids = lambda xs: [x["id"] for x in xs]
for name, xs in [("prelims", P), ("mains", M), ("concepts", C), ("resources", R), ("syllabus", S)]:
    dup = [k for k, v in collections.Counter(ids(xs)).items() if v > 1]
    chk(not dup, f"duplicate ids in {name}: {dup[:5]}")
qid, cid, rid, sid = set(ids(P) + ids(M)), set(ids(C)), set(ids(R)), set(ids(S))
stub = set(ids(ST))
for q in P:
    chk(len(q["options"]) == 4 or any(f.startswith("options=") for f in q["flags"]), f"{q['id']}: option count unflagged")
    chk(q["answer"] in (None, "a", "b", "c", "d"), f"{q['id']}: bad answer")
    chk(q["answer"] is not None or q["flags"], f"{q['id']}: no answer and no flag")
    chk(q["source_page"] and q["source_file"], f"{q['id']}: missing provenance")
for q in M:
    chk(q["source_file"] and q["source_page"], f"{q['id']}: missing provenance"); chk(q["text"], f"{q['id']}: empty text")
for c in C:
    for k in ("definition", "subconcepts", "foundation_focus", "mains_focus", "resource_ids", "syllabus_ids"):
        chk(c.get(k), f"{c['id']}: empty {k}")
    if len(c["subconcepts"]) < 5: warns.append(f"{c['id']}: only {len(c['subconcepts'])} subconcepts (PRD says 5-15)")
    chk(len(c["subconcepts"]) <= 15, f"{c['id']}: >15 subconcepts")
    chk(all(p in cid for p in c["prerequisites"]), f"{c['id']}: unknown prerequisite")
    chk(all(r in rid for r in c["resource_ids"]), f"{c['id']}: unknown resource")
    chk(all(s in sid for s in c["syllabus_ids"]), f"{c['id']}: unknown syllabus id")
    chk(all(x in stub or x in cid for x in c["cross_subject"]), f"{c['id']}: unknown cross-subject target")
# DAG
g = {c["id"]: c["prerequisites"] for c in C}; state = {}
def dfs(n, path):
    state[n] = 1
    for m in g[n]:
        if state.get(m) == 1: errs.append("prerequisite cycle: " + " -> ".join(path + [n, m])); continue
        if m not in state: dfs(m, path + [n])
    state[n] = 2
for n in g:
    if n not in state: dfs(n, [])
tgt = cid | sid | stub
for l in CL:
    chk(l["source"] in cid and l["target"] in tgt, f"link {l['id']}: dangling")
    chk(l["rationale"] and l["evidence"], f"link {l['id']}: missing rationale/evidence")
for l in QL:
    chk(l["question_id"] in qid and l["concept_id"] in cid, f"qlink dangling {l}")
    chk(l["status"] == "proposed", f"qlink not marked proposed: {l['question_id']}")
qc = collections.Counter(l["concept_id"] for l in QL)
for c in C:
    chk(qc[c["id"]] or c["syllabus_ids"], f"{c['id']}: no PYQ or syllabus link")
    if not qc[c["id"]]: warns.append(f"{c['id']}: no PYQ link in supplied data (syllabus link only)")
print(f"{len(P)} prelims, {len(M)} mains, {len(C)} concepts, {len(CL)} concept links, {len(QL)} question links")
for w in warns: print("WARN", w)
for e in errs: print("ERROR", e)
print("FAILED" if errs else "OK"); sys.exit(1 if errs else 0)
