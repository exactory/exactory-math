"""Two-sided Moebius (diagram) expansion of the matching sums r_k(F), and the best diagram-wise
bound it gives for the Taylor tail at n = 7 in the application regime.

For F with zero row and column sums,

    k! r_k(F) = sum_{pi, rho} mu(pi) mu(rho) hom(G_{pi,rho}, F)

over set partitions pi, rho of [k] with no singleton block; G_{pi,rho} is the bipartite
multigraph with a row-vertex per block of pi, a column-vertex per block of rho, and one edge per
element l of [k] joining the block of pi containing l to the block of rho containing l;
hom(G, F) = sum over labellings of the vertices by [n] of the product of F over the edges.

Part 1 verifies the expansion against the direct matching sum at n = 7 for k = 4, 5 on random
zero-margin F (k = 6, 7 use fewer samples).

Part 2 bounds each diagram in the regime of the Dittert application at n = 7 (from the
capacity route, Theorem 1 + Lemma C applied to every row and column of a matrix with
per(B) <= e^{K_0} gamma_7, K_0 = log(m_7/gamma_7)):

    Phi = ||F||_F^2 <= 49 * 0.1861,   every row and column of F has squared norm <= 49 * 2 K_0,
    max |F_ij| <= 7 * sqrt(2 K_0),

using, for a diagram with column-vertex degrees d_w and row-vertex degrees d_v,

    |hom| <= prod_w sum_j C_j^{d_w/2} <= c0^{k - 2|V_c|} Phi^{|V_c|}    (contract rows first),
    |hom| <= r0^{k - 2|V_r|} Phi^{|V_r|}                                 (contract columns first),
    |hom| <= Phi m^{k-2}  for the one-block/one-block diagram (it is sum F_ij^k),

and reports sum_{pi,rho} |mu mu| bound / (k! (n)_k) as a multiple of ||E||_F^2 = Phi/49 at the
largest Phi of the regime.  This is the number the k >= 5 tail would have to beat.
"""
import itertools
import math

import numpy as np

rng = np.random.default_rng(8)
n = 7


def set_partitions(elements):
    if not elements:
        yield []
        return
    first, rest = elements[0], elements[1:]
    for smaller in set_partitions(rest):
        for i in range(len(smaller)):
            yield smaller[:i] + [[first] + smaller[i]] + smaller[i + 1:]
        yield [[first]] + smaller


def moebius(pi):
    return math.prod((-1) ** (len(b) - 1) * math.factorial(len(b) - 1) for b in pi)


def no_singletons(k):
    return [p for p in set_partitions(list(range(k))) if all(len(b) >= 2 for b in p)]


def hom(pi, rho, F):
    """sum over labellings of prod over elements l of F[i(block_pi(l)), j(block_rho(l))]."""
    k = sum(len(b) for b in pi)
    row_of = {l: a for a, b in enumerate(pi) for l in b}
    col_of = {l: a for a, b in enumerate(rho) for l in b}
    # einsum: one operand per element l, indices (row letter, column letter)
    letters = "abcdefghijklmnop"
    subs = []
    for l in range(k):
        subs.append(letters[row_of[l]] + letters[len(pi) + col_of[l]])
    return float(np.einsum(",".join(subs) + "->", *([F] * k), optimize=True))


def matching_sum(F, k):
    return sum(np.linalg.det(np.eye(k)) * 0 + permanent(F[np.ix_(S, T)])
               for S in itertools.combinations(range(n), k)
               for T in itertools.combinations(range(n), k))


def permanent(A):
    m = A.shape[0]
    idx = np.arange(1 << m)
    S = np.zeros((1 << m, m))
    sizes = np.zeros(1 << m, dtype=np.int64)
    for b in range(m):
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    sign = np.where((m - sizes) % 2 == 0, 1.0, -1.0)
    return float((sign * np.prod(S, axis=1))[1:].sum())


def random_zero_margin(scale=0.5):
    X = rng.standard_normal((n, n))
    X -= X.mean(0, keepdims=True)
    X -= X.mean(1, keepdims=True)
    return scale * X


print("Part 1: Moebius expansion against direct matching sums, n = 7")
for k, samples in ((4, 3), (5, 3), (6, 1), (7, 1)):
    parts = no_singletons(k)
    worst = 0.0
    for _ in range(samples):
        F = random_zero_margin()
        total = 0.0
        for pi in parts:
            for rho in parts:
                total += moebius(pi) * moebius(rho) * hom(pi, rho, F)
        direct = matching_sum(F, k)
        worst = max(worst, abs(total / math.factorial(k) - direct) / max(1.0, abs(direct)))
    print(f"  k={k}: {len(parts)} no-singleton partitions, {len(parts)**2} diagrams, "
          f"max relative discrepancy {worst:.2e}")

print("\nPart 2: diagram-wise bound of |alpha_k| on the application regime at n = 7")
K0 = math.log((math.factorial(5) * (5.0 / 36.0) ** 5) / (math.factorial(7) / 7.0 ** 7))
Phi = 49 * 2 * n * K0          # ||F||^2 <= n^2 * 2 n K_0   (Theorem 2 of the capacity route)
c0sq = 49 * 2 * K0             # every row / column of F: squared norm <= n^2 * 2 K_0
m = 7 * math.sqrt(2 * K0)      # max |F_ij|
print(f"  K_0 = {K0:.5f}, Phi <= {Phi:.3f}, row/col squared norm <= {c0sq:.4f}, max|F| <= {m:.4f}")
for k in (4, 5, 6, 7):
    parts = no_singletons(k)
    total = 0.0
    total_fullfull = 0.0
    for pi in parts:
        for rho in parts:
            w = abs(moebius(pi) * moebius(rho))
            Vr, Vc = len(pi), len(rho)
            b1 = c0sq ** ((k - 2 * Vc) / 2) * Phi ** Vc
            b2 = c0sq ** ((k - 2 * Vr) / 2) * Phi ** Vr
            bound = min(b1, b2)
            if Vr == 1 and Vc == 1:
                bound = min(bound, Phi * m ** (k - 2))
                total_fullfull += w * bound
            total += w * bound
    coef = total / (math.factorial(k) * math.perm(n, k))          # bound on |alpha_k|
    per_E2 = coef / (Phi / 49)                                     # as a multiple of ||E||^2
    ff = total_fullfull / (math.factorial(k) * math.perm(n, k)) / (Phi / 49)
    print(f"  k={k}: |alpha_k| <= {coef:.4f} = {per_E2:.3f} ||E||^2   "
          f"(one-block/one-block diagram alone: {ff:.3f} ||E||^2; budget for k>=5 total: 0.17)")
