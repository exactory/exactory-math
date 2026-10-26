#!/usr/bin/env python3
"""Chambers of the rank-five hive family: the deformation cone of one hive polytope,
its extreme rays, and the linear functional the linear Ehrhart coefficient becomes on it."""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from math import gcd
from typing import List, Sequence, Tuple

TOOLS = "<workspace>/stretched-lr-negative-coefficient/tools"
sys.path.insert(0, TOOLS)
from hivepoly import hive_inequalities, hive_setup, normalize  # noqa: E402


def hive_rows_symbolic(n: int):
    """Rows (a, c): a . x + c . (lam,mu,nu) >= 0, x the interior entries, in the same order
    and normalisation as hivepoly.hive_inequalities."""
    interior = [(x, y) for x in range(1, n) for y in range(1, n) if x + y <= n - 1]
    index = {v: i for i, v in enumerate(interior)}
    D = len(interior)
    B = 3 * n

    def bnd(v):
        """The boundary value at v as a 0/1 vector in (lam, mu, nu)."""
        x, y = v
        c = [0] * B
        if x == 0:
            for i in range(y):
                c[n + i] += 1
            return c
        if y == 0:
            for i in range(x):
                c[i] += 1
            return c
        if x + y == n:
            for i in range(n):
                c[n + i] += 1
            for i in range(x):
                c[2 * n + i] += 1
            return c
        raise KeyError(v)

    rows = []

    def add(plus, minus):
        a = [0] * D
        c = [0] * B
        for v in plus:
            if v in index:
                a[index[v]] += 1
            else:
                for j, t in enumerate(bnd(v)):
                    c[j] += t
        for v in minus:
            if v in index:
                a[index[v]] -= 1
            else:
                for j, t in enumerate(bnd(v)):
                    c[j] -= t
        if any(a):
            rows.append((a, c))

    for x in range(n + 1):
        for y in range(n + 1):
            if x + y <= n - 2:
                add([(x + 1, y), (x, y + 1)], [(x, y), (x + 1, y + 1)])
            if y >= 1 and x + y <= n - 1:
                add([(x, y), (x + 1, y)], [(x, y + 1), (x + 1, y - 1)])
            if x >= 1 and x + y <= n - 1:
                add([(x, y), (x, y + 1)], [(x + 1, y), (x - 1, y + 1)])
    return D, rows


def pack(lam, mu, nu, n: int) -> List[int]:
    out = list(lam) + [0] * (n - len(lam)) + list(mu) + [0] * (n - len(mu)) + list(nu) + [0] * (n - len(nu))
    return out


def check_symbolic(lam, mu, nu):
    """The symbolic rows evaluated at (lam,mu,nu) must be hive_inequalities' rows."""
    n, _, _, _ = hive_setup(lam, mu, nu)
    D, rows = hive_rows_symbolic(n)
    b = pack(normalize(lam), normalize(mu), normalize(nu), n)
    got = [list(a) + [sum(ci * bi for ci, bi in zip(c, b))] for a, c in rows]
    D2, want = hive_inequalities(lam, mu, nu)
    return D == D2 and got == want


def dominance_rows(n: int):
    """lam_i - lam_{i+1} >= 0, lam_n >= 0, and the same for mu and nu, as vectors in (lam,mu,nu)."""
    B = 3 * n
    out = []
    for blk in range(3):
        for i in range(n):
            c = [0] * B
            c[blk * n + i] = 1
            if i + 1 < n:
                c[blk * n + i + 1] = -1
            out.append(c)
    return out


def size_equation(n: int):
    """|lam| - |mu| - |nu| = 0."""
    return [1] * n + [-1] * n + [-1] * n


def _rref(M: List[List[Fraction]]):
    M = [row[:] for row in M]
    piv = []
    r = 0
    ncols = len(M[0])
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M[:r], piv


