"""Independent check for numerical optimisation run 4: re-evaluate the recorded minimisers.

For each recorded matrix B: feasibility (nonnegative, row and column sums 1 to 1e-8,
b_11 = 0), the permanent by a direct sum over permutations (no code shared with run.py's
Ryser formula), lambda_2 = 1 - sigma_2(B) by numpy's SVD, and agreement with the recorded
values to 1e-6; also that per(B)/gamma_n <= 1 + eta + 1e-6 and that the recorded c_n
matches its definition.
"""
import itertools
import json
import math
import sys

import numpy as np

d = json.load(open("gap-minima.json"))
ok = True
for k, rec in d.items():
    n = rec["n"]
    B = np.array(rec["matrix"])
    gamma = math.factorial(n) / n ** n
    feas = (B >= -1e-12).all() and abs(B.sum(1) - 1).max() < 1e-8 and abs(B.sum(0) - 1).max() < 1e-8 and B[0, 0] == 0
    per = sum(math.prod(B[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    l2 = 1 - np.linalg.svd(B, compute_uv=False)[1]
    g = gamma
    h = math.sqrt(2 * g)
    c = 2 * math.sqrt(g / ((1 - g) * (1 - 2 * h / 3))) / (1 - h)
    good = feas and abs(per / gamma - rec["per_over_gamma"]) < 1e-6 and abs(l2 - rec["min_lambda2"]) < 1e-6 \
        and per / gamma <= 1 + rec["eta"] + 1e-6 and abs(c - rec["c_n"]) < 1e-9
    print(f"n={n}: feasible={feas}, per/gamma={per / gamma:.6f} (recorded {rec['per_over_gamma']:.6f}), "
          f"lambda_2={l2:.6f} (recorded {rec['min_lambda2']:.6f}), c_n={c:.5f}: {'ok' if good else 'MISMATCH'}")
    ok &= good
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
