#!/usr/bin/env python3
"""Checker for the certified special-case check of the 7-part box.

1. The summary of verify7.py must report as many records as enumeration-run-4 holds
   polynomials, agreement of the tableau-polytope encoding on every record, agreement of
   lrcalc (t = 1 on every record, t = 2 when P(2) <= 1,000,000) on every record, and zero
   mismatches; the mismatch file must be empty.
2. The second encoding re-run on a seeded sample: for 300 seeded random records, the 10
   records with the smallest coefficient ratio, and the 3 records of largest dimension, the
   Ehrhart polynomial of the tableau polytope is recomputed here (tableau_polytope.py,
   Normaliz) and compared with the recorded hive-encoding polynomial.
3. Third implementation on a sample: for 30 seeded random records with P(3) <= 300,000,
   c^{t lam}_{t mu, t nu} for t = 0..3 is recounted by the lattice-word counter
   lrtableaux.py (no lrcalc, no Normaliz, no hive code) and compared with the values of the
   recorded polynomial (consistency at four points; a 7-part polynomial has degree up to 13,
   so these points do not pin it).
Exit 0 iff all hold.
"""
import gzip
import json
import os
import random
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lrtableaux import count_lr_tableaux  # noqa: E402
from tableau_polytope import ehrhart_tableau  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RUN4 = os.path.join(HERE, "..", "enumeration-run-4", "scan-n7.jsonl.gz")


def recorded(r):
    p = [Fraction(x, r["den"]) for x in r["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(p, t):
    return sum(c * Fraction(t) ** i for i, c in enumerate(p))


summary = json.load(open(os.path.join(HERE, "verify7.summary.json")))
recs = []
with gzip.open(RUN4, "rt") as f:
    for line in f:
        r = json.loads(line)
        if "num" in r:
            recs.append(r)
bad = 0
n = len(recs)
mismatch_lines = sum(1 for _ in open(os.path.join(HERE, "verify7.mismatches.jsonl")))
if (summary["records"] != n or summary["tableau_agree"] != n or summary["lrcalc_agree"] != n
        or summary["mismatches"] != 0 or mismatch_lines != 0):
    bad += 1
    print(f"SUMMARY MISMATCH: summary {summary}, run-4 polynomials {n}, mismatch lines {mismatch_lines}")
else:
    print(f"summary: {n} records, tableau encoding agrees on {summary['tableau_agree']}, "
          f"lrcalc agrees on {summary['lrcalc_agree']} (t = 2 checked on {summary['t2_checked']}), 0 mismatches")

rng = random.Random(20260904)
sample = rng.sample(recs, 300)
sample += sorted(recs, key=lambda r: Fraction(r["minr"]))[:10]
sample += sorted(recs, key=lambda r: -r["dim"])[:3]
ebad = 0
for r in sample:
    if ehrhart_tableau(r["lam"], r["mu"], r["nu"])[1] != recorded(r):
        ebad += 1
        print(f"SECOND-ENCODING MISMATCH {r['lam']} {r['mu']} {r['nu']}")
bad += ebad
print(f"second encoding re-run (tableau polytope, Normaliz): {len(sample)} records, {ebad} mismatches")

small = [r for r in recs if evalp(recorded(r), 3) <= 300_000]
sample3 = rng.sample(small, min(30, len(small)))
sbad = 0
for r in sample3:
    lam, mu, nu = r["lam"], r["mu"], r["nu"]
    p = recorded(r)
    for t in range(4):
        v = count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1
        if v != evalp(p, t):
            sbad += 1
            print(f"THIRD-IMPLEMENTATION MISMATCH {lam} {mu} {nu} t={t} count={v} poly={evalp(p, t)}")
            break
bad += sbad
print(f"third implementation (lattice-word counter, t = 0..3): {len(sample3)} records, {sbad} mismatches")
sys.exit(1 if bad else 0)
