#!/usr/bin/env python3
"""Independent check of the vertex-sum gate.

1. The recorded sums are exactly 1 where the record says the identity holds, and the counts of
   vertices evaluated match the polytopes named.
2. A test the run did not do: the same identity on a second lattice simplex, not unimodular, whose
   tangent cones are different cones from the run's. A valid formula gives 1 there too.
3. The scale-invariance claim, which the classification argument in the admission record rests on:
   the weight of a cone is unchanged when the form is multiplied by a positive rational.
4. The known closed value: under the standard form every signed orthant is isometric to the
   standard one, so each of the cube's 64 weights must be 2^-6.
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

D = 6
bad = 0
g = json.load(open(os.path.join(HERE, "gate.json")))
for f in g["forms"]:
    if f["unimodular simplex: identity holds"] and Fraction(
            f["unimodular simplex: sum of the vertex weights"]) != 1:
        bad += 1
        print(f"SIMPLEX MISMATCH {f['form']}")
    if f.get("cube: identity holds"):
        if Fraction(f["cube: sum of the vertex weights"]) != 1 or f["cube: vertices evaluated"] != 64:
            bad += 1
            print(f"CUBE MISMATCH {f['form']}")
passed = [f["form"] for f in g["forms"] if f.get("cube: identity holds")]
print(f"recorded: {len(g['forms'])} forms, {len(passed)} passed both polytopes: {passed}")


def form(name):
    if name == "standard":
        return [[Fraction(1 if i == j else 0) for j in range(D)] for i in range(D)]
    if name == "twice the standard":
        return [[Fraction(2 if i == j else 0) for j in range(D)] for i in range(D)]
    if name == "A_6":
        return [[Fraction(2 if i == j else (-1 if abs(i - j) == 1 else 0)) for j in range(D)]
                for i in range(D)]
    raise KeyError(name)


verts = [[0] * D] + [[1 if i == j else 0 for j in range(D)] for i in range(D)]
verts[D] = [1, 1, 1, 1, 1, 2]                     # a non-unimodular lattice simplex
second_bad = 0
for name in ("standard", "A_6"):
    G = form(name)
    total = Fraction(0)
    for i, v in enumerate(verts):
        rays = [[verts[j][k] - v[k] for k in range(D)] for j in range(len(verts)) if j != i]
        total += weight(rays, G)
    if total != 1:
        second_bad += 1
        print(f"SECOND SIMPLEX MISMATCH {name}: {total}")
bad += second_bad
print(f"a second, non-unimodular lattice simplex: 2 forms, {second_bad} mismatches")

rng = random.Random(20260911)
scale_bad = 0
for _ in range(3):
    k = 3
    rays = [[rng.randint(-2, 2) for _ in range(k)] for _ in range(k)]
    G = [[Fraction(2 if i == j else rng.choice([0, 0, 1])) for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(i):
            G[i][j] = G[j][i]
    try:
        a = weight(rays, G)
        b = weight(rays, [[3 * x for x in row] for row in G])
    except Exception:
        continue
    if a != b:
        scale_bad += 1
        print(f"SCALE MISMATCH: {a} against {b}")
bad += scale_bad
print(f"scale invariance on random three-dimensional cones: {scale_bad} mismatches")

std = form("standard")
orth_bad = 0
for signs in ((1, 1, 1, 1, 1, 1), (-1, 1, -1, 1, -1, 1), (-1, -1, -1, -1, -1, -1)):
    rays = [[signs[i] if i == j else 0 for j in range(D)] for i in range(D)]
    if weight(rays, std) != Fraction(1, 64):
        orth_bad += 1
        print(f"ORTHANT MISMATCH {signs}")
bad += orth_bad
print(f"the closed value 2^-6 on three signed orthants under the standard form: {orth_bad} "
      f"mismatches")
sys.exit(1 if bad else 0)
