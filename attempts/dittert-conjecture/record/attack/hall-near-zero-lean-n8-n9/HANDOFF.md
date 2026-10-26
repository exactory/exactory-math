# Near-zero Lean handoff

Status: FINISHED with one formalisation unit at closing journal move 2.
The independent source review, fresh harness, direct all-principal-axiom
audit, standalone replay, and Stage 8 evaluation all pass. All tasks are
done. See independent-review.md and units/1/evaluation.md. The final
reviewed checkpoint is CP-d68bc3f612310f32 in ../checkpoints; the earlier
CP-29b31b7c95983bc7 remains unchanged as an author-proof snapshot.

Durable kernel-verification checkpoint: checkpoints/CP-29b31b7c95983bc7, with an immutable source archive and SHA256SUMS. Independent review is explicitly pending in that snapshot. The coordinator can add this reference to SEARCH_TREE.md after the reviewer finishes.

Exact theorem: deterministic/formal-check-1/Main.lean, near_zero_certificate, proves (forall real u, 0<=u<=1/400 implies p_8(u)>0) AND (forall real u, 0<=u<=1/500 implies p_9(u)>0). Definitions.lean implements the literal factorial/power polynomial. There is no coefficient-list or positivity premise.

The principal lemmas are NearZero.identity8, NearZero.positive8, NearZero.identity9 and NearZero.positive9. All four and the final theorem have exactly [propext, Classical.choice, Quot.sound]; see axioms.log. The identities are norm_num/ring proofs. Strict positivity includes both endpoints. No native_decide, sorry, custom axiom, or Python verdict is in the final proof.

Lean v4.33.1; Mathlib v4.33.1, commit 0df444a360eaa60ab8c11dca51a86af692955474; dependency revisions pinned in lake-manifest.json. Direct imports: Mathlib.Data.Real.Basic, Mathlib.Data.Nat.Factorial.Basic, Mathlib.Tactic.NormNum, Mathlib.Tactic.Ring, Mathlib.Tactic.Positivity, Mathlib.Tactic.Linarith, and local modules. Existing .lake/packages symlink reused. No installs, dependency downloads, full Mathlib rebuild, commits or external writes occurred.

Proof compilations ran sequentially at nice 15 with Lean -j1 -M2048. Certificate8: 15.00 s, max RSS 1621475328 bytes. Certificate9: 11.46 s, max RSS 1640792064 bytes. Main: 7.15 s. Harness: 10.05 s. Explicit constrained axiom audit: 6.14 s. Raw logs: build-certificate8.log, build-certificate9.log, build-main.log, harness-final.log, axioms.log. These are local incremental measurements, not clean-install or total-development times.

Failed attempts: one missing noncomputable declaration in Certificate8 (18.91 s), repaired; initial sorry gate intentionally failed. No mathematical restatement or exhausted budget. ATTEMPTS.md includes the harness's lightweight axiom printer using its built-in unflagged command, followed by the explicit constrained audit. Packaging hook required check-unit before writing draft; the patch was split accordingly.

Remaining broader formal work: n8 support z=1..6 on [1/400,1/20]; n9 support z=1..7 on [1/500,3/100] (existing external proof compresses the n9 floor case); monotone tails and denominator/localization hypotheses; all n7 sign/tree/bridge cases; matrix-to-scalar interfaces. None is proved by this theorem.

Coordinator owns SEARCH_TREE.md, global STATUS.md, manuscript integration and independent review. Only this new attack was modified. Logical lineage: CP-6652cad9cc40fe99 and CP-6602f547de0eb72c. Candidate generator imports no inherited checker code and is outside the trusted base.

Exact next successor hypothesis: for n=9 and z=7, with m=1 and E,H,T,L as above, set Q=(2-gamma)*E^8-T^8, W=(8+u)*Q-E^8, S=(2-gamma+L*(1-u)^9)*E^9-(E+H)*T^8. Prove that G_7(u)=7^7*Q^8*S-(1-u)*E^17*W^7 is strictly positive for every real u in [1/500,3/100], by a standard-axiom Lean proof of its actual formula and full interval. This is the degree-82 literal support polynomial in the inherited checker. Success would certify only the largest n9 support case; the separate U_z<=U_(z+1) compression and matrix interfaces still need formal proofs. Failure signal: the degree-82 identity or its certificate cannot be checked under -M2048 and the prescribed bounded attempts. The near-zero result is inherited as an adjacent interval, not as an assumption proving this support interval. No successor has been initialized.
