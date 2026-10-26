# Strategy study: ladder-the-parameter

Written 2026-09-04 (step 1 of the plan). Contract: STUDY.md.

## 1. Queries

The query set of novelty.md, re-read for the three things step 1 asks for: the current and the
ideal value of the constant, the chain of steps in the known proofs and where each loses the
deficiency term, and any rung already climbed in print.

## 2. Hits worth reading

- Gurvits, arXiv:math/0510452 and arXiv:0711.3496, and Laurent and Schrijver, Amer. Math.
  Monthly 117 (2010) 903-911. The capacity proof of van der Waerden is a chain: `p_B` is
  H-stable; peel one variable at a time; each peeling loses at most the factor `g(k) =
  ((k-1)/k)^(k-1)` in the capacity (Theorem 1 of Laurent and Schrijver); the product of the
  factors is `n!/n^n`. The loss is located exactly: it is the one-variable inequality at each
  peeling, and it is tight only when the peeled column is uniform on its support.
- Egorychev 1981, Falikman 1981. The variational proof: at a minimiser the partial derivatives
  of the permanent are all equal, and that forces `J_n/n`. No rung: the argument is a first
  order condition and does not see the second order.
- Knopp and Sinkhorn 1982. The one climbed rung in print: on the face with a zero entry the
  minimum is `m_n`, which is `gamma_n (1 + (n/(2(n-1)^3)) + ...)`, that is the quadratic
  strengthening evaluated at `T_n` to leading order.

## 3. What was learned, as constraints on the plan

1. **The ledger.** Proved in print: a constant of 0. Ideal: `n/(2(n-1))`, the local Hessian,
   which no constant can exceed. Measured truth: `c*(n) = 0.250, 0.333, 0.418, 0.461, 0.487,
   0.497` at `n = 3..8`, so the target of the claim is `1/4`, and the application needs only
   `1/n`. Every rung is measured against these three numbers.
2. **The lossiest step is the peeling step of the capacity proof.** The AM-GM step
   `cap(p_B) >= 1` is an equality for every doubly stochastic `B` (attained at `x = 1`), so it
   carries no deficiency at all; whatever deficiency the capacity proof can carry sits in the
   peeling, where the one-variable inequality is tight only for uniform columns. So the first
   rung is: quantify the peeling loss for a non-uniform column.
3. **The certificate rung at small n.** At `n = 3` the sharp inequality is a polynomial
   identity plus a classical inequality: `per(B)/gamma_3 - 1 - ||E||^2/4` is a sum over the
   three rows of `1 - 4 e_2 + 9 e_3`, which is Schur. So a certificate exists at `n = 3`, and the
   plan can ask for its shape at larger `n` before attacking the general case.
4. **What the interpolation from the centre gives and does not give.** Writing
   `f(t) = per(J/n + tE)` as a polynomial in `t`, the coefficients are the matching sums
   `r_k(nE)/(n)_k`; the local constant is exact, the cubic and quartic have closed forms, and the
   tail can be bounded near the centre, but far from the centre the tail is a sum of large
   cancelling terms and no termwise bound survives. So this route climbs only a local rung.

## 4. Stop reason

The queries ran dry: the two proof families and the one climbed rung are the whole literature
on the shape of the bound, and none contains a global deficiency term.
