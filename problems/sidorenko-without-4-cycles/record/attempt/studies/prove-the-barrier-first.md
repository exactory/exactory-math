# Strategy study: prove-the-barrier-first

Node: the statement on the girth-six patterns outside the class C_2 (the class with a bipartition in which one side has
maximum degree at most two), attacked in the negative direction by transferring the mechanism of [161] (the reported
counterexample). Study written on 2026-10-21. Question of the study: how have barrier and near-miss arguments been made
for Sidorenko-type inequalities, and what must a barrier for the mechanism of [161] state?

## 1. Queries run

Saved in the workspace under `sources/study-queries/`; the manifest `manifest.json` records the URL, the capture time,
the HTTP status and the totals of each.

| Source | Query | Result |
|---|---|---|
| arXiv API | `abs:Sidorenko AND (abs:"sum of squares" OR abs:barrier OR abs:obstruction OR abs:"not weakly norming" OR abs:"fold-stable")` (`bar-arxiv-sidorenko-method-limits`, 2026-10-21T23:04:33Z) | complete: 7 of 7 |
| Semantic Scholar | `Sidorenko conjecture barrier sum of squares` (`bar-s2-sidorenko-barrier`, 2026-10-21T23:07:41Z) | unavailable: HTTP 429 on four attempts with 30, 60 and 90 second waits |
| Crossref | `query.bibliographic=Sidorenko conjecture barrier sum of squares certificate` (`bar-cr-sidorenko-barrier`, 2026-10-21T23:09:46Z) | top 20 of 287,470 by relevance; none concerns graph homomorphism densities (sum-of-squares certificates for other conjectures, control barrier functions) |
| zbMATH Open | `Sidorenko & squares` (`bar-zb-sidorenko-squares`, 2026-10-21T23:09:52Z) | complete: 5 of 5; Garg, Raymond and Redlich (zbMATH 1582.05151), Collins, Galvin, Kelley and McMillon, "Characterizing graphs as algebraic squares" (arXiv:2510.05372), and three proceedings volumes |

The common-store searches of `problem.md` are not repeated here.

## 2. Hits worth reading

- [161], the reported counterexample (full text, `reading-openai-sidorenko-2026`; copy in `sources/`). The mechanism to
  be bounded: Lemma 3.1 (rank-layer limit, Equation (3.2)), Equation (3.4) (parity factors on pairs in two faces),
  Lemma 3.2 (coordinate expansion), Sections 3.3 to 3.5 (one negative term, pinning, dilution), Proposition 3.5
  (symmetrization t(H, V) = t_{I,J}(W) t_{I,J}(W^⊤)), Lemma 3.6 (finite host).
- Lee and Schülke 2019, arXiv:1910.08454v2 (full text): K_{5,5} minus C_10 and the twisted blow-ups of cycles are not
  weakly norming, proved through Hessian matrices of homomorphism densities; a limit of the norming method, not of the
  Sidorenko property.
- Kral, Martins, Pach and Wrochna 2019, arXiv:1802.05007v4 (full text): many bipartite graphs fail the step Sidorenko
  property, and some bipartite edge-transitive graph is not weakly norming.
- Conlon and Lee 2017, arXiv:1611.05784v2 (full text): cut-percolation, the technique that proves weak norming.
- Blekherman, Raymond, Singh and Thomas 2018, arXiv:1812.08820v1 (abstract): a simple condition under which a graph
  density expression is not a sum of squares; the smallest open case of Sidorenko's inequality has no sum-of-squares
  certificate.
- Garg, Raymond and Redlich 2022, arXiv:2206.10058v1 (abstract): the inequality has no sum-of-squares certificate when
  the pattern is a trivial square; the patterns with at most 7 edges whose inequality has such a certificate are
  classified.
- Coregliano 2024, arXiv:2408.14257v2 (abstract): cut-percolation is the only known technique for weak norming, and it
  is obstructed exactly by non-monochromatic fold-stable colourings of the edges.
- Doležal, Grebík, Hladký, Rocha and Rozhoň, arXiv:1809.03797v5 (abstract): a connected graph is weakly norming if and
  only if it is step Sidorenko.
- Lovász 2011, arXiv:1004.3026v1 (full text): local Sidorenko holds for every bipartite graph, so no barrier exists in a
  neighbourhood of the constant graphon.

## 3. What was learned, as constraints on the plan

1. Barriers in this field are method-relative: each names the admissible class of a method (sum-of-squares
   certificates, cut-percolation, the step property) and shows that the class cannot certify, or cannot refute, the
   target. A barrier for [161] must likewise name its admissible class: kernels of the form (3.6) whose limiting moments
   are given by the sign model (3.2), with arbitrary finite type, coordinate and activation data.
