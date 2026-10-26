# Strategy study: attack-the-negative-side

Objective `objective-000001`, claim of obligation-000001 (see `studies/problem.md`). This
study settles what the strategy's step 1 asks for before any entry is dispatched: the range
searched with no counterexample, the constructions in print and their resource, and the near
misses with the conditions each passes. Written on 2026-10-20; every query below was run on
2026-10-20.

## 1. Queries

Records of the common store reused (no identical evidence recaptured): the four arXiv
searches of `studies/problem.md`, section 1a, in particular
`search-theory-period-collapse` (digest `9811032a8ddd...`; q3, q4, q7: scissors congruence,
period collapse, Ehrhart equivalence) and `search-direct-equidecomposability` (digest
`32855ac1aebf...`; q8: rational polytopes with lattice-polytope Ehrhart polynomials).

Queries of this study (raw responses under `studies/queries/`, index
`studies/queries/index.json`):

| source | file | query | requested | returned | coverage |
|---|---|---|---|---|---|
| arXiv API | `arxiv/n-arxiv-equidecomposability-ehrhart.xml` | `all:equidecomposability AND all:Ehrhart` | 20 | 4 of 4 | complete |
| arXiv API | `arxiv/n-arxiv-hstar-inequalities.xml` | `all:"h*-vector" AND all:inequalities AND all:"lattice polytope"` | 20 | 3 of 3 | complete |
| arXiv API | `arxiv/n-arxiv-dehn-lattice.xml` | `all:"Dehn invariant" AND all:lattice AND all:polytope` | 20 | 0 of 0 | complete |
| arXiv API (abstracts by id) | `arxiv/abstracts-strategy-hits.xml` | `id_list` of the twelve new hits of the strategy studies | 12 | 12 | complete |
| Semantic Scholar | `s2/n-s2-invariants-equidecomposability.json` | `invariants unimodular equidecomposability rational polytopes Ehrhart equivalence` | 20 | 8 of 8 (on a retry with 45 s spacing after HTTP 429) | complete |
| Semantic Scholar | `s2/n-s2-hstar-inequalities.json` | `inequalities h*-vector lattice polytopes Stapledon Hibi Stanley` | 20 | HTTP 429 twice | gap (rate limit) |
| Semantic Scholar | `s2/n-s2-ehrhart-polynomial-not-lattice.json` | `Ehrhart polynomial rational polytope period collapse not realized by a lattice polytope` | 20 | HTTP 429 twice | gap (rate limit) |
| Crossref | `crossref/n-cr-stapledon.json` | `Inequalities and Ehrhart delta-vectors` | 10 | 10 | top_k (bibliographic) |
| Crossref | `crossref/n-cr-hibi-lower-bound.json` | `A lower bound theorem for Ehrhart polynomials of convex polytopes` | 10 | 10 | top_k (bibliographic) |
| zbMATH Open | `zbmath/n-zb-hstar-inequalities.json` | `h*-vector inequalities lattice polytope` | 20 | 14 of 14 | complete |
| zbMATH Open | `zbmath/n-zb-scissors-unimodular.json` | `scissors congruence unimodular` | 20 | 3 of 3 | complete |

## 2. Hits worth reading

