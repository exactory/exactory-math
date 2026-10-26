# Checkpoint 000025: cyclic spectral thinning

Recorded: 2026-09-08, revision352. Reporting snapshot: revision356.
Source: node19, journal move1. Logical predecessor: node18 and CP24.
Checkpoint digest: d4bd27ddc94cba4d102e89ba5c19266074b4ea8dea254df7d33625d0fac79dcd.
Manifest: 73f908145b8601b3f44dc351f0ac5330620a8e315aefc7e4eaba6484c336cb1e.

## Exact result and status

This is a frozen analytical proof candidate, not yet accepted.
The native unit record passed check-unit. Independent frozen-result
review and unit draft evaluation are pending. The root remains open.

For every nonempty finite set D of distinct integers at least 4, write sigma(D)=sum_{d in D}1/(d-1) and H={h in D:sigma(D minus {h})>=1}; if H is nonempty with gcd(H)=1, then for every integer k>=1 and finite set F of labels (d,j) with d in D and j>=k, there is an explicitly recursive infinite sequence Q of distinct remaining labels, strictly increasing in numerical value q_i, whose complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), such that every h in H occurs infinitely often in Q with bounded gaps between its selected exponents and sum_i ||beta q_i||^2=infinity for every beta in R/Z other than zero; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers, with a terminating witness procedure and each label used at most once.

## Mathematical change

The [proof](../attack/erdos-124-cyclic-spectral-thinning/moves/001-cyclic-spectral-thinning.md)
chooses individual powers cyclically, rather than whole base classes.
The next value is the least h-power greater than (h-1)(C+W), where C
is fixed by D,k,F and W is the earlier selected weight. Its strict-prefix
estimate preserves a positive buffer and the same complement gap,
even when the other bases have reciprocal mass exactly one.
It applies directly to the infinite complement, without interchanging
an intersection with the finite-subset-sum operation.

Minimality bounds successive selected exponents for each active base.
Nearest-integer recurrence excludes all nontrivial characters for the
same sequence. Sequential dominated convergence before a cluster point
gives the full Fourier-Stieltjes mean. Griesmer's sumset corollary yields
arbitrarily long intervals using disjoint label supports. The terminating
witness procedure is described, not executed. Coincident numerical
values remain independent occurrence labels.

The sufficient condition sigma(D)>=1+1/(min D-1), with min D>=4 and
gcd(D)=1, makes H=D. This is a thickness consequence within the same
unit, not a second checkpoint or an improved completeness threshold.

## Verification

The [manifest](../attack/preflight/cyclic-spectral-thinning/evidence-manifest.json)
binds eight artifacts and accepted CP24's transitive Mass/Core closure.
The eight raw digests were computed before the public checkpoint command
validated and froze the candidate. No mathematical program was run.

The published input is John T. Griesmer, Discrete sumsets with one large
summand, arXiv:2507.10512v1,
https://arxiv.org/pdf/2507.10512v1. The exact interfaces are checked;
its main sumset theorem remains an explicit trusted literature input.

Fresh reviewer Godel, host01a08011-97a1-7570-97c7-15ebe2b99cdb,
received the exact [context](../attack/admission/cyclic-spectral-result-review-context.json),
frozen proof, dependency closure and unit package without other reviews
or author conversation. Its result is pending. No formal, priority or
exhaustive novelty claim is made. The repeated nine-query unit study
retains its search-index and access limitations.

## Obligations and next work

Only obligation46 is the acceptance target. Complement47, bridge48,
the full half-mass assertion28 and all root obligations remain open.
Length-two intervals imply a signed unit only on the stated criterion.
Thickness does not imply eventual completeness.

After review and local finish, reassess all old routes before another
move. Candidate questions concern a concrete operation below removable
mass one, or a legally disjoint reserve using this new input.
Neither is solved or admitted by this checkpoint.

Formal assessment2 passed at348. The move was reserved349 and
journalled351. Consolidation, inventory, novelty and the checked unit
are prepared. The required unit-before-draft ordering was enforced;
a combined patch was refused before writes and then split into the
required checked sequence. No gate was suppressed.

Account1 retains24 moves; account2 has three of24 used,24 historical,
zero reservations and zero runs. No resource renewal, research commit
or publication occurred. The historical subjective15% estimate is
unchanged and is not proof coverage. Research remains local.

## Acceptance and local-finish addendum

At revision358, the public acceptance command audited the complete
transitive immutable evidence closure and accepted obligation46 as
acceptance-000012, analytical reviewed proof. The coordinating agent
read the complete independent result review and unit evaluation.
There were no blocking findings. The reviewer separately reported its
actual source-reading and byte-hash boundaries, including the trusted
Griesmer main theorem and supplied canonical object bindings.

The eight working proof/study artifacts matched the frozen manifest
before acceptance. A separate public audit passed at357. The reviewed
draft and unit.json raw digests also matched the evaluator's recorded
digests. These are evidence-identity checks, not formal proof checking.

A fresh native check-unit passed and finish completed the node with one
unit. At revision362, node19 is finished, result and cash-out actions are
clear, and next requires a strategy reassessment. Account2 remains at
three used moves, zero reservations and zero runs. The root remains open.

The [result review](../attack/admission/cyclic-spectral-result-review.md)
and [unit evaluation](../attack/erdos-124-cyclic-spectral-thinning/units/1/evaluation.md)
record the exact limited approval. The [acceptance input](../attack/admission/cyclic-spectral-accept.json)
pins it. The [post-CP25 all-node comparison](../attack/preflight/frontier-refresh/FR-CP25-20260908-1.md)
keeps all previous failures and node14's deferral. Its formal assessment
continues no admitted strategy and is undergoing fresh independent review.
The proposed next preflight concerns phase-aware removal on the strict-mass
domain; it is not a proved extension or root completeness theorem.
