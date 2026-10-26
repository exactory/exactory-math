# Persistent Dittert search tree

Original objective, unchanged: prove Phi(A)<=2-n!/n^n for every integer
5<=n<=15 and every nonnegative real n by n matrix with total entry sum n,
with equality exactly at J_n/n. All artifacts are local and English.

## Cross-attack index

| Attack | Exact scope | Logical predecessor and checkpoint | Relationship | Status and evidence | Next unresolved question |
|---|---|---|---|---|---|
| dittert-conjecture-n5-to-n15 | Original full objective | Original root | Root | Finished with partial results: n5,6 certificates; early n8+ completion withdrawn | Old proof never excluded its large-cost branch; full matrix Lean optional |
| spectral-gap-near-maximisers | For every4<=n<=15 and every boundary A of mass n with Phi(A)>=2-gamma_n, prove 1-sigma_2(D_r^(-1/2) A D_c^(-1/2))>=c_n, with c_n defined below | Original root, historical evidence retained | Hypothesis / alternative route | Finished with a barrier; units/5/draft.md | Exclude near-decomposable large-cost candidates within that method |
| quantitative-van-der-waerden | For every n>=2 and doubly stochastic B, prove per(B)>=gamma_n*(1+norm_F(B-J_n/n)^2/4) | Spectral route, historical evidence retained | Continuation / alternative route | Finished with partial bounds and obstruction; units/6/draft.md | Constant1/4 claim not closed; two-column improvement and old large-cost branch remain method questions |
| dittert-completion-tree | Original full objective, equality included | Prior three records; CP-49692413fac97be7 snapshots closing move7 | Alternative Hall route | Finished attributed assembly; PROOF.md and deterministic checks1..5 | User-requested branch-completeness challenge handled by successor, not assumed away |
| dittert-branch-complete-audit | Original full objective, with explicit verification of all branches | dittert-completion-tree move7, CP-49692413fac97be7 | Logical verification continuation, no native parent | FINISHED at move4; PROOF.md, both child checks, study/independent-review.md | None for the declared computer-assisted theorem; full Lean optional |
| hall-n7-branch-coverage | Exclude every n7 boundary global maximizer through the complete Hall/sign/tree split | dittert-branch-complete-audit move1; inherits CP-49692413fac97be7 | Native child / exact special case | FINISHED at move2; COVERAGE_PROOF.md;6476 cuts,62 leaves,94 rejected omissions; checkpoint HALL-N7-COVERAGE-M2-2026-09-05 | No remaining branch; return boundary exclusion to parent |
| hall-n8-n15-branch-coverage | Exclude every boundary global maximizer for each8<=n<=15 through full Hall and scalar covers | dittert-branch-complete-audit move1; inherits CP-49692413fac97be7 | Native child / exact range | FINISHED at move2; PROOF.md, CODE_MAP.md;596 size pairs,428 scalar cases,9 interval certificates; CP-7acc4c92dd0dd957 | No remaining branch; common source floors discharged by parent |
| hall-scalar-lean-n11-n15 | Kernel-certify the explicit Hall scalar polynomial positivity and infeasibility for every nonfull cut size at each 11 <= n <= 15 | dittert-branch-complete-audit move 4; CP-6652cad9cc40fe99 | Logical formal-verification successor, no native parent | FINISHED at move 3 with one formalisation unit and no open task; both formal checks and independent final review pass; CP-eb3a961dbe4535ad | Local manuscript complete; matrix reduction, full cut and equality remain outside the formal claim |
| hall-near-zero-lean-n8-n9 | Kernel-certify the literal near-zero polynomial on closed [0,1/400] at n8 and [0,1/500] at n9, including coefficient identity | Full Hall audit CP-6652cad9cc40fe99; finite Lean implementation CP-6602f547de0eb72c | Logical special-case formalization successor, no native parent | FINISHED at move 2 with one formalisation unit; independent source, all 36 coefficients, fresh Lean and endpoint checks pass; CP-d68bc3f612310f32 | Exact n9,z7 support-polynomial successor is stated in HANDOFF.md, but not initialized; support compression, tails and matrix interfaces remain |

The two new native children were initialized after parent move0 and their
opening is recorded in parent move1, as parent.json states. Deeper logical
successors must use a normal init and LINEAGE.md, not an edited parent.json.

For the spectral attack's exact original threshold, gamma_n=n!/n^n,
h_n=sqrt(2*gamma_n), theta_n=1-h_n,
kappa_n=1/((1-gamma_n)*(1-2*h_n/3)), and
c_n=2*sqrt(gamma_n*kappa_n)/theta_n. This historical kappa_n is not the
one-zero permanent floor also denoted kappa in the later Hall records.
Likewise the historical spectral attack is not automatically reclassified
as a proved independent spectral theorem by the Hall conclusion.

## Contribution and failure rules

The parent retains all eleven dimensions. n5,6 are inherited only through
their exact identity and PSD evidence. n7 and n8..15 must each return a
strict boundary contradiction on their whole feasible domain. A result for
one dimension never closes another dimension. Positive maximizers and the
uniform equality condition are separate common obligations.

The old Sinkhorn fixed-point strategy remains a preserved unsuccessful
branch. The Hall construction is different and does not assume the old cost
is small. It can replace that route only after proving that every hypothetical
boundary global maximizer enters its full/marginal/proper case cover.

Checkpoint archive and exact statement: [CP-49692413fac97be7](checkpoints/CP-49692413fac97be7.md).
No checkpoint or reviewer verdict alone certifies a theorem.

## Final recombination

The parent has combined both strict boundary exclusions with its common
Hall construction and all-dimensional positive-maximizer proof, plus the
inherited full-domain n5,6 certificates. PROOF.md establishes every requested
dimension and equality. Both complete new wrappers were rerun by the
coordinator; exact outputs pass. The fresh independent review confirms all
quantifiers and finds no remaining mathematical branch. All new attack tasks
are done. No successor is needed merely to repeat this result or reset a
budget. Optional independent method questions remain recorded above.

Final immutable checkpoint:
[CP-6652cad9cc40fe99](checkpoints/CP-6652cad9cc40fe99.md).
