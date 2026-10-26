# Lemma 2': the scaling cost against the scaling's own spectral gap

Written 2026-09-04. Scripts in this directory: `lemma2-prime-identity.py` (the two identities
and every inequality of the chain, to rounding), `lemma2-prime.py` (the statement over 2400
cases), `lemma2-prime-rigorous.py`, `lemma2-prime-sharp.py` and `lemma2-prime-rho.py` (three
bootstraps of increasing sharpness and their tables).

## 1. Why this lemma

Theorem R's Lemma 2 bounds the scaling cost `K = -log cap(A)` by
`(|u|^2 + |v|^2) / (2 theta_n lambda_2(A))`, where `lambda_2(A)` is the spectral gap of the
normalised bipartite Laplacian of `A` itself. The capacity route (`route-capacity.md`, Theorem 2)
bounds `lambda_2(B)` for the Sinkhorn scaling `B` of `A`, not `lambda_2(A)`. Comparing the two
gaps was obligation 1 of `application.md`. Measured, the difference is small
(`lambda2-comparison.py`: at most `0.030 sqrt(2nK)`), but any proof through Weyl and Pinsker
loses a factor of order one and kills `n = 7` and `n = 8`.

This lemma removes the comparison: it bounds `K` by `lambda_2(B)` directly.

## 2. Setting

`A` is a fully indecomposable non-negative `n x n` matrix with total sum `n`, row sums
`r = 1 - u`, column sums `c = 1 - v`, so `sum u = sum v = 0`. `B = D_1 A D_2` is its Sinkhorn
scaling, doubly stochastic with the same support. Write `l_1 = log d_1`, `l_2 = log d_2`,
`w_ij = l_1i + l_2j`, so `b_ij = a_ij e^{w_ij}`. The scaling is unique up to `l_1 -> l_1 + t`,
`l_2 -> l_2 - t`, which leaves `w` unchanged; fix it by `sum l_1 = sum l_2`, that is
`l = (l_1; l_2)` orthogonal to `(1; -1)`. Then

    K = -log cap(A) = sum_ij b_ij log(b_ij / a_ij) = sum_ij b_ij w_ij = sum_i l_1i + sum_j l_2j,

the last step because `B` is doubly stochastic. Let `lambda = lambda_2(B) = 1 - sigma_2(B)`,
`mu = |(u; v)|_2`, `Q = sum_ij b_ij w_ij^2`, `W = max |w_ij|` over the support of `B`, and

    psi(w) = (e^{-w} - 1 + w) / w^2,     chi(w) = (1 - e^{-w}) / w,     rho(w) = psi(w) / chi(w),

with `psi(0) = 1/2`, `chi(0) = 1`, `rho(0) = 1/2`. Since `psi(w) = int_0^1 t e^{-(1-t)w} dt` and
`chi(w) = int_0^1 e^{-(1-t)w} dt`, both are positive and decreasing. `rho` is increasing on
`[-1, 1]` (checked on a grid of step 0.05 in `lemma2-prime-rho.py`; `rho(-0.25) = 0.4792`,
`rho(0.25) = 0.5208`), and `rho(w) = 1/2 + w/12 + O(w^2)`.

## 3. Three exact identities

**(I)** `K = sum_ij b_ij w_ij^2 psi(w_ij)`.

*Proof.* Let `F(l) = sum_ij a_ij e^{l_1i + l_2j} - sum_i l_1i - sum_j l_2j`. `F` is convex; its
gradient is `(sum_j a_ij e^{w_ij} - 1)_i ; (sum_i a_ij e^{w_ij} - 1)_j`, which vanishes exactly
at the scaling `l*` because the rows and columns of `B` sum to 1; and its Hessian at `l` is the
weighted bipartite Laplacian of the matrix `(a_ij e^{w_ij})`, so `l^T H(l) l = sum_ij a_ij
e^{w_ij} w_ij^2`. Now `F(0) = sum a_ij = n` and `F(l*) = n - sum l*_1 - sum l*_2 = n - K`, so
`K = F(0) - F(l*)`. Along the segment `s l*`, `K = -int_0^1 grad F(s l*) . l* ds`, and
`grad F(s l*) = grad F(0) + int_0^s H(t l*) l* dt`; since `grad F(l*) = 0`,
`grad F(0) . l* = -int_0^1 l*^T H(t l*) l* dt`. Substituting and exchanging the order of
integration gives `K = int_0^1 t l*^T H(t l*) l* dt = sum_ij b_ij w_ij^2 int_0^1 t e^{-(1-t) w_ij}
dt`, because `a_ij e^{t w_ij} = b_ij e^{-(1-t) w_ij}`. QED

