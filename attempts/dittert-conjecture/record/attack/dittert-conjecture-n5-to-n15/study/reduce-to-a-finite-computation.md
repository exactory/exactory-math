# Strategy study: reduce-to-a-finite-computation

Written 2026-09-03 (stage 5, step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv | `Dittert` (all fields, by date) | 2026-09-03 | the three 2026 proofs; the only finite computations in print for this statement |
| arXiv | `abs:permanent AND abs:"sum of squares" AND (abs:certificate OR abs:"van der Waerden")` | 2026-09-03 | nothing relevant: no SOS certificate for a permanent inequality other than 2607.29191 |
| Crossref, zbMATH | as in novelty.md | 2026-09-03 | Cheon-Wanless 2012 is the only earlier computer-assisted result (Thm 3.2 for 4 <= n <= 11 by interval narrowing) |
| local | `study/fetched/src-2607.29191/main.tex` sections 3-5 and the Lean section, grepped and read | 2026-09-03 | the n = 4 pipeline, below |
| local | `study/kafidov-threshold.py` (exact over Q) | 2026-09-03 | where the analytic finite check stops, below |
| local | `study/gate-symmetry-blocks/blocks.py` (character-theoretic block sizes, n = 4..12) | 2026-09-03 | the SOS Gram sizes after symmetry reduction, below |

## 2. Hits worth reading

- arXiv:2607.29191 (full text). The last value settled by an SOS computation is n = 4. Encoder: gap polynomial Q_4 = 32(phi(U_4) - phi(A)), stability parameter lambda, template sigma_0 + sum x_i sigma_i + sum_{i<j} x_i x_j sigma_ij + h q at degree 4 (the template without the x_i x_j terms gives no positive lambda). Solver: MOSEK (double precision), lambda ~ 0.6153852, rounded to 8/13. Independent checker: exact LDL^T over Q of each reduced Gram matrix, then coefficientwise comparison over Q; formal check in Lean 4 with `native_decide` (trusted base includes the Lean compiler). Sizes: main Gram 153, 136 small Grams of 17; recovery denominator 1331 for the small blocks. The paper does not use the symmetry group.
- arXiv:2607.19439 and arXiv:2606.01531 (full text). The last value settled by the analytic finite check is n = 16 (Kafidov) and n >= 17 (Pang). Their residue is one rational inequality per n; its completeness argument is compactness + Hwang 1986 + Cheon-Wanless Thm 3.2 + Knopp-Sinkhorn 1982 + the joint-deficit dilation lemma. Checker: exact rational bounds by hand ((4.4) in Kafidov).
- doi:10.1016/j.laa.2010.08.041 (full text). Thm 3.2's computer part: interval narrowing of a few structural variables for 4 <= n <= 11, no certificate published.

## 3. What was learned, as constraints on the plan

1. **Analytic residue and its exact stopping point.** Kafidov's chain is dimension-generic except the final comparison m_n - gamma_n > n^3 m_n^2 / (4 (1 - gamma_n)). Exact over Q (`study/kafidov-threshold.py`): true for n >= 16, false for n <= 15 with ratio 0.987 at n = 15, 0.535 at 14, 0.298 at 13, 0.172 at 12, 0.104 at 11, 0.065 at 10, 0.044 at 9, 0.031 at 8, 0.025 at 7, 0.022 at 6, 0.023 at 5. Without Bernoulli (exact (1-t)^n, 60-digit evidence) the residue still fails at n = 15 by 2.1e-5 gamma_15 against the gap 2.5e-3 gamma_15, and the Pinsker step can give at most a further 0.4 percent at the worst pair (a, b) = (7, 7). So the loss is structural, not in the elementary inequalities: it is the uniform scalar dilation of all n rows and the comparison per(S) >= per(B) >= m_n that discards the excess mass n t/(1-t) of S over B. In capacity terms the published chain proves cap(A) >= (1-t)^n; anything sharper on cap(A) (per(A) >= cap(A) m_n by Sinkhorn scaling, since a near-maximiser is fully indecomposable) moves the analytic residue down. Not in print. This is the route to try first for the largest n, and it must not duplicate Kafidov's lemma (which it extends).
2. **SOS residue and its scale after symmetry reduction** (`study/gate-symmetry-blocks/blocks-output.txt`, group G_n = (S_n x S_n) x| Z_2, main Gram over degree-ceil(n/2) monomials, multiplier Grams x_i x_j s_ij over degree ceil(n/2)-1):

   | n | certificate degree | main Gram unreduced | main: largest block, commutant dim | multipliers: largest block, commutant dim |
   |---|---|---|---|---|
   | 4 | 4 | 136 | 4, 54 | 28, 4014 |
   | 5 | 6 | 2925 | 16, 1128 | 303, 493258 |
   | 6 | 6 | 8436 | 16, 1159 | 320, 579073 |
   | 7 | 8 | 270725 | 83, 34828 | 2514, 5.9e7 |
   | 8 | 8 | 766480 | 83, 34937 | 2514, 6.0e7 |
   | 9 | 10 | 3.3e7 | 424, 1.2e6 | 22818, 5.7e9 |
   | 10 | 10 | 9.2e7 | 424, 1.2e6 | 22818, 5.7e9 |
   | 11 | 12 | 4.9e9 | 2099, 5.1e7 | 198774, 5.3e11 |
   | 12 | 12 | 1.4e10 | 2099, 5.1e7 | 198774, 5.3e11 |

   Block sizes at fixed certificate degree stabilise in n (a degree-D monomial touches at most D rows and D columns). Consequence: the n = 4 pipeline (pairwise preordering at minimal degree, double-precision SDP, rational recovery, exact LDL^T, Lean) is workstation-size at n = 5 and 6 (largest PSD block ~300, about 5e5 free entries), heavy at n = 7 and 8 (block 2514, 6e7 entries: beyond a high-precision solver, marginal for a double-precision one), and out of reach from n = 9 (block 22818) as a literal repetition. Independent of the solver, the coefficient comparison must be done in G_n-orbit coordinates from n = 7 on (2.7e5 main monomials at n = 7, 1e24 at n = 15).
3. **Certificate existence at the minimal degree is unknown for n >= 5.** At n = 4 the first template failed and the pairwise one succeeded; nothing says the pairwise template suffices at degree 6 for n = 5. A negative SDP value at n = 5 sends the SOS residue to degree 8 (main Gram over degree-4 monomials, 20475 unreduced).
4. **Two routes with opposite ceilings.** The analytic residue gets easier as n grows (the loss ratio doubles per dimension up), the SOS residue as n shrinks. The plan therefore runs both from their good ends: the analytic sharpening from n = 15 down, the SOS pipeline from n = 5 up, and records where each stops; the eleven dimensions close only if they meet.
5. **Trusted base.** The n = 4 formal check rests on `native_decide`; the harness classifies that as `evidence`, not `pass`. A kernel-reduced check (`decide`/`norm_num` on rational inequalities) is available for a residue of Kafidov's kind (one rational inequality per n) and is out of reach for an SOS identity with 1e5 rational entries. This favours the analytic residue wherever it reaches.

## 4. Stop reason

The queries ran dry: the two arXiv statement-term queries added nothing, and the three 2026 preprints cite each other and Cheon-Wanless 2012 as the complete prior computational record. The local computations were run to settle the two things step 1 asks for: the last settled value on each route (n = 4 by SOS, n = 16 by the rational inequality) and the exact size of what remains.
