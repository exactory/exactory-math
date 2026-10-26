# Exact near-zero formal check

Target: every real u in the closed interval [0,1/400] has p_8(u)>0, and every real u in [0,1/500] has p_9(u)>0. Definitions.lean follows DEFINITIONS.md exactly. No matrix or support-case theorem is asserted.

The first build intentionally has sorry to validate the statement and observe the failing axiom gate. Final status depends on result.json after all obligations are discharged. Lean and Mathlib are pinned to v4.33.1. Existing dependency caches are reused. All Lean processes run sequentially with -j1 -M2048 at nice 15.

Final result: PASS. near_zero_certificate and all four identity/positivity lemmas depend only on propext, Classical.choice and Quot.sound. The initial gate is preserved in ../../INITIAL_RED_GATE.md. The completed development and exact proof are described in ../../PROOF.md and ../../ATTEMPTS.md. The initial statement paragraph describes the historical red gate, not the final source.

Run ./replay.sh from this directory with the pinned dependencies available. It builds Definitions, Certificate8, Certificate9 and Main sequentially, then prints every principal axiom list with explicit -j1 -M2048. The package configuration applies those flags to all proof compilations. The Exactory harness's own lightweight axiom-print command has no explicit Lean flags; this limitation and the separate constrained audit are recorded in ATTEMPTS.md.

The direct imports are Mathlib.Data.Real.Basic, Mathlib.Data.Nat.Factorial.Basic, Mathlib.Tactic.NormNum, Mathlib.Tactic.Ring, Mathlib.Tactic.Positivity and Mathlib.Tactic.Linarith. candidate-data.json records the unnormalized homogeneous Bernstein coefficients. generate_certificate.py independently proposes these constants from power-basis arithmetic, but neither its execution nor its output is a proof premise. The literal identities and positivity proofs are checked in Lean.
