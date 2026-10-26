# Removing the nonnegativity condition (N) from Theorem R

Written 2026-09-03, after move 1 established that (N) is the binding constraint by a factor
of 12 at `n = 7` and 577 at `n = 15` (`study/binding-constraint.py`). This note records the
mechanism, why the obvious fixes fail, and the one that looks like it works.

## What (N) is and why it costs a square root

Theorem R's Lemma 2 builds a doubly stochastic competitor `B' = A + E` with
`e_ij = a_ij (alpha_i + beta_j)`, where `(alpha; beta) = L^+ (u; v)` solves the weighted
bipartite Laplacian system for the margins `u = 1 - r`, `v = 1 - c`. Then Lemma 1(ii) gives
`-log cap(A) <= KL(B' || A) <= Phi := (u; v)^T L^+ (u; v)`, and the contradiction follows.

`B' >= 0` needs `alpha_i + beta_j >= -1` wherever `a_ij > 0`. Lemma 3(c) discharges it with
the crude bound `|alpha|_inf + |beta|_inf <= sqrt(2) |(alpha; beta)|_2 <= sqrt(2) |(u;v)|_2 /
(theta_n lambda_2)`, and `|(u;v)|_2^2 <= 2 delta kappa_n`, so the requirement becomes
`lambda_2 >= 2 sqrt(delta kappa_n)/theta_n`. The margins have size `sqrt(delta)`, so the
correction has size `sqrt(delta)/lambda_2` and the condition is `sqrt(delta)`-sized, whereas
the contradiction itself is `delta`-sized. **That square root is the entire gap between the
two bars.**

## The right object: `L` is a bipartite graph Laplacian, so `alpha_i + beta_j` is a resistance

With the sign change `beta -> -beta` the quadratic form `(alpha; beta)^T L (alpha; beta) =
sum_ij a_ij (alpha_i + beta_j)^2` becomes `sum_ij a_ij (alpha_i - beta_j)^2`, the Dirichlet
form of the weighted bipartite graph on rows and columns with edge weights `a_ij`. Then for
the vector `q = e_i^{row} - e_j^{col}`,

    |alpha_i + beta_j| = |q^T L^+ (u; v)| <= sqrt( q^T L^+ q ) * sqrt( Phi )
                       = sqrt( R_eff(i, j) ) * sqrt( Phi ),

where `R_eff(i, j)` is the effective resistance between row `i` and column `j`. This is the
Cauchy-Schwarz inequality in the `L^+` inner product, and it replaces the `1/lambda_2` of
Lemma 3(c) by a local quantity. Since a single edge of conductance `a_ij` already connects
`i` to `j`, Rayleigh monotonicity gives

    R_eff(i, j) <= 1 / a_ij      whenever a_ij > 0,

which is exactly where (N) has to hold. So

    |alpha_i + beta_j| <= sqrt( Phi / a_ij )      on the support of A.                   (*)

**(N) therefore holds at every entry with `a_ij >= Phi`, with no spectral hypothesis at all.**
And `Phi <= 2 delta kappa_n / (theta_n lambda_2)` is `delta`-sized, not `sqrt(delta)`-sized,
once the spectral factor is separated out.

## What is left: the small entries

Entries with `0 < a_ij < Phi` are the only obstruction. Their total mass is at most
`n^2 Phi`. The construction to try is: set `b'_ij = a_ij (1 + alpha_i + beta_j)` where
`a_ij >= Phi` and `b'_ij = 0` where `a_ij < Phi`, then repair the margins, which are now off
by at most `n^2 Phi` in `l_1`. The repair is a second application of the same lemma with
margins of size `n^2 Phi` instead of `sqrt(delta)`, so its cost is
`(n^2 Phi)^2 / lambda_2`, a second-order term. Setting an entry of `B'` to zero costs nothing
in `KL(B' || A) = sum b' log(b'/a)` because the term vanishes.

Two things have to be checked before this is a proof:

1. **The repair terminates.** Each round replaces margins of size `s` by margins of size
   `O(n^2 s^2 / (something))`; the iteration converges when the first `s` is small enough.
   This is a Newton step for the Sinkhorn scaling and the standard local quadratic
   convergence should apply, but with explicit constants.
2. **The support does not fall apart.** Deleting the entries below `Phi` must leave the
   bipartite graph connected, or `L^+` for the repair is not defined. Cheon-Wanless Thm 3.2
   gives full indecomposability of `A`, not of the truncation.

## What it would buy

If the repair works, the bar the spectral routes must clear drops from
`c_N = 2 sqrt(gamma_n kappa_n)/theta_n` to (a constant times) `c_C = 2 m_n kappa_n/theta_n`.
Against `c_C`, from `study/binding-constraint.py`:

| route | what it proves | settles |
|---|---|---|
| Cheeger and blocks, crude `(1-eps)^n` block capacity | `lambda_2 >= 1/(2 n^4)` | `n >= 15` |
| the same with an `exp(-2 eps)` block capacity | `lambda_2 >= 1/(8 n^2)` | `n >= 10` |
| the same with `exp(-4 eps)` | `lambda_2 >= 1/(32 n^2)` | `n >= 12` |

So (N) plus a block capacity bound would leave only `n = 7, 8, 9` of the eleven open
dimensions, and `n = 5, 6` are already closed by the sibling attack's exact certificates.

## Status

(*) is proved above (Cauchy-Schwarz in the `L^+` inner product, then Rayleigh monotonicity);
it is the new ingredient. The repair argument is not proved. Nothing here is in the
literature (`novelty.md`).
