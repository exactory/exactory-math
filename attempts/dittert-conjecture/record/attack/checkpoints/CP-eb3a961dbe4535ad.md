# Checkpoint CP-eb3a961dbe4535ad

Archive: hall-scalar-reviewed-m3.tar.
SHA256: eb3a961dbe4535ada313356667ff16c9c29e0cd6e4155f3c4c0c6b27a5a8e5ce.
Source attack: hall-scalar-lean-n11-n15, closing journal move 3.
Predecessors: full Hall audit CP-6652cad9cc40fe99 and finite-certificate
checkpoint CP-6602f547de0eb72c.

Exact statement: for every natural 11 <= n <= 15, every natural pair
with 0 < a+b < n, and every real u <= 1, the directly defined rational
C and M satisfy C*u^2 + M*(1-u)^n - gamma(n) > 0. The permanent lower
bound, quadratic deficit lower bound, and relaxed total budget are
therefore inconsistent. The reduced family has exactly 340 cases in
Lean, and formal coverage includes all original marginal orientations.

Compared with the finite-only checkpoint, this snapshot adds the real
composition, public positivity and exclusion declarations, complete
boundary fixtures, fresh independent execution and direct axiom audit,
resolved Stage 8 reference finding, and FINISHED.json with one
formalisation unit and no open task. Both deterministic checks pass;
all principal axioms are exactly propext, Classical.choice, Quot.sound.
The .lake dependency and build caches are excluded from the archive.

The separate near-zero successor is finished at CP-d68bc3f612310f32.
The local English manuscript, with a separately scoped appendix for
that result, is in ../../paper-hall-scalar-lean. Its finished write stage
does not mean publication or a full matrix formalization.

Unresolved broader obligations remain the matrix-to-scalar interfaces,
full cut, equality characterization, and remaining dimensional scalar
families. The completed scalar theorem does not assume any of those
interfaces and does not prove them. No successor repeats this exact
claim or resets its completed move budget.
