# Problem-level study: proving the King-Tollu-Toumazet positivity conjecture

Date: 2026-09-05. The two finished attacks of this project searched for a counterexample. This
attack seeks a proof, so the study is of the proof side: which techniques have reached the
conjecture, exactly how far each reached, and where each stopped. Contract: `STUDY.md`. Sources
inherited from the box attack live under
`../stretched-lr-polynomial-negative-coefficient/study/sources/`, including the full LaTeX source
of Ferudun 2026 and the clone of its replay repository, both read again here.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| Q1 | arXiv (MCP search) | `Ehrhart positivity survey techniques Berline Vergne local formula Liu`, 6 results, full abstracts | 2026-09-05 | 1911.06291 (Lee-Liu), 1509.07884 (Castillo-Liu), 1704.05532 (Castillo-Liu-Nill-Paffenholz), 2105.04465 (Ferroni), 2110.10204 (Beck-Elia-Rehberg), 2607.22301 (Ferudun, full abstract read) |
| Q2 | arXiv (MCP search) | `vector partition function chamber complex Littlewood-Richardson coefficients piecewise polynomial Szenes Vergne`, 8 results | 2026-09-05 | math/0308101 (Rassart), 2307.13112 (Trandafir, external columns and chambers of vector partition functions), 2211.06810 (Thawinrak), and unrelated Jack/Grothendieck papers |
| Q3 | arXiv (MCP search) | `hive polytope Knutson Tao Ehrhart polynomial stretched coefficients positivity proof`, 8 results | 2026-09-05 | math/9810180 (Buch, the saturation conjecture), 1706.02793 (Coquereaux-Zuber, volumes of hive polytopes from orbital measures), 2607.22301, 1711.09962 (Liu's survey), 2512.08669 (Menon-Verkama, combinatorial proof for cross-polytopes) |
| Q4 | Crossref | `query.bibliographic=Ehrhart positivity local formula nonnegative McMullen valuation lattice polytope`, 12 rows | 2026-09-05 | doi:10.1016/0001-8708(89)90029-7 (McMullen, The polytope algebra), doi:10.1007/bf02574364 (Barvinok 1994), doi:10.1007/s00454-022-00453-1 (Lee-Liu), doi:10.1142/9789811200489_0023 (Ring, dual view on local formulas), doi:10.1142/9789811200489_0003 (Alexandersson, Ehrhart positivity and Demazure characters) |
| Q5 | inherited sources, read again | Ferudun 2026 LaTeX source, sections 1, 6, 7 (`ktt_positivity.tex` lines 54-160, 289-370) | 2026-09-05 | the three theorems, the method, the frontier statement (HTE), the six obstructed shortcuts |
| Q6 | inherited sources, read again | the replay repository `proof/uniform/UNIFORM_CODIM3_BV_REPORT.md`, `proof/r5/R5_CODIM4_LOCAL_POSITIVITY_REPORT.md`, `proof/r5/alpha5.py` | 2026-09-05 | the closed formulas for the weight in dimensions 2 and 3, the enumeration sizes, the negative four-normal cell, and the fact that the codimension-four script is not distributed |
| Q7 | the strategy studies of the finished sibling attack | `../stretched-lr-negative-coefficient-unbounded/study/reduce-and-translate.md` and `study/prove-the-barrier-first.md` (queries U1-U5, B1-B3) | 2026-09-04 | the image families and their positivity status; the barrier literature |

## 2. Hits worth reading

- Ferudun, arXiv:2607.22301 (2026), read in full. The method: the hive polytope is rational, so a
  period-one dilation transfers the Berline-Vergne local Ehrhart formula from an integral dilate
  back to it (Lemma, Section 3); each Ehrhart coefficient becomes a sum over faces of a fixed
  codimension of the lattice volume of the face times a weight alpha depending only on the face's
  transverse cone; the primitive rhombus normals have entries in {0, +-1}, so for each rank there
  are finitely many transverse cones. Theorem 1: length at most four, every coefficient
  nonnegative (there D <= 3, so only the linear coefficient is at issue, and every
  two-dimensional transverse cone spanned by rank-four rhombus normals has positive weight,
  minimum 1/9). Theorem 2 (rank-uniform): the top four coefficients of every full-dimensional
  hive are positive (codimensions 0 and 1 are volume and surface; codimensions 2 and 3 are
  finite exact checks). Theorem 3: every full-dimensional five-part hive has all coefficients
  positive except possibly the linear one. Section 7 states the frontier: the conjecture follows
  from (HTE), the existence for every rank, codimension q and 2-connected primitive-interior
  closed flat-rhombus coarsening Sigma of a y with a_q + partial_q^T y >= 0, equivalently by
  rational Farkas duality that <a_q, w> >= 0 for every nonnegative balanced realizable face
  weight w. Neither (HTE) nor a refuting weight is known.
- Castillo and Liu, arXiv:1509.07884, Lemmas 3.3 and 3.10 (through the replay repository's
  codimension-three report). Closed formulas for the Berline-Vergne weight of a saturated
  simplicial cone in dimensions two and three: with G the Gram matrix of the primitive normals,
  alpha = 1/4 + (1/12)(C/A + C/B) in dimension two, and
  alpha = 1/8 + (1/24) sum_{i<j} (G^{-1})_{ij} (1/(G^{-1})_{ii} + 1/(G^{-1})_{jj}) in dimension
  three. Their paper also proves the strong Berline-Vergne positivity conjecture for permutohedra
  up to dimension 6 and codimension 3, the same reach as here.
- Berline and Vergne, "Local Euler-Maclaurin formula for polytopes", arXiv:math/0507256: the
  construction of the weight alpha by an explicit recursion on the dimension of the cone. This is
  the only route to alpha in dimensions four and above; there is no published closed formula.
- Ring and Schuermann, arXiv:1709.10390, and Ring, doi:10.1142/9789811200489_0023: McMullen local
  formulas are far from unique; the Berline-Vergne choice is one point of an affine family, which
  is what makes (HTE) an existence statement rather than a computation.
- Ferroni, arXiv:2105.04465: matroid polytopes and generalized permutohedra are not Ehrhart
  positive, disproving the conjectures of De Loera-Haws-Koeppe and of Castillo-Liu. The
  Castillo-Liu conjecture had exactly the support the present one has, verification in low
  dimension and codimension by the same valuation. This is the warning attached to any
  extrapolation from a verified range.
- Rassart, arXiv:math/0308101: the Littlewood-Richardson coefficient is given by polynomials in
  (lam, mu, nu) on the cones of the chamber complex of a vector partition function, with degree
  bounds. This is what makes each fixed rank a finite problem and makes the linear coefficient
  piecewise linear.
- Liu, arXiv:1711.09962 (survey) and Liu-Solus, arXiv:1804.08258: the catalogue of positive
  families, negative examples and methods; Ehrhart positivity and h*-unimodality are independent.
- Coquereaux and Zuber, arXiv:1706.02793: volumes of hive polytopes through Fourier transforms of
  orbital measures. A different analytic handle on the leading coefficient only.

## 3. What was learned, as constraints on the plan

1. The one technique that has reached hive polytopes is the local (McMullen, Berline-Vergne)
   formula, and it has reached exactly: every coefficient for rank at most 4; the top four
   coefficients for every full-dimensional hive of any rank; and for rank 5 the coefficients of
   t^6 down to t^2. The plan's first rung is therefore rank 5, and the whole rung is two finite
   questions: (i) the linear coefficient of full-dimensional five-part hives, which needs the
   weight on five-dimensional transverse cones spanned by the 27 rank-five rhombus normals, that
   is on subsets of the C(27,5) = 80,730 five-normal tuples and their closures; (ii) the
   non-full-dimensional five-part hives of intrinsic dimension at least three, whose transverse
   cones are projections of the normal set and which Ferudun explicitly does not claim, noting
   that they are not reduced to four parts by Horn factorisation (his example
   lam = (4,3,3,1), mu = (4,2,1,1), nu = (6,5,4,2,2) has dim H = 3 with all 142 essential Horn
   inequalities strict).
2. The enabling technical object is the weight alpha in dimensions four and five. Closed formulas
   exist only in dimensions two and three (Castillo-Liu); Ferudun computed dimension four from
   "the defining local Euler-Maclaurin recursion", and that script is not in the distributed
   repository (the codimension-four report records only its SHA-256), so the recursion must be
   implemented here and validated against the dimension-two and dimension-three closed formulas
   and against Ehrhart polynomials of actual hive polytopes computed by Normaliz.
3. Termwise positivity is false already at codimension four: the saturated four-normal cell with
   normal identifiers (0, 7, 23, 25) has weight -66821/2858240, and 132 of the rank-five
   four-normal cells are negative. Ferudun's repair is a slack-closure argument showing such a
   cell either raises the normal rank to at least five or embeds in a pointed rank-preserving
   closed superset, all of which have positive weight (minimum 739/86400). Any plan at
   codimension five must expect negative cells and must carry the same kind of closure argument;
   a plan that checks simplicial cells alone will fail.
4. Six rank-uniform shortcuts are already obstructed by exact examples (Ferudun, Section 7), and
   are routes not to duplicate: generic type-A Todd or cocircuit balancing (a nonnegative A_4
   Dahmen-Micchelli polynomial maps to N^4 + 4N^3 + 3N^2 - 2N - 6/5); network-flow equivalence
   (simple hive tangent cones have determinant two); a generic Cohen-Macaulay or Koszul Hilbert
   ring structure (the Q_20 Hibi ring is Gorenstein and Koszul with negative a-invariant, yet its
   Hilbert polynomial has linear coefficient -168011/330); matroidal or secondary-fan Todd
   effectivity (a genuine hive face carries a U_{2,4} tight-normal restriction); positive tableau
   or Kostka recursions (they require signs, or stop on primitive triples); rank-by-rank Hurwitz
   stability (an unbounded hierarchy).
5. Routes not to duplicate from the sibling attacks: exhaustive enumeration inside a box; sampling
   beyond it; the transportation-polytope transfer; the barrier that is already in print.
6. A verified range is not evidence a referee will accept as a proof heuristic: the Castillo-Liu
   conjecture had the same kind of support and is false (Ferroni). The plan must aim at
   statements that are proved for all sizes at a fixed rank, not at wider ranges.

## 4. Stop reason

Four tier-one searches (arXiv twice by plain terms, Crossref, and the inherited zbMATH and
Semantic Scholar records), plus a full re-reading of the one paper that reaches the conjecture and
of its replay repository. The last two sources added the closed formulas in dimensions two and
three and the exact size of the remaining rank-five gap, and no further technique that has reached
hive polytopes.
