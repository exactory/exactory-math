# Checkpoint 000024: an unconditional two-supply mass theorem

Recorded: September 8, 2026. Controller checkpoint revision336.
Source: node-000018, erdos-124-ergodic-mass-threshold, journal move2.
Checkpoint digest: `f6411470e7dd2ceb27a0af659ea2cfeeb0ef321d7f859bf5f56ffa4910f7f91a`.
Manifest digest: `c34b753e9129af8fd6fc65f54ef85887cee309ab7dddb872749b1aaa9d8c574a`.

## Status and exact claim

This is an analytical proof candidate undergoing fresh independent result
review. It is not yet accepted. The original objective and T_4=1 remain
open. The historical subjective15% estimate is unchanged, not a measured
coverage fraction or a reason to choose the next branch.

For every nonempty finite set D of distinct integers at least 4 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=b(m)=2+1/(m-1)+(floor(log_2(m))+1)/m, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining labelled occurrences d^j, each pair used at most once and coincident numerical values retained separately; moreover b(m)<=37/12 for every integer m>=4 and b(m) tends to 2 as m tends to infinity.

## Mathematical change

The old general proof used two density supplies, a gcd-one correction
supply and an amplifying reserve. The new argument constructs a
Fourier-Stieltjes mean supported on the subset sums of any finite gcd-one
power supply, without imposing a reciprocal-mass lower bound on that supply.

The proof first establishes sequential Bernoulli Fourier limits for all
characters and then for every positive finite spectral measure by dominated
convergence. Only afterward does it take a weak-star cluster point. This
avoids assuming that an arbitrary character-annihilating mean has the
stronger Fourier-Stieltjes property.

Griesmer's pinned Corollary4.2(ii) then makes the sum of this supply and one
mass-one density supply thick. A second disjoint mass-one supply amplifies
a represented interval to all sufficiently large integers. A logarithmic
gcd descent and strict first-crossing allocation prove the inclusive b(m)
threshold and its stated uniform and limiting bounds.

If accepted, the theorem changes the general minimum-four uniform
sufficient bound from13/4 to37/12 and the leading large-minimum sufficient
mass from3 to2. It does not establish threshold one. It retains every
positive cutoff, arbitrary finite labelled deletion and numerical collision.

## Exact method limitation

The criterion in this proof requires disjoint B and R of mass at least one
each, plus a nonempty A of positive mass. It therefore cannot apply to an
input of total mass at most two. Refining only its gcd-seed or crossing
constants cannot remove this obstruction. This is a limitation of this
specific partition criterion, not a negative result about completeness or
every possible Fourier-Stieltjes method.

Move2 recorded the actual entry failure and native fail ended the
parameter-ladder strategy. The native attack remains unfinished, with two
completed tasks and no stall. T_4=1 was not closed, so no local full-proof
cash-out is claimed.

A controller retreat naming CP24 was refused because that checkpoint has
no accepted usable result yet. The failed transition changed no controller
state. Complete result review and acceptance before retrying that exact
retreat; no gate repair or bypass is needed.

## Lineage and verification

The logical predecessor is node17 and checkpoint23. There is no native
parent. The mathematical dependency is accepted Mass, acceptance5, whose
closure includes Core, acceptance1. The primary external input is Griesmer,
Discrete sumsets with one large summand, arXiv:2507.10512v1.

The proof states its literature trust boundary: the relevant mean lemmas
and corollary have been inspected, but the full primary paper's principal
structure theorem has not been independently reproved here. There is no
exhaustive novelty or priority claim.

Fresh independent reviewer Dalton, host thread
01a07fa5-7b0c-7ab2-8257-67adbb8a9964, received the exact frozen checkpoint,
proof, source and dependency closure, with accepted dependency claims but
without other reviews or the author's conversation. Its result is pending.
The checkpoint command validates evidence identity, not prose mathematics.

## Remaining obligations and next hypothesis

Obligations1,40,42,43,44 and45 remain open. In particular, the strict
sub-rung interval, minimum-three cases and reciprocal equality have not
been discharged. No implication bridge is accepted merely because its
conditional deduction is explained in the proof.

The [post-CP24 frontier assessment](../attack/preflight/frontier-refresh/FR-CP24-20260908-1.md)
keeps every earlier failure, hold and accepted dependency. It drops further
constant-only partition rungs from execution priority. The next preflight
question is whether a genuinely new occurrence-allocation or one-supply
method can avoid spending two full unit masses. Direct WOC and arbitrary
half-mass signed units are not automatically reinstated.

