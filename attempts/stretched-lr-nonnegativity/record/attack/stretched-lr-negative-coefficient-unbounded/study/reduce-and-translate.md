# Strategy study: reduce-and-translate (the unbounded conjecture)

Date: 2026-09-04. How the sign of an Ehrhart coefficient of a hive polytope has been carried into
another family of polytopes, and what is known about Ehrhart positivity in the families a hive
polytope maps to. Contract: `STUDY.md`. The box attack's record
(`../stretched-lr-polynomial-negative-coefficient/study/reduce-and-translate.md`, queries T1-T5
of 2026-09-03, sources under its `study/sources/`) is the starting point; the queries below are
the ones added for the unbounded statement, where the images are no longer confined to a box.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| U1 | arXiv (MCP search) | `abs:"transportation polytope" AND abs:Ehrhart`; `abs:"flow polytopes" AND abs:"Ehrhart" AND abs:positiv` | 2026-09-04 | 0 results each (the field-prefixed phrase search of this tool misses papers it finds with plain terms) |
| U2 | arXiv (MCP search) | `Ehrhart positivity flow polytopes Lidskii`, 10 results by relevance | 2026-09-04 | 1710.00701 (Meszaros-Morales), 1911.06291 (Lee-Liu), 1801.07684 (Benedetti et al.), 1806.08403, 2412.07164, 1711.09962, 2604.08394, 1804.08258 (Liu-Solus), 2409.16648, 2504.21395 |
| U3 | arXiv (MCP search) | `Ehrhart polynomial transportation polytopes negative coefficient Birkhoff`, 10 results | 2026-09-04 | math/0202267 (Beck-Pixton), 2206.02276 (Alexandersson-Hopkins-Zaimi), 1312.7049 and 1506.00467 (Hibi-Higashitani-Tsuchiya-Yoshida), 1704.05532, 1202.2652 (Breuer), 2410.01743 (Jiang), math/0402148 (Beck-De Loera-Develin-Pfeifle-Stanley), 1806.08403, 1711.09962 |
| U4 | Crossref | `query.bibliographic=Ehrhart positivity flow polytopes transportation polytopes Birkhoff`, 12 rows | 2026-09-04 | doi:10.1007/s00209-019-02283-z (Meszaros-Morales, Math. Z. 2019), doi:10.1007/s00454-022-00453-1 (Lee-Liu, DCG 2022), doi:10.1007/s00454-023-00611-z (Alexandersson-Hopkins-Zaimi, DCG 2023), doi:10.1142/9789811200489_0003 (Alexandersson, Ehrhart positivity and Demazure characters, 2019), doi:10.37236/4499 (Paffenholz, faces of Birkhoff polytopes), doi:10.5070/c65465670 (Jiang, positroid h*), doi:10.1016/0012-365x(90)90226-8 (Hibi 1990) |
| U5 | arXiv abstract pages | 1710.00701, 1911.06291 (read in full) | 2026-09-04 | see the hits |

## 2. Hits worth reading

- Meszaros and Morales, "Volumes and Ehrhart polynomials of flow polytopes", Math. Z. (2019),
  arXiv:1710.00701, doi:10.1007/s00209-019-02283-z: the Lidskii formula (volume and Ehrhart
  polynomial of the flow polytope of the complete graph with nonnegative integer netflows in
  terms of Kostant partition functions) proved by canonical polytopal subdivisions for arbitrary
  graphs. The abstract makes no claim of Ehrhart positivity for flow polytopes.
- Lee and Liu, "Ehrhart positivity of Tesler polytopes and Berline-Vergne's valuation", Discrete
  Comput. Geom. (2022), arXiv:1911.06291, doi:10.1007/s00454-022-00453-1: motivated by a
  conjecture of Morales, the third and fourth Ehrhart coefficients of the Tesler polytope
  Tes_n(1, ..., 1) are positive (Berline-Vergne's function positive on faces of codimension 2
  and 3), generalised to integral Tesler polytopes; full positivity stays open.
