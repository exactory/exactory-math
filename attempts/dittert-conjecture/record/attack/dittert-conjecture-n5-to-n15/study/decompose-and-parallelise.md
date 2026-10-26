# Strategy study: decompose-and-parallelise

Written 2026-09-03 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv, Crossref, zbMATH, MathOverflow, web | as recorded in `novelty.md` and `study/problem.md` | 2026-09-03 | the complete list of proved dimensions and the method of each |
| local | `study/kafidov-threshold.py` | 2026-09-03 | the analytic component's scalar per n (exact) |
| local | `study/gate-symmetry-blocks/blocks-output.txt` | 2026-09-03 | the computational component's block sizes per n |
| local | `deterministic/numerical-optimisation-run-2` | 2026-09-03 | the n = 5 component's numerical value (lambda* = 40.1156) |

## 2. Hits worth reading

- arXiv:2606.01531 (Pang): improved the analytic component at every n >= 17 to the value "closed"; its scalar, m_n - gamma_n over (3/4) n^3 m_n^2, is 1.21 at n = 17 and 0.62 at n = 16 (its Remark 3.2). Full text read.
- arXiv:2607.19439 (Kafidov): improved the same component at n = 16 (scalar 1.87 at 16, 0.987 at 15 by the exact computation here). Full text read.
- arXiv:2607.29191 (Li-Xiong-Yang): the computational component at n = 4, value kappa = 1/52. Full text read.
- Cheon-Wanless 2012, Thm 3.2: a computer-assisted component (partly decomposable maximisers excluded) that was itself split by dimension, 4 <= n <= 11 by machine and n >= 12 by hand. Full text read.

## 3. What was learned, as constraints on the plan

1. **The components are the dimensions.** The claim is a conjunction of eleven statements C_5, ..., C_15 with no implication between them in print; each carries its own scalar. On the analytic route the scalar is r_n = (m_n - gamma_n) / (n^3 m_n^2 / (4(1 - gamma_n))) and the interface is r_n > 1; on the computational route the scalar is the stability parameter lambda_n of the symmetry-reduced pairwise template at degree 2 ceil(n/2), and the interface is lambda_n > 0 with an exact rational certificate.
2. **Settled values and where each route stopped.** Analytic: r_16 = 1.87 (closed), r_15 = 0.987, r_14 = 0.535, r_13 = 0.298, r_12 = 0.172, r_11 = 0.104, r_10 = 0.065, falling by about 1.9 per dimension down; the route stopped at 16 because the uniform dilation loses the factor n^3 m_n^2 (study/route-a-capacity-notes.md). Computational: lambda_4 = 8/13 exact (kappa = 1/52); lambda_5 = 40.1 numerical (kappa = 0.0128), exact recovery in progress; n = 6 feasible at the same block sizes (16 and about 22); n = 7, 8 heavy (main block 83); n >= 9 out of reach at minimal degree (main block 424 and up, and the equation count grows with the orbits of degree-2D monomials).
3. **The two routes share no parameter.** Raising lambda_n does not move r_n and conversely, so the components are independent in the strategy's sense (question 3 of its precondition). The only coupling is the budget: every move spent on one route is not spent on the other.
4. **A third component kind for the middle.** For 7 <= n <= 14 neither route is settled. The candidates are (a) the missing lemma of route A (spectral gap from a small permanent), which if proved closes every n >= 4 at once and makes the whole ledger one rational inequality per n; (b) a cheaper computational template for the middle dimensions (lower degree with the analytic reduction to a neighbourhood of Omega_n, so that only a local certificate is needed). Neither is in print.
5. **Interface theorem for the formal check.** Each closed component is a finite statement (one rational inequality, or one rational SOS identity), so the machine check of an interface theorem stays inside Lean's standard axioms when kernel-reduced; the n = 4 precedent used native_decide (evidence under this harness).

## 4. Stop reason

The queries ran dry: no source beyond those of the problem-level study speaks to a per-dimension organisation of this conjecture, and the values in the table above are the settled ones. The strategy's step 2 (the component table) follows directly.
