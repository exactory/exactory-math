# Route: a deficiency term from the capacity proof

Written 2026-09-04. Scripts: `route-capacity-01-last-step.py` to `route-capacity-06-step-checks.py`
in this directory, outputs in `route-capacity-0k-output.txt`. Python: the project venv,
`OMP_NUM_THREADS=1`.

## 0. Summary

**Proved.** For every `n >= 2` and every doubly stochastic `n x n` matrix `B`, with
`E = B - J_n/n`,

    per(B) >= gamma_n * exp( ||E||_F^2 / (2n) ) >= gamma_n * ( 1 + ||E||_F^2 / (2n) ).

That is claim Q(c) with `c = 1/(2n)`, which the assignment lists as a complete success. The
proof is short: one new lemma (two applications of the weighted AM-GM inequality) plus Gurvits'
theorem applied to the polynomial obtained after peeling one variable. The lemma is sharp. The
theorem it gives, `per(B) >= gamma_{n-1} * prod_i (1 - b_ij)^(1 - b_ij)` for every column `j`,
is exact at the Knopp-Sinkhorn face minimisers and at `(I + C_3)/2`.

**Not proved.** Q(1/n) and Q(1/4). The route above sees one column at a time, and a
single-column bound cannot give more than about `1/(2n)` (Section 5, item 1). Seeing two
columns at once gives Q(1/n) numerically (measured constant about `0.55 * (2/n)`), and the
inequality that would prove it is stated exactly in Section 5, item 2; it is verified
numerically at `n = 3..6` but not proved.

**On part (a) of the assignment.** `cap(p_B) = 1` for every doubly stochastic `B`, attained at
`x = (1,...,1)`, so the AM-GM step alone carries no deficiency. This is a fact, not a
conjecture (Section 2.4). The deficiency of the capacity proof lives in the peeling step, and
for the first peeled variable it is exactly the lemma below.

## 1. Notation and the two cited theorems

`n >= 2`. `B = (b_ij)` is doubly stochastic. `gamma_n = n!/n^n`. For `k >= 2`,
`g(k) = ((k-1)/k)^(k-1)`, and `g(1) = 1`. Then

    gamma_n = prod_{k=2}^{n} g(k),      gamma_n = gamma_{n-1} g(n),      gamma_1 = 1,

because `prod_{k=2}^{n} (k-1)^(k-1) / k^(k-1) = (prod_{m=1}^{n-1} m^m) * n! / prod_{k=2}^{n} k^k
= n!/n^n`.

For a polynomial `P` in `m` variables, homogeneous of degree `m`, with non-negative coefficients,
its capacity is

    cap(P) = inf_{x in R^m, x > 0}  P(x) / (x_1 ... x_m).

This is `Cap(p)` of Gurvits [G, abstract] and, by homogeneity, the `cap(p)` of Laurent and
Schrijver [LS, (12)], who take the infimum over `prod x_j = 1`.

`P` is H-stable if `P(z) != 0` whenever every `Re(z_j) > 0` [G, Section 2, item 5; LS, Section 2].
`Hom_+(m, m)` is Gurvits' name for the polynomials above (homogeneous of degree `m` in `m`
variables, non-negative coefficients).

The two results quoted from the literature:

- **[G, Fact 4.9(2)]** (also [LS, Theorem 1, first part]). If `p` is in `Hom_+(m, m)` and is
  H-stable, then `q(x_1, ..., x_{m-1}) = (d/dx_m) p(x_1, ..., x_{m-1}, 0)` is either zero or
  H-stable.
- **[G, Corollary 2.5]** (the case `deg` unrestricted of [G, Theorem 2.4]). If `p` is in
  `Hom_+(m, m)` and is H-stable, then

      (d^m / dx_1 ... dx_m) p(0) >= (m!/m^m) * cap(p).

  For `m = 1` this is trivial (`p = a x_1`, both sides equal `a`). The same inequality follows
  by iterating [LS, Theorem 1], `cap(p') >= cap(p) g(deg_{x_m} p)` with `p' = (d/dx_m) p(., 0)`,
  which is stated there for every H-stable homogeneous `p`, not only for products of linear
  forms; `deg_{x_i} q_i <= i` and `g` is non-increasing.

