# Problem study: adding legal signed units to the strong profile

Read QUERY_LOG.md for the full dated query record and sources/ for responses.
This is a distinct auxiliary inference, not a replacement of Erdős 124.

## Exact question

For every nondecreasing locally finite infinite positive-integer sequence
with bounded numerical multiplicity, assume every tail has gcd one and full
finite-subset-sum coverage modulo every positive integer, its labelled
counting liminf (log 2) A(X)/log X is greater than one, its squared norms
sum to infinity for every irrational multiplier, and
(S_m-a_(m+1))/a_(m+1)^beta tends to infinity for every fixed beta in (0,1).
Add: every tail contains two disjoint finite label sets P,Q with
sum(Q)-sum(P)=1. Does there exist a fixed L such that all sufficiently
late finite prefixes cover [L,S_m-L]?

The added property is occurrence-respecting. Coefficients in a signed
identity are only -1,0,1 per label. An unrestricted Bezout identity is
not enough. Arbitrarily large support is permitted.

## Canonical root and neighbours

The canonical root remains Erdos124.erdos124.ne_zero in
../../../sources/124.lean. It quantifies over all finite distinct bases
at least 3, all positive k, gcd one, reciprocal mass at least one, and
all sufficiently large integers, using each (d,j) once. The zero-cutoff
lemma and the specific {3,4,7}, k=1 lemma do not decide it. The current
abstract claim has no assertion that its hypotheses hold for pure powers.
That profile and the implication bridges must be separate obligations.

Neighbour status, with evidence:
- The same abstract inference without legal signed units is false:
  accepted node-000006, moves/001-paired-perturbation.md, complete
  analytical proof read. Its affine coefficient 3 exceeds the two
  available copies and cannot establish the new condition.
- Persistent signed unit identities imply arbitrarily long represented
  intervals: Graham (1964), Lemma 4, full proof read on pp. 277-278.
  This does not specify a common central loss L.
- A separate bounded-deficit supply plus a nearly complete supply yields
  completeness in Graham's Lemma 1. The supplies cannot be the same
  labelled terms used twice.
- Actual pure-power deep bounded nonzero signed identities cannot have
  bounded support size: node-000008 move 2, read completely, an ESS
  corollary recorded as a method finding. It does not rule out increasing
  support. Neither it nor its hypothesis checkpoint is new proof credit.
- The common-base coefficient setting of Chen, Fang and Hegyvári (2016)
  is different; only its publisher abstract was read.

## Constraints on the plan

Test whether increasing-support legal unit gadgets repair the previous
generic failure, before investing in the stronger pure-power profile.
The predecessor's coefficient-three identity cannot simply be relabelled.
Any counterexample must check all prefix types and every fixed beta,
not only selected block endpoints. Its norm proof must handle support
lengths tending to infinity; convergence of each norm alone is not
enough. Full modular coverage must respect labels.

A viable construction question is to alter sparse endpoints of a
slowly perturbed geometric sequence, forcing a legal signed identity
over a long block. The alteration must preserve both the lower digit
weight bound controlling numerical support and all-prefix surplus.
This is a hypothesis, not an established result in this study.

## Stop reason

The bounded query count in QUERY_LOG.md was reached. No exact answer was
located, subject to the reported access limits. No global novelty claim
is made. No lemma was proved and no mathematical process was run during
this study.
