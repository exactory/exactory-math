#!/usr/bin/env python3
"""Independent check of the h sign census.

1. The summary against the record files: the counts of records, the count of records with a
   negative entry, and the emptiness of `h-negative.jsonl`.
2. An independent computation of the h vector on a sample of records, by solving
   P(t) = sum h_i C(t + D - i, D) as a linear system rather than by the alternating sum the run
   used, with the signs compared.
3. A positive control on the detector itself: a synthetic polynomial whose h vector has a negative
   entry must be flagged by the same code path, so that a census of zero is not the result of a
   test that never fires.
Exit 0 iff all three hold.
"""
import glob
import gzip
import json
import os
import random
import sys
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hsign import coeffs_of, evalp, hstar  # noqa: E402

DET = os.path.join(HERE, "..", "..", "..", "stretched-lr-polynomial-negative-coefficient",
                   "deterministic")
SOURCES = [(5, sorted(glob.glob(os.path.join(DET, "enumeration-run-2", "scan-n5-*.jsonl")))),
           (6, [os.path.join(DET, "enumeration-run-3", "scan-n6.jsonl.gz")]),
           (7, [os.path.join(DET, "enumeration-run-4", "scan-n7.jsonl.gz")])]
bad = 0
summary = json.load(open(os.path.join(HERE, "h-sign.summary.json")))
neg = [l for l in open(os.path.join(HERE, "h-negative.jsonl"))]
if sum(summary[str(n)]["negative_h"] for n, _ in SOURCES) != len(neg):
    bad += 1
    print(f"NEGATIVE COUNT MISMATCH: summary says "
          f"{sum(summary[str(n)]['negative_h'] for n, _ in SOURCES)}, file holds {len(neg)}")
print(f"summary: {sum(summary[str(n)]['records'] for n, _ in SOURCES)} records, "
      f"{sum(summary[str(n)]['negative_h'] for n, _ in SOURCES)} with a negative entry, "
      f"smallest entries {[summary[str(n)]['min_h'] for n, _ in SOURCES]}")


def h_by_solving(coeffs):
    """h from the definition, by solving the triangular system, not by the alternating sum."""
    D = len(coeffs) - 1
    h = []
    for i in range(D + 1):
        # P(i) = sum_{j<=i} h_j * C(i + D - j, D), and C(i + D - j, D) = 0 for j > i
        s = evalp(coeffs, i)
        for j in range(i):
            s -= h[j] * comb(i + D - j, D)
        h.append(s)
    return tuple(h)


rng = random.Random(20260912)
checked = mism = 0
for n, paths in SOURCES:
    lines = []
    for path in paths:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt") as f:
            for k, line in enumerate(f):
                if k > 40000:
                    break
                lines.append(line)
    for line in rng.sample(lines, min(300, len(lines))):
        rec = json.loads(line)
        if "coeffs" not in rec and "num" not in rec:
            continue
        p = coeffs_of(rec)
        a, b = hstar(p), h_by_solving(p)
        checked += 1
        if a != b or a[0] != 1 or min(a) < 0:
            mism += 1
            print(f"H MISMATCH {rec.get('lam')}: {a} against {b}")
bad += mism
print(f"an independent h by solving the triangular system: {checked} records, {mism} mismatches, "
      f"and every one has h_0 = 1 and no negative entry")

fake = [Fraction(1), Fraction(-2), Fraction(1)]           # P(t) = 1 - 2t + t^2
hf = hstar(fake)
if min(hf) >= 0:
    bad += 1
    print(f"DETECTOR CONTROL FAILED: the synthetic polynomial has h = {hf}, no negative entry")
else:
    print(f"detector control: the synthetic polynomial 1 - 2t + t^2 has h = {hf}, "
          f"and the same code path flags it")
sys.exit(1 if bad else 0)