References. [G] L. Gurvits, Van der Waerden/Schrijver-Valiant like conjectures and stable (aka
hyperbolic) homogeneous polynomials: one theorem for all, Electron. J. Combin. 15 (2008), no. 1,
Research Paper R66 (published 5 May 2008, corrigendum 29 May 2008); arXiv:0711.3496. The v2
text on arXiv was read for this note and the numbering above is that of v2. [LS] M. Laurent and
A. Schrijver, On Leonid Gurvits's proof for permanents, Amer. Math. Monthly 117 (2010), no. 10,
903-911 (the statements were read from the authors' copy at homepages.cwi.nl/~monique). [KS]
P. Knopp and R. Sinkhorn, Minimum permanents of doubly stochastic matrices with at least one
zero entry, Linear Multilinear Algebra 11 (1982), 351-355; the value `m_n` is also derived in
[G, Section 2, item 4].

The polynomial of `B` is `p_B(x) = prod_{i=1}^{n} l_i(x)`, `l_i(x) = sum_j b_ij x_j`. Its
coefficient of `x_1 ... x_n` is `per(B)`, and equals `(d^n/dx_1...dx_n) p_B(0)`.

Column `n` of `B` is `v = (b_1n, ..., b_nn)`, a probability vector. For `x in R^{n-1}` write
`l'_s(x) = sum_{j<=n-1} b_sj x_j` (the row forms with column `n` removed) and

    q(x) = (d/dx_n) p_B(x, 0) = sum_{r=1}^{n} v_r prod_{s != r} l'_s(x).          (1.1)

(1.1) is checked symbolically for `n = 3, 4` in script 06, part (iii). Finally

    K(v) = prod_{s=1}^{n} (1 - v_s)^(1 - v_s),      with 0^0 = 1.

## 2. The proof

### 2.1 Lemma A (the deficiency of the first peeled variable)

**Lemma A.** For every `x in R^{n-1}` with all `x_j > 0`,

    q(x) >= K(v) * x_1 x_2 ... x_{n-1}.

Consequently `cap(q) >= K(v)`.

*Proof.* Write `a_s = l'_s(x) >= 0`.

Case 1: some `v_s = 1`. Column `n` sums to 1, so `v_r = 0` for `r != s`; row `s` sums to 1, so
`b_sj = 0` for `j <= n-1`. Then `q(x) = prod_{r != s} l'_r(x)`, and the `(n-1) x (n-1)` matrix
`(b_rj)_{r != s, j <= n-1}` is doubly stochastic (row sums `1 - b_rn = 1`, column sums
`1 - b_sj = 1`). By the weighted AM-GM inequality on each row, `l'_r(x) >= prod_j x_j^(b_rj)`,
and multiplying over `r != s` gives `q(x) >= prod_j x_j^(sum_{r != s} b_rj) = prod_j x_j`. Here
`K(v) = 1`, so the claim holds.

Case 2: every `v_s < 1`. Then row `s` has positive mass on columns `1..n-1`
(`sum_{j<=n-1} b_sj = 1 - v_s > 0`), so `a_s > 0`.

Step 1 (AM-GM with weights `v`). By (1.1), `q(x) = (prod_s a_s) * sum_r v_r / a_r`. The weights
`v_r` are non-negative and sum to 1, so the weighted AM-GM inequality gives
`sum_r v_r (1/a_r) >= prod_r a_r^(-v_r)`, hence

    q(x) >= prod_s a_s^(1 - v_s).                                                  (2.1)

Step 2 (AM-GM inside each row). For each `s`, the weights `b_sj/(1 - v_s)`, `j <= n-1`, sum to
1, so `a_s/(1 - v_s) = sum_j (b_sj/(1-v_s)) x_j >= prod_j x_j^(b_sj/(1-v_s))`. Raising to the
power `1 - v_s > 0`,

    a_s^(1 - v_s) >= (1 - v_s)^(1 - v_s) * prod_j x_j^(b_sj).

Multiply over `s` and use the column sums `sum_s b_sj = 1` for `j <= n-1`:

    prod_s a_s^(1 - v_s) >= K(v) * prod_j x_j.                                     (2.2)

(2.1) and (2.2) give the lemma. QED.

Both steps are checked pointwise at random `x` and random (dense and sparse) `B` in script 06,
part (i); the minimum ratios are `1.000000013` and `1.000000000`.

**Sharpness.** If `v` is uniform on its support, `v_s = 1/k` for `k` rows and `0` elsewhere,
then `K(v) = (1 - 1/k)^(k-1) = g(k)`, and `cap(q) <= q(1, ..., 1) = prod_s (1 - v_s) *
sum_r v_r/(1 - v_r) = (1 - 1/k)^k * k * (1/k) / (1 - 1/k) = g(k)`. So `cap(q) = g(k) = K(v)`
exactly, whatever the other columns of `B` are. Gurvits' degree bound [G, Theorem 4.10],
`cap(q) >= g(deg_{x_n} p_B) cap(p_B) = g(#supp v)`, is recovered from Lemma A by convexity of
`t -> (1-t) log(1-t)` (Jensen over the support of `v`), and Lemma A is strictly stronger for
every column that is not uniform on its support.

### 2.2 Lemma B (Gurvits' theorem after one peeling)

**Lemma B.** `per(B) >= gamma_{n-1} * cap(q)`.

*Proof.* `p_B` is in `Hom_+(n, n)`. It is H-stable: if every `Re(x_j) > 0` then
`Re(l_i(x)) = sum_j b_ij Re(x_j) > 0` for every `i` (each row of `B` is non-zero), so
`p_B(x) != 0`. The polynomial `q` of (1.1) is homogeneous of degree `n-1` in `n-1` variables with
non-negative coefficients, so `q` is in `Hom_+(n-1, n-1)`. It is not zero: its coefficient of
`x_1 ... x_{n-1}` is the coefficient of `x_1 ... x_n` in `p_B`, which is `per(B)`, and
`per(B) > 0` because `B` is a convex combination of permutation matrices (Birkhoff) and so some
permutation has all its entries positive in `B`. By [G, Fact 4.9(2)], `q` is H-stable. For a
multilinear monomial the mixed derivative at `0` equals the coefficient, so
`(d^{n-1}/dx_1...dx_{n-1}) q(0) = per(B)`. [G, Corollary 2.5] for `q` (equivalently, [LS,
Theorem 1] applied `n-2` times along `q = q_{n-1}, q_{n-2}, ..., q_1 = per(B) x_1`) gives
`per(B) >= ((n-1)!/(n-1)^(n-1)) cap(q) = gamma_{n-1} cap(q)`. For `n = 2` the statement is
`per(B) >= cap(per(B) x_1) = per(B)`. QED.

### 2.3 Theorem 1 (one column, exact form)

**Theorem 1.** For every doubly stochastic `B` and every column index `j`,

    per(B) >= gamma_{n-1} * prod_{i=1}^{n} (1 - b_ij)^(1 - b_ij).

The same holds for every row `i` with `prod_j (1 - b_ij)^(1 - b_ij)`.

*Proof.* `per(B)` is invariant under column permutations, so take `j = n`; then Lemma B and
Lemma A give `per(B) >= gamma_{n-1} cap(q) >= gamma_{n-1} K(v)`. Rows: apply this to `B^T`,
which is doubly stochastic with `per(B^T) = per(B)`. QED.

Equality cases. At Gurvits' matrices `D` of [G, (19)] (last column uniform on `k` rows, the rest
constant in each row) `per(D) = g(k) gamma_{n-1}` [G, Section 2, item 4] and `K(col_n) = g(k)`,
so Theorem 1 is an equality. For `k = n-1` these are the Knopp-Sinkhorn face minimisers with
`per = m_n = gamma_{n-1} g(n-1)`. At `(I + C_3)/2`: `per = 1/4 = gamma_2 * K((1/2, 1/2, 0)) =
(1/2)(1/2)`. Theorem 1 also contains the face bound of [KS]: if `B` has a zero entry, the column
`v` through it has `v_s = 0` for some `s`, and Jensen on the other `n-1` coordinates gives
`K(v) >= (1 - 1/(n-1))^(n-2) = g(n-1)`, so `per(B) >= gamma_{n-1} g(n-1) = m_n`.

### 2.4 Lemma C (the quadratic lower bound of `K`)

**Lemma C.** For every probability vector `v` in `R^n`, `n >= 2`,

    K(v) >= g(n) * exp( ||v - 1/n||^2 / 2 ),      ||v - 1/n||^2 = sum_s (v_s - 1/n)^2.

*Proof.* Let `phi(t) = (1 - t) log(1 - t)` on `[0, 1)`, extended by `phi(1) = 0` (continuous).
`phi'(t) = -log(1-t) - 1` and `phi''(t) = 1/(1-t) >= 1` on `[0, 1)` (script 06, part (ii),
checks `phi''` with sympy). Taylor's formula with integral remainder at `t_0 = 1/n`, for `t` in
`[0, 1)`:

    phi(t) = phi(t_0) + phi'(t_0)(t - t_0) + int_{t_0}^{t} (t - u) phi''(u) du
          >= phi(t_0) + phi'(t_0)(t - t_0) + (t - t_0)^2 / 2,

since the integrand `(t - u) phi''(u)` has the sign of `(t - t_0)` on the interval and
`phi'' >= 1`. By continuity the bound also holds at `t = 1`. Sum over `s`, using
`sum_s (v_s - 1/n) = 0` and `n phi(1/n) = (n-1) log((n-1)/n) = log g(n)`:
`sum_s phi(v_s) >= log g(n) + ||v - 1/n||^2 / 2`. Exponentiate; `K(v) = exp(sum_s phi(v_s))`.
QED.

Checked at 20000 random probability vectors, `n = 2..11` (script 06, part (ii)): minimum ratio
`1.0000000086`.

### 2.5 Theorem 2 (the claim, with `c = 1/(2n)`)

