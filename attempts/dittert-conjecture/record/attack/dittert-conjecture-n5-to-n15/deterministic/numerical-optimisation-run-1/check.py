"""Independent check for numerical optimisation run 1.

Re-evaluates phi at each recorded optimiser in exact rational arithmetic (Fractions;
the permanent by a direct sum over permutations, sharing no code with run.py),
verifies feasibility after rationalisation (nonnegative, entry sum n, a_11 = 0),
and confirms the recorded value to 1e-9 and the sign of the recorded gap.
"""
import itertools
import json
import math
import sys
from fractions import Fraction as Fr

d = json.load(open("optima.json"))
ok = True
for rec in d.values():
    n = rec["n"]
    A = [[Fr(x).limit_denominator(10 ** 12) for x in row] for row in rec["optimiser"]]
    A[0][0] = Fr(0)
    s = sum(sum(r) for r in A)
    A = [[x * n / s for x in r] for r in A]
    assert all(x >= 0 for r in A for x in r)
    assert sum(sum(r) for r in A) == n and A[0][0] == 0
    R = math.prod(sum(r) for r in A)
    C = math.prod(sum(A[i][j] for i in range(n)) for j in range(n))
    P = sum(math.prod(A[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    phi = R + C - P
    gamma = Fr(math.factorial(n), n ** n)
    g = 2 - gamma - phi
    diff = abs(float(phi) - rec["max_phi_on_face"])
    print(f"n={n}: exact phi at rationalised optimiser = {float(phi):.12f} "
          f"(recorded {rec['max_phi_on_face']:.12f}, diff {diff:.1e}); "
          f"exact gap = {float(g):.6e} {'> 0' if g > 0 else '<= 0 !!'}")
    ok &= diff < 1e-9 and (g > 0) == (rec["boundary_gap"] > 0)
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
