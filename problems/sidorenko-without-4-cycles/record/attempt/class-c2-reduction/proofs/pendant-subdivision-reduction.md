# The statement on C_2 is equivalent to Problem 1.5 of Conlon, Kim, Lee and Lee

Node `class-c2-reduction`, move 1 (strategy reduce-and-translate, entry change-the-ambient-space). This file is the
proof for the checkpoint of milestone `c2-reduces-to-problem-1-5`. It proves an equivalence, a reduction of the
node's claim to a named open problem; it decides neither side. A draft was written during the exploration, outside
this attack root (`attempt/drafts/pendant-subdivision-reduction.md`); this version was checked against the sources
and completed in move 1, and it answers the four non-blocking objections of the admission review
(`assignment-admission-c2-fable`): the tensor power trick and its order relative to the bounded-degree reduction are
proved (Section 2), the edgeless core is handled (Proposition B), the two forms of the inequality are stated with
their citation (Section 1), and both directions of Lemma A are proved, of which the class equivalence uses one.

Sources, read in full in the common store and copied under `studies/sources/` of this attack root: Conlon, Kim, Lee and
Lee, "Some advances on Sidorenko's conjecture", arXiv:1510.06533v2 (CKLL below); Kim, Lee and Lee, "Two approaches to
Sidorenko's conjecture", arXiv:1310.4383v3 (KLL below); Coregliano and Razborov, "Biregularity in Sidorenko's
Conjecture", arXiv:2108.06599v2.

## 1. Conventions and the two forms of the inequality

All graphs are finite and simple and have at least one vertex. For graphs F and G, Hom(F, G) is the set of all maps
V(F) → V(G) that send edges to edges, including non-injective maps, and t(F, G) = |Hom(F, G)| / |V(G)|^{|V(F)|}. For a
graph G on n vertices write p(G) = 2|E(G)|/n² = t(K_2, G) and d(G) = 2|E(G)|/n, so that p(G) = d(G)/n.

A bipartite graph H is Sidorenko if t(H, G) ≥ p(G)^{|E(H)|} for every graph G. KLL state Sidorenko's conjecture in the
integral form (1.1), for every bounded, nonnegative, symmetric, measurable function on [0, 1]², and give (1.2), the
inequality above for all graphs G, as "an equivalent discrete form". The node's claim is the graphon form. The two
forms are equivalent for each bipartite H:

- graphon form ⇒ discrete form: for a graph G, the step graphon W_G (constant 1 on the squares of adjacent pairs and 0
  elsewhere, for a partition of [0, 1] into n intervals of length 1/n) satisfies t(F, W_G) = t(F, G) for every F,
  because the integral counts all maps V(F) → V(G), injective or not, with weight n^{-|V(F)|}; in particular
  t(K_2, W_G) = p(G).
- discrete form ⇒ graphon form: every graphon W is a limit in the cut distance of finite simple graphs (for example
  W-random graphs), and t(F, ·) is continuous in the cut distance (the counting lemma); see Lovász, Large networks and
  graph limits (2012). Passing to the limit in t(H, G_n) ≥ p(G_n)^{e(H)} gives t(H, W) ≥ t(K_2, W)^{e(H)}. A bounded
  nonnegative symmetric function reduces to a graphon by scaling, since both sides are homogeneous of degree e(H).

Adding or deleting an isolated vertex of H does not change t(H, G), since the count and the normalisation change by
the same factor n. Hence isolated vertices of a pattern may be added or deleted freely.

## 2. Two reductions of the host

