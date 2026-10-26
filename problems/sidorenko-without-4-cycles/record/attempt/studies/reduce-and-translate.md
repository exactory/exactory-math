# Strategy study: reduce-and-translate

Node: the statement on bipartite graphs of girth at least six with one side of maximum degree at most two. Study
written on 2026-10-21. Question of the study: which reductions of the Sidorenko property are proved, in which setting,
and how have subdivision questions been translated into statements about base graphs?

## 1. Queries run

Saved in the workspace under `sources/study-queries/`; the manifest `manifest.json` records the URL, the capture time,
the HTTP status and the totals of each.

| Source | Query | Result |
|---|---|---|
| arXiv API | `abs:Sidorenko AND (abs:"regular graphon" OR abs:"regular host" OR abs:"maximum degree" OR abs:pendant OR abs:biregular)` (`red-arxiv-sidorenko-regular-pendant`, 2026-10-21T23:09:58Z) | complete: 4 of 4; Coregliano and Razborov 2021 (read in full), and three works outside the question (common graphs, tree-degenerate graphs, large deviations) |
| Semantic Scholar | `Sidorenko conjecture regular host reduction` (`red-s2-sidorenko-regular-host`, 2026-10-21T23:13:06Z) | unavailable: HTTP 429 on four attempts with 30, 60 and 90 second waits |
| Crossref | `query.bibliographic=Sidorenko property subdivision reduction regular graphon` (`red-cr-sidorenko-subdivision-reduction`, 2026-10-21T23:15:11Z) | top 20 of 914,848 by relevance; none concerns the reduction (land subdivision, spectra, graphon estimation, linear equations) |
| zbMATH Open | `Sidorenko & tree` (`red-zb-sidorenko-tree`, 2026-10-21T23:15:17Z) | complete: 21 of 21; the read works of Kim, Lee and Lee, of Conlon, Kim, Lee and Lee and of Coregliano and Razborov, and class results or works outside the question (higher tree decompositions, tree-degenerate graphs, tournaments, linear equations, Steiner trees) |

The common-store searches on subdivisions and biregular graphs (`problem.md`) are not repeated here.

## 2. Hits worth reading (full texts read in the common store; copies of the first three in `sources/`)

- Conlon, Kim, Lee and Lee 2018, arXiv:1510.06533v2: Lemma 3.3 (attributed there to Fox: for a bipartite H, a lower
  bound c |V(G)|^{|V(H)|} (2|E(G)|/|V(G)|²)^{|E(H)|} on |Hom(H, G)| for every graph G of maximum degree at most
  4|E(G)|/|V(G)| implies the Sidorenko property), Lemma 3.4 (a graph on n vertices with average degree d and maximum
  degree at most 2d has a subgraph on at least 2^{-6} n vertices with minimum degree at least d/4, proved), Theorems 1.3
  and 3.1 (subdivisions of cliques, of Sidorenko graphs and of KNRS graphs), Problem 1.5.
- Kim, Lee and Lee 2016, arXiv:1310.4383v3: Lemma 3.3 with its proof by splitting vertices of large degree, and Lemma
  3.4 (the tensor power trick, proof omitted, Sidorenko's Remark 2).
- Coregliano and Razborov 2021, arXiv:2108.06599v2: Theorem 3.1 (biregular bigraphons suffice, full proof),
  Corollary 5.3 (a vertex of degree one can be removed, bigraph setting), Theorem 8.2 (regular graphons suffice in the
  symmetric setting, proof sketched).
- Im, Li and Liu 2024 and Chen, Lin and Ma 2024 (Lemma 2.2 in both, citing Coregliano and Razborov, Theorem 8.2) and
  Zhao 2026, arXiv:2606.30010v1 (Proposition 1.4(4), the 1-subdivision through the square kernel W∘W of a regular W):
  the translation of a subdivision question into a question about the base graph in a derived kernel.

## 3. What was learned, as constraints on the plan

1. The symmetric regular reduction (Coregliano and Razborov, Theorem 8.2) is published as a sketch; the finite
   bounded-degree reduction (Kim, Lee and Lee, Lemma 3.3, with Conlon, Kim, Lee and Lee, Lemmas 3.3 and 3.4) is fully
   proved. The pendant-vertex step must therefore be proved from the finite lemmas, with the regular reduction cited
   only as a second route.
2. The removal of a vertex of degree one is stated in print only in the bigraph setting (Corollary 5.3); the statement
   is posed for graphons, so the symmetric version must be proved, not cited.
3. The image problem of the reduction must be exactly Problem 1.5 of Conlon, Kim, Lee and Lee, without a hidden
   restriction: the 4-cycle-free condition is what makes the base multigraph simple, and every simple base graph with
   an edge must arise.
4. The known cases of the image problem (KNRS, regular-KNRS or Sidorenko base graphs) transfer back through the
   reduction; the reduction must be stated so that they can be read off.
5. The reduction settles nothing by itself; its value is that the statement on the class is exactly a named open
   problem, so the class cannot be the place where a new counterexample mechanism is found without answering
   Problem 1.5.

## 4. Stop reason

A fixed count: one query per tier-one source. The reductions needed are the published Lemmas 3.3 and 3.4 and
Corollary 5.3, all read in full; the complete arXiv and zbMATH queries returned no further reduction. Semantic Scholar
was unavailable (rate limit), recorded as a gap.
