# Formal statement (Lean 4)

[`Challenge.lean`](Challenge.lean) states the problem in Lean 4 with Mathlib. Its theorem
`TriangleFreeEdit.editDistance_le_three_deficit` has the proof `sorry`; a solution proves the same
theorem with the same definitions. Lean v4.35.0, Mathlib v4.35.0.

## What it says

- `editCost G S T` is $|E(G)\mathbin{\triangle}E(K_{S,T})|$, where `bicliqueEdges S T` is the edge
  set of the complete bipartite graph with parts `S` and `T` on the vertex type.
- `editDistance G` is the minimum of `editCost G S T` over all pairs of disjoint finite sets
  `(S, T)`, empty sets allowed. This is $D(G)$ of the problem.
- `spectralRadius G` is the largest absolute value of an eigenvalue of the real adjacency matrix,
  and `0` when there are no vertices. For an adjacency matrix this equals the largest eigenvalue
  $\lambda(G)$.
- `G.CliqueFree 3` says that `G` has no triangle. The vertex type is any finite type with
  decidable equality, so disconnected graphs and isolated vertices are included.
- The theorem: `(editDistance G : ℝ) ≤ 3 * ((G.edgeFinset.card : ℝ) - (spectralRadius G) ^ 2)`.

## Checking a solution

1. Put the solution in this folder as `Solution.lean`. It must state the theorem in the namespace
   `TriangleFreeEdit` with these definitions unchanged, and prove it.
2. Uncomment the `Solution` library in `lakefile.toml`.
3. Run `lake exe cache get` and then `lake comparator` (Linux with bubblewrap). The file
   [`comparator.json`](comparator.json) names the theorem and the permitted axioms (`propext`,
   `Quot.sound`, `Classical.choice`).

Write the definitions exactly as here, including `by exact editCosts_nonempty G` in
`editDistance`. Under Lean's module system an inline proof in a definition becomes a private
lemma whose name contains the module name, and `lake comparator` would then report that the
definitions differ.

A solution that passes this check is
[`attempts/triangle-free-spectral-stability/lean/`](../../../attempts/triangle-free-spectral-stability/lean/).
