#!/usr/bin/env python3
"""Two-dimensional hive polytopes against the Ehrhart polynomials of lattice polygons.

Enumerate the canonical triples (lam, mu, nu) with at most `parts` parts and |lam| <= `size`
(the canonical form and the enumeration order of the earlier box scan: mu >= nu
lexicographically, no common column at the largest length), keep those with
c = c^{lam}_{mu nu} >= 3 (lrcalc, the classical rule) whose hive polytope H has affine
dimension exactly 2 (Normaliz), and compute the Ehrhart quasi-polynomial of H (Normaliz).

For a rational polygon with quasi-period 1 the Ehrhart polynomial is
    P(t) = A t^2 + (b/2) t + 1,  with  b = P(1) - P(-1)  and  i = P(-1)
(reciprocity), where b counts the lattice points on the boundary and i the interior ones.
The polynomial is the Ehrhart polynomial of a lattice polygon exactly when b >= 3 and
Scott's inequality holds: if i >= 1 then b <= 2i + 6, or (i, b) = (1, 9) (Scott 1976).
A two-dimensional hive polytope whose (i, b) violates this is not Ehrhart-equivalent to any
lattice polygon. Output: summary JSON on stdout; `dim2-records.jsonl` (every
two-dimensional hive with c, i, b, maxden, period and polynomial) in the output directory.
"""
import json
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities, normalize  # noqa: E402


def partitions(n, max_parts, max_part=None):
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


def contained(inner, outer):
    return len(inner) <= len(outer) and all(inner[i] <= outer[i] for i in range(len(inner)))


def canonical(lam, mu, nu):
    lam, mu, nu = normalize(lam), normalize(mu), normalize(nu)
    if mu < nu:
        mu, nu = nu, mu
    n = max(len(lam), len(mu), len(nu))
    if len(lam) == n and n > 0:
        if (len(mu) == n) or (len(nu) == n):
            return None
    return lam, mu, nu


def triples(parts, size):
    seen = set()
    for N in range(1, size + 1):
        for lam in partitions(N, parts):
            for a in range(0, N + 1):
                for mu in partitions(a, parts):
                    if not contained(mu, lam):
                        continue
                    for nu in partitions(N - a, parts):
                        if not contained(nu, lam):
                            continue
                        tr = canonical(lam, mu, nu)
                        if tr is None or tr in seen:
                            continue
                        seen.add(tr)
                        yield tr


def analyse(triple):
    import lrcalc  # type: ignore
    from PyNormaliz import Cone  # type: ignore

    lam, mu, nu = triple
    c = int(lrcalc.lrcoef(list(lam), list(mu), list(nu)))
    if c < 3:
        return {"c": c, "skipped": "c<3"}
    D, rows = hive_inequalities(lam, mu, nu)
    C = Cone(inhom_inequalities=rows)
    dim = C.AffineDim()
    if dim != 2:
        return {"c": c, "dim": dim, "skipped": "dim!=2"}
    verts = C.VerticesOfPolyhedron()
    maxden = max(v[-1] for v in verts) if verts else 1
    q = C.EhrhartQuasiPolynomial()
    den = q[-1]
    period = len(q) - 1
    rec = {"lam": list(lam), "mu": list(mu), "nu": list(nu), "c": c, "dim": 2, "maxden": maxden,
           "nverts": len(verts), "period": period}
    if period != 1:
        rec["quasi"] = [[str(Fraction(x, den)) for x in comp] for comp in q[:-1]]
        return rec
    coeffs = [Fraction(x, den) for x in q[0]]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    rec["coeffs"] = [str(x) for x in coeffs]
    P = lambda t: sum(cf * Fraction(t) ** k for k, cf in enumerate(coeffs))
    p1, pm1 = P(1), P(-1)
    assert p1 == c
    b = p1 - pm1
    i = pm1
    rec["b"] = str(b)
    rec["i"] = str(i)
    lattice_ok = b >= 3 and (i == 0 or b <= 2 * i + 6 or (i, b) == (1, 9))
    rec["lattice_polygon_ehrhart"] = bool(lattice_ok)
    return rec


def main():
    spec = json.load(open(sys.argv[1]))
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(outdir, exist_ok=True)
    t0 = time.time()
    parts, size, workers = spec["parts"], spec["size"], spec.get("workers", 6)
    counts = {"triples": 0, "c_ge_3": 0, "dim2": 0, "period_not_1": 0, "lattice_polygon_ehrhart": 0,
              "not_lattice_polygon_ehrhart": 0, "by_maxden": {}, "by_ib": {}}
    violations = []
    with Pool(workers) as pool, open(os.path.join(outdir, "dim2-records.jsonl"), "w") as out:
        for rec in pool.imap_unordered(analyse, triples(parts, size), chunksize=64):
            counts["triples"] += 1
            if rec.get("skipped") == "c<3":
                continue
            counts["c_ge_3"] += 1
            if rec.get("skipped"):
                continue
            counts["dim2"] += 1
            out.write(json.dumps(rec) + "\n")
            md = str(rec["maxden"])
            counts["by_maxden"][md] = counts["by_maxden"].get(md, 0) + 1
            if rec["period"] != 1:
                counts["period_not_1"] += 1
                violations.append(rec)
                continue
            key = f"i={rec['i']},b={rec['b']},maxden={md}"
            counts["by_ib"][key] = counts["by_ib"].get(key, 0) + 1
            if rec["lattice_polygon_ehrhart"]:
                counts["lattice_polygon_ehrhart"] += 1
            else:
                counts["not_lattice_polygon_ehrhart"] += 1
                if len(violations) < 200:
                    violations.append(rec)
    counts["by_ib"] = dict(sorted(counts["by_ib"].items()))
    counts["violations_sample"] = violations[:50]
    counts["parts"] = parts
    counts["size"] = size
    counts["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(counts, indent=1))


if __name__ == "__main__":
    main()
