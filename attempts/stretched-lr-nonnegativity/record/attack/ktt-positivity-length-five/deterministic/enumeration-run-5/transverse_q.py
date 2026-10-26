#!/usr/bin/env python3
"""The transverse cone of a face, in the orthogonal complement of a chosen form.

`tools/transverse.py` places the transverse cone in the standard orthogonal complement of the
span of the face and equips it with the standard Gram. The cone with its lattice is metric-free,
but that identification is not: under a form Q the complement and the Gram are both Q-dependent.
Three things change and nothing else:

  * the projection is Q-orthogonal, so `_Proj` is given Q instead of the identity;
  * the Gram of the projected basis is taken under Q;
  * the linear span of the face, which the projection kills, is unchanged, because it is the
    common kernel of the normals and so is metric-free.

The inequalities that cut the cone are unchanged too: a normal is a linear functional and its
value on a basis vector is a dual pairing, not an inner product.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from typing import Sequence

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bvweight import _Proj, _gcd, int_kernel, lattice_basis, rank, weight  # noqa: E402


def transverse_cone_q(normals: Sequence[Sequence[int]], Q, d: int = 6):
    """(rays of the transverse cone in lattice coordinates, its Gram matrix under Q)."""
    from PyNormaliz import Cone  # type: ignore

    span = [list(map(int, n)) for n in normals]
    r = rank(span)
    comp = int_kernel(span, d)                      # the span of the face, metric-free
    pr = _Proj(comp, Q)                             # Q-orthogonal projection onto its complement
    gens = [pr([1 if c == i else 0 for c in range(d)]) for i in range(d)]
    den = 1
    for g in gens:
        for x in g:
            den = den * x.denominator // _gcd(den, x.denominator)
    base = [[Fraction(x, den) for x in b]
            for b in lattice_basis([[int(x * den) for x in g] for g in gens])]
    assert len(base) == r, f"projected lattice has rank {len(base)}, expected {r}"
    ineq = []
    for n in span:
        row = [-sum(Fraction(n[i]) * base[a][i] for i in range(d)) for a in range(r)]
        m = 1
        for x in row:
            m = m * x.denominator // _gcd(m, x.denominator)
        ineq.append([int(x * m) for x in row])
    C = Cone(inequalities=ineq)
    rays = [tuple(int(x) for x in v) for v in C.ExtremeRays()]
    gram = [[sum(base[a][i] * Q[i][j] * base[b][j] for i in range(d) for j in range(d))
             for b in range(r)] for a in range(r)]
    return rays, gram


def transverse_weight_q(normals: Sequence[Sequence[int]], Q, d: int = 6) -> Fraction:
    rays, gram = transverse_cone_q(normals, Q, d)
    r = len(gram)
    if len(rays) == r:
        return weight(rays, gram)
    from transverse import _triangulated_weight
    return _triangulated_weight(rays, gram)
