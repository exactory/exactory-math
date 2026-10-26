# Inventory: hall-near-zero-lean-n8-n9

Every journal move and what its output leaves in the record, grouped by
strategy. A move marked as a fired failure signal leaves what that
strategy's Failure signal names. Convert each into a unit under
CASHOUT.md or discard it.

Walk: verify-formally-with-lean4.

## verify-formally-with-lean4

- move 1 (pass 1, formalise-while-fresh): The exact formula and both closed intervals elaborate. Initial result is evidence only: sorryAx appears as expected. INITIAL_RED_GATE.md preserves it; no theorem is declared proved.
- move 2 (pass 1, formalise-while-fresh, closed the attack): The actual p8 polynomial is positive for every u in [0,1/400], and actual p9 is positive for every u in [0,1/500]. Harness PASS for near_zero_certificate with exactly propext, Classical.choice, Quot.sound. No coefficient hypotheses, custom axioms, native evaluation or unresolved proof obligations.

## Candidate retained after claim test

One formalisation unit: both literal near-zero inequalities and their full closed intervals have standard-axiom Lean proofs. Evidence: formal-check-1/result.json and sources. The mathematics is inherited; this is a formal verification artifact. No separate generic basis lemma or evidence-only unit is needed. Support, tail and matrix obligations remain outside the claim.
