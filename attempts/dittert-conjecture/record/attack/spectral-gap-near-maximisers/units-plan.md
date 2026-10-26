# What this attack has that is worth cashing out

Written 2026-09-04 after move 7, as the input to stage 7.

1. **Theorem R is the sibling attack's, not this one's.** It is already unit 3 of
   `attack/dittert-conjecture-n5-to-n15`. This attack must not re-claim it.
2. **The effective-resistance lemma (move 3).** For a fully indecomposable `A` with margins
   `u, v`, `(alpha; beta) = L^+ (u; v)` and `Phi = (u;v)^T L^+ (u;v)`,
   `|alpha_i + beta_j| <= sqrt(R_eff(i,j) Phi) <= sqrt(Phi / a_ij)` on the support. Proved,
   checked on 24 instances, not in print. A lemma about weighted bipartite graphs, useful
   beyond this problem. Form: new-machinery.
3. **The conditional theorem with its threshold table (move 5).** `H(n, K)` implies
   Dittert's conjecture at `n` whenever `K < K_max(n) = log(m_n/gamma_n)/(2 gamma_n kappa_n)`,
   with the table 1.00 at `n = 7` up to 2.9e4 at `n = 20`. Form: reduction-or-equivalence
   (it is an implication with an explicit threshold), or conditional-or-special-case.
4. **The refutation of the unrestricted hypothesis (move 6) and the dichotomy.** `H(n, K)`
   with a universal `K` is false, by the block-diagonal direction; and the resulting
   dichotomy names the single open link. Form: survey-or-problem-paper.
5. **The two refuted routes with their exact thresholds (moves 1, 4, 7).** The Cheeger and
   blocks chain closes from `n = 35` crudely, `n = 23` refined; the entrywise lower bound is
   false on the natural relaxation; the truncation repair enlarges the margins it repairs.
   Form: survey-or-problem-paper, together with item 4.

Nothing here closes a dimension of Dittert's conjecture. Items 2 and 3 are the parts a
reader could use; items 4 and 5 are the map.