- Beck and Pixton, "The Ehrhart polynomial of the Birkhoff polytope", arXiv:math/0202267:
  volumes and Ehrhart polynomials of the Birkhoff polytopes B_n for n <= 8 (the sibling run
  `counterexample-search-run-2` reproduces B_3 and the volume of B_5).
- Alexandersson, Hopkins and Zaimi, "Restricted Birkhoff polytopes and Ehrhart period
  collapse", arXiv:2206.02276, doi:10.1007/s00454-023-00611-z: rational polytopes cut from the
  Birkhoff polytope whose Ehrhart quasi-polynomials are polynomials (period collapse), the same
  phenomenon the hive polytopes show (Derksen-Weyman).
- Liu and Solus, "On the relationship between Ehrhart unimodality and Ehrhart positivity",
  arXiv:1804.08258: h*-unimodality and Ehrhart positivity are independent properties in general.
- Hibi, Higashitani, Tsuchiya and Yoshida, arXiv:1312.7049 and 1506.00467; Castillo, Liu, Nill
  and Paffenholz, arXiv:1704.05532; Liu and Tsuchiya, arXiv:1806.08403; Liu, Xin and Zhang,
  arXiv:2412.07164: the known Ehrhart-negative families (each coefficient of t, ..., t^{d-2}
  negative for some polytope in every dimension d >= 4; smooth examples; order polytopes from
  dimension 14), as in the box attack's study.
- Ferudun 2026 (arXiv:2607.22301, read in full for the box attack): the strip construction maps
  any 3 x N transportation polytope T(r, c) with integer margins to the Littlewood-Richardson
  polytope of a fixed triple, compatibly with dilation (the 3 x 8 example is
  c^{nu}_{lam mu} with lam = (9,6,3), mu = (9,9,7,6,5,4,3,2,1), nu = (15,12,9,7,6,5,4,3,2,1)),
  so a negative Ehrhart coefficient of a transportation polytope refutes the conjecture; the
  codegree-3 3 x 8 family is Ehrhart positive (minimum linear coefficient 2157/280) and the
  recorded obstructions (hive tangent cones of determinant 2; a U_{2,4} restriction on tight-row
  systems) rule out flow-polytope and regular-matroid images of general hives.

## 3. What was learned, as constraints on the plan

1. The one map in print that lands in the hive family is the strip construction, stated for three strips: 3 x N transportation polytopes are Littlewood-Richardson polytopes, so the image statement "every 3 x N transportation polytope with integer margins is Ehrhart positive" is implied by the conjecture, and its negation would refute the conjecture. Whether k x N tables for k >= 4 are images is not in print (the sibling run 2 searched 4 x 4, 4 x 5 and 5 x 5 families as neighbours). Its pull-back is one-way (the image
   statement is weaker than the conjecture), so the translation pays `implication`.
2. Ehrhart positivity of transportation polytopes is not a theorem in print: the searches find
   partial results for related families (Tesler polytopes: the third and fourth coefficients;
   flow polytopes of the complete graph: volume and Ehrhart formulas via Kostant partition
   functions, no positivity claim; Birkhoff polytopes: computed to n = 8), and no source
   asserting positivity for transportation polytopes or reporting a negative one. The image
   statement is therefore open and computable in small cases: the destination has Lidskii-type
   formulas and the Berline-Vergne method that the origin lacks in usable form.
3. The other candidate images (order and marked order polytopes, flow polytopes, matroid
   polytopes) do not receive hive polytopes by any map in print, and the recorded obstructions
   of Ferudun 2026 say why; they are not maps for this strategy.
4. Route not to duplicate: the small-margin families of the sibling run
   (`counterexample-search-run-2`: 3 x 4 to 3 x 6, 4 x 4, 4 x 5, 5 x 5 with small totals, all
   positive) and the codegree-3 3 x 8 family of Ferudun 2026.

## 4. Stop reason

One query per tier-one source that answers (arXiv by two plain-term searches, Crossref), the two
abstracts read in full, and the box attack's record; the last two sources (Crossref and the
arXiv abstracts) added no map beyond the strip construction and no positivity theorem for
transportation polytopes.
