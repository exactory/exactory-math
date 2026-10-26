# Checkpoint report: checkpoint-000002

Overall proof-completion estimate: 2% (subjective, low confidence).
This retrospective research-planning estimate is not a verified fraction of
the proof, a probability of success, or a fraction of the remaining time.
See [reporting policy](README.md) for its interpretation.

This copy adds the estimate retrospectively; the
[original checkpoint report](../attack/checkpoints/checkpoint-000002-report.md)
remains unchanged. The original snapshot content follows.


Date: 2026-09-06.
Source: node-000001, journal moves 1 through 3.
Previous checkpoint: checkpoint-000001.
Status: hypothesis checkpoint. The original objective remains open.
Research usage: 3 of 24 shared moves, 0 mathematical runs.
Evidence manifest: 7ea2142c85bba2678bbafd4e265de5b7833ff64225e954dd2f5128a6a86de917.

## Original objective

For every finite set D of distinct integers d >= 3 with gcd(D)=1 and
sum_{d in D}1/(d-1)>=1, and every integer k>=1, every sufficiently large
integer is a finite sum of labelled occurrences d^j with j>=k, each pair
(d,j) used at most once. Equal numerical values retain their multiplicity.

No part of this quantification has been removed or declared solved.

## What changed

Move 1 proposed C1: after any finite deletion F, the first m remaining
occurrences eventually represent the whole central interval [L,S_m-L],
where S_m is their total and L is independent of m. Taking F empty and
S_m>=n+L shows that C1 implies the original objective. C1 remains unproved.

Moves 2 and 3 exposed two different obligations: producing an actual
represented interval, and maintaining it at every subsequent prefix.
The existence of a short interval alone does not supply the second.

## Exact analytical output

Let a_i be the remaining occurrences in nondecreasing order. For a prefix
beyond every deleted value, let q=a_{m+1} and let x_d be the next unused
power of base d. Put

    sigma = sum_{d in D}1/(d-1),
    C = sum_{d in D}d^k/(d-1) + sum_{(d,j) in F}d^j.

The geometric-series identity gives

    S_m-q = (sigma-1)q + sum_{d in D}(x_d-q)/(d-1) - C.

Since x_d>=q, the surplus is at least (sigma-1)q-C. Consequently, when
sigma>1, a nonempty represented seed [L,S_m-L] together with

    (sigma-1)q >= C+2L-1

guarantees that this interval extends to [L,S_r-L] at every later prefix r.
The proof uses the exact disjoint-occurrence recursion
T_{r+1}=T_r union (T_r+a_{r+1}) and the interval length condition
a_{r+1}<=S_r-2L+1.

This is a conditional sufficient criterion, not an existence proof for the
seed. It is an elementary Brown-type argument and is not claimed as a new
completeness theorem. The equality case sigma=1 still needs a stronger
all-future estimate; the displayed lower bound alone is insufficient.

## Hand-checked obstruction to the attempted base

For D={3,4,7}, k=1, the first six values are 3,4,7,9,16,27.

- The first four terms have maximal central interval [9,14].
- After adding 16, the maximal central interval is [19,20].
- After adding 27, the total is 66 but 33 is absent, so no nonempty central
  interval exists.

Moreover, 18 and 33 are absent from the entire tail: each is absent from
the prefix containing every term at most that integer, and all later
terms are too large. Thus neither of the early endpoint losses can
support C1 at later scales. These are finitely many omissions, not a
disproof of eventual completeness. BEGL96 already proves eventual
completeness for this particular family at cutoff 1.

## Verification status

The identities, endpoint induction and small case splits are written out in
the evidence files. Independent mathematical review of moves 2 and 3 is
pending at this snapshot. No controller-accepted result or formal proof is
claimed. C1's independent admission review approves investigation only.

Checkpointing preserves the record; it does not confer theorem status or
increase the research account.

## Search tree and remaining work

The root node remains the full original objective. The separately admitted
native child node-000002, erdos-124-central-prefix, carries C1. It inherits
the same account and is linked to checkpoint-000001. Its proposed route has
a separate C1-to-root implication obligation, obligation-000003, which also
requires acceptance before the route can close.

The present early-seed induction did not satisfy its strengthened base
condition. The next hypothesis is to choose the seed scale and endpoint
loss together, rather than propagate the first available short interval.
Seed existence and the critical-mass extension problem remain unresolved.

## Evidence

- [Candidate and implication](../attack/erdos-124-positive-cutoff/moves/001-central-prefix-candidate.md)
- [Small-prefix diagnostic](../attack/erdos-124-positive-cutoff/moves/002-small-prefix-test.md)
- [Seed and surplus argument](../attack/erdos-124-positive-cutoff/moves/003-seed-and-surplus.md)
- [Immutable evidence manifest](../attack/checkpoints/root-002-manifest.json)
- [Successor proposal](../admission/c1-proposal.json)
- [Independent successor-admission review](../admission/c1-review.json)

Primary context: Burr, Erdos, Graham and Li (1996), DOI
10.4064/aa-77-2-133-138; Bergelson and Simmons (2017),
arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016. Their known interval and
disjoint-supply methods are distinguished from the unresolved seed here.

All work remains local. Nothing has been committed or published.
