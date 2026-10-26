# Route: one-variable interpolation from the centre

Written 2026-09-04, updated after the coordinator's message of the same day (the capacity route
has proved `Q(1/(2n))`; the request is the large-distance half with `c >= 1/n`). Scripts
`route-interpolation-0*.py` in this directory, outputs `route-interpolation-0*-output.txt`.
Status: **complete for what this route can give; the large-distance half is not obtained, and
Section 6 proves why the natural sub-approaches cannot give it.**

Notation. `B = J_n/n + E` doubly stochastic, so `E` has zero row and column sums and
`E_ij >= -1/n`. `F = nE` (entries `>= -1`, zero margins), `Phi = ||F||_F^2 = n^2 ||E||_F^2`,
`d = ||E||_F`, `gamma_n = n!/n^n`, `(n)_k = n!/(n-k)!`, `D_k` = number of derangements of `[k]`.
`f(t) = per(J_n/n + tE)`, `alpha_k` = coefficient of `t^k` in `f(t)/gamma_n`.
`r_k(F) = sum_{|S|=|T|=k} per(F[S,T])` (the `k`-matching sum of `F`).
`Sigma_k(B) = sum_{|S|=|T|=k} per(B[S,T])`, `q_k = Sigma_k(B)/Sigma_k(J_n/n)`.
`y_sigma = (F_{1 sigma(1)}, ..., F_{n sigma(n)})` for a permutation `sigma`; `e_k`, `p_k` are the
elementary and power-sum symmetric functions.

Correction to the task statement: the maximum of `||E||_F^2` over the polytope is `n - 1`
(`||E||_F^2 = ||B||_F^2 - 1` and `||B||_F^2 <= n`, with equality at permutation matrices), not
`2n - 3 + 1/n`.

## 1. What is proved

**Theorem 1 (n = 2).** `per(B) = gamma_2 (1 + ||E||_F^2)`: with `B = [[t,1-t],[1-t,t]]` both
sides are `1/2 + 2(t - 1/2)^2`.

**Theorem 2 (n = 3, sharp).** For every `B` in `Omega_3`,

    per(B)/gamma_3 - 1 - ||E||_F^2/4  =  sum over the three rows b of B of  ( 1 - 4 e_2(b) + 9 e_3(b) )  >= 0.

So `Q(1/4)` holds at `n = 3`, with equality exactly at `J_3/3` and at the row/column permutations
of `(I + C_3)/2`. No `c > 1/4` works at `n = 3`.

**Theorem 3 (every n >= 5, local).**

    per(B)/gamma_n - 1  >=  [ n/(2(n-1)) - 2n/(3(n-1)(n-2)) ] d^2  -  sum_{k=4}^{n} beta_k d^k,
    beta_k = min( n^k/k! ,  (n^k/(n)_k) D_k^2/k! ).

Consequently `Q(c)` holds whenever `d <= rho_n(c)`, the largest radius with
`[n/(2(n-1)) - 2n/(3(n-1)(n-2)) - c] rho^2 >= sum_{k>=4} beta_k rho^k` (script 07):

| n | rho_n(1/4) | rho_n(1/n) |
|---|---|---|
| 5 | 0.0708 | 0.0862 |
| 6 | 0.0900 | 0.1082 |
| 7 | 0.0919 | 0.1098 |
| 8 | 0.0987 | 0.1173 |
| 10 | 0.1008 | 0.1184 |
| 15 | 0.1012 | 0.1155 |
| 20 | 0.1013 | 0.1136 |
| 30 | 0.0964 | 0.1051 |
| 50 | 0.0875 | 0.0928 |

With the first bound alone (`beta_k = n^k/k!`) the radius is about `1.9/n`; the second keeps it
near `0.1` up to `n ~ 30` and then decays like `n^{-1/2}`.

