# Formalisation unit: hall-domination

## Statement

For every integer n >= 1, every n by n real matrix A with nonnegative entries, and every real lambda > 0 such that for all subsets I of the rows and J of the columns with |I| + |J| > n the sum of the entries of A over I x J is at least lambda (|I| + |J| - n), there exists an n by n doubly stochastic real matrix B with lambda B_ij <= A_ij for all i and j. Lean theorem Dittert.hall_domination with requested type Dittert.HallDomination, checked with propext, Classical.choice and Quot.sound only.

## Claim, quantifier by quantifier

The controller obligation reads: For every integer n >= 1, every n by n real matrix A with nonnegative entries, and every real lambda > 0 such that for all subsets I of the rows and J of the columns with |I| + |J| > n the sum of the entries of A over I x J is at least lambda (|I| + |J| - n), there exists an n by n doubly stochastic real matrix B with lambda B_ij <= A_ij for all i and j.

Quantifiers: For every integer n >= 1, every nonnegative n by n real matrix A and every real lambda > 0 satisfying the cut condition for all row and column subsets.

The Lean declaration `Dittert.hall_domination` has the requested type `Dittert.HallDomination`, whose definitions are the blueprint's (Dittert/Basic.lean, Dittert/Obligations.lean, Dittert/Scalar/Defs*.lean in the frozen step directory).

## Evidence

- Controlled formal check: `deterministic/formal-check-1/result.json`, status `pass`, axioms ["propext", "Classical.choice", "Quot.sound"].
- Journal moves: [1].

## Moves

- Move 1 (verify-formally-with-lean4 / formalise-while-fresh): Formalized the Hall domination theorem in Dittert/Hall.lean by the augmenting-path argument: a maximal flow exists by compactness of the flow set, residual reachability as an inductive predicate, augmentation along a derivation by an explicit direction matrix, saturation of reachable columns and unreachable rows, the cut identity for the reachable sets, and the cut condition forcing total flow n lambda; installed the frozen project and ran the controlled formal check of Dittert.hall_domination. Output: Dittert.hall_domination : Dittert.HallDomination is kernel-checked with propext, Classical.choice and Quot.sound only (393 lines, no sorry).

## Provenance

See study/problem.md, study/verify-formally-with-lean4.md and novelty.md of this node; ported sources are attributed in their file headers.
