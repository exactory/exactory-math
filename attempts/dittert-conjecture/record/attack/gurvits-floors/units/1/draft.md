# Formalisation unit: gurvits-floors

## Statement

For every integer n >= 1 and every n by n doubly stochastic real matrix B: per(B) >= n!/n^n; and for all integers a, b >= 1 with a + b <= n - 1, if there are a rows and b columns of B whose a x b block of entries is zero, then per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b), where gamma(k) = k!/k^k. Lean theorem Dittert.gurvits_floors with requested type Dittert.GurvitsFloors, checked with propext, Classical.choice and Quot.sound only.

## Claim, quantifier by quantifier

The controller obligation reads: For every integer n >= 1 and every n by n doubly stochastic real matrix B: per(B) >= n!/n^n; and for all integers a, b >= 1 with a + b <= n - 1, if there are a rows and b columns of B whose a x b block of entries is zero, then per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b), where gamma(k) = k!/k^k.

Quantifiers: For every integer n >= 1, every n by n doubly stochastic real matrix B, and all integers a, b >= 1 with a + b <= n - 1.

The Lean declaration `Dittert.gurvits_floors` has the requested type `Dittert.GurvitsFloors`, whose definitions are the blueprint's (Dittert/Basic.lean, Dittert/Obligations.lean, Dittert/Scalar/Defs*.lean in the frozen step directory).

## Evidence

- Controlled formal check: `deterministic/formal-check-1/result.json`, status `pass`, axioms ["propext", "Classical.choice", "Quot.sound"].
- Journal moves: [1].

## Moves

- Move 1 (verify-formally-with-lean4 / formalise-while-fresh): Formalized the Gurvits permanent floors in Dittert/Floors.lean with the helper modules Dittert/Floors/Analytic.lean and Dittert/Floors/Chain.lean on top of the ported DCPRevere/maths-pub development (GurvitsPort, Apache-2.0): van der Waerden from the port's Egorychev-Falikman theorem; for the rectangle floor, one analytic closure lemma (a nonzero polynomial that is, along every complex line, the limit as a positive real parameter tends to zero from above of nonvanishing polynomials is H-stable, by the minimum modulus principle on a small closed disc and uniform closeness on a compact set), from which the restriction closure x_0 := 0, the leading-coefficient closure and an explicit non-degeneracy lemma feeding the port's derivative closure follow; the extraction chain with the degree-refined constants tracked by a bound on the total degree of the zero-block column variables (preserved by each extraction with the bound decreased by one), the port's Gurvits bound for the remaining variables, the telescoping of the constants to gamma(n-a) gamma(n-b) / gamma(n-a-b), the column permutation putting the zero-block columns first, capacity at least one for the row form of a doubly stochastic matrix, and the top coefficient identified with the permanent; installed the frozen project and ran the controlled formal check of Dittert.gurvits_floors. Output: Dittert.gurvits_floors : Dittert.GurvitsFloors is kernel-checked with propext, Classical.choice and Quot.sound only (922 new lines over the ported GurvitsPort library, no sorry).

## Provenance

See study/problem.md, study/verify-formally-with-lean4.md and novelty.md of this node; ported sources are attributed in their file headers.
