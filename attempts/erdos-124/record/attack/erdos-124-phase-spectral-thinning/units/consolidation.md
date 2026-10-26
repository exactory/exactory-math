# Consolidation of the phase-aware partition candidate

Node20, move1, at the native closing boundary. Status: pending independent
exact-result review. The complete rewritten proof is
[001-phase-spectral-thinning.md](../moves/001-phase-spectral-thinning.md).
This consolidation neither adds a mathematical move nor changes the claim.

## Marked steps and replacements

| Marked step | Consolidated argument and exact role |
| --- | --- |
| An unexplained favorable phase margin | For z>1, each (p_d(z)-1)/(d-1) is an integer. Their sum is strictly greater than ceil(z)-1, hence at least ceil(z). This gives sum p_d(z)/(d-1)>=z+sigma, proof(5). |
| Extending the old removed-base coefficient estimate below one | Do not use that coefficient. Near q, retain each aligned base prefix below a_d; at intermediate scales compare to the integer ideal model; far away use the ordinary delta x surplus. Proof(8)--(10) cover all x and give one fixed margin. |
| Moving tolerance or scale parameters | Fix rational K, epsilon, eta and Lambda in proof(1), depending only on D. Their algebraic inequalities give an absolute margin exceeding one half eta q, without iteration-dependent adjustment. |
| Assuming generic simultaneous equidistribution | Use compactness of the actual logarithmic orbit closure. Its forward orbit is dense in that compact subgroup; a finite open cover gives bounded waiting. No logarithmic independence premise is introduced. |
| Transferring finite-prefix gaps to an infinite reserve | At each fixed scale only finitely many selected values have been removed. Estimate that actual prefix directly, then use the ordinary finite gap induction. Do not commute FS_0 with an intersection. |
| Inferring a full mean from character cancellation alone | First use the sequence of countably additive Bernoulli subset-sum measures and dominated convergence for every finite Radon spectral measure. Only then take a weak-star cluster point. |
| Reusing labels in a sumset theorem | Q and R are an actual occurrence partition. Their numerical sumset is exactly the legal FS_0 of the full supply. Values coinciding across labels do not consume the same resource. |

## Rewritten proof chain

For fixed D,k,F write sigma=1+delta, C as in the claim, and g=ceil(C).
Let K=2+2/delta, epsilon=delta/[4(sigma+2K)], eta=delta/(2sigma),
and Lambda=2 max(D)+2/eta. These are fixed positive rationals.

Cycle through all bases and take the least h-power q above
Lambda(C+W) having a power a_d of each base in the fixed
[(1-epsilon)q,(1+epsilon)q] window. The all-scale invariant comes
before the seed. Each a_d exceeds d^k and each preceding d-power
is below q.

For q<=x<=(1+epsilon)q, the base prefixes below a_d exclude the
selected label and sum, after deletions, to at least
x+(3delta/4)q-C-W. For (1+epsilon)q<x<=Kq, compare least powers
above x to (1-epsilon)q times the ideal powers at
z=x/((1+epsilon)q). The integer geometric inequality gives the
same bound after paying q. For x>=Kq, the elementary surplus
gives at least x+q-C-W. In every case the total exceeds
x+(eta/2)q. Before the first removed value it is at least x-C.

This proves the prescribed deficit for every finite selected prefix
and for the actual infinite complement. Ordering labels and applying
the two-translates subset-sum induction gives the same gap g.

In each cyclic base, compact return times to a fixed neighborhood
of zero in the actual orbit closure have a fixed forward waiting
bound. The operation therefore terminates and has a multiplicative
upper growth bound. One nonempty selection is the smallest seed;
its absolute margin is positive. Iteration has bounded every-base
selected exponent gaps.

If a character tends to zero on those selected powers, bounded
exponent gaps extend the limit to all powers of every base.
The nearest-integer recurrence forces its denominator to divide
powers of every base, so collective gcd one makes the character
trivial. Nontrivial characters therefore have divergent square mass.

The Bernoulli measures have character limits equal to the trivial
character indicator. Dominated convergence before taking a mean
gives Griesmer's full FS-mean condition. FS_0(R) has positive
invariant density and FS_0(Q) has full FS-mean mass. The exact
Corollary4.2(ii) gives thickness of their sumset, FS_0(P).
Finite-prefix enumeration consequently terminates with legal
witnesses for every requested interval length. The procedure is
described, not run.

## Independent second route and generality

The simpler global estimate delta x-C-W-q does not cover the
near scales when delta is small. CP25's alternative removed-base
estimate needs sigma(D minus {h})>=1, which the new claim omits.
Neither is an independent full route to this claim. The consolidated
proof remains one route, not a second-proof unit.

The prefix preservation and compact-return parts do not use gcd one;
that hypothesis enters the conclusion that no nontrivial character
survives. This records the componentwise assumption boundary within
the single theorem. No wider minimum-base or equality result is
asserted as an additional unit or checkpoint.

The positive delta margin is essential to the displayed construction.
No limiting argument proves equality. The final sumset already uses
R; it leaves no additional disjoint bounded-gap reserve. Therefore
the argument proves the exact partition and full-supply thickness,
not eventual completeness, the subunit half-mass problem, or the root.

## Evidence and costs

The complete proof states every lemma or the exact trusted primary
interface with its identifier. Its Griesmer theorem boundary is the
same as the inherited accepted spectral proof; no new formal or
computational certification is claimed. The closing journal pays
no costs because no required assertion or prescribed bound is lost.
No deterministic step exists. Freeze the proof and exact claim,
obtain an independent result review, and accept only through the
controller's immutable-evidence audit.

