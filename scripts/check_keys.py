"""Compare the supplied Prelims answers with an official-key file you provide. Writes data/key_check.json; never edits answers.
usage: python3 -I scripts/check_keys.py <data_dir> <official_keys.json>
official_keys.json: {"2023": {"1": "b", "2": "d", ...}, ...}  (transcribe from the UPSC answer-key PDF for the same question-paper set as the compilation;
UPSC prints several booklet sets, so say which set you used under the key "_set_note" per year if needed)."""
import sys, json, collections
data, keys_path = sys.argv[1], sys.argv[2]
qs = json.load(open(f"{data}/questions_prelims.json"))
keys = json.load(open(keys_path))
res = {"matches": 0, "mismatches": [], "no_official_key": 0, "years_checked": sorted(k for k in keys)}
for q in qs:
    y = keys.get(str(q["year"]))
    if not y:
        continue
    off = y.get(str(q["number"]))
    if off is None:
        res["no_official_key"] += 1
    elif (q["answer"] or "").lower() == off.lower():
        res["matches"] += 1
    else:
        res["mismatches"].append({"id": q["id"], "year": q["year"], "number": q["number"], "supplied": q["answer"], "official": off})
json.dump(res, open(f"{data}/key_check.json", "w"), indent=1)
print(f"matches {res['matches']} | mismatches {len(res['mismatches'])} | no official key for {res['no_official_key']} | years {res['years_checked']}")
