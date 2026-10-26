"""An exact integer positive-semidefiniteness certificate for the n = 6 main Gram matrix.

The n = 6 certificate (`certified-special-case-check-2`) proves positive definiteness of its
8436 x 8436 main Gram by a floating-point Cholesky factorisation with Higham's rigorous
backward-error bound.  That is a theorem given IEEE-754 semantics, not a gap; this script
replaces it with integer arithmetic, which is what `n = 5` already has.

The certificate is the one `Cert/Sym.lean` calls the exact route:

    B := A + d J - delta I,        N := integer Cholesky of B (truncating division),
    E := A + d J - N N^T   is diagonally dominant with non-negative diagonal.

Then `E >= 0` by Gershgorin, `N N^T >= 0`, so `A + d J >= 0`; and `A . 1 = 0` gives `A >= 0`.
No `F` scaling is needed at this size: the integer entries already reach 2.5e16, so the pivots
are around 4.6e12 and their integer square roots carry seven significant digits.

Two things make it run.  The entries are divided by their greatest common divisor first, which
keeps every partial sum inside `int64`; a float64 shadow of each column update checks that, and
the run stops if it fails.  The residual `N N^T` is formed once, by FLINT's multi-precision
integer matrix multiplication, which is multi-modular inside and does not overflow at all.
"""
import json
import math
import sys
import time

import numpy as np

T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


HERE = __import__("pathlib").Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "numerical-optimisation-run-3"))
from sdp_n import build  # noqa: E402

cert = json.load(open(HERE.parent / "certified-special-case-check-2" / "certificate6.json"))
S = build(6)
MD = len(S["VD"].mons)
log(f"main Gram {MD} x {MD}")

from fractions import Fraction as Fr  # noqa: E402
coords = [Fr(x) for x in cert["main"]]
den = 1
for c in coords:
    den = den * c.denominator // math.gcd(den, c.denominator)
vals = np.array([int(c * den) for c in coords], dtype=object)
g = 0
for v in vals:
    g = math.gcd(g, int(v))
log(f"den = {den}, gcd of the orbit values = {g}")
vals = np.array([int(v) // g for v in vals], dtype=np.int64)

u = np.unique(S["labD"])
assert len(u) == len(coords)
A = vals[np.searchsorted(u, S["labD"])].reshape(MD, MD)
assert (A == A.T).all() and (A.sum(axis=1) == 0).all()
amax = int(np.abs(A).max())
log(f"after dividing by the gcd: max |A| = {amax:.4e}")

lam2 = float(np.linalg.eigvalsh(A.astype(np.float64))[1])
assert lam2 > 0, lam2
d = max(1, int(math.ceil(lam2 / MD)))
delta = int(lam2 // 2)
log(f"lambda_2 = {lam2:.6e}, d = {d}, delta = {delta}")

B = A + d
np.fill_diagonal(B, np.diagonal(B) - delta)
assert np.abs(B).max() < 2 ** 62

log("integer Cholesky")
N = np.zeros((MD, MD), dtype=np.int64)
Bf = B.astype(np.float64)
Nf = np.zeros((MD, MD))
for i in range(MD):
    s = int(B[i, i]) - (int(N[i, :i] @ N[i, :i]) if i else 0)
    if s <= 0:
        raise SystemExit(f"pivot {i} is {s} <= 0")
    nii = math.isqrt(s)
    N[i, i] = nii
    Nf[i, i] = float(nii)
    if i + 1 < MD:
        t = B[i + 1:, i] - (N[i + 1:, :i] @ N[i, :i] if i else 0)
        tf = Bf[i + 1:, i] - (Nf[i + 1:, :i] @ Nf[i, :i] if i else 0.0)
        if np.abs(tf).max() > 4e18:
            raise SystemExit(f"column {i}: partial sums reach {np.abs(tf).max():.3e}, int64 unsafe")
        N[i + 1:, i] = t // nii
        Nf[i + 1:, i] = N[i + 1:, i]
    if i % 1000 == 0:
        log(f"  column {i}, pivot {nii}")
log(f"max |N| = {int(np.abs(N).max()):.4e}")

log("N N^T by FLINT multi-precision integer matrix multiplication")
from flint import fmpz_mat  # noqa: E402
Nm = fmpz_mat([[int(x) for x in row] for row in N])
NN = Nm * Nm.transpose()
log("residual and diagonal dominance")
E = np.array([[int(NN[i, j]) for j in range(MD)] for i in range(MD)], dtype=object)
AplusdJ = (A.astype(object) + d)
E = AplusdJ - E
diag = np.array([int(E[i, i]) for i in range(MD)], dtype=object)
off = np.array([sum(abs(int(E[i, j])) for j in range(MD) if j != i) for i in range(MD)],
               dtype=object)
slack = min(int(diag[i]) - int(off[i]) for i in range(MD))
log(f"diagonal dominance slack: min {slack}")
if slack < 0:
    raise SystemExit(f"EXACT PSD FAIL: negative diagonal-dominance slack {slack}")
print("EXACT PSD PASS")