| work | identifier | what it did | read |
|---|---|---|---|
| Haase, McAllister 2008 | arXiv:0709.4070v1 | Example 2.4: a rational quadrilateral with quasi-period 1 whose Ehrhart polynomial is that of no integral polygon (two boundary points, linear coefficient 1 against the lattice bound 3/2); Problem 4.5: no Dehn-like invariant for GL_n(Z) is known. | full (`reading-haase-mcallister-2008-3`) |
| Turner, Wu 2014 | arXiv:1412.0196v1 | Theorem 1.4 and Section 3: two Ehrhart-equivalent denominator-5 minimal triangles T(1,2), T(1,4) that are not finitely rationally discretely equidecomposable, separated by an edge weighting W invariant under such decompositions (Corollary 3.18: for minimal triangles, equidecomposable iff G-equivalent iff equal W). | full (`reading-turner-wu-2014-3`) |
| Bohnert 2024 | arXiv:2405.13404v2 | Half-integral polygons with period collapse whose (i, b) pairs (b = 2, or b = 2i + 7) no lattice polygon realizes; Corollary 2.2, a criterion for period collapse of half-integral polygons. | full (`reading-bohnert-2024-3`) |
| Alexandersson, Hopkins, Zaimi 2022 | arXiv:2206.02276v2 | Restricted Birkhoff polytopes: period collapse with vertices of unbounded denominator (Remark 6.2); a non-hive family where the conclusion of the statement is not known either. | full (`reading-ahz-2022-3`) |
| Ferudun 2026 v2 | arXiv:2607.22301v2 | Proposition 11: a five-part hive with a negative Berline-Vergne edge weight (the local positivity route fails pointwise at codimension five); Section 9: the obstructions to rank-uniform shortcuts. | full (`reading-ferudun-2026-3`) |
| Ghodsi 2026 | arXiv:2609.14357v1 | The monomial coefficients are nonnegative throughout the seven-part size-thirty box (Theorem 19); a disproof of the consequence N4 or of the statement through negative monomial coefficients is excluded there. | full (`reading-ghodsi-2026-3`) |
| De Loera, McAllister 2006 | arXiv:math/0501446v1 | Lattice-point enumeration of hive polytopes; stretching experiments with no negative coefficient. | full (`reading-dlm-2006-3`) |
| Erbe, Haase, Santos 2019 | arXiv:1807.09485v1 (Proc. AMS 147) | Ehrhart-equivalent lattice 3-polytopes are GL_3(Z)-equidecomposable: in the integral case the Ehrhart polynomial is a complete invariant up to dimension 3. | abstract |
| Abney-McPeek et al. 2021 | arXiv:2101.08771v1 | Conjecture that Ehrhart-equivalent integral n-polytopes are equidecomposable into 1/(n-1)!-unimodular simplices; the integral case only. | abstract |
| Balletti, Higashitani 2018 | arXiv:1703.09600v1 (Israel J. Math.) | Universal inequalities: h*_1, h*_2 satisfy Scott's inequality whenever h*_3 = 0, independently of dimension and degree. | abstract |
| Beck, Deligeorgaki, Hlavacek, Valencia-Porras 2024 | arXiv:2210.12271v1 (Adv. Geom. 24) | Inequalities among the coefficients of f*-vectors of lattice polytopes (binomial basis binom(n-1, j)). | abstract |
| Stapledon 2009 | DOI 10.1090/s0002-9947-09-04776-x (Trans. AMS) | Inequalities for Ehrhart delta-vectors (the source of the inequalities the census probe tests). | record (Crossref) |
| Hibi 1994 | DOI 10.1006/aima.1994.1042 (Adv. Math.) | The lower bound theorem for Ehrhart polynomials. | record (Crossref) |
| Hibi 1990 | DOI 10.1016/0012-365x(90)90226-8 (Discrete Math.) | Results on Ehrhart polynomials of convex polytopes (the 1990 inequality). | record (Crossref) |
| Lev, Liu 2018 | arXiv:1804.09920v2 | Equidecomposability by lattice translations, a different group; out of scope. | abstract |
| Equivariant Hilbert and Ehrhart series under translative group actions | arXiv:2312.14088 | Equivariant Ehrhart series for translative actions (a Semantic Scholar hit of the retried query); not an invariant of unimodular equidecomposability; out of scope. | record (Semantic Scholar) |

The eight hits of the retried Semantic Scholar query are Abney-McPeek et al. 2021, Turner-Wu
(the arXiv version and the Discrete Comput. Geom. 2020 version, DOI
10.1007/s00454-020-00211-1), Haase-McAllister 2008, Luo 2026, the equivariant series paper
above, a 2015 dissertation on matroid h-vectors and a 1991 DIMACS volume; none adds an
invariant or a construction to the list above.

