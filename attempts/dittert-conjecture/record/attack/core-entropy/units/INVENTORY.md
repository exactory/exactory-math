# Inventory: core-entropy

Every journal move and what its output leaves in the record, grouped by
strategy. A move marked as a fired failure signal leaves what that
strategy's Failure signal names. Convert each into a unit under
CASHOUT.md or discard it.

Walk: verify-formally-with-lean4.

## verify-formally-with-lean4

- move 1 (pass 1, formalise-while-fresh, closed the attack): Dittert.core_entropy : Dittert.CoreEntropy is kernel-checked with propext, Classical.choice and Quot.sound only (581 new lines over the floors modules and the GurvitsPort library, no sorry).