**Proposition 4 (exact identities, all n).**
(a) `f(t)/gamma_n = sum_{k=0}^n r_k(F) t^k/(n)_k`; `r_0 = 1`, `r_1 = 0`, `r_2 = Phi/2`,
    `r_3 = (2/3) sum_ij F_ij^3`,
    `24 r_4 = 36 sum F_ij^4 - 18 (sum_i R_i^2 + sum_j C_j^2) + 3 Phi^2 + 6 ||F F^T||_F^2`
    (`R_i, C_j` = row and column sums of the entrywise square of `F`). In particular
    `alpha_2 = (n/(2(n-1))) d^2` (fact 2 of the task) and `alpha_3 = (2n^3/(3 (n)_3)) sum_ij E_ij^3`.
(b) Bernstein form: `f(t)/gamma_n = sum_k C(n,k) q_k t^k (1-t)^{n-k}`, `q_0 = q_1 = 1`,
    `q_2 = 1 + d^2/(n-1)^2`, `q_n = per(B)/gamma_n`, and
    `f'(t) = n gamma_n sum_k C(n-1,k) (q_{k+1} - q_k) t^k (1-t)^{n-1-k}`.
(c) `Q(c)` is equivalent to `q_n - 1 >= c (n-1)^2 (q_2 - 1)`; in particular `q_n >= q_2` is
    `Q(1/(n-1)^2)`.
(d) Two-sided Moebius expansion: for `F` with zero margins,
    `k! r_k(F) = sum_{pi, rho} mu(pi) mu(rho) hom(G_{pi,rho}, F)`, the sum over pairs of set
    partitions of `[k]` with no singleton block (`mu(pi) = prod_blocks (-1)^{|b|-1}(|b|-1)!`),
    where `G_{pi,rho}` is the bipartite multigraph with a row-vertex per block of `pi`, a
    column-vertex per block of `rho`, one edge per element, and `hom(G, F)` is the sum over
    labellings of the vertices by `[n]` of the product of `F` over the edges. Verified at
    `n = 7` for `k = 4, 5, 6, 7` (16, 121, 1681, 26244 diagrams) to relative `3e-14` (script 08).

## 2. Proofs

### 2.1 Taylor form and the matching sums (Proposition 4a, d)

`per(J/n + tE) = n^{-n} sum_sigma prod_i (1 + t F_{i sigma(i)})`. The coefficient of `t^k`
collects, for each `k`-subset `S` of rows, the products `prod_{i in S} F_{i sigma(i)}`; summing
over `sigma` counts each injection `S -> [n]` exactly `(n-k)!` times, so the coefficient is
`n^{-n} (n-k)! r_k(F)` and `alpha_k = r_k(F)/(n)_k`.

`r_2`: `2 r_2 = sum_{i != i', j != j'} F_ij F_i'j' = (sum F)^2 - sum_i (row_i)^2 - sum_j (col_j)^2 + sum F_ij^2 = Phi`.

Moebius expansion (d). `k! r_k` is the sum over `k`-tuples of entries with pairwise distinct rows
and pairwise distinct columns. Moebius inversion on the partition lattice of `[k]`, applied to the
row indices and to the column indices separately, expresses it as
`sum_{pi,rho} mu(pi) mu(rho) S(pi,rho)`, where `S(pi,rho)` sums over row labels constant on the
blocks of `pi` and column labels constant on the blocks of `rho`; that is `hom(G_{pi,rho}, F)`.
If `pi` has a singleton block `{l}`, the row label of `l` occurs in exactly one factor, and summing
it gives a row sum of `F`, which is zero; likewise for `rho`. So only partitions without
singletons survive. `k = 3`: the only such partition is the one-block partition (`mu = 2`),
giving `6 r_3 = 4 sum F_ij^3`. `k = 4`: the one-block partition (`mu = -6`) and the three pair
partitions (`mu = 1`); the nine diagrams are `S(full,full) = sum F^4`,
`S(full, pair) = sum_i R_i^2`, `S(pair, full) = sum_j C_j^2`, `S(pair, same pair) = Phi^2`,
`S(pair, other pair) = ||F F^T||_F^2`. Checked exactly (script 06) and numerically (scripts 01, 08).

