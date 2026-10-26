# Working notes for route A (the analytic residue), 2026-09-03

Not a strategy study record; a note kept in the workspace so the reasoning behind
move 1's route A survives the session. Everything below is unproved unless a
reference is given.

## The published chain in capacity terms

For A in K_n fully indecomposable, Sinkhorn scaling gives B = D1 A D2 in Omega_n and
per(A) = per(B) / (prod D1 prod D2). At the Sinkhorn scaling, 1/(prod D1 prod D2)
equals the capacity cap(A) = inf_{x > 0} prod_i (Ax)_i / prod_j x_j (the infimum is
attained at x = diag(D2), where (Ax)_i = 1/(D1)_i). If A has a zero entry so does B,
so per(B) >= m_n (Knopp-Sinkhorn) and

    per(A) >= cap(A) m_n.                                                   (1)

Pang and Kafidov prove cap(A) >= (1 - t)^n with t = sqrt(n delta / (1 - delta)):
(1 - t)^{-1} A is doubly superstochastic, so its capacity is >= 1 (it dominates a
doubly stochastic matrix, and cap is monotone), and cap is homogeneous of degree n.
The final comparison m_n (1 - t)^n > gamma_n - delta then needs
m_n - gamma_n > n^3 m_n^2 / (4 (1 - gamma_n)), true iff n >= 16.

The two losses are (i) the uniform dilation, which multiplies every row by the
factor needed for the worst Hall pair, and (ii) cap(S) >= 1 for the dilated matrix
S, whereas cap(S) <= prod_i r_i(S) = (1 - t)^{-n} (1 - rho) and is typically close
to that upper bound. Removing (ii) alone would remove the whole factor (1 - t)^n.

## The entropy dual of the capacity

For a nonnegative matrix A with positive permanent (Gurvits; Linial-Samorodnitsky-
Wigderson), cap(A) = max over B in Omega_n of prod_{ij} (a_ij / b_ij)^{b_ij}, the
maximiser being the Sinkhorn scaling of A. (To be cited precisely before use:
this is the standard "capacity equals max-entropy" duality; reference to be
fixed at the study of the strategy that dispatches it.) Hence for ANY doubly
stochastic B with supp B contained in supp A,

    log cap(A) >= sum_{ij} b_ij log(a_ij / b_ij) >= - sum_{ij} (b_ij^2 / a_ij - b_ij)
               = -( sum_{ij} b_ij^2 / a_ij - n ),                              (2)

using log x >= 1 - 1/x. So a lower bound on cap(A) follows from one explicit
doubly stochastic B close to A in the chi-square sense. Kafidov's bound is (2)
with B <= (1 - t)^{-1} A, which only gives a_ij / b_ij >= 1 - t entrywise.

## The correction B = A + E

Write u_i = 1 - r_i, v_j = 1 - c_j (sum u = sum v = 0). A doubly stochastic B = A + E
needs E 1 = u, E^T 1 = v, B >= 0. The chi-square cost sum e_ij^2 / a_ij is a weighted
least-squares problem whose minimiser is e_ij = a_ij (alpha_i + beta_j) with
(alpha, beta) solving r_i alpha_i + (A beta)_i = u_i, (A^T alpha)_j + c_j beta_j = v_j;
the cost is <alpha, u> + <beta, v>. This is a quadratic form in (u, v) through the
pseudo-inverse of the bipartite weighted Laplacian of A, so

    cost <= (|u|^2 + |v|^2) / lambda_2(A),                                    (3)

with lambda_2 the spectral gap of the normalised bipartite Laplacian (1 minus the
second singular value of D_r^{-1/2} A D_c^{-1/2}). From log R = sum log r_i <=
-sum (r_i - 1)^2 / 2 + O(eps^3) (since sum (r_i - 1) = 0): |u|^2 <= 2 rho'(1 + o(1)),
rho' = -log(1 - rho), and likewise |v|^2 <= 2 sigma'. With rho + sigma <= delta:

    cap(A) >= exp(-(2 delta + o(delta)) / lambda_2(A)).                       (4)

If lambda_2(A) >= c for every near-maximiser, then (1) and (4) give
per(A) >= m_n exp(-2 delta / c), and m_n exp(-2 delta / c) > gamma_n - delta holds
for every delta in (0, gamma_n] as soon as (2/c) m_n < 1 - (m_n - gamma_n)/gamma_n,
i.e. for every n >= 4 with c = 1/2 (m_4 = 0.0988). The whole residue would then be
one rational inequality per n, kernel-checkable in Lean.

Caveats. B = A + E must be nonnegative: E is supported on supp A and
|e_ij| <= a_ij |alpha_i + beta_j|, so B >= 0 needs |alpha_i + beta_j| <= 1, a
consequence of (3) with room when delta is small. Where a_ij = 0, e_ij = 0.

## The missing lemma

A near-maximiser has per(A) <= gamma_n. The needed input is a lower bound on the
spectral gap lambda_2(A) (equivalently an upper bound on the second singular value
of the normalised matrix) from per(A) <= gamma_n(1 + eta) and near-double-
stochasticity. Heuristic: a small spectral gap gives a sparse cut (Cheeger), a
sparse cut makes A nearly block-diagonal, and a nearly block-diagonal near-doubly-
stochastic matrix has per >= about gamma_k gamma_{n-k} = gamma_n sqrt(2 pi k(n-k)/n)
(1 - o(1)), far above gamma_n. Making this quantitative with explicit constants per
n is the research content of route A; no stability theorem of this kind for the
van der Waerden inequality was found (arXiv query
`"van der Waerden" AND permanent AND (stability OR "spectral gap" OR capacity)`,
2026-09-03: one unrelated hit, Gurvits-Leake 1804.04351).

## What to compute first

1. For the numerical near-maximisers on the face a_11 = 0 (numerical-optimisation-
   run-1), compute cap(A), lambda_2(A), and the ratio per(A) / (cap(A) m_n): this
   measures how much of the loss is in (i)+(ii) and whether (4) is tight.
2. The exact Kafidov residue at n = 15 with (2) replaced by the best B: if the
   worst case over the numerical optimisers already satisfies the inequality with
   margin, the lemma above is the target; if not, route A needs more.

## Numerical results (2026-09-03, evidence only)

`capacity-numerics.py 5 8 15` (random near-doubly-stochastic A with a_11 = 0, row
and column sums perturbed by 1e-3 or 1e-2): -log cap(A) / (rho' + sigma') lies in
[0.67, 1.18] in all 18 samples, while Kafidov's loss n log(1/(1-t)) is 400 to 17000
times rho' + sigma'; the chi-square bound (|u|^2 + |v|^2)/lambda_2 is above -log cap
in every sample, by a factor 2.4 to 28 (large only when lambda_2 is small).

`per-vs-gap-numerics.py 5 8 12` (400 doubly stochastic samples with b_11 = 0 per n,
including planted near-block structure): among samples with per(B) <= 1.05 gamma_n
the smallest lambda_2 is 0.71 (n = 5), 0.78 (n = 8), 0.86 (n = 12); among samples
with lambda_2 <= 0.3 the smallest per(B)/gamma_n is 1.62, 1.70, 2.08. So the
missing lemma ("per(B) <= (1 + eta) gamma_n forces lambda_2(B) >= c") is
numerically true with c around 0.5 for eta = 0.05, and with c = 0.5 the bound (4)
gives cap(A) >= exp(-4 delta), enough for every n >= 4.
