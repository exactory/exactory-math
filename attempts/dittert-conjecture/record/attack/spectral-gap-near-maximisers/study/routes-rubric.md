# Ten routes to G(n, c_n), scored and ranked

Written 2026-09-03, move 1 of the attack. The claim is `problem.json`'s: every `A` in `K_n`
with `phi(A) >= 2 - gamma_n` and a zero entry has `lambda_2(A) >= c_n ~ 2 sqrt(gamma_n)`.

## Standing facts (used by every route, each cited)

Write `gamma_n = n!/n^n`, `m_n = (n-2)!((n-2)/(n-1)^2)^(n-2)`, `delta = gamma_n - per(A)`,
`u = 1 - r`, `v = 1 - c` the margin deficits, `cap(A) = inf_{z>0} prod_i (Az)_i / prod_j z_j`.

* (F1) `0 < delta <= gamma_n` and `rho + sigma <= delta` (AM-GM on the hypothesis).
* (F2) every row and column sum is within `sqrt(2 delta) <= sqrt(2 gamma_n)` of 1
  (Cheon-Wanless 2012, Thm 2.1, k = 1).
* (F3) `A` is fully indecomposable (Cheon-Wanless 2012, Thm 3.2), so it has a Sinkhorn
  scaling `B = D_1 A D_2` in `Omega_n`, and `per(A) = cap(A) per(B)`.
* (F4) `B` inherits the zero, so `per(B) >= m_n` (Knopp-Sinkhorn 1982).
* (F5) `per(B) >= gamma_n` with equality only at `J_n/n` (Egorychev, Falikman 1981).

**The single scalar the whole problem reduces to.** (F3) and (F4) give
`gamma_n - delta = per(A) = cap(A) per(B) >= cap(A) m_n`, so

    -log cap(A) >= log( m_n / (gamma_n - delta) ) >= log(m_n/gamma_n) ~ 1/(2(n-1)^2).   (LOW)

Every published proof, and Theorem R, is an upper bound on the same quantity:

    -log cap(A) <= U(delta, n).                                                          (UP)

The conjecture at `n` holds as soon as `U(delta, n) < log(m_n/(gamma_n - delta))` for every
`delta` in `(0, gamma_n]`. The known upper bounds are
`U = -n log(1 - sqrt(3 n delta))` (Pang, closes `n >= 17`),
`U = -n log(1 - sqrt(n delta/(1-delta)))` (Kafidov, closes `n = 16`), and
`U = 2 delta kappa_n / (theta_n lambda_2(A))` (Theorem R, closes every `n` given `G`).
**So G is not a weaker statement than the conjecture: by Theorem R the two are equivalent.
Its value is that it changes what has to be estimated, and the constant it needs is smaller
than the truth by a factor of about `0.7 / (2 sqrt(gamma_n))`, which is `4` at `n = 7` and
`200` at `n = 15`. A route may be crude and still finish.**

## The rubric

Each route is scored 0-5 on six axes. `C` and `K` are the gates: a route with `K <= 1`
cannot finish at the open dimensions however elegant it is.

| axis | question | weight |
|---|---|---|
| C | Is every step either a citable theorem or one whose proof is in sight? | 3 |
| K | Do the estimated constants clear `c_n` at the open `n` (7 to 15)? | 4 |
| T | Are the tools citable as they stand, or must new theory be built? | 2 |
| F | Can the key lemma be refuted numerically before the work is invested? | 1 |
| N | Does it settle all `n` at once, or one `n` at a time? | 2 |
| L | Does it end in something a proof assistant can check by kernel reduction? | 1 |

Maximum 65.

## The ten routes

