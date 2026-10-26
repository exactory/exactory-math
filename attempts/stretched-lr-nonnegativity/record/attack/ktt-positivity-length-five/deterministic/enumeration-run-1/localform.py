#!/usr/bin/env python3
"""Local Ehrhart formula data of hive polytopes: faces, transverse cone types, relative volumes.

For a rational polytope P of dimension D whose dilate qP is a lattice polytope, the McMullen
local formula (Berline-Vergne; transferred to the rational polytope by the period-one dilation
lemma of Ferudun 2026, Section 3) writes the Ehrhart coefficients as

    a_k(P) = sum over the k-dimensional faces F of P of  alpha(type(F)) * relvol(F),

where relvol(F) is the volume of F relative to the lattice in its affine hull (Normaliz's
`Volume` divided by k!), and alpha depends only on the transverse cone of P along F, hence only
on the set of primitive outward normals of the facets containing F (the normal cone is the cone
they generate, and the transverse lattice is dual to the saturation of the lattice they span).

This module extracts, for a hive polytope:
  * the outward primitive facet normals,
  * the faces of a given codimension with their normal sets and relative volumes (`faces_by_codim`,
    which calls Normaliz once per face), and
  * the edges with their lattice lengths and normal sets (`edges`, exact arithmetic from the
    vertices and support hyperplanes, no Normaliz call per edge).

`alpha_pair` is the closed weight of a two-dimensional transverse cone (Castillo-Liu Lemma 3.3,
in the form recorded in the replay repository of Ferudun 2026, `proof/r5/alpha5.py`); it is used
only to validate the extraction against the recorded coefficients.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from math import factorial, gcd
from typing import Dict, List, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities  # noqa: E402


def prim(v: Sequence[int]) -> Tuple[int, ...]:
    g = 0
    for x in v:
        g = gcd(g, abs(int(x)))
    return tuple(int(x) // g for x in v) if g else tuple(int(x) for x in v)


def as_frac(v) -> Fraction:
    return Fraction(v[0], v[1]) if isinstance(v, list) else Fraction(v)


def dot(a: Sequence[int], b: Sequence[int]) -> int:
    return sum(x * y for x, y in zip(a, b))


def sat_index(u: Sequence[int], v: Sequence[int]) -> int:
    g = 0
    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            g = gcd(g, abs(u[i] * v[j] - u[j] * v[i]))
    return g


def alpha_pair(u: Sequence[int], v: Sequence[int]) -> Fraction:
    """Weight of the two-dimensional transverse cone of a codimension-two face."""
    q = sat_index(u, v)
    A, B, C = dot(u, u), dot(v, v), dot(u, v)
    if q == 1:
        return Fraction(1, 4) - Fraction(C, 12) * (Fraction(1, A) + Fraction(1, B))
    if q == 2:
        if any((a + b) % 2 for a, b in zip(u, v)):
            raise ValueError("saturation index 2 but the half sum is not integral")
        s = tuple((a + b) // 2 for a, b in zip(u, v))
        t = tuple((a - b) // 2 for a, b in zip(u, v))
        if dot(s, t) != 0:
            raise ValueError("saturation index 2 but the half sums are not orthogonal")
        Ap, Bp = dot(s, s), dot(t, t)
        return Fraction(Ap + 2 * Bp, 6 * (Ap + Bp))
    raise ValueError(f"unexpected saturation index {q}")


def rank_of(rows: Sequence[Sequence[int]]) -> int:
    """Exact rank over the rationals."""
    m = [[Fraction(x) for x in r] for r in rows]
    r = 0
    ncols = len(m[0]) if m else 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


class HivePolytope:
    """A hive polytope with its Normaliz description, for local-formula extraction."""

    def __init__(self, lam, mu, nu):
        from PyNormaliz import Cone  # type: ignore

        self.lam, self.mu, self.nu = tuple(lam), tuple(mu), tuple(nu)
        self.D, self.rows = hive_inequalities(lam, mu, nu)
        self.cone = Cone(inhom_inequalities=self.rows)
        self.dim = self.cone.AffineDim()
        self.support = self.cone.SupportHyperplanes()          # a.x + b >= 0
        self.normals = [prim([-a for a in h[: self.D]]) for h in self.support]
        self.vertices = [
            (tuple(Fraction(x, v[-1]) for x in v[: self.D])) for v in self.cone.VerticesOfPolyhedron()
        ]

    def is_full_dimensional(self) -> bool:
        return self.dim == self.D

    def ehrhart(self) -> List[Fraction]:
        q = self.cone.EhrhartQuasiPolynomial()
        if len(q) - 1 != 1:
            raise ValueError("period is not one")
        den = q[-1]
        c = [Fraction(x, den) for x in q[0]]
        while len(c) > 1 and c[-1] == 0:
            c.pop()
        return c

    def active(self, point) -> Tuple[int, ...]:
        """Indices of the support hyperplanes tight at a point."""
        out = []
        for i, h in enumerate(self.support):
            if sum(Fraction(h[j]) * point[j] for j in range(self.D)) + h[self.D] == 0:
                out.append(i)
        return tuple(out)

    def faces_by_codim(self, codim_bound: int) -> Dict[int, List[Tuple[Tuple[int, ...], Fraction]]]:
        """Faces of codimension <= codim_bound as (active support indices, relative volume)."""
        from PyNormaliz import Cone  # type: ignore

        self.cone.SetFaceCodimBound(codim_bound)
        out: Dict[int, List[Tuple[Tuple[int, ...], Fraction]]] = {}
        for bits, codim in self.cone.FaceLattice():
            act = tuple(i for i, b in enumerate(bits) if b)
            if codim > self.dim:          # the empty face
                continue
            if codim == 0:
                vol = as_frac(self.cone.Volume())
            else:
                F = Cone(inhom_equations=[self.support[i] for i in act], inhom_inequalities=self.support)
                if F.AffineDim() != self.dim - codim:
                    continue
                vol = as_frac(F.Volume())
            out.setdefault(codim, []).append((act, vol / factorial(self.dim - codim)))
        return out

    def edges(self) -> List[Tuple[Tuple[Tuple[int, ...], ...], Fraction]]:
        """Edges as (sorted tuple of outward primitive normals, lattice length).

        Two vertices span an edge exactly when the normals of the facets tight at both have rank
        dim - 1. The lattice length of the segment is the factor t with q - p = t * v, v the
        primitive integer vector in the direction of the edge.
        """
        acts = [self.active(p) for p in self.vertices]
        out = []
        n = len(self.vertices)
        for i in range(n):
            for j in range(i + 1, n):
                common = tuple(sorted(set(acts[i]) & set(acts[j])))
                if len(common) < self.dim - 1:
                    continue
                if rank_of([self.support[k][: self.D] for k in common]) != self.dim - 1:
                    continue
                p, q = self.vertices[i], self.vertices[j]
                d = [b - a for a, b in zip(p, q)]
                den = 1
                for x in d:
                    den = den * x.denominator // gcd(den, x.denominator)
                di = [int(x * den) for x in d]
                g = 0
                for x in di:
                    g = gcd(g, abs(x))
                v = [x // g for x in di]
                t = Fraction(g, den)
                out.append((tuple(sorted(self.normals[k] for k in common)), t))
        return out


def check_top_coefficients(lam, mu, nu) -> Dict[str, object]:
    """Validate the extraction: the top three Ehrhart coefficients from the local formula."""
    P = HivePolytope(lam, mu, nu)
    if not P.is_full_dimensional():
        return {"skipped": "not full-dimensional", "dim": P.dim}
    a = P.ehrhart()
    D = P.dim
    faces = P.faces_by_codim(2)
    got = {D: faces[0][0][1],
           D - 1: sum(v for _, v in faces[1]) / 2,
           D - 2: sum(alpha_pair(*[P.normals[i] for i in ext_rays(P, act)]) * v
                      for act, v in faces.get(2, []))}
    return {"lam": list(lam), "mu": list(mu), "nu": list(nu), "dim": D,
            "facets": len(P.support), "codim2": len(faces.get(2, [])),
            "agree": all(a[k] == got[k] for k in got),
            "recorded": {k: str(a[k]) for k in got}, "local": {k: str(got[k]) for k in got}}


def ext_rays(P: "HivePolytope", act: Sequence[int]) -> Tuple[int, int]:
    """The two extreme rays of a two-dimensional normal cone given by the active facets."""
    if len(act) == 2:
        return act[0], act[1]
    ns = [P.normals[i] for i in act]
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            u, v = ns[i], ns[j]
            if all(_in_cone(w, u, v) for w in ns):
                return act[i], act[j]
    raise ValueError("no extreme pair found in a two-dimensional normal cone")


def _in_cone(w, u, v) -> bool:
    """Is w a nonnegative combination of u and v (all in one plane)?"""
    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            det = u[i] * v[j] - u[j] * v[i]
            if det == 0:
                continue
            s = Fraction(w[i] * v[j] - w[j] * v[i], det)
            t = Fraction(u[i] * w[j] - u[j] * w[i], det)
            return s >= 0 and t >= 0
    return False
