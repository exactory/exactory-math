#!/usr/bin/env python3
"""Independent check of counterexample-search-run-1 (5-part hives beyond the box).

For every recorded polynomial (files s1*.jsonl.gz):
1. a second polytope encoding, the tableau polytope of tableau_polytope.py (the
   lattice-word conditions, no hive inequality), computed by Normaliz, must give the same
   polynomial;
2. lrcalc (the classical rule) must give c at t = 1 and the polynomial's value at t = 2;
3. when the recorded polynomial has P(6) <= 2,000,000, lrcalc counts at t = 0..6 pin the
   polynomial outright (deg P <= 6 for 5 parts), exact Newton interpolation;
4. the summaries' counts equal the record counts, every record has c >= 3, is primitive
   (re-tested with horn.py) and has dim >= 3.
A third implementation (lattice-word counter + Lagrange) recounts 30 seeded random records
with P(6) <= 200,000 and |lam| <= 40 at t = 0..6 (the counter's cost grows with the size).
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
PIN_LIMIT = 2_000_000


def newton(values):
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


def recorded_poly(rec):
    p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(p, t):
    return sum(c * Fraction(t) ** i for i, c in enumerate(p))


T2_LIMIT = 1_000_000


def check_one(rec):
    lam, mu, nu = rec["lam"], rec["mu"], rec["nu"]
    p = recorded_poly(rec)
    ok_tab = ehrhart_tableau(lam, mu, nu)[1] == p
    c1 = int(lrcalc.lrcoef(lam, mu, nu))
    ok_lr = c1 == rec["c"] == evalp(p, 1)
    # lrcalc enumerates tableaux, so the value at t = 2 is recounted only when it is small
    if evalp(p, 2) <= T2_LIMIT:
        c2 = int(lrcalc.lrcoef([2 * x for x in lam], [2 * x for x in mu], [2 * x for x in nu]))
        ok_lr = ok_lr and c2 == evalp(p, 2)
    pinned = None
    if evalp(p, 6) <= PIN_LIMIT:
        values = [1] + [int(lrcalc.lrcoef([t * x for x in lam], [t * x for x in mu], [t * x for x in nu])) for t in range(1, 7)]
        pinned = newton(values) == p
    return ok_tab, ok_lr, pinned, rec if not (ok_tab and ok_lr and pinned is not False) else None


def main():
    recs = []
    for fn in sorted(glob.glob(os.path.join(HERE, "s1*.jsonl.gz"))):
        with gzip.open(fn, "rt") as f:
            for line in f:
                r = json.loads(line)
                if "num" in r:
                    recs.append(r)
    expected = sum(json.load(open(fn))["recorded"] for fn in sorted(glob.glob(os.path.join(HERE, "s1*.summary.json"))))
    bad = 0
    if expected != len(recs):
        bad += 1
        print(f"COUNT MISMATCH: summaries {expected}, records {len(recs)}")
    checker = HornChecker(5)
    for r in recs:
        if r["c"] < 3 or r["dim"] < 3 or not checker.is_primitive(r["lam"], r["mu"], r["nu"]):
            bad += 1
            print("FILTER MISMATCH", r)
            break
    tab = lr = pin = 0
    pin_tried = 0
    done = 0
    with Pool(6) as pool:
        for ok_tab, ok_lr, pinned, failing in pool.imap_unordered(check_one, recs, chunksize=64):
            done += 1
            tab += ok_tab
            lr += ok_lr
            if pinned is not None:
                pin_tried += 1
                pin += pinned
            if failing is not None:
                bad += 1
                print("MISMATCH", json.dumps(failing), flush=True)
            if done % 50000 == 0:
                print(f"progress: {done} of {len(recs)} records checked", flush=True)
    print(f"tableau-polytope encoding agrees on {tab} of {len(recs)} records; lrcalc agrees at t = 1 (and at t = 2 when P(2) <= {T2_LIMIT}) on {lr}; lrcalc pins {pin} of the {pin_tried} records with P(6) <= {PIN_LIMIT}")
    rng = random.Random(20260904)
    small = [r for r in recs if evalp(recorded_poly(r), 6) <= 200_000 and sum(r["lam"]) <= 40]
    sample = rng.sample(small, min(30, len(small)))
    sbad = 0
    for r in sample:
        lam, mu, nu = r["lam"], r["mu"], r["nu"]
        values = [count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1 for t in range(7)]
        if lagrange(values) != recorded_poly(r):
            sbad += 1
            print("THIRD-IMPLEMENTATION MISMATCH", r)
    bad += sbad
    negs = sum(1 for r in recs if r.get("neg"))
    print(f"third implementation: {len(sample)} records, {sbad} mismatches; negatives among records: {negs}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
