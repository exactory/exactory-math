# Consolidation of the binary-block candidate

The closing move is move1. The exact claim is preserved in problem.json
and moves/001-binary-block-reserve.md. This harness-entry record is not
a new mathematical move or accepted controller result.

## Marked steps and their treatment

The steps needing explicit explanation were the signed interval
criterion, the actual multiplicities in a period, the even-radix digit
endpoints, finite termination, original-exponent alignment, and reserve
independence. Sections2-6 of the proof now supply all of them.
The finite table checks eight grouped inequalities by exact displayed
arithmetic; it is not an executed certificate or a substitute for the
signed-interval induction. No computer-dependent step remains.

## Rewritten proof with each role explicit

First fix a reserve of reciprocal mass at least one on bases disjoint
from the seed bases. The geometric strict-prefix bound and numerical
mesh induction give a finite integer gap g, depending only on the
reserve, cutoff and its finite deletion.

The labelled normalized block on4,8,16 has13 weights. Starting at
{0}, adjoining a weight w with w<=2S+1 enlarges a complete signed
interval [-S,S] to [-S-w,S+w]. The exact block satisfies this condition
and reaches [-2223,2223], containing [-2048,2047]. Division with the
latter digit interval gives a strictly decreasing nonnegative quotient
and hence a finite radix4096 expansion of every positive integer.

At a binary exponent L divisible by12 and at least4K, multiply the
t-th block by2^L*4096^t. Its original exponent at base2^e is
(L+12t+r)/e for the offsets r divisible by e, where e is2,3 or4.
This assigns distinct permitted labels in disjoint half-open blocks,
all with exponent at least K.

For an odd b choose J>=K with b^J congruent to one modulo2^L. Expand
(b^J-1)/2^L by the blocks and separate signs, giving two disjoint
positive alternatives with unit difference. Choosing each new K above
all forbidden original exponents and both earlier supports gives
g-1 pairwise disjoint pairs. They represent [A,A+g-1]. None uses
the fixed reserve, so an appropriate reserve sum supplies every
n>=A+g-1. The entire rewritten chain is proved in Sections1-7.

The exact mass bound removes19/35 for4,8,16 and at most1/4 for an
odd b>=5. Thus251/140 leaves at least one, including equality.

## Second-route assessment

The same block could also be organized as a signed-prefix induction
over repeated blocks. That presentation shares the exact block
coverage with this argument, so it is not an independent second
proof. The older quarter-mass theorem does not reach251/140, and the
ternary theorem requires the absent base3. No independent second
route to this exact claim is asserted. There is no need to replace
the short elementary digit proof by computation.

## General statement extracted from the argument

For every finite set D of bases at least4 containing4,8,16 and an
odd b>=5, if sigma(D minus {4,8,16,b})>=1, then its labelled power
supply is eventually complete at every positive cutoff and after
every finite labelled deletion. This is a direct corollary of the
same proof, with the reserve hypothesis given explicitly. It is not
a replacement for the admitted claim or a separately accepted result.

The reusable ingredient is a finite signed block covering a balanced
radix alphabet, with a proved legal repetition on the original labels.
The present proof establishes that ingredient only for the stated
block. Other alphabets, other base families and smaller reserves
remain separate questions, not additional results from this record.

## Local ledger and status

Every auxiliary mathematical obligation is discharged in the closing
move, and the exact claim and quantifier order are unchanged. The cost
ledger is empty. The construction is finite and effective in principle,
but no efficiency or input-independent threshold is claimed. There is
no proof dependency outside the local argument. Independent result
review and controller acceptance are still required. The original
root remains open; no publication or formalization is claimed.
