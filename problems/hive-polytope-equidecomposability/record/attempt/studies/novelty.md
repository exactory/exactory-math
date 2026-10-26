# Novelty study for the claim of objective-000001

Written on 2026-10-20. The problem study `studies/problem.md` holds the queries, the hits
and the constraints; this record binds the exact statement and each neighbouring
formulation to the common searches and readings that cover it, and states the outcome.

## The exact statement

The claim of obligation-000001 (claim digest
`a678173591c44441e071c678db7bb93bea918497ea45ab56fdf2d90349d4aa16`), equal to the statement
text of the common record `statement-1`: for every n >= 2 and every triple of partitions
(lambda, mu, nu) with at most n parts, |lambda| + |mu| = |nu| and c^nu_{lambda mu} > 0, the
hive polytope H(lambda, mu, nu) in R^D is GL_D(Z)-equidecomposable with a lattice polytope Q.

## Neighbouring formulations

- N1, Ehrhart form (weaker): for every admissible triple some lattice polytope Q has
  Ehrhart polynomial c^{t nu}_{t lambda, t mu}.
- N2, Haase-McAllister form (weaker): H(lambda, mu, nu) is GL_D(Z)-equidecomposable with a
  disjoint union of integral open simplices (Conjecture 3.2 of Haase-McAllister 2008
  restricted to hive polytopes).
- N3, Gelfand-Tsetlin sibling: GT(lambda, mu) is GL(Z)-equidecomposable with a lattice
  polytope.
- N4, consequence (weaker): the numerator G(z) of sum_t c^{t nu}_{t lambda, t mu} z^t has
  nonnegative integer coefficients (King-Tollu-Toumazet 2004).
- N5, rank restriction: the statement for partitions with at most n parts; settled for
  n <= 4 and open from n = 5 on.

## Searches bound to each formulation

All searches are common `literature_search` records (provider arXiv, captured
2026-10-20T20:05Z, every query complete with at most 13 returned works):

| formulation | search record | digest |
|---|---|---|
| statement | `search-direct-equidecomposability` | `32855ac1aebf81d98d6fb869ee34e981e8cd73f47eec6393e3958d4beacf4d81` |
| statement | `search-theory-period-collapse` | `9811032a8ddd6b676ac4d83cb7438b8c18ad99ad72f29c1b9c407a1a44fce450` |
| N1 | `search-direct-equidecomposability` | as above |
| N1 | `search-theory-period-collapse` | as above |
| N2 | `search-theory-period-collapse` | as above |
| N2 | `search-direct-equidecomposability` | as above |
| N3 | `search-adjacent-gelfand-tsetlin` | `fc0c45a4daa2813a549af362040b6ba276ddf0d1383a72d182938afa259c088b` |
| N4 | `search-recent-stretched-lr` | `d0f8e3a4ec3b9cc84c9cc5fd95977753aee0044bf76b56df95e2761acea80c76` |
| N5 | `search-recent-stretched-lr` | as above |

The additional tier-one queries of the problem study (arXiv, Semantic Scholar, Crossref,
zbMATH; `studies/queries/index.json`) found no work absent from these records that bears
on any formulation.

## Readings bound (complete `fulltext` readings of the common store)

`reading-haase-mcallister-2008-3`
(`aae21c2354cdedad834a228e381555897b487a7ca68f25aa309e73f6a9454edc`),
`reading-ferudun-2026-3` (`3b3ddf996d37bc51489d886b756ae54239573863c1008e7623fb256b4c8370a7`),
`reading-ktt-2006-3` (`ab6abbdc4f71759b2a43ce9c1a1b8f265786a90c378f9203a048fa8808e35178`),
`reading-rassart-2004-3` (`6fe3a9b00faff3da43d1043596af97dcda15d8959a935acfedb13870ea054c3a`),
`reading-buch-2000-3` (`f85945fdf911c0cd40691280fbd9045385a5377618261d3c6b1811abe014b675`),
`reading-dlm-2006-3` (`cd33775751acd78fb977cd4e175f57b151033f2a4dccd745b116f98f610309b3`),
`reading-fernandes-2018-3` (`f1fa638414ef9bbae57167c522091174fd6f7525f8060bdb0a8df61a2849d8b5`),
`reading-turner-wu-2014-3` (`ddf1f9dbd258b69a234c7b027f319a42b49999beaa9084b70b8cf9ca0b915aa5`),
`reading-bohnert-2024-3` (`b5ba1f1fc81eb05bbed3e4c9e0a3be947735c0b13ec421384cf472405d5ce4e8`),
`reading-ahz-2022-3` (`6be9fce8384df602f13e559a5e593bbafb707323a3f71369831558a2dfb105ec`),
`reading-alexandersson-alhajjar-2018-3`
(`900e1fdf0af41ea3c0698ac0b0908a8c7ae63c344b31503cb00fa6b6e6f501a8`),
`reading-ghodsi-2026-3` (`35f875777a59e3aca9b4e8562d99302f42627843061c95726b0cbbfa122ee025`).

## What the readings settle

- The statement is not posed in print. The closest prior is Haase-McAllister 2008,
  Conjecture 3.2, whose conclusion (a disjoint union of integral open simplices) is weaker
  than one lattice polytope, and whose Example 2.4 shows the one-polytope conclusion fails
  for general rational polytopes with period collapse; the hive case is named as motivation
  and not treated.
- N1 appears nowhere; N2 is exactly the hive case of Conjecture 3.2, recorded as open by
  AHZ 2022 (their introduction); N3 is not posed, and its ingredients (period collapse of
  GT(lambda, mu), open positivity) are recorded in Alexandersson-Alhajjar 2018 and AHZ 2022;
  N4 is the open King-Tollu-Toumazet numerator conjecture of 2004, restated in KTT 2006 and
  recorded open in AHZ 2022, Remark 6.3; N5 is settled for n <= 3 by the dimension argument
  of this record, reported settled for n = 4 by Buch 2000 (stated there without a printed
  proof), and open from n = 5 (Buch 2000, Example 2; Ferudun 2026 treats monomial
  positivity, not equidecomposability).
- No settling source exists for the statement or a neighbour in either direction. The only
  disproof tools in print are necessary conditions on the Ehrhart polynomial (Scott in
  dimension 2, h*-inequalities in general) and the Turner-Wu edge weighting for polygons;
  no computed violation is in print.

## Gaps

- King-Tollu-Toumazet 2004 (DOI 10.1090/crmp/034/10) is not available to this record; it
  is the origin of N4 and is cited through KTT 2006, which restates both conjectures. It
  cannot settle the statement (it predates the question and treats positivity).
- King-Tollu-Toumazet 2009 (DOI 10.1016/j.jcta.2008.06.005) is not available (publisher
  returned HTTP 403); its factorization theorem is read through Cho-Jung-Moon 2008 (full
  text saved under `studies/sources/`) and Ghodsi 2026. It bears on the constructive
  strategy, not on openness.
- Four Semantic Scholar queries of the problem study were rate-limited (HTTP 429); the
  statement-level and neighbour-level coverage rests on the complete arXiv and zbMATH
  searches and the readings above.

## Outcome of the local novelty check

No decisive prior or settling work was found for the statement or for any declared
neighbour; the local outcome is "supported open", subject to the independent openness review
of the common workspace, which binds the search and reading records listed above.
