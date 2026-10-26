#!/usr/bin/env python3
"""Exhaustive streaming scan of a stratum (largest length n, |lam| = N).

Jobs are indexed by lam: a worker enumerates every canonical (mu, nu) for its lam,
computes c (lrcalc), and for c >= 3 the hive dimension and, for dim >= 3, the Ehrhart
polynomial (Normaliz).  It returns per-lam counts and the compact polynomial records.
Output: one gzip JSON-lines file of polynomial records plus a summary JSON.

Record fields: lam, mu, nu, c, dim, den (common denominator), num (coefficient
numerators low->high), maxden (largest vertex denominator), M (leading factors),
minr (min over k >= 1 of a_k divided by the unimodular-simplex coefficient), neg.
Canonical form and the theorem-based skips are those of scan.py / move 1 of the attack.
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities  # noqa: E402
from scan import canonical, contained, lr_coef, partitions  # noqa: E402

_SIMPLEX = {}


def simplex_coeffs(D):
    if D not in _SIMPLEX:
        poly = [Fraction(1)]
        for k in range(1, D + 1):
            new = [Fraction(0)] * (len(poly) + 1)
            for i, c in enumerate(poly):
                new[i] += c * k
                new[i + 1] += c
            poly = new
        _SIMPLEX[D] = [c / math.factorial(D) for c in poly]
    return _SIMPLEX[D]


def analyse_lam(args):
    from PyNormaliz import Cone  # type: ignore

    n_parts, N, lam = args
    counts = {"triples": 0, "c_ge_3": 0, "dim_ge_3": 0, "period_ne_1": 0, "negative": 0}
    records = []
    for m in range(1, N):
        for mu in partitions(m, n_parts, lam[0]):
            if not contained(mu, lam):
                continue
            for nu in partitions(N - m, n_parts, lam[0]):
                if nu > mu or not contained(nu, lam):
                    continue
                can = canonical(lam, mu, nu)
                if can is None or max(len(can[0]), len(can[1]), len(can[2])) != n_parts:
                    continue
                counts["triples"] += 1
                c = lr_coef(*can)
                if c < 3:
                    continue
                counts["c_ge_3"] += 1
                D, rows = hive_inequalities(*can)
                C = Cone(inhom_inequalities=rows)
                dim = C.AffineDim()
                if dim < 3:
                    continue
                counts["dim_ge_3"] += 1
                q = C.EhrhartQuasiPolynomial()
                den = q[-1]
                period = len(q) - 1
                rec = {"lam": list(can[0]), "mu": list(can[1]), "nu": list(can[2]), "c": c, "dim": dim}
                if period != 1:
                    counts["period_ne_1"] += 1
                    rec["quasi"] = [[str(Fraction(x, den)) for x in comp] for comp in q[:-1]]
                    rec["neg"] = any(x < 0 for comp in q[:-1] for x in comp)
                    records.append(rec)
                    continue
                coeffs = [Fraction(x, den) for x in q[0]]
                while len(coeffs) > 1 and coeffs[-1] == 0:
                    coeffs.pop()
                Dd = len(coeffs) - 1
                s = simplex_coeffs(Dd)
                minr = min(coeffs[k] / s[k] for k in range(1, Dd + 1))
                neg = any(x < 0 for x in coeffs)
                verts = C.VerticesOfPolyhedron()
                maxden = max(v[-1] for v in verts) if verts else 1
                M = 0
                for mm in range(1, Dd + 1):
                    if sum(cf * Fraction(-mm) ** i for i, cf in enumerate(coeffs)) == 0:
                        M += 1
                    else:
                        break
                rec.update({"den": den, "num": [x for x in q[0][: Dd + 1]], "maxden": maxden, "M": M,
                            "minr": str(minr), "neg": neg})
                if neg:
                    counts["negative"] += 1
                records.append(rec)
    return lam, counts, records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", type=int, required=True)
    ap.add_argument("--sizes", type=int, nargs="+", required=True)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--out", required=True, help="output prefix")
    args = ap.parse_args()
    jobs = [(args.parts, N, lam) for N in args.sizes for lam in partitions(N, args.parts)]
    jobs.sort(key=lambda j: (-j[1], j[2]))
    print(f"{len(jobs)} lam-jobs", flush=True)
    t0 = time.time()
    total = {"triples": 0, "c_ge_3": 0, "dim_ge_3": 0, "period_ne_1": 0, "negative": 0, "lams": 0}
    per_size = {}
    with Pool(args.workers) as pool, gzip.open(args.out + ".jsonl.gz", "wt") as f:
        for lam, counts, records in pool.imap_unordered(analyse_lam, jobs, chunksize=1):
            total["lams"] += 1
            for k, v in counts.items():
                total[k] += v
            ps = per_size.setdefault(sum(lam), {"triples": 0, "c_ge_3": 0, "dim_ge_3": 0, "negative": 0})
            for k in ps:
                ps[k] += counts[k]
            for rec in records:
                f.write(json.dumps(rec) + "\n")
                if rec["neg"]:
                    print("NEGATIVE", json.dumps(rec), flush=True)
            if total["lams"] % 50 == 0:
                print(f"{total['lams']}/{len(jobs)} lams, {total['dim_ge_3']} polys, {time.time()-t0:.0f}s, negatives {total['negative']}", flush=True)
    total["seconds"] = round(time.time() - t0, 1)
    total["per_size"] = per_size
    with open(args.out + ".summary.json", "w") as f:
        json.dump(total, f, indent=1)
    print("done", json.dumps(total), flush=True)


if __name__ == "__main__":
    main()
