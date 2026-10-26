#!/usr/bin/env python3
"""Can the recorded Ehrhart data determine the codimension-five weights? An exact rank computation.

A valid McMullen local formula gives, for every polytope P whose facet normals lie in the
rank-five rhombus set N_5,

    a_1(P) = sum over the edges E of P of w(class(E)) * (lattice length of E),

one linear equation in the unknown weights. The weight is an invariant of the transverse cone
under the isometries of (Z^6, standard inner product), so the unknowns are indexed by the
isometry classes of the edge types (`isotypes.canonical`), and any class the system pins carries
that value for every valid local formula, whatever construction produced it.

This run builds that system from the edge data of `certified-special-case-check-1` (2,000
full-dimensional five-part hive polytopes), reduces it exactly over the rationals by sparse
Gauss-Jordan elimination, and reports the rank, the number of pinned classes, and the number of
distinct equations. Output: `system.summary.json`, `classes.json` (the canonical form of each
class and the types in it).
"""
import gzip
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from isotypes import canonical  # noqa: E402

CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")


def main():
    t0 = time.time()
    types = [tuple(tuple(x) for x in t) for t in json.load(open(os.path.join(CHECK1, "edge-types.json")))]
    canon_of, cls_of, members = {}, [], {}
    for i, t in enumerate(types):
        c = canonical(t)
        if c not in canon_of:
            canon_of[c] = len(canon_of)
        cls_of.append(canon_of[c])
        members.setdefault(canon_of[c], []).append(i)
    print(f"{len(types)} edge types -> {len(canon_of)} isometry classes, {time.time() - t0:.0f}s",
          flush=True)

    recs = [json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt")]
    rows = []
    for r in recs:
        d = {}
        for i, ln in r["edges"]:
            c = cls_of[i]
            d[c] = d.get(c, Fraction(0)) + Fraction(ln)
        rows.append((d, Fraction(r["a1"])))
    distinct = len({(tuple(sorted(d.items())), b) for d, b in rows})
    print(f"{len(rows)} equations, {distinct} distinct, {len(canon_of)} unknowns", flush=True)

    piv = {}
    inconsistent = 0
    for d, b in rows:
        d = dict(d)
        while d:
            c = min(d)
            if c not in piv:
                inv = Fraction(1) / d[c]
                piv[c] = ({k: v * inv for k, v in d.items()}, b * inv)
                d = None
                break
            pd, pb = piv[c]
            f = d[c]
            for k, v in pd.items():
                nv = d.get(k, Fraction(0)) - f * v
                if nv:
                    d[k] = nv
                elif k in d:
                    del d[k]
            b -= f * pb
        if d is not None and not d and b != 0:
            inconsistent += 1
    for c in sorted(piv, reverse=True):
        d, b = piv[c]
        for k in [k for k in d if k != c and k in piv]:
            pd, pb = piv[k]
            f = d[k]
            for kk, vv in pd.items():
                nv = d.get(kk, Fraction(0)) - f * vv
                if nv:
                    d[kk] = nv
                elif kk in d:
                    del d[kk]
            b -= f * pb
        piv[c] = (d, b)
    pinned = {c: b for c, (d, b) in piv.items() if len(d) == 1}

    summary = {"polytopes": len(rows), "distinct_equations": distinct,
               "edge_types": len(types), "isometry_classes": len(canon_of),
               "rank": len(piv), "pinned_classes": len(pinned),
               "inconsistent_equations": inconsistent,
               "pinned_values": {str(c): str(v) for c, v in sorted(pinned.items())},
               "class_size_histogram": {},
               "seconds": round(time.time() - t0, 1)}
    hist = {}
    for v in members.values():
        hist[len(v)] = hist.get(len(v), 0) + 1
    summary["class_size_histogram"] = {str(k): v for k, v in sorted(hist.items())}
    json.dump(summary, open(os.path.join(HERE, "system.summary.json"), "w"), indent=1)
    json.dump({"canonical": [list(map(list, c)) for c, _ in sorted(canon_of.items(), key=lambda kv: kv[1])],
               "members": {str(k): v for k, v in sorted(members.items())}},
              open(os.path.join(HERE, "classes.json"), "w"))
    print("done", json.dumps({k: v for k, v in summary.items() if k != "pinned_values"}), flush=True)


if __name__ == "__main__":
    main()
