# Counterexamples to Dittert conjecture are near-decomposable, for n >= 8

**Form.** Reduction or equivalence. **Venue.** On the path of the application.

## 1. Statement

Let n >= 8 and let A in K_n have a zero entry and phi(A) >= 2 - gamma_n, that is, let A be a
counterexample to Dittert conjecture at n. Let B be its Sinkhorn scaling and K = -log cap(A).
Then K >= K_2(n) and lambda_2(B) <= 1 - sqrt(2 n K_2(n)), where K_2(n) is the second solution of
K = Psi_n(K) below (0.047 at n = 8, 0.048 at n = 9, 0.046 at n = 10, and lambda_2(B) <= 0.13 at
n = 8). In particular no counterexample whose scaling is an expander exists, and Dittert
conjecture at n >= 8 reduces to the near-decomposable case.

## 2. The ingredients

- (a) Margins: |u|^2 + |v|^2 <= 2 gamma_n kappa_n, from Lemma 3(a) of Theorem R, with u = 1 - r,
  v = 1 - c the margin deviations of A (attack/dittert-conjecture-n5-to-n15,
  study/route-a-reduction-theorem.md).
- (b) per(A) <= gamma_n, from the hypothesis and AM-GM on the products of the margins.
- (c) per(B) >= m_n = (n-2)!((n-2)/(n-1)^2)^(n-2), because B has a zero (Knopp-Sinkhorn); with
  per(A) = e^{-K} per(B) and (b), K >= log(m_n / gamma_n).
- (d) Unit 2 in exponential form: per(B) >= gamma_n exp(||E||^2 / (2n)) with E = B - J_n/n; with
  per(B) = e^K per(A) <= e^K gamma_n this gives ||E||_F^2 <= 2 n K, and since J_n/n annihilates
  the complement of the all-ones vector, lambda_2(B) = 1 - sigma_2(B) >= 1 - ||E||_F >= 1 - sqrt(2nK).
- (e) Lemma 2' (study/lemma2-prime.md): K <= rho(W_0) mu^2 / (lambda_2(B) chi(W_0)), with mu the
  margin norm, W_0 the least fixed point of W = sqrt(2) mu / (lambda_2(B) chi(W)),
  psi(w) = (e^{-w} - 1 + w)/w^2, chi(w) = (1 - e^{-w})/w, rho = psi / chi. Its proof rests on three
  exact identities for the log-scalings l and the potentials w_ij = l_1i + l_2j: K = sum b_ij
  w_ij^2 psi(w_ij), u_i = sum_j b_ij (1 - e^{-w_ij}), and l^T(u; v) = sum b_ij w_ij^2 chi(w_ij),
  together with l^T L_B l >= lambda_2(B) |l|^2 for l orthogonal to (1; -1).

## 3. The deduction

(d) and (e) give K <= Psi_n(K) := Phi_n(1 - sqrt(2nK)), with Phi_n(lambda) the right side of (e)
at mu^2 = 2 gamma_n kappa_n, which is decreasing in lambda; Psi_n is increasing in K, positive at
K = 0, and tends to infinity as K tends to 1/(2n). So the set of K with K <= Psi_n(K) is
[0, K_1(n)] together with [K_2(n), infinity), for the two crossings of the diagonal
(study/branch-structure.py). By (c), K >= log(m_n / gamma_n), and at every n >= 8 that exceeds
K_1(n) (0.0037 at n = 8 against 0.0098). So K >= K_2(n), and then (d) bounds lambda_2(B). QED

## 4. What it does not say, and the correction it records

The record briefly claimed that this deduction closes n >= 8. It does not: the large-cost branch
[K_2(n), infinity) satisfies every inequality above, and on it the scaling B is near-decomposable.
Excluding that branch needs a lower bound on the permanent of a near-decomposable doubly
stochastic matrix well above gamma_n, which is the barrier of unit 6 and of the previous attack.
What is proved is the structure theorem: the expander side is closed.

At n = 7 the same deduction excludes the small branch as soon as unit 2 holds with the constant
1/n in place of 1/(2n) (margin 1.227x, study/lemma2-prime-rho.py); with 1/(2n) it gives 0.83x and
excludes nothing.

## 5. Checks

Every inequality of Lemma 2' is checked on 1600 random near-doubly-stochastic matrices with a
zero, including scalings with gap down to 0.005 (study/lemma2-prime-identity.py); the statement
itself holds with room, 2 K lambda_2(B) / mu^2 <= 0.877 over 2400 cases (study/lemma2-prime.py).
The branch structure and the values of K_1, K_2 are in study/branch-structure.py, at 30 digits.

## 6. References

- Knopp and Sinkhorn 1982; Theorem R and its Lemma 3(a), in the sibling attack (unpublished).
- Unit 2 of this attack for (d).

## 7. Ledger

Bound quality: the constant 1/(2n) of unit 2 is what limits the small branch to n >= 8.
