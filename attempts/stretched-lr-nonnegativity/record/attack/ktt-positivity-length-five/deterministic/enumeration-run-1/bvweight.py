#!/usr/bin/env python3
"""The Berline-Vergne local weight of a simplicial rational cone, by the defining recursion.

Berline and Vergne, "Local Euler-Maclaurin formula for polytopes", arXiv:math/0507256,
Proposition 4.1: for a rational space W with a rational scalar product there is a unique family
of maps mu, indexed by the rational quotients of W, with mu({0}) = 1 and

    S(a) = sum over the faces f of a of mu( t(a,f) ) I(f),                                   (*)

S(a) the exponential sum over the lattice points of a, I(f) the exponential integral over f with
the measure normalized by the lattice of lin(f), and t(a,f) the transverse cone, the image of a
in W/lin(f) identified with the orthogonal complement of lin(f) and carrying the projected
lattice. The term of the vertex has transverse cone a itself and integral 1, so (*) is a
recursion on the dimension:

    mu(a) = S(a) - sum over the faces f of positive dimension of mu( t(a,f) ) I(f).

The Ehrhart weight of a face F of a polytope P is alpha(F, P) = mu(t(P,F))(0). Everything is
evaluated along a generic line xi = t xi_0, so every term is a Laurent series in one variable
with rational coefficients whose poles cancel in the sum, and the weight is the constant term.

This module implements the recursion for simplicial cones, where every ingredient is explicit.
For a simplicial cone with primitive generators v_1, ..., v_d in a lattice L with Gram matrix G:

    S = ( sum over the lattice points x of the half-open parallelepiped of e^{<xi,x>} )
        * product over i of 1/(1 - e^{<xi,v_i>}),
    I(f_J) = (-1)^{|J|} * m_J * product over j in J of 1/<xi, v_j>,

with m_J the index of the sublattice the v_j, j in J, span inside L intersected with their span;
the faces are indexed by the subsets J, and the transverse cone along f_J is the simplicial cone
spanned by the images of the v_i, i not in J, in the quotient lattice.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from typing import Dict, List, Sequence, Tuple

Vec = Tuple[int, ...]
PREC = 10          # terms of each series kept above the leading power


# --------------------------------------------------------------------------- Laurent series


class L:
    """sum_{n = off}^{off + len(c) - 1} c[n - off] t^n."""

    __slots__ = ("off", "c")

    def __init__(self, off: int, c: Sequence[Fraction]):
        self.off, self.c = off, list(c)

    def top(self) -> int:
        return self.off + len(self.c)

    def at(self, n: int) -> Fraction:
        i = n - self.off
        return self.c[i] if 0 <= i < len(self.c) else Fraction(0)

    def __add__(self, o: "L") -> "L":
        lo, hi = min(self.off, o.off), min(self.top(), o.top())
        return L(lo, [self.at(n) + o.at(n) for n in range(lo, hi)])

    def __sub__(self, o: "L") -> "L":
        lo, hi = min(self.off, o.off), min(self.top(), o.top())
        return L(lo, [self.at(n) - o.at(n) for n in range(lo, hi)])

    def __mul__(self, o: "L") -> "L":
        n = min(len(self.c), len(o.c))
        out = [Fraction(0)] * n
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if i + j < n:
                        out[i + j] += a * b
        return L(self.off + o.off, out)

    def times(self, r) -> "L":
        r = Fraction(r)
        return L(self.off, [r * x for x in self.c])


def const(x) -> L:
    return L(0, [Fraction(x)] + [Fraction(0)] * PREC)


def _exp_coeffs(c: Fraction, n: int) -> List[Fraction]:
    out, term = [], Fraction(1)
    for k in range(n):
        out.append(term)
        term = term * c / (k + 1)
    return out


def exp_series(c: Fraction) -> L:
    """e^{c t}."""
    return L(0, _exp_coeffs(c, PREC + 1))


def inv_one_minus_exp(c: Fraction) -> L:
    """1 / (1 - e^{c t}), c nonzero: leading term -1/(c t)."""
    if c == 0:
        raise ZeroDivisionError("the linear form vanishes on a ray; choose another direction")
    e = _exp_coeffs(c, PREC + 3)
    a = [e[k + 1] / c for k in range(1, PREC + 2)]       # 1 - e^{ct} = -c t (1 + sum a_k t^k)
    inv = [Fraction(1)] + [Fraction(0)] * (PREC + 1)
    for n in range(1, PREC + 2):
        inv[n] = -sum(a[k - 1] * inv[n - k] for k in range(1, n + 1))
    return L(-1, [-x / c for x in inv])


def inv_linear(c: Fraction) -> L:
    """1 / (c t)."""
    if c == 0:
        raise ZeroDivisionError("the linear form vanishes on a ray; choose another direction")
    return L(-1, [Fraction(1) / c] + [Fraction(0)] * PREC)


# ------------------------------------------------------------- exact rational linear algebra


def _rref(m: List[List[Fraction]]) -> Tuple[List[List[Fraction]], List[int]]:
    m = [r[:] for r in m]
    piv, r = [], 0
    for c in range(len(m[0]) if m else 0):
        p = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        piv.append(c)
        r += 1
        if r == len(m):
            break
    return m[:r], piv


def rank(rows: Sequence[Sequence]) -> int:
    return len(_rref([[Fraction(x) for x in r] for r in rows])[0]) if rows else 0


def solve(A: List[List[Fraction]], b: List[Fraction]) -> List[Fraction]:
    """The unique solution of A x = b for a square invertible A."""
    n = len(A)
    m = [A[i][:] + [b[i]] for i in range(n)]
    red, piv = _rref(m)
    assert piv == list(range(n)), "singular system"
    return [red[i][n] for i in range(n)]


def det(A: List[List[Fraction]]) -> Fraction:
    n = len(A)
    if n == 0:
        return Fraction(1)
    m = [r[:] for r in A]
    d = Fraction(1)
    for c in range(n):
        p = next((i for i in range(c, n) if m[i][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            m[c], m[p] = m[p], m[c]
            d = -d
        d *= m[c][c]
        inv = Fraction(1) / m[c][c]
        m[c] = [x * inv for x in m[c]]
        for i in range(c + 1, n):
            if m[i][c]:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[c])]
    return d


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lattice_basis(rows: Sequence[Sequence[int]]) -> List[List[int]]:
    """A basis of the lattice generated by integer row vectors, by Hermite reduction."""
    m = [list(map(int, r)) for r in rows if any(r)]
    k = len(rows[0]) if rows else 0
    out: List[List[int]] = []
    col = 0
    while m and col < k:
        nz = [r for r in m if r[col] != 0]
        rest = [r for r in m if r[col] == 0]
        if not nz:
            col += 1
            m = rest
            continue
        while len(nz) > 1:
            nz.sort(key=lambda r: abs(r[col]))
            p0 = nz[0]
            nxt = []
            for r in nz[1:]:
                q = r[col] // p0[col]
                r = [a - q * b for a, b in zip(r, p0)]
                if r[col] != 0:
                    nxt.append(r)
                elif any(r):
                    rest.append(r)
            nz = [p0] + nxt
        out.append(nz[0])
        m = rest
        col += 1
    return out


class _Proj:
    """Orthogonal projection onto the complement of a span, with respect to a Gram matrix."""

    def __init__(self, span: Sequence[Sequence[int]], G: List[List[Fraction]]):
        self.G, self.k = G, len(G)
        self.S = [list(map(Fraction, v)) for v in span]
        if self.S:
            self.GS = [[self._ip(u, w) for w in self.S] for u in self.S]

    def _ip(self, a, b) -> Fraction:
        return sum(a[i] * self.G[i][j] * b[j] for i in range(self.k) for j in range(self.k))

    def __call__(self, x: Sequence) -> List[Fraction]:
        x = [Fraction(v) for v in x]
        if not self.S:
            return x
        coef = solve([r[:] for r in self.GS], [self._ip(x, w) for w in self.S])
        return [x[c] - sum(coef[i] * self.S[i][c] for i in range(len(self.S))) for c in range(self.k)]


def int_kernel(rows: Sequence[Sequence[int]], k: int) -> List[List[int]]:
    """A basis of the saturated lattice {x in Z^k : r . x = 0 for every row r}.

    Augment the identity with the transpose of the row matrix and clear the right block by
    integer row operations, freezing each pivot row as its column is cleared; the left blocks of
    the rows whose right block vanishes form a basis, saturated because only unimodular row
    operations were used.
    """
    m = len(rows)
    if m == 0:
        return [[1 if c == i else 0 for c in range(k)] for i in range(k)]
    aug = [[1 if c == i else 0 for c in range(k)] + [int(rows[j][i]) for j in range(m)]
           for i in range(k)]
    active = aug
    for col in range(k, k + m):
        nz = [r for r in active if r[col] != 0]
        if not nz:
            continue
        while len(nz) > 1:
            nz.sort(key=lambda r: abs(r[col]))
            p0 = nz[0]
            for r in nz[1:]:
                q = r[col] // p0[col]
                for j in range(k + m):
                    r[j] -= q * p0[j]
            nz = [r for r in nz if r[col] != 0]
        active = [r for r in active if r is not nz[0]]
    return [r[:k] for r in active if not any(r[k:])]


def saturated_basis(vs: Sequence[Sequence[int]], k: int) -> List[List[int]]:
    """A basis of Z^k intersected with the span of vs."""
    ann = int_kernel(vs, k)
    return int_kernel(ann, k) if ann else [[1 if c == i else 0 for c in range(k)] for i in range(k)]


# ----------------------------------------------------------------------------- the recursion


class SimplicialCone:
    """cone(v_1, ..., v_d) in Z^k with Gram matrix G; the v_i are linearly independent."""

    def __init__(self, rays: Sequence[Sequence[int]], gram: Sequence[Sequence[Fraction]]):
        self.rays = [tuple(int(x) for x in r) for r in rays]
        self.k = len(gram)
        self.G = [[Fraction(x) for x in row] for row in gram]
        assert rank(self.rays) == len(self.rays), "the generators must be independent"

    def ip(self, a: Sequence, b: Sequence) -> Fraction:
        return sum(Fraction(a[i]) * self.G[i][j] * Fraction(b[j])
                   for i in range(self.k) for j in range(self.k))

    def index_of(self, idx: Sequence[int]) -> int:
        """Index of the sublattice the chosen rays span inside Z^k intersected with their span."""
        vs = [list(self.rays[i]) for i in idx]
        if not vs:
            return 1
        sat = saturated_basis(vs, self.k)
        B = [[Fraction(sat[i][c]) for i in range(len(sat))] for c in range(self.k)]
        M = [list(_coords(B, [Fraction(x) for x in v], len(sat))) for v in vs]
        d = abs(det([[Fraction(M[i][j]) for j in range(len(sat))] for i in range(len(vs))]))
        assert d.denominator == 1, 'the index must be an integer'
        return int(d)

    def box_points(self) -> List[Tuple[int, ...]]:
        """Lattice points of the half-open parallelepiped sum_i t_i v_i, 0 <= t_i < 1."""
        d = len(self.rays)
        m = self.index_of(tuple(range(d)))
        if m == 1:
            return [tuple([0] * self.k)]
        # coordinates in the ray basis of a point of Z^k: solve V a = x over the span
        pts = []
        # enumerate candidate coefficient vectors with denominators dividing m
        for num in product(range(m), repeat=d):
            x = [Fraction(0)] * self.k
            for i, v in enumerate(self.rays):
                f = Fraction(num[i], m)
                for c in range(self.k):
                    x[c] += f * v[c]
            if all(y.denominator == 1 for y in x):
                pts.append(tuple(int(y) for y in x))
        assert len(pts) == m, f"expected {m} box points, found {len(pts)}"
        return pts

    def projected_basis(self, idx: Sequence[int]):
        """A basis of the projected lattice in the orthogonal complement of the chosen face."""
        pr = _Proj([self.rays[j] for j in idx], self.G)
        gens = [pr([1 if c == i else 0 for c in range(self.k)]) for i in range(self.k)]
        den = 1
        for g in gens:
            for x in g:
                den = den * x.denominator // _gcd(den, x.denominator)
        ints = [[int(x * den) for x in g] for g in gens]
        base = lattice_basis(ints)
        return pr, [[Fraction(x, den) for x in b] for b in base]

    def quotient(self, idx: Sequence[int]) -> "SimplicialCone":
        """The transverse cone along the face spanned by the chosen rays."""
        pr, base = self.projected_basis(idx)
        r = len(base)
        B = [[base[i][c] for i in range(r)] for c in range(self.k)]      # columns are basis vectors
        rays_q = []
        for i in range(len(self.rays)):
            if i in idx:
                continue
            rays_q.append(_coords(B, pr(self.rays[i]), r))
        Gq = [[sum(base[a][i] * self.G[i][j] * base[b][j]
                   for i in range(self.k) for j in range(self.k))
               for b in range(r)] for a in range(r)]
        return SimplicialCone(rays_q, Gq)


def _coords(B: List[List[Fraction]], x: List[Fraction], r: int) -> Tuple[int, ...]:
    """Integer coordinates of x in the basis whose columns are the columns of B."""
    red, piv = _rref([B[c][:] + [x[c]] for c in range(len(B))])
    sol = [Fraction(0)] * r
    for i, p in enumerate(piv):
        if p < r:
            sol[p] = red[i][r]
    assert all(y.denominator == 1 for y in sol), "the quotient coordinates must be integral"
    return tuple(int(y) for y in sol)


def mu(cone: SimplicialCone, xi: Sequence[Fraction]) -> L:
    """mu(cone) along the line t -> t xi, as a Laurent series."""
    d = len(cone.rays)
    if d == 0:
        return const(1)
    c = [sum(Fraction(xi[i]) * cone.rays[j][i] for i in range(cone.k)) for j in range(d)]
    box = cone.box_points()
    S = const(0)
    for x in box:
        S = S + exp_series(sum(Fraction(xi[i]) * x[i] for i in range(cone.k)))
    for j in range(d):
        S = S * inv_one_minus_exp(c[j])
    out = S
    for size in range(1, d + 1):
        for J in combinations(range(d), size):
            m = cone.index_of(J)
            I = const((-1) ** size * m)
            for j in J:
                I = I * inv_linear(c[j])
            q = cone.quotient(J)
            xq = _push(cone, J, xi)
            out = out - mu(q, xq) * I
    return out


def _push(cone: SimplicialCone, J: Sequence[int], xi: Sequence[Fraction]) -> List[Fraction]:
    """The linear form xi read in the quotient coordinates of the transverse cone along J."""
    _, base = cone.projected_basis(J)
    return [sum(Fraction(xi[i]) * b[i] for i in range(cone.k)) for b in base]


def weight(rays: Sequence[Sequence[int]], gram: Sequence[Sequence[Fraction]],
           xi: Sequence[Fraction] = None) -> Fraction:
    """alpha(C) = mu(C)(0) for the simplicial cone spanned by `rays`."""
    cone = SimplicialCone(rays, gram)
    if xi is None:
        xi = _generic_direction(cone)
    s = mu(cone, xi)
    assert all(s.at(n) == 0 for n in range(s.off, 0)), "the poles did not cancel"
    return s.at(0)


def _generic_direction(cone: SimplicialCone) -> List[Fraction]:
    """A rational xi with <xi, v> nonzero for every ray of every face, found by search."""
    from itertools import count
    import random
    rng = random.Random(20260905)
    for _ in count():
        xi = [Fraction(rng.randint(1, 97)) for _ in range(cone.k)]
        if _nondegenerate(cone, xi):
            return xi
    raise RuntimeError


def _nondegenerate(cone: SimplicialCone, xi: Sequence[Fraction]) -> bool:
    for j in range(len(cone.rays)):
        if sum(Fraction(xi[i]) * cone.rays[j][i] for i in range(cone.k)) == 0:
            return False
    for size in range(1, len(cone.rays)):
        for J in combinations(range(len(cone.rays)), size):
            q, xq = cone.quotient(J), _push(cone, J, xi)
            if not _nondegenerate(q, xq):
                return False
    return True
