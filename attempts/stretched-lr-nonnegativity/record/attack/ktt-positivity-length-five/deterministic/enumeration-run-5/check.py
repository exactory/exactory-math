#!/usr/bin/env python3
"""Independent check of the projected atlas.

1. The summary recomputed from `types.jsonl` and `projected.jsonl`.
2. The identity recomputed from scratch on a sample of contracted polytopes, with no cache, so
   that a wrong cache key cannot hide behind a right answer. That failure mode occurred once and
   the identity caught it: types were keyed by the normal set alone, but the weight depends on the
   intrinsic lattice as well, and two contracted polytopes can share a normal set and carry
   different lattices.
3. The contraction checks on a sample: the intrinsic lattice saturated, the basis generating it
   rather than a sublattice, the Gram recomputed from ambient inner products, and positive
   definite.
4. The seven two-dimensional weights of move 18, recomputed here because a route decision rests on
   them, together with the identity that makes negativity in dimension two a consequence: the
   vertex weights of a lattice polygon sum to one.
Exit 0 iff all four hold.
"""
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from bvweight import weight  # noqa: E402
from contract import Contracted  # noqa: E402
from run import contracted_polytope, edges_of  # noqa: E402
from transverse_q import transverse_weight_q  # noqa: E402

bad = 0
s = json.load(open(os.path.join(HERE, "projected.summary.json")))
types = [json.loads(l) for l in open(os.path.join(HERE, "types.jsonl"))]
recs = [json.loads(l) for l in open(os.path.join(HERE, "projected.jsonl"))]
weighed = [t for t in types if t["weight"] is not None]
by_dim = {}
for t in types:
    by_dim[str(t["intrinsic dimension"])] = by_dim.get(str(t["intrinsic dimension"]), 0) + 1
recomputed = {
    "polytopes contracted": len(recs),
    "identity mismatches": sum(1 for r in recs if r["identity holds"] is False),
    "distinct types, keyed by the normal set in the intrinsic lattice": len(types),
    "types by intrinsic dimension": by_dim,
    "types weighed": len(weighed),
    "types with a negative weight": sum(1 for t in weighed if Fraction(t["weight"]) < 0),
    "most negative weight": str(min(Fraction(t["weight"]) for t in weighed)),
}
for k, v in recomputed.items():
    if s[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: {s[k]} against {v}")
print(f"summary: {len(recs)} polytopes, {recomputed['identity mismatches']} identity mismatches, "
      f"{len(types)} types of which {len(weighed)} weighed, "
      f"{recomputed['types with a negative weight']} negative, minimum "
      f"{recomputed['most negative weight']}")

rng = random.Random(20260916)
sample = rng.sample([r for r in recs if r["identity holds"] is True], 8)
fresh_bad = check_bad = 0
for r in sample:
    C = Contracted(r["lam"], r["mu"], r["nu"])
    if not all(C.checks.values()):
        check_bad += 1
        print(f"CONTRACTION CHECK FAILED {r['lam']}: {C.checks}")
    verts, sup, normals = contracted_polytope(C)
    edges = edges_of(C, verts, sup, normals)
    total = Fraction(0)
    for ns, length in edges:
        total += transverse_weight_q([list(v) for v in ns], C.gram, C.dim) * length
    if total != Fraction(r["a1 recorded"]):
        fresh_bad += 1
        print(f"FRESH IDENTITY MISMATCH {r['lam']} {r['mu']} {r['nu']}: {total} against "
              f"{r['a1 recorded']}")
bad += fresh_bad + check_bad
print(f"recomputed with no cache on {len(sample)} contracted polytopes: {fresh_bad} identity "
      f"mismatches, {check_bad} failed contraction checks")

I2 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
table = {((1, 0), (1, 1)): "3/8", ((1, 0), (-1, 1)): "1/8", ((1, 0), (-2, 1)): "1/20",
         ((1, 0), (-5, 1)): "-19/104", ((1, 0), (-20, 1)): "-2279/1604",
         ((20, 1), (-20, 1)): "-2279/802", ((1, 0), (100, 1)): "343401/40004"}
tab_bad = 0
for rays, want in table.items():
    got = weight([list(r) for r in rays], I2)
    if got != Fraction(want):
        tab_bad += 1
        print(f"MOVE 18 TABLE MISMATCH {rays}: {got} against {want}")
tri = (weight([[1, 0], [1, 1]], I2) + weight([[-1, 0], [0, 1]], I2)
       + weight([[-1, -1], [0, -1]], I2))
if tri != 1:
    tab_bad += 1
    print(f"POLYGON IDENTITY MISMATCH on the unimodular triangle: {tri}")
bad += tab_bad
print(f"the seven two-dimensional weights of move 18 and the polygon identity on the unimodular "
      f"triangle: {tab_bad} mismatches")
sys.exit(1 if bad else 0)
