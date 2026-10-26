# Problem study: hive polytopes and lattice polytopes

Objective `objective-000001` of the attack root `attack/` (contract digest
`36fee328a7b0028ac7d6565458e2cb2b0edca9e5fcad192020e0c73de8203068`). The claim: for every
integer n >= 2 and every triple of partitions (lambda, mu, nu) with at most n parts,
|lambda| + |mu| = |nu| and c^nu_{lambda mu} > 0, the hive polytope H(lambda, mu, nu) in R^D,
D = binom(n-1, 2), is GL_D(Z)-equidecomposable with a lattice polytope Q (finitely many
relatively open rational simplices, affine unimodular maps, disjoint images whose union is a
lattice polytope), so that c^{t nu}_{t lambda, t mu} is the Ehrhart polynomial of Q.

The problem record of the common workspace (statement `statement-1`) declares five
neighbouring formulations, searched here together with the statement: (N1) the Ehrhart form,
some lattice polytope has Ehrhart polynomial c^{t nu}_{t lambda, t mu}; (N2) the
Haase-McAllister form, H is equidecomposable with a disjoint union of integral open simplices;
(N3) the Gelfand-Tsetlin sibling; (N4) the consequence that the numerator G(z) of the
generating function has nonnegative integer coefficients (King-Tollu-Toumazet 2004); (N5) the
rank restriction to partitions with at most n parts.

Dates: every query below was run on 2026-10-20. The study was written on 2026-10-20.

## 1. Queries

### 1a. Searches recorded in the common store (problem workspace)

All four are `literature_search` records of provider arXiv (API `export.arxiv.org`,
`sortBy=relevance`, `max_results=20`), responses captured 2026-10-20T20:05Z and recorded at
20:19Z. Every query returned fewer than 20 works, so each query's coverage is `complete`.

| record (digest) | query | returned | formulations |
|---|---|---|---|
| `search-direct-equidecomposability` (`32855ac1aebf81d98d6fb869ee34e981e8cd73f47eec6393e3958d4beacf4d81`) | q1 `all:"hive polytope" AND (all:"scissors congruence" OR all:equidecomposable OR all:"period collapse")` | 0 | statement, N2 |
| same | q2 `all:"Littlewood-Richardson" AND (all:"period collapse" OR all:"quasi-period" OR all:"scissors congruence" OR all:equidecomposable)` | 1 | statement, N1 |
| same | q8 `all:"rational polytope" AND all:"Ehrhart polynomial" AND (all:"lattice polytope" OR all:"integral polytope") AND (all:"quasi-period" OR all:"period")` | 1 | N1, statement |
| `search-theory-period-collapse` (`9811032a8ddd6b676ac4d83cb7438b8c18ad99ad72f29c1b9c407a1a44fce450`) | q3 `all:"scissors congruence" AND all:Ehrhart` | 2 | statement, N2 |
| same | q4 `all:"period collapse" AND all:Ehrhart` | 13 | N1, N2 |
| same | q7 `all:"Ehrhart equivalent" OR all:"Ehrhart-equivalent" OR all:"Ehrhart equivalence"` | 10 | N1 |
| `search-adjacent-gelfand-tsetlin` (`fc0c45a4daa2813a549af362040b6ba276ddf0d1383a72d182938afa259c088b`) | q6 `all:"Gelfand-Tsetlin" AND (all:equidecomposable OR all:"scissors congruence" OR all:"period collapse" OR all:"quasi-period" OR all:"Ehrhart polynomial")` | 7 | N3 |
| `search-recent-stretched-lr` (`d0f8e3a4ec3b9cc84c9cc5fd95977753aee0044bf76b56df95e2761acea80c76`) | q5 `all:"stretched Littlewood-Richardson" OR all:"hive polytope" OR all:"hive polytopes"` | 10 | N4, N5 |

Every returned work carries a disposition in the record (relevant, potentially relevant or
out of scope, with a reason); the twelve relevant works are read in full (section 2).

### 1b. Queries of this study (raw responses under `studies/queries/`, index in
`studies/queries/index.json`)

