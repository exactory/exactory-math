#!/usr/bin/env python3
"""Stratified scan of stretched Littlewood-Richardson polynomials.

For each triple (lam, mu, nu) in a stratum the scan records: c = c^{lam}_{mu nu}
(lrcalc, the classical rule), dim H, the Ehrhart polynomial of the hive polytope
(Normaliz), the maximal vertex denominator, the number M of leading factors
(t+1)...(t+M) (Ehrhart reciprocity: P(-m) = 0 for m <= M), and the minimal
coefficient with its index.  Output: JSON lines.

Two modes.
  sample:  seeded random triples per stratum (n_parts, |lam|), canonicalised.
  enumerate: every triple of the stratum in a fixed order (optionally capped).
Canonical form: mu >= nu lexicographically; no common column in (lam, mu) or
(lam, nu) at the largest length n (column removal keeps P and shrinks the size).
Only triples with c >= 3 and dim H >= 3 are worth a polynomial (c <= 2 and
dim <= 2 are positive by theorem); the others are counted but not recorded.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities, normalize  # noqa: E402


def partitions(n: int, max_parts: int, max_part: int | None = None):
    """Partitions of n with at most max_parts parts and parts <= max_part."""
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    if max_parts == 0:
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, max_parts - 1, first):
            yield (first,) + rest


def contained(inner, outer) -> bool:
    return len(inner) <= len(outer) and all(inner[i] <= outer[i] for i in range(len(inner)))


def canonical(lam, mu, nu):
    """Return the canonical representative or None if the triple is reducible."""
    lam, mu, nu = normalize(lam), normalize(mu), normalize(nu)
    if mu < nu:
        mu, nu = nu, mu
    n = max(len(lam), len(mu), len(nu))
    if len(lam) == n and n > 0:
        if (len(mu) == n) or (len(nu) == n):
            return None  # a common column at length n: reducible to a smaller triple
    return lam, mu, nu


def lr_coef(lam, mu, nu) -> int:
    import lrcalc  # type: ignore

    return int(lrcalc.lrcoef(list(lam), list(mu), list(nu)))


def analyse(triple):
    """Full record for one triple, or a short record when it is not worth a polynomial."""
    from PyNormaliz import Cone  # type: ignore

    lam, mu, nu = triple
    c = lr_coef(lam, mu, nu)
    rec = {"lam": list(lam), "mu": list(mu), "nu": list(nu), "n": max(len(lam), len(mu), len(nu)),
           "N": sum(lam), "c": c}
    if c < 3:
        rec["skipped"] = "c<3"
        return rec
    D, rows = hive_inequalities(lam, mu, nu)
    C = Cone(inhom_inequalities=rows)
    dim = C.AffineDim()
    rec["dim"] = dim
    if dim < 3:
        rec["skipped"] = "dim<3"
        return rec
    verts = C.VerticesOfPolyhedron()
    maxden = max(v[-1] for v in verts) if verts else 1
    rec["maxden"] = maxden
    rec["nverts"] = len(verts)
    q = C.EhrhartQuasiPolynomial()
    den = q[-1]
    period = len(q) - 1
    rec["period"] = period
    if period != 1:
        rec["quasi"] = [[str(Fraction(x, den)) for x in comp] for comp in q[:-1]]
        return rec
    coeffs = [Fraction(x, den) for x in q[0]]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    rec["deg"] = len(coeffs) - 1
    rec["coeffs"] = [str(x) for x in coeffs]
    mval = min(coeffs)
    rec["min_coeff"] = str(mval)
    rec["min_index"] = coeffs.index(mval)
    rec["a1"] = str(coeffs[1]) if len(coeffs) > 1 else "0"
    rec["negative"] = mval < 0
    # leading factors (t+1)...(t+M): P(-m) == 0 for m = 1..M
    M = 0
    for m in range(1, len(coeffs) + 1):
        if sum(cf * Fraction(-m) ** i for i, cf in enumerate(coeffs)) == 0:
            M += 1
        else:
            break
    rec["M"] = M
    Dd = len(coeffs) - 1
    rec["Lint1"] = str(abs(sum(cf * Fraction(-1) ** i for i, cf in enumerate(coeffs))))
    rec["hstar1"] = c - Dd - 1
    return rec


def random_partition(rng: random.Random, n: int, max_parts: int, max_part: int):
    """Uniform-ish random partition of n with the given bounds (rejection on a random composition)."""
    for _ in range(10000):
        k = rng.randint(1, max_parts)
        cuts = sorted(rng.sample(range(1, n + k), k - 1)) if k > 1 else []
        parts = sorted([b - a - 1 for a, b in zip([0] + cuts, cuts + [n + k])], reverse=True)
        parts = tuple(p for p in parts if p > 0)
        if sum(parts) == n and len(parts) <= max_parts and (not parts or parts[0] <= max_part):
            return parts
    return None


def sample_triples(rng, n_parts: int, N: int, count: int, max_part: int):
    """Random canonical triples with max length exactly n_parts and |lam| = N."""
    seen = set()
    out = []
    tries = 0
    while len(out) < count and tries < 200 * count:
        tries += 1
        lam = random_partition(rng, N, n_parts, max_part)
        if lam is None or len(lam) > n_parts:
            continue
        m = rng.randint(1, N - 1)
        mu = random_partition(rng, m, n_parts, lam[0])
        nu = random_partition(rng, N - m, n_parts, lam[0])
        if mu is None or nu is None:
            continue
        if not contained(mu, lam) or not contained(nu, lam):
            continue
        can = canonical(lam, mu, nu)
        if can is None:
            continue
        if max(len(can[0]), len(can[1]), len(can[2])) != n_parts:
            continue
        if can in seen:
            continue
        seen.add(can)
        out.append(can)
    return out


def enumerate_triples(n_parts: int, N: int, max_part: int, cap: int | None = None):
    """Every canonical triple with max length exactly n_parts, |lam| = N, parts <= max_part."""
    out = []
    for lam in partitions(N, n_parts, max_part):
        for m in range(1, N):
            for mu in partitions(m, n_parts, lam[0]):
                if not contained(mu, lam):
                    continue
                for nu in partitions(N - m, n_parts, lam[0]):
                    if nu > mu or not contained(nu, lam):
                        continue
                    can = canonical(lam, mu, nu)
                    if can is None:
                        continue
                    if max(len(can[0]), len(can[1]), len(can[2])) != n_parts:
                        continue
                    out.append(can)
                    if cap is not None and len(out) >= cap:
                        return out
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["sample", "enumerate"], required=True)
    ap.add_argument("--parts", type=int, nargs="+", required=True, help="max lengths (strata)")
    ap.add_argument("--sizes", type=int, nargs="+", required=True, help="|lam| values (strata)")
    ap.add_argument("--count", type=int, default=1000, help="sample: triples per stratum")
    ap.add_argument("--cap", type=int, default=None, help="enumerate: cap per stratum")
    ap.add_argument("--max-part", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20260903)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    triples = []
    for n_parts in args.parts:
        for N in args.sizes:
            if args.mode == "sample":
                triples += sample_triples(rng, n_parts, N, args.count, args.max_part)
            else:
                triples += enumerate_triples(n_parts, N, args.max_part, args.cap)
    print(f"{len(triples)} candidate triples", flush=True)
    t0 = time.time()
    done = 0
    negatives = 0
    with Pool(args.workers) as pool, open(args.out, "w") as f:
        for rec in pool.imap_unordered(analyse, triples, chunksize=8):
            f.write(json.dumps(rec) + "\n")
            done += 1
            if rec.get("negative"):
                negatives += 1
                print("NEGATIVE", json.dumps(rec), flush=True)
                f.flush()
            if done % 2000 == 0:
                print(f"{done}/{len(triples)} in {time.time()-t0:.0f}s, negatives {negatives}", flush=True)
    print(f"done {done} triples in {time.time()-t0:.0f}s, negatives {negatives}", flush=True)


if __name__ == "__main__":
    main()
