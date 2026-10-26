# Dittert's conjecture follows from a spectral gap of near-maximisers

## Statement

Let n >= 4, gamma_n = n!/n^n, h_n = sqrt(2 gamma_n), theta_n = 1 - h_n,
kappa_n = 1/((1 - gamma_n)(1 - 2h_n/3)) and c_n = 2 sqrt(gamma_n kappa_n)/theta_n. For A in K_n
(nonnegative, entry sum n) with row sums r and column sums c, put
lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2}), one minus the second singular value of the
normalised matrix.

**Hypothesis G(n, c).** Every A in K_n with phi(A) >= 2 - gamma_n and at least one zero entry
satisfies lambda_2(A) >= c.

**Theorem R.** If G(n, c) holds for some c >= c_n, then phi(A) <= 2 - gamma_n for every A in K_n,
with equality only at J_n/n.

The constants: c_7 = 0.183, c_8 = 0.108, c_9 = 0.0649, c_10 = 0.0395, c_11 = 0.0242,
c_12 = 0.0149, c_13 = 0.00913, c_14 = 0.00563, c_15 = 0.00347 (c_5 = 0.612, c_6 = 0.323; at
n = 4, c_4 = 1.35 > 1 and the theorem is vacuous). The full proof, with every input cited, is
`study/route-a-reduction-theorem.md`; this draft states it and the deduction.

## The hypothesis and what it is credible on

G(n, c_n) is a quantitative form of "no maximiser has a zero entry" (the statement whose
proof for n >= 16 is the content of arXiv:2606.01531 and arXiv:2607.19439). It asks that a
near-maximiser with a zero, which is nearly doubly stochastic (Cheon-Wanless 2012, Thm 2.1),
not be nearly reducible. Numerically (`deterministic/numerical-optimisation-run-4`, unit 5):
minimising lambda_2 over doubly stochastic matrices with a zero and per <= 1.05 gamma_n gives
0.697, 0.696, 0.726, 0.733 at n = 5, 6, 7, 8, against c_n = 0.612, 0.323, 0.183, 0.108; in 1200
random samples, per <= 1.05 gamma_n forced lambda_2 >= 0.71, 0.78, 0.86 at n = 5, 8, 12. The
required gap decreases like sqrt(gamma_n), so the hypothesis weakens rapidly with n.

## The proof in outline

1. A maximiser A exists; if positive it is J_n/n (Hwang, Linear Algebra Appl. 76 (1986),
   doi:10.1016/0024-3795(86)90212-0). Otherwise A has a zero, phi(A) >= 2 - gamma_n, and with
   delta = gamma_n - per(A): 0 < delta <= gamma_n and rho + sigma <= delta for the row- and
   column-product deficits (AM-GM); A is fully indecomposable (Cheon-Wanless, Linear Algebra
   Appl. 436 (2012), doi:10.1016/j.laa.2010.08.041, Thm 3.2); its Sinkhorn scaling B is doubly
   stochastic with a zero, so per(B) >= m_n = (n-2)!((n-2)/(n-1)^2)^{n-2} (Knopp-Sinkhorn,
   Linear Multilinear Algebra 11 (1982), doi:10.1080/03081088208817459).
2. Lemma 1: per(A) = per(B) cap(A), and cap(A) >= exp(sum b'_ij log(a_ij/b'_ij)) for every
   doubly stochastic B' supported in supp A (Jensen). The published proofs use B' <= (1-t)^{-1} A
   and get cap(A) >= (1-t)^n, t = sqrt(n delta/(1 - delta)), which loses the factor n^{1.5}
   sqrt(delta) and stops at n = 16.
3. Lemma 2: B' = A + E with e_ij = a_ij(alpha_i + beta_j), (alpha, beta) solving the weighted
   bipartite Laplacian system for the margins u = 1 - r, v = 1 - c, is doubly stochastic and
   supported in supp A, and cap(A) >= exp(-Phi(A)) with Phi(A) = (u; v)^T L^+ (u; v), provided
   |alpha_i + beta_j| <= 1.
4. Lemma 3: |u|^2 + |v|^2 <= 2 delta kappa_n (from log(1 + x) <= x - x^2/2 + x^3/3 and Thm 2.1
   with k = 1), Phi(A) <= (|u|^2 + |v|^2)/(theta_n lambda_2(A)), and the nonnegativity condition
   holds when lambda_2(A) >= c_n.
5. Hence per(A) >= m_n exp(-2 delta kappa_n/(theta_n c)) and, with exp(-x) >= 1 - x,
   m_n - gamma_n <= delta (2 m_n kappa_n/(theta_n c) - 1) < 0 for c >= c_n, a contradiction.

## What the bootstrap still needs

A proof of G(n, c_n) for 7 <= n <= 15: a stability statement for the van der Waerden
inequality of explicit, weak strength (the required gap is 0.0035 at n = 15). Nothing of
this kind was found in print (novelty.md). With it, Theorem R closes the eleven open
dimensions at once (n = 5, 6 are closed independently by units 1 and 2).
