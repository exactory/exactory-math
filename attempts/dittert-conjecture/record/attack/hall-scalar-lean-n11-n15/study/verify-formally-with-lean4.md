# Formal verification strategy study

## Queries

The complete query and source ledger is ../../../scratch/lean-novelty-2026-09-05.md relative to this attack. Its findings were read by the coordinator before this study was recorded. All queries ran on 2026-09-05.

Strategy queries5..7,9..11 searched arXiv, Semantic Scholar, Crossref and zbMATH for Bernstein/formal/rational/certificates; follow-up exact-title query resolved Bertot, Guilhot and Mahboubi. The source ledger records the exact query strings and all failures.

## Sources read

- Mathlib rational normalization implementation and Rat cast-order source, and local Algebra/Order/Ring/Pow.lean with one_add_mul_le_pow. The coordinator inspected the installed pinned library, not only a floating online API.
- Official Lean verification requirements: https://leanprover-community.github.io/did_you_prove_it.html . Main theorem must be built, use only the standard axioms, and match the intended claim.
- Prior Bernstein formalization: DOI10.1017/S0960129511000090, abstract/metadata; DOI10.1007/s10817-012-9256-3, metadata. This is not a new generic method.
- arXiv:2607.26413v1, abstract, is prior exact-rational and kernel-checker architecture for a different finite problem.
- Existing local scalar Main.lean was read completely and rerun as a baseline; both its theorems use precisely propext, Classical.choice, Quot.sound.

## Constraints on steps2..6

All objects required by this finite scalar claim exist: Nat, Fin, Rat, Real, factorial, finite quantification, ordered ring arithmetic and Bernoulli. No custom mathematical infrastructure is needed for the first milestone. Use direct rational definitions and kernel decision, with n11 as the initial cost pilot. Split by dimensions or proper-cut rows if needed, never accept native_decide as this attack's certificate. Prove the real implication using Rat.cast_pos and the completed-square identity. Compare every formula to the explicit claim and review coverage independently.

## Stop reason

The fixed12-query combined study completed. The first milestone needs no Bernstein implementation; that is a distinct successor question if its identity/coverage cost is warranted. Lean version and actual installed APIs were checked locally.
