#!/usr/bin/env python3
"""Checker for the certified special-case check of the 5-part box.

1. The summary must report as many records as enumeration-run-2 holds polynomials, and
   zero mismatches between the lrcalc interpolation and the Normaliz polynomials.
2. Third implementation on a sample: for 300 seeded random records and the records with
   the smallest linear coefficient, recount c^{t lam}_{t mu, t nu} for t = 0..6 by the
   classical lattice-word counter lrtableaux.py (no lrcalc, no Normaliz, no hive code),
   interpolate with an interpolation written here (Lagrange, not the Newton code of
   verify5.py), and compare with the recorded polynomial.
Exit 0 iff both hold.
"""
import glob
import json
import os
import random
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enumeration-run-2"))
from lrtableaux import count_lr_tableaux  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")

summary = json.load(open(os.path.join(HERE, "verify5.summary.json")))
recs = []
for fn in sorted(glob.glob(os.path.join(RUN2, "scan-n5-*.jsonl"))):
    with open(fn) as f:
        for line in f:
            r = json.loads(line)
            if "coeffs" in r:
                recs.append(r)
bad = 0
if summary["records"] != len(recs) or summary["mismatches"] != 0 or summary["agree"] != len(recs):
    bad += 1
    print(f"SUMMARY MISMATCH: summary {summary}, run-2 polynomials {len(recs)}")
else:
    print(f"summary: {summary['records']} records pinned by lrcalc at t = 0..{summary['degree_bound']}, 0 mismatches")


def lagrange(values):
    """Monomial coefficients of the polynomial through (t, values[t]), t = 0..m-1."""
    m = len(values)
    poly = [Fraction(0)] * m
    for i in range(m):
        # basis polynomial prod_{j != i} (t - j) / (i - j)
        num = [Fraction(1)]
        den = Fraction(1)
        for j in range(m):
            if j == i:
                continue
            new = [Fraction(0)] * (len(num) + 1)
            for k, b in enumerate(num):
                new[k] -= j * b
                new[k + 1] += b
            num = new
            den *= (i - j)
        for k, b in enumerate(num):
            poly[k] += Fraction(values[i]) * b / den
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


rng = random.Random(20260904)
sample = {}
for r in rng.sample(recs, min(300, len(recs))):
    sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r
for r in sorted(recs, key=lambda r: Fraction(r["a1"]))[:10]:
    sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r
sbad = 0
for (lam, mu, nu), r in sample.items():
    values = [count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1 for t in range(7)]
    poly = lagrange(values)
    if poly != [Fraction(x) for x in r["coeffs"]]:
        sbad += 1
        print(f"THIRD-IMPLEMENTATION MISMATCH {lam} {mu} {nu}: {[str(x) for x in poly]} vs {r['coeffs']}")
bad += sbad
print(f"third implementation (lattice-word counter + Lagrange): {len(sample)} records, {sbad} mismatches")
sys.exit(1 if bad else 0)
