# Strategy study: ladder-the-parameter

Written 2026-09-03 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv | `Dittert` and the statement-term queries of `novelty.md` | 2026-09-03 | the analytic chain in print (Cheon-Wanless 2012, Pang 2606.01531, Kafidov 2607.19439) and its two improvements |
| arXiv | `abs:"van der Waerden" AND abs:permanent AND (abs:stability OR abs:"spectral gap" OR abs:capacity)` | 2026-09-03 | 1 hit, Gurvits-Leake 1804.04351 (capacity-preserving operators; not a stability theorem for the permanent) |
| local | `study/kafidov-threshold.py`, `study/capacity-numerics.py`, `study/per-vs-gap-numerics.py`, `study/route-a-capacity-notes.md` | 2026-09-03 | the rung values and the numerical tests of the intended sharpening |

## 2. Hits worth reading

- Cheon-Wanless 2012 (full text): Thm 2.1 gives the first rung, subset sums within sqrt(2 delta k); Thm 2.4 the resulting per(A) > (1 - sqrt(8 delta n^3 gamma_n)) gamma_n; the dilation lemma is theirs (Lemma 2.2 with Li's criterion). No dimension closed by it alone.
- Pang 2606.01531 (full text): the rung is the dilation factor t = sqrt(3 n delta) from a sharper subset-sum estimate (Lemma 3, Pinsker plus Thm 2.1); closes n >= 17; Remark 3.2 records the scalar Lambda_n = (m_n - gamma_n)/((3/4) n^3 m_n^2) with Lambda_16 = 0.62.
- Kafidov 2607.19439 (full text): the rung is t = sqrt(n delta/(1 - delta)) from the joint budget rho + sigma <= delta; closes n = 16; the exact scalar here, r_n = (m_n - gamma_n)/(n^3 m_n^2/(4(1 - gamma_n))), is 1.87 at 16 and 0.987 at 15.

## 3. What was learned, as constraints on the plan

1. **The ladder and its rungs.** The progress parameter is the dilation loss: the chain proves per(A) >= cap(A) m_n with cap(A) >= (1 - t)^n, and the claim at n follows when m_n (1 - t)^n > gamma_n - delta for all delta in (0, gamma_n]. Rungs climbed in print: t = sqrt(8 delta n) (Cheon-Wanless, no n closed), t = sqrt(3 n delta) (n >= 17), t = sqrt(n delta/(1 - delta)) (n >= 16). The trivial value is the published t; the ideal value is a loss of order delta (no n^{1.5} sqrt(delta) term), at which every n >= 4 closes with one rational inequality per n.
2. **Where the loss is.** Each elementary step of the published chain (Pinsker, the joint budget, the subset-sum to Hall conversion, Bernoulli) is within one percent of tight at n = 15 (exact and 60-digit computations); the structural loss is (i) the uniform scalar dilation of every row and (ii) comparing the dilated matrix only to a doubly stochastic matrix it dominates, which discards its excess mass. In capacity terms both are the bound cap(A) >= (1 - t)^n against a true value cap(A) = exp(-(rho' + sigma')(1 + o(1))) in every sampled near-doubly-stochastic matrix (ratio 0.67 to 1.18 in 18 samples at n = 5, 8, 15).
3. **The next rung and its one obstacle.** By the entropy dual of the capacity, cap(A) >= exp(-(|u|^2 + |v|^2)/lambda_2(A)) for a near-doubly-stochastic A with margins u = 1 - r, v = 1 - c (route-a notes, (2)-(4)), so the rung is a lower bound on the spectral gap lambda_2(A) of a near-maximiser; numerically per(B) <= 1.05 gamma_n forces lambda_2(B) >= 0.71 (n = 5), 0.78 (n = 8), 0.86 (n = 12) in 1200 doubly stochastic samples with a zero. No theorem of this kind ("a small permanent forces a spectral gap") was found in print.
4. **Routes not to duplicate.** Re-deriving the joint-deficit lemma or the Pinsker step gains nothing; the record already has them exactly.
5. **Cash-out shape if the rung is not climbed.** The rung as a conditional result: "if lambda_2(A) >= c for every A in K_n with phi(A) >= 2 - gamma_n and a zero entry, then Dittert's conjecture holds at n", with the explicit rational condition m_n exp(-4 delta/c) > gamma_n - delta; plus the exact threshold table as computational evidence and the spectral-gap statement as a problem paper.

## 4. Stop reason

The queries ran dry: the two arXiv statement-term queries and the stability query added nothing beyond the three chain papers, and the numerical tests were run to settle the strategy's step-1 questions (the current and trivial values of the rung, and the step where the loss sits).
