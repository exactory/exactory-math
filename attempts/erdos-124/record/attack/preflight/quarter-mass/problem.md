# Problem study: a quarter-mass surplus

## Exact claim

For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+min{1/4,2/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

## Queries and prior methods

The complete dated source-by-source floor, hits, irrelevant returns,
access failures, reading extent, and fixed-count stop are in QUERY_LOG.md.
The exact threshold and the neighbouring old threshold were searched.
No source returned the exact proposed constant; that is not a priority
certificate. The general three-component argument is already in print.

## Constraints learned

Acceptance-000005 proves the threshold 3+2/m for every m, every k and
every finite labelled deletion. Its proof explicitly supplies the
label-preserving three-component criterion and finite seed amplification.
Acceptance-000001 supplies the minimum-preserving gcd seed construction.
Their quantitative partition step, not their infinite completeness
argument, is the input proposed for refinement.

The prospective hypothesis is that the gcd-seeded first crossing can
be chosen below 9/8 for minima 3 through 7, and the first crossing for
a second bin after removing that core can also be kept below 9/8.
This is not asserted as proved. Large added bases have weights at
most 1/8; the only potentially exceptional additions have bases 3
through 8. Small gcd seeds extending beyond this range must be
treated explicitly, not ignored. A computer-free argument is proposed.

If these two strict bounds hold, their total loss is less than 1/4,
so the accepted three-component amplification can be used at total
mass 13/4, including equality. For minima at least eight the existing
3+2/m result is retained directly. This is a new quantitative proof
question based on accepted evidence, not a reset of the same attack.

The named scope is infinite. No finite prefix computation, bin search,
unbounded range extension, or hidden mathematical process is admitted.
The original sigma>=1 root and the exact complementary range remain
separate obligations.

## Novelty and stop

This is expected to be a modest quantitative corollary of the accepted
method, not new general completeness machinery or a standalone paper.
Cash-out may have no publication units if the claim test so decides.
The exact source studies stopped at their fixed counts.

