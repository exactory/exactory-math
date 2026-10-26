# Edge Spectral

## Problem

Extend the Erdos-Stone-Simonovits theorem and its stability to adjacency spectral radius measured against the number of edges, then apply the method to common-neighbour counts.

## Claims

Theorem 1.2 gives the asymptotic edge-spectral bound for fixed F of chromatic number r+1. Theorem 1.6 gives edit stability to a complete bipartite graph for r=2 and to a balanced complete r-partite graph on a subset for r>=3. Theorem 4.1 handles triangle-free graphs: lambda>=(1-delta)sqrt(m) implies edit distance at most epsilon*m; the proof chooses delta=epsilon^36/4. Lemma 4.2 obtains a bipartite subgraph after deleting at most epsilon*m edges under lambda>=(1-epsilon/2)sqrt(m). Lemma 4.4 treats bipartite graphs with delta=epsilon^4/100. The final section proves an asymptotically sharp common-neighbour bound above the Nosal threshold.

## Assumptions

Finite simple graphs, fixed forbidden F with chromatic number at least three, and asymptotically large edge count for the general theorem. The triangle-free stability theorem states epsilon in (0,0.01). The target for r=2 permits arbitrary part sizes and isolated vertices; higher-clique targets use a balanced Turan graph on a subset.

## Methods

Spectral and weighted clique inequalities, Perron-vector estimates, graph removal, a bipartite approximation, and stability reductions. The appendix offers a second proof for larger forbidden cliques via clique counts and a Kruskal-Katona type hypergraph stability theorem. The common-neighbour bound uses Cauchy-Schwarz and Rayleigh estimates, with a random construction for the leading constant.

## Evidence

Read the complete captured HTML extraction, including all five main sections, all 56 bibliography entries and Appendix A. Read the proof of the triangle case, the bipartite lemma, the larger-clique and general-F reductions, and both common-neighbour arguments. Cross-checked Theorem 4.1, Lemma 4.2 and the epsilon^36 proof in rendered native PDF pages 12 and 15.

## Limitations

The triangle-free edit-distance conclusion is qualitative with an explicit but weak power dependence. Its linear edge-deletion bound only makes the graph bipartite, which is a different target from one complete bipartite graph. It does not give the proposed linear edit-distance law. The appendix depends on an external hypergraph stability theorem, and no independent reproof of every cited theorem is claimed.

## Relevance

This fixes the existing triangle-free theorem and distinguishes bipartite deletion from complete-bipartite edit distance. A universal linear bound would improve the deficit dependence and provide an explicit law rather than another ordinary extremal value. The source also records use of edge-spectral stability in a companion color-critical extremal theorem, without establishing that every quantitative sharpening transfers automatically.
