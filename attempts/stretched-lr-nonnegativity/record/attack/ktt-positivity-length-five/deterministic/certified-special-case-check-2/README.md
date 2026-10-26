# certified-special-case-check-2: the Berline-Vergne weight, implemented and validated to dimension five

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, action 1 (two independent
computations of the same quantity compared exactly), applied to the object the rung needs and
that no distributed code computes: the local weight of a cone above dimension three. Step kind:
certified special-case check.

## What was implemented (`bvweight.py`, also in `tools/`)

Berline and Vergne, "Local Euler-Maclaurin formula for polytopes", arXiv:math/0507256,
Proposition 4.1: for a rational space with a rational scalar product there is a unique family of
maps mu, indexed by the rational quotients, with mu({0}) = 1 and

    S(a) = sum over the faces f of a of mu(t(a,f)) I(f),

S the exponential sum over the lattice points of the cone, I the exponential integral over the
face with the measure normalized by the lattice of its span, and t(a,f) the transverse cone, the
image of a in the quotient by the span of f, identified with its orthogonal complement and
carrying the projected lattice. The term of the vertex has transverse cone a itself and integral
1, so the identity is a recursion on the dimension. Everything is evaluated along a generic line
xi = t xi_0, so every term is a Laurent series in one variable with exact rational coefficients
whose poles cancel in the sum, and the weight of the cone is the constant term.

For a simplicial cone with primitive generators v_1, ..., v_d in a lattice with Gram matrix G the
ingredients are explicit: S is the sum over the lattice points of the half-open parallelepiped
times the product of 1/(1 - e^{<xi,v_i>}); the face indexed by a subset J contributes
(-1)^{|J|} times the index of the sublattice its generators span inside its saturation, times the
product of 1/<xi,v_j>; and the transverse cone along that face is spanned by the images of the
remaining generators in the projected lattice, whose basis and Gram matrix the module computes by
exact integer and rational linear algebra (saturation and quotient bases by an augmented Hermite
reduction, so the bases are saturated by construction).

## Result (`weights.json`, `result.json` status pass)

| cone | weight | time |
|---|---|---|
| half-line | 1/2 | |
| dimension 2, orthant / shear / obtuse | 1/4, 3/8, 1/8 | |
| dimension 2, index 3 | 13/40 | |
| dimension 3, orthant and three others | 1/8, 3/16, 5/16, 17/72 | |
| dimension 3, index 2 | 1/4 | |
| dimension 4, orthant | 1/16 | 0.09 s |
| dimension 4, orthogonal 2 + 2 | 9/64 | 0.09 s |
| dimension 5, orthant | 1/32 | 0.70 s |
| dimension 5, orthogonal 2 + 3 | 15/128 | 0.73 s |
| dimension 5, irreducible | 63/256 | 0.78 s |
| dimension 5, index 2 | 1/16 | 0.78 s |

A five-dimensional weight costs under a second, so the rank-five edge atlas of 3,406 isometry
classes is about forty minutes of computation.

## Independent check (`check.sh` -> `check.py`, `result.json`)

Every identity is rewritten in the checker and shares no code with the recursion.

1. The half-line is 1/2.
2. Dimension two, unimodular: the closed formula of Castillo-Liu Lemma 3.3, on six cones.
3. The four vertex weights of the unit square sum to the Ehrhart constant term 1.
4. Dimension two, index three: the valuation property. Subdividing the cone along the interior
   ray (0,1) into two unimodular cones sharing that ray must give
   alpha(C) = alpha(C_1) + alpha(C_2) - 1/2, and it does (13/40 = 3/8 + 9/20 - 1/2). This tests
   the non-unimodular case with no closed formula available.
5. Dimension three: the closed formula of Castillo-Liu Lemma 3.10 on five cones, including one of
   index two.
6. Dimensions four and five: the orthants must be the fourth and fifth powers of 1/2, by
   multiplicativity over orthogonal sums.
7. Dimensions four and five: the cones that split orthogonally as 2 + 2 and 2 + 3 must equal the
   products of the closed formulas of their blocks.

Trusted base: Python integers and Fractions, and Proposition 4.1 of Berline-Vergne as the
definition. The two published closed formulas and the two structural identities (the vertex sum
and multiplicativity) are what the checker tests against; nothing here rests on the source's
undistributed dimension-four script.

## What the step decided

The weight is computable at the dimension the rung needs. This removes the obstruction that
closed the fitting route: the codimension-five weights of five-part hives can be computed
directly, one cone at a time, in exact arithmetic, and the implementation agrees with everything
in print where the two overlap. What remains before the atlas can be evaluated is the conversion
from an edge's normal set to its transverse cone in the projected lattice, and the treatment of
the edges whose normal cone has more than five extreme rays, where the transverse cone is not
simplicial and has to be triangulated.
