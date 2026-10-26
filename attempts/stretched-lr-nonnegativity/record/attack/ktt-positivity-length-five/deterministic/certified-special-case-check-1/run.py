#!/usr/bin/env python3
"""Validate the local Ehrhart formula extraction on full-dimensional five-part hive polytopes.

For each polytope the top three coefficients are recomputed from the faces:

    a_D     = relvol(P),
    a_{D-1} = (1/2) * sum over facets of relvol(facet),
    a_{D-2} = sum over codimension-two faces of alpha(u, v) * relvol(face),

with alpha the closed weight of a two-dimensional transverse cone (Castillo-Liu Lemma 3.3) and
u, v the extreme rays of the face's normal cone, and compared with the coefficients recorded by
`enumeration-run-2` of the box attack, which Normaliz computed from the Ehrhart series and lrcalc
independently pinned. Agreement checks the whole extraction: the outward normals, the face
lattice, the relative volumes, the dilation convention for the rational polytope, and the weight.

The run also records the edge data the codimension-five step needs: for every polytope, the
edges with their lattice lengths and the set of outward normals of the facets containing them,
which is the transverse cone type of the edge.

Output: `validation.summary.json`, `edge-types.json` (the type census), `edges.jsonl.gz` (one
record per polytope: the triple, its linear coefficient, and its edges as type index and length).
"""
import glob
import gzip
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from localform import HivePolytope, alpha_pair, ext_rays  # noqa: E402

RUN2 = os.path.join(HERE, "..", "..", "..", "stretched-lr-polynomial-negative-coefficient",
                    "deterministic", "enumeration-run-2")


def records(limit):
    out = []
    for fn in sorted(glob.glob(os.path.join(RUN2, "scan-n5-*.jsonl"))):
        with open(fn) as f:
            for line in f:
                r = json.loads(line)
                if r.get("dim") == 6:
                    out.append(r)
                    if len(out) >= limit:
                        return out
    return out


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    recs = records(limit)
    t0 = time.time()
    agree = 0
    mismatches = []
    types = {}
    per_poly = []
    facet_hist = {}
    for i, r in enumerate(recs):
        P = HivePolytope(r["lam"], r["mu"], r["nu"])
        assert P.is_full_dimensional() and P.dim == 6
        a = [Fraction(x) for x in r["coeffs"]]
        faces = P.faces_by_codim(2)
        got = {6: faces[0][0][1],
               5: sum(v for _, v in faces[1]) / 2,
               4: sum(alpha_pair(P.normals[i0], P.normals[i1]) * v
                      for act, v in faces.get(2, [])
                      for i0, i1 in [ext_rays(P, act)])}
        ok = all(a[k] == got[k] for k in got)
        agree += ok
        if not ok:
            mismatches.append({"lam": r["lam"], "mu": r["mu"], "nu": r["nu"],
                               "recorded": {str(k): str(a[k]) for k in got},
                               "local": {str(k): str(v) for k, v in got.items()}})
        E = P.edges()
        ids = []
        for t, ln in E:
            key = json.dumps([list(x) for x in t])
            if key not in types:
                types[key] = len(types)
            ids.append([types[key], str(ln)])
        per_poly.append({"lam": r["lam"], "mu": r["mu"], "nu": r["nu"],
                         "a1": str(a[1]), "edges": ids})
        facet_hist[len(P.support)] = facet_hist.get(len(P.support), 0) + 1
        if (i + 1) % 200 == 0:
            print(f"{i + 1} polytopes, {agree} agree, {len(types)} edge types, "
                  f"{time.time() - t0:.0f}s", flush=True)
    with gzip.open(os.path.join(HERE, "edges.jsonl.gz"), "wt") as f:
        for rec in per_poly:
            f.write(json.dumps(rec) + "\n")
    inv = [None] * len(types)
    for key, idx in types.items():
        inv[idx] = json.loads(key)
    json.dump(inv, open(os.path.join(HERE, "edge-types.json"), "w"))
    summary = {"polytopes": len(recs), "agree_top_three": agree, "mismatches": len(mismatches),
               "edge_types": len(types),
               "edges_total": sum(len(p["edges"]) for p in per_poly),
               "facets_histogram": {str(k): v for k, v in sorted(facet_hist.items())},
               "type_size_histogram": {},
               "seconds": round(time.time() - t0, 1)}
    hs = {}
    for t in inv:
        hs[len(t)] = hs.get(len(t), 0) + 1
    summary["type_size_histogram"] = {str(k): v for k, v in sorted(hs.items())}
    json.dump(summary, open(os.path.join(HERE, "validation.summary.json"), "w"), indent=1)
    json.dump(mismatches, open(os.path.join(HERE, "validation.mismatches.json"), "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
