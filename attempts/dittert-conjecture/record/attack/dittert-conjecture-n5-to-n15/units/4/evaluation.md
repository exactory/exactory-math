# Evaluation of units/4/draft.md (second reader, 2026-09-03)

Read against unit.json, deterministic/numerical-optimisation-run-3 (sdp_n.py, recover_n.py,
README.md, result.json), numerical-optimisation-run-2 (sdpcore5.py, recover5.py, recover5.log),
study/gate-symmetry-blocks (blocks.py, blocks-output.txt), the journal excerpt for moves 2-4.

1. **Statement.** The draft's proposition and pipeline description are unit.json's statement
   (block sizes 16 and 22 at n = 5, 6; the orbit-indexed equations; the exact recovery through
   rational isotypic projectors; the implementation). Match.
2. **Claims and evidence.** The block-size table is blocks-output.txt (n = 4..12); its
   self-checks (orthogonality, the two sums, integrality) are in the code and ran. The n = 5
   pair-orbit count 1128 predicted by characters equals the count found by label propagation
   (sdp5 log), an independent confirmation. The SDP sizes and times are those of the logs.
   The exact recovery steps are those of recover5.py (isotypic check run and logged) and
   recover_n.py (n = 6, floating step declared). result.json of run 3 records pass.
3. **References.** Murota, Kanno, Kojima, Kojima 2010 (the two-generic-element block
   diagonalisation) and Gatermann-Parrilo 2004 (symmetry reduction of SOS programs) are
   classical; the draft attributes the classical parts and claims only the block table, the
   orbit-coordinate recovery and the isotypic exact check as new.
4. **Ledger.** costs = [bound_quality] (move 3): the pipeline fixes lambda below the optimum
   by design; stated.
5. **Findings.** The "where it stops" section is honest about n = 7 (the expansion and the
   pair orbits) and n >= 9 (block sizes). The application sentence is generic but true
   (any G_n-invariant P). The draft passes as a machinery unit judged on its own merits.