### R1. Cheeger, then block factorisation of the permanent
`sigma_2` near 1 gives, by the bipartite Cheeger inequality, a cut `(S, T)` of conductance
`h <= sqrt(2 lambda_2)`; the cut is balanced (`|S| ~ |T| = k`) because the row and column
sums are near 1; `A` is then near block diagonal, and
`per(A) >= (1-eps)^n gamma_k gamma_{n-k}` with `eps ~ 2k h` the cut mass, while
`gamma_k gamma_{n-k} / gamma_n >= (n/(n-1))^{n-1} > e` for every `1 <= k <= n-1`.
The contradiction needs `eps < log(e/1)/n ~ 1/n`, that is `lambda_2 > 1/(2 n^4)`.
**Computed threshold:** `1/(2n^4) <= c_n = 2 sqrt(gamma_n kappa_n)/theta_n` fails for every
`n <= 34` and holds from about `n = 35`; the route is quantitatively empty on the open range.
C 4, K 1, T 5, F 4, N 4, L 5 → **12 + 4 + 10 + 4 + 8 + 5 = 43**.

### R2. Dirichlet energy with a weighted-path bound
`lambda_2 = min` of `sum_ij a_ij (x_i - y_j)^2` over normalised `(x, y)` orthogonal to the
stationary pair, so `|x_i - y_j| <= sqrt(lambda_2 / a_ij)` on every edge. Along a path of
length `L` through edges of weight at least `w`, the variation is at most `2L sqrt(lambda_2/w)`,
and the normalisation forces a variation of order 1 somewhere, giving
`lambda_2 >= w / (4 L^2)`. Needs a positive lower bound `w` on the nonzero entries of a
near-maximiser and a bound `L` on the diameter of its support; neither is in print, and a
near-maximiser may have entries as small as it likes.
C 3, K 2, T 4, F 5, N 4, L 4 → **9 + 8 + 8 + 5 + 8 + 4 = 42**.

### R3. Quantitative van der Waerden through the capacity proof
Gurvits's capacity proof of `per(B) >= gamma_n` is a chain of one-variable inequalities on
real stable polynomials whose equality cases are known exactly. Making each step
quantitative gives `per(B) <= (1 + eta) gamma_n` implies `B` close to `J_n/n`, and
`sigma_2(B) <= ||B - J_n/n||` then follows. The needed conclusion is very weak
(`sigma_2` bounded away from 1, not close to 0), so a lossy stability version suffices.
C 3, K 4, T 3, F 4, N 5, L 3 → **9 + 16 + 6 + 4 + 10 + 3 = 48**.

### R4. Stability of the Alexandrov-Fenchel equality cases
Egorychev's proof runs through Alexandrov-Fenchel; the equality cases of AF were
characterised by Shenfeld and van Handel (2020-2023) and their work carries quantitative
statements. If a stability form transfers to the permanent it gives exactly the missing
input, in the strongest available form.
C 2, K 4, T 2, F 2, N 5, L 2 → **6 + 16 + 4 + 2 + 10 + 2 = 40**.

### R5. Lorentzian polynomials and local Alexandrov-Fenchel
The permanent is the mixed derivative of a Lorentzian polynomial; Branden-Huh give
log-concavity with equality conditions, and local AF gives a rank-one deficiency statement
that quantifies "near equality". Same target as R4 through a lighter machine.
C 2, K 4, T 3, F 2, N 5, L 2 → **6 + 16 + 6 + 2 + 10 + 2 = 42**.

### R6. Split `K_n` by distance from `U_n`
Near `U_n` a Taylor expansion with Hwang's strict local maximum settles the claim; far from
`U_n` a crude bound suffices. The split radius must exceed `1/n`, the distance from `U_n` to
the face `a_ij = 0`, so no zero-entry matrix survives. The near part is a Hessian estimate;
the far part is where the difficulty moves.
C 3, K 3, T 4, F 5, N 4, L 4 → **9 + 12 + 8 + 5 + 8 + 4 = 46**.

