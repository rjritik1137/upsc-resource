"""Driver: merges the Polity pilot and the batch-1 subjects, resolves cross-subject stubs, writes data/*.json.
usage: python3 scripts/author_all.py <data_dir>   (authoring scripts read no untrusted input, so no -I here)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import author_polity as P
import author_subjects as S
import author_subjects2 as S2
import author_subjects3 as S3
import author_subjects4 as S4

S.STUB_RESOLVE.update({
    'xs-governance-rti': 'governance-transparency-e-governance-citizens-charter',
    'xs-governance-civil-services': 'governance-civil-services-role',
    'xs-society-social-justice': 'governance-vulnerable-sections-welfare',
    'xs-security-internal': 'security-external-actors-extremism',
})
S.SUBJECT_META.update(S2.SUBJECT_META)
S.SUBJECT_META.update(S3.SUBJECT_META)
S.RATIONALE.update(S3.RATIONALE)
S.RATIONALE.update(S4.RATIONALE)
S.RATIONALE.update(S2.RATIONALE)

for c in P.CONCEPTS:
    c["cross_subject"] = [S.STUB_RESOLVE.get(x, x) for x in c["cross_subject"]]
P.STUBS[:] = [t for t in P.STUBS if t[0] not in S.STUB_RESOLVE]
P.RATIONALE.update(S.RATIONALE)
for sub in P.SUBJECTS:
    if sub["id"] in S.SUBJECT_META:
        title, status, papers = S.SUBJECT_META[sub["id"]]
        sub.update(title=title, status=status, papers=papers, groups=[dict(id=g, title=t) for g, t in S.GROUPS[sub["id"]]])
P.main(sys.argv[1])
