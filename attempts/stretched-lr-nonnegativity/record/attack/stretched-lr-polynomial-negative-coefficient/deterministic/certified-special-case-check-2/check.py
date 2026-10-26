#!/usr/bin/env python3
"""Checker for the certified special-case check of the 6-part box.

1. The summary must report as many records as enumeration-run-3 holds polynomials, and
   zero mismatches between the lrcalc interpolation (t = 0..10) and the Normaliz polynomials.
2. Third implementation on a sample: for 30 seeded random records whose value at t = 10 is
   at most 200,000, recount c^{t lam}_{t mu, t nu} for t = 0..10 by the lattice-word counter
   lrtableaux.py (no lrcalc, no Normaliz, no hive code), interpolate by a Lagrange formula
   written here, and compare with the recorded polynomial.
Exit 0 iff both hold.
"""
import gzip
import json
import os
import random
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enumeration-run-3"))
from lrtableaux import count_lr_tableaux  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RUN3 = os.path.join(HERE, "..", "enumeration-run-3", "scan-n6.jsonl.gz")

summary = json.load(open(os.path.join(HERE, "verify6.summary.json")))
recs = []
with gzip.open(RUN3, "rt") as f:
    for line in f:
        r = json.loads(line)
        if "num" in r:
            recs.append(r)
bad = 0
if summary["records"] != len(recs) or summary["mismatches"] != 0 or summary["agree"] != len(recs):
    bad += 1
    print(f"SUMMARY MISMATCH: summary {summary}, run-3 polynomials {len(recs)}")
else:
    print(f"summary: {summary['records']} records pinned by lrcalc at t = 0..{summary['degree_bound']}, 0 mismatches")


def lagrange(values):
    m = len(values)
    poly = [Fraction(0)] * m
    for i in range(m):
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


def recorded(r):
    p = [Fraction(x, r["den"]) for x in r["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(p, t):
    return sum(c * Fraction(t) ** i for i, c in enumerate(p))


rng = random.Random(20260904)
small = [r for r in recs if evalp(recorded(r), 10) <= 200_000]
sample = rng.sample(small, min(30, len(small)))
sbad = 0
for r in sample:
    lam, mu, nu = r["lam"], r["mu"], r["nu"]
    values = [count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1 for t in range(11)]
    if lagrange(values) != recorded(r):
        sbad += 1
        print(f"THIRD-IMPLEMENTATION MISMATCH {lam} {mu} {nu}")
bad += sbad
print(f"third implementation (lattice-word counter + Lagrange, t = 0..10): {len(sample)} records, {sbad} mismatches")
sys.exit(1 if bad else 0)
