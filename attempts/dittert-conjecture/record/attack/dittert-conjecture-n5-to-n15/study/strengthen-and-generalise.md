# Strategy study: strengthen-and-generalise

Written 2026-09-03 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv, Crossref, zbMATH | as in `novelty.md` | 2026-09-03 | the strengthenings in print, below |
| arXiv | `abs:"van der Waerden" AND abs:permanent AND (abs:stability OR abs:"spectral gap" OR abs:capacity)` | 2026-09-03 | no stability theorem for the van der Waerden inequality |
| local | `deterministic/numerical-optimisation-run-1`, `study/per-vs-gap-numerics.py`, `deterministic/numerical-optimisation-run-4` | 2026-09-03 | small-instance tests of the candidate strengthenings |

## 2. Hits worth reading

- arXiv:2607.29191: the quantitative stability strengthening phi(U_n) - phi(A) >= c_1 ||A - U_n||_F^2 at n = 4 (c_1 = 1/52); the SOS route needs it (a certificate must be strictly positive away from U_n). Extended here to n = 5 (c_1 = 32/3125) and n = 6 (c_1 = 128/46656). Not refuted at any n.
- Cheon-Wanless 2012, Thm 2.4: the strengthening "per(A) > (1 - sqrt(8 delta n^3 gamma_n)) gamma_n for near-maximisers" (a quantitative near-double-stochasticity); proved for all n.
- Cheon and Hwang (cited in Cheon-Wanless 2012, introduction): a problem generalising the Dittert conjecture; not pursued here.
- Lih-Wang conjecture (Udayan-Somasundaram 2024): a sibling strengthening on Omega_n (convexity of per along segments to J_n); open; shares the bottleneck (behaviour of per near J_n).

## 3. What was learned, as constraints on the plan

1. **Candidate strengthenings in print, none refuted.** (i) The stability form with an explicit c_1(n): proved at n = 4, 5, 6. (ii) The face statement max_{a_11 = 0} phi = 2 - m_n, attained at the Knopp-Sinkhorn extremal T_n (numerically exact at n = 5, 6, run 1); it is stronger than the conjecture on the face by the whole gap m_n - gamma_n and is the natural inductive object for the boundary.
2. **The candidate that the walk needs.** Hypothesis G(n, c) of study/route-a-reduction-theorem.md is a strengthening of "no maximiser has a zero entry" into a quantitative spectral statement about every near-maximiser with a zero; its deduction to the original is Theorem R (short, explicit). It is the statement to test by counterexample (step 3) and, if it survives, the statement to prove (step 4).
3. **Refutations available.** None in print. Small-instance tests here: 1200 doubly stochastic samples with a zero at n = 5, 8, 12 and the multi-start minimisation of run 4 found no matrix with per <= 1.05 gamma_n and lambda_2 below c_n; the minimum lambda_2 found is recorded there.
4. **The induction that stopped.** No induction on n is in print for this conjecture; the three proved ranges use three different arguments. A strengthened inductive hypothesis would have to carry the boundary structure (T_n-like extremals) from n - 1 to n, and no such step is known.

## 4. Stop reason

The queries ran dry: the stability query returned no theorem of the needed kind, and the candidate list is complete relative to the sources searched.
