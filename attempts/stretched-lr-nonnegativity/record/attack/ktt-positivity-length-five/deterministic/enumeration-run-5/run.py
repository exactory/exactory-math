#!/usr/bin/env python3
"""The projected atlas: transverse cone types of the non-full-dimensional five-part hives.

Move 11 reduced obligation O-B to the same problem in the intrinsic lattice one dimension lower.
Move 18 removed the shortcut that would have closed the low dimensions by citation: the weight of
a two-dimensional cone is already negative when the cone is wide enough, so this project's
positivity at codimensions two and three is about cones spanned by the twenty-seven rank-five
normals and not about all cones of those dimensions.

So each intrinsic dimension needs its own atlas, and this run builds it. For a five-part triple
whose hive polytope has intrinsic dimension d < 6:

  * `contract.py` translates by a lattice point of the polytope, takes the lattice of the linear
    span saturated in the ambient lattice, and expresses the polytope and the hive rows in a basis
    of it, carrying the induced Gram;
  * the polytope is rebuilt in those coordinates, its vertices and irredundant facets taken from
    Normaliz, and its edges found as the vertex pairs whose common tight facets have rank d - 1;
  * the transverse cone of an edge is built by `transverse_q.py` with the induced Gram in place of
    the identity, and its weight by the same recursion the full-dimensional case used.

Before any type is recorded the run validates the whole chain end to end: the local formula in the
intrinsic lattice must reproduce the certified linear coefficient of the polytope exactly. That is
the identity the full-dimensional case used, and it exercises the contraction, the coordinate
change and the induced Gram together.
"""
from __future__ import annotations

import glob
import json
import os
import sys
import time
from fractions import Fraction
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from contract import Contracted  # noqa: E402
from localform import prim, rank_of  # noqa: E402
from transverse_q import transverse_weight_q  # noqa: E402

BOX = os.path.join(HERE, "..", "..", "..", "stretched-lr-polynomial-negative-coefficient",
                   "deterministic", "enumeration-run-2")
BUDGET = float(os.environ.get("BUDGET", "1600"))
DIMS = tuple(int(x) for x in os.environ.get("DIMS", "3,4,5").split(","))
WEIGH = tuple(int(x) for x in os.environ.get("WEIGH", "3,4").split(","))


def contracted_polytope(C: Contracted):
    """(vertices, support hyperplanes, outward primitive normals) in the intrinsic coordinates."""
    from PyNormaliz import Cone  # type: ignore

    rows = [list(f) + [c] for f, c in C.rows_in_basis()]
    rows = [r for r in rows if any(r[:-1])]
    K = Cone(inhom_inequalities=rows)
    assert K.AffineDim() == C.dim, "the contracted polytope changed dimension"
    verts = [tuple(Fraction(x, v[-1]) for x in v[:C.dim]) for v in K.VerticesOfPolyhedron()]
    sup = K.SupportHyperplanes()
    normals = [prim([-a for a in h[:C.dim]]) for h in sup]
    return verts, sup, normals


def edges_of(C: Contracted, verts, sup, normals):
    """Edges as (normal set, lattice length), in the intrinsic lattice."""
    def tight(p):
        return [i for i, h in enumerate(sup)
                if sum(Fraction(h[j]) * p[j] for j in range(C.dim)) + h[C.dim] == 0]

    acts = [tight(p) for p in verts]
    out = []
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            common = sorted(set(acts[i]) & set(acts[j]))
            if len(common) < C.dim - 1:
                continue
            if rank_of([sup[k][: C.dim] for k in common]) != C.dim - 1:
                continue
            p, q = verts[i], verts[j]
            d = [b - a for a, b in zip(p, q)]
            den = 1
            for x in d:
                den = den * x.denominator // gcd(den, x.denominator)
            di = [int(x * den) for x in d]
            g = 0
            for x in di:
                g = gcd(g, abs(x))
            out.append((tuple(sorted(normals[k] for k in common)), Fraction(g, den)))
    return out


