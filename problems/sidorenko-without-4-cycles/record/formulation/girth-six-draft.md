# Draft formulation: Sidorenko's inequality for bipartite graphs without 4-cycles

Status: working draft, not recorded. It waits for the two blind problem bars and the slate. Nothing here is a
claim of the record until a statement record, an attempt and an openness finding support it.

## Statement (draft)

Let $H$ be a finite bipartite graph with at least one edge and no cycle of length four, that is, of girth at
least six. Is it true that
$$t(H,W) \ge t(K_2,W)^{e(H)}$$
for every graphon $W$?

Here $t(F,W)=\int_{[0,1]^{V(F)}}\prod_{uv\in E(F)}W(x_u,x_v)\,dx$ is the homomorphism density.

## Resolution criteria (draft)

A positive resolution proves the inequality for every bipartite graph of girth at least six and every graphon
(equivalently, for every finite host graph $G$, $t(H,G) \ge t(K_2,G)^{e(H)}$, by the standard
graphon-to-graph sampling argument; the record must cite or prove this equivalence if it uses it).

A negative resolution exhibits a bipartite graph $H$ of girth at least six and a graphon $W$ (or a finite host
graph $G$) with $t(H,W) < t(K_2,W)^{e(H)}$, with a complete proof of the strict inequality.

## Neighbours to declare

1. The 1-subdivision of every graph (Conlon, Kim, Lee and Lee 2018, Problem 1.5). A positive answer to the
   statement answers it positively. The 1-subdivision of the 35-vertex counterexample $H_0$ is a girth-8
   instance with 101 vertices and 132 edges, and $t(S(H_0),W)=t(H_0,W\circ W)$.
2. Whether some girth $g$ makes every bipartite graph of girth at least $g$ Sidorenko (a weakening).
3. Vertex-edge incidence graphs of linear $k$-uniform hypergraphs, $k \ge 3$ (the class that contains the
   incidence graphs of partial linear spaces; the counterexample is a non-linear 3-uniform instance).
4. The Heawood graph (incidence graph of the Fano plane), the smallest cubic graph of girth six. Its status must be
   settled by the openness search before it is declared open or known.
5. The forcing analogue for bipartite graphs of girth at least six that contain a cycle.

## Points to settle before formulation

- Whether any known theorem already gives Sidorenko for a girth class (search: girth, C4-free, linear
  hypergraph incidence, Heawood, subdivision; arXiv after 2026-09-23 and the openai/math catalogue).
- The exact relation between this statement and CKLL Problem 1.5, established by proof in the record (the
  subdivision of a simple graph has girth at least six, so the implication is immediate; state it).
- The strongest objection: a restriction of a false conjecture to a class. The answer to argue: the class is
  where the only known mechanism produces no correction term (pairs of points in two faces are 4-cycles of the
  incidence graph), so either answer says whether 4-cycles are needed for a failure. This is a reasoned
  judgment from the construction, and a different mechanism could still exist.
