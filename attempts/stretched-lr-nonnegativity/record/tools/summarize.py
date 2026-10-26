#!/usr/bin/env python3
"""Aggregate the exhaustive scans (runs 2, 3, 4) into one table for the write-up."""
import glob
import gzip
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction

base = sys.argv[1] if len(sys.argv) > 1 else "attack/stretched-lr-polynomial-negative-coefficient/deterministic"


def simplex_coeffs(D):
    poly = [Fraction(1)]
    for k in range(1, D + 1):
        new = [Fraction(0)] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i] += c * k
            new[i + 1] += c
        poly = new
    return [c / math.factorial(D) for c in poly]


S = {D: simplex_coeffs(D) for D in range(1, 16)}
H = lambda D: sum(Fraction(1, k) for k in range(1, D + 1))


def summarise(name, records):
    polys = 0
    dims = Counter()
    maxden = Counter()
    negs = 0
    mins = defaultdict(lambda: (Fraction(10 ** 6), None))
    minr = (Fraction(10 ** 6), None)
    empties = Counter()
    for r in records:
        polys += 1
        D = r["dim"]
        dims[D] += 1
        maxden[r["maxden"]] += 1
        co = r["coeffs"]
        if any(x < 0 for x in co):
            negs += 1
        if co[1] < mins[D][0]:
            mins[D] = (co[1], r)
        rr = min(co[k] / S[D][k] for k in range(1, D + 1))
        if rr < minr[0]:
            minr = (rr, r)
        if r["c"] == D + 1 and co[-1] * math.factorial(D) > 1:
            empties[(D, str(co[-1] * math.factorial(D)))] += 1
    print(f"## {name}: {polys} polynomials, {negs} with a negative coefficient")
    print("dimensions:", dict(sorted(dims.items())))
    print("largest vertex denominator:", dict(sorted(maxden.items())))
    for D in sorted(mins):
        a1, r = mins[D]
        print(f"dim {D}: min a_1 = {a1} (H_D = {H(D)}{', below' if a1 < H(D) else ''}) at {r['lam']} {r['mu']} {r['nu']} c={r['c']}")
    rr, r = minr
    print(f"min coefficient ratio to the unimodular simplex: {rr} at {r['lam']} {r['mu']} {r['nu']} (dim {r['dim']}, c {r['c']})")
    print("empty non-unimodular simplices (dim, normalized volume): count", dict(empties))
    print()


# run 2 (plain jsonl)
recs = []
for fn in sorted(glob.glob(f"{base}/enumeration-run-2/scan-n5-*.jsonl")):
    for line in open(fn):
        r = json.loads(line)
        if "coeffs" in r:
            recs.append({"lam": r["lam"], "mu": r["mu"], "nu": r["nu"], "c": r["c"], "dim": r["dim"],
                         "maxden": r["maxden"], "coeffs": [Fraction(x) for x in r["coeffs"]]})
summarise("5 parts (enumeration-run-2)", recs)

for run, pref in (("3", "scan-n6"), ("4", "scan-n7")):
    recs = []
    horn = 0
    try:
        with gzip.open(f"{base}/enumeration-run-{run}/{pref}.jsonl.gz", "rt") as f:
            for line in f:
                r = json.loads(line)
                if "num" in r:
                    recs.append({"lam": r["lam"], "mu": r["mu"], "nu": r["nu"], "c": r["c"], "dim": r["dim"],
                                 "maxden": r["maxden"], "coeffs": [Fraction(x, r["den"]) for x in r["num"]]})
                elif r.get("skipped") == "horn":
                    horn += 1
    except (FileNotFoundError, EOFError):
        pass
    try:
        summary = json.load(open(f"{base}/enumeration-run-{run}/{pref}.summary.json"))
        print(f"run {run} summary:", {k: v for k, v in summary.items() if k != "per_size"})
    except FileNotFoundError:
        print(f"run {run}: no summary yet")
    if recs:
        summarise(f"{'6' if run == '3' else '7'} parts (enumeration-run-{run}), {horn} sampled horn-skipped records", recs)
