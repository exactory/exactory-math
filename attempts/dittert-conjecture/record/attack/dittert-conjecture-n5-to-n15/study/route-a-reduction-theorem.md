# Route A: reduction of Dittert's conjecture at n to a spectral-gap statement

Written 2026-09-03 under move 9 (ladder-the-parameter, entry
choose-the-auxiliary-weight-or-certificate). Every step below is proved here or
cited; the one unproved input is stated as Hypothesis G(n, c) and is what the
theorem is conditional on.

## Notation and the facts used

n >= 4. For A in K_n write r_i, c_j for its row and column sums, R = prod r_i = 1 - rho,
C = prod c_j = 1 - sigma, gamma_n = n!/n^n, m_n = (n-2)! ((n-2)/(n-1)^2)^{n-2},
u_i = 1 - r_i, v_j = 1 - c_j (so sum u = sum v = 0), and h_n = sqrt(2 gamma_n).

- (F1) If phi(A) >= 2 - gamma_n then, with delta := gamma_n - per(A):
  0 <= delta <= gamma_n and rho + sigma <= delta. [AM-GM gives R, C <= 1; then
  R + C - per(A) >= 2 - gamma_n reads delta >= rho + sigma; delta <= gamma_n since
  per(A) >= 0; delta >= 0 since R + C <= 2.]
- (F2) If phi(A) >= phi(J_n/n) then every row sum and column sum of A lies in
  [1 - sqrt(2 delta), 1 + sqrt(2 delta)], hence in [1 - h_n, 1 + h_n].
  [Cheon-Wanless 2012, Thm 2.1 with k = 1.]
- (F3) If phi(A) >= phi(J_n/n) then A is fully indecomposable. [Cheon-Wanless 2012,
  Thm 3.2: a partly decomposable matrix has phi < phi(J_n/n).]
- (F4) A fully indecomposable nonnegative matrix has a Sinkhorn scaling: x, y > 0 with
  B = D_x A D_y doubly stochastic. [Sinkhorn-Knopp 1967.]
- (F5) If B in Omega_n has a zero entry and n > 3 then per(B) >= m_n. [Knopp-Sinkhorn
  1982, as used in arXiv:2606.01531 Lemma 1 and arXiv:2607.19439 Prop 2.1(iv).]
- (F6) A positive maximiser of phi on K_n is J_n/n. [Hwang 1986.]

## Lemma 1 (capacity lower bound from any doubly stochastic competitor)

Let A >= 0 be n x n with a Sinkhorn scaling B = D_x A D_y in Omega_n, and let
cap(A) := inf_{z > 0} prod_i (Az)_i / prod_j z_j. Then

  (i)  per(A) = per(B) cap(A);
  (ii) for every B' in Omega_n with supp B' contained in supp A,
       cap(A) >= exp( sum_{ij} b'_ij log(a_ij / b'_ij) ).

