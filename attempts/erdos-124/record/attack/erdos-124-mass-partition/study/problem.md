# Problem study: high-mass pure-power completeness

## Exact proposed claim

For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+2/m, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

## Queries and reading

See QUERY_LOG.md and its raw source responses for the dated problem-level
and strategy-level searches. This record is completed before proposal
admission; no proof result has yet been produced by the proposed attack.

Primary sources inspected:

- Burr, Erdos, Graham and Li, Complete sequences of sets of integer powers,
  DOI 10.4064/aa-77-2-133-138 (1996). The saved text at the research root,
  sources/begl1996.txt, was read through the introduction, main construction
  and concluding pure-power examples. Its conjecture is the original target.
  Its varying-base and k-dependent large-interval results are not the
  proposed all-k high-mass result for each fixed finite D.
- Bergelson and Simmons, New examples of complete sets, with connections
  to a Diophantine theorem of Furstenberg, arXiv:1507.02208v2,
  DOI 10.4064/aa8221-10-2016 (published 2017). The local text
  sources/bergelson-simmons.txt at the research root was read selectively:
  Theorem 1.23, its set/multiset qualification, Theorem 2.1 and its proof,
  Lemmas 2.11-2.12, and section 2.7. This is not a new discovery.
- Steve Fan, Strongly complete sets and a conjecture of Erdos,
  arXiv:2607.14071v3. Sections 1-2 and the relevant source links were read.
  Corollary 2.3 reduces the completeness mechanism to three components.
  Version 1 had been inspected in earlier attacks, but was not converted
  into an accepted pure-power parameter-range theorem.
- The canonical Erdos124.ne_zero formal statement, URL in QUERY_LOG.md,
  was read with its neighbouring declarations. No formal proof is asserted.
- Accepted checkpoint-000008, acceptance-000001, the minimum-preserving
  reciprocal-core lemma. Its complete local proof
  attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md
  was reread. It is the proposed branch's logical and mathematical predecessor.

## Constraints on the plan

The complete original claim is still open in the controller. Its original
threshold is one, not three. An admitted proof of the proposed range would
leave every D with 1<=sigma(D)<3+2/min D open, including reciprocal equality.

The earlier strong-profile and signed-profile counterexamples do not refute
this pure-power claim. Their generic growth hypotheses are not used as an
unproved completeness engine.

The new task is to connect an explicit finite partition of the actual
base labels to the three-component theorem, including a careful extension
from numerical sets to disjoint occurrence supplies. In particular,
different bases can have equal powers. Neither pairwise coprimality nor
multiplicative independence may be added silently.

The proposed partition uses the accepted reciprocal core for the component
that must retain collective gcd one. The other two components need bounded
prefix deficit, not gcd one. The original positive cutoff and every finite
deletion must be retained in the geometric-sum estimates and modular proof.

A criterion imported from Fan is existing mathematics, not a claimed new
theorem. The mass threshold and occurrence-preserving application require
a new checked deduction. No exact published statement of that quantitative
corollary was identified in this bounded search; this is not proof of novelty.

## Stop reason

The fixed count in QUERY_LOG.md was reached. No finite mathematical run is
proposed. The task is an analytical proof on the existing account.