Success requires a useful precisely stated mechanism with a current
primary-source study and an entry whose hypotheses can actually be met.
Failure is a repeated two-unit requirement, circular support deletion, or
an unproved inference from qualitative density or thickness to completeness.
Any successor needs separate independent admission and the current account,
not a duplicate checkpoint or a resource reset.

## Resources and evidence

Account1 retains24 used moves. Account2 has two of24 used moves and24
historical moves, zero reservations and zero runs. No new mathematical
program, formal verification, publication or research commit occurred.

- [Candidate proof](../attack/erdos-124-ergodic-mass-threshold/moves/002-two-supply-ergodic-rung.md)
- [Loss ledger](../attack/erdos-124-ergodic-mass-threshold/moves/001-reciprocal-mass-loss-ledger.md)
- [Checkpoint input](../attack/admission/ergodic-mass-rung-checkpoint.json)
- [Frozen evidence manifest](../attack/preflight/ergodic-mass-threshold/rung-evidence-manifest.json)
- [Restricted result-review context](../attack/admission/ergodic-mass-rung-result-context.json)
- [Native-account audit repair](../../renewal-audit-repair-ea40fw/REPAIR_LOG.md)

All research output remains local.

## Acceptance and reassessment addendum, September8,2026

At revision337, the public acceptance command completed the transitive
immutable-evidence and proof-policy audit and accepted obligation41 as
acceptance-000011, analytical reviewed proof. The main agent read the
complete independent review and checked all ten current artifact bytes
against their frozen digests. All ten matched. The independent reviewer
could not run its own hash commands under the host guard; that limitation
remains disclosed. No formal or exhaustive source-proof verification is implied.

At revision338, the same justified strategy-failure retreat naming CP24
succeeded. Node18 is retreated, not locally finished; all original and
sub-rung obligations remain open. Replan339 recorded this distinct accepted
progress once and preserved every account and node14's deferral.

The installed controller now requires a formal, independently reviewed
strategy reassessment. Its read-only strategy-context response previews
activation of this policy for the existing history. The full current
context and retained failures are bound in the proposed assessment. It
defers the sole nonterminal admitted strategy, node14's unstarted
constructive attempt, and continues no mathematical move. A fresh reviewer
is checking the occurrence-level partition hypothesis as a preflight
question, not approving it as a theorem or an executable entry.

The manual all18-node comparison remains in force. The latest policy
requirement adds an actual controller gate; it is no longer only an
agent-operated reminder. Neither this assessment nor the accepted partial
theorem resets a resource account. Current account2 usage remains two of24.

- [Independent result review](../attack/admission/ergodic-mass-rung-result-review.md)
- [Accepted specification](../attack/admission/ergodic-mass-rung-accept.json)
- [Recorded retreat](../attack/admission/ergodic-mass-rung-retreat.json)
- [Post-acceptance replan](../attack/admission/ergodic-mass-rung-replan.json)
- [Proposed formal reassessment](../attack/admission/strategy-reassessment-cp24-draft.json)

## Completed formal reassessment addendum, September8,2026

At revision340, the public service accepted assessment-000001 after fresh
independent full-context review. The assessment preserves every residual
obligation and retained failure, defers node14 and continues no strategy.
The installed policy is enabled. Fresh next returns replan, round1.
The preceding proposed-review wording records the earlier state only.

The [verification addendum](../attack/preflight/frontier-refresh/FR-CP24-20260908-1-verification.md)
records the reviewer, exact bindings, source boundary and current resource
usage. The [occurrence-allocation preflight](../attack/preflight/occurrence-allocation/problem.md)
finished its fixed24-query sweep without a usable new operation.
The candidate partition is still open. Neither the assessment nor the
preflight is a mathematical checkpoint, successor admission or budget reset.

## Successor admission addendum, September8,2026

A later focused study identified a cyclic least-power selection to test
under a removable mass-one core condition. Proposal19 was independently
reviewed and admitted as node19, with native setup complete at revision347.
Its explicit Q,R partition and all-tail thickness remain unproved.
The [all19-node comparison](../attack/preflight/frontier-refresh/FR-CP24-20260908-2.md)
and proposed formal assessment retain the original objective and every
remaining obligation. A separate independent strategy review is pending;
no move has been reserved. CP24 is still the latest mathematical checkpoint.