**Tensor power trick (KLL, Lemma 3.4; Sidorenko's Remark 2).** If there is c > 0 with t(H, G) ≥ c p(G)^{|E(H)|} for
every graph G, then H is Sidorenko.

*Proof.* For graphs G_1, G_2 let G_1 × G_2 be their tensor product: vertex set V(G_1) × V(G_2), and (a, b) adjacent to
(a', b') if and only if a a' ∈ E(G_1) and b b' ∈ E(G_2). It has no loop, since G_1 has none, so it is a simple graph.
A map V(F) → V(G_1) × V(G_2) is a pair of maps, and it is a homomorphism if and only if both components are; hence
|Hom(F, G_1 × G_2)| = |Hom(F, G_1)| |Hom(F, G_2)| and t(F, G_1 × G_2) = t(F, G_1) t(F, G_2). Taking F = K_2 gives
p(G_1 × G_2) = p(G_1) p(G_2). Let G^{×k} be the k-fold tensor power. The hypothesis on G^{×k} gives
t(H, G)^k = t(H, G^{×k}) ≥ c p(G)^{k|E(H)|}, so t(H, G) ≥ c^{1/k} p(G)^{|E(H)|} for every k, and letting k → ∞ gives
t(H, G) ≥ p(G)^{|E(H)|}. ∎

**Bounded-degree reduction (CKLL, Lemma 3.3, attributed there to Fox; proof as in KLL, Lemma 3.3).** Let H be a
bipartite graph. If there is c > 0, depending only on H, with |Hom(H, G)| ≥ c |V(G)|^{|V(H)|} p(G)^{|E(H)|} for every
graph G whose maximum degree is at most 4|E(G)|/|V(G)| = 2 d(G), then H is Sidorenko.

*Proof.* By the remark on isolated vertices we may assume that H has none, so h = |V(H)| ≤ 2|E(H)| = 2m. Let G be any
graph with an edge (if G has no edge, the inequality to be proved reads t(H, G) ≥ 0). Put Δ = 2|E(G)|/|V(G)| and form
G' by taking the vertices of G one at a time in a fixed order and replacing each vertex v by t_v = ⌈deg(v)/Δ⌉
vertices v_1, …, v_{t_v}, whose neighbourhoods partition the current neighbourhood of v into parts of size at most Δ;
this can be done greedily, the degree of v is unchanged until v is replaced, and the number of edges stays |E(G)|.
The map π: V(G') → V(G), π(v_i) = v, is a homomorphism, and for adjacent v, w of G exactly one pair v' ∈ π^{-1}(v),
w' ∈ π^{-1}(w) is adjacent in G'. Hence h ↦ π ∘ h is injective on Hom(H, G') (two homomorphisms with the same image
agree on both ends of every edge, and H has no isolated vertex), so |Hom(H, G)| ≥ |Hom(H, G')|. Moreover
|V(G')| ≤ Σ_v (1 + deg(v)/Δ) = 2|V(G)|, |E(G')| = |E(G)|, and every degree of G' is at most
Δ = 2|E(G)|/|V(G)| ≤ 4|E(G')|/|V(G')|. The hypothesis applies to G', and since h − 2m ≤ 0,

  |Hom(H, G)| ≥ c |V(G')|^{h} (2|E(G')|/|V(G')|²)^{m} = c |V(G')|^{h−2m} (2|E(G)|)^{m}
             ≥ c (2|V(G)|)^{h−2m} (2|E(G)|)^{m} = c 2^{h−2m} |V(G)|^{h} p(G)^{m}.

So t(H, G) ≥ c 2^{h−2m} p(G)^m for every graph G, and the tensor power trick, applied to all graphs and not only to
those of bounded degree, shows that H is Sidorenko. ∎

The order matters: the bounded-degree hypothesis is used once, through the splitting, to obtain a lower bound with a
constant factor for every host; the tensor power trick is then applied in the class of all hosts, where it is valid.
Tensor powers need not keep the maximum degree within twice the average degree, and the argument never asks them to.

**Large subgraph of large minimum degree (CKLL, Lemma 3.4, proved there).** If G has n vertices, average degree d and
maximum degree at most 2d, then G has a subgraph G_0 with at least 2^{-6} n vertices and minimum degree at least d/4.

## 3. Lemma A (a vertex of degree one)

**Lemma A.** Let H be a bipartite graph with at least one edge, and let v be a vertex of degree one in H. Then H is
Sidorenko if and only if H − v is Sidorenko.

*Proof.* Let u be the neighbour of v. Every homomorphism φ of H − v into a graph G extends to exactly deg_G(φ(u))
homomorphisms of H into G, one for each neighbour of φ(u), and every homomorphism of H restricts to one of H − v.
Hence

  |Hom(H, G)| = Σ_{φ ∈ Hom(H − v, G)} deg_G(φ(u)).   (1)

Write h = |V(H)| and m = |E(H)| ≥ 1, so that H − v has h − 1 vertices and m − 1 edges. By the bounded-degree reduction
it suffices, in each direction, to bound the homomorphism count from below on every graph G whose maximum degree is
at most 2 d(G). Fix such a G with n vertices, d = d(G) and p = p(G). If G has no edge, then p = 0, and both lower
bounds required below hold (for m − 1 = 0 the count of H − v is n^{h−1} = n^{h−1} p^0). Assume that G has an edge, so
that d > 0.

(⇐) Assume that H − v is Sidorenko. Let G_0 be the subgraph of CKLL, Lemma 3.4, with n_0 ≥ 2^{-6} n vertices and
minimum degree at least d/4. Then |E(G_0)| ≥ n_0 d/8, so p(G_0) = 2|E(G_0)|/n_0² ≥ d/(4 n_0) ≥ d/(4n) = p/4. Every
homomorphism into G_0 is one into G, so by (1) for G_0, the minimum degree of G_0, and the Sidorenko property of
H − v in the host G_0,

  |Hom(H, G)| ≥ |Hom(H, G_0)| ≥ (d/4) |Hom(H − v, G_0)| ≥ (d/4) n_0^{h−1} p(G_0)^{m−1}
             ≥ (pn/4) (2^{-6} n)^{h−1} (p/4)^{m−1} = 4^{-m} 2^{-6(h−1)} n^{h} p^{m}.

The constant c = 4^{-m} 2^{-6(h−1)} depends only on H, so H is Sidorenko by the bounded-degree reduction.

(⇒) Assume that H is Sidorenko. By (1) and the maximum degree bound, |Hom(H, G)| ≤ 2d |Hom(H − v, G)|. Hence

  |Hom(H − v, G)| ≥ |Hom(H, G)| / (2d) ≥ n^{h} p^{m} / (2pn) = (1/2) n^{h−1} p^{m−1},

using d = pn. Since H − v is bipartite, the bounded-degree reduction with c = 1/2 shows that H − v is Sidorenko. ∎

The class equivalence below uses only the direction (⇐). The same statement in the bigraph setting is Corollary 5.3
of Coregliano and Razborov, derived there from their biregular reduction; in the symmetric setting it also follows
from their Theorem 8.2 (regular graphons suffice), whose proof is sketched. The proof above uses neither.

## 4. Proposition B (the reduction)

Let C_2 be the class of finite bipartite graphs H with at least one edge and no cycle of length four that have a
bipartition (X, Y) in which every vertex of X has degree at most two. The 1-subdivision S(F) of a graph F replaces
every edge ab of F by a path a – x_{ab} – b through a new vertex x_{ab}; this is the subdivision of CKLL ("replacing
its edges with paths of length two that are internally vertex disjoint"). CKLL, Problem 1.5: "Show that the
subdivision of an arbitrary graph H has Sidorenko's property." Graphs are simple there, and the subdivision of an
edgeless graph is edgeless and Sidorenko, so Problem 1.5 is the assertion that S(F) is Sidorenko for every simple
graph F with at least one edge.

**Proposition B.** The following are equivalent.

(i) Every graph in C_2 is Sidorenko; that is, the node's claim holds.

(ii) For every finite simple graph F with at least one edge, S(F) is Sidorenko (Problem 1.5 of CKLL).

*Proof.* (i) ⇒ (ii). Let F be a simple graph with at least one edge. S(F) is bipartite with parts
X = {x_{ab} : ab ∈ E(F)} and Y = V(F), every vertex of X has degree exactly two, and S(F) has an edge. A cycle of S(F)
alternates between X and Y, so it has length 2ℓ, where ℓ ≥ 2 is the number of its vertices in X; it passes through ℓ
distinct vertices of Y. A cycle with ℓ = 2 would consist of two distinct edges of F with the same two endpoints, which
a simple graph does not have. Hence S(F) has no cycle of length four, S(F) ∈ C_2, and S(F) is Sidorenko by (i).

(ii) ⇒ (i). Let H ∈ C_2 with a bipartition (X, Y) as in the definition. Delete from H the vertices of X of degree zero
or one, one at a time; each vertex of X keeps its degree until it is deleted, because X is an independent set, so
each deletion removes an isolated vertex or a vertex of degree one. Then delete the vertices of Y that have become
isolated. Call the result H''. By Lemma A (direction ⇐, applied in the reverse order of the deletions) and the remark
on isolated vertices, H is Sidorenko if H'' is Sidorenko, where an edgeless graph counts as Sidorenko (t = 1 = p^0).

If H'' has no edge, then it has no vertex: every vertex of X'' would have degree two, and every vertex of Y'' would have
a neighbour. This is the degenerate case: H consists of stars whose centres lie in Y and whose leaves lie in X, and
isolated vertices; it is obtained from an edgeless graph by adding isolated vertices and vertices of degree one, so it
is Sidorenko by Lemma A, without using (ii).

Otherwise H'' has an edge, every vertex of X'' = X ∩ V(H'') has degree exactly two, and H'' has no isolated vertex.
Define a multigraph F on Y'' = Y ∩ V(H'') with one edge ab for each x ∈ X'' with neighbourhood {a, b}; a ≠ b because H
is simple. Two distinct vertices x, x' of X'' with the same neighbourhood {a, b} would form the cycle x a x' b of
length four in H'' ⊆ H, which H does not have. Hence F is a simple graph with at least one edge and no isolated
vertex, and H'' is isomorphic to S(F). By (ii), H'' is Sidorenko, and therefore H is Sidorenko. ∎

## 5. What the reduction gives and what it does not

1. On the class C_2 the node's claim is exactly Problem 1.5 of CKLL: a proof of the claim proves Problem 1.5, and a
   solution of Problem 1.5 proves the claim. A counterexample inside C_2 yields, through the construction above, a
   simple graph F whose 1-subdivision is not Sidorenko, and conversely.
2. Known cases of Problem 1.5 transfer to C_2 through the construction in the proof: a graph H ∈ C_2 whose base graph F
   is a clique, a KNRS graph or a Sidorenko graph (CKLL, Theorems 1.3 and 3.1) or a regular-KNRS graph (Zhao,
   arXiv:2606.30010v1, Proposition 1.4) is Sidorenko.
3. Every graph of girth at least six with an edge that is not in C_2 has, in each of its bipartitions, a vertex of
   degree at least three on each side. The rest of the root statement, the premise outside C_2 of the case-split route,
   is untouched by this node.
4. The equivalence decides neither Problem 1.5 nor the node's claim.