| source | file | query | requested | returned | coverage |
|---|---|---|---|---|---|
| arXiv API | `arxiv/p-arxiv-hive-unimodular.xml` | `all:hive AND all:unimodular AND all:polytope` | 20 | 0 of 0 | complete |
| arXiv API | `arxiv/p-arxiv-lr-ehrhart.xml` | `all:"Littlewood-Richardson" AND all:Ehrhart` | 20 | 4 of 4 | complete |
| arXiv API | `arxiv/p-arxiv-quasi-period-collapse.xml` | `all:"quasi-period collapse"` | 20 | 5 of 5 | complete |
| Semantic Scholar `graph/v1/paper/search` | `s2/p-s2-hive-equidecomposable.json` | `hive polytope equidecomposable lattice polytope` | 20 | 9 of 9 | complete |
| Semantic Scholar | `s2/p-s2-period-collapse-lattice.json` | `period collapse Ehrhart quasi-polynomial rational polytope lattice polytope` | 20 | HTTP 429 twice (second call 45 s apart) | gap (rate limit) |
| Semantic Scholar | `s2/p-s2-stretched-lr-ehrhart.json` | `stretched Littlewood-Richardson coefficients Ehrhart polynomial hive polytope` | 20 | HTTP 429 twice | gap (rate limit) |
| Semantic Scholar | `s2/p-s2-gt-period-collapse.json` | `Gelfand-Tsetlin polytope Ehrhart period collapse` | 20 | HTTP 429 twice | gap (rate limit) |
| Semantic Scholar | `s2/p-s2-ktt-numerator.json` | `King Tollu Toumazet positivity conjecture stretched Littlewood-Richardson generating function` | 20 | HTTP 429 twice | gap (rate limit) |
| Crossref `works?query.bibliographic` | `crossref/p-cr-haase-mcallister.json` | `Quasi-period collapse and GL_n(Z)-scissors congruence in rational polytopes` | 10 | 10 (top 10 by relevance) | top_k |
| Crossref | `crossref/p-cr-ktt-2004.json` | `Stretched Littlewood-Richardson coefficients and Kostka coefficients` | 10 | 10 | top_k |
| Crossref | `crossref/p-cr-derksen-weyman.json` | `On the Littlewood-Richardson polynomials` | 10 | 10 | top_k |
| Crossref | `crossref/p-cr-hive-equidecomposable.json` | `hive polytope equidecomposable lattice polytope Ehrhart` | 10 | 10 | top_k |
| zbMATH Open `document/_search` | `zbmath/p-zb-hive-polytope.json` | `hive polytope` | 20 | 9 of 9 | complete |
| zbMATH Open | `zbmath/p-zb-period-collapse.json` | `period collapse Ehrhart` | 20 | 17 of 17 | complete |
| zbMATH Open | `zbmath/p-zb-lr-ehrhart.json` | `Littlewood-Richardson Ehrhart polynomial` | 20 | 4 of 4 | complete |
| zbMATH Open | `zbmath/p-zb-equidecomposable.json` | `equidecomposable rational polytope` | 20 | 0 (status "No results found") | complete |

The Crossref queries are bibliographic resolutions: they confirm the venue and DOI of the
three works the statement rests on (section 2) and test a free-text combination; a
bibliographic top-10 is a bounded view, not an enumeration. The Semantic Scholar rate limit
(HTTP 429 on four of five calls) is recorded as a gap of this study; the openness review
rests on the complete arXiv searches of section 1a, the zbMATH searches and the readings.

## 2. Hits worth reading

Read in full (common `reading` records with complete coverage of every required unit):

