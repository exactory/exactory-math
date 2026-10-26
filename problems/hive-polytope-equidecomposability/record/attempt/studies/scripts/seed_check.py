"""Exploratory check of the hand construction for the smallest non-lattice hive polytope.
H = conv{0, e1, e3, e1+e3, p=(1,1,1), w=(1/2,-1/2,1/2)}; U(x,y,z) = (x, y + x - z, z);
Q = H+ u U(H-) with H+ = H n {x >= z}, H- = H n {x <= z}. Claims: Q = conv{0,(1,0,1),(1,1,1),(1,0,0),(0,-1,1)},
L_Q = L_H = 1 + 2t + 3/2 t^2 + 1/2 t^3, and the pieces are disjoint."""
from fractions import Fraction as F
from PyNormaliz import Cone
import itertools

def ehrhart(vertices):
    # vertices as integer-scaled: use inhom from polytope vertices via Normaliz 'polytope' input (rational)
    den = 1
    for v in vertices:
        for c in v:
            den = den * F(c).denominator // __import__("math").gcd(den, F(c).denominator)
    pts = [[int(F(c) * den) for c in v] + [den] for v in vertices]
    C = Cone(vertices=pts)
    q = C.EhrhartQuasiPolynomial()
    period = len(q) - 1
    d = q[-1]
    return period, [[F(c, d) for c in comp] for comp in q[:-1]], C.AffineDim()

H = [(0,0,0),(1,0,0),(0,0,1),(1,0,1),(1,1,1),(F(1,2),F(-1,2),F(1,2))]
Q = [(0,0,0),(1,0,1),(1,1,1),(1,0,0),(0,-1,1)]
print("H:", ehrhart(H))
print("Q:", ehrhart(Q))
# count lattice points of tH and of t(H+) + t U(H- minus plane) directly for t = 1..6 by brute force
def in_hull(pt, vertices):
    # membership via Normaliz: check with supporting hyperplanes
    den = 1
    for v in vertices:
        for c in v:
            den = den * F(c).denominator // __import__("math").gcd(den, F(c).denominator)
    pts = [[int(F(c) * den) for c in v] + [den] for v in vertices]
    C = Cone(vertices=pts)
    hyps = C.SupportHyperplanes()
    x = list(pt) + [1]
    return all(sum(h[i] * x[i] for i in range(4)) >= 0 for h in hyps)
def U(p):
    x, y, z = p
    return (x, y + x - z, z)
def Uinv(p):
    x, y, z = p
    return (x, y - x + z, z)
for t in range(1, 7):
    tH = [tuple(c * t for c in v) for v in H]
    tQ = [tuple(c * t for c in v) for v in Q]
    R = range(-t - 1, 2 * t + 2)
    nH = sum(1 for p in itertools.product(R, R, R) if in_hull(p, tH))
    nQ = sum(1 for p in itertools.product(R, R, R) if in_hull(p, tQ))
    # pieces: points of tQ with x >= z should be in tH (H+ part); points with x < z should map by U^{-1} into tH with x < z
    ok = True
    for p in itertools.product(R, R, R):
        if not in_hull(p, tQ):
            continue
        x, y, z = p
        if x >= z:
            ok &= in_hull(p, tH)
        else:
            q = Uinv(p)
            ok &= in_hull(q, tH) and q[0] < q[2]
    print("t", t, "L_H", nH, "L_Q", nQ, "pieces consistent", ok)
