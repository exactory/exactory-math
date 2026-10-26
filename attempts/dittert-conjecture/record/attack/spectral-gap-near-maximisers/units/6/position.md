# Position of unit 6

**On the path or off to the side.** Off to the side of Dittert's conjecture, and on the path of
anyone who wants to check it by machine. It is a roadmap, stated as six missing definitions.

**Prior best it improves.** No formalisation of the van der Waerden inequality was found in any
repository searched, so there is no prior roadmap to improve. What the unit adds over a guess is
that every claim in it was read from the Mathlib checkout rather than recalled: the declaration
lists of the four relevant modules are in `study/verify-formally-with-lean4.md`.

**Why the sixth item is the one that matters.** The first five block a proof. The sixth, the
spectral gap of a weighted bipartite graph, blocks the statement: the claim of this attack is a
statement about that quantity and cannot be written in Lean before it is defined. That is what
turns precondition question 2 of the formalising strategy into a no rather than a maybe.

**What is formalisable today.** A fixed-dimension integer computation, which is what the sibling
attack encodes at `attack/dittert-conjecture-n5-to-n15/deterministic/formal-check-1`: orbit
indices, a Gram matrix and an integer Cholesky, all decidable `Bool` computations needing no
analysis. That discharges a single dimension and nothing uniform.
