# What this statement would give Dittert's conjecture

Written 2026-09-04. Arithmetic: `study/application.py`, which prints every number below.

## 1. The deduction

Let `A` be in `K_n` with a zero entry and `phi(A) >= 2 - gamma_n`, that is, a counterexample to
Dittert's conjecture at `n`. Let `B` be its Sinkhorn scaling and `K = -log cap(A)`, so
`per(A) = e^{-K} per(B)`. The sibling attack's record already gives four facts, with
`gamma_n = n!/n^n`, `m_n = (n-2)!((n-2)/(n-1)^2)^{n-2}`, `theta_n = 1 - 2 sqrt(2 gamma_n)/3` and
`kappa_n = 1/((1 - gamma_n) theta_n)`:

- (a) `|u|^2 + |v|^2 <= 2 gamma_n kappa_n`, the margins of `A` (Theorem R, Lemma 3(a));
- (b) `per(A) <= gamma_n`, from the hypothesis and AM-GM;
- (c) `per(B) >= m_n`, because `B` has a zero entry (Knopp-Sinkhorn);
- (d) `K <= (|u|^2 + |v|^2) / (2 theta_n lambda_2)`, given the non-negativity condition (N)
  (Theorem R, Lemma 2).

From (b) and (c), `K >= log(m_n / gamma_n)`: the scaling has to be **expensive**. Everything the
sibling attack tried was an attempt to show it is **cheap**, and every route needed a lower bound
on `lambda_2` that no argument supplied.

This claim supplies it, and does not go through the spectrum at all. From (b),
`per(B) = e^K per(A) <= e^K gamma_n`, so the claim gives

    ||B - J_n/n||_F^2 <= (e^K - 1) / c.

`B = J_n/n + E` with `E 1 = 0` and `E^T 1 = 0`, and `J_n/n` annihilates the orthogonal complement
of the all-ones vector, so the second singular value of `B` is at most `||E||_F` and

    lambda_2(B) >= 1 - sqrt((e^K - 1)/c).

Substituting into (d) gives a fixed-point inequality in `K` alone, whose least solution is an
upper bound on `K`. The case closes when that bound is below `log(m_n / gamma_n)`.

## 2. What it closes, at c = 1/4

| n | K upper bound | lambda_2 >= | log(m_n/gamma_n) | closes | margin | \|alpha+beta\| <= |
|---|---|---|---|---|---|---|
| 5 | no fixed point | | 2.95e-2 | no | | |
| 6 | 3.12e-2 | 0.6437 | 1.90e-2 | no | 0.61x | 0.4689 |
| 7 | 8.84e-3 | 0.8115 | 1.33e-2 | **yes** | 1.50x | 0.2170 |
| 8 | 2.97e-3 | 0.8909 | 9.82e-3 | **yes** | 3.30x | 0.1183 |
| 9 | 1.06e-3 | 0.9348 | 7.54e-3 | **yes** | 7.09x | 0.0685 |
| 10 | 3.92e-4 | 0.9604 | 5.98e-3 | **yes** | 15.3x | 0.0408 |
| 11 | 1.47e-4 | 0.9758 | 4.86e-3 | **yes** | 33.1x | 0.0247 |
| 12 | 5.53e-5 | 0.9851 | 4.02e-3 | **yes** | 72.8x | 0.0150 |
| 13 | 2.09e-5 | 0.9909 | 3.39e-3 | **yes** | 162x | 0.0092 |
| 14 | 7.93e-6 | 0.9944 | 2.89e-3 | **yes** | 365x | 0.0057 |
| 15 | 3.01e-6 | 0.9965 | 2.50e-3 | **yes** | 830x | 0.0035 |

`n = 5` and `n = 6` are already proved, by the exact sum-of-squares certificates of
`attack/dittert-conjecture-n5-to-n15`. `n >= 16` is Kafidov's inequality and `n >= 17` is Pang,
arXiv:2606.01531.

**Correction (2026-09-04, later the same day).** The sentence that stood here, that the claim
closes every open dimension, was wrong, and the table above measures less than it seems to. The
fixed-point inequality `K <= Psi(K)` has an increasing right side with `Psi(0) > 0` and a pole,
so its solution set is two branches, `[0, K_1]` and `[K_2, infinity)`
(`study/branch-structure.py`; at `n = 8`, `K_1 = 0.0037` and `K_2 = 0.047` against the needed
`0.0098`). The margins in the table are for the small-cost branch only. The large-cost branch is
the case where the Sinkhorn scaling `B` of the counterexample is near-decomposable
(`lambda_2(B) <= 1 - sqrt(2 n K_2)`, which is `0.13` at `n = 8`), and nothing in this deduction
excludes it: it is the barrier of `attack/spectral-gap-near-maximisers`, unit 5, unchanged. What
the claim gives, with any `c >= 1/n`, is the structure theorem that every counterexample at
`n >= 7` is near-decomposable in that quantitative sense; expander counterexamples cannot exist.

## 3. Condition (N) is free here, and that is the point

Condition (N) is what made the spectral route fail: it is binding by a factor of 12.1 at `n = 7`
rising to 6555 at `n = 20` (`attack/spectral-gap-near-maximisers`, unit 5), because the margins
have size `sqrt(delta)` and non-negativity costs a square root. It needs
`|alpha_i + beta_j| <= 1` for the competitor `B'_ij = a_ij (1 + alpha_i + beta_j)`, and Lemma 3(c)
bounds that by `sqrt(2) |(u; v)| / (theta_n lambda_2)`.

The last column of the table is that bound. At `n = 7` it is 0.2170, and it falls to 0.0035 at
`n = 15`. Condition (N) holds with room to spare at every dimension the route closes, because
`lambda_2` is now near 1 rather than near 0. The binding constraint of the whole previous attack
disappears.

## 4. How weak the constant may be

The sharp constant was measured as `c*(n) = 0.25, 0.333, 0.418, 0.461, 0.487, 0.497` at `n = 3`
to 8. The application needs far less:

| c | closes |
|---|---|
| 1/4 | n >= 7 |
| 0.1 | n >= 7 |
| 0.05 | n >= 8 |
| 0.02 | n >= 8 |
| 0.01 | n >= 9 |
| 1/n | n >= 7, every n from 7 to 15 |
| 1/n^2 | n >= 9 |
| 1/n^3 | n >= 12 |

So **`c(n) >= 1/n` is enough**, against a measured truth of at least `1/4`. A proof does not have
to find the sharp constant, and does not have to be tight anywhere.

## 5. The two steps a proof still owes

- **`lambda_2(A)` against `lambda_2(B)`.** Step (d) is stated for `A`, and the claim bounds
  `lambda_2(B)` for the scaling `B`. `A` and `B` have the same support and `A` has margins within
  `O(sqrt(gamma_n))` of 1, so the two differ by `O(sqrt(gamma_n))`, but that comparison is not
  written down here.
- **Selecting the least fixed point.** The substitution gives an inequality with two solution
  branches; the least one is the correct bound by a continuity argument in `delta`, which is not
  written down here either.

Both are routine and both are obligations, recorded as such.
