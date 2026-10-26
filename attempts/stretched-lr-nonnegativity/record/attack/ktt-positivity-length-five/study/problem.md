# Problem-level study: the rank-five rung

Date: 2026-09-05. This attack is the child of `ktt-positivity-conjecture` opened at its move 1;
the parent's problem-level study (`../ktt-positivity-conjecture/study/problem.md`, queries Q1-Q7
of 2026-09-05) is the general survey of the proof side and is not repeated. This record settles
what is known at rank five specifically, and what the remaining statement costs.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| R1 | Ferudun 2026 LaTeX source (inherited) | Theorem 3 and Section 6, the rank-uniform and five-part section | 2026-09-05 | the exact statement of what rank five leaves open, and the example showing the non-full-dimensional case is not reduced by Horn factorisation |
| R2 | replay repository (inherited) | `proof/r5/R5_CODIM4_LOCAL_POSITIVITY_REPORT.md` (196 lines), `R5_AUDIT_VERDICT.md`, `alpha5.py`, `polytope5.py`, `hive5.py`, `GENERALIZATION_REPORT.md` | 2026-09-05 | the codimension-four enumeration and its counts; the 27 normals; the closed weight formula in dimension two; the absence of the codimension-four script |
| R3 | parent study, inherited | Castillo-Liu Lemmas 3.3 and 3.10; Berline-Vergne arXiv:math/0507256; Ring-Schuermann arXiv:1709.10390 | 2026-09-05 | closed formulas exist only in dimensions two and three; local formulas are not unique, and the freedom is an affine space |
| R4 | this project's finished attacks | `../stretched-lr-polynomial-negative-coefficient/deterministic/enumeration-run-2` and `certified-special-case-check-1`; `../stretched-lr-negative-coefficient-unbounded/deterministic/counterexample-search-run-1` | 2026-09-05 | 1,334,669 exact five-part Ehrhart polynomials of size at most 30, each certified by two independent programs, of which 13,217 are full-dimensional; 400,000 more sampled five-part polynomials of sizes 31 to 200 |

## 2. Hits worth reading

- Ferudun 2026, Theorem 3 and Section 6. At rank five the hive polytope has dimension at most six.
  For a full-dimensional one the coefficients of t^6, t^5, t^4 and t^3 are positive by the
  rank-uniform codimension-0 to 3 argument, and the coefficient of t^2 by the codimension-four
  atlas (all C(27, 4) = 17,550 four-normal tuples; 903 nonsaturated tuples with minimum weight
  1/14400; 132 negative saturated cells, extreme value -66821/2858240 at the normal identifiers
  (0, 7, 23, 25), each repaired by a slack closure into pointed rank-preserving closed supersets
  of minimum weight 739/86400). What is left is the linear coefficient, at codimension five, and
  the non-full-dimensional hives of intrinsic dimension at least three, whose transverse cones
  are projections of N_5; the example lam = (4,3,3,1), mu = (4,2,1,1), nu = (6,5,4,2,2) has
  dim H = 3 with all 142 essential Horn inequalities strict, so Horn factorisation does not
  dispose of that case.
- Castillo-Liu Lemmas 3.3 and 3.10 (through the codimension-three report). The weight of a
  saturated simplicial cone is 1/4 + (1/12)(C/A + C/B) in dimension two and
  1/8 + (1/24) sum_{i<j} (G^{-1})_{ij} (1/(G^{-1})_{ii} + 1/(G^{-1})_{jj}) in dimension three,
  with G the Gram matrix of the primitive normals. Nothing of this kind is in print in dimension
  four or five, and the source's dimension-four script is not distributed.
- Ring and Schuermann, arXiv:1709.10390. A McMullen local formula is a weight function on
  transverse cones such that the count is the weighted sum of face volumes; the valid weights
  form an affine space, not a point. This is what makes a second, elementary route possible: the
  weights of a valid local formula on the cone types that actually occur are constrained by the
  Ehrhart data of the polytopes that realise them, and if that data pins them, the pinned values
  are the weights of some valid local formula whatever construction produced them.
- The certified data of this project. 1,334,669 five-part Ehrhart polynomials of size at most 30,
  each computed by Normaliz from the hive inequalities and independently pinned by lrcalc counts
  with exact interpolation, of which 13,217 are full-dimensional; and 400,000 sampled five-part
  polynomials of sizes 31 to 200 with the same certification. Each carries its exact coefficients.

## 3. What was learned, as constraints on the plan

1. The remaining statement at rank five is exactly two finite lists: (a) the weight on the
   five-dimensional transverse cones of edges of full-dimensional five-part hives, and (b) the
   non-full-dimensional five-part hives of intrinsic dimension three, four and five.
2. The route in print needs the weight in dimension five, for which there is no closed formula
   and no distributed implementation, so following it means implementing the local
   Euler-Maclaurin recursion first.
3. A second route avoids that implementation. Because the valid local formulas form an affine
   space and the weight of a face depends only on its transverse cone type, the identity
   a_1(P) = sum over edges E of P of w(type(E)) times the lattice length of E is a linear equation
   in the unknown weights, one per polytope, with an exactly known right-hand side for every
   polytope of this project's certified records. If the equations coming from the recorded
   polytopes pin w on the types that occur, then the pinned values are the weights of every valid
   local formula on those types, since a valid formula exists by McMullen's theorem and satisfies
   the same equations; their nonnegativity then proves a_1 >= 0 for every hive polytope all of
   whose edge types are pinned, and their enumeration against the finite atlas says which types
   remain. If instead the system is infeasible in the nonnegative orthant, that is a proof that no
   local formula is nonnegative at rank five, a barrier for the whole class.
4. The same construction is testable before it is trusted: at codimension two and three the
   pinned weights must agree with the closed formulas of Castillo-Liu, and at codimension four
   with the reported minimum 739/86400 of the source. A pipeline that fails those tests is wrong.
5. Routes not to duplicate: the codimension 0 to 4 atlases (in print), the enumeration of triples
   in a box, and the sampling beyond it.

## 4. Stop reason

Two readings of the source's rank-five material and of the replay repository, the parent's survey
of the proof side, and an inventory of this project's own certified data. The last source added
the second route and the tests that keep it honest; no further rank-five result was found.
