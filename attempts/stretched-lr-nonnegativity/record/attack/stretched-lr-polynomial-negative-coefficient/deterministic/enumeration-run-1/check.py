#!/usr/bin/env python3
"""Independent checker for the scan records (no Normaliz, no hive code).

For a sample of records (every record with a negative coefficient, the records with
the smallest linear coefficient and the smallest coefficient overall, and a seeded
random sample), recompute c^{t lam}_{t mu, t nu} for t = 0..T by the classical
lattice-word rule (lrtableaux.count_lr_tableaux) and compare with the recorded
polynomial evaluated at t.  T = min(deg + 2, T_MAX); when deg + 2 <= T the check
pins the polynomial (deg + 1 interpolation nodes plus two held-out points); when
deg + 2 > T the check is a consistency check at T + 1 points and says so.
Exit 0 iff every compared value agrees.
"""
import json
import random
import sys
from fractions import Fraction

from lrtableaux import count_lr_tableaux

T_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5
files = sys.argv[1].split(",")
recs = []
for fn in files:
    with open(fn) as f:
        for line in f:
            r = json.loads(line)
            if "coeffs" in r:
                recs.append(r)

def key_frac(s):
    return Fraction(s)

sample = {}
for r in recs:
    if r.get("negative"):
        sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r
for r in sorted(recs, key=lambda r: key_frac(r["a1"]))[:15]:
    sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r
for r in sorted(recs, key=lambda r: key_frac(r["min_coeff"]))[:15]:
    sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r
rng = random.Random(20260903)
for r in rng.sample(recs, min(30, len(recs))):
    sample[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r

bad = 0
pinned = 0
consistent = 0
for (lam, mu, nu), r in sample.items():
    coeffs = [Fraction(x) for x in r["coeffs"]]
    deg = len(coeffs) - 1
    T = min(deg + 2, T_MAX)
    ok = True
    for t in range(0, T + 1):
        v = count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]) if t else 1
        p = sum(c * Fraction(t) ** i for i, c in enumerate(coeffs))
        if v != p:
            ok = False
            print(f"MISMATCH {lam} {mu} {nu} t={t} count={v} poly={p}")
            break
    if not ok:
        bad += 1
    elif T >= deg + 2:
        pinned += 1
    else:
        consistent += 1
print(f"checked {len(sample)} records: {pinned} pinned (deg+2 points), {consistent} consistent at {T_MAX+1} points, {bad} mismatches")
sys.exit(1 if bad else 0)
