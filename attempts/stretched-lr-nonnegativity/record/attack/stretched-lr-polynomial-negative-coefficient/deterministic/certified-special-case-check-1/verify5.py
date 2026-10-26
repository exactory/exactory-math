#!/usr/bin/env python3
"""Second implementation for the whole 5-part box: pin every polynomial by lrcalc counts.

For a triple whose partitions have at most 5 parts the hive polytope lives in R^6 (six
interior hive entries), so deg P <= 6 unconditionally, and P is determined by its values
at t = 0..6.  For every polynomial record of enumeration-run-2 this script computes
c^{t lam}_{t mu, t nu} for t = 1..6 with lrcalc (the classical Littlewood-Richardson rule,
a program that shares nothing with Normaliz or with the hive encoder), interpolates
exactly (Newton divided differences over Fractions), and compares with the recorded
Normaliz polynomial.  Output: verify5.summary.json with the counts and every mismatch,
verify5.mismatches.jsonl (empty when all agree).
"""
import glob
import json
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

import lrcalc  # type: ignore

RUN2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enumeration-run-2")
DEG_BOUND = 6


def newton_interpolate(values):
    """Monomial coefficients (low->high) of the polynomial through (t, values[t]), t = 0..m."""
    xs = [Fraction(t) for t in range(len(values))]
    dd = [Fraction(v) for v in values]
    m = len(values)
    coefs = [dd[0]]
    for j in range(1, m):
        for i in range(m - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) / (xs[i] - xs[i - j])
        coefs.append(dd[j])
    poly = [Fraction(0)] * m
    basis = [Fraction(1)]
    for j in range(m):
        for k, b in enumerate(basis):
            poly[k] += coefs[j] * b
        if j < m - 1:
            new = [Fraction(0)] * (len(basis) + 1)
            for k, b in enumerate(basis):
                new[k] -= xs[j] * b
                new[k + 1] += b
            basis = new
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def check(rec):
    lam, mu, nu = rec["lam"], rec["mu"], rec["nu"]
    values = [1]
    for t in range(1, DEG_BOUND + 1):
        values.append(int(lrcalc.lrcoef([t * x for x in lam], [t * x for x in mu], [t * x for x in nu])))
    poly = newton_interpolate(values)
    recorded = [Fraction(x) for x in rec["coeffs"]]
    ok = poly == recorded
    return ok, rec if not ok else None, values[1], values[DEG_BOUND]


def records():
    for fn in sorted(glob.glob(os.path.join(RUN2, "scan-n5-*.jsonl"))):
        with open(fn) as f:
            for line in f:
                r = json.loads(line)
                if "coeffs" in r:
                    yield r


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    t0 = time.time()
    n = ok = 0
    max_p6 = 0
    with Pool(workers) as pool, open("verify5.mismatches.jsonl", "w") as mm:
        for good, bad, c1, p6 in pool.imap_unordered(check, records(), chunksize=64):
            n += 1
            max_p6 = max(max_p6, p6)
            if good:
                ok += 1
            else:
                mm.write(json.dumps(bad) + "\n")
                mm.flush()
                print("MISMATCH", json.dumps(bad), flush=True)
            if n % 50000 == 0:
                print(f"{n} checked, {ok} agree, {time.time()-t0:.0f}s, max P(6) {max_p6}", flush=True)
    summary = {"records": n, "agree": ok, "mismatches": n - ok, "degree_bound": DEG_BOUND,
               "points": list(range(DEG_BOUND + 1)), "max_P6": max_p6, "seconds": round(time.time() - t0, 1),
               "second_implementation": "lrcalc " + getattr(lrcalc, "__version__", "?")}
    json.dump(summary, open("verify5.summary.json", "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