## 3. What was learned, as constraints on the plan

Range searched with no hit. Two exploratory probes of the common workspace (no native
credit): `hstar-inequalities-1` tests the five h*-inequalities (nonnegativity, the interior
bound h*_d <= h*_1, Hibi's lower bound, Stanley's inequality, Hibi's 1990 inequality) on
6,855,302 certified hive polynomials of five, six and seven parts and size at most 30
(38,550 distinct (parts, dimension, denominator, h*) keys, vertex denominators up to 6) and
finds no violation; `dim2-hives-1` tests Scott's inequality and b >= 3 on the 52,671
two-dimensional hive polytopes of at most five parts and size at most 22 and finds every
polynomial realizable by a lattice polygon. Monomial positivity holds for at most five parts
(Ferudun 2026) and throughout the seven-part size-thirty box (Ghodsi 2026). No computed
necessary condition is violated anywhere in the record. Any later search starts above these
ranges, or tests conditions these did not: the universal inequalities of Balletti-Higashitani
(when h*_3 = 0) and the f*-vector inequalities of Beck et al. are necessary conditions the
census did not test.

Constructions in print and their resource. Every known rational polytope with period
collapse whose Ehrhart polynomial is not that of a lattice polytope is two-dimensional:
Haase-McAllister's quadrilateral (Example 2.4) and Bohnert's half-integral polygons with
b = 2 or b = 2i + 7. Every known pair of Ehrhart-equivalent rational polytopes that is not
finitely equidecomposable is two-dimensional with denominator 5 (Turner-Wu); the separating
tool is an edge weighting on minimal triangulations that the authors say does not extend to
higher dimension. No invariant of GL_D(Z)-equidecomposability other than the Ehrhart
polynomial (hence volume, h*-vector, f*-vector) is known in dimension at least 3
(Haase-McAllister Problem 4.5), and in the integral case the Ehrhart polynomial is complete
up to dimension 3 (Erbe-Haase-Santos). None of the constructions is a hive polytope.

Near misses and the conditions each passes. The quadrilateral of Example 2.4 and Bohnert's
polygons pass period collapse and fail the conclusion of the statement, so the hypothesis
"rational polytope with quasi-period 1" is not sufficient and a proof must use the hive
structure; they do not pass "is a hive polytope" (hive polytopes of dimension 2 in the
computed range all pass Scott). Turner-Wu's triangles pass Ehrhart equivalence and fail
finite equidecomposability; they are not lattice polytopes and not hives.

Consequences for the entries. The counterexample space is compressed by necessary
conditions and a finite range (question 4 of the precondition): a counterexample must have
n >= 5 parts (Buch 2000), dimension at least 2 (dimension 1 is settled), a non-integral
vertex, and either an Ehrhart polynomial that no lattice polytope realizes (which in
dimension 2 means a violation of Scott's inequality or b <= 2, found nowhere in the computed
range) or a separation by an invariant finer than the Ehrhart polynomial, which exists in
print only in dimension 2. The entry extract-structure-from-a-hypothetical-counterexample
therefore produces a condition list and a structured residual class (dimension-2 hives
beyond the computed box, and hives of dimension at least 3 whose polynomial passes every
known inequality); it cannot produce a contradiction with a known theorem, because no
theorem excludes that class. The entry test-strengthenings-by-counterexample applies to the
Ehrhart form N1 and the consequence N4, whose small instances are computable: the record's
censuses are the hand-check part of that test and have found no refutation. The record of
constructions is two-dimensional only, so decide-the-direction-from-construction-cost has
no construction of the kind the statement quantifies over (a hive) and is not dispatched.

## 4. Stop reason

The queries ran dry: the three arXiv queries returned only works in the record or the
integral case of Question 4.1; zbMATH and Crossref returned the sources of the known
inequalities and no construction beyond those listed; the Semantic Scholar queries were
rate-limited (recorded gap). Two consecutive sources returned nothing new.
