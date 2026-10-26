#!/usr/bin/env python3
"""Seeded random search for a negative coefficient outside the box.

Samples triples (lam, mu, nu) with largest length n and |lam| in a size range, keeps the
primitive ones with c >= 3 and dim H >= dmin (the King-Tollu-Toumazet factorisation makes
non-primitive triples products of smaller ones), computes the Ehrhart polynomial by
Normaliz, and records the coefficients, the minimal coefficient ratio to the unimodular
simplex, the normalized volume, and the largest vertex denominator.  Output: gzip JSON
lines plus a summary.  A negative coefficient is printed at once.
"""
from __future__ import annotations

import argparse
import gzip
import json
import math
import os
import random
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities  # noqa: E402
from scan import canonical, contained, lr_coef  # noqa: E402
from scan2 import simplex_coeffs  # noqa: E402

_HORN = {}


def random_partition(rng, total, k, maxp):
    for _ in range(1000):
        parts = rng.randint(1, k)
        cuts = sorted(rng.sample(range(1, total + parts), parts - 1)) if parts > 1 else []
        p = sorted([b - a - 1 for a, b in zip([0] + cuts, cuts + [total + parts])], reverse=True)
        p = tuple(x for x in p if x > 0)
        if sum(p) == total and len(p) <= k and (not p or p[0] <= maxp):
            return p
    return None


def sample_one(args):
    seed, n, smin, smax, dmin, want_full, cmax_excess, nu_max, dmax = args
    from PyNormaliz import Cone  # type: ignore

    rng = random.Random(seed)
    if n not in _HORN:
        from horn import HornChecker

        _HORN[n] = HornChecker(n)
    checker = _HORN[n]
    stats = {"tried": 0, "c_ge_3": 0, "primitive": 0, "dim_ok": 0}
    for _ in range(200):
        stats["tried"] += 1
        size = rng.randint(smin, smax)
        lam = random_partition(rng, size, n, size)
        if lam is None or len(lam) != n:
            continue
        if nu_max is None:
            m = rng.randint(max(1, size // 4), min(size - 1, 3 * size // 4))
        else:
            m = size - rng.randint(1, min(nu_max, size - 1))
        mu = random_partition(rng, m, n, lam[0])
        nu = random_partition(rng, size - m, n, lam[0])
        if mu is None or nu is None or not contained(mu, lam) or not contained(nu, lam):
            continue
        can = canonical(lam, mu, nu)
        if can is None or max(len(can[0]), len(can[1]), len(can[2])) != n:
            continue
        c = lr_coef(*can)
        if c < 3:
            continue
        stats["c_ge_3"] += 1
        if checker.saturated(*can):
            continue
        stats["primitive"] += 1
        D, rows = hive_inequalities(*can)
        C = Cone(inhom_inequalities=rows)
        dim = C.AffineDim()
        if dim < dmin or (want_full and dim != D) or (dmax is not None and dim > dmax):
            continue
        if cmax_excess is not None and c > dim + cmax_excess:
            continue
        stats["dim_ok"] += 1
        q = C.EhrhartQuasiPolynomial()
        den = q[-1]
        if len(q) - 1 != 1:
            return stats, {"lam": list(can[0]), "mu": list(can[1]), "nu": list(can[2]), "c": c, "dim": dim,
                           "quasi": [[str(Fraction(x, den)) for x in comp] for comp in q[:-1]], "neg": None}
        coeffs = [Fraction(x, den) for x in q[0]]
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        Dd = len(coeffs) - 1
        s = simplex_coeffs(Dd)
        minr = min(coeffs[k] / s[k] for k in range(1, Dd + 1))
        verts = C.VerticesOfPolyhedron()
        maxden = max(v[-1] for v in verts) if verts else 1
        rec = {"lam": list(can[0]), "mu": list(can[1]), "nu": list(can[2]), "c": c, "dim": dim, "den": den,
               "num": q[0][: Dd + 1], "V": str(coeffs[-1] * math.factorial(Dd)), "maxden": maxden,
               "minr": str(minr), "a1": str(coeffs[1]), "neg": any(x < 0 for x in coeffs)}
        return stats, rec
    return stats, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", type=int, required=True)
    ap.add_argument("--smin", type=int, required=True)
    ap.add_argument("--smax", type=int, required=True)
    ap.add_argument("--dmin", type=int, default=3)
    ap.add_argument("--full", action="store_true", help="full-dimensional hives only")
    ap.add_argument("--count", type=int, required=True, help="number of recorded polynomials wanted")
    ap.add_argument("--seed", type=int, default=20260904)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cmax-excess", type=int, default=None,
                    help="keep only hives with at most dim + this many lattice points (few-point, large-volume hives)")
    ap.add_argument("--nu-max", type=int, default=None,
                    help="draw the smaller partition nu with |nu| uniform in 1..this (the small-third-partition corner)")
    ap.add_argument("--dmax", type=int, default=None, help="skip hives of dimension above this (solver cost)")
    args = ap.parse_args()
    rng = random.Random(args.seed)
    t0 = time.time()
    total = {"tried": 0, "c_ge_3": 0, "primitive": 0, "dim_ok": 0, "recorded": 0, "negative": 0, "quasi": 0}
    minr = (Fraction(10), None)
    mina1 = (Fraction(10 ** 6), None)
    maxV_small_c = (Fraction(0), None)
    jobs = ((rng.randrange(1 << 30), args.parts, args.smin, args.smax, args.dmin, args.full, args.cmax_excess,
             args.nu_max, args.dmax) for _ in range(10 ** 9))
    with Pool(args.workers) as pool, gzip.open(args.out + ".jsonl.gz", "wt") as f:
        for stats, rec in pool.imap_unordered(sample_one, jobs, chunksize=1):
            for k, v in stats.items():
                total[k] += v
            if rec is None:
                continue
            total["recorded"] += 1
            f.write(json.dumps(rec) + "\n")
            if rec.get("neg") is None:
                total["quasi"] += 1
                print("QUASI-POLYNOMIAL", json.dumps(rec), flush=True)
            elif rec["neg"]:
                total["negative"] += 1
                print("NEGATIVE", json.dumps(rec), flush=True)
                f.flush()
            else:
                r = Fraction(rec["minr"])
                if r < minr[0]:
                    minr = (r, rec)
                a1 = Fraction(rec["a1"])
                if a1 < mina1[0]:
                    mina1 = (a1, rec)
                if rec["c"] <= rec["dim"] + 2:
                    V = Fraction(rec["V"])
                    if V > maxV_small_c[0]:
                        maxV_small_c = (V, rec)
            if total["recorded"] % 2000 == 0:
                print(f"{total['recorded']} recorded ({total['tried']} tried), {time.time()-t0:.0f}s, negatives {total['negative']}, min ratio {minr[0]}, min a1 {mina1[0]}", flush=True)
            if total["recorded"] >= args.count:
                pool.terminate()
                break
    total["seconds"] = round(time.time() - t0, 1)
    total["min_ratio"] = str(minr[0])
    total["min_ratio_at"] = minr[1]
    total["min_a1"] = str(mina1[0])
    total["min_a1_at"] = mina1[1]
    total["max_volume_with_c_le_dim_plus_2"] = str(maxV_small_c[0])
    total["max_volume_at"] = maxV_small_c[1]
    total["args"] = vars(args)
    json.dump(total, open(args.out + ".summary.json", "w"), indent=1)
    print("done", json.dumps({k: v for k, v in total.items() if not k.endswith("_at")}), flush=True)


if __name__ == "__main__":
    main()
