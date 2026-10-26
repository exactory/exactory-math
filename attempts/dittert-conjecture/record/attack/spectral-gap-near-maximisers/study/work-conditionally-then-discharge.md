# Strategy study: work-conditionally-then-discharge

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv, zbMATH | the query set of `novelty.md` | 2026-09-03 | no stability theorem for van der Waerden; no bound on the cost of Sinkhorn scaling in terms of the margins |
| arXiv | `abs:Sinkhorn AND (abs:convergence OR abs:"matrix scaling") AND abs:bound` | 2026-09-04 | the Sinkhorn literature bounds the number of iterations to reach a given margin error, not the value of the scaling factors at the fixed point; the two are different quantities |
| local | `study/conditional-K.py`, run here | 2026-09-04 | the threshold the hypothesis must beat, per dimension |
| local | `study/capacity-numerics.py` of the sibling attack | 2026-09-03 | the measured value of the quantity the hypothesis bounds |

## 2. Hits worth reading

- Sinkhorn and Knopp 1967 (through the statements used by the three 2026 Dittert preprints):
  a fully indecomposable nonnegative matrix has a doubly stochastic scaling, unique up to
  the obvious rescaling. This gives the object; nothing in that literature bounds
  `sum log d_1 + sum log d_2` at the fixed point in terms of the margins.
- Gurvits and Leake, arXiv:1804.04351 (abstract): capacity is the right invariant and it is
  exactly `1/(prod d_1 prod d_2)`, but the paper is about lower bounds on permanents, not
  about how far scaling moves a nearly doubly stochastic matrix.
- Theorem R (sibling attack, full text): proves the hypothesis below with
  `K = 1/(2 theta_n lambda_2(A))`.

## 3. What was learned, as constraints on the plan

1. **The hypothesis to condition on, in its most ordinary form.**

       H(n, K): for every fully indecomposable A in K_n with margins u = 1 - r, v = 1 - c,
                -log cap(A) <= K (|u|^2 + |v|^2).

   In words: the cost of Sinkhorn scaling is at most `K` times the squared margins. It is a
   statement about matrix scaling with no permanent and no spectrum in it.
2. **The threshold, computed** (`study/conditional-K.py`). Since
   `-log cap(A) >= log(m_n/gamma_n)` (Knopp-Sinkhorn) and `|u|^2 + |v|^2 <= 2 delta kappa_n`
   with `delta <= gamma_n`, the conjecture at `n` follows from `H(n, K)` whenever
   `K < K_max(n) := log(m_n/gamma_n) / (2 gamma_n kappa_n)`:

   | n | 4 | 5 | 6 | 7 | 8 | 10 | 12 | 15 | 20 |
   |---|---|---|---|---|---|---|---|---|---|
   | `K_max` | 0.179 | 0.301 | 0.536 | 1.00 | 1.94 | 8.09 | 37.2 | 417 | 2.9e4 |

   The bar roughly doubles per dimension, so `n = 7` needs `K < 1` and everything from
   `n = 10` needs only a crude constant.
3. **What the truth looks like.** The sibling attack measured
   `-log cap(A) / (rho' + sigma')` in `[0.67, 1.18]` over 18 samples at `n = 5, 8, 15`
   (`study/capacity-numerics.py`), and `|u|^2 + |v|^2` is `2(rho' + sigma')` to leading
   order, so `K` is about `0.5` in those samples. Against `K_max(7) = 1.00` that is a factor
   of two of room at the hardest open dimension and orders of magnitude above it.
4. **Why this is the right conditional.** Every route in `study/routes-rubric.md` ends by
   bounding `-log cap(A)`; H is that bound stated without the spectral detour, so a proof of
   H closes the problem whatever route produces it, and a counterexample to H at `K < K_max`
   would refute the conjecture. The discharge is therefore not a side quest.
5. **What the discharge needs.** `H(n, K)` is a second-order statement about the Sinkhorn
   fixed point. The linearisation gives it with `K = 1/(2 theta lambda_2)`; a proof with a
   universal `K` needs the second-order term of the Sinkhorn map controlled without a
   spectral gap, which is the same difficulty in new wording, or a convexity argument on the
   scaling functional that does not pass through its Hessian.

## 4. Stop reason

The queries ran dry: the matrix scaling literature bounds convergence rates, not the value
of the scaling at the fixed point, and no source states H in any form.
