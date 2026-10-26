# Cyclic spectral thinning query log

Date: 2026-09-08. These are statement and method studies, not proof evidence.
The fetched web responses are preserved verbatim under sources. Combined
search output does not establish that any registry was searched exhaustively.
Direct API failures are recorded as failures, not successful database queries.

## Problem study

Fixed ceiling: 16 statement or method-discovery queries, plus primary text reads.
The preliminary four discovery queries and the following twelve indexed,
API and final queries reached that ceiling. The problem database is included
through its indexed fallback, with an additional direct primary page read.

1. General: "subset sums" "syndetic" "subsequence" spectral.
2. General: "strongly complete" "removing" "powers".
3. General: "integer powers" "thick" subset sums.
4. General: "complete sequences" "bounded gaps" "subsequence".
5. arXiv index: site:arxiv.org "subset sums" "bounded gaps" "powers".
6. Semantic Scholar index: site:semanticscholar.org "complete" "powers" "syndetic".
7. Crossref index: site:api.crossref.org "complete sequences" powers.
8. zbMATH index: site:zbmath.org "complete sequences" "powers".
9. arXiv API: integer powers AND (subset sums OR complete sequences), maximum 5.
10. Semantic Scholar API: integer powers subset sums bounded gap, limit 5.
11. Crossref API: integer powers subset sums bounded gap, rows 5.
12. zbMATH API: complete sequences powers.
13. Problem index: site:erdosproblems.com/124 "powers" "gcd".
14. General: "powers" "subset sums" "syndetic" "removing".
15. General: "complete sequences" "thinning" powers.
16. General: "integer powers" "thick" "subsequence".

The exact encoded API URLs and primary abstract reads are in
sources/skeletonProblemPrimary.txt. All four direct API calls were refused
by the web tool's safe-open boundary. The direct Problem 124 page returned
403. Indexed fallbacks were attempted and their limitations remain.
Queries 1--4 are in skeletonPreflightQ1, 5--8 in skeletonProblemTier1,
9--12 in skeletonProblemPrimary, 13 in skeletonStrategyTier1a, and
14--16 in cyclicProblemFinalQueries. The count includes the indexed
problem fallback, not the primary page read.

The combined responses returned Bergelson--Simmons and earlier completeness
references, database profiles, and many unrelated hits. No exact removable-core
criterion or cyclic label partition was identified. The last three queries
were particularly noisy; no theorem is imported from their unrelated hits.
An intersective-sets paper was visible by abstract/snippet only and is not a
dependency. A lack of an indexed match is not a novelty certification.

## Constructive strategy study

Fixed ceiling: six method queries, reached.

1. arXiv index: site:arxiv.org "syndetic" "subsequence" "powers".
2. Semantic Scholar index: site:semanticscholar.org "subsequence" "complete sequences".
3. zbMATH index: site:zbmath.org "subset sums" "subsequence".
4. Crossref index: site:api.crossref.org "subset sums" "subsequence".
5. Problem index: site:erdosproblems.com/124 "signed".
6. General: "powers" "syndetic" "deletion" mathematics.

The first three are in skeletonStrategyTier1a; the rest are in
skeletonStrategyTier1b. Every tier-one source was queried through its web
index. These are index attempts, not successful comprehensive API searches.
No exact constructive thinning lemma was identified.

## Primary identifiers and reading boundaries

- Bergelson and Simmons, arXiv:1507.02208v2, on completeness of sparse
  sequences. The local text ../../../sources/bergelson-simmons.txt
  has been inspected at Theorem 2.1, the Cassels discussion, and Remarks
  2.4--2.7. This is not claimed as a whole-paper reading.
- Griesmer, arXiv:2507.10512v1. The abstract was refreshed in the saved
  primary response. The previously saved local full text
  ../../../sources/griesmer2507.10512v1.txt supplies Corollary 4.2(ii)
  and the definitions used in the accepted CP24 argument. Theorem 3.17
  remains a published, trusted dependency, not a theorem reproved here.
- Fan, arXiv:2607.14071v3, was checked by its current abstract and the
  previously saved v3 local reading extracts at its gap/FS lemmas.
  Its completeness partition is background, not proof of this claim.
- Formal Conjectures, FormalConjectures/ErdosProblems/124.lean, local
  ../../../sources/124.lean, was read in full. The canonical positive-
  cutoff statement is Erdos124.erdos124.ne_zero, not the solved zero case.

No source's abstract, search snippet, or reported status is treated as an
independent proof or a root acceptance.
