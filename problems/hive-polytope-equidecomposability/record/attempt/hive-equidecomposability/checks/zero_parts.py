"""Exploratory (no native credit): does appending zero parts (side n -> n + 1, n + 2) change the
hive polytope up to affine unimodular equivalence? For admissible triples (|lam| = |mu| + |nu| in
the notation of hivepoly.py), compare the dimension, the number of vertices, the vertex
denominators and the Ehrhart polynomial at sides 5, 6, 7, and list the interior labels that are
constant over all vertices (the forced labels of Lemma Z)."""
import sys
from fractions import Fraction as F

from PyNormaliz import Cone


def hive_with_side(lam, mu, nu, n):
    lam, mu, nu = tuple(lam), tuple(mu), tuple(nu)
    assert sum(lam) == sum(mu) + sum(nu), "inadmissible triple"
    assert max(len(lam), len(mu), len(nu)) <= n
    lam_p = list(lam) + [0] * (n - len(lam))
    mu_p = list(mu) + [0] * (n - len(mu))
    nu_p = list(nu) + [0] * (n - len(nu))
    boundary = {}
    for y in range(n + 1):
        boundary[(0, y)] = sum(mu_p[:y])
    for x in range(n + 1):
        boundary[(x, 0)] = sum(lam_p[:x])
    for x in range(n + 1):
        boundary[(x, n - x)] = sum(mu_p) + sum(nu_p[:x])
    interior = [(x, y) for x in range(1, n) for y in range(1, n) if x + y <= n - 1]
    index = {v: i for i, v in enumerate(interior)}
    D = len(interior)
    rows = []

    def add(plus, minus):
        row = [0] * (D + 1)
        for v in plus:
            if v in index:
                row[index[v]] += 1
            else:
                row[D] += boundary[v]
        for v in minus:
            if v in index:
                row[index[v]] -= 1
            else:
                row[D] -= boundary[v]
        if any(row[:D]):
            rows.append(row)
        elif row[D] < 0:
            raise ValueError("empty")

    for x in range(n + 1):
        for y in range(n + 1):
            if x + y <= n - 2:
                add([(x + 1, y), (x, y + 1)], [(x, y), (x + 1, y + 1)])
            if y >= 1 and x + y <= n - 1:
                add([(x, y), (x + 1, y)], [(x, y + 1), (x + 1, y - 1)])
            if x >= 1 and x + y <= n - 1:
                add([(x, y), (x, y + 1)], [(x + 1, y), (x - 1, y + 1)])
    C = Cone(inhom_inequalities=rows)
    verts = [[F(c, v[-1]) for c in v[:-1]] for v in C.VerticesOfPolyhedron()]
    q = C.EhrhartQuasiPolynomial()
    den = q[-1]
    poly = [F(c, den) for c in q[0]] if len(q) == 2 else q
    return interior, C.AffineDim(), verts, poly


TRIPLES = [((5, 4, 3, 2, 1), (4, 3, 2, 1), (3, 2)),        # the seed pair, hivepoly notation (lam = nu of the statement)
           ((6, 5, 4, 2, 2), (4, 3, 3, 1), (4, 2, 1, 1)),  # Ferudun's dim-3 five-part example with all Horn inequalities strict
           ((3, 2, 1), (2, 1), (2, 1))]
for lam, mu, nu in TRIPLES:
    for n in (5, 6, 7):
        interior, dim, verts, poly = hive_with_side(lam, mu, nu, n)
        dens = sorted({max(x.denominator for x in v) for v in verts})
        forced = [interior[i] for i in range(len(interior)) if len({v[i] for v in verts}) == 1]
        print(lam, mu, nu, "side", n, "D", len(interior), "dim", dim, "#vertices", len(verts),
              "denominators", dens, "ehrhart", [str(c) for c in poly])
        print("    forced interior labels:", forced)
