#!/usr/bin/env python3
"""Independent checks for an exhaustive scan2 run (no Normaliz, no hive code).

Usage: check_gz.py <n_parts> <prefix> <N_FULL> <T_MAX>

1. Completeness for small sizes: recount the canonical triples with largest length
   n_parts and |lam| = N for N <= N_FULL by an independent generator and compare with
   the per-size totals of <prefix>.summary.json.
2. Recount of polynomials from <prefix>.jsonl.gz: every record with a negative
   coefficient, the 20 with the smallest minr, the 20 with the smallest linear
   coefficient, 40 seeded random records; c^{t lam}_{t mu, t nu} for
   t = 0..min(deg + 2, T_MAX) by the classical lattice-word rule against the record.
Exit 0 iff every comparison agrees.
"""
import gzip
import json
import random
import sys
from fractions import Fraction

from lrtableaux import count_lr_tableaux

n_parts = int(sys.argv[1])
prefix = sys.argv[2]
N_FULL = int(sys.argv[3])
T_MAX = int(sys.argv[4])


def parts_iter(n, k, maxp):
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
    for lam in parts_iter(N, n_parts, N):
        for m in range(1, N):
            for mu in parts_iter(m, n_parts, lam[0]):
                if not inside(mu, lam):
                    continue
                for nu in parts_iter(N - m, n_parts, lam[0]):
                    if nu > mu or not inside(nu, lam):
                        continue
                    cn = canon(lam, mu, nu)
                    if cn is None or max(len(cn[0]), len(cn[1]), len(cn[2])) != n_parts:
                        continue
                    total += 1
    return total


summary = json.load(open(prefix + ".summary.json"))
per_size = {int(k): v for k, v in summary["per_size"].items()}
bad = 0
for N in range(n_parts, N_FULL + 1):
    ind = count_size(N)
    got = per_size.get(N, {}).get("triples", 0)
    if ind != got:
        bad += 1
        print(f"COMPLETENESS MISMATCH size {N}: scan {got} independent {ind}")
print(f"completeness: sizes {n_parts}..{N_FULL} recounted independently, {bad} mismatches")

recs = []
horn_recs = []
with gzip.open(prefix + ".jsonl.gz", "rt") as f:
    for line in f:
        r = json.loads(line)
        if "num" in r:
            recs.append(r)
        elif r.get("skipped") == "horn":
            horn_recs.append(r)

# 3. Horn-filter records (a 1-in-100 sample of the skipped triples written by the scan):
#    the saturation equality holds for the recorded essential triple, both factor triples
#    have length <= n_parts - 1 and size <= |lam|, and c = c1 * c2 by lrcalc (the classical
#    rule, independent of the hive model and of Normaliz).  This checks that the skip rule
#    was applied as stated; the factors' positivity rests on the other runs and the theorems.
if horn_recs:
    import lrcalc  # type: ignore

    hbad = 0
    for r in horn_recs:
        lam, mu, nu = r["lam"], r["mu"], r["nu"]
        I, J, K = r["horn"]
        pad = lambda p: list(p) + [0] * (n_parts - len(p))
        L, M, Nn = pad(lam), pad(mu), pad(nu)
        if sum(L[k - 1] for k in K) != sum(M[i - 1] for i in I) + sum(Nn[j - 1] for j in J):
            hbad += 1
            print(f"HORN MISMATCH (not saturated) {lam} {mu} {nu} {r['horn']}")
            continue
        sub = lambda p, S: [x for x in (p[s - 1] for s in S) if x > 0]
        comp = lambda S: [i for i in range(1, n_parts + 1) if i not in S]
        f1 = (sub(L, K), sub(M, I), sub(Nn, J))
        f2 = (sub(L, comp(K)), sub(M, comp(I)), sub(Nn, comp(J)))
        c1 = int(lrcalc.lrcoef(*f1)) if (f1[1] or f1[2]) else 1
        c2 = int(lrcalc.lrcoef(*f2)) if (f2[1] or f2[2]) else 1
        if c1 * c2 != r["c"] or len(K) >= n_parts or len(K) < 1:
            hbad += 1
            print(f"HORN MISMATCH (factorisation) {lam} {mu} {nu} c={r['c']} c1={c1} c2={c2} {r['horn']}")
    bad += hbad
    print(f"horn filter: {len(horn_recs)} sampled skipped triples, {hbad} mismatches")


def coeffs_of(r):
    return [Fraction(x, r["den"]) for x in r["num"]]


def key(r):
    return (tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))


sample = {}
for r in recs:
    if r.get("neg"):
        sample[key(r)] = r
for r in sorted(recs, key=lambda r: Fraction(r["minr"]))[:20]:
    sample[key(r)] = r
for r in sorted(recs, key=lambda r: coeffs_of(r)[1])[:20]:
    sample[key(r)] = r
rng = random.Random(20260903)
for r in rng.sample(recs, min(40, len(recs))):
    sample[key(r)] = r
pinned = consistent = 0
for (lam, mu, nu), r in sample.items():
    coeffs = coeffs_of(r)
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
negs = sum(1 for r in recs if r.get("neg"))
print(f"recount: {len(sample)} records, {pinned} pinned (deg+2 points), {consistent} consistent at {T_MAX+1} points; polynomials in scan {len(recs)}, negatives {negs}, summary {json.dumps({k: v for k, v in summary.items() if k != 'per_size'})}")
sys.exit(1 if bad else 0)
