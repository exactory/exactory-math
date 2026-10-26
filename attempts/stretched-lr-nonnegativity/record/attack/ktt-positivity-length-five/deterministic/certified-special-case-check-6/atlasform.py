#!/usr/bin/env python3
"""The linear functional the linear Ehrhart coefficient becomes on a cell, from the local formula.

On the relative interior of a cell of the chamber complex the hive polytope keeps its face
lattice, so each edge keeps the set of facet normals through it, hence its transverse cone and
its Berline-Vergne weight, while its lattice length is a linear function of the boundary triple.
The local Euler-Maclaurin formula then reads

    a1(b) = sum over the edges e of  w(class of e) * (lattice length of e)(b),

a linear functional. Taking it this way costs nothing per triple, unlike a finite difference of
Ehrhart coefficients, so a cell at a large generic triple is as cheap as a cell at a small one.

The weights come from the codimension-five atlas of `enumeration-run-1` when the class is in it
and from `bvweight` through `transverse` when it is not; new weights are cached on disk.
"""
from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from math import gcd
from typing import Dict, List, Sequence, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chamber import Chamber, ChamberCone, _rref, primitive  # noqa: E402
from isotypes import canonical  # noqa: E402
from localform import prim, rank_of  # noqa: E402


class WeightBook:
    """Berline-Vergne weights of codimension-five transverse cone types, atlas first, cache next."""

    def __init__(self, atlas_path: str, cache_path: str):
        self.weights: Dict[tuple, Fraction] = {}
        self.cache_path = cache_path
        self.computed = 0
        for line in open(atlas_path):
            r = json.loads(line)
            self.weights[canonical([tuple(v) for v in r["normals"]])] = Fraction(r["weight"])
        self.from_atlas = len(self.weights)
        if os.path.exists(cache_path):
            for line in open(cache_path):
                r = json.loads(line)
                self.weights[canonical([tuple(v) for v in r["normals"]])] = Fraction(r["weight"])

    def __len__(self):
        return len(self.weights)

    def weight(self, normals: Sequence[Tuple[int, ...]]) -> Fraction:
        key = canonical(normals)
        if key not in self.weights:
            from transverse import transverse_weight
            w = transverse_weight([list(v) for v in normals])
            self.weights[key] = w
            self.computed += 1
            with open(self.cache_path, "a") as fh:
                fh.write(json.dumps({"normals": [list(v) for v in key], "weight": str(w)}) + "\n")
        return self.weights[key]


def edges_with_linear_length(Z: ChamberCone):
    """Edges as (facet normals, length as a row in b, the two vertices, the facet indices)."""
    C: Chamber = Z.C
    support = C.cone.SupportHyperplanes()
    normals = [prim([-a for a in h[: C.D]]) for h in support]

    def tight_facets(p):
        return [i for i, h in enumerate(support)
                if sum(Fraction(h[j]) * p[j] for j in range(C.D)) + h[C.D] == 0]

    facets = [tight_facets(p) for p in C.vertices]
    out = []
    n = len(C.vertices)
    for i in range(n):
        for j in range(i + 1, n):
            common = sorted(set(facets[i]) & set(facets[j]))
            if len(common) < C.dim - 1:
                continue
            if rank_of([support[k][: C.D] for k in common]) != C.dim - 1:
                continue
            p, q = C.vertices[i], C.vertices[j]
            d = [b - a for a, b in zip(p, q)]
            den = 1
            for x in d:
                den = den * x.denominator // gcd(den, x.denominator)
            di = [int(x * den) for x in d]
            g = 0
            for x in di:
                g = gcd(g, abs(x))
            u = [x // g for x in di]
            k = next(t for t in range(C.D) if u[t])
            Xi, Xj = Z.maps[i], Z.maps[j]
            row = [(Xj[k][t] - Xi[k][t]) / Fraction(u[k]) for t in range(C.B)]
            out.append((tuple(sorted(normals[k2] for k2 in common)), row, (i, j),
                        tuple(common)))
    return out


def cell_functional(Z: ChamberCone, book: WeightBook) -> List[Fraction]:
    """The functional as a row vector in the boundary triple."""
    total = [Fraction(0)] * Z.B
    for normals, row, _, _ in edges_with_linear_length(Z):
        w = book.weight(normals)
        if w:
            total = [t + w * r for t, r in zip(total, row)]
    return total


def apply_functional(ell: Sequence[Fraction], b: Sequence[int]) -> Fraction:
    return sum(e * Fraction(x) for e, x in zip(ell, b))