def solve_vertex_map(basis_rows, D: int, B: int):
    """Given D rows (a, c) with a of rank D, return the D x B matrix X with x(b) = X b."""
    A = [[Fraction(v) for v in a] for a, _ in basis_rows]
    C = [[Fraction(-v) for v in c] for _, c in basis_rows]      # A x = -C b
    aug = [A[i] + C[i] for i in range(D)]
    red, piv = _rref(aug)
    if piv != list(range(D)):
        return None
    return [row[D:] for row in red]


def primitive(v: Sequence[Fraction]) -> Tuple[int, ...]:
    den = 1
    for x in v:
        den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]
    g = 0
    for x in iv:
        g = gcd(g, abs(x))
    return tuple(x // g for x in iv) if g else tuple(iv)


class Chamber:
    """The deformation cone of the hive polytope at one triple, and the linear coefficient on it."""

    def __init__(self, lam, mu, nu):
        from PyNormaliz import Cone  # type: ignore

        self.lam, self.mu, self.nu = normalize(lam), normalize(mu), normalize(nu)
        self.n, _, _, _ = hive_setup(lam, mu, nu)
        self.D, self.rows = hive_rows_symbolic(self.n)
        self.B = 3 * self.n
        self.b0 = pack(self.lam, self.mu, self.nu, self.n)
        num = [list(a) + [sum(ci * bi for ci, bi in zip(c, self.b0))] for a, c in self.rows]
        self.cone = Cone(inhom_inequalities=num)
        self.dim = self.cone.AffineDim()
        self.vertices = [tuple(Fraction(x, v[-1]) for x in v[:self.D])
                         for v in self.cone.VerticesOfPolyhedron()]

    def tight(self, p):
        return [i for i, (a, c) in enumerate(self.rows)
                if sum(Fraction(a[j]) * p[j] for j in range(self.D))
                + sum(c[j] * self.b0[j] for j in range(self.B)) == 0]

    def vertex_maps(self):
        """One D x B matrix per vertex; None when the vertex is not simple."""
        out = []
        for p in self.vertices:
            t = self.tight(p)
            sub = [self.rows[i] for i in t]
            X = None
            # a simple vertex has exactly D independent tight rows; take the first independent D
            picked = []
            A: List[List[Fraction]] = []
            for i, (a, c) in enumerate(sub):
                cand = A + [[Fraction(v) for v in a]]
                if len(_rref(cand)[1]) == len(cand):
                    A = cand
                    picked.append(sub[i])
                if len(picked) == self.D:
                    break
            if len(picked) == self.D:
                X = solve_vertex_map(picked, self.D, self.B)
            out.append((t, X))
        return out

    def is_simple(self):
        return all(len(t) == self.D for t, _ in self.vertex_maps())


def left_null(A):
    """Basis of {y : y A = 0} for a list of rows A."""
    m = len(A)
    n = len(A[0])
    aug = [[Fraction(x) for x in A[i]] + [Fraction(1 if j == i else 0) for j in range(m)]
           for i in range(m)]
    red, _ = _rref(aug)
    return [row[n:] for row in red if all(row[j] == 0 for j in range(n))]


def _is_multiple(v, se):
    nz = [i for i, x in enumerate(v) if x != 0]
    if not nz:
        return True
    if se[nz[0]] == 0:
        return False
    t = Fraction(v[nz[0]], se[nz[0]])
    return all(Fraction(v[i]) == t * se[i] for i in range(len(v)))


def wall_vertices(C: "Chamber"):
    """Vertices whose tight rows impose a condition on b beyond the ones that hold identically."""
    se = size_equation(C.n)
    out = []
    for k, p in enumerate(C.vertices):
        t = C.tight(p)
        A = [list(C.rows[i][0]) for i in t]
        Cm = [list(C.rows[i][1]) for i in t]
        for y in left_null(A):
            yc = [sum(y[j] * Cm[j][i] for j in range(len(t))) for i in range(len(se))]
            if not _is_multiple(yc, se):
                out.append(k)
                break
    return out


def lattice_basis_of_size_hyperplane(n: int):
    """A basis of the integer vectors (lam,mu,nu) with |lam| = |mu| + |nu|, as 3n-vectors."""
    B = 3 * n
    out = []
    for i in range(1, n):                       # lam_0 - lam_i
        v = [0] * B
        v[0] = 1
        v[i] = -1
        out.append(v)
    for blk in (1, 2):                          # mu_j and nu_j, each paid for by lam_0
        for j in range(n):
            v = [0] * B
            v[blk * n + j] = 1
            v[0] = 1
            out.append(v)
    return out                                   # (n-1) + 2n = 3n - 1 vectors


class ChamberCone:
    """The deformation cone of the hive polytope at a wall-free triple, with the linear
    functional the linear Ehrhart coefficient becomes on it."""

    def __init__(self, lam, mu, nu):
        self.C = Chamber(lam, mu, nu)
        self.n, self.D, self.B = self.C.n, self.C.D, self.C.B
        self.se = size_equation(self.n)
        self.walls = wall_vertices(self.C)
        self.maps = []
        for p in self.C.vertices:
            t = self.C.tight(p)
            picked, A = [], []
            for i in t:
                cand = A + [[Fraction(v) for v in self.C.rows[i][0]]]
                if len(_rref(cand)[1]) == len(cand):
                    A = cand
                    picked.append(self.C.rows[i])
                if len(picked) == self.D:
                    break
            self.maps.append(solve_vertex_map(picked, self.D, self.B))

    def residual_rows(self):
        """The deformation-cone inequalities: every vertex satisfies every hive row."""
        rows = set()
        for X in self.maps:
            for a, c in self.C.rows:
                v = [sum(Fraction(a[k]) * X[k][j] for k in range(self.D)) + c[j]
                     for j in range(self.B)]
                if all(x == 0 for x in v):
                    continue
                rows.add(primitive(v))
        return sorted(rows)

    def inequalities(self):
        return self.residual_rows() + [tuple(r) for r in dominance_rows(self.n)]

    def extreme_rays(self):
        from PyNormaliz import Cone  # type: ignore

        K = Cone(inequalities=[list(r) for r in self.inequalities()],
                 equations=[self.se])
        K.Compute("ExtremeRays", "DualMode")
        return [tuple(int(x) for x in r) for r in K.ExtremeRays()]

    def contains(self, b) -> bool:
        if sum(self.se[i] * b[i] for i in range(self.B)) != 0:
            return False
        return all(sum(r[i] * b[i] for i in range(self.B)) >= 0 for r in self.inequalities())


def a1_of(b, n: int) -> Fraction:
    """The linear Ehrhart coefficient of the hive polytope of the triple packed in b."""
    from PyNormaliz import Cone  # type: ignore

    lam = tuple(x for x in b[:n] if x)
    mu = tuple(x for x in b[n:2 * n] if x)
    nu = tuple(x for x in b[2 * n:] if x)
    D, rows = hive_inequalities(lam, mu, nu)
    q = Cone(inhom_inequalities=rows).EhrhartQuasiPolynomial()
    if len(q) - 1 != 1:
        raise ValueError("period is not one")
    c = [Fraction(x, q[-1]) for x in q[0]]
    return c[1] if len(c) > 1 else Fraction(0)


def unpack(b, n: int):
    return (tuple(x for x in b[:n] if x), tuple(x for x in b[n:2 * n] if x),
            tuple(x for x in b[2 * n:] if x))


def solve_coeffs(rays, b):
    """The coordinates of b in the ray basis, when the rays are a basis of their span."""
    m = len(rays)
    cols = [[Fraction(r[i]) for r in rays] + [Fraction(b[i])] for i in range(len(b))]
    red, piv = _rref(cols)
    if piv[:m] != list(range(m)) or len(piv) > m:
        return None
    out = [Fraction(0)] * m
    for i, p in enumerate(piv):
        out[p] = red[i][m]
    return out


def hive_cone_rays(n: int):
    """Extreme rays of the full hive cone of side n, in the coordinates h(x,y), h(0,0) = 0."""
    from PyNormaliz import Cone  # type: ignore

    pts = [(x, y) for x in range(n + 1) for y in range(n + 1) if x + y <= n]
    idx = {p: i for i, p in enumerate(pts)}
    rows = []

    def add(plus, minus):
        v = [0] * len(pts)
        for p in plus:
            v[idx[p]] += 1
        for p in minus:
            v[idx[p]] -= 1
        if any(v):
            rows.append(v)

    for x in range(n + 1):
        for y in range(n + 1):
            if x + y <= n - 2:
                add([(x + 1, y), (x, y + 1)], [(x, y), (x + 1, y + 1)])
            if y >= 1 and x + y <= n - 1:
                add([(x, y), (x + 1, y)], [(x, y + 1), (x + 1, y - 1)])
            if x >= 1 and x + y <= n - 1:
                add([(x, y), (x, y + 1)], [(x + 1, y), (x - 1, y + 1)])
    for last, prev in (((n, 0), (n - 1, 0)), ((0, n), (0, n - 1)), ((n, 0), (n - 1, 1))):
        add([last], [prev])                      # the last part of each boundary partition >= 0
    eq = [0] * len(pts)
    eq[idx[(0, 0)]] = 1
    K = Cone(inequalities=rows, equations=[eq])
    return pts, idx, [list(int(x) for x in r) for r in K.ExtremeRays()]


def triple_of_hive(h, idx, n: int):
    """The boundary triple (lam, mu, nu) of a hive given as a vector of vertex values."""
    lam = tuple(h[idx[(i, 0)]] - h[idx[(i - 1, 0)]] for i in range(1, n + 1))
    mu = tuple(h[idx[(0, i)]] - h[idx[(0, i - 1)]] for i in range(1, n + 1))
    nu = tuple(h[idx[(i, n - i)]] - h[idx[(i - 1, n - i + 1)]] for i in range(1, n + 1))
    return (tuple(x for x in lam if x), tuple(x for x in mu if x), tuple(x for x in nu if x))


class Cell(ChamberCone):
    """The cell of the chamber complex whose relative interior holds the given triple.

    Every incidence of the hive polytope at that triple is imposed: a hive row tight at a vertex
    stays tight (an equation), a hive row slack at a vertex stays satisfied (an inequality). On
    the relative interior of the cell the polytope keeps its face lattice and every vertex is the
    same linear function of the boundary triple, so the Ehrhart coefficient a_k is a homogeneous
    polynomial of degree k there, and a1 is a linear functional.
    """

    def split_rows(self):
        eqs, ineqs = set(), set()
        for k, X in enumerate(self.maps):
            tight = set(self.C.tight(self.C.vertices[k]))
            for i, (a, c) in enumerate(self.C.rows):
                v = [sum(Fraction(a[j]) * X[j][t] for j in range(self.D)) + c[t]
                     for t in range(self.B)]
                if all(x == 0 for x in v):
                    continue
                (eqs if i in tight else ineqs).add(primitive(v))
        return sorted(eqs), sorted(ineqs - eqs)

    def cone(self):
        from PyNormaliz import Cone  # type: ignore

        eqs, ineqs = self.split_rows()
        K = Cone(inequalities=[list(r) for r in ineqs] + [list(r) for r in dominance_rows(self.n)],
                 equations=[list(r) for r in eqs] + [self.se])
        K.Compute("ExtremeRays", "DualMode")
        return K, eqs, ineqs

    def contains_cell(self, b, eqs, ineqs) -> bool:
        if sum(self.se[i] * b[i] for i in range(self.B)) != 0:
            return False
        if any(sum(r[i] * b[i] for i in range(self.B)) != 0 for r in eqs):
            return False
        if any(sum(r[i] * b[i] for i in range(self.B)) < 0 for r in ineqs):
            return False
        return all(sum(r[i] * b[i] for i in range(self.B)) >= 0 for r in dominance_rows(self.n))
