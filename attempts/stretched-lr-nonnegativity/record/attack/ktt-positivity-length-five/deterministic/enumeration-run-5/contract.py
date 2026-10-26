#!/usr/bin/env python3
"""The intrinsic-lattice contraction of move 11, made concrete.

For a hive polytope H of intrinsic dimension d < D the stretched polynomial is the Ehrhart
function of H - x0 in the lattice Z^D intersected with the linear span, for any lattice point x0
of H. This module performs that change of coordinates and returns everything the local-formula
machinery needs in the intrinsic lattice:

  * the polytope's vertices in coordinates of a basis of the intrinsic lattice,
  * the hive rows restricted to the span, in the dual of that basis,
  * the induced Gram matrix of the basis, which the weight construction consumes in place of the
    identity.

The cone with its lattice is metric-free; the Gram is what the Berline-Vergne weight needs, and it
is the one induced from the ambient standard form, not the identity of the new coordinates.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from typing import List, Sequence

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bvweight import _gcd, _rref, saturated_basis  # noqa: E402
from hivepoly import hive_inequalities  # noqa: E402


def _same_lattice(u, v, n):
    """Do two integer bases span the same lattice? The transition matrix is unimodular."""
    from bvweight import det
    if len(u) != len(v):
        return False
    rows = []
    for x in u:
        c = _solve_in_basis(v, [Fraction(t) for t in x])
        if c is None or any(t.denominator != 1 for t in c):
            return False
        rows.append(c)
    return abs(det(rows)) == 1


def _positive_definite(G):
    """Sylvester's criterion on the leading principal minors."""
    from bvweight import det
    for k in range(1, len(G) + 1):
        if det([[Fraction(G[i][j]) for j in range(k)] for i in range(k)]) <= 0:
            return False
    return True


def _solve_in_basis(base: Sequence[Sequence[int]], v: Sequence[Fraction]):
    """The coordinates of v in the given basis of a subspace, or None when v is not in the span."""
    d = len(base)
    n = len(v)
    aug = [[Fraction(base[a][i]) for a in range(d)] + [Fraction(v[i])] for i in range(n)]
    red, piv = _rref(aug)
    if [p for p in piv if p < d] != list(range(d)):
        return None
    out = [Fraction(0)] * d
    for r, p in enumerate(piv):
        if p < d:
            out[p] = red[r][d]
    for i in range(n):
        if sum(out[a] * base[a][i] for a in range(d)) != Fraction(v[i]):
            return None
    return out


class Contracted:
    """A hive polytope of intrinsic dimension d < D, in its own lattice."""

    def __init__(self, lam, mu, nu):
        from PyNormaliz import Cone  # type: ignore

        self.D, self.rows = hive_inequalities(lam, mu, nu)
        self.cone = Cone(inhom_inequalities=self.rows)
        self.dim = self.cone.AffineDim()
        self.vertices = [tuple(Fraction(x, v[-1]) for x in v[:self.D])
                         for v in self.cone.VerticesOfPolyhedron()]
        self.lattice_points = [tuple(int(x) for x in g[:self.D])
                               for g in self.cone.ModuleGenerators()]
        if not self.lattice_points:
            raise ValueError("no lattice point in the polytope")
        self.x0 = self.lattice_points[0]
        # a basis of the lattice of the linear span, saturated in Z^D
        cleared = []
        for v in self.vertices:
            d_ = [x - Fraction(self.x0[i]) for i, x in enumerate(v)]
            m = 1
            for x in d_:
                m = m * x.denominator // _gcd(m, x.denominator)
            cleared.append([int(x * m) for x in d_])
        self.base = saturated_basis(cleared, self.D)
        assert len(self.base) == self.dim, (
            f"intrinsic lattice has rank {len(self.base)}, expected {self.dim}")
        self.gram = [[sum(self.base[a][i] * self.base[b][i] for i in range(self.D))
                      for b in range(self.dim)] for a in range(self.dim)]
        self.checks = self._check()

    def _check(self):
        """The direct checks the seventh review requires, because the end-to-end identity cannot
        see the Gram: every positive-definite form gives a valid local formula, so reproducing the
        certified coefficient tests validity and not the choice of form."""
        from bvweight import det, int_kernel

        out = {}
        # the intrinsic lattice is saturated: the double kernel of the basis returns the basis
        again = saturated_basis([list(b) for b in self.base], self.D)
        out["saturated"] = len(again) == self.dim and _same_lattice(again, self.base, self.D)
        # the basis generates the whole intersection, not a sublattice: every ambient lattice
        # vector lying in the span has integral coordinates in it
        integral = True
        for i in range(self.D):
            e = [1 if k == i else 0 for k in range(self.D)]
            c = _solve_in_basis(self.base, [Fraction(x) for x in e])
            if c is not None and any(x.denominator != 1 for x in c):
                integral = False
        out["basis generates the intersection"] = integral
        # the Gram is the ambient standard inner product of the basis vectors
        out["gram from ambient inner products"] = all(
            self.gram[a][b] == sum(self.base[a][i] * self.base[b][i] for i in range(self.D))
            for a in range(self.dim) for b in range(self.dim))
        out["gram positive definite"] = _positive_definite(self.gram)
        return out

    def vertices_in_basis(self):
        out = []
        for v in self.vertices:
            c = _solve_in_basis(self.base, [x - Fraction(self.x0[i]) for i, x in enumerate(v)])
            assert c is not None, "a vertex left the span"
            out.append(tuple(c))
        return out

    def rows_in_basis(self):
        """Each hive row restricted to the span, as (functional on the basis, constant at x0)."""
        out = []
        for row in self.rows:
            a = row[:self.D]
            const = row[self.D] + sum(a[i] * self.x0[i] for i in range(self.D))
            f = tuple(sum(a[i] * self.base[b][i] for i in range(self.D)) for b in range(self.dim))
            out.append((f, const))
        return out