**(II)** `u_i = sum_j b_ij (1 - e^{-w_ij})` and `v_j = sum_i b_ij (1 - e^{-w_ij})`.

*Proof.* `u_i = 1 - sum_j a_ij = sum_j b_ij - sum_j b_ij e^{-w_ij}`; columns likewise. QED

**(III)** `l^T (u; v) = sum_ij b_ij w_ij^2 chi(w_ij)`.

*Proof.* From (II), `l^T (u; v) = sum_i l_1i u_i + sum_j l_2j v_j = sum_ij b_ij (l_1i + l_2j)
(1 - e^{-w_ij}) = sum_ij b_ij w_ij (1 - e^{-w_ij})`. QED

(I) and (II) hold to `6e-15` on every test matrix of `lemma2-prime-identity.py`; (III) follows
from (II) algebraically.

## 4. The chain

With `L_B = [[I, B], [B^T, I]]`, whose eigenvalues are `1 +/- sigma_k(B)` and whose kernel is
spanned by `(1; -1)`:

- **(A)** `Q = l^T L_B l >= lambda |l|^2`, since `l` is orthogonal to the kernel and every other
  eigenvalue is at least `1 - sigma_2 = lambda`.
- **(B)** From (I) and (III), `K / l^T(u; v) <= max rho(w_ij) =: rho_max` over the support, and
  from (III), `l^T(u; v) >= chi(W) Q` because `chi` is decreasing and `w_ij <= W`.
- **(C)** Hence `lambda |l|^2 <= Q <= l^T(u; v) / chi(W) <= |l| mu / chi(W)`, so
  `|l| <= mu / (lambda chi(W))`, and

      K <= rho_max l^T(u; v) <= rho_max |l| mu <= rho_max mu^2 / (lambda chi(W)).

- **(D)** `W <= |l_1|_inf + |l_2|_inf <= sqrt(2) |l| <= sqrt(2) mu / (lambda chi(W))`.

Each of (A) to (D) is checked on 1600 random near-doubly-stochastic matrices with a zero entry,
including ones whose scaling has gap down to `0.005` (`lemma2-prime-identity.py`). The statement
itself holds with room: `2 K lambda / mu^2 <= 0.877` over 2400 cases with margins up to 1.86
(`lemma2-prime.py`).

**Lemma 2'.** Let `W_0` be the least fixed point of `W = sqrt(2) mu / (lambda chi(W))`, when one
exists. Then

    K <= rho(W_0) mu^2 / ( lambda chi(W_0) ),

with `rho(W_0) = max(rho(W_0), rho(-W_0))`, which is `rho(W_0)` for `W_0 <= 1`.

*Proof.* The map `W -> sqrt(2) mu / (lambda chi(W))` is increasing (`chi` decreasing) and
`W = 0` lies below it, so by (D) the true `W` is at most its least fixed point `W_0`. Then (C)
with `chi(W) >= chi(W_0)` and `rho_max <= max(rho(W_0), rho(-W_0))`. QED

As `mu / lambda -> 0`, `W_0 -> 0` and the bound tends to `mu^2 / (2 lambda)`, which is Theorem
R's Lemma 2 with `theta = 1` and `lambda_2(B)` in place of `lambda_2(A)`. At `n = 7` in the
application `W_0` is about `0.25`, and the loss against that limit is the factor
`2 rho(0.25) / chi(0.25) = 1.17`, against Theorem R's `1 / theta_7 = 1.08`.

