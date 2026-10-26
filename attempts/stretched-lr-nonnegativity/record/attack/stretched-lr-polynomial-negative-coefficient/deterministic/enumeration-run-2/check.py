#!/usr/bin/env python3
"""Independent checks for the exhaustive 5-part scan (no Normaliz, no hive code).

1. Completeness of the enumeration for small sizes: recount the canonical triples
   with largest length 5 and |lam| = N for N <= N_FULL by an independent generator
   (integer partitions by an iterative algorithm, containment and canonical form
   written again here) and compare with the per-size totals in the scan output.
2. Recount of polynomials: for every record with a negative coefficient, the 20
   records with the smallest minr (coefficient over unimodular-simplex value), the
   20 with the smallest linear coefficient, and 40 seeded random records, recount
   c^{t lam}_{t mu, t nu} for t = 0..min(deg + 2, T_MAX) by the classical lattice-word
   rule and compare with the recorded polynomial.
Exit 0 iff every comparison agrees.
"""
import glob
import json
import random
import sys
from collections import Counter
from fractions import Fraction

from lrtableaux import count_lr_tableaux

N_FULL = int(sys.argv[1]) if len(sys.argv) > 1 else 18
T_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5


def parts_iter(n, k, maxp):
    """Partitions of n into at most k parts, each <= maxp, as tuples (independent generator)."""
    if n == 0:
        yield ()
        return
    if k == 0:
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in parts_iter(n - p, k - 1, p):
            yield (p,) + rest


def inside(a, b):
    return len(a) <= len(b) and all(x <= y for x, y in zip(a, b))


def canon(lam, mu, nu):
    if mu < nu:
        mu, nu = nu, mu
    n = max(len(lam), len(mu), len(nu))
    if len(lam) == n and (len(mu) == n or len(nu) == n):
        return None
    return lam, mu, nu


def count_size(N):
    total = 0
    for lam in parts_iter(N, 5, N):
        for m in range(1, N):
            for mu in parts_iter(m, 5, lam[0]):
                if not inside(mu, lam):
                    continue
                for nu in parts_iter(N - m, 5, lam[0]):
                    if nu > mu or not inside(nu, lam):
                        continue
                    cn = canon(lam, mu, nu)
                    if cn is None or max(len(cn[0]), len(cn[1]), len(cn[2])) != 5:
                        continue
                    total += 1
    return total


recs = []
per_size = Counter()
for fn in sorted(glob.glob("scan-n5-*.jsonl")):
    with open(fn) as f:
        for line in f:
            r = json.loads(line)
            per_size[r["N"]] += 1
            if "coeffs" in r:
                recs.append(r)

bad = 0
for N in range(5, N_FULL + 1):
    ind = count_size(N)
    if ind != per_size[N]:
        bad += 1
        print(f"COMPLETENESS MISMATCH size {N}: scan {per_size[N]} independent {ind}")
print(f"completeness: sizes 5..{N_FULL} recounted independently, {bad} mismatches; scan totals per size {dict(sorted(per_size.items()))}")

sample = {}
def key(r):
    return (tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))
for r in recs:
    if r.get("negative"):
        sample[key(r)] = r
for r in sorted(recs, key=lambda r: Fraction(r["a1"]))[:20]:
    sample[key(r)] = r
for r in sorted(recs, key=lambda r: Fraction(r["min_coeff"]))[:20]:
    sample[key(r)] = r
rng = random.Random(20260903)
for r in rng.sample(recs, min(40, len(recs))):
    sample[key(r)] = r
pinned = consistent = 0
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
print(f"recount: {len(sample)} records, {pinned} pinned (deg+2 points), {consistent} consistent at {T_MAX+1} points; polynomials in scan {len(recs)}, negatives {sum(1 for r in recs if r.get('negative'))}")
sys.exit(1 if bad else 0)
