# Problem-level study: the spectral gap of a near-maximiser with a zero entry

Written 2026-09-03. Contract: STUDY.md. Sources: references/sources.md.
The sibling attack `attack/dittert-conjecture-n5-to-n15` produced this problem: its
Theorem R (`study/route-a-reduction-theorem.md` there) shows that G(n, c_n) implies
Dittert's conjecture at n, and its numerical run 4 supports G with a wide margin.

## 1. Queries

See `novelty.md`: five arXiv queries, one zbMATH query, plus the Crossref, zbMATH,
MathOverflow and web queries of the sibling attack, all on 2026-09-03.

## 2. Hits worth reading

| identifier | what it did | read |
|---|---|---|
| Egorychev 1981, Falikman 1981 (zbMATH 0478.15003) | per(B) >= n!/n^n on Omega_n with equality only at J_n/n, by the Alexandrov-Fenchel inequality | not read; the statement is used as a black box |
| Knopp-Sinkhorn 1982, doi:10.1080/03081088208817459 | the minimum of per on the boundary of Omega_n is m_n, attained at T_n | not read; the value is used, as in the three 2026 Dittert preprints |
| Cheon-Wanless 2012, doi:10.1016/j.laa.2010.08.041 | Thm 2.1 (subset-sum control of a near-maximiser), Thm 3.2 (a maximiser is fully indecomposable), Thm 3.7 (its zeros are not one block) | full text (fetched by the sibling attack) |
| arXiv:1804.04351 (Gurvits-Leake) | capacity-preserving operators; the capacity proof of van der Waerden and of Schrijver's inequality | abstract only |
| Theorem R (this record's sibling) | the reduction that makes G(n, c_n) worth proving | full text |

## 3. What was learned, as constraints on the plan

1. **No stability theorem exists to cite.** Every route must build the quantitative step
   itself. The qualitative results (full indecomposability) are strictly weaker than a gap.
2. **The target constant is very small.** c_n is of order sqrt(gamma_n): 0.18 at n = 7,
   0.0035 at n = 15, while the truth appears to be about 0.7 uniformly. A proof may lose
   several orders of magnitude and still succeed. This is the single most important
   feature of the problem: it makes crude arguments admissible.
3. **The permanent has to enter through a lower bound.** The hypothesis is
   phi(A) >= 2 - gamma_n, which by AM-GM forces per(A) <= gamma_n. So the contrapositive
   needs: small spectral gap implies per(A) large. Any route therefore needs a
   *lower* bound on the permanent from structure, and the two known families are
   (i) van der Waerden and Schrijver type bounds (via capacity or Alexandrov-Fenchel), and
   (ii) block or expansion bounds (a permanent of a block-decomposable matrix factorises).
4. **Cheeger is the natural bridge.** lambda_2 small gives a sparse cut of the bipartite
   graph carrying the mass of A; a sparse cut makes A nearly block diagonal after
   permutations; and gamma_k gamma_{n-k}/gamma_n = C(n,k)^{-1} n^n/(k^k (n-k)^{n-k})
   which is at least sqrt(2 pi k(n-k)/n) (1 + o(1)) >= 2 for every 1 <= k <= n-1 and n >= 4.
   So a genuine block decomposition already multiplies the permanent by at least 2, far more
   than the (1 + gamma_n) the hypothesis allows. The whole difficulty is that a *sparse* cut
   is not a *zero* cut, and the cross terms have to be controlled.
5. **The extremal candidate is T_n and its gap is bounded below uniformly.** T_n has
   lambda_2 about 0.70 at every n tested. So the statement is not tight anywhere in sight,
   which is again a reason to expect a crude proof to work.
6. **Two settled ranges give free test cases.** n = 5 and n = 6 of the Dittert conjecture
   are proved by the sibling attack, so any candidate lemma can be tested against the exact
   certificates there; and n >= 16 is in print.

## 4. Stop reason

The queries ran dry: three arXiv queries on the stability formulation returned only the
capacity paper and the Dittert preprints, the spectral query returned nothing, and zbMATH
returned only the original van der Waerden solution. There is no prior art to build on
beyond the four black boxes above.