## 5. What it closes, with the capacity route

`lemma2-prime-rho.py` runs the joint fixed point: `lambda >= 1 - sqrt(K / a)` from
`per(B) >= gamma_n exp(a ||E||_F^2)`, `mu <= sqrt(2 gamma_n kappa_n)` from Theorem R's Lemma 3(a),
`K` from Lemma 2', and the case closes when `K < log(m_n / gamma_n)`. Margins:

| n | a = 1/(2n), proved | a = 1/n | a = 0.2 | a = 0.3 | a = 1/2 |
|---|---|---|---|---|---|
| 7 | 0.827x, no | **1.227x** | 1.331x | 1.426x | 1.514x |
| 8 | 2.682x | 2.994x | 3.137x | 3.232x | 3.325x |
| 9 to 15 | 5.9x to 820x | | | | |

**What these margins do and do not mean.** The table reports the least fixed point `K_1` of
`K <= Psi(K) := Phi(1 - sqrt(K/a))`. But `Psi` is increasing with `Psi(0) > 0` and a pole at
`K = a`, so the solution set of `K <= Psi(K)` is `[0, K_1]` together with `[K_2, infinity)`
for a second crossing `K_2` (`branch-structure.py`: at `n = 8`, `K_1 = 0.0037`, `K_2 = 0.047`,
against the needed `log(m_8/gamma_8) = 0.0098`). A counterexample needs `K >= log(m_n/gamma_n)`.
The small-cost branch `[0, K_1]` is therefore excluded at every `n >= 8` (and at `n = 7` once
`a >= 1/n`), and that is what the margins measure. The large-cost branch `[K_2, infinity)` is
**not** excluded by anything here: there `lambda_2(B) <= 1 - sqrt(2 n K_2)`, which is `0.13` at
`n = 8`, so `B` is near-decomposable, and that is exactly the barrier of
`attack/spectral-gap-near-maximisers`, unit 5. So what Theorem 2 and Lemma 2' prove is a
structure theorem: **every counterexample to Dittert's conjecture at `n >= 8` has scaling cost at
least `K_2(n)` and a Sinkhorn scaling with spectral gap at most `1 - sqrt(2 n K_2(n))`**;
expander counterexamples do not exist. They do not prove the conjecture. The comparison between
`lambda_2(A)` and `lambda_2(B)` still never arises, and `n = 7` joins the same statement as soon
as `a >= 1/n`, the two-column form `per(B) >= gamma_n exp((d_j + d_l)/2)`.

The two earlier chains are kept for the record. The crude one, with `|e|_2 <= e^delta Q` in
place of identity (III), closes `n >= 8` (1.98x at `n = 8`) and does not close `n = 7` for any
`a`, even `1/2`; the intermediate one, with the third-order term bounded by `e^delta W Q / 2`,
closes `n = 7` only from `a = 0.3`. Identity (III) is what makes the third-order loss enter once
and linearly.

## 6. What remains

- Inside Lemma 2' itself, the least fixed point `W_0` is the right bound: the map is increasing
  and the true `W` is bounded by its own image, so `W <= W_0` whenever `W` starts below the
  fixed point, which it does (`W = 0` when `A` is doubly stochastic, and `W` depends continuously
  on `A` within the connected set of fully indecomposable matrices). This is not the same as
  the branch question of section 5, which is about the joint inequality with Theorem 2 and is
  genuinely open.
- The large-cost branch of section 5: a counterexample whose scaling has `K >= K_2(n)` and
  `lambda_2(B) <= 1 - sqrt(2 n K_2(n))`. Excluding it needs a lower bound on the permanent of a
  near-decomposable doubly stochastic matrix that is far above `gamma_n`, which is the barrier
  the previous attack recorded, and no tool in this record touches it.
- `n = 7` joins the small-branch exclusion once `a >= 1/n`: the two-column theorem, unproved.
