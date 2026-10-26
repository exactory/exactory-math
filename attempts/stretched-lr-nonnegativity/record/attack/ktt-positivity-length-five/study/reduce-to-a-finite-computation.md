# Strategy study: reduce-to-a-finite-computation at rank five

Date: 2026-09-05. The parent attack's study of this strategy
(`../ktt-positivity-conjecture/study/reduce-to-a-finite-computation.md`, queries F1-F4 of
2026-09-05) settles how this statement has been finitised, what the last settled value is, which
certificates were replayable, and where the residue stops. This record settles the three things
the strategy's step 1 asks for at this rank, and adds the inventory of what this project can
compute with.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| C1 | inherited replay repository | `proof/r5/R5_CODIM4_LOCAL_POSITIVITY_REPORT.md`, sections on the enumeration, the negative cells and the closure | 2026-09-05 | the codimension-four method and counts in full, and the statement that the linear coefficient is outside the audit |
| C2 | inherited replay repository | `proof/r5/hive5.py`, `polytope5.py`, `alpha5.py` | 2026-09-05 | the 27 rank-five normals and the 342 nonparallel pairs are computed by distributed code; the weight code is distributed only in dimension two |
| C3 | this project's records | `../stretched-lr-polynomial-negative-coefficient/deterministic/enumeration-run-2/README.md` and `certified-special-case-check-1/README.md`; `../stretched-lr-negative-coefficient-unbounded/deterministic/counterexample-search-run-1/README.md` | 2026-09-05 | 1,334,669 certified five-part polynomials of size <= 30 with 13,217 full-dimensional; 400,000 more of sizes 31..200; every record carries exact coefficients, the dimension and the vertex denominators |
| C4 | parent study | Ring-Schuermann on the non-uniqueness of local formulas; McMullen's polytope algebra | 2026-09-05 | the affine space of valid weights, which is what makes the inverse determination legitimate |

## 2. What was learned, as constraints on the plan

1. Last value settled by computation at this rank, with encoder and solver: the coefficient of
   t^2, by enumerating all C(27, 4) = 17,550 four-normal tuples of N_5, evaluating the
   Berline-Vergne weight by the defining local Euler-Maclaurin recursion in exact rational
   arithmetic, and repairing the 132 negative saturated cells by slack closure into pointed
   rank-preserving closed supersets of minimum weight 739/86400. The solver is exact rational
   arithmetic; the enumeration is over normal tuples, not over polytopes.
2. Independent checkers: the rank-five codimension-two data has a distributed replay script with
   self-tests; the codimension-four computation has none, only a recorded hash. So the value this
   attack needs at codimension five has no reference implementation to check against, and the
   attack must build its own check: the weights it determines must reproduce the closed formulas
   at codimensions two and three and the reported minimum at codimension four.
3. The residue at this rank stops exactly at two lists, (a) codimension five for full-dimensional
   hives and (b) the non-full-dimensional hives of intrinsic dimension three to five. Sizes are
   not part of the residue.
4. The route this attack takes, and why it is available here and not in the source: a valid local
   formula assigns to each face a weight depending only on its transverse cone type, so for every
   polytope P of the family the identity a_1(P) = sum over the edges E of P of w(type(E)) times
   the lattice length of E is one linear equation in the unknown weights with an exactly known
   right-hand side. This project holds 1,334,669 certified five-part Ehrhart polynomials, of
   which 13,217 are full-dimensional, so the equations are available in bulk. A valid formula
   exists by McMullen's theorem and satisfies all of them, so any type on which the system pins
   the weight carries that value for every valid formula, and the sign of the pinned value is a
   fact about the family rather than about a particular construction.
5. What the plan must test before it is trusted: at codimension two and three the pinned weights
   must equal the Castillo-Liu closed formulas, and at codimension four the minimum over the
   closed cones must be 739/86400. A pipeline failing any of these is wrong, and the tests cost
   nothing extra because the same polytopes carry all their faces.
6. Routes not to duplicate: the codimension 0 to 4 atlases, the enumeration of five-part triples
   in a box, and the sampling beyond it, all of which this project or the source has done.

## 3. Stop reason

The three questions the strategy's step 1 asks are answered from the source's own reports and
from this project's records; the parent's study covers the general literature and adds no further
finitisation.
