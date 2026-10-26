# Position of unit 4

**On the path or off to the side.** On the path, as evidence rather than as proof. It is the
only direct test of `G(n, c_n)` in the record, and it covers `n = 5` to 12, which is eight of the
eleven dimensions Dittert's conjecture leaves open.

**Why the test had to be indirect.** `G(n, c_n)` quantifies over `A in K_n` with a zero entry and
`phi(A) >= 2 - gamma_n`. Dittert's conjecture says `phi <= 2 - gamma_n` with equality only at
`J_n/n`, which has no zero, so the hypothesis set of `G` is exactly the counterexample set of
Dittert's conjecture at `n`, and sampling it is impossible. Move 1 established that equivalence
and move 4 recorded the consequence: every numerical test in this attack is a test of a
relaxation, and a relaxation that is non-empty is one in which the structure being sought can be
absent. The contrapositive removes that problem, because its constraint set is large.

**When the run was made.** After the walk closed at move 11, so it carries no journal move of its
own; the two moves it lists are the ones that produced the statement it tests, not the ones that
ran it. `deterministic/numerical-optimisation-run-1/README.md` holds the run itself and
`result.json` records the pass.

**Prior best it improves.** No search over `K_n` at `n >= 4` exists in print. Sinkhorn 1984 and
Hwang 1986/87 exhaust the critical points at `n = 2` and `n = 3`.

**What it is not.** A multi-start local optimiser gives a lower bound on the true constrained
maximum, so a positive shortfall is evidence and not a certificate. At `n = 9` to 12 the best
point found sits well inside the spectral constraint, so those four rows show only that no
near-decomposable matrix reaches the ceiling.