2. The decisive property is written down in [161] itself: after Equation (3.4), every fully active pair "tests the
   parity of its four incidence signs". The attack must check whether a pattern of girth at least six has any pair of
   points in two faces; if it has none, the method's optimum equals the Sidorenko value (a near miss with equality),
   which is entry step 2 of `axiomatise-the-method-and-build-a-near-miss` ("prove that the optimum over the method's
   admissible family equals the stalled value").
3. The barrier must be conditional where [161] is: Lemma 3.1 is proved only for the 35-vertex complex, whose faces are
   triples; for any other pattern the limit formula is an assumption of the route. The statement of the barrier must
   say so.
4. The barrier must not claim more than the limit: the o(1) error at fixed q is not controlled by [161], so a vanishing
   deficit at finite q is outside its scope.
5. The tightness check of step 5 of the entry is available: on a pattern with a 4-cycle the sign model takes the values
   0 and 2, which is what [161] exploits.

## 4. Stop reason

A fixed count: one query per tier-one source. The arXiv and zbMATH queries were complete and returned only works
already known to this record or outside the question; none treats the construction of [161]. Semantic Scholar was
unavailable (rate limit), recorded as a gap.

## Appendix: the passages of [161] that the barrier uses

Transcribed from the text extracted from the PDF (`studies/sources/openai-161-counterexample.txt` of this attack root,
sha256 `3530e151fe7dd587af079b46e79fc213bc31f238ee71f5b6dde86a99a0471a77`; line numbers of that file in brackets).
The equations are re-typeset in plain notation; the full text is the authority.

- Setting [300-304]: I = {0, ..., 12}, J = {0, ..., 21}; each j in J is a three-element subset of I (a face); "Let E
  be the set of unordered point pairs contained in a face"; H = (I ⊔ J, C) with C = {(i, j) : i ∈ j}.
- Proposition 2.1, item 1 [353]: "Every pair in E lies in exactly two faces, |E| = 33, and the face-neighbor graph is
  connected."
- Kernel [431-443]: for an even dimension D = 2r and an odd prime q, K_ξ(Z) = 1{rank Z = r, sign(Z) = ξ} divided by
  P(rank Z' = r, sign(Z') = ξ) for uniform symmetric D-by-D matrices Z' over F_q, ξ ∈ {1, -1}, and c_0 = χ((-1)^r),
  where χ is the quadratic character; K_ξ ≥ 0 and E K_ξ = 1.
- Lemma 3.1 (rank-layer limit) [444-455]: "There is an integer D_0 such that, for every fixed even D ≥ D_0, the
  following assertion holds as q tends to infinity through odd primes. Let X_i, i ∈ I, and Y_j, j ∈ J, be independent
  uniform elements of S_D. For every set B ⊆ C and every choice of signs ξ_ij ∈ {1, -1} on B,
  E ∏_{(i,j)∈B} K_{ξ_ij}(X_i − Y_j) = E_η ∏_{j∈J} ∏_{e={i,k}⊂j, (i,j),(k,j)∈B} (1 + c_0 η_e ξ_ij ξ_kj) + o(1),   (3.2)
  where the η_e, e ∈ E, are independent uniform signs. The error is uniform over all such B and sign choices. The same
  assertion holds with Y_j − X_i in place of X_i − Y_j."
- Equations (3.3) and (3.4) [456-470]: for e = {v, w} ∈ E with faces j, l, U_e = {(v, j), (w, j), (v, l), (w, l)}. "If
  only one of the two face factors on e is present, its average over η_e is 1. If both are present, their average is
  1 + ∏_{κ∈U_e} ξ_κ, since c_0² = 1. Independence of the η_e therefore gives" that the right side of (3.2) equals
  ∏_{e∈E, U_e⊆B} (1 + ∏_{κ∈U_e} ξ_κ).   (3.4)
  [471] "Thus every fully active pair tests the parity of its four incidence signs, contributing 0 or 2."
- Densities [479-484]: t_{I,J}(W) = E ∏_{(i,j)∈C} W(x_i, y_j) with independent x_i ∈ X and y_j ∈ Y, and
  W^⊤(y, x) = W(x, y).   (3.5)
- Kernel of the construction [494-510]: X = A × S_D^K and Y = B × S_D^K for finite type sets A, B with distributions
  π, ν and a finite coordinate set K; for each type pair a law on subsets S ⊆ K with signs (ξ_κ)_{κ∈S}, and
  W_q((a, x), (b, y)) = E_{S,ξ | a,b} ∏_{κ∈S} K_{ξ_κ}(x^κ − y^κ).   (3.6)
  "For fixed types, averaging over the matrices gives one ... Therefore E W_q = 1, for every q."
- Lemma 3.2, proof [553-559]: "Conditional on all types, sample an activation law independently at each incidence when
  expanding the product in Equation (3.5). Conditional on these samples, the matrix integral factors across
  coordinates. At coordinate κ apply Lemma 3.1 with the active set of incidences for which κ ∈ S, and with their
  sampled signs. Use Equation (3.4) at each coordinate. There are only finitely many activation and sign
  configurations. ... A finite product and then the finite average therefore preserve the o(1) error."
- Proposition 3.5, proof [834-843]: V((x, y), (x', y')) = W(x, y') W(x', y) on Ω = X × Y; "In its product over H,
  the factors using x_i for i ∈ I and y_j for j ∈ J are independent of those using y_i for i ∈ I and x_j for j ∈ J.
  Therefore t(H, V) = t_{I,J}(W) t_{I,J}(W^⊤)". The identity uses only that H is bipartite with parts I and J.
