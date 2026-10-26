#!/usr/bin/env python3
"""Independent check of counterexample-search-run-3 (6-part hives of dimension >= 8 beyond the box).

1. Every hit (a record with a negative coefficient) is re-verified against the full hypothesis:
   the tableau-polytope encoding (tableau_polytope.py, the lattice-word conditions, no hive
   inequality) recomputed by Normaliz must give the same polynomial, and lrcalc must give c at
   t = 1 and 2. There are none expected; the check then reports 0 hits.
2. For every record, lrcalc (the classical rule) must give c at t = 1.
3. For a seeded sample of 1,500 records (seed 20260904), the tableau-polytope encoding must give
   the recorded polynomial and lrcalc the value at t = 2 when it is at most 1,000,000.
4. The summary's count equals the record count, and every record has c >= 3, is primitive
   (re-tested with horn.py) and has dim >= 8.
A third implementation (the lattice-word counter lrtableaux.py) recounts 30 seeded random
records with P(3) <= 300,000 at t = 0..3 (consistency at four points, not a pinning).
Exit 0 iff everything agrees.
"""
import glob
import gzip
import json
import os
import random
import sys
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lrcalc  # type: ignore
from horn import HornChecker  # noqa: E402
from lrtableaux import count_lr_tableaux  # noqa: E402
from tableau_polytope import ehrhart_tableau  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PREFIX = "s2"
PARTS = 6
DMIN = 8
T2_LIMIT = 1_000_000
SAMPLE = 1500


def recorded_poly(rec):
    p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(p, t):
    return sum(c * Fraction(t) ** i for i, c in enumerate(p))


def check_full(rec):
    lam, mu, nu = rec["lam"], rec["mu"], rec["nu"]
    p = recorded_poly(rec)
    ok = ehrhart_tableau(lam, mu, nu)[1] == p
    ok = ok and int(lrcalc.lrcoef(lam, mu, nu)) == rec["c"] == evalp(p, 1)
    if evalp(p, 2) <= T2_LIMIT:
        ok = ok and int(lrcalc.lrcoef([2 * x for x in lam], [2 * x for x in mu], [2 * x for x in nu])) == evalp(p, 2)
    return ok, rec


def check_c1(rec):
    return int(lrcalc.lrcoef(rec["lam"], rec["mu"], rec["nu"])) == rec["c"] == evalp(recorded_poly(rec), 1)


def main():
    recs = []
    for fn in sorted(glob.glob(os.path.join(HERE, PREFIX + "*.jsonl.gz"))):
        with gzip.open(fn, "rt") as f:
            for line in f:
                r = json.loads(line)
                if "num" in r:
                    recs.append(r)
    expected = sum(json.load(open(fn))["recorded"] for fn in sorted(glob.glob(os.path.join(HERE, PREFIX + "*.summary.json"))))
    bad = 0
    if expected != len(recs):
        bad += 1
        print(f"COUNT MISMATCH: summaries {expected}, records {len(recs)}")
    checker = HornChecker(PARTS)
    for r in recs:
        if r["c"] < 3 or r["dim"] < DMIN or not checker.is_primitive(r["lam"], r["mu"], r["nu"]):
            bad += 1
            print("FILTER MISMATCH", r)
            break
    hits = [r for r in recs if r.get("neg")]
    rng = random.Random(20260904)
    sample = rng.sample(recs, min(SAMPLE, len(recs)))
    with Pool(6) as pool:
        c1_ok = sum(pool.imap_unordered(check_c1, recs, chunksize=256))
        full_ok = 0
        for ok, r in pool.imap_unordered(check_full, hits + sample, chunksize=4):
            full_ok += ok
            if not ok:
                bad += 1
                print("MISMATCH", json.dumps(r), flush=True)
    print(f"hits (negative coefficient): {len(hits)}, all re-verified from the definition: {len(hits) == 0 or bad == 0}; "
          f"lrcalc agrees at t = 1 on {c1_ok} of {len(recs)} records; tableau-polytope encoding and lrcalc (t = 2 when P(2) <= {T2_LIMIT}) agree on {full_ok} of {len(hits) + len(sample)} sampled records")
    if c1_ok != len(recs):
        bad += 1
    small = [r for r in recs if evalp(recorded_poly(r), 3) <= 300_000]
    sample3 = rng.sample(small, min(30, len(small)))
    sbad = 0
    for r in sample3:
        lam, mu, nu = r["lam"], r["mu"], r["nu"]
        p = recorded_poly(r)
        for t in range(4):
            v = count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1
            if v != evalp(p, t):
                sbad += 1
                print("THIRD-IMPLEMENTATION MISMATCH", r, "t =", t)
                break
    bad += sbad
    print(f"third implementation (lattice-word counter, t = 0..3): {len(sample3)} records, {sbad} mismatches")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