def main():
    t0 = time.time()
    paths = sorted(glob.glob(os.path.join(BOX, "scan-n5-*.jsonl")))
    types: dict = {}
    out = open(os.path.join(HERE, "projected.jsonl"), "w")
    seen = validated = mismatched = 0
    skipped: dict = {}
    for path in paths:
        for line in open(path):
            if time.time() - t0 > BUDGET:
                break
            rec = json.loads(line)
            if "coeffs" in rec:
                p = [Fraction(x) for x in rec["coeffs"]]
            elif "num" in rec:
                p = [Fraction(x, rec["den"]) for x in rec["num"]]
            else:
                continue
            while len(p) > 1 and p[-1] == 0:
                p.pop()
            D = len(p) - 1
            if D not in DIMS:
                continue
            try:
                C = Contracted(rec["lam"], rec["mu"], rec["nu"])
            except Exception as exc:
                skipped[type(exc).__name__] = skipped.get(type(exc).__name__, 0) + 1
                continue
            if not all(C.checks.values()):
                skipped["contraction checks failed"] = skipped.get("contraction checks failed", 0) + 1
                print(f"CONTRACTION CHECK FAILED {rec['lam']} {rec['mu']} {rec['nu']}: {C.checks}",
                      flush=True)
                continue
            if C.dim != D:
                skipped["dimension disagreed with the polynomial degree"] = \
                    skipped.get("dimension disagreed with the polynomial degree", 0) + 1
                continue
            verts, sup, normals = contracted_polytope(C)
            edges = edges_of(C, verts, sup, normals)
            gkey = tuple(tuple(int(x) if x.denominator == 1 else (x.numerator, x.denominator)
                                for x in row) for row in
                         [[Fraction(v) for v in r] for r in C.gram])
            for ns, _ in edges:
                types.setdefault((tuple(ns), gkey), {"dim": C.dim, "weight": None,
                                                     "gram": [[str(Fraction(v)) for v in r]
                                                              for r in C.gram]})
            seen += 1
            ok = None
            if C.dim in WEIGH:
                total = Fraction(0)
                for ns, length in edges:
                    key = (tuple(ns), gkey)
                    if types[key]["weight"] is None:
                        types[key]["weight"] = transverse_weight_q([list(v) for v in ns],
                                                                   C.gram, C.dim)
                    total += types[key]["weight"] * length
                ok = total == p[1]
                validated += ok
                mismatched += not ok
                if not ok:
                    print(f"IDENTITY MISMATCH {rec['lam']} {rec['mu']} {rec['nu']}: {total} "
                          f"against {p[1]}", flush=True)
            out.write(json.dumps({"lam": rec["lam"], "mu": rec["mu"], "nu": rec["nu"],
                                  "intrinsic dimension": C.dim, "edges": len(edges),
                                  "a1 recorded": str(p[1]),
                                  "a1 from the local formula": str(total) if ok is not None else None,
                                  "identity holds": ok}) + "\n")
            out.flush()
            if seen % 25 == 0:
                neg = sum(1 for v in types.values() if v["weight"] is not None and v["weight"] < 0)
                print(f"{seen} polytopes, {len(types)} types, {neg} negative, {mismatched} "
                      f"identity mismatches, {round(time.time() - t0)} s", flush=True)
    out.close()

    with open(os.path.join(HERE, "types.jsonl"), "w") as f:
        for k, v in types.items():
            f.write(json.dumps({"normals": [list(x) for x in k[0]], "gram": v["gram"],
                                "intrinsic dimension": v["dim"],
                                "weight": str(v["weight"]) if v["weight"] is not None else None})
                    + "\n")
    weighed = {k: v["weight"] for k, v in types.items() if v["weight"] is not None}
    neg = {k: w for k, w in weighed.items() if w < 0}
    by_dim = {}
    for v in types.values():
        by_dim[v["dim"]] = by_dim.get(v["dim"], 0) + 1
    summary = {
        "intrinsic dimensions": list(DIMS),
        "polytopes contracted": seen,
        "polytopes where the local formula reproduces the certified coefficient": validated,
        "identity mismatches": mismatched,
        "distinct types, keyed by the normal set in the intrinsic lattice": len(types),
        "types by intrinsic dimension": dict(sorted(by_dim.items())),
        "types weighed": len(weighed),
        "types with a negative weight": len(neg),
        "most negative weight": str(min(weighed.values())) if weighed else None,
        "largest weight": str(max(weighed.values())) if weighed else None,
        "skipped": skipped,
        "note": ("a type is keyed by the normal set together with the Gram of the intrinsic "
                 "lattice, because the weight depends on both: two contracted polytopes can share "
                 "a normal set and carry different lattices. Types are not merged by isometry, so the count "
                 "is an upper bound on the number of classes; the sign census is unaffected. "
                 "Carrying the induced form is a choice, not forced: a different positive-definite "
                 "form on the same lattice gives a different sign census, as move 16 measured, "
                 "twenty-one negatives against five. The end-to-end identity tests validity and "
                 "cannot see the form, so the contraction is checked directly instead."),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "projected.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
