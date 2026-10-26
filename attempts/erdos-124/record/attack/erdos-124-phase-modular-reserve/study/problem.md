# Phase-restricted modular correction: problem study

Date: 2026-09-08. Exact-claim preflight at revision387. No analytical entry or mathematical process has been executed.

## 1. Statement, queries and canonical comparison

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there exist an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, V=D minus R has min V>=4 and sigma(V)>1, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once and coincident numerical values from different pairs retained separately.

[QUERY_LOG.md](QUERY_LOG.md) records all twelve executed queries, their source indexes, date and complete raw hits. The planned ceiling was fifteen; two consecutive dry neighbour queries ended the study after both five-source floors.

The canonical statement is Erdos124.erdos124.ne_zero in the pinned [canonical file](sources/canonical-124.lean), originally https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/124.lean. The complete105-line file was reread. It quantifies over every positive cutoff and finite base set, imposes collective gcd1 and reciprocal mass at least1, and asks for eventual membership in a sum of digit-restricted sets. The proposal preserves distinct occurrence labels and those cutoff quantifiers, strengthens the conclusion by allowing finite deletion, but restricts the base-set premise by an explicit common-radix criterion. It does not replace the canonical root. The web index displays a denominator typo; the canonical d_i-dependent sum, not that typo, governs this study.

## 2. Primary and inherited evidence inspected

Burr, Erdos, Graham and Li, Complete sequences of sets of integer powers, Acta Arith.77(1996),133--138, DOI10.4064/aa-77-2-133-138, primary PDF https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf. The full six-page extracted text was reread and pinned as [begl1996-extracted.txt](sources/begl1996-extracted.txt). Its original conjecture is the positive-cutoff question. Theorem1 begins with an infinite positive-upper-density base sequence; its disjoint supplies and collective modular correction do not prove the present fixed-finite-D structural criterion. The reported small examples and interval-base theorems remain prior results, not evidence for all cutoffs of arbitrary finite D.

Li, Oprocha, Ye and Zhang, When all closed subsets are recurrent?, arXiv:1504.08191v1, https://arxiv.org/html/1504.08191v1. The return-time definitions and Lemma2.1(2) were reread in the saved primary extract [return-time-primary.txt](sources/return-time-primary.txt); the full paper was not read. They identify bounded returns for a minimal orbit. The proposed proof must establish the appropriate orbit closure for each exponent period. It cannot assume that an arbitrary congruence coset meets the original logarithmic orbit. No source independence theorem is presumed.

CP26, acceptance-000013, checkpoint-000026, node20 move1 Sections1--4, was reread in full for the finite-deletion and compact-return interfaces. Its all-scale one-label estimate uses min bases>=4 and strict mass>1, while its later spectral theorem additionally uses gcd1. Applying the estimate to V with possibly nontrivial gcd requires a scope-checked argument in the new move, not citing the whole theorem beyond its hypotheses. The proof is pinned by manifest d163c10e8912e56761050398242131c0a390f355238b5e98b48e197b672a5a4c.

The common-radix construction, acceptance-000009, checkpoint-000022, node16 move1 Sections1--6, was reread. Its signed lattice uses one label per (base,exponent); its old eventual-completeness statement dedicates an entire collectively coprime correction set C and requires mass>=1 outside R union C. The proposed new operation instead chooses only the correction occurrences, preserving a fixed gap in V. This is not an already proved consequence of the old allocation theorem.

## 3. Constraints and proposed operation

The invariant has two parts: an interval grows by one from each fresh signed unit, and the actual remaining V labels retain the original gap g fixed from V,k,F before the first unit. Positive correction labels are selected one at a time at the fixed CP26 tolerance and scale threshold. Their exponent restrictions should be chosen as multiples of suitable periods, to seek stable residues at prime-power divisors of B^L. Collective gcd(B,V)=1, not coprimality of every individual base, is the available arithmetic input. The common-radix labels then supply the remaining signed multiple on fresh tails.

No proof of simultaneous modular and phase selection is asserted in this study. In particular, it must not invoke full-torus density, subtract two signed sums without checking coefficient capacity, reuse labels, change the tolerance as supports grow, or invoke a fixed-gap estimate with a constant depending on the finished gadget. The failed node8 support-cost approach and node15 universal-scalar approach remain failed on their original scopes.

This claim has a concrete implication absent from the old allocation criterion: it is designed to cover every min-D3 set with total mass>3/2 using R={3}, as well as nonternary common-radix families. The strict complement-mass boundary remains essential. The original mass-one inputs outside this structural criterion, all-half-mass units, and all bridge proofs remain open. No new computation or account renewal is justified by the study.

## 4. Stop and next action

Two consecutive queries returned no new applicable lead after the tier-one floors. Twelve of the at-most-fifteen queries were run. No exact theorem for the proposal was located. Prepare one independently reviewed prerequisite proposal for this structural claim, inheriting the current account, and only then its native plans and reviewed strategy selection. A proposed operation is not proof credit.

