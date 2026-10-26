# Strategy study: prove-the-barrier-first (the unbounded conjecture)

Date: 2026-09-04. Which methods have been tried on Ehrhart positivity of hive polytopes and of
the neighbouring families, what property they share, and where each is known to stop. Contract:
`STUDY.md`.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| B1 | arXiv (MCP search) | `Berline-Vergne valuation Ehrhart positivity generalized permutohedra Castillo Liu`, 8 results by relevance | 2026-09-04 | 1509.07884 (Castillo-Liu), 1911.06291 (Lee-Liu), 2105.04465 (Ferroni), 1704.05532 (Castillo-Liu-Nill-Paffenholz), 1909.08448 (Jochemko-Ravichandran), 2110.10204 (Beck-Elia-Rehberg), 2607.03854 (Liu-Zhang), 2403.06975 (Behrend) |
| B2 | arXiv (MCP search) | `Ehrhart positivity local formula McMullen valuation counterexample negative coefficient Ferroni Higashitani survey`, 8 results | 2026-09-04 | 1709.10390 (Ring-Schuermann), 1812.06654 (Ring), 2608.28585 (Panzer), 2110.11549 (Fan-Li), 1711.09962 (Liu), 1506.00467 (Hibi et al.), 2607.03854, 1704.05532 |
| B3 | the problem's replay repository and Ferudun 2026 (read for the box attack) | `proof/GENERAL_KTT_PROOF_STATUS.md`, the (HTE) reduction and the codimension-4 cell | 2026-09-03 | the recorded state of the positive side |

## 2. Hits worth reading

- Castillo and Liu, "Berline-Vergne valuation and generalized permutohedra", arXiv:1509.07884
  (Discrete Comput. Geom.): Berline-Vergne's valuation writes each Ehrhart coefficient as a
  sum over faces of the face volume times a value depending only on the face's normal cone;
  positivity of the values on all faces of a family proves Ehrhart positivity of the family;
  the paper conjectured that integral generalized permutohedra are Ehrhart positive.
- Ferroni, "Matroids are not Ehrhart positive", arXiv:2105.04465: disproves the conjectures of
  De Loera-Haws-Koeppe (matroid polytopes) and Castillo-Liu (generalized permutohedra):
  matroid polytopes with a negative Ehrhart coefficient exist for every n >= 19. The method's
  termwise positivity therefore fails on a family that was expected to be positive.
- Lee and Liu, arXiv:1911.06291: Berline-Vergne's function positive on faces of codimension
  2 and 3 of Tesler polytopes, giving the third and fourth coefficients; the method is applied
  face-class by face-class and stops where the values are no longer computed positive.
- Castillo, Liu, Nill and Paffenholz, arXiv:1704.05532: smooth polytopes with negative
  coefficients; Berline-Vergne valuations discussed as a tool for positivity.
- Ring and Schuermann, arXiv:1709.10390 (and Ring, arXiv:1812.06654): McMullen's local
  formulas (Ehrhart coefficients as weighted sums of face volumes with weights depending only
  on outer normal cones) are far from unique; a construction from lattice tiles.
- Jochemko and Ravichandran, arXiv:1909.08448: Minkowski linear functionals on generalized
  permutahedra and Ehrhart positivity results for subfamilies.
- Panzer, arXiv:2608.28585: the Tutte polynomial determines the linear Ehrhart coefficient of a
  matroid polytope (a conjecture of Ferroni), an exact formula for one coefficient in one family.
- Ferudun 2026, arXiv:2607.22301 (read in full for the box attack): for hive polytopes,
  positivity for length <= 4 and the top four coefficients of full-dimensional hives are proved
  by the local (Berline-Vergne) formula with exact rational computation on the cells of low
  codimension; termwise positivity fails at codimension 4 (a cell of weight -349/28800), so a
  general proof cannot proceed cell by cell; the general conjecture is reduced to an
  effectivity statement (HTE) that is neither proved nor refuted.

## 3. What was learned, as constraints on the plan

1. The uniform property of the methods that reached hive polytopes: they are local formulas
   (McMullen, Berline-Vergne) evaluated termwise on faces, and they prove positivity exactly
   where every term of the chosen local formula is nonnegative on the family. For hives this
   stops at codimension 4 (Ferudun 2026); for matroid polytopes the same approach was
   conjectured to work and fails (Ferroni). The admissible class for a barrier is "proofs by
   termwise nonnegativity of one fixed local formula on the face classes of the family".
2. The barrier for that class on hives is already in the record: the codimension-4 cell of
   weight -349/28800 is a near miss inside the class (a hive face on which the fixed local
   formula's term is negative), stated by Ferudun 2026; a unit restating it would not be new.
   What is not in print is whether some other local formula (McMullen's are not unique) is
   termwise nonnegative on all hive faces; (HTE) is exactly this question in Farkas form.
3. The near miss of the negative side (the volume-2 few-point polytopes, ratio 24/25; the
   volume-3 one at 8 parts, ratio 393/406) passes every necessary condition of move 1 and is
   not a counterexample; a barrier theorem would have to show that the necessary conditions
   C1-C6 cannot be sharpened by the methods that produced them, which nothing in print does.
4. Route not to duplicate: the cell-by-cell Berline-Vergne computation at codimensions 1 to 4
   (Ferudun 2026) and its replay bundle.

## 4. Stop reason

Two arXiv searches by plain terms (the field-prefixed search of the tool returns nothing) and
the records read for the box attack; the second search added the local-formula literature
(Ring-Schuermann, Panzer) and nothing that changes item 1.