### R7. One-entry variation (Hwang's method, quantified)
`per` is linear in each entry, so `per(A + t E_ij) = per(A) + t per(A(i|j))`; the derivative
of `phi` at a zero entry is computable and, at a maximiser, must be non-positive. Hwang used
this to prove the positive case; pushing it at a zero entry gives an inequality between
`per(A(i|j))` and the row and column products, which is a bound on a minor rather than on
the spectrum.
C 4, K 2, T 5, F 5, N 4, L 5 → **12 + 8 + 10 + 5 + 8 + 5 = 48**.

### R8. Bound the Sinkhorn scaling factors directly (Hilbert metric)
`-log cap(A) = sum log d_1 + sum log d_2` for the Sinkhorn factors. Sinkhorn's algorithm
contracts in the Hilbert projective metric with rate given by the Birkhoff coefficient of
`A`, which is controlled by `min a_ij / max a_ij`. A bound on the factors in terms of the
margin deficits alone (no spectral quantity) would replace `(UP)` and close the problem
without `G` at all.
C 3, K 3, T 4, F 4, N 5, L 4 → **9 + 12 + 8 + 4 + 10 + 4 = 47**.

### R9. Optimise the doubly stochastic competitor (the direct continuation of Theorem R)
Theorem R bounds `-log cap(A)` by `Phi = (u;v)^T L^+ (u;v)`, the chi-square cost of the
nearest doubly stochastic competitor, and then by `|(u;v)|^2 / (theta_n lambda_2)`. The
second step is where `lambda_2` enters. Any competitor whose cost is bounded by the margins
alone removes `G` from the picture. The Sinkhorn scaling is the exact optimum, so the bound
cannot be improved by a better competitor; only a better estimate of `L^+` on the specific
vector `(u; v)` can help.
C 4, K 2, T 5, F 4, N 5, L 4 → **12 + 8 + 10 + 4 + 10 + 4 = 48**.

### R10. Compute the one-dimensional profile and read the margin off it
Define `Psi_n(delta) = sup { -log cap(A) }` over the constraint set at fixed `delta`. By the
displayed reduction the conjecture at `n` is exactly
`Psi_n(delta) < log(m_n/(gamma_n - delta))` on `(0, gamma_n]`. This is a one-dimensional
statement; `Psi_n` is computable numerically, and its shape says which of R1 to R9 has room.
Not a proof route by itself: it is the measurement that tells the others where to aim.
C 5, K 5, T 5, F 5, N 3, L 2 → **15 + 20 + 10 + 5 + 6 + 2 = 58** (as a measurement, not a proof).

## Ranking

| rank | route | score | why it sits there |
|---|---|---|---|
| 1 | R10 profile computation | 58 | not a proof, but it is cheap, it is decisive about where the margin is, and every other route needs it |
| 2 | R3 quantitative van der Waerden via capacity | 48 | the only route whose target is exactly the missing input and whose constants have room |
| 2 | R7 one-entry variation | 48 | cheapest to try, uses only linearity of the permanent, and is the method that proved the positive case |
| 2 | R9 optimise the competitor | 48 | the direct continuation of what already worked, but the optimum is already attained, so it needs a new estimate rather than a new competitor |
| 5 | R8 Sinkhorn factors by Hilbert metric | 47 | would bypass `G` entirely; the Birkhoff coefficient needs an entrywise bound that may not exist |
| 6 | R6 split by distance from `U_n` | 46 | clean split, but the far region is the whole difficulty |
| 7 | R1 Cheeger and blocks | 43 | complete chain, computed to be empty below `n = 35` |
| 8 | R2 Dirichlet energy and paths | 42 | needs an entrywise lower bound that is not available |
| 8 | R5 Lorentzian polynomials | 42 | strong target, heavy machine, low chance of closing inside this attack |
| 10 | R4 Alexandrov-Fenchel stability | 40 | strongest possible outcome, least likely to be finished here |

## What is run first

R10, because it costs one optimisation run and it re-scores R1 to R9. Then R7, because it
costs only algebra. Then R3.
