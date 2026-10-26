#!/usr/bin/env python3
"""Ehrhart polynomials of k x N transportation polytopes (an image family of LR polytopes).

T(r, c) = {x in R_{>=0}^{k x N} : row sums r, column sums c}, |r| = |c|.  Its lattice points
are contingency tables; Ferudun 2026 records that the lattice points of a 3 x N
transportation polytope are the LR tableaux of a fixed triple, compatibly with dilation,
so a transportation polytope with a negative Ehrhart coefficient would refute
King-Tollu-Toumazet positivity outright.  This tool enumerates margin pairs (r, c) with
sorted margins up to a total, computes the Ehrhart polynomial with Normaliz (equations for
the margins, nonnegativity), and reports the minimal coefficient ratio to the unimodular
simplex and any negative coefficient.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import os
import time
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan import partitions  # noqa: E402
from scan2 import simplex_coeffs  # noqa: E402


def ehrhart_transport(r, c):
    from PyNormaliz import Cone  # type: ignore

    k, N = len(r), len(c)
    nvar = k * N
    eqs = []
    for i in range(k):
        row = [0] * (nvar + 1)
        for j in range(N):
            row[i * N + j] = 1
        row[nvar] = -r[i]
        eqs.append(row)
    for j in range(N - 1):  # the last column equation is implied
        row = [0] * (nvar + 1)
        for i in range(k):
            row[i * N + j] = 1
        row[nvar] = -c[j]
        eqs.append(row)
    ineqs = []
    for v in range(nvar):
        row = [0] * (nvar + 1)
        row[v] = 1
        ineqs.append(row)
    C = Cone(inhom_equations=eqs, inhom_inequalities=ineqs)
    dim = C.AffineDim()
    q = C.EhrhartQuasiPolynomial()
    den = q[-1]
    if len(q) - 1 != 1:
        return dim, None
    coeffs = [Fraction(x, den) for x in q[0]]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return dim, coeffs


def job(args):
    r, c = args
    t0 = time.time()
    dim, coeffs = ehrhart_transport(r, c)
    if coeffs is None:
        return {"r": r, "c": c, "dim": dim, "quasi": True}
    D = len(coeffs) - 1
    s = simplex_coeffs(D)
    minr = min(coeffs[k] / s[k] for k in range(1, D + 1)) if D >= 1 else Fraction(1)
    return {"r": r, "c": c, "dim": dim, "coeffs": [str(x) for x in coeffs], "minr": str(minr),
            "a1": str(coeffs[1]) if D >= 1 else "0", "neg": any(x < 0 for x in coeffs), "sec": round(time.time() - t0, 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--total-max", type=int, required=True)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    jobs = []
    for total in range(max(args.k, args.N), args.total_max + 1):
        rows = [p for p in partitions(total, args.k) if len(p) == args.k]
        cols = [p for p in partitions(total, args.N) if len(p) == args.N]
        for r in rows:
            for c in cols:
                jobs.append((list(r), list(c)))
    print(f"{len(jobs)} margin pairs", flush=True)
    t0 = time.time()
    n = negs = 0
    minr = (Fraction(10), None)
    with Pool(args.workers) as pool, open(args.out + ".jsonl", "w") as f:
        for rec in pool.imap_unordered(job, jobs, chunksize=1):
            n += 1
            f.write(json.dumps(rec) + "\n")
            if rec.get("quasi"):
                print("QUASI", json.dumps(rec), flush=True)
                continue
            if rec["neg"]:
                negs += 1
                print("NEGATIVE", json.dumps(rec), flush=True)
            m = Fraction(rec["minr"])
            if m < minr[0]:
                minr = (m, rec)
            if n % 50 == 0:
                print(f"{n}/{len(jobs)} in {time.time()-t0:.0f}s, negatives {negs}, min ratio {minr[0]}", flush=True)
    summary = {"k": args.k, "N": args.N, "total_max": args.total_max, "pairs": n, "negatives": negs,
               "min_ratio": str(minr[0]), "min_ratio_at": minr[1], "seconds": round(time.time() - t0, 1)}
    json.dump(summary, open(args.out + ".summary.json", "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