| work | identifier | what it does | reading record |
|---|---|---|---|
| Haase, McAllister 2008 | arXiv:0709.4070v1; DOI 10.1090/conm/452/08777 (Contemp. Math. 452) | States Conjecture 3.2, verbatim: "Suppose that P is a rational polytope with quasi-period 1. Then there exists a disjoint union Q of integral open simplices such that P and Q are GL_n(Z)-equidecomposable.", Open Problem 3.3 (a systematic technique), Question 4.1 (does Ehrhart equivalence imply equidecomposability; yes in dimension 2 in Greenberg's sense [Gre93, Thm 1.3]), Proposition 4.3 (weak equidecomposability after a common dilation), Problem 4.5 (a Dehn-like invariant); Example 2.4 is a rational quadrilateral with quasi-period 1 whose Ehrhart polynomial is that of no integral polygon; names the Littlewood-Richardson polynomials (Derksen-Weyman) among the motivating examples of period collapse with no polyhedral proof. | `reading-haase-mcallister-2008-3` (`aae21c2354cdedad834a228e381555897b487a7ca68f25aa309e73f6a9454edc`) |
| Ferudun 2026 v2 | arXiv:2607.22301v2 | Proves the King-Tollu-Toumazet monomial-positivity conjecture for at most five parts (monomial coefficients only; this says nothing about the numerator N4 or about lattice realizability); the proof of Lemma 8 records, verbatim, "let q be the least common multiple of the denominators of the vertices of H. Then qH = {x : A_r x <= qb} has the same normal fan as H ... and its vertices are q times those of H, hence integral; thus qH is a lattice polytope. Since L_{qH}(t) = #(t qH n Z^D) = L_H(qt)"; Section 9 fixes the frontier (six or more parts below the top four coefficients) and the effectivity statement (HTE); notes that lower-dimensional five-part hives are not all reduced to four parts by Horn-facet factorisation (lambda = (4,3,3,1), mu = (4,2,1,1), nu = (6,5,4,2,2): dim H = 3, all 142 essential Horn inequalities strict). | `reading-ferudun-2026-3` (`3b3ddf996d37bc51489d886b756ae54239573863c1008e7623fb256b4c8370a7`) |
| King, Tollu, Toumazet 2006 | Sem. Lothar. Combin. B54Ad, https://eudml.org/doc/227653 | Restates the two 2004 conjectures (positive monomial coefficients; positive integer coefficients of the numerator G(z)); the hive model; factorisation Conjecture 4.3 when an essential Horn inequality is saturated. | `reading-ktt-2006-3` (`ab6abbdc4f71759b2a43ce9c1a1b8f265786a90c378f9203a048fa8808e35178`) |
| Rassart 2004 | arXiv:math/0308101v2 | Chamber polynomiality through Steinberg's formula; Corollary 4.2, the stretched coefficient is a polynomial (period collapse of hive polytopes, second proof); records that H is rational and non-integral in general. | `reading-rassart-2004-3` (`6fe3a9b00faff3da43d1043596af97dcda15d8959a935acfedb13870ea054c3a`) |
| Buch 2000 | arXiv:math/9810180v1 (Enseign. Math. 46) | The hive model and the saturation proof; Example 2, a hive polytope with a non-integral vertex ("a hive polytope over an integral border can still have non-integral corners"); immediately after it the remark, stated without a printed proof, "It is not hard to show that for n <= 4 and b in Z^B, all corners of rho^{-1}(b) n C are integral hives." (Section 1, before Section 2 "Flatspaces"). | `reading-buch-2000-3` (`f85945fdf911c0cd40691280fbd9045385a5377618261d3c6b1811abe014b675`) |
| De Loera, McAllister 2006 | arXiv:math/0501446v1 (Experiment. Math. 15) | Conjecture 4.5 and Theorem 4.6: the homogenized hive matrix has a unimodular triangulation for rank at most six, so every generalized hive polytope has an integral vertex; period collapse stated as Derksen-Weyman's theorem; stretching experiments. | `reading-dlm-2006-3` (`cd33775751acd78fb977cd4e175f57b151033f2a4dccd745b116f98f610309b3`) |
| Fernandes, de Pina, Ramirez Alfonsin, Robins 2018 | arXiv:1802.07164v1 | Theorem 3: the polytopes of two {1,3}-graphs with the same degree sequence are GL(Z)-equidecomposable, by a piecewise unimodular map attached to the weighted nearest-neighbour interchange (dissection by one or two hyperplanes per move). | `reading-fernandes-2018-3` (`f1fa638414ef9bbae57167c522091174fd6f7525f8060bdb0a8df61a2849d8b5`) |
| Turner, Wu 2014 | arXiv:1412.0196v1 | Theorem 1.4: Ehrhart-equivalent rational polygons need not be rationally discretely equidecomposable with finitely many pieces (denominator-five minimal triangles separated by an edge weighting); Theorem 1.5 and Conjecture 1.6 on infinite or irrational decompositions. | `reading-turner-wu-2014-3` (`ddf1f9dbd258b69a234c7b027f319a42b49999beaa9084b70b8cf9ca0b915aa5`) |
| Bohnert 2024 | arXiv:2405.13404v2 | Classifies the Ehrhart polynomials of half-integral polygons with period collapse: pairs (i, b) with b = 2 or b = 2i + 7 occur, which no lattice polygon realizes (Scott). | `reading-bohnert-2024-3` (`b5ba1f1fc81eb05bbed3e4c9e0a3be947735c0b13ec421384cf472405d5ce4e8`) |
| Alexandersson, Hopkins, Zaimi 2022 | arXiv:2206.02276v2 | Period collapse of restricted Birkhoff polytopes through Pak's piecewise-linear RSK, a lattice-respecting bijection to a Gelfand-Tsetlin polytope; records the Haase-McAllister conjecture and the KTT positivity conjectures as open. | `reading-ahz-2022-3` (`6be9fce8384df602f13e559a5e593bbafb707323a3f71369831558a2dfb105ec`) |
| Alexandersson, Alhajjar 2018 | arXiv:1812.03345v1 | The Gelfand-Tsetlin sibling: GT(lambda, mu) is rational with period collapse; Ehrhart positivity conjectures (7, 8, 10) open. | `reading-alexandersson-alhajjar-2018-3` (`900e1fdf0af41ea3c0698ac0b0908a8c7ae63c344b31503cb00fa6b6e6f501a8`) |
| Ghodsi 2026 | arXiv:2609.14357v1 | Theorem 19: monomial positivity over the seven-part size-thirty box; Theorem 12 restates the essential Horn factorization theorem (King-Tollu-Toumazet 2009, Theorem 1.4, in the subset formulation of Cho-Jung-Moon 2008). | `reading-ghodsi-2026-3` (`35f875777a59e3aca9b4e8562d99302f42627843061c95726b0cbbfa122ee025`) |

Read in full outside the common store (file saved under `studies/sources/`):

| work | identifier | what it does | status |
|---|---|---|---|
| Cho, Jung, Moon 2008 | DMTCS Proc. AJ (FPSAC 2008) 483-494, https://dmtcs.episciences.org/3592/pdf | Theorem 1.3 states the King-Tollu-Toumazet factorization theorem: if (I, J, K) are r-subsets of [n], r < n, with c^{pi(K)}_{pi(I) pi(J)} = 1 and sum_{k in K} nu_k = sum_{i in I} lambda_i + sum_{j in J} mu_j, then c^nu_{lambda mu} = c^{nu_K}_{lambda_I mu_J} c^{nu_{K^c}}_{lambda_{I^c} mu_{J^c}} and the stretched polynomials factor accordingly; gives hive and tableau bijections for the reduction cases r = 1, 2, n-1, n-2. | full text read on 2026-10-20 (`studies/sources/cjm2008.pdf`, `cjm2008.txt`) |

Abstract or record only:

| work | identifier | what it does | status |
|---|---|---|---|
| King, Tollu, Toumazet 2004 | DOI 10.1090/crmp/034/10 (CRM Proc. Lecture Notes 34) | The two positivity conjectures (monomial coefficients; numerator G(z)). | not available; cited through KTT 2006 (full) and Ferudun 2026 (full) |
| King, Tollu, Toumazet 2009 | DOI 10.1016/j.jcta.2008.06.005 (JCTA 116, 314-333) | The factorization theorem (their Theorem 1.4). | publisher page returned HTTP 403 to the download; statement read through Cho-Jung-Moon 2008 (full) and Ghodsi 2026 (full) |
| Derksen, Weyman 2002 | DOI 10.1016/s0021-8693(02)00125-4 (J. Algebra 255) | First proof that the stretched coefficient is a polynomial. | not read; cited as the period-collapse theorem by HM 2008, Rassart 2004, AHZ 2022 (all full) |
| Thawinrak 2022 | arXiv:2211.06810v2 (Ars Combin. 2025, DOI 10.61091/ars162-15) | A short third proof of polynomiality. | abstract (disposition potentially relevant in `search-recent-stretched-lr`) |
| Clarke, Higashitani, Zaffalon 2022 | arXiv:2211.07995v1 (zbMATH 1581.52011) | Restricted chain-order polytopes are related by combinatorial mutations, which preserve period collapse; the RSK bijection of AHZ is realized by mutations (AHZ Remark 6.5). | abstract (potentially relevant in `search-adjacent-gelfand-tsetlin`) |
| Ardila, Bliem, Salazar 2011 | arXiv:1008.2365v1 | Gelfand-Tsetlin and Feigin-Fourier-Littelmann-Vinberg polytopes as marked order and marked chain polytopes, Ehrhart-equivalent through a transfer map. | abstract (potentially relevant in `search-adjacent-gelfand-tsetlin`) |
| Ehrhart-equivalent 3-polytopes are equidecomposable | arXiv:1807.09485v1 | The integral case of Question 4.1 in dimension 3. | abstract (potentially relevant in `search-theory-period-collapse`) |
| McAllister, Moriarity 2015 | arXiv:1509.03680v1 | Ehrhart polynomials of pseudo-integral polygons. | abstract (potentially relevant) |
| Greenberg 1993 | Trans. Amer. Math. Soc. 335, 705-720 | Piecewise SL_2(Z) geometry; cited by HM for the affirmative answer to Question 4.1 in dimension 2. | record only (cited in HM 2008) |
| Multi-tiling and equidecomposability of polytopes by lattice translates | arXiv:1804.09920 | Equidecomposability under lattice translations, a different group. | abstract (Semantic Scholar hit); out of scope |
| Molev 2009 | DOI 10.1016/j.jalgebra.2008.02.034 | "Littlewood-Richardson polynomials" in the sense of equivariant Schubert calculus, unrelated to stretched coefficients. | record only (Crossref hit); out of scope |

## 3. What was learned, as constraints on the plan

1. No route in print attacks the statement, the Ehrhart form (N1) or the hive case of the
   Haase-McAllister form (N2). Haase-McAllister pose the general conjecture and name the
   Littlewood-Richardson polynomials as a motivating example without treating them; no later
   work found by the eight arXiv queries, the zbMATH and Crossref searches or the one
   completed Semantic Scholar search treats hive polytopes together with equidecomposability,
   scissors congruence or period collapse as a question. The attack duplicates nothing.
2. Period collapse is a premise, not a target. The polynomiality of c^{t nu}_{t lambda, t mu}
   is a theorem by three non-polyhedral routes (Derksen-Weyman 2002; Rassart 2004, Corollary
   4.2; Thawinrak 2022). The attack spends no move on it; it uses it as the hypothesis of the
   Haase-McAllister conjecture, which for hive polytopes is the form N2.
3. Settled and reported ranges, kept apart. Proved here: every hive polytope of dimension
   at most 1 is a lattice polytope (a rational segment whose dilates have polynomial
   lattice-point counts has lattice endpoints; the argument is written in the attack's move
   1 note), so the statement holds for n <= 3 (D <= 1) with Q = H. Reported, not proved in
   the source: for n <= 4 every hive polytope is a lattice polytope, which Buch 2000 states
   after Example 2 as "not hard to show" without a printed proof; this record treats n = 4
   as settled on Buch's authority and marks it as such wherever it is used. Non-integral
   vertices exist from five parts on (Buch 2000, Example 2, an explicit hive). Exploratory
   (no native credit): the scan `studies/scripts/instance_check.py` (output
   `instance_check.out.txt`) finds that among the five-part triples with |nu| <= 15 exactly
   five, all of size 15, have a hive polytope with a non-integral vertex; the first,
   nu = (5,4,3,2,1), lambda = (4,3,2,1), mu = (3,2) in the statement's notation, has
   dim H = 3 in R^6, six vertices, one of them half-integral, c = 5 and Ehrhart polynomial
   1 + 2t + (3/2)t^2 + (1/2)t^3. This instance is the seed candidate for an explicit
   equidecomposition; its minimality is an exploratory observation, not a theorem of this
   record, and nothing in the attack depends on it.
4. Necessary conditions in print, and the only known disproof tools. The Ehrhart polynomial
   is an invariant of GL_D(Z)-equidecomposability, so a disproof may come from a hive
   polynomial that no lattice polytope realizes: in dimension 2 Scott's inequality decides
   realizability (Bohnert 2024 shows half-integral polygons with period collapse can fail it,
   with b = 2 or b = 2i + 7); in higher dimension only necessary h*-inequalities are known.
   The two exploratory probes of the common workspace (`hstar-inequalities-1`, 6,855,302
   polynomials of five to seven parts and size at most 30; `dim2-hives-1`, 52,671
   two-dimensional hive polytopes of at most five parts and size at most 22) found no
   violation; they are exploratory, carry no native credit, their programs and outputs are
   held in the common workspace (`probes/`, `research/probes-manual/`) and not in this
   attack root, and even as certified facts they would exclude nothing outside their ranges
   and nothing that the tested inequalities do not detect. The attack uses them only to
   choose where to look, never as premises. Beyond the Ehrhart polynomial,
   the only invariant of finite unimodular equidecomposability in print is Turner-Wu's edge
   weighting for polygons (dimension 2, fixed denominator); Haase-McAllister's Problem 4.5
   (a Dehn-like invariant) is open. In dimension 2 the geometric statement is strictly
   stronger than the Ehrhart form: Turner-Wu, Theorem 1.4, prove that Ehrhart-equivalent
   rational polygons need not be finitely rationally discretely equidecomposable, which is
   the notion of the statement, while Haase-McAllister record an affirmative answer to
   Question 4.1 in dimension 2 from Greenberg [Gre93, Theorem 1.3] under Greenberg's own
   notion (Turner-Wu relate their open questions to a conjecture of Greenberg). So a
   dimension-2 case of the statement cannot be closed by Scott's inequality alone.
5. Mechanisms in print to transfer, none of which treats hives: a local combinatorial move
   turned into a piecewise unimodular map (weighted nearest-neighbour interchange, Fernandes
   et al. 2018); lattice-respecting piecewise-linear bijections (piecewise-linear RSK, AHZ
   2022; combinatorial mutations, Clarke-Higashitani-Zaffalon 2022); transfer maps between
   marked order and marked chain polytopes (Ardila-Bliem-Salazar 2011). All of these map a
   rational polytope to another rational polytope of the same family; none lands on a lattice
   polytope, which is what the statement asks for.
6. A structural reduction in print: the essential Horn factorization theorem (King-Tollu-
   Toumazet 2009; Cho-Jung-Moon 2008, Theorem 1.3; Ghodsi 2026, Theorem 12) factors the
   stretched polynomial when an essential Horn inequality is tight under the multiplicity-one
   subset condition. Whether the hive polytope itself is then unimodularly a product of the
   two smaller hive polytopes is not stated in the sources read; if it is, the statement
   reduces to primitive triples, with Ferudun's example showing that lower-dimensional
   five-part hives need not factor. This is an obligation for the constructive strategy, not
   a known fact.
7. The sibling N3 is in the same state: Gelfand-Tsetlin polytopes are rational, have period
   collapse (Kirillov-Reshetikhin; AHZ 2022 Theorem 2.1) and open positivity conjectures
   (Alexandersson-Alhajjar 2018); nobody has asked whether they are equidecomposable with
   lattice polytopes. A proof for hives would be expected to transfer, and a method that
   works for one family is a test for the other.
8. The consequence N4 is a known conjecture (KTT 2004, restated in KTT 2006 and AHZ 2022
   Remark 6.3); a proof of the statement implies it through Stanley's nonnegativity of the
   h*-vector of a lattice polytope; a disproof of N4 refutes the statement. No work in the
   record addresses the h*-vector of hive polytopes.

## 4. Stop reason

The queries ran dry: the three additional arXiv queries returned only works already in the
record or out of scope (q1-type queries return nothing), the four zbMATH queries and the
completed Semantic Scholar query returned no relevant work absent from the arXiv results,
and the Crossref resolutions confirmed venues without adding works. Two consecutive sources
(zbMATH, Crossref) returned nothing new. The four rate-limited Semantic Scholar queries
remain a recorded gap of this study.
