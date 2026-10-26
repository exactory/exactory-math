# Consolidated scalar proof

The mathematical scalar argument is already in Nascimento's public proof. This attack adds an exact Lean artifact, not an independent analytic route or mathematical theorem discovery.

## Marked and replaced steps

The prior external rational enumeration is replaced by direct Lean definitions and five kernel-reduced finite propositions. No external list of successful arithmetic values is imported. The implicit coverage of marginal size pairs is replaced by all_good: every proper ordered pair embeds into Fin15; all marginal constants equal those at(n-1,0). The case total is itself proved from the same predicate.

The informal completion of the square is replaced by a ring-verified identity and square nonnegativity. The passage from a rational discriminant to the real statement is explicit via Rat.cast_pos and exact_mod_cast. The binomial estimate is an application of Mathlib's Bernoulli theorem. Summing the permanent and deficit bounds proves the relaxed-budget contradiction.

## Rewritten proof

Let n,a,b satisfy11<=n<=15 and0<a+b<n. Definitions.lean supplies the exact rational M,C,gamma. The finite theorem gives M>0,C>0,D=4C(M-gamma)-(nM)^2>0. Thus4C(Cu^2-nMu+M-gamma)=(2Cu-nM)^2+D>0. For u<=1, Bernoulli yields(1-u)^n>=1-nu. Multiplication by positive M proves Cu^2+M(1-u)^n-gamma>0. The three stated scalar lower/budget bounds would force the left side to be nonpositive, a contradiction.

## Generality, costs and limitations

The proof covers all real u<=1 and P+delta<=gamma, stronger scalar domains than the source's[0,1] and equality budget. These elementary extensions are not claimed as new mathematical results. Move1's proof-hole obligation is completely discharged at move3. The final evidence is moves2 and3 with no paid cost, no extra axiom and no hidden hypothesis.

There is no second independent analytic proof; the algebra is the source argument in a checked form. The two packages share the finite Lean source, as their hashes confirm. Neither package formalizes Hall domination, row selection, stationarity, permanent floors, matrix deficit bounds, full cuts, or the Dittert matrix theorem. The new artifact is useful as a reproducible partial formalization; its research novelty is limited and should be assessed separately from correctness.
