# Exact-result novelty check

Date: 2026-09-07. Target: an infinite sequence with bounded multiplicity,
legal signed integer coverage and arbitrarily long positive intervals
in every tail, the stated arithmetic and all-sublinear-power surplus
profile, but numerical subset-sum upper density at most one ninth.
See study/problem.md for the original inference and the source
distinctions; see the preflight ERRATA.md for corrected irrelevant-hit
descriptions. No publication priority is asserted.

## Unit-level first-tier queries

- arXiv: all:"complete sequences" AND all:"signed". URL: https://export.arxiv.org/api/query?search_query=all%3A%22complete%20sequences%22%20AND%20all%3A%22signed%22&start=0&max_results=5. Saved response: study/unit-sources/arxiv-unit.txt.
- Semantic Scholar: complete sequences signed sums perturbed sequences. URL: https://api.semanticscholar.org/graph/v1/paper/search?query=complete%20sequences%20signed%20sums%20perturbed%20sequences&fields=title,year,externalIds&limit=5. Saved response: study/unit-sources/semantic-unit.txt.
- Crossref: complete sequences signed sums perturbed sequences. URL: https://api.crossref.org/works?query.bibliographic=complete%20sequences%20signed%20sums%20perturbed%20sequences&rows=3. Saved response: study/unit-sources/crossref-unit.txt.
- zbMATH: ti:"Completeness properties of perturbed sequences". URL: https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22Completeness%20properties%20of%20perturbed%20sequences%22. Saved response: study/unit-sources/zbmath-unit.txt.
- Erdos problem database: positive cutoff power sequences. URL: https://www.erdosproblems.com/124. Saved response: study/unit-sources/erdos-unit.txt.

arXiv returned three irrelevant results, whose abstracts were read:
- http://arxiv.org/abs/2509.10824v1, Multi-Task Diffusion Approach For Prediction of Glioma Tumor Progression.
- http://arxiv.org/abs/2411.01691v2, Closing the complexity gap of the double distance problem.
- http://arxiv.org/abs/2608.05002v1, HaploPerturb: Low-rank copula construction of haplotype perturbations improves sequence-to-function analysis of Alzheimer's disease loci.

Semantic Scholar returned 429. No retry was made and no negative
literature conclusion is drawn from that response.

Crossref returned:
- DOI 10.22541/au.177368891.19811728/v1, Sums of Sums Sequences.
- DOI 10.1016/0022-314x(88)90105-9, Sums of perturbed sequences of integers.
- DOI 10.4236/am.2017.811120, Complete Convergence of Weighted Sums for Asymptotically Almost Negatively Associated Sequences.

These were bibliographic records, not full-text readings. Burke and
Webb is a potentially relevant perturbation paper, not confirmed to
contain this exact conjunction. The other two records do not state it.

zbMATH returned 3735923, Zbl0469.10037, Burr and Erdos, Completeness
properties of perturbed sequences, J. Number Theory13 (1981),446-455,
DOI10.1016/0022-314X(81)90036-6. The review was read. It describes the
sensitivity of completeness and subcompleteness to perturbations but
does not state this exact signed-tail and squared-norm conjunction.
The review is not a substitute for a primary theorem.

The refreshed problem page retains the positive-cutoff question as
open and distinguishes the zero-cutoff and fixed-base results. It is
not a database for this newly defined auxiliary sequence inference.

## Focused queries, source comparisons and stop reason

The following web queries were run:
- "complete sequences" "signed" "perturbed"
- "nearly complete" "not complete" sequence sums
- "sequence" "subset sums" "surplus" "signed"

The full returned records, including irrelevant hits, are saved in
study/unit-sources/web-unit.json. The relevant mathematical hit was
Schissel, Characterizations of three types of completeness,
https://www.fq.math.ca/Scanned/27-5/schissel.pdf, a search excerpt only.
Its vocabulary distinguishes coverage of all positive integers from
eventual coverage; no theorem from its excerpt is used. Other returned
records concern genomics, course audits, semantics, trees, calculus,
Fibonacci sums, unrelated discrepancy, algebra or graph conjectures;
none supplies the exact result. Search snippets are not proof evidence.

The primary Graham Lemmas1 and4 read during the problem study explain
long intervals and the separate-supply completeness construction.
They do not state the present counterexample or the exact conjunction.
The prior local paired construction lacks a proved legal signed-unit
property, so it cannot simply replace the new proof. The new argument
in the evidence file is self-contained.

The fixed count of five first-tier requests and three focused queries
was reached. The search located no exact prior statement, subject to
the stated access and reading limitations. In particular this is not
an exhaustive novelty check of every perturbation theorem. The result
is retained as an internal auxiliary counterexample resolving a
specific proposed route, not presented as a standalone publication
with established novelty or broad significance.
