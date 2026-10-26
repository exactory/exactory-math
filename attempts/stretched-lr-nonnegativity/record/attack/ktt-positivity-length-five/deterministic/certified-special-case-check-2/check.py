#!/usr/bin/env python3
"""Independent check of the Berline-Vergne weights, by identities the recursion does not use.

Every test below is written here and shares no code with `bvweight.py`.

1. Dimension 1: a half-line has weight 1/2.
2. Dimension 2, unimodular cones: the closed formula of Castillo-Liu Lemma 3.3,
   alpha = 1/4 + (1/12)(<x,y>/<x,x> + <x,y>/<y,y>), rewritten here.
3. Dimension 2, the unit square: the four vertex weights sum to the Ehrhart constant term 1.
4. Dimension 2, a cone of index 3: the valuation property. Subdividing it along the interior ray
   (0,1) into two unimodular cones sharing that ray gives
   alpha(C) = alpha(C_1) + alpha(C_2) - alpha(ray), with alpha(ray) = 1/2. This tests the
   non-unimodular case without any closed formula.
5. Dimension 3: the closed formula of Castillo-Liu Lemma 3.10, rewritten here in terms of the
   Gram matrix of the rays.
6. Dimensions 4 and 5: the orthants must be 1/16 and 1/32, by multiplicativity over orthogonal
   sums of half-lines.
7. Dimensions 4 and 5: the cones that split orthogonally as 2 + 2 and 2 + 3 must equal the
   product of the weights of their blocks, computed here from the closed formulas.
Exit 0 iff every identity holds.
"""
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
W = json.load(open(os.path.join(HERE, "weights.json")))
bad = 0


def w(name):
    return Fraction(W[name]["weight"])


def dot(a, b):
    return Fraction(sum(p * q for p, q in zip(a, b)))


def closed2(x, y):
    return Fraction(1, 4) + Fraction(1, 12) * (dot(x, y) / dot(x, x) + dot(x, y) / dot(y, y))


def closed3(rays):
    H = [[dot(a, b) for b in rays] for a in rays]
    s = Fraction(1, 8)
    for i in range(3):
        for j in range(i + 1, 3):
            s += Fraction(1, 24) * H[i][j] * (Fraction(1) / H[i][i] + Fraction(1) / H[j][j])
    return s


def check(name, got, exp, what):
    global bad
    if got != exp:
        bad += 1
        print(f"MISMATCH {name}: {what}, computed {got}, expected {exp}")
    else:
        print(f"{name}: {got} agrees with {what}")


check("dim1_halfline", w("dim1_halfline"), Fraction(1, 2), "the weight of a half-line")
for name in ("dim2_orthant", "dim2_shear", "dim2_obtuse", "dim2_square_b", "dim2_square_c",
             "dim2_square_d", "dim2_index3_piece1", "dim2_index3_piece2"):
    rays = [tuple(r) for r in W[name]["rays"]]
    if W[name]["index"] == 1:
        check(name, w(name), closed2(*rays), "Castillo-Liu Lemma 3.3")
check("unit square", w("dim2_orthant") + w("dim2_square_b") + w("dim2_square_c") + w("dim2_square_d"),
      Fraction(1), "the sum of the vertex weights, the Ehrhart constant term")
check("dim2_index3", w("dim2_index3"),
      w("dim2_index3_piece1") + w("dim2_index3_piece2") - Fraction(1, 2),
      "the valuation property under the subdivision along (0,1)")
for name in ("dim3_orthant", "dim3_a", "dim3_b", "dim3_c", "dim3_index2"):
    rays = [tuple(r) for r in W[name]["rays"]]
    check(name, w(name), closed3(rays), "Castillo-Liu Lemma 3.10")
check("dim4_orthant", w("dim4_orthant"), Fraction(1, 16), "the fourth power of the half-line weight")
check("dim5_orthant", w("dim5_orthant"), Fraction(1, 32), "the fifth power of the half-line weight")
check("dim4_split22", w("dim4_split22"), closed2((1, 1), (1, 0)) * closed2((1, 1), (1, 0)),
      "multiplicativity over the orthogonal sum of two two-dimensional blocks")
check("dim5_split23", w("dim5_split23"),
      closed2((1, 1), (1, 0)) * closed3([(1, 0, 0), (1, 1, 0), (1, 1, 1)]),
      "multiplicativity over the orthogonal sum of a two- and a three-dimensional block")
print(f"dimension-five cones computed: irreducible {w('dim5_irreducible')} in "
      f"{W['dim5_irreducible']['seconds']} s, index two {w('dim5_index2')} in "
      f"{W['dim5_index2']['seconds']} s")
sys.exit(1 if bad else 0)
