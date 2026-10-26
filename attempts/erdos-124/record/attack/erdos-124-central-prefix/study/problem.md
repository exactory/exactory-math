# Problem study: central-prefix coverage after finite deletion

Date: 2026-09-06. This is a successor study, not a restart of the root.

## Exact statement and lineage

Candidate C1 asks: for every finite set D of distinct integers d >= 3 with
gcd(D)=1 and sum 1/(d-1)>=1, every k>=1, and every finite deleted set F of
labelled occurrences, do the remaining occurrences a_i, ordered by value and
then by base label, have constants L>=0 and m_0>=1 such that all integers in
[L,S_m-L] belong to the subset sums of a_1,...,a_m for every m>=m_0?
Here S_m=sum_{i<=m}a_i. Repeated numerical values remain separate occurrences.

The logical predecessor is root move 1 and its hypothesis checkpoint.
The root move gives only an elementary implication from C1 to the complete
original claim, not a proof of C1 or an accepted dependency.

The canonical formal root is Erdos124.erdos124.ne_zero in the inspected
FormalConjectures/ErdosProblems/124.lean. C1 adds finite-prefix control and
finite-deletion quantification. It is not presented as that formal declaration.

## Queries and hits

All queries below were run on 2026-09-06.

- arXiv web: `site:arxiv.org "subset sums" "central interval"`; no applicable
  result returned. API: `ti:complete AND (all:powers OR all:sequences)`, first
  three results. These concerned matrix powers or commutative algebra and were
  excluded. The inherited focused arXiv search had identified 1507.02208v2.
- Semantic Scholar web: `site:semanticscholar.org "complete sequences"
  "interval"` and `site:semanticscholar.org "completeness" "integer sequences"
  "Brown"`. A Fibonacci partitions result referred to classical completeness
  papers; no C1 theorem was obtained. API query `complete integer sequences
  finite subset sums interval` returned HTTP 429, with no usable result.
- Crossref API query `complete integer sequences semi completeness interval`,
  three results: Brown's 1963 equivalence paper, DOI 10.2307/2687907 and
  10.1080/0025570X.1963.11975438, and his generalization paper, DOI
  10.1080/00150517.1963.12431594. Only metadata were read; no theorem is imported.
- zbMATH web: `site:zbmath.org "complete sequences" "finite"` and
  `site:zbmath.org "semi-completeness" "integer sequences"`. No exact C1
  theorem was obtained. The primary DML-CZ metadata at
  https://dml.cz/handle/10338.dmlcz/126904 identifies the 1966 paper by Bosak,
  Kotzig and Znam, MR0201385, Zbl0144.28003, and cites Brown. Only its catalogue
  and references were inspected, not its theorem text.
- Erdős database web: `site:erdosproblems.com/124 "interval"`; the problem-124
  discussion returned the zero-cutoff warning. The previously refreshed exact
  problem, discussion, proof-claim page, and formal statement remain recorded
  in the root study. An unrelated discussion of problem 346 mentions an
  interval-extension argument; its comments were not accepted as a theorem.
- General web: `"complete sequences" "central" "subset sums"`,
  `"powers" "subset sums" "interval" "Erdős" "124"`, and
  `"On the Equivalence of Completeness and Semi-Completeness" sequences`.
  No exact proof or disproof of C1 was identified.

## Primary evidence and constraints

The inherited full-text study of BEGL96, DOI 10.4064/aa-77-2-133-138, separates
bounded gaps, a long interval, and modular coverage. The cutoff-1 examples do
not prove C1 uniformly for all cutoffs.

Bergelson-Simmons, arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016, uses three
disjoint bounded-deficit supplies and a separate irrational/modular supply.
The original study inspected Main Theorem 2.1 and Theorem 1.23 in full; this
successor reread Remarks 2.3-2.7 about sufficient growth and the disjointness
issue. This is a known sufficient completeness method, not a proof that one
reciprocal-mass block has C1. The incomplete syndetic examples exclude treating
bounded gaps as interval coverage.

The elementary extension operation from root move 1 is already a Brown-type
operation. The new research question is whether a seed satisfying all future
extension requirements can be obtained from the pure-power hypotheses. Neither
the operation nor the bibliographic search is claimed as novel mathematics.

## Stop reason

The fixed first-tier query count, with a second focused web query where the
initial query was broad, was reached. No exact C1 solution was identified.
The record preserves the inaccessible metadata-only papers and the rate limit;
it does not infer absence of literature from those failures.
