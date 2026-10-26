# Spectral Book

## Problem

Relate graph booksize and triangle counts to the spectral radius at both the vertex and edge thresholds, identify equality examples, and establish stability at those thresholds.

## Claims

Theorems 1.2, 1.3, 1.5 and 1.6 give sharp spectral booksize bounds. Theorem 1.7 sharpens the triangle-count lower bound. Theorems 1.8 and 1.9 give stability alternatives. Lemma 4.3 proves that a bipartite m-edge graph of spectral radius lambda is within 3(m-lambda^2) edge additions/deletions of a single complete bipartite graph, with isolates allowed. Lemma 4.4 gives a cut with at most (h-lambda^2)(1+2 beta/(lambda-3 beta)) internal edges when lambda>3 beta.

## Assumptions

Finite simple undirected graphs and adjacency spectral radius. Lemma 4.3 assumes bipartiteness. Lemma 4.4 assumes a connected component with at least one edge and lambda>3 beta. Theorem 1.9 is a near-threshold dichotomy and allows an unbalanced complete bipartite target on subsets of the original vertex set.

## Methods

Perron-vector weighted local triangle and outside-neighbourhood counts, exact identities, equality analysis, and explicit constructions. Lemma 4.3 uses Cauchy-Binet to count nonzero 2 by 2 minors of the biadjacency matrix and averages edit costs over edge-neighbourhood bicliques. Theorem 1.9 first deletes internal edges of a cut and then controls spectral loss with Weyl and Frobenius norm estimates.

## Evidence

Read the complete captured HTML extraction including the references and Appendix A. Cross-checked its statements and notation against the native PDF extraction and rendered PDF pages 4, 5, 14, 15, 17, 19, 20, 21 and 22. Inspected both figures and both tables; the table of small tight graphs is reported by the paper, not independently reproduced here. Followed the Cauchy-Binet argument and the counting behind equations (28)-(30).

## Limitations

The linear factor-three edit bound is stated and proved only for bipartite graphs. The general graph stability proof uses a square-root spectral perturbation estimate after deleting a cut complement. It does not state the same linear factor-three bound for all triangle-free graphs. The paper has no formal verification supplied here; its cited results have not all been independently read. Text-only reviewer delivery will not establish their inspection of the original figures.

## Relevance

This is the decisive comparator for a proposed sharp triangle-free spectral stability law. The exact bipartite theorem provides a substantial resolved subcase; the cut lemma and the spectral-loss step identify the additional issue in extending it. The source provides evidence for what is known, not by itself for the new formulation being open.
