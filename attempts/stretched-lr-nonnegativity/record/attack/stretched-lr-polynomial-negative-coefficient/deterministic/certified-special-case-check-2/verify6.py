#!/usr/bin/env python3
"""Second implementation for the whole 6-part box: pin every polynomial by lrcalc counts.

For a triple whose partitions have at most 6 parts the hive polytope lives in R^10 (ten
interior hive entries), so deg P <= 10 unconditionally and P is determined by its values
at t = 0..10.  For every polynomial record of enumeration-run-3 this script computes
c^{t lam}_{t mu, t nu} for t = 1..10 with lrcalc (the classical rule; shares nothing with
Normaliz or the hive encoder), interpolates exactly (Newton over Fractions), and compares
with the recorded Normaliz polynomial.  Records are processed largest-dimension first so
the slow ones surface early.  Output: verify6.summary.json, verify6.mismatches.jsonl.
"""
import gzip
import json
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

import lrcalc  # type: ignore

RUN3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enumeration-run-3", "scan-n6.jsonl.gz")
DEG_BOUND = 10


def newton_interpolate(values):
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
    t0 = time.time()
    values = [1]
    for t in range(1, DEG_BOUND + 1):
        values.append(int(lrcalc.lrcoef([t * x for x in lam], [t * x for x in mu], [t * x for x in nu])))
    poly = newton_interpolate(values)
    recorded = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(recorded) > 1 and recorded[-1] == 0:
        recorded.pop()
    ok = poly == recorded
    return ok, rec if not ok else None, values[DEG_BOUND], time.time() - t0, rec["dim"]


def records():
    recs = []
    with gzip.open(RUN3, "rt") as f:
        for line in f:
            r = json.loads(line)
            if "num" in r:
                recs.append(r)
    recs.sort(key=lambda r: -r["dim"])
    return recs


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    t0 = time.time()
    recs = records()
    print(f"{len(recs)} records", flush=True)
    n = ok = 0
    max_p = 0
    slowest = (0.0, None)
    with Pool(workers) as pool, open("verify6.mismatches.jsonl", "w") as mm:
        for good, bad, p10, dt, dim in pool.imap_unordered(check, recs, chunksize=4):
            n += 1
            max_p = max(max_p, p10)
            if dt > slowest[0]:
                slowest = (dt, dim)
            if good:
                ok += 1
            else:
                mm.write(json.dumps(bad) + "\n")
                mm.flush()
                print("MISMATCH", json.dumps(bad), flush=True)
            if n % 20000 == 0:
                print(f"{n} checked, {ok} agree, {time.time()-t0:.0f}s, max P(10) {max_p}, slowest {slowest[0]:.1f}s at dim {slowest[1]}", flush=True)
    summary = {"records": n, "agree": ok, "mismatches": n - ok, "degree_bound": DEG_BOUND,
               "points": list(range(DEG_BOUND + 1)), "max_P10": max_p, "slowest_seconds": round(slowest[0], 1),
               "seconds": round(time.time() - t0, 1), "second_implementation": "lrcalc"}
    json.dump(summary, open("verify6.summary.json", "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
