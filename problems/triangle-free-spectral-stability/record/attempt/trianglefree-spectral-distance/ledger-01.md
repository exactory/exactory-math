# Move 1: losses in the published two-step argument

This is an analytical derivation for the admitted universal claim. It is not an accepted proof of that claim. No numerical process was used.

Let G be triangle-free, with m edges, adjacency radius lambda, and xi=m-lambda^2. First suppose G is connected and has an edge. Lemma 4.4 of arXiv:2609.20225v2, with booksize zero, supplies a neighbourhood cut whose b internal edges satisfy 0 <= b <= xi. Let F be the bipartite graph obtained by deleting those b edges and let E be the graph of deleted edges. Then e(F)=m-b. E is itself triangle-free, so Nosal's inequality gives ||A(E)|| <= sqrt(b). The Rayleigh variational principle gives lambda(F) >= lambda-sqrt(b).

If xi <= m/2, then lambda >= sqrt(xi) >= sqrt(b). Consequently

    e(F)-lambda(F)^2 <= xi-2b+2 lambda sqrt(b).

Lemma 4.3 of the same source and the triangle inequality for edit distance give

    D(G) <= b+3(e(F)-lambda(F)^2)
         <= 3xi-5b+6 lambda sqrt(b)
         <= 3xi+6 sqrt(m xi).

For xi > m/2, the same final upper bound holds because D(G) <= m < 3xi. Thus this derivation gives the explicit, but weaker, estimate

    D(G) <= min(m, 3xi+6 sqrt(m xi)).

For a disconnected graph, apply the argument to a component having radius lambda and delete every other component. If that component has m0 edges and deficit xi0=m0-lambda^2, then m-m0=xi-xi0. The obtained cost is at most xi-xi0+3xi0+6 sqrt(m0 xi0), hence at most 3xi+6 sqrt(m xi). The empty graph and lambda=0 cases are immediate by taking an empty target.

## Loss ledger

1. The cut deletes b <= xi edges. This is a linear loss with coefficient one.
2. Spectral perturbation gives lambda(F) >= lambda-sqrt(b). Squaring introduces 2 lambda sqrt(b), which is of order sqrt(m xi) when b is comparable with xi.
3. Bipartite editing multiplies its deficit by three. The negative terms combine to -5b and do not cancel the square-root contribution as xi/m tends to zero.

The published cube-power stability statement is not contradicted. This calculation uses the special hypothesis of zero triangles and zero booksize throughout. It is a derived estimate, not a novelty claim.

## Exact obstruction to using only the two separate estimates

For G=C5, m=5, lambda=2, xi=1. Each neighbourhood cut deletes one edge, leaving P5. The path recurrence p_k(t)=t p_{k-1}(t)-p_{k-2}(t), with p_0=1 and p_1=t, gives p_5(t)=t(t^2-1)(t^2-3), so lambda(P5)^2=3. Its four edges therefore have bipartite deficit one. The two separate bounds give 1+3(4-3)=4, exceeding the desired value 3.

In fact D(C5)=3. A two-edge path is a target K_1,2 contained in C5, giving cost three. For the lower bound, write the gain as 2e(A,B)-|A||B|. Up to exchanging parts, possible positive part sizes with |A|+|B| <= 5 are (1,1), (1,2), (1,3), (1,4), (2,2), and (2,3). Their gains are respectively at most 1,2,1,0,2,2: use maximum degree two, absence of a four-cycle for (2,2), and maximum cut size four for (2,3). Empty parts have gain zero. Thus the maximum gain is two and the minimum cost is five minus two.

This establishes a limitation of that displayed composition, not a barrier for all methods or a counterexample to the root claim. A possible next refinement is a joint functional of the chosen cut and the final complete-bipartite target, avoiding the separate worst-case constants. Perron weighting and a fourth-moment count are potential analytical routes; neither has yet supplied the missing inequality.