### 2.2 Bernstein form (Proposition 4b, c)

`f(t) = per((1-t) J/n + tB)`; the terms using `k` columns of `tB` and `n-k` columns of
`(1-t)J/n` sum to `t^k ((1-t)/n)^{n-k} (n-k)! Sigma_k(B)`, and `Sigma_k(J/n) = C(n,k)^2 k!/n^k`.
`Sigma_2(B) = (n^2 - 2n + ||B||_F^2)/2` gives `q_2`. Differentiate termwise for `f'`.

### 2.3 Theorem 2

At `n = 3` the polynomial has degree 3, so `per(B)/gamma_3 - 1 = (3/4) d^2 + 3 sum_ij E_ij^3` and

    per(B)/gamma_3 - 1 - d^2/4 = (1/2) sum_ij E_ij^2 (1 + 6 E_ij) = (1/2) sum_ij g(B_ij),
    g(x) = (x - 1/3)^2 (6x - 1) = 6x^3 - 5x^2 + (4/3) x - 1/9.

For a row `(x,y,z)` with `x + y + z = 1`, `sum g = 6 p_3 - 5 p_2 + 1 = 2 (1 - 4 e_2 + 9 e_3)`
(`p_2 = 1 - 2e_2`, `p_3 = 1 - 3e_2 + 3e_3`). Schur's inequality of degree 1,
`sum_sym x(x-y)(x-z) = e_1^3 - 4 e_1 e_2 + 9 e_3 >= 0` for `x, y, z >= 0`, gives
`1 - 4e_2 + 9e_3 >= 0` on the simplex, with equality iff `x = y = z` or one variable is `0` and
the other two are equal. A doubly stochastic matrix whose rows are all of these two types is
`J_3/3` or a row/column permutation of `(I + C_3)/2` (a uniform row cannot coexist with a
`(1/2,1/2,0)` row: the other rows would have to contribute `2/3` to each column with entries in
`{0, 1/2, 1}`). Checked exactly in script 06.

### 2.4 Theorem 3

Cubic term. `F_ij >= -1` gives `sum_ij F_ij^3 >= -sum_{F_ij<0} F_ij^2 >= -Phi`, so
`alpha_3 >= -(2/3) Phi/(n)_3 = -(2n/(3(n-1)(n-2))) d^2`.

Bound A (Cauchy-Schwarz). There are `C(n,k)^2 k!` `k`-matchings, and the sum over matchings of
the squared products is at most `Phi^k/k!`. So `|r_k| <= C(n,k) Phi^{k/2}` and
`|alpha_k| <= Phi^{k/2}/k! = (n^k/k!) d^k`.

Bound B (Moebius + Hoelder). Lemma (generalised Hoelder, counting measure): if nonnegative
functions `f_e`, each depending on the variables of its edge `e`, and exponents `p_e >= 1` satisfy
`sum_{e ni v} 1/p_e >= 1` at every vertex `v`, then `sum_x prod_e f_e <= prod_e ||f_e||_{p_e}`.
Proof by induction on the number of vertices: fix all variables but `x_v`; choose `q_e >= p_e`
with `sum_{e ni v} 1/q_e = 1` (scale the `1/p_e` down), apply Hoelder in `x_v`, use
`||.||_{q_e} <= ||.||_{p_e}` for counting measure, and note that the functions
`x_{e-v} -> ||f_e(., x_{e-v})||_{p_e}` again satisfy the hypothesis on the remaining vertices,
with `||g_e||_{p_e} = ||f_e||_{p_e}` by Fubini. Every vertex of `G_{pi,rho}` has degree `>= 2`,
so all `p_e = 2` is admissible and `|hom(G_{pi,rho}, F)| <= Phi^{k/2}`. Since
`sum_{pi no singleton} |mu(pi)| = D_k` (permutations of cycle type `pi` number
`prod (|b|-1)!`, and no singleton blocks means no fixed points),
`|r_k| <= D_k^2 Phi^{k/2}/k!` and `|alpha_k| <= (n^k/(n)_k)(D_k^2/k!) d^k`.

