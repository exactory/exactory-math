"""Exploratory check (not admitted evidence): the smallest five-part hive polytopes with
non-integral vertices, and the data of the first one.

Run on 2026-10-20 with the interpreter of the dim2-hives-1 probe
(<venv>/bin/python,
PyNormaliz available). The output is kept in instance_check.out.txt. Notation of hivepoly.py:
c^{lam}_{mu,nu} with |lam| = |mu| + |nu|; in the statement's notation lam is nu.
"""
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "probes"))
import hivepoly  # noqa: E402
from PyNormaliz import Cone  # noqa: E402


def partitions_max_parts(size, parts):
    def rec(remaining, maxpart, left):
        if remaining == 0:
            yield ()
            return
        if left == 0:
            return
        for p in range(min(remaining, maxpart), 0, -1):
            for rest in rec(remaining - p, p, left - 1):
                yield (p,) + rest
    return list(rec(size, size, parts))


def vertex_data(lam, mu, nu):
    D, rows = hivepoly.hive_inequalities(lam, mu, nu)
    C = Cone(inhom_inequalities=rows)
    dim = C.AffineDim()
    verts = C.VerticesOfPolyhedron()
    dens = []
    for v in verts:
        den = v[-1]
        g = 0
        for c in v[:-1]:
            g = math.gcd(g, c)
        g = math.gcd(g, den)
        dens.append(den // g)
    return D, dim, verts, max(dens)


def main():
    lam, mu, nu = (5, 4, 3, 2, 1), (4, 3, 2, 1), (3, 2)
    D, dim, verts, maxden = vertex_data(lam, mu, nu)
    c1 = hivepoly.count_hives(lam, mu, nu, 1)
    print("instance", lam, mu, nu, "D", D, "dim", dim, "vertices", len(verts), "maxden", maxden, "c", c1)
    print("ehrhart", hivepoly.ehrhart_polynomial(lam, mu, nu))
    for v in verts:
        print("  vertex", [Fraction(x, v[-1]) for x in v[:-1]])
    found = []
    for size in range(5, 16):
        for lamx in partitions_max_parts(size, 5):
            if len(lamx) != 5:
                continue
            for a in range(1, size):
                for mux in partitions_max_parts(a, 5):
                    for nux in partitions_max_parts(size - a, 5):
                        if mux > nux:  # symmetry c^lam_{mu,nu} = c^lam_{nu,mu}
                            continue
                        try:
                            hivepoly.hive_inequalities(lamx, mux, nux)
                        except ValueError:
                            continue
                        if hivepoly.count_hives(lamx, mux, nux, 1) == 0:
                            continue
                        _, dimx, vertsx, maxdenx = vertex_data(lamx, mux, nux)
                        if maxdenx > 1:
                            found.append((size, lamx, mux, nux, dimx, maxdenx, len(vertsx)))
        if found:
            print("smallest size with a non-integral vertex:", size)
            for f in found[:40]:
                print("  ", f)
            break
    else:
        print("no non-integral vertex up to size 15")


main()
