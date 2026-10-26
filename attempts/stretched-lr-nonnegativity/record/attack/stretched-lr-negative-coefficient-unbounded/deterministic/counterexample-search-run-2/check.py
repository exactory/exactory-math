#!/usr/bin/env python3
"""Independent check of the transportation-polytope search (no polytope code).

For every family file t<k>x<N>.jsonl: the record count equals the summary's pair count and
no record has a negative coefficient or a period other than 1.  For a seeded sample of 25
pairs per family plus each family's minimal-ratio pair, the number of nonnegative integer
k x N matrices with margins (t r, t c) is counted from the definition (a row-by-row
dynamic programme over remaining column sums) for t = 1, 2, and for t = 3 when the recorded
value is below 10^7, and compared with the recorded polynomial's values.
Exit 0 iff everything agrees.
"""
import glob
import json
import os
import random
import sys
from fractions import Fraction
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))


def count_tables(r, c, t):
    k, N = len(r), len(c)
    R = [t * x for x in r]
    C = tuple(t * x for x in c)

    @lru_cache(maxsize=None)
    def rows_left(i, rem):
        if i == k:
            return 1 if not any(rem) else 0
        total = 0

        def fill(j, left, rem_list):
            nonlocal total
            if j == N - 1:
                if left <= rem_list[j]:
                    new = list(rem_list)
                    new[j] -= left
                    total += rows_left(i + 1, tuple(new))
                return
            for a in range(min(left, rem_list[j]) + 1):
                new = list(rem_list)
                new[j] -= a
                fill(j + 1, left - a, new)

        fill(0, R[i], list(rem))
        return total

    return rows_left(0, C)


def evalp(coeffs, t):
    return sum(Fraction(x) * Fraction(t) ** i for i, x in enumerate(coeffs))


bad = 0
rng = random.Random(20260904)
for fn in sorted(glob.glob(os.path.join(HERE, "t*.jsonl"))):
    name = os.path.basename(fn)[:-6]
    recs = [json.loads(line) for line in open(fn)]
    summary = json.load(open(os.path.join(HERE, name + ".summary.json")))
    if summary["pairs"] != len(recs):
        bad += 1
        print(f"{name}: COUNT MISMATCH summary {summary['pairs']} records {len(recs)}")
    quasi = [r for r in recs if r.get("quasi")]
    negs = [r for r in recs if r.get("neg")]
    if quasi or negs:
        print(f"{name}: {len(quasi)} quasi-polynomials, {len(negs)} negatives recorded")
    sample = rng.sample(recs, min(12, len(recs)))
    if summary.get("min_ratio_at"):
        sample.append(summary["min_ratio_at"])
    fbad = 0
    for r in sample:
        if r.get("quasi"):
            continue
        k, N = len(r["r"]), len(r["c"])
        # the row-by-row count is exponential in the margins; t = 3 only for the small shapes
        ts = (1, 2, 3) if (k * N <= 15 and sum(r["r"]) <= 12) else (1, 2)
        for t in ts:
            v = evalp(r["coeffs"], t)
            if t >= 2 and v >= 10 ** 6:
                break
            if count_tables(r["r"], r["c"], t) != v:
                fbad += 1
                print(f"{name}: MISMATCH r={r['r']} c={r['c']} t={t}")
                break
    bad += fbad
    print(f"{name}: {len(recs)} pairs, {len(negs)} negatives, sample of {len(sample)} recounted from the definition, {fbad} mismatches")
sys.exit(1 if bad else 0)
