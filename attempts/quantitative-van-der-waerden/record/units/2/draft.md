# The quantitative van der Waerden inequality with constant 1/(2n)

**Form.** Quantitative improvement. **Venue.** On the path: it is the claim with a weaker constant.

## 1. Statement

For every n >= 2 and every doubly stochastic n by n real matrix B, with E = B - J_n/n and
d_j = ||col_j(B) - 1/n||^2,

    per(B) >= gamma_n exp( max_j d_j / 2 ) >= gamma_n exp( ||E||_F^2 / (2n) )
           >= gamma_n ( 1 + ||E||_F^2 / (2n) ).

## 2. Proof

Unit 1 gives per(B) >= gamma_{n-1} K(v) for the column v = col_j(B).

**Lemma C.** For every probability vector v in R^n, K(v) >= g(n) exp(||v - 1/n||^2 / 2), with
g(n) = ((n-1)/n)^(n-1).

Let phi(t) = (1 - t) log(1 - t) on [0, 1), phi(1) = 0. Then phi is C^2 on [0, 1) with
phi(t) = 1/(1 - t) >= 1 (second derivative). Taylor with integral remainder at t_0 = 1/n gives
phi(t) >= phi(t_0) + phi(t_0)(t - t_0) + (t - t_0)^2 / 2 for t in [0, 1) (first derivative in the
middle term), and by continuity at t = 1. Summing over the coordinates of v, the linear terms
cancel because sum (v_s - 1/n) = 0, and n phi(1/n) = (n-1) log((n-1)/n) = log g(n). Exponentiate:
K(v) = exp(sum phi(v_s)). QED

So per(B) >= gamma_{n-1} g(n) exp(d_j / 2) = gamma_n exp(d_j / 2) for every j, and
||E||_F^2 = sum_j d_j <= n max_j d_j. Finally e^t >= 1 + t. QED

## 3. What it is worth

The claim asks for 1/4 and the truth is c*(n) >= 1/4 rising to 1/2 (unit 4); the constant
proved here is 1/(2n), a factor about n/2 short. It is the first deficiency term for the van der
Waerden inequality in the record or in print. Its single-column origin is also its ceiling: unit
1 is an equality at sparse uniform columns for every completion, so the constant cannot be pushed
past about 0.6/n by any bound of the form gamma_{n-1} F(column) (route-capacity.md, section 5).

For the Dittert application the exponential form is the useful one: per(B) <= e^K gamma_n for
the scaling of a counterexample gives ||E||_F^2 <= 2 n K directly (unit 5).

## 4. Checks

study/verify-capacity-claim.py: minimum ratio per(B) / (gamma_n exp(||E||^2/(2n))) exactly
1.0000000000 at n = 2 to 7 over about 500 matrices per n, equality at J_n/n. Lemma C is checked at
20000 random probability vectors, n = 2 to 11, in route-capacity.md (minimum ratio 1.0000000086).

## 5. References

As in unit 1, plus Egorychev, Adv. Math. 42 (1981) 299-305 and Falikman, Mat. Zametki 29 (1981)
931-938 for the inequality itself.

## 6. Ledger

Bound quality: 1/(2n) against the needed 1/n and the true 1/4.
