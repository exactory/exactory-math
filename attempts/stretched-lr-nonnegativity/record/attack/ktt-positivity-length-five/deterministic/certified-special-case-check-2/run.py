#!/usr/bin/env python3
"""The Berline-Vergne weight in dimensions 1 to 5, computed by the defining recursion.

`bvweight.py` implements Proposition 4.1 of Berline-Vergne (arXiv:math/0507256): mu({0}) = 1 and
S(a) = sum over the faces f of a of mu(t(a,f)) I(f), which isolates mu(a) as a recursion on the
dimension, evaluated along a generic line so that every term is a Laurent series whose poles
cancel. The weight of a cone is the constant term. This run computes the weight on a fixed list
of cones where the answer is known or constrained, and records the values for the checker:

  * dimension 1: a half-line, weight 1/2;
  * dimension 2: unimodular cones, against the closed formula of Castillo-Liu Lemma 3.3;
  * dimension 2: the four vertex cones of the unit square, which must sum to the constant term 1;
  * dimension 2: a non-unimodular cone, against the valuation property under a subdivision into
    two unimodular cones sharing a ray;
  * dimension 3: unimodular and index-two cones, against Castillo-Liu Lemma 3.10;
  * dimensions 4 and 5: the orthants, which must be 1/16 and 1/32 by multiplicativity over
    orthogonal sums, and cones that split orthogonally as 2 + 2 and 2 + 3, against the product of
    the closed formulas;
  * dimension 5: an irreducible cone, recorded with its timing.

Output: `weights.json`.
"""
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from bvweight import SimplicialCone, weight  # noqa: E402


def I(n):
    return [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]


CASES = {
    "dim1_halfline": ([(1,)], 1),
    "dim2_orthant": ([(1, 0), (0, 1)], 2),
    "dim2_shear": ([(1, 0), (1, 1)], 2),
    "dim2_obtuse": ([(1, 0), (-1, 1)], 2),
    "dim2_square_b": ([(-1, 0), (0, 1)], 2),
    "dim2_square_c": ([(1, 0), (0, -1)], 2),
    "dim2_square_d": ([(-1, 0), (0, -1)], 2),
    "dim2_index3": ([(1, 1), (-1, 2)], 2),
    "dim2_index3_piece1": ([(1, 1), (0, 1)], 2),
    "dim2_index3_piece2": ([(0, 1), (-1, 2)], 2),
    "dim3_orthant": ([(1, 0, 0), (0, 1, 0), (0, 0, 1)], 3),
    "dim3_a": ([(1, 0, 0), (1, 1, 0), (0, 0, 1)], 3),
    "dim3_b": ([(1, 0, 0), (1, 1, 0), (1, 1, 1)], 3),
    "dim3_c": ([(1, 0, 0), (0, 1, 0), (1, 1, 1)], 3),
    "dim3_index2": ([(1, 1, 0), (0, 1, 1), (1, 0, 1)], 3),
    "dim4_orthant": ([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)], 4),
    "dim4_split22": ([(1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 1), (0, 0, 1, 0)], 4),
    "dim5_orthant": ([tuple(1 if j == i else 0 for j in range(5)) for i in range(5)], 5),
    "dim5_split23": ([(1, 1, 0, 0, 0), (1, 0, 0, 0, 0),
                      (0, 0, 1, 0, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 1)], 5),
    "dim5_irreducible": ([(1, 0, 0, 0, 0), (1, 1, 0, 0, 0), (1, 1, 1, 0, 0),
                          (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)], 5),
    "dim5_index2": ([(1, 1, 0, 0, 0), (0, 1, 1, 0, 0), (1, 0, 1, 0, 0),
                     (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)], 5),
}

out = {}
for name, (rays, n) in CASES.items():
    t0 = time.time()
    w = weight(list(rays), I(n))
    idx = SimplicialCone(list(rays), I(n)).index_of(tuple(range(len(rays))))
    out[name] = {"rays": [list(r) for r in rays], "dim": n, "index": idx,
                 "weight": str(w), "seconds": round(time.time() - t0, 3)}
    print(f"{name}: {w}  (index {idx}, {out[name]['seconds']}s)", flush=True)
json.dump(out, open(os.path.join(HERE, "weights.json"), "w"), indent=1)
print("done", flush=True)
