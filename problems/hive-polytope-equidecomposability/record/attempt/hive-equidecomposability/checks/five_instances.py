"""Exploratory: vertex data of the five size-15 five-part hive polytopes with a non-integral vertex."""
import os
import sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "probes"))
import hivepoly
from PyNormaliz import Cone
TRIPLES = [((5,4,3,2,1),(3,2),(4,3,2,1)), ((5,4,3,2,1),(2,2,1),(4,3,2,1)), ((5,4,3,2,1),(3,2,1),(4,2,2,1)),
           ((5,4,3,2,1),(3,2,1),(3,3,2,1)), ((5,4,3,2,1),(3,2,1,1),(3,2,2,1))]
for lam, mu, nu in TRIPLES:
    D, rows = hivepoly.hive_inequalities(lam, mu, nu)
    C = Cone(inhom_inequalities=rows)
    verts = [[F(c, v[-1]) for c in v[:-1]] for v in C.VerticesOfPolyhedron()]
    eqs = C.Equations()
    print("==", lam, mu, nu, "dim", C.AffineDim(), "c", hivepoly.count_hives(lam, mu, nu, 1), "ehrhart", hivepoly.ehrhart_polynomial(lam, mu, nu)[2])
    print("   equations", eqs)
    for v in verts:
        print("   ", [str(x) for x in v], "" if all(x.denominator == 1 for x in v) else "<- non-integral")
    print("   support hyperplanes", C.SupportHyperplanes())
