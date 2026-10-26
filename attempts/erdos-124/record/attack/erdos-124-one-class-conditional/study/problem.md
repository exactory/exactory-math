# Problem study: the one-class conditional route

Date: September 8, 2026.
Status: prospective analytical work. No successor move has been executed.

## Exact target

For every nonempty finite set D of distinct integers at least 3 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=2+min{1/8,1/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

The target is unconditional. A proof of an implication with an unresolved
hypothesis does not prove this sentence.

## One named missing input

OC is the following named hypothesis, not a theorem.

For every nonempty finite set E of distinct integers at least 3 with sigma(E)=sum_{d in E}1/(d-1)>=1, every integer k>=1 and every finite deletion F of labels (d,j), d in E and j>=k, there exist an integer r>=1, theta in (R/Z)^r, an open set U in (R/Z)^r meeting K=closure{n*theta:n in Z}, and a set J of positive integers containing intervals of every finite length, such that every n in J with n*theta in U can be written as sum_{(d,j) in H}d^j for some nonempty finite set H of remaining labels.

Finite sums are numerical values of finite nonempty label sets. Equal powers
from distinct pairs remain separately available. The condition U intersects K
prevents an empty Bohr set; J is thick towards positive infinity. No uniform
dimension, gap constant, open set or threshold is requested.

The prospective restricted input WOC is:

For every nonempty finite set E of distinct integers at least 4 with sigma(E)=sum_{d in E}1/(d-1)>1 and every integer k>=1, there exist an integer r>=1, theta in (R/Z)^r, an open set U in (R/Z)^r meeting K=closure{n*theta:n in Z}, and a set J of positive integers containing intervals of every finite length, such that every n in J with n*theta in U can be written as sum_{(d,j) in H}d^j for some nonempty finite set H of labels (d,j) with d in E and j>=k.

The proposed two applications first establish OC implies the exact target,
then trace its actual use and attempt to justify WOC implies that same target.
WOC removes reciprocal equality, the minimum-three supply, and explicit finite
deletions from the input. These restrictions are proposed for verification,
not asserted as established results in this study.

## Prior results read and constraints

The exact queries and all raw hits are in QUERY_LOG.md and sources/.
Fourteen problem/neighbor queries and seven strategy queries were run using
domain-filtered web searches. Every level includes arXiv, Semantic Scholar,
Crossref, zbMATH and the Erdos problem database, then the second tier.
A domain-filtered search is not a complete database API search.

The main agent reread the complete pinned canonical response at
../mass-partition/sources/canonical-124-reading.txt. The root is
Erdos124.erdos124.ne_zero, source lines43-54. The outer finite sum of per-base
sets retains occurrence multiplicity. The proposed target restricts D by a
higher reciprocal mass and strengthens the conclusion to finite deletions.
It neither substitutes the solved zero-cutoff statement nor fixes k=1.

The complete local accepted proofs read are:
../../erdos-124-mass-partition/moves/001-high-mass-completeness.md and
../../erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md.
The former uses two disjoint syndetic finite-sum supplies and a gcd-one
correction/reserve supply of mass one. Its Sections3.2-3.3 explicitly prove
the phase closure and finite correction on labels. The latter's Section2
proves a minimum-preserving gcd-one core of mass in [1,9/8); the earlier
accepted core gives [1,1+1/m). Their thresholds alone are not these
intermediate lemmas. Acceptance-000001, acceptance-000005 and
acceptance-000006 must be cited and audited if those intermediates are used.

Bergelson-Simmons, arXiv1507.02208v2, DOI10.4064/aa8221-10-2016,
Lemma2.12 supplies the published two-syndetic piecewise-Bohr theorem.
The publisher and author pages were inspected as selected excerpts, not a
new full-paper review. Fan2607.14071v3, Lemma2.2 is the finite-correction
source already pinned in the accepted mass proof. These established inputs
do not state OC or WOC.

Host-Kra, Nil-Bohr sets of integers,
https://www.math.northwestern.edu/~kra/papers/nilcubes.pdf,
Definition2.7 and Theorem2.8 send Delta-star sets to strongly piecewise
Bohr-zero sets. Definition2.5 and Theorem2.6 concern finite-sums dual sets
and nilpotent structure. The introduction and theorem excerpts were read,
not the complete proof. This gives a possible future sufficient input,
not a proof that the present finite-sum sets are Delta-star. Ordinary
syndeticity, containing an IP set, and higher-step nil-Bohr structure must
not be substituted for that hypothesis.

Griesmer, Sumsets of dense sets and sparse sets, arXiv0911.2278,
https://arxiv.org/html/0911.2278, Theorems1.4 and3.1 and their deduction
from Proposition3.2 were inspected. An equidistributed averaging sequence
and positive density for the other summand yield piecewise-Bohr structure;
full relative density yields thickness. This still concerns a sumset,
and no required disjoint sparse averaging supply was established here.
Neither thickness alone nor reusing its representation labels supplies
the final syndetic reserve. This is a prospective alternative, not a
dependency of the conditional proof.

Chen-Fang-Hegyvary, DOI10.4064/aa8133-3-2016, studied in
../post-common-radix/DISCOVERY_NOTES.md, uses mixed products p^n a_i.
Their presence in that theorem is not legal access to mixed products in
a union of pure power streams. No such transfer was established.

## Neighbours, novelty and limits

The accepted common-radix theorem at checkpoint22 is a different structural
positive family. Its constructive unit mechanism and the recorded scalar
obstruction do not establish one-class Bohr structure for arbitrary bases.
The accepted high-mass range remains 3+min{1/4,2/m}; the minimum-three
11/6 and structural common-radix families remain available independently.

No exact OC, WOC or target theorem was identified by this bounded search.
That is not an assertion of publication priority. The conditional implication
may be a useful explicit corollary of the existing correction method, not
a substantial standalone publication. No equivalence between OC or WOC
and the high-mass target was found; absence of a found equivalence is not a
proof of strict logical weakness.

The desired candidate threshold is 2+min{1/8,1/m}. No claim of optimality
is made. The remaining reserve must be fixed after its finite correction
labels are chosen, and every subsequent interval must use the other supply.
The exact allocation and all strict endpoints must be verified in the move.

## Stop reason

The fixed counts, fourteen problem/neighbor queries and seven strategy
queries, were reached. Unrelated and secondary hits are retained as raw
discovery, not imported as mathematical facts. No finite computation,
unbounded prefix extension, external publication or native cash-out is proposed.
