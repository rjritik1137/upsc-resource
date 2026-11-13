"""Driver: merges the Polity pilot and the batch-1 subjects, resolves cross-subject stubs, writes data/*.json.
usage: python3 scripts/author_all.py <data_dir>   (authoring scripts read no untrusted input, so no -I here)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import author_polity as P
import author_subjects as S
import author_subjects2 as S2
import author_subjects3 as S3
import author_subjects4 as S4
import author_subjects5 as S5
import author_subjects6 as S6

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
S.RATIONALE.update(S6.RATIONALE)
S.RATIONALE.update(S2.RATIONALE)

for c in P.CONCEPTS:
    c["cross_subject"] = [S.STUB_RESOLVE.get(x, x) for x in c["cross_subject"]]
P.STUBS[:] = [t for t in P.STUBS if t[0] not in S.STUB_RESOLVE]
P.RATIONALE.update(S.RATIONALE)
for sub in P.SUBJECTS:
    if sub["id"] in S.SUBJECT_META:
        title, status, papers = S.SUBJECT_META[sub["id"]]
        sub.update(title=title, status=status, papers=papers, groups=[dict(id=g, title=t) for g, t in S.GROUPS[sub["id"]]])

# Corrections of syllabus ids after checking data/syllabus.json (some batch 2-6 guesses pointed at the wrong item)
SYL_FIX = {
    "economy-subsidies-direct-transfers": ["S-GS3-05", "S-GS3-03"],
    "economy-msme-startups-manufacturing": ["S-GS3-08", "S-GS3-01", "S-P1-05"],
    "economy-energy-sector-economy": ["S-GS3-09", "S-GS3-01"],
    "economy-agriculture-marketing-pricing-credit": ["S-GS3-05", "S-GS3-07", "S-P1-05"],
    "geography-geomorphic-processes-landforms": ["S-GS1-10", "S-P1-03"],
    "geography-climate-phenomena-enso-jetstreams": ["S-GS1-10", "S-P1-03"],
    "geography-world-climate-regions-biomes": ["S-GS1-10", "S-P1-03"],
    "geography-world-regional-geography-features": ["S-GS1-10", "S-P1-03"],
    "geography-global-resources-distribution": ["S-GS1-11", "S-GS1-10", "S-P1-03"],
    "geography-indian-energy-industry-regions": ["S-GS1-11", "S-P1-03"],
    "geography-human-geography-settlements-migration": ["S-GS1-07", "S-P1-03"],
    "geography-india-map-locations": ["S-P1-03"],
    "geography-remote-sensing-gis-maps": ["S-GS1-10", "S-GS3-11", "S-P1-03"],
    "environment-species-conservation-iucn-cites": ["S-P1-06", "S-GS3-14"],
    "environment-forest-resources-policy": ["S-P1-06", "S-GS3-14"],
    "environment-marine-coastal-crz": ["S-P1-06", "S-GS3-14"],
    "environment-invasive-species-human-wildlife-conflict": ["S-P1-06", "S-GS3-14"],
    "environment-carbon-markets-climate-finance": ["S-P1-06", "S-GS3-14"],
    "environment-environmental-organisations-indices": ["S-P1-06", "S-GS3-14"],
    "environment-sustainable-development-green-economy": ["S-P1-06", "S-GS3-14", "S-GS3-01"],
    "history-maratha-sikh-regional-powers": ["S-P1-02"],
    "governance-food-security-pds": ["S-GS2-14", "S-GS3-05", "S-GS2-12"],
    "disaster-climate-risk-resilience": ["S-GS3-15", "S-GS3-14"],
}
for c in P.CONCEPTS:
    if c["id"] in SYL_FIX:
        c["syllabus_ids"] = SYL_FIX[c["id"]]
P.main(sys.argv[1])