Proof. (i) per(B) = prod x prod y per(A), so it suffices to show cap(A) = 1/(prod x prod y).
For any doubly stochastic B, cap(B) = 1: AM-GM gives (Bz)_i >= prod_j z_j^{b_ij}, so
prod_i (Bz)_i >= prod_j z_j^{sum_i b_ij} = prod_j z_j, with equality at z = 1. And
cap(D_x A D_y) = prod x prod y cap(A): substituting w = D_y z, prod_i (D_x A D_y z)_i /
prod_j z_j = prod x prod y prod_i (Aw)_i / prod_j w_j. Hence 1 = cap(B) =
prod x prod y cap(A).
(ii) Fix z > 0. For each i, log (Az)_i = log sum_j a_ij z_j >= sum_j b'_ij log(a_ij z_j / b'_ij)
by Jensen's inequality for the concave logarithm with the weights b'_ij (which sum to 1
over j; terms with b'_ij = 0 are omitted, and a_ij > 0 wherever b'_ij > 0). Summing over
i and using sum_i b'_ij = 1: log prod_i (Az)_i >= sum_ij b'_ij log(a_ij/b'_ij) + sum_j log z_j.
Taking the infimum over z gives (ii). QED

Remark. The published dilation argument is (ii) with any B' <= (1-t)^{-1} A, which
only gives a_ij/b'_ij >= 1 - t entrywise and hence cap(A) >= (1-t)^n.

## Lemma 2 (the chi-square competitor)

Let A in K_n satisfy phi(A) >= 2 - gamma_n, and let L be the symmetric 2n x 2n matrix
[[D_r, A], [A^T, D_c]]. Then (alpha; beta)^T L (alpha; beta) = sum_ij a_ij (alpha_i + beta_j)^2,
so L is positive semidefinite, and by (F3) its kernel is exactly span{(1; -1)} (the
bipartite graph of supp A is connected, so a_ij (alpha_i + beta_j) = 0 for all ij forces
alpha_i = -beta_j constant). Since sum u = sum v, (u; v) is orthogonal to (1; -1), and the
system L (alpha; beta) = (u; v) has a unique solution orthogonal to (1; -1). Put

    e_ij = a_ij (alpha_i + beta_j),   B' = A + E.

Then: row sums of E are r_i alpha_i + (A beta)_i = u_i and column sums are v_j, so B' has
all row and column sums 1; supp B' is contained in supp A; and B' >= 0 as soon as

    (N)   |alpha_i + beta_j| <= 1 for all i, j.

Under (N), B' in Omega_n and Lemma 1(ii) gives, with tau_ij = alpha_i + beta_j and
log(1 + tau) <= tau,

    log cap(A) >= - sum_ij b'_ij log(1 + tau_ij) >= - sum_ij b'_ij tau_ij
               = - sum_i alpha_i - sum_j beta_j.

Summing the first n equations of the system: sum_i r_i alpha_i + sum_j c_j beta_j = sum_i u_i = 0,
hence sum_i alpha_i + sum_j beta_j = sum_i u_i alpha_i + sum_j v_j beta_j = (u; v)^T (alpha; beta)
= (alpha; beta)^T L (alpha; beta) =: Phi(A) >= 0. Therefore

    (1)   cap(A) >= exp(-Phi(A)),   Phi(A) = (u; v)^T L^+ (u; v),

whenever (N) holds. QED

## Lemma 3 (sizes)

Let A be as in Lemma 2 and let M = D_r^{-1/2} A D_c^{-1/2}, sigma_2(M) its second singular
value, lambda_2(A) := 1 - sigma_2(M), theta_n := 1 - h_n, and

    kappa_n := 1 / ( (1 - gamma_n) (1 - 2 h_n / 3) ).

Then (a) |u|^2 + |v|^2 <= 2 delta kappa_n;
(b) Phi(A) <= (|u|^2 + |v|^2) / (theta_n lambda_2(A));
(c) |alpha|_inf + |beta|_inf <= sqrt(2) sqrt(|u|^2 + |v|^2) / (theta_n lambda_2(A)).

Proof. (a) With x_i = r_i - 1 (so sum x_i = 0 and |x_i| <= h_n by (F2)) and the
inequality log(1 + x) <= x - x^2/2 + x^3/3 for x > -1: -rho' := log R = sum log(1 + x_i)
<= -|u|^2/2 + sum x_i^3/3 <= -|u|^2/2 + (h_n/3)|u|^2, so |u|^2 <= 2 rho' / (1 - 2h_n/3),
where rho' = -log(1 - rho) <= rho/(1 - rho) <= rho/(1 - gamma_n) by (F1). Likewise for v
with sigma. Adding and using rho + sigma <= delta gives (a).
(b), (c) Write S = diag(D_r^{1/2}, D_c^{1/2}), so L = S L~ S with L~ = [[I, M], [M^T, I]].
The eigenvalues of L~ are 1 +- sigma_k(M); sigma_1(M) = 1 with singular vectors
(r^{1/2}, c^{1/2}) (since M c^{1/2} = D_r^{-1/2} A 1 = r^{1/2}), so ker L~ = span S(1; -1)
and the smallest nonzero eigenvalue of L~ is 1 - sigma_2(M) = lambda_2(A). Now
(alpha; beta) = S^{-1} L~^+ S^{-1} (u; v), and S^{-1}(u; v) is orthogonal to ker L~
(its inner product with (r^{1/2}; -c^{1/2}) is sum u - sum v = 0). Hence
Phi = (S^{-1}(u;v))^T L~^+ (S^{-1}(u;v)) <= |S^{-1}(u;v)|^2 / lambda_2 <= (|u|^2+|v|^2)/(theta_n lambda_2)
since every r_i, c_j >= theta_n by (F2); and |(alpha; beta)| <= |S^{-1}|^2 |L~^+| |(u; v)|
<= (|u|^2+|v|^2)^{1/2} / (theta_n lambda_2), whence (c) with |alpha|_inf + |beta|_inf <= sqrt(2) |(alpha; beta)|. QED

## Theorem R (the reduction)

Hypothesis G(n, c): every A in K_n with phi(A) >= 2 - gamma_n and at least one zero
entry satisfies lambda_2(A) >= c.

Put c_n := 2 sqrt(gamma_n kappa_n) / theta_n. If G(n, c) holds for some c >= c_n, then
Dittert's conjecture holds at n: phi(A) <= 2 - gamma_n for all A in K_n, with equality
only at J_n/n.

Proof. phi is continuous on the compact K_n, so a maximiser A exists, and
phi(A) >= phi(J_n/n) = 2 - gamma_n. If A is positive, A = J_n/n by (F6) and we are done.
Suppose A has a zero entry and write per(A) = gamma_n - delta, so 0 <= delta <= gamma_n by
(F1). If delta = 0 then R = C = 1, A is doubly stochastic with a zero, and per(A) >= m_n > gamma_n
by (F5), a contradiction; so delta > 0. By (F3), (F4) and (F5), Lemma 1(i) gives
per(A) >= m_n cap(A). By Lemma 3(a),(c) and G(n, c) with c >= c_n:
|alpha|_inf + |beta|_inf <= sqrt(2) sqrt(2 delta kappa_n) / (theta_n c) <= 2 sqrt(gamma_n kappa_n)/(theta_n c) <= 1,
so (N) holds and Lemma 2 and Lemma 3(b) give cap(A) >= exp(-2 delta kappa_n/(theta_n c)).
Hence, using exp(-x) >= 1 - x,

    gamma_n - delta = per(A) >= m_n (1 - 2 delta kappa_n/(theta_n c)),

i.e. m_n - gamma_n <= delta (2 m_n kappa_n/(theta_n c) - 1). The right side is <= 0
because 2 m_n kappa_n/(theta_n c) <= 2 m_n kappa_n/(theta_n c_n) = m_n sqrt(kappa_n)/sqrt(gamma_n) < 1
(for n >= 4, m_n <= 1.06 gamma_n and gamma_n kappa_n < 0.15), while the left side is
m_n - gamma_n > 0: a contradiction. So no maximiser has a zero entry, and the
conclusion follows from (F6). QED

## The numbers

| n | gamma_n | h_n | kappa_n | theta_n | c_n = 2 sqrt(gamma_n kappa_n)/theta_n |
|---|---|---|---|---|---|
| 4 | 0.09375 | 0.4330 | 1.552 | 0.567 | 1.346 |
| 5 | 0.03840 | 0.2771 | 1.276 | 0.723 | 0.612 |
| 6 | 0.01543 | 0.1757 | 1.150 | 0.824 | 0.323 |
| 7 | 0.006120 | 0.1106 | 1.086 | 0.889 | 0.183 |
| 8 | 0.002403 | 0.06933 | 1.050 | 0.931 | 0.108 |
| 9 | 0.0009367 | 0.04328 | 1.030 | 0.957 | 0.0649 |
| 10 | 0.0003629 | 0.02694 | 1.018 | 0.973 | 0.0395 |
| 11 | 0.0001399 | 0.01673 | 1.011 | 0.983 | 0.0242 |
| 12 | 5.372e-5 | 0.01037 | 1.007 | 0.990 | 0.0149 |
| 13 | 2.056e-5 | 0.006413 | 1.004 | 0.994 | 0.00913 |
| 14 | 7.845e-6 | 0.003961 | 1.003 | 0.996 | 0.00563 |
| 15 | 2.986e-6 | 0.002444 | 1.002 | 0.998 | 0.00347 |

(Values to three or four figures; the exact rational c_n is what a certified check
would carry.) At n = 4 the constant exceeds 1 and G(4, c) cannot hold with the
normalisation lambda_2 <= 1; the theorem is vacuous there, and n = 4, 5, 6 are settled
by other means anyway. For 7 <= n <= 15 the required gap is 0.18 down to 0.0035.

## What is proved and what is not

Proved above: Theorem R, with all constants explicit and every input cited.
Not proved: G(n, c_n) for any n. Evidence (study/per-vs-gap-numerics.py, 1200 doubly
stochastic samples with a zero at n = 5, 8, 12): every sample with per(B) <= 1.05 gamma_n
had lambda_2(B) >= 0.71, 0.78, 0.86 respectively, against the required 0.61, 0.108,
0.0149; every sample with lambda_2 <= 0.3 had per(B) >= 1.6 gamma_n. The lemma that
would close the route is therefore a stability statement for the van der Waerden
inequality of a weak, explicit kind: a doubly stochastic (or near-doubly-stochastic)
matrix with a zero entry and permanent within a factor 1 + O(1/n^2) of n!/n^n has
second singular value at most 1 - c_n.
