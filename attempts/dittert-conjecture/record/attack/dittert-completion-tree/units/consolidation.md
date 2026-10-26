# Proof consolidation

## Marked steps and their replacements

1. The old Sinkhorn-cost deduction selected the least fixed-point branch
   without excluding a large branch. It is not used. Dominated Hall scaling
   and exhaustive cut inequalities give a contradiction on every feasible
   parameter value, with no branch selection.
2. The rectangular-zero permanent floor initially cited a specialized
   extremizer theorem for which only an abstract was accessible. The
   dimension-independent capacity proof in study/audit-n7.md, section 3,
   derives exactly the same sharp constant directly from Gurvits's
   extraction theorem. Taking a=b=1 also gives the one-zero floor.
3. The n=7 reconstruction needed positivity before division by its scaling
   factor. The supplemented subset localization proves |e|<7/47 and then
   proves positivity in the correct order.
4. The positive-maximizer averaging argument needed an explicit limit
   justification. Continuity and strict-local backtracking supply it.
   The cited Hwang positive-maximizer theorem is also sufficient.
5. The two-zero face bound retains a finite polynomial check. A new
   independent implementation reconstructs it from integer permanent
   evaluations, justified by an a priori degree bound, and counts roots
   exactly. The n=7 alternative trees and n=8,9 support polynomials likewise
   retain their finite exact certificates. No computation-free replacement
   was established, so the proof is explicitly computer-assisted.
6. The shared quadratic contradiction is checked separately in Lean. Its
   first compilation exposed a left/right factor theorem-application slip,
   not a gap in the completion-of-squares identity. The record states the
   narrow scalar theorem exactly and does not claim a formal matrix theorem.

## Rewritten argument

The final independent review also identified a legacy n=6 checker whose
negative-slack branch printed FAIL without failing its exit status. The
complete original integer-run log was recovered and preserved, establishing
the original positive slack. A gate-only regression then reproduced the
exit defect and verified the fix. This does not replace the mathematical
residual check or pretend that the large matrix computation was rerun.

PROOF.md is the rewritten assembly. It follows compactness and uniqueness
of positive maximizers, positive Hall domination, complete cut separation,
dimension-specific exact positivity, and the equality conclusion. Its
linked audits contain the longer analytic details and code correspondences.

## Alternative route and general statement

The capacity argument is an alternative derivation of the rectangle lemma,
not an independent second proof of Dittert's conjecture. The old spectral
route remains open as a separate method. The complete assembly still uses
Lu's and Nascimento's principal arguments and is attributed accordingly.

The rectangle lemma proves, for every a,b,p>=1 and n=a+b+p, that every
doubly stochastic n by n matrix with an a by b zero block has permanent
at least gamma_(n-a)*gamma_(n-b)/gamma_p, and this bound is attained.
This is a general supporting theorem already known through other methods,
not a novelty claim. The audited Dittert conclusion here is restricted to
the requested range 5<=n<=15; no unaudited infinite-range argument is used.

## Publication decision

The exact target statement and its principal proofs were already public.
The local checks and exposition do not establish theorem novelty. The
inventory should retain the assembled proof as a verified exposition and
should not manufacture a new full-proof or second-proof publication unit.