`alpha_2`, the cubic bound and `beta_k = min(A, B)` give Theorem 3; the radii are by bisection.

## 3. Numerical picture (not proved)

- Sharp constants (task facts): `c*(n) = 1/4, 1/3, 0.4184, 0.4605, 0.4867, 0.4975` for `n = 3..8`.
  The lighter re-run in script 03 found only upper bounds (`0.429, 0.543, 0.584` at `n = 5, 6, 7`)
  but shows the shape of the Taylor profile at its minimisers: at `n = 3, 4, 5` (zeros present,
  `d^2 = 0.5, 1, 1.46`) the whole loss is in the cubic and top coefficients
  (`alpha_k/d^2 = +0.75, -0.50` at `n = 3`; `+0.667, 0, -0.333` at `n = 4`;
  `+0.625, +0.137, -0.055, -0.278` at `n = 5`), while at the interior points found for
  `n = 6, 7` (`d^2 = 0.15, 0.14`) the `k >= 4` tail is below `0.01 d^2` in absolute value and the
  cubic term is `-0.067 d^2`, `-0.006 d^2`.
- Structured families (script 04, `n <= 12`): the cubic remainder
  `(per/gamma - 1 - (n/(2(n-1))) d^2)/d^3` stayed in `[-0.64, +2.9]`; the negative values come
  from `T_n` (about `-0.63`) and `(I + C_4)/2` (`-1/3`). A uniform one-sided bound
  `per/gamma - 1 >= (n/(2(n-1))) d^2 - C d^3` with `C ~ 0.7` is consistent with all data;
  Theorem 3 does not prove it.
- `max_k |alpha_k|/d^k` over random matrices is about `1` for `n <= 6` (script 05; its
  `n = 7, 8` lines are floating-point noise from tiny `d` and are superseded by script 08).

## 4. The chain through the subpermanent sums, and why it is closed

By Proposition 4c the termwise chain `q_{k+1} >= q_k` (nonnegative Bernstein coefficients of
`f'`) is the Holens-Dokovic conjecture `sigma_i(A) >= ((n-i+1)^2/(i n)) sigma_{i-1}(A)` of
Wanless, Linear Algebra Appl. 286 (1999) 273-285 (pages 1-5 and 10-13 read):

- proved for `i <= 2` (Holens, thesis, Manitoba 1964), `i = 3` (Dokovic, Mat. Vesnik 19 (1967)
  566-569), `i = 4`, `n >= 5` (Kopotun, Linear Multilinear Algebra 36 (1994) 205-216);
