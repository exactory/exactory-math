"""Exploratory (no credit): apply the general cut-and-shear lemma to the five size-15 instances in
their free coordinates. Pattern: lattice hyperplane {l = c} containing all vertices except a lattice
vertex a with l(a) = c+1 and lattice vertices b_1..b_m with l(b_i) = c-1; w a half-integral vertex on
the hyperplane; d = a + b_1 - 2w; U(x) = x + (l(x) - c) d. Report the vertices of P_+ u U(P_-) =
conv(K u {a} u {b_i - d}) (when the midpoints (a + b_i - d)/2 lie in K) and whether it is a lattice
polytope; iterate once more if a half-integral vertex remains."""
import itertools, os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "probes"))
import hivepoly
from PyNormaliz import Cone
import sympy

TRIPLES = {
 1: (((5,4,3,2,1),(4,3,2,1),(3,2)), [0,1,2]),
 2: (((5,4,3,2,1),(2,2,1),(4,3,2,1)), [1,3,4,5]),
 3: (((5,4,3,2,1),(3,2,1),(4,2,2,1)), [0,1,3,5]),
 4: (((5,4,3,2,1),(3,2,1),(3,3,2,1)), [0,1,3,5]),
 5: (((5,4,3,2,1),(3,2,1,1),(3,2,2,1)), [0,3,4,5]),
}

def hull_vertices(points):
    den = 1
    for p in points:
        for c in p:
            den = sympy.ilcm(den, F(c).denominator)
    pts = [[int(F(c) * den) for c in p] + [int(den)] for p in points]
    C = Cone(vertices=pts)
    return [[F(c, v[-1]) for c in v[:-1]] for v in C.VerticesOfPolyhedron()], C

def in_hull(pt, C):
    hyps = C.SupportHyperplanes()
    x = list(pt) + [F(1)]
    return all(sum(h[i] * x[i] for i in range(len(x))) >= 0 for h in hyps)

def try_pattern(coords, depth=0):
    k = len(coords[0])
    ints = [i for i, c in enumerate(coords) if all(x.denominator == 1 for x in c)]
    nonint = [i for i, c in enumerate(coords) if not all(x.denominator == 1 for x in c)]
    results = []
    # choose a: one lattice vertex with l(a) = c+1; the hyperplane contains all non-integral vertices and all other
    # lattice vertices except a set B (l = c-1).
    for a in ints:
        for size in range(1, len(ints)):
            for B in itertools.combinations([i for i in ints if i != a], size):
                others = [coords[i] for i in range(len(coords)) if i != a and i not in B]
                if len(others) < k:
                    continue
                Mo = sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in o] + [1] for o in others])
                null = Mo.nullspace()
                if len(null) != 1:
                    continue
                n = null[0]
                den = sympy.ilcm(*[sympy.fraction(x)[1] for x in n])
                n = [int(x * den) for x in n]
                g = 0
                for x in n[:-1]:
                    g = sympy.gcd(g, x)
                if g != 1:
                    continue
                l = lambda p: sum(n[i] * p[i] for i in range(k)) + n[-1]
                if l(coords[a]) == -1:
                    n = [-x for x in n]
                if l(coords[a]) != 1 or any(l(coords[b]) != -1 for b in B):
                    continue
                for wi in nonint:
                    w = coords[wi]
                    if any(2 * x != int(2 * x) for x in w):
                        continue  # not half-integral
                    b1 = coords[B[0]]
                    d = [coords[a][i] + b1[i] - 2 * w[i] for i in range(k)]
                    if any(x.denominator != 1 for x in d):
                        continue
                    U = lambda p: [p[i] + l(p) * d[i] for i in range(k)]
                    K = [coords[i] for i in range(len(coords)) if i != a and i not in B]
                    Kv, KC = hull_vertices(K)
                    mids_ok = all(in_hull([(coords[a][i] + U(coords[b])[i]) / 2 for i in range(k)], KC) for b in B)
                    newpts = K + [coords[a]] + [U(coords[b]) for b in B]
                    newv, _ = hull_vertices(newpts)
                    lattice = all(all(x.denominator == 1 for x in v) for v in newv)
                    results.append({"a": coords[a], "B": [coords[b] for b in B], "normal": n[:-1], "offset": n[-1], "w": w,
                                    "d": d, "midpoints_in_K": mids_ok, "new_vertices": newv, "lattice": lattice})
    return results

for key, ((lam, mu, nu), free) in TRIPLES.items():
    D, rows = hivepoly.hive_inequalities(lam, mu, nu)
    C = Cone(inhom_inequalities=rows)
    verts = [[F(c, v[-1]) for c in v[:-1]] for v in C.VerticesOfPolyhedron()]
    coords = [[v[i] for i in free] for v in verts]
    print("==", key, lam, mu, nu, "dim", C.AffineDim())
    res = try_pattern(coords)
    good = [r for r in res if r["midpoints_in_K"]]
    print("   patterns with midpoints in K:", len(good), "of", len(res))
    for r in good[:6]:
        print("    a", [str(x) for x in r["a"]], "B", [[str(x) for x in b] for b in r["B"]], "normal", r["normal"], "w", [str(x) for x in r["w"]],
              "d", [str(x) for x in r["d"]], "lattice:", r["lattice"])
        if not r["lattice"]:
            nonint_new = [v for v in r["new_vertices"] if not all(x.denominator == 1 for x in v)]
            print("      remaining non-integral vertices:", [[str(x) for x in v] for v in nonint_new])
            # iterate once
            res2 = try_pattern(r["new_vertices"])
            good2 = [q for q in res2 if q["midpoints_in_K"] and q["lattice"]]
            print("      second step lattice patterns:", len(good2))
            for q in good2[:2]:
                print("        a", [str(x) for x in q["a"]], "B", [[str(x) for x in b] for b in q["B"]], "normal", q["normal"], "d", [str(x) for x in q["d"]],
                      "final vertices", [[str(x) for x in v] for v in q["new_vertices"]])
