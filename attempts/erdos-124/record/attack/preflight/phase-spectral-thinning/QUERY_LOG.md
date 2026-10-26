# Phase-aware spectral thinning preflight query log

Date: 2026-09-08. Status: complete,20 of the fixed20 queries used.
This is a source study, not mathematical proof or an admitted new attack.
Formal assessment3 was accepted at363; replan364 records CP25 progress
once without changing route priorities, deferrals or resource accounts.

## Problem-level first-tier queries,1--5

1. arxiv.org index: "powers" "subset sums" "logarithms" "thick"
2. semanticscholar.org index: "powers" "subset sums" "simultaneous approximation"
3. search.crossref.org index: "complete sequences" "powers" "reciprocal"
4. zbmath.org index: "complete sequences" "powers"
5. erdosproblems.com index: "124" "powers" "gcd"

## Constructive-method first-tier queries,6--10

6. arxiv.org index: "compact group" "rotation" "return times" "syndetic"
7. semanticscholar.org index: "almost periodic" "syndetic" "compact group"
8. search.crossref.org index: "Bohr" "recurrence" "Kronecker"
9. zbmath.org index: "Kronecker" "almost periodic"
10. erdosproblems.com index: "124" "Kronecker"

These are domain-filtered index searches, not exhaustive registry or API
traversals. Batch1 covers1--3; batch2 covers4--6; batch3 covers7--10.
Batch1's visible response reported no results. Batches2 and3 are preserved
in full as returned text. The engine combines results within each batch,
so no finer attribution is asserted.

## Relevant hits and constraints so far

- https://www.erdosproblems.com/124 and its thread returned the original
  positive-cutoff problem, the known zero-cutoff distinction and the
  {3,4,7} case. The current indexed display has d_r where the canonical
  statement and discussion have d_i in the reciprocal sum. Do not adopt
  this index/display typo as a changed objective.
- The thread https://www.erdosproblems.com/forum/thread/124 returned
  discussions of Pomerance's necessary-condition argument using near
  alignment of powers and Kronecker approximation. These are research
  leads, not a proof of the proposed strict-mass sufficient condition.
  The comments also distinguish the delicate equality case.
- zbMATH returned BEGL96, Zbl0863.11014, Complete sequences of sets of
  integer powers, Acta Arith.77(2),133--138(1996). It did not return an
  identified exact phase-thinning theorem.
- The source indices returned several unrelated profiles and MSC entries.
  No new recurrence theorem has yet been read from these hits.

## Existing primary material actually read in this preflight

The canonical local sources/124.lean was read completely. Its
Erdos124.erdos124.ne_zero is the unchanged original positive-cutoff
claim; zero cutoff and finite {3,4,7} are separate entries.

The local Bergelson--Simmons arXiv:1507.02208v2 text was inspected at
lines625--655, particularly Claim2.13 and the compact-subsemigroup
argument in footnote10 citing Numakura [19]. The footnote supplies a
primary proof of the compact-semigroup-to-group fact. It does not by
itself establish the required quantitative selected exponent gaps,
and no new mathematical lemma is declared in this study.
The complete paper is not claimed read here. Its exact theorem2.1 and
reserve interface were read in preceding studies.

The prior CP25 proof, accepted12, is the exact predecessor. It requires
removable-core mass one at equation(7). The proposed recurrence must
replace that estimate with a valid strict-mass all-scale invariant,
without assuming full-torus density or multiplicative independence.

## Remaining queries,11--20

11. General web: "minimal rotation" "syndetic" "compact" group
12. General web: "powers" "subset sums" "thick" reciprocal sum
13. General web: "Complete sequences of sets of integer powers"
14. arxiv.org index: "syndetic" "rotation" "compact"
15. General web: "When all closed subsets are recurrent" arxiv
16. General web: "powers" "subset sums" "reciprocal" "thick" "1"
17. erdosproblems.com index: "124" "equality" "cutoff"
18. arxiv.org index: "Bohr sets" "syndetic" "compact"
19. General web: "pure powers" "thick" "finite sums"
20. erdosproblems.com index: "124" "3" "1/2" "positive"

Batch4 covers11--13, batch5 covers14--17 and batch6 covers18--20.
Their complete returned text is saved in sources/query-batch-4.txt,
sources/query-batch-5.txt and sources/query-batch-6.txt. The engine
combines query hits, so individual no-hit claims are not reconstructed.
The fixed count was reached, and no further search is claimed.

## Additional primary reading and findings

BEGL96, DOI:10.4064/aa-77-2-133-138, was retrieved as a primary indexed
paper and its existing local extracted text was read through its end.
It records Pomerance's necessity argument but not a general strict-mass
sufficiency theorem. It also explains its disjoint-supply construction.

Li--Oprocha--Ye--Zhang, arXiv:1504.08191v1,
https://arxiv.org/html/1504.08191v1, was opened from the primary server.
The targeted reading covers the abstract and relevant definitions in
Sections2.1--2.3, especially minimal points, positive syndeticity and
Lemma2.1(2). It supplies the classical minimal-return interface.
Its full HTML is saved as sources/li-oprocha-ye-zhang1504.08191v1.html;
the visible targeted excerpt response is saved separately. The complete
paper is not claimed read. The journal DOI is10.1017/etds.2016.5.

Grivaux--Roginskaya, arXiv:1202.3113, was seen at abstract level only.
It studies recurrence sets for products of rotations, a different
question from bounded returns of a fixed compact rotation. No theorem
from it is imported. Several other hits are unrelated or secondary.

The current #125 thread returned a density-below-one discussion and
the zero-cutoff distinction. It is a warning about nearby claims, not
a proof of strict-mass thickness. General Star Fleet reports were also
returned. The predecessor's relevant #254 source-status addendum was
reread and is expressly retained in problem.md and novelty.md.

The full accepted CP25 proof was reread. Its equation(7) identifies
exactly the removable-core premise that the new operation would replace.
The Griesmer FS-mean transfer is inherited with its stated trusted
published-theorem boundary, not reclassified as a new theorem.

No exact solution of the prospective statement was identified by this
bounded study. The separate problem, novelty and constructive strategy
studies now state the proposed exact-power test and its unproved
all-scale preservation condition. Independent proposal review is next;
this log authorizes no proof writing or mathematical process.
