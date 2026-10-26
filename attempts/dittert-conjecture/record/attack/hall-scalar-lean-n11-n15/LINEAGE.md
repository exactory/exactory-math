# Lineage

Logical predecessor: dittert-branch-complete-audit, closing move 4.
Immutable checkpoint: CP-6652cad9cc40fe99, SHA256 6652cad9cc40fe999d88579bcd8984c5afebb2fa4dba80b3eff6b3fc7aa1198b.
Relationship: a new formal-verification subproblem, not a new proof of the original theorem or a budget reset. There is no native harness parent because the predecessor is finished.

Inherited input: hall-n8-n15-branch-coverage/PROOF.md, Sections 3 through 5, and its independent Fraction check. Those checks motivate the formal theorem; their correctness is not an axiom of it.

New hypothesis: all 340 normalized finite cases can be checked inside Lean's kernel at modest local cost, and combined with Bernoulli and the shared quadratic argument.
Success: the exact problem.json claim, a reproducible pinned build, standard axioms only, and independent statement review.
Failure: a mathematical counterexample; missing library infrastructure; six failed attempts and two restatements on a resisting lemma; or an impractical kernel reduction measured in the pilot.

Remaining broader obligations: n7..10 interval/tree formalization, n5,6 SOS formalization, and the matrix-to-scalar analytic dependencies. None is discharged by this attack.
