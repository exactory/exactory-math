# Formalization scope and publication handoff

Date: 2026-09-05. All research remains local. This record distinguishes
the existing attributed computer-assisted matrix proof from the new
partial Lean developments.

## Completed mathematical artifacts

| Artifact | Exact formal claim | Coverage and trust |
| --- | --- | --- |
| [Hall scalar family](attack/hall-scalar-lean-n11-n15/deterministic/formal-check-1/Main.lean) | For natural 11 <= n <= 15 and 0 < a+b < n, the directly defined C and M satisfy C*u^2 + M*(1-u)^n - gamma(n) > 0 for every real u <= 1; hence the three relaxed-budget bounds are inconsistent. | 340 normalized cases have a Lean cardinality theorem. Universal coverage includes every original marginal size and orientation, giving 455 uncompressed cases by the reviewed combinatorial count. |
| [Near-zero polynomials](attack/hall-near-zero-lean-n8-n9/deterministic/formal-check-1/Main.lean) | The literal p8(u) is strictly positive for every real u in [0,1/400], and p9(u) is strictly positive for every real u in [0,1/500]. | The literal identities and positive homogeneous expansions, with 17 and 19 coefficients, are kernel-checked, including both endpoints and the exact rescaling. |

Every principal theorem in these developments has exactly `propext`,
`Classical.choice`, and `Quot.sound` in its audited transitive axiom list.
The final proof sources contain no `sorry`, `native_decide`, custom axiom,
or assumption that an external certificate is correct. The near-zero
generator proposes constants; Lean independently checks their meaning.

The original packages have successful harness checks and separate
source and execution reviews. A separately executed finite-only audit
uses the same n11..15 source, so it is not a second arithmetic algorithm.
Separate assistant reviewers are not journal peer reviewers. No alternate
kernel or clean rebuild of all Mathlib dependencies was run.

The toolchain is Lean v4.33.1 with Mathlib revision
`0df444a360eaa60ab8c11dca51a86af692955474`. Mathematical computations were
serialized and run at niceness 15. Proof builds and explicit audits use
one Lean thread and `-M2048`. The harness also invokes a lightweight
axiom printer without explicit Lean resource flags; a separate constrained
audit checks the declarations. Existing dependency caches were reused.

## What is not formalized

The Lean results do not establish the full Dittert matrix theorem for any
of the dimensions above. In particular, they do not establish:

- The Hall minorant construction and the complete matrix-to-scalar reduction.
- The matrix permanent floors, deficit estimates, stationarity, and support
  reductions used to supply the scalar premises.
- The full-cut case (a,b) = (0,0), or the matrix equality characterization.
- Complete n8 or n9 support intervals and tails, the n7 branch tree, or
  the n10 scalar family.
- The complete n5 or n6 matrix theorem from their inherited SOS evidence.

The broader 5 <= n <= 15 computer-assisted proof and its attribution remain
in [STATUS.md](STATUS.md) and
[the branch-complete proof](attack/dittert-branch-complete-audit/PROOF.md).
That evidence is not converted into a Lean theorem by naming it as an
assumption. The older failed Sinkhorn route remains a separate historical
branch, not a premise silently accepted by the new formal artifacts.

## Local manuscript

The manuscript workspace is [paper-hall-scalar-lean](paper-hall-scalar-lean/HANDOFF.md).
It uses `exactory:write`, an evidence ledger, five separately recorded
literature passes, and eight registry-verified bibliography entries.
Its contribution is a limited formal-verification technical note, not
a new proof of the Dittert conjecture or a first Dittert formalization.
Prior dimension-four Lean work is explicitly acknowledged.

The formulas, cardinalities, source hashes, execution records, and declared
trust boundary provide concrete material for a citable verification note.
This is an assessment of the artifact's usefulness, not a certification
of originality, journal significance, or publication acceptance. The user
has specified Ryosuke Shiroshita and Ryosuke.Shiroshita@exactory.ai as
the author and contact email. A distribution license and final publication
decisions remain for the user. No Zenodo record or DOI has been created.

## Next distinct research branch

The near-zero attack records an exact successor in
[HANDOFF.md](attack/hall-near-zero-lean-n8-n9/HANDOFF.md): certify the literal
n9, z7 support polynomial on [1/500,3/100]. Its total degree is 82 in the
inherited exact computation. A successful interval certificate would
still leave support compression, the tail argument, and the matrix
interfaces to formalize. Kernel cost for that larger identity has not
been measured, and no CPU or completion-time estimate is claimed.

Any successor must retain its exact claim, its own study and strategy
records, and explicit predecessor checkpoints in
[SEARCH_TREE.md](attack/SEARCH_TREE.md). It must not replace the full
matrix objective or restart a completed attack merely to reset a budget.
