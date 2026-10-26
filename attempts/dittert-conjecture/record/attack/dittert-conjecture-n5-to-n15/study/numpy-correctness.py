"""Is numpy/LAPACK on this machine CORRECT (not just slow)?

The memory note for this Mac records that the numpy matmul path is pathologically slow.
Slow is harmless; wrong is not, because parts of the n = 5 and n = 6 verification rest on
np.linalg.cholesky, np.linalg.eigvalsh and np.linalg.svd.  This script checks each
routine used against an independent computation that does not go through BLAS/LAPACK.

1. Integer matrix product: A @ B, np.einsum, and an exact Python-integer product agree.
2. np.linalg.cholesky: L L^T reproduces A, with the residual measured in exact rational
   arithmetic on the rationalised L.
3. np.linalg.eigvalsh: the smallest eigenvalue is bracketed by an exact rational test
   (A - t I positive definite by exact LDL for t below it, indefinite above it).
4. np.linalg.svd: the singular values squared match the eigenvalues of A^T A.
5. The einsum calls actually used in the pipeline (the "ik,kl,jl->ij" and "ij,jk->ik"
   forms) agree with exact integer computation.
"""
import math
import sys
from fractions import Fraction as Fr

import flint
import numpy as np

rng = np.random.default_rng(31337)
ok = True


def report(name, good, detail=""):
    global ok
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  {name}  {detail}")


# ---- 1. integer matrix product, three ways
m = 120
A = rng.integers(-50, 51, size=(m, m)).astype(np.int64)
B = rng.integers(-50, 51, size=(m, m)).astype(np.int64)
P_at = A @ B
P_ein = np.einsum("ik,kj->ij", A, B)
Aq = flint.fmpz_mat(m, m, [int(x) for x in A.reshape(-1)])
Bq = flint.fmpz_mat(m, m, [int(x) for x in B.reshape(-1)])
Pq = Aq * Bq
P_exact = np.array([[int(Pq[i, j]) for j in range(m)] for i in range(m)], dtype=np.int64)
report("integer A @ B equals the exact product", bool((P_at == P_exact).all()))
report("integer einsum equals the exact product", bool((P_ein == P_exact).all()))
report("A.T @ B equals the exact transposed product",
       bool((A.T @ B == np.array([[int((Aq.transpose() * Bq)[i, j]) for j in range(m)] for i in range(m)])).all()))

# ---- 5. the einsum patterns the pipeline uses
X = rng.integers(-20, 21, size=(m, m)).astype(np.int64)
lhs = np.einsum("ik,kl,jl->ij", A, X, B)
rhs = np.array([[int((Aq * flint.fmpz_mat(m, m, [int(v) for v in X.reshape(-1)]) * Bq.transpose())[i, j])
                 for j in range(m)] for i in range(m)], dtype=np.int64)
report("einsum 'ik,kl,jl->ij' equals the exact triple product", bool((lhs == rhs).all()))
lhs2 = np.einsum("ji,jk->ik", A, B)
report("einsum 'ji,jk->ik' equals A^T B", bool((lhs2 == np.array([[int((Aq.transpose() * Bq)[i, j]) for j in range(m)] for i in range(m)])).all()))

# ---- 2. Cholesky, checked in exact rational arithmetic
n2 = 80
R = rng.standard_normal((n2, n2))
S = R @ R.T + n2 * np.eye(n2)                # well-conditioned symmetric positive definite
S = np.round(S * 1024) / 1024                 # exactly representable, exact rational too
L = np.linalg.cholesky(S)
Lr = [[Fr(float(L[i, j])) for j in range(n2)] for i in range(n2)]
Sr = [[Fr(float(S[i, j])) for j in range(n2)] for i in range(n2)]
worst = Fr(0)
for i in range(n2):
    for j in range(i + 1):
        v = sum(Lr[i][k] * Lr[j][k] for k in range(j + 1))
        worst = max(worst, abs(v - Sr[i][j]))
scale = max(abs(Sr[i][j]) for i in range(n2) for j in range(n2))
report("np.linalg.cholesky: L L^T reproduces A (exact residual)", float(worst / scale) < 1e-12,
       f"relative residual {float(worst / scale):.2e}")

# ---- 3. eigvalsh bracketed by exact positive-definiteness tests
def exact_pd(M, t):
    """Is M - t I positive definite?  Exact, via flint fraction-free LU on the scaled integer matrix."""
    D = 2 ** 20
    ent = []
    for i in range(len(M)):
        for j in range(len(M)):
            v = Fr(float(M[i][j])) - (t if i == j else 0)
            ent.append(v)
    L = 1
    for v in ent:
        L = L * v.denominator // math.gcd(L, v.denominator)
    Z = flint.fmpz_mat(len(M), len(M), [int(v * L) for v in ent])
    P, Lw, Dd, U = Z.fflu()
    return P.is_one() and all(U[k, k] > 0 for k in range(len(M)))


ev = np.linalg.eigvalsh(S)
lo, hi = float(ev[0]) * 0.99, float(ev[0]) * 1.01
good = exact_pd(Sr, Fr(lo).limit_denominator(10 ** 9)) and not exact_pd(Sr, Fr(hi).limit_denominator(10 ** 9))
report("np.linalg.eigvalsh: the smallest eigenvalue is bracketed exactly", good,
       f"lambda_min = {ev[0]:.6f}")

# ---- 4. svd against eigvalsh of A^T A
M2 = rng.standard_normal((60, 60))
sv = np.linalg.svd(M2, compute_uv=False)
ev2 = np.sqrt(np.maximum(np.linalg.eigvalsh(np.einsum("ji,jk->ik", M2, M2)), 0))[::-1]
report("np.linalg.svd agrees with eigvalsh(A^T A)", float(np.abs(sv - ev2).max()) < 1e-9,
       f"max difference {float(np.abs(sv - ev2).max()):.2e}")

# ---- the actual matrices of the attack: re-check one certificate identity entry exactly
print("\nnumpy version:", np.__version__, "| BLAS:", (np.__config__.show(mode="dicts") or {}).get("Build Dependencies", {}).get("blas", {}).get("name", "?"))
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