**Theorem 2.** For every `n >= 2` and every doubly stochastic `n x n` matrix `B`, with
`E = B - J_n/n`, `d_j = ||col_j(B) - 1/n||^2` and `d'_i = ||row_i(B) - 1/n||^2`,

    per(B) >= gamma_n * exp( max( max_j d_j, max_i d'_i ) / 2 )
           >= gamma_n * exp( ||E||_F^2 / (2n) )
           >= gamma_n * ( 1 + ||E||_F^2 / (2n) ).

*Proof.* Theorem 1 and Lemma C give `per(B) >= gamma_{n-1} g(n) exp(d_j/2) = gamma_n exp(d_j/2)`
for every `j`, and likewise for rows. `||E||_F^2 = sum_j d_j <= n max_j d_j`. Finally
`e^t >= 1 + t`. QED.

The geometric mean over the columns of Theorem 1 gives the equivalent product form

    per(B) >= gamma_{n-1} * prod_{i,j} (1 - b_ij)^((1 - b_ij)/n) >= gamma_n exp(||E||_F^2/(2n)),

which is not implied by Schrijver's bound `per(B) >= prod_{i,j} (1 - b_ij)^(1 - b_ij)`: at
`J_n/n` the latter is `g(n)^n < gamma_n`.

### 2.6 The `m`-column form (proved, but with an implicit constant)

Fix `1 <= m <= n-1`, let `V = B[:, n-m+1..n]` (an `n x m` block), `w = V 1` its row sums, and
assume `w_s < 1` for all `s`. Let `l''_s(x) = sum_{j<=n-m} b_sj x_j`,

    q_{n-m}(x) = (d^m / dx_{n-m+1} ... dx_n) p_B(x, 0, ..., 0) = sum_{|S|=m} per(V[S,:]) prod_{s not in S} l''_s(x),
    P_V(y) = sum_{|S|=m} per(V[S,:]) prod_{s in S} y_s,          C_m(V) = inf_{y > 0} P_V(y) / prod_s y_s^(w_s).

**Lemma A_m.** `q_{n-m}(x) >= C_m(V) K(w) prod_{j<=n-m} x_j` for all `x > 0`; hence
`per(B) >= gamma_{n-m} C_m(V) K(w)`.

*Proof.* With `a_s = l''_s(x) > 0`, expanding the coefficient of `x_{n-m+1} ... x_n` in
`prod_s (a_s + sum_l V_sl x_{n-m+l})` gives the first formula for `q_{n-m}`, and
`q_{n-m}(x) = (prod_s a_s) * P_V(1/a)` (checked symbolically for `n = 4, m = 2` and numerically
for `m = 2, 3`, script 06 parts (iii) and (iv)). By definition of `C_m`,
`P_V(1/a) >= C_m(V) prod_s a_s^(-w_s)`, so `q_{n-m}(x) >= C_m(V) prod_s a_s^(1 - w_s)`, and
Step 2 of Lemma A (row weights `b_sj/(1 - w_s)`, `j <= n-m`, column sums 1) gives
`prod_s a_s^(1 - w_s) >= K(w) prod_j x_j`. The last claim is Lemma B for `q_{n-m}`, which is in
`Hom_+(n-m, n-m)`, non-zero, and H-stable by `m` applications of [G, Fact 4.9(2)]. QED.

`C_1 = 1` (AM-GM, attained at `y = 1`), so `m = 1` is Lemma A. At `B = J_n/n`,
`C_m = n!/((n-m)! n^m)` by Maclaurin's inequality and `C_m K(w) = gamma_n / gamma_{n-m}`, so
nothing is lost at the centre for any `m`. At `m = n` the statement is the tautology
`per(B) >= per(B)`. The constant `C_m(V)` is the capacity of a real polynomial in the row
variables and has no closed form for `m >= 2`; that is the obstacle recorded in Section 5.

## 3. What the theorem does for the application

`study/application.py` feeds `per(B) <= e^K gamma_n`. Theorem 2 in its exponential form gives
directly `||E||_F^2 <= 2nK`, so `lambda_2(B) >= 1 - sqrt(2nK)`. Script 06, part (v), runs the
fixed point of `application.py` with this bound and with `(e^K - 1)/c`, `c = 1/(2n)`:

    n    K bound (exp form)   margin    |alpha+beta| <=
    6    no fixed point
    7    1.2251e-02           1.09x     0.3005
    8    3.4635e-03           2.83x     0.1378
    9    1.1622e-03           6.49x     0.0748
   10    4.1410e-04          14.44x     0.0431
   15    3.0249e-06         825.35x     0.0035

`route-capacity-03-application.py` prints the same table for `c = 1/(2n)`, `1/n`, `1/4` at
`n = 5..20`: with `c = 1/(2n)` every `n >= 7` closes (margins `1.08x, 2.83x, 6.49x, ...` and
condition (N) holds with `|alpha + beta| <= 0.30` at `n = 7`). The two obligations of
`application.md` Section 5 (`lambda_2(A)` versus `lambda_2(B)`, and selecting the least fixed
point) are unchanged by this note.

## 4. Numerical checks and their output

All scripts use exact permanents (sum over permutations) and compute capacities by minimising
the convex function `u -> log P(e^u) - <w, u>` with BFGS and an analytic gradient.

1. `route-capacity-01-last-step.py` (output `route-capacity-01-output.txt`). Measures
   `c'(n) = min_{B, column} (cap(q)/g(n) - 1) / ||v - 1/n||^2`, the best single-column constant
   in the form `cap(q) >= g(n)(1 + c' ||v - 1/n||^2)`. Found: `0.750000` (n=3), `0.641975`
   (n=4), `0.638024` (n=5), each at a column uniform on a support of size `k` (`k = 2, 3, 3`),
   where the value is exactly `(g(k)/g(n) - 1)/(1/k - 1/n)`. The search missed `k = 4` at
   `n = 5`, where the same formula gives `0.599`; this is what led to Lemma A, whose constant
   `1/2` in Lemma C is the `n -> infinity` limit of these values.
2. `route-capacity-02-verify.py` (output `route-capacity-02-output.txt`). Lemma A as
   `min cap(q)/K(v) = 1.000000000000` over 63 matrices times `n` columns at `n = 3, 4, 5, 6`
   (equality cases exist, as predicted). Theorem 1 as `min per(B)/(gamma_{n-1} max_j K(col_j))
   = 1.0000011, 1.0000209, 1.0000113, 1.0009485` at `n = 3..6` over 400 matrices each; and the
   two weaker forms of Theorem 2, all `>= 1`. Also the local constants at `J_n/n + eps E`: the
   truth `n/(2(n-1))` against Theorem 1's `0.437, 0.291, 0.197, 0.159` at `n = 3..6`, which
   shows the factor lost by the single-column route near the centre.
3. `route-capacity-03-application.py` (output `route-capacity-03-output.txt`). Section 3.
4. `route-capacity-04-two-columns.py` (output `route-capacity-04-output.txt`). Lemma A_2 with the
   exact `C_2`: `min per(B)/(gamma_{n-2} C_2 K) = 1.000000000` at `n = 3..6` (equality cases
   exist). Two-column constant `c_2(n) = min (C_2 K/(g(n)g(n-1)) - 1)/(d_j + d_l)`: `0.375,
   0.578, 0.555, 0.554` at `n = 3..6`; at `n = 4` and `n = 6` the worst pair is the first two
   columns of the Knopp-Sinkhorn matrix `T_n` (a column uniform on `n-1` rows next to the column
   `(1/(n-1), (n-2)/(n-1)^2, ...)`), at `n = 3` it is `(I + C_3)/2`. Best-pair quadratic
   constant `(bound/gamma_n - 1)/||E||_F^2`: `0.250, 0.333, 0.288, 0.228` at `n = 3..6`,
   against `1/n = 0.333, 0.250, 0.200, 0.167`. These minima
   are over 112 matrices per `n` (random Sinkhorn scalings, sparse convex combinations of
   permutation matrices, and the structured matrices), so they are upper bounds on the true
   minima.
5. `route-capacity-05-explicit-C2.py` (output `route-capacity-05-output.txt`). The explicit
   entropy-dual lower bound `L` for `C_2` (a one-sided feasible `lambda`) is too weak: the
   constant it yields is negative at `n = 4, 5, 6`, although `L = C_2` exactly at the
   Knopp-Sinkhorn pair.
6. `route-capacity-06-step-checks.py` (output `route-capacity-06-output.txt`). Every algebraic
   step of Section 2, listed in Sections 2.1 to 2.6, plus the application table of Section 3.
7. `route-capacity-07-large-n.py` (output `route-capacity-07-output.txt`). Theorems 1 and 2 at
   `n = 7, 8, 9` with a vectorised Ryser permanent (checked against the permutation sum at
   `n = 4`), 600 matrices per `n` (Sinkhorn scalings of random matrices, sparse convex
   combinations of 2 to 5 permutation matrices, and segments from `J_n/n` to a permutation
   matrix): `min per(B)/(gamma_{n-1} max_j K(col_j)) = 1.0000057, 1.0000037, 1.0000253` and
   `min per(B)/(gamma_n exp(||E||_F^2/(2n))) = 1.0000058, 1.0000038, 1.0000257`. The smallest
   `(per/gamma_n - 1)/||E||_F^2` in these samples was `0.579, 0.569, 0.564`, far above the
   proved `1/(2n) = 0.071, 0.063, 0.056`; the sharp constants measured by `qvdw-constant.py`
   are `0.487` at `n = 7` and `0.497` at `n = 8`.

## 5. What remains unproved

1. **The single-column route cannot reach `1/n`.** Any bound of the form
   `per(B) >= gamma_{n-1} F(col_j)` must have `F(v) <= g(k)` when `v` is uniform on `k` rows,
   because Theorem 1 is an equality there (Section 2.3). Hence its quadratic constant is at most
   `(g(k)/g(n) - 1)/(1/k - 1/n)`, which tends to `1/2` (take `k = n-1`; `log g(k) = -1 + 1/(2k)
   + O(1/k^2)`). Dividing by `n` for the Frobenius norm gives `1/(2n)`, which is what Theorem 2
   has. So Q(1/n) and Q(1/4) need at least two columns at once.
2. **Q(1/n) reduces to one explicit inequality about a quadratic form.** With Lemma A_2 and the
   best pair of columns, `per(B) >= gamma_n (1 + ||E||_F^2 / n)` follows if for all probability
   vectors `v, v'` in `R^n` with `v + v' <= 1` entrywise,

       C_2(v, v') K(v + v') >= g(n) g(n-1) ( 1 + (1/2) ( ||v - 1/n||^2 + ||v' - 1/n||^2 ) ),

   where `C_2(v, v') = inf_{y > 0} sum_{r != r'} v_r v'_{r'} y_r y_{r'} / prod_s y_s^(v_s + v'_s)`.
   Numerically the left side exceeds the right with `1/2` replaced by `0.55` at `n = 4, 5, 6`
   (item 4 of Section 4). `C_2` is a capacity: `log C_2` is the maximum of
   `sum lambda_{rr'} log(v_r v'_{r'} / lambda_{rr'})` over distributions `lambda` on ordered
   pairs `r != r'` whose margins satisfy `lambda_{r.} + lambda_{.r} = v_r + v'_r`. The natural
   explicit choice of `lambda` is not good enough (item 5 of Section 4), and the optimum is a
   Sinkhorn-type scaling with no closed form. A proof would need either a better explicit
   `lambda`, or a quantitative convexity argument for `t -> log P(e^t) - <v + v', t>` that
   controls the drop from `t = 0` (value `1 - <v, v'>`) to its minimum by less than the gain
   in `K`. Neither is done here.
3. **Q(1/4).** Even with item 2 the constant is about `1.1/n`. Reaching a constant independent of
   `n` through this route means Lemma A_m with `m` of order `n` and an explicit lower bound for
   `C_m(V)`; for `m = n` that is the original problem. No other idea was tried, in line with the
   assignment.
4. **Lemma A_m for rows with `w_s = 1`.** Lemma A_m is stated under `w_s < 1` for all `s`. For
   `m = 1` the degenerate case is handled in Lemma A (Case 1); for `m >= 2` it is not written
   out, since Lemma A_m is not used in the proved theorems.

## Follow-up: pushing the constant to 1/n

Started 2026-09-04 (coordinator request). Target: `per(B) >= gamma_n exp(a ||E||_F^2)` with
`a >= 1/n`; only `n = 7` is in doubt for the application (n = 5, 6 are proved by certificates,
`n >= 8` closes with `a = 1/(2n)` even with the measured `lambda_2(A)` versus `lambda_2(B)` gap).
Theorem R's `lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2})`, `D_r, D_c` the row and column
sum diagonals of `A` (Theorem R, Lemma 3 of the sibling attack).

### State of the analysis (nothing below is proved unless it says so)

1. **The single-column route is capped near `0.6/n`, even with the exact `K`.** Proved fact:
   Theorem 1 is an equality at the sparse uniform columns for every completion, so any bound
   `per >= gamma_{n-1} F(col)` has `F <= g(k)` there; the ratio `log(g(k)/g(n))/(1/k - 1/n)` is
   at most `2 log(e/2) = 0.614` (at `k = 2`, `n -> infinity`) and tends to `1/2` for `k = n-1`.
   Near `J_n/n` the exact `K` gives `(n/(2(n-1))) d_j`, and `max_j d_j = ||E||^2/n` when all
   columns deviate equally. So no single-column statement reaches `a = 1/n`.

2. **The two-column route needs `c_2 >= 1/2` exactly, and `1/2` is the local boundary.** With
   `v = 1/n + delta`, `v' = 1/n + delta'`: the value of the `C_2` objective at `y = 1` is
   `1 - <v, v'> = 1 - 1/n - <delta, delta'>`, and `C_2` is at most that. Expanding
   `K(v + v')` exactly (`phi''(2/n) = n/(n-2)`), the quadratic form in `(delta, delta')` of
   `C_2 K / (g(n) g(n-1)) - 1` is at most
   `(n/(2(n-2))) (|delta|^2 + |delta'|^2) + (n/((n-1)(n-2))) <delta, delta'>`, whose minimum
   ratio to `|delta|^2 + |delta'|^2` is `n/(2(n-1))` at `delta' = -delta` (there the gradient
   of the `C_2` objective at `y = 1` is second order, so `C_2 = 1 - <v,v'> + O(delta^4)`). For
   `delta' = t delta`, `t != -1`, the drop of `C_2` below `1 - <v,v'>` is first order in
   `G = -(delta + delta')/(n-1)`, about `|G|^2 / (2 mu)` with `mu` about `2(n-2)/(n(n-1))`
   the Hessian floor on `1^perp`, i.e. about `|delta + delta'|^2 / (4n)`; the local `c_2` at
   `t = 0` is then about `n/(2(n-2)) - 1/(4n)` and at `t = 1` larger. So the local two-column
   constant is `n/(2(n-1))` (`0.583` at `n = 7`), consistent with the measured global `0.55`.
   Proving `c_2 >= 1/2` for all `(v, v')` needs a global lower bound on the capacity `C_2`;
   the one-sided entropy-dual `lambda` fails (Section 4, item 5), and the optimal `lambda` is
   an implicit Sinkhorn-type scaling. Not done.

3. **A third route that fits the application's regime (most promising, not finished).** In
   the application `per(B) <= e^K gamma_n` with `K < log(m_7/gamma_7) = 0.0133`, so Theorem 2
   already forces `||E||_F^2 <= 2nK < 0.186` at `n = 7`. On that region a local expansion with
   explicit remainder may give a much better constant than `1/n`. Exact expansion (proved in
   the sibling unit and re-derived here): `per(J/n + E)/gamma_n = sum_k alpha_k P_k(E)`,
   `alpha_k = n^k (n-k)!/n!`, `P_k(E) = sum_{|S|=|T|=k} per(E[S,T])`, with `P_0 = 1`,
   `P_1 = 0`, `P_2 = ||E||^2/2`, `P_3 = (2/3) sum_ij e_ij^3` (Moebius inversion over set
   partitions; only partitions with all blocks of size `>= 2` survive because row and column
   sums of `E` vanish). Key observation: `e_ij >= -1/n` because `b_ij >= 0`, so the negative
   part of the cubic term is bounded by `alpha_3 (2/3) sum_{e<0} |e|^3 <= (2n/(3(n-1)(n-2)))
   ||E||^2 = 0.156 ||E||^2` at `n = 7`, a quadratic (not cubic) loss, leaving
   `n/(2(n-1)) - 0.156 = 0.427` before the `k >= 4` terms. The `k >= 4` terms are the open
   part: the crude bound `|P_k| <= C(n,k)^2 ||E||^k` is useless (`3500 ||E||^4` at `k = 4`);
   the partition formula `24 P_4 = 36 sum e^4 - 18 sum_i r_i^2 - 18 sum_j c_j^2 + 3 ||E||^4
   + 6 tr((E E^T)^2)` (`r_i, c_j` the squared row and column norms; derived, NOT yet checked
   numerically) gives `|alpha_4 P_4| <= 9.6 ||E||^4 <= 1.8 ||E||^2` on the region, still too
   big; sharper structure (signs, `sum_i r_i^2 <= ||E||^4` is far from tight under zero
   margins) and the `k = 5, 6, 7` terms remain. If this closes, the deliverable would be:
   for all doubly stochastic `7 x 7` `B` with `||E||_F^2 <= 0.186`,
   `per(B) >= gamma_7 (1 + a' ||E||_F^2)` with explicit `a'` near `0.4`, which combined with
   Theorem 2 is exactly what the fixed point needs.

4. **Averaging over columns (coordinator's route 2).** Any bound
   `per >= gamma_n prod_j (K(col_j)/g(n))^(theta_j)` must have `sum_j theta_j <= 1` in the
   worst case, because at `(I + C_3)/2` the geometric mean with exponent `1/n` is already an
   equality (`per/gamma_3 = 9/8 = (K/g(3))` for every column). So a multiplicative average
   cannot beat `1/n` per column in general; the gain has to come from a genuinely two-column
   object (`C_2`) or from the regime restriction of item 3.

5. **Route 3 probes (script `route-capacity-11-local-remainder.py`, output
   `route-capacity-11-output.txt`).** The `P_4` partition formula of item 3 is now verified
   numerically (`n = 4, 5, 6`, agreement to 1e-10), and so is `P_3 = (2/3) sum e^3`. At `n = 7`
   on the region `||E||_F^2 <= 2 n log(m_7/gamma_7) = 0.1861`: over 2307 sampled doubly
   stochastic matrices and 12 Nelder-Mead minimisations restricted to the region, the smallest
   `(per/gamma_7 - 1)/||E||^2` is `0.482` (sampling) and `0.485` (minimisation), the cubic
   term `alpha_3 (2/3) sum e^3 / ||E||^2` is at least `-0.108`, and the whole `k >= 4` tail
   `sum_{k>=4} alpha_k P_k(E) / ||E||^2` lies in `[-0.0007, 0.0877]`. So on this region the
   true constant is about `0.48`, more than three times `1/n`, and the tail is negligible.

   Partial rigorous accounting on the region (`n = 7`, `K_0 = log(m_7/gamma_7) = 0.01330`):
   by Theorem 1 with Lemma C applied to every column and every row,
   `d_j, d'_i <= 2 K_0 = 0.0266`, hence `max |e_ij| <= 0.163`, `sum_i r_i^2 <= 0.0266 ||E||^2`,
   `sum_j c_j^2 <= 0.0266 ||E||^2` (`r_i, c_j` squared row and column norms) and
   `||E||^2 <= 0.1861`. Then: cubic term `>= -(2n/(3(n-1)(n-2))) ||E||^2 = -0.156 ||E||^2`
   (proved: `e_ij >= -1/n`); quartic term `alpha_4 P_4 >= -alpha_4 (18/24)(sum r_i^2 + sum
   c_j^2) >= -2.858 * 0.75 * 0.0532 ||E||^2 = -0.114 ||E||^2` (proved, from the verified
   formula, dropping the non-negative terms). Running total `0.583 - 0.156 - 0.114 = 0.313`
   before `k = 5, 6, 7`. To reach `a' >= 1/7 = 0.143` the `k = 5, 6, 7` terms must be shown
   `>= -0.17 ||E||^2` on the region; numerically they are about `10^-3 ||E||^2`. Plan: the
   Moebius expansion `P_k = (1/k!) sum_{pi, rho} mu(0,pi) mu(0,rho) F(pi, rho)` over set
   partitions of `[k]` with all blocks of size `>= 2` (162 partitions at `k = 7`), with each
   diagram value `F` bounded through `|e_ij| <= 0.163`, row and column norms `<= 0.163`,
   `sum e^2 = ||E||^2` and Cauchy-Schwarz; enumerate and bound by computer, then check the
   resulting constant. Crude bounds that ignore the zero-margin cancellations (Cauchy-Schwarz
   over permutations, `|P_k| <= C(n,k)^2 ||E||^k`) are hopeless (`37 ||E||^2` at `k = 4`).

### RESUME FROM HERE (superseded by the "Two-column theorem" section below; Route 3 dropped)

Next steps, in order: (a) DONE: `P_4` formula verified (item 5). (b) Write
`route-capacity-12-diagrams.py`: enumerate the Moebius expansion of `P_5, P_6, P_7` for
zero-margin `E`, verify each against direct sub-permanent sums at `n = 7` on random `E`, then
bound the negative part of `alpha_k P_k` on the region by an explicit multiple of `||E||^2`
using the regime constants of item 5; if the `k = 5, 6, 7` total is `>= -0.17 ||E||^2`, state
and prove Proposition (n = 7): `per(B) <= e^{K_0} gamma_7` implies `per(B)/gamma_7 >= 1 + a'
||E||_F^2` with the explicit `a'`, and rerun the fixed point with `||E||^2 <= (e^K - 1)/a'`.
(c) if (b) fails, fall back to the explicit bound on
`|lambda_2(B) - lambda_2(A)|` in terms of `|(u; v)|` (Weyl on
`D_r^{-1/2} A D_c^{-1/2} - B` with `B = D_1 A D_2` the Sinkhorn scaling, `D_1, D_2` close to
`D_r^{-1/2}, D_c^{-1/2}` by the margins), which the coordinator asked for.

## Two-column theorem

Written 2026-09-04, after the coordinator narrowed the target to

    (V1)   per(B) >= gamma_n exp( (d_j + d_l) / 2 )   for every pair of columns j != l,

which gives `a = 1/n`. Scripts `route-capacity-21-two-column-claims.py` and
`route-capacity-22-I2-direction.py`, outputs in the matching `-output.txt` files. Notation:
`v = col_l`, `v' = col_j`, `delta = v - 1/n`, `delta' = v' - 1/n`, `d = |delta|^2`,
`d' = |delta'|^2`, `w = v + v'`, `s = delta + delta'`, `t = delta - delta'`, `gg = g(n) g(n-1)`,
and `C_2(v, v') = inf_{y > 0} P(y) / prod_s y_s^(w_s)` with
`P(y) = sum_{r != r'} v_r v'_{r'} y_r y_{r'}` (Section 2.6).

### 1. Outcome in one paragraph

**Not proved.** What is proved: (V1) follows from the pure two-column inequality (I2) below
(Lemma A_2, Section 2.6); the sequential versions of (I2) are false, so any proof must treat
the two columns symmetrically; (I2) holds in three special cases (Section 4); and the exact
optimiser of `C_2` is a two-scalar fixed point with an explicit formula (Section 3), which is
the "one-variable optimisation after symmetry" of the coordinator's hint (i). What is measured:
(I2) holds with `a' = 1/2` at `n = 4, 5, 6, 7` in every family tried, with the ratio tending to
1 only as `d + d' -> 0`. What is proved about `a'`: only the trivial `a' = 1/4`
(`max(d_j, d_l) >= (d_j + d_l)/2` in Theorem 2). The remaining gap is one explicit inequality
about a quadratic form, stated in Section 5 with the reasons the standard tools fail.

### 2. Which intermediate statement is true (script 21)

Peel `x_l` first, then `x_j`; `q_1 = q_{n-1}`, `q_2 = q_{n-2}` as in Section 2.6. Five
statements, each implying (V1) when combined with Gurvits' theorem for `q_2`:

    I1 : cap(q_2) >= gg exp((d + d')/2)
    I2 : C_2(v, v') K(v + v') >= gg exp((d + d')/2)          (implies I1 by Lemma A_2)
    I3 : cap(q_2) >= g(n-1) exp(d'/2) cap(q_1)                (with Lemma A would imply I1)
    I4 : cap(q_2) >= g(n-1) exp(d'/2) K(v)

Minimum ratios (left over right) over 62 matrices times all ordered column pairs:

    n=4: V1 1.002476   I1 1.000941   I2 1.000682   I3 0.967445   I4 0.976114
    n=5: V1 1.002970   I1 1.000723   I2 1.000487   I3 0.984246   I4 0.998439

So I3 and I4 are **false**: the second peeled column cannot be charged a factor
`exp(d'/2)` on top of whatever the first one gave. The gain of a pair is a joint quantity.
I2 is the statement to prove; its tight cases are pairs near `(1/n, 1/n)`.

### 3. What is proved about `C_2`

**Proposition 3.1 (stationarity).** Let `v, v'` be probability vectors with `v + v' <= 1` and
`w = v + v'` in the relative interior of the Newton polytope of `P` (true whenever every
`w_s < 1` and the bipartite support is connected; otherwise argue by a limit). Then
`F(t) = log P(e^t) - <w, t>` is convex, coercive on `1^perp`, and its minimiser `y = e^t`
satisfies, for every `s`, with `A = <v, y>`, `A' = <v', y>`, `P = P(y)`,

    2 v_s v'_s y_s^2 - (v_s A' + v'_s A) y_s + w_s P = 0,

and `y_s` is the smaller root: `y_s = 2 w_s P / (beta_s + sqrt(beta_s^2 - 8 v_s v'_s w_s P))`,
`beta_s = v_s A' + v'_s A`. Hence `log C_2 = -log P - sum_s w_s log(2 w_s) + sum_s w_s log(
beta_s + sqrt(beta_s^2 - 8 v_s v'_s w_s P))`, a function of the two scale-free scalars
`A'/A` and `P/(A A')`.

*Proof.* `d/dy_s [log P - sum w log y] = (v_s A' + v'_s A - 2 v_s v'_s y_s)/P - w_s/y_s`;
multiply by `y_s P`. Convexity: `log P(e^t)` is a log-sum-exp of linear forms. The root is
the smaller one because at `v = v' = 1/n` the roots are `y = 1` and `y = n - 1` and the
minimiser is `y = 1` (Maclaurin), and the smaller root is the continuous branch. QED.

Equivalently, with `rho = v y / A`, `rho' = v' y / A'` (the tilted columns), the
minimiser is characterised by the margin equations
`rho_s (1 - rho'_s) + rho'_s (1 - rho_s) = w_s (1 - <rho, rho'>)`, and
`log C_2 = D(v || rho) + D(v' || rho') + log(1 - <rho, rho'>)`; the optimal dual weights
are `lambda_{rr'} = rho_r rho'_{r'} / (1 - <rho, rho'>)`. Any pair `(rho, rho')` satisfying
the margin equations gives a lower bound on `log C_2` (weighted AM-GM); the one-sided choice
`rho' = v'` is Section 4 item 5's `L1` and is too weak, and the true pair is a common tilt of
`v` and `v'`, which no explicit choice reproduces.

**Proposition 3.2 (symmetric decomposition).** With `m = (v + v')/2`, `e = (v - v')/2`
(`sum e = 0`),

    P(y) = [ (sum m y)^2 - sum m^2 y^2 ] - [ (sum e y)^2 - sum e^2 y^2 ],

because the cross terms `sum_{r != r'} (e_r m_{r'} - m_r e_{r'}) y_r y_{r'}` cancel by
antisymmetry. At `y = 1` this reads `P(1) = 1 - |m|^2 + |e|^2 = 1 - <v, v'>`.

**Proposition 3.3 (a valid but useless explicit bound).** `W(A, A', P)` of Proposition 3.1 is
increasing in `A, A'` and decreasing in `P`, and at the optimum `P <= A A'`; so, normalising
`A = 1`, `log C_2 >= inf_theta W(1, theta, min(theta, P_max(theta)))` with
`P_max(theta) = min_s beta_s^2/(8 v_s v'_s w_s)`. This one-variable bound is proved but loses
too much: at `v = v' = 1/n`, `n = 7`, it gives `0.684` against the true `C_2 = 6/7`. The loss
is the replacement of `P/(AA') = 1 - <rho, rho'>` by 1; a tight upper bound on `P/(AA')` is
equivalent to controlling the optimal tilt, which is the whole problem.

### 4. Where (I2) is proved

1. **Disjoint supports** (`v_s v'_s = 0` for all `s`). Then `P(y) = (sum v y)(sum v' y)` and
   `C_2 = 1` by AM-GM. Lemma C's argument for `phi` at `2/n` gives
   `log K(w) >= (n-2) log((n-2)/n) + |w - 2/n|^2 / 2`, and `|w - 2/n|^2 = d + d' + 2 <delta,
   delta'> = d + d' - 2/n` since `<v, v'> = 0`. With `(n-2) log((n-2)/n) = log gg - log(1 -
   1/n)`, (I2) reduces to `-log(1 - 1/n) - 1/n >= 0`, which holds.
2. **Both columns uniform on their supports with the same support size** is contained in 1
   or in the next item.
3. **`|e_s| = 1/n` for all `s` with `m = 1/n`** (so `v = 2/n` on half the rows and `v' = 2/n`
   on the other half): the gradient of `F` at `t = 0` vanishes and `C_2 = 1`; this is item 1.
4. **Local statement.** Expanding to second order at `v = v' = 1/n` (the coordinator's
   Follow-up item 2 and script 22): with the exact `phi''(2/n) = n/(n-2)` and the first-order
   drop of `C_2` below `P(1)` (gradient `G = -s/(n-1) + O(delta^2)`, Hessian floor about
   `2(n-2)/(n(n-1))` on `1^perp`), `log(C_2 K/gg) - (d + d')/2` equals
   `|t|^2/(4(n-1)) + |s|^2 (2n^2 + n - 2)/(4n(n-1)(n-2)) + O(delta^3)`, both coefficients
   positive. So (I2) holds in a neighbourhood of `(1/n, 1/n)` (size not made explicit), and
   its only second-order-tight direction is `s = 0`, i.e. `v' = 2/n - v`, where `K` gives
   nothing and the whole gain is `1 - <v, v'> = 1 - 1/n + |delta|^2`.

### 5. The gap, stated exactly, and why the standard tools fail

**Gap.** For all probability vectors `v, v'` in `R^n` with `v + v' <= 1`:

    C_2(v, v') K(v + v') >= g(n) g(n-1) exp( a' (|v - 1/n|^2 + |v' - 1/n|^2) ),

with `a' = 1/2` (gives V1 and `a = 1/n`), or any `a' >= 0.36` at `n = 7` (enough for the
application: `a = 2a'/n`). Numerically (script 22, `n = 4..7`, 300 pairs in each of three
families: the tight direction `v' = 2/n - v`, the `n = 7` region `d, d' <= 0.0266`, and global
Dirichlet and sparse pairs) the ratio is `>= 1` for `a' = 1/2` in every case; it equals 1
exactly at `v = v' = 1/n` (for every `a'`) and is above 1 at every other sampled pair, the
smallest values being `1.000017` (tight direction, `n = 7`, `d = 0.0001`) for `a' = 1/2` and
`1.000045` for `a' = 0.36`.

**Why it is not proved here.**
- *Convexity plus a Hessian floor.* `min F >= F(0) - |G|^2/(2 mu)` needs `Hess F >= mu` on a
  ball of radius `R >= 2|G|/mu` around `0`. `Hess F(t)` is the covariance of `e_r + e_{r'}`
  under `lambda_t`, and the only lower bounds I can prove go through the smallest entry of a
  tilted column; a column of the `n = 7` region may have an entry as small as `0.02`, which
  makes `mu` about thirty times smaller than its typical value `2/n` and the condition
  `R >= 2|G|/mu` unsatisfiable. For disjoint supports the Hessian is genuinely degenerate
  (`P/y^w` is constant along `y = 1 + c e`), so a uniform `mu` cannot exist in general.
- *Explicit dual weights.* Every explicit feasible `lambda` I tried (one-sided, symmetric
  `rho = rho'`, their mixtures) is exact in one regime and loses a first-order amount in
  another; the symmetric choice is `-infinity` as soon as one column has a zero. The optimal
  `lambda` is a common tilt of both columns (Proposition 3.1) and has no closed form.
- *Second-order expansion on the region.* The tight direction has relative margin
  `1/(n-1)` (i.e. `1/6` at `n = 7`), while on the region the relative entry deviations reach
  100 percent, so cubic remainders are not small against the quadratic term.
- *Route 3 (Taylor terms of `per` itself)* was dropped at the coordinator's instruction: the
  cancellation is between diagrams, not within them.

**What would close it.** A "drop lemma" `C_2(v, v') >= (1 - <v, v'>) exp(-c_n |s|^2 -
c'_n Q(delta, delta'))` with `Q` fourth order and explicit `c_n <= 0.15` at `n = 7`, combined
with the exact `K` (Lemma C with `phi''(2/n) = n/(n-2)` on the coordinates above `2/n`),
gives `a' >= 0.36` at `n = 7` by the arithmetic of item 4 above. Proving the drop lemma
needs a convexity argument for `F` that survives small entries and degenerate directions;
one candidate is the two-scalar reduction of Proposition 3.1, where the whole problem is a
fixed point in `(A'/A, P/(AA'))` and a monotonicity argument in those two scalars, with
bounds sharper than `P <= AA'`, would give an explicit inequality.

### 6. Statements proved in this section, for the record

- (V1) is implied by (I2) through Lemma A_2 and Gurvits' theorem for `q_{n-2}`.
- (I3), (I4) are false (counterexamples in `route-capacity-21-output.txt`).
- Propositions 3.1, 3.2, 3.3 and Section 4 items 1 to 3.
- `per(B) >= gamma_n exp((d_j + d_l)/4)` for every pair, from Theorem 2 (this is `a' = 1/4`).

## Drop lemma via the two-scalar reduction

Written 2026-09-04 (final push). Scripts `route-capacity-31-drop-budget.py` to
`route-capacity-35-hessian-check.py`, outputs in the matching `-output.txt` files. Target: (I2) with
`a' = 0.36` on the `n = 7` region `R_7 = {(v, v') : d, d' <= 0.0266}`; notation of the
"Two-column theorem" section, plus `m = w/2`, `theta = A'/A`, `p = P/(A A')`, `Phi(tau) = log
P(e^tau) - <w, tau>`, `tau*` a minimiser of `Phi`, `rho, rho'` the tilted columns at `tau*`,
`h_s = 2 v_s v'_s / w_s`, `G_s = w_s (hbar - h_s)/(1 - hbar) = grad Phi(0)_s`.

### 1. Outcome in one paragraph

**Not proved.** The route reduces (I2') on `R_7` to one explicit inequality (★) in `(v, v')`,
Section 3, plus one hypothesis (T) on the minimiser, Section 5. Everything else is proved:
a base-point convexity bound that needs only a crude Hessian floor (Lemma E1), the exact Hessian
of `Phi` (Lemma E2) and an explicit floor for it (Lemma E3), the scalar bound `p* <= 1 - hbar`
(Lemma E4), the root formula for the minimiser (Proposition 3.1 with the vertex condition made
explicit, Lemma E5). Numerically on `R_7`, including its corner: the bound of Lemma E1 uses at
most 44 percent of the budget of (I2') at `a' = 0.36`, the fourth-order correction less than 1
percent, the Hessian floor along every segment is `>= 1.16`, the tilted entries stay `<= 0.37`
(the root formula needs `< 1/2`), and `|theta* - 1| <= 0.028`, `p* - (1 - hbar) in [-0.022, 0]`
(the coordinator's step 2 ranges). What is missing is (T): an a priori bound on the oscillation
of the optimal tilt that holds uniformly on `R_7`, and a rigorous (interval or grid) verification
of (★).

### 2. Proved lemmas

**Lemma E1 (base-point convexity).** Let `Phi` be convex on `R^n` with `Phi(tau + c 1) =
Phi(tau)`, `tau*` a global minimiser, `tau~` any point, `g = grad Phi(tau~)` (so `<g, 1> = 0`),
`N_m(u)^2 = Var_m(u) = min_c sum_s m_s (u_s - c)^2`, `|g|_* = (sum_s g_s^2 / m_s)^(1/2)` its dual
seminorm. Suppose that for some `R, kappa > 0` and every `tau` with `osc(tau - tau~) <= R` (the
oscillation `max - min` of the vector) and every `u`, `u^T Hess Phi(tau) u >= kappa N_m(u)^2`.
Then, with `u = tau* - tau~`, either `osc(u) <= R` and

    Phi(tau*) >= Phi(tau~) - |g|_*^2 / (2 kappa),      N_m(u) <= 2 |g|_* / kappa,

or `osc(u) > R`, in which case the same lower bound holds provided `R N_m(u) / osc(u) >= 2
|g|_* / kappa`.

*Proof.* `h(t) = Phi(tau~ + t u)` is convex, `h'(0) = <g, u> >= -|g|_* N_m(u)`, and `h''(t) >=
kappa N_m(u)^2` while `osc(t u) <= R`. If `osc(u) <= R`: `h(1) >= h(0) - |g|_* N_m(u) + (kappa/2)
N_m(u)^2 >= h(0) - |g|_*^2/(2 kappa)`, and `h(1) <= h(0)` gives `N_m(u) <= 2|g|_*/kappa`. If
`osc(u) > R`, put `t_R = R/osc(u)`: `h(t_R) >= h(0) - |g|_* t_R N_m(u) + (kappa/2) t_R^2 N_m(u)^2
>= h(0)` under the proviso, and convexity `h(t_R) <= (1 - t_R) h(0) + t_R h(1)` gives `h(1) >=
h(0)`. QED.

The proviso is exactly where light coordinates (small `m_s`) hurt: a direction concentrated on
them has small `N_m` and large `osc`. This is the obstacle recorded in Section 5.

**Lemma E2 (exact Hessian).** For `tau in R^n`, `y = e^tau`, `rho = v y/<v,y>`, `rho' = v'
y/<v',y>`, `rhobar = (rho + rho')/2`, `q = <rho, rho'>`, and every `u` with `<rhobar, u> = 0`:

    u^T Hess Phi(tau) u = [ 2 sum_s rhobar_s u_s^2 - 2 <rho,u>^2 - 4 sum_s rho_s rho'_s u_s^2 ] / (1 - q)
                          - 4 ( sum_s rho_s rho'_s u_s )^2 / (1 - q)^2.

*Proof.* `Hess Phi(tau)` is the covariance of `e_r + e_{r'}` under `lambda(r, r') = rho_r
rho'_{r'} / (1 - q)`, `r != r'`. With `E_lambda F = [sum_{r,r'} rho_r rho'_{r'} F(r,r') - sum_s
rho_s rho'_s F(s,s)]/(1-q)`, `<rho,u> + <rho',u> = 0` gives `E[u_r + u_{r'}] = -2 sum_s rho_s
rho'_s u_s/(1-q)` and `E[(u_r + u_{r'})^2] = [2 sum rhobar u^2 - 2 <rho,u>^2 - 4 sum rho rho'
u^2]/(1-q)`. QED. (Script 35 checks the closed form against the covariance matrix at 3000 random
`(v, v', tau, u)`: relative error `1e-12`; it also checks the floor of Lemma E3 and `V >=
e^{-osc} Var_m(u)` in every sample.)

**Lemma E3 (Hessian floor).** With `V = sum_s rhobar_s u_s^2` (for `<rhobar,u> = 0`), `chi = sum_s
(rho_s - rho'_s)^2 / (2 (rho_s + rho'_s))`, `Hm = max_s 2 rho_s rho'_s/(rho_s + rho'_s)`, `Xi =
Var_rhobar( 2 rho rho'/(rho + rho') )`:

    u^T Hess Phi(tau) u >= V * { [2 (1 - chi) - 4 Hm] / (1 - q) - 4 Xi / (1 - q)^2 },

and `V >= e^{-osc(tau)} Var_m(u)`. *Proof.* Cauchy-Schwarz gives `<rho,u>^2 = <(rho -
rho')/2, u>^2 <= chi V`, `sum rho_s rho'_s u_s^2 = sum_s h^rho_s rhobar_s u_s^2 <= Hm V`, and, since
`sum rhobar_s u_s = 0`, `sum rho_s rho'_s u_s = sum_s (h^rho_s - mean) rhobar_s u_s <= (Xi V)^(1/2)`.
For the last claim, `Var_m(u) <= sum m_s u_s^2 <= max_s (m_s/rhobar_s) V` and `rhobar_s/m_s = y_s
(v_s/A + v'_s/A')/w_s >= y_s / max_r y_r`. QED. At `v = v' = 1/n` the floor is `2(n-2)/(n-1)
= 1.667`, the exact value.

**Lemma E4 (`p* <= 1 - hbar`).** `C_2 = P(y*)/y*^w = p* e^{D(v||rho) + D(v'||rho')}` (because
`prod y_s^{v_s} = A e^{-D(v||rho)}`), so `p* <= C_2 <= P(1) = 1 - hbar`. QED.

**Lemma E5 (root formula, vertex condition).** `P` is affine in each `y_s`; at the minimiser,
`y*_s B_s = w_s P*` with `B_s = dP/dy_s = v_s A'(1 - rho'_s) + v'_s A (1 - rho_s)`, which is the
quadratic of Proposition 3.1. `y*_s` is its smaller root if and only if `1/rho*_s + 1/rho'*_s
>= 4`, in particular whenever `max(rho*_s, rho'*_s) <= 1/2`. Given the smaller root,
`-<G, tau*> = eta(theta*, p*)` with `eta(theta, p) = sum_s G_s [ log(beta_s/w_s) + log(1 +
sqrt(1 - x_s)) ]`, `beta_s = v_s theta + v'_s`, `x_s = 8 v_s v'_s w_s p theta / beta_s^2`
(`sum G_s = 0` removes the common factor `2 p theta`). *Proof.* The vertex of `y -> y (beta_s -
2 v_s v'_s y)` is `beta_s/(4 v_s v'_s)`, and `y_s <= vertex` is `4 <= A'/(v'_s y_s) + A/(v_s
y_s)`. QED. Also `eta(1, p)` is increasing in `p` (Chebyshev: `d/dp log(1 + sqrt(1 - 4 h p)) =
-2h/(q(1+q))` is decreasing in `h`, and `sum_s w_s (h_s - hbar) = 0`). Numerically (script
32, 700 pairs) `eta(theta*, p*) = -<G, tau*>` to `1e-9`, no root mismatch, and `eta(1, p)` is
monotone in every sample.

### 3. The reduction

Fix `(v, v')` in `R_7`. Base point: `p_ref = min(1 - hbar, 1/(4 h_max))`, `y~_s = 2 p_ref/(1 +
sqrt(1 - 4 h_s p_ref))` (the `theta = 1` smaller root), `tau~ = log y~` centred. Then, by Lemma
E1 with `u = tau* - tau~`, `g = grad Phi(tau~)` (explicit: `g_s = [rho~_s (1 - rho~'_s) +
rho~'_s (1 - rho~_s)]/(1 - q~) - w_s` with `rho~, rho~'` the tilts at `tau~`):

    log C_2 = Phi(tau*) >= Phi(tau~) - |g|_*^2 / (2 kappa)                                  (E)

whenever (T) below holds, so that Lemma E1 applies with an explicit `kappa`. Since `Phi(0) =
log(1 - hbar)`, (I2') at `a' = 0.36` on `R_7` follows from the explicit inequality

    (★)   [ Phi(0) - Phi(tau~) ] + |g|_*^2 / (2 kappa)  <=  term1 + term3 - 0.36 (d + d'),

with `term1 = log((1 - hbar)/(1 - 1/7))`, `term3 = sum_s phi(w_s) - 7 phi(2/7)`, `Phi(0) -
Phi(tau~) = log(1 - hbar) - log P(y~) + <w, tau~>`. Both sides of (★) are explicit elementary
functions of `(v, v')`; `kappa` enters only through the fourth-order term.

**Hypothesis (T).** There are `R` and `kappa > 0`, valid on all of `R_7`, such that the floor of
Lemma E1 holds on `{osc(tau - tau~) <= R}` and the proviso holds for `u = tau* - tau~`. By Lemma
E3 this follows from a bound `osc(tau*) <= R_0` together with bounds on the tilted entries along
the segment (which give `chi, Hm, Xi, q` and hence `kappa`), and the proviso needs the direction
`tau* - tau~` not to be concentrated on light coordinates.

### 4. Numerical verification on `R_7`

- Script 31 (1200 pairs, four families incl. holes): `max |tau*|_inf = 0.207`, `theta* - 1 in
  [-0.025, 0.028]`, `p* - (1 - hbar) in [-0.0159, -0.00000]`, `max drop/Var_w(h) = 1.049`, and the
  true drop uses at most `0.362` of the budget `term1 + term3 - 0.36(d + d')`.
- Script 32 (700 pairs): `max -<G,tau*>/B = 0.697`, `max eta(1, p_up)/B = 0.706` with `p_up =
  min(1 - hbar, 1/(4 h_max))`, the `theta`-correction `eta(theta*,p*) - eta(1,p*)` at most `3.5e-4`
  (`3.6` percent of `B`).
- Script 33 (600 pairs): `max [Phi(0) - Phi(tau~)]/B = 0.406`, `max corr/B = 0.0074` with the
  exact `kappa`, `min kappa = 1.201` along all segments `[tau~, tau*]`, `max |grad Phi(tau~)|_inf
  = 0.011`, `max |tau~ - tau*|_inf = 0.037`, so (★) holds with 59 percent room.
- Script 34 (400 corner pairs, `v_1, v'_1 in [0.27, 0.306]`): `max D~/B = 0.441`, `min kappa =
  1.158`, `p* <= 1/(4 h_max) - 0.058`, discriminant at the fixed point `>= 0.018`, `max tilted
  entry = 0.3705 < 1/2`, `|theta* - 1| <= 0.0072`. No sampled pair has `4 h_max (1 - hbar) > 1`;
  the extreme point `v = v' = (0.306, 0.1157 x 6)` has `4 h_max (1 - hbar) = 1.011`, and there
  `p_ref = 1/(4 h_max)` keeps `y~` defined.

So on `R_7` the explicit inequality (★) holds in every sample with the fourth-order term below
1 percent of the budget, and the hypotheses of Lemma E1 hold with `R = 0.5`, `kappa = 1`.

### 5. What remains

1. **(T), the a priori tilt bound.** Numerically `osc(tau*) <= 0.41` and tilted entries `<=
   0.37`. Every proof attempt fails in the same two places: (a) the only lower bounds I can
   prove for `V/Var_m` go through `min_s rhobar_s/m_s >= e^{-osc}`, and a light coordinate
   (`w_s` down to `0` on `R_7`) can carry an arbitrary tilt at negligible cost in `N_m`, so the
   proviso of Lemma E1 fails in that direction; (b) the crude root bounds `y_s in [w_s P/beta_s,
   2 w_s P/beta_s]` do not close a bootstrap (`Y <= 1.05/(1 - 0.34 Y)` has no solution below
   the trivial `Y <= 3.2`), because the factor 2 from `sqrt >= 0` is exact at the corner
   (double root). A remedy would be to eliminate light coordinates by partial minimisation
   (`Phi` is explicit in each `tau_s` separately, `P` being affine in `y_s`), which changes the
   form of the reduced function; not done.
2. **Rigorous check of (★).** (★) is a 12-dimensional inequality of elementary functions with
   59 percent room. It decomposes as coordinatewise sums in `(s_s, t_s)` plus three global
   scalars (`hbar`, `<v, y~ - 1>`, `<v', y~ - 1>`); a grid with Lipschitz margins over
   `(s_s, t_s)` for the global scalars in their intervals is the natural computer-assisted
   proof. Not done.
3. **The coordinator's step 3 as literally stated** (second-order expansion of `log C_2` in the
   two scalars) does not work: `d/dp` of the two-scalar function is `-n^2/((n-1)(n-2)) = -1.63`
   at the centre, so a first-order error in `p*` costs first order, while `p* - (1 - hbar) =
   (1 - hbar) <G, epsilon*> + ...` is second order in the tilt and needs the tilt to first order.
   Lemma E1 avoids this: the value is evaluated at an explicit base point, and the scalars are
   never needed to second order.

### 6. Statements proved in this section

Lemmas E1 to E5 and the monotonicity of `eta(1, p)`. The identities `h_s = m_s - e_s^2/m_s`,
`hbar = 1/n + (|s|^2 - |t|^2)/4`, `theta* - 1 = -<v - v', y* - 1>` (with `<v, y*> = 1`) and
`drop <= -<G, tau*>` are elementary. (I2') at `a' = 0.36` on `R_7` is reduced to (★) and (T);
neither is proved.
