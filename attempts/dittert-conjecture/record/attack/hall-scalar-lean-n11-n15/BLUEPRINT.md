# Formal dependency blueprint

1. Direct rational formulas: gamma, rectangle, oneZero, floor, curvature.
2. Finite criterion: M>0, C>0 and 4*C*(M-gamma)-(n*M)^2>0 for every reduced size pair.
3. Coverage: every natural pair with0<a+b<n is proper or marginal; all marginal constants agree with the normalized pair(n-1,0).
4. Real transport: rational positivity implies positivity of the same constants in the reals.
5. Completed square: C*u^2-n*M*u+M-gamma>0 for every real u.
6. Bernoulli: u<=1 gives1-n*u<=(1-u)^n. Multiplication by positive M proves scalar_positive.
7. scalar_exclusion sums the two lower bounds and contradicts P+delta<=gamma.
8. Audit imports the theorem and its tests. The harness prints the transitive axioms of the final declaration.

The matrix-derived meaning of P,delta,u and the proof of their lower bounds are not axioms or implicit premises: they are separate, unformalized analytic obligations needed to apply this scalar theorem to matrices.

Initial red test: the skeleton elaborated and the public axiom gate rejected sorryAx, as study/initial-red-result.json records. The setup corrections were a missing Lake root list, factorial unfolding in a fixture, and a required explicit theorem type. They changed no mathematical statement. The successful red-gate run took25.82s wall,3.23s user,9.91s system and maximum RSS1455439872 bytes under the shared local load. These are setup measurements, not the cost of the completed proof.