- the case `i = n` is `n^2 per(A) >= sigma_{n-1}(A)`, i.e. `f'(1) >= 0` ("monotonicity of the
  permanent" along the segment from `J_n/n` to `A`). Wanless's Example 2 is an order-22 doubly
  stochastic matrix with `sigma_22 = 295245/2^40`, `sigma_21 = 143644347/2^40`, and
  `143644347/295245 > 22^2`: `f'(1) < 0` there. So `per` is not monotone along every ray from the
  centre once `n = 22`, and any argument needing `f' >= 0` on `[0,1]` is closed for general `n`.
- Even where the whole chain holds it only gives `q_n >= q_2`, that is `Q(1/(n-1)^2)`, and
  `1/(n-1)^2 < 1/n` for every `n >= 3`. So the chain cannot reach `1/n` at any `n >= 3`, true or
  not. At `n = 3` it is Dokovic's case and equals `Q(1/4)`; Theorem 2 reproves it.
- Friedland, Linear Multilinear Algebra 11 (1982) 107-120, proved `Sigma_k(B) >= Sigma_k(J_n/n)`
  for all `k` (Tverberg's conjecture), i.e. `q_k >= 1` (seen only through the journal listing and
  Wanless's bibliography; used in no proof here). Heilmann-Lieb real-rootedness gives the Newton
  inequalities `q_i^2 >= ((n-i)/(n-i+1)) q_{i-1} q_{i+1}`, which bound the ratios `q_{i+1}/q_i`
  from above, the wrong direction.

## 5. Gaps of the local theorem

1. Theorem 3's radius decays like `n^{-1/2}`; a uniform bound `|alpha_k| <= C^k d^k` would give
   a radius independent of `n`. Both coefficient bounds lose factors growing with `k`: Bound B
   counts `D_k^2` diagrams that in fact cancel (for rank-one `F = M v v^T`,
   `r_k = M^k k! e_k(v)^2`, smaller than the bound by a factor of order `(k!)^2`), and the
   cancellation is between diagrams, not inside them (Section 6.3).
2. `n = 4`: numerically `c*(4) = 1/3` at `(I + C_4)/2`, where `alpha_4 = -d^2/3` against
   `alpha_2 = 2 d^2/3`; the cubic bound of Theorem 3 gives only `c < 2/9` locally. The degree-4
   polynomial inequality that is `Q(1/4)` at `n = 4`,
   `15 Phi + 16 p_3 + 36 p_4 - 18 (sum R_i^2 + sum C_j^2) + 3 Phi^2 + 6 ||F F^T||^2 >= 0` (value
   `48` at `(I + C_4)/2`), was not certified.

## 6. The large-distance half: what this route cannot give, with proofs

The coordinator's target: `per(B) >= gamma_n (1 + c d^2)` with `c >= 1/n` on the annulus
`rho_n(1/n) <= d <= sqrt(n-1)`; at `n = 7` that is `0.1098 <= d <= 2.449`. The capacity route's
Theorem 2 gives `per(B) >= gamma_n exp(d^2/(2n))` there, and `exp(u) >= 1 + 2u` fails for every
`u = d^2/(2n) <= (n-1)/(2n) < 1/2`, so the exponential bound alone never reaches `c = 1/n`; the
missing factor `(1 + d^2/n)/exp(d^2/(2n))` is `1.21` at `d^2 = 6`, `1.06` at `d^2 = 1`, `1.01` at
`d^2 = 0.137` (`n = 7`). Nothing below closes this gap. What is established is that the three
sub-approaches available inside the one-variable route cannot close it.

### 6.1 One-variable information at the point `t = 1` is only the exponential bound

Every input this route has is a lower bound on `f(t)` at points of the segment: van der Waerden
and Friedland (`q_m >= 1`, hence `f >= gamma_n` on `[0,1]`), the local Theorem 3 for
`t d <= rho_n`, the exponential bound `f(t) >= gamma_n exp(t^2 d^2/(2n))` on `[t_-, t_+]`, the
proved chain steps (`q_4 >= q_3 >= q_2`, `n >= 5`), and Newton's inequalities (upper bounds on
`q_{i+1}/q_i`). In the Bernstein form, `q_n = f(1)/gamma_n` is a free coordinate: every input listed is
either a lower bound on a value `f(t)`, which is non-decreasing in `q_n` (the Bernstein weight
`t^n` of `q_n` is positive) and so stays satisfied when `q_n` grows, or an upper bound on `q_n`
(Newton: `q_n <= 2 q_{n-1}^2 / q_{n-2}`); the only lower bound on `q_n` itself is the exponential
bound. So no combination of these inputs gives more at `t = 1` than `exp(d^2/(2n))`. A new input
has to be a genuinely multi-column statement about `B`.

### 6.2 Bounds that hold permutation by permutation lose a factor `n`

`per(B)/gamma_n = E_sigma prod_i (1 + y_i)` with `y = y_sigma`, `sigma` uniform. The known
moments are `E e_1 = 0`, `E p_2 = Phi/n = n d^2`, `E e_1^2 = Phi/(n-1)`, `E e_2 = Phi/(2n(n-1))`,
and `E e_3 = alpha_3 >= -(2n/(3(n-1)(n-2))) d^2`. The natural scheme is a pointwise inequality

    h(y) := prod_i (1 + y_i) - 1 - e_1(y) - lambda e_1(y)^2 + a p_2(y) >= 0   on [-1, oo)^n,

which yields `per/gamma_n - 1 >= (lambda n/(n-1) - a) n d^2`, so the constant is
`c = (lambda n/(n-1) - a)`. Second order at `y -> 0` forces `a >= 1/2` and `a >= lambda`; the
point `y = (-t, -t, -t, 0, ..., 0)` gives `h = t^2 (3 - 9 lambda + 3a) - t^3`, so `t = 1`
forces `a >= 3 lambda - 2/3`. Hence `c <= lambda n/(n-1) - max(1/2, 3 lambda - 2/3)`, whose
maximum over `lambda` is at `lambda = 7/18`: `c <= 7n/(18(n-1)) - 1/2 < 0` for every `n >= 5`.
Removing the cubic obstruction by paying `E e_3` (test function `e_3`) moves it to fourth order:
at `y = (t, t, t, -t, 0, ..., 0)`, `h = 4 t^2 (a - lambda) - t^4`, forcing `a >= lambda + 1/4`
and `c <= lambda/(n-1) - 1/4 < 0` for `n >= 4` and `lambda <= 1/2`. Each further test function
`e_k` costs its own Moebius bound and meets the same obstruction one order up. The reason is
structural: the second-order term `E e_2 = E p_2/(2(n-1))` is a `1/n` effect of the permutation
constraint (negative correlation `-1/(n-1)` between `sigma(i)` and `sigma(i')`), and a pointwise
inequality cannot see it.

### 6.3 Diagram-wise bounds on the tail cannot close `n = 7` in the application regime

The capacity route's notes reduce the application at `n = 7` to the regime
`per(B) <= e^{K_0} gamma_7`, `K_0 = log(m_7/gamma_7) = 0.01330`, where its Theorems 1-2 applied
to every row and column give `d_j, d'_i <= 2 K_0 = 0.0266` (so `|E_ij| <= 0.163`) and
`d^2 <= 2 n K_0 = 0.1861`; in `F`-units: `Phi <= 9.121`, row and column squared norms `<= 1.303`,
`max |F_ij| <= 1.1415`. The running total there is `alpha_2 = 0.5833 d^2`, cubic `>= -0.156 d^2`
(Theorem 3's bound), quartic `>= -0.114 d^2` (from Proposition 4a: `24 r_4 >= -18 (sum R_i^2
+ sum C_j^2) >= -36 * 1.303 * Phi`), total `0.313 d^2`; to reach `c = 1/7` the `k = 5, 6, 7`
terms must together be `>= -0.170 d^2`. Numerically (capacity route, 2307 samples) the whole
`k >= 4` tail lies in `[-0.0007, 0.0877] d^2`.

Script 08 bounds every diagram of Proposition 4d with the regime constants, using for a diagram
with `|V_r|` row-vertices and `|V_c|` column-vertices

    |hom| <= min( c0^{k - 2|V_c|} Phi^{|V_c|},  c0^{k - 2|V_r|} Phi^{|V_r|} ),     c0^2 = 1.303,

(contract the row-vertices first: a row-vertex of degree `d` contributes
`|sum_i prod_l F_{i j_l}| <= prod_l ||F_{. j_l}||_2` by Hoelder, then `sum_j C_j^{d_w/2} <=
c0^{d_w-2} Phi`; or the column-vertices first), and `|sum F_ij^k| <= Phi m^{k-2}` for the
one-block/one-block diagram. The result, as multiples of `d^2` at the largest `Phi`:

| k | all diagrams | one-block/one-block diagram alone |
|---|---|---|
| 4 | 0.428 | 0.114 |
| 5 | 1.045 | 0.139 |
| 6 | 4.719 | 0.330 |
| 7 | 48.62 | 1.938 |

So the term-by-term bound of the `k = 5, 6, 7` tail is `54 d^2` against the needed `0.17 d^2`,
and already the single diagram `((k-1)!)^2 p_k/k!` at `k = 6` or `k = 7` exceeds the budget on
its own (its size is real: `p_7 = sum F_ij^7` can be of order `Phi m^5` for a matrix with a few
entries near `1/n + 0.163`). The truth is small only because diagrams cancel each other, as in
the rank-one identity `r_k = M^k k! e_k(v)^2`. Consequence: the plan "enumerate the Moebius
diagrams for `P_5, P_6, P_7` and bound each" in the capacity route's follow-up cannot reach
`a' >= 1/7`; the required cancellation has to be captured by an identity, not by bounds.

### 6.4 What the two halves cover at `n = 7`

Theorem 3: `Q(1/7)` for `d <= 0.1098`. Capacity route: `per >= gamma_7 exp(d^2/14)` everywhere.
The application's fixed point with the exponential bound alone gives `K = 0.01225 < K_0 =
0.01330` (margin `1.086`, condition (N) with `|alpha + beta| <= 0.30`), the same numbers as the
capacity route's table; it is the two owed corrections (`lambda_2(A)` versus `lambda_2(B)`, of
size up to `sqrt(gamma_7) = 0.078` in `lambda_2`) that make the margin insufficient, not the
constant on the far annulus. In that regime the matrices to be excluded have `per/gamma_7 <=
1.0123`, hence `d <= 0.414` by the exponential bound; the uncovered set is therefore
`0.1098 < d <= 0.414` with all row and column deviations `<= 0.0266`, not the full annulus up
to `sqrt 6`. Nothing here covers it.

## 7. Gaps, precisely

1. **Annulus.** No bound with `c >= 1/n` is proved for `d > rho_n(1/n)`; at `n = 7` the set
   that matters is `0.1098 < d <= 0.414` (Section 6.4). Sections 6.1-6.3 show that one-variable
   inputs, permutation-wise inequalities, and diagram-wise tail bounds cannot give it.
2. **Uniform local constant.** A bound `|alpha_k| <= C^k d^k` uniform in `n`, or a one-sided
   `per/gamma - 1 >= (n/(2(n-1))) d^2 - C d^3`, is numerically plausible (Section 3) and would
   make the local radius independent of `n`; it needs an expansion of `r_k(F)` that exhibits the
   cancellation between Moebius diagrams. For rank-one `F` that is Newton's identity for `e_k` of
   a zero-sum vector; for general `F` no analogue is known here.
3. **`n = 4`.** `c*(4) = 1/3` numerically; the degree-4 inequality of Section 5, item 2, is not
   certified; the chain `q_4 >= q_3 >= q_2` would give only `1/9` and needs the `i = n = 4` case,
   whose status in print was not checked.

## 8. Numerical checks run

- `route-interpolation-01-identities.py`: Taylor and Bernstein forms against direct permanents,
  `r_3`, `r_4`, `q_2`, the Bernstein step identity; max discrepancy `8e-13`.
- `route-interpolation-02-chain.py`: `min (q_n - q_{n-1})/(q_2 - q_1) = 0` at `n = 3, 4, 5`,
  attained at `(P + Q)/2` with `P^{-1} Q` an `n`-cycle (the equality case of the last chain step);
  smallest step at `n = 4`: `+0.022`.
- `route-interpolation-03-profile.py`: Taylor profiles at ratio minimisers, `n = 3..7` (light
  search; the far-region table at `c = 1/4` was still running when this was written).
- `route-interpolation-04-families.py`: ratio and cubic remainder on structured families.
- `route-interpolation-05-coefficients.py`: the `n = 3` identity on 2000 random matrices and
  Schur's form on `2e5` simplex points.
- `route-interpolation-06-exact.py`: identities (i)-(v) exact in sympy, `n = 3, 4, 5`; Schur's
  identity; `(I + C_3)/2` is an equality case.
- `route-interpolation-07-radius.py`: the radius table of Theorem 3.
- `route-interpolation-08-diagrams.py`: Proposition 4d verified at `n = 7`, `k = 4..7`; the
  regime bounds of Section 6.3.
