# Lean 4 formalization

Lean v4.35.0, Mathlib v4.35.0 (commit `56a005855ea17e0b0958f73ec801ae140b0a1679`).

| File | Content |
|---|---|
| `TriangleFreeEdit.lean` | The definitions and the main theorem `TriangleFreeEdit.editDistance_le_three_deficit` with its proof |
| `TriangleFreeSharpness.lean` | The five-cycle: `cycle5_equality` ($D=3\,\xi$ with $\xi=1$) and `triangleFree_constant_sharp` (every coefficient below 3 fails) |
| `Challenge.lean` | A byte-identical copy of the problem's formal statement, [`problems/triangle-free-spectral-stability/formal/Challenge.lean`](../../../problems/triangle-free-spectral-stability/formal/Challenge.lean) |
| `comparator.json` | Configuration of `lake comparator`: challenge `Challenge`, solution `TriangleFreeEdit` |
| `Audit.lean` | `#print axioms` for the three main theorems |
| `checks/` | Output of the checks listed below |

## What the definitions say

- `editCost G S T` is $|E(G)\mathbin{\triangle}E(K_{S,T})|$, where `bicliqueEdges S T` is the edge
  set of the complete bipartite graph with parts `S` and `T` on the vertex type.
- `editDistance G` is the minimum of `editCost G S T` over all pairs of disjoint finite sets
  `(S, T)`, empty sets allowed. This is $D(G)$.
- `spectralRadius G` is the largest absolute value of an eigenvalue of the real adjacency matrix,
  and `0` when there are no vertices. For an adjacency matrix this is the largest eigenvalue.
- `G.CliqueFree 3` says that `G` has no triangle.
- The vertex type is any finite type with decidable equality, so every finite simple graph is
  covered, including disconnected graphs and isolated vertices.

The main theorem states
`(editDistance G : ℝ) ≤ 3 * ((G.edgeFinset.card : ℝ) - (spectralRadius G) ^ 2)` under
`G.CliqueFree 3`.

## Build and check

```sh
lake exe cache get
lake build
lake env lean Audit.lean
lake comparator             # needs Linux with bubblewrap
lake comparator --paranoid  # also runs the external checkers bundled with Lean
```

## What we ran (25 October 2026, macOS arm64)

- `lake build`: success (9,050 jobs).
- `lake env lean Audit.lean`: each of the three theorems depends only on `propext`,
  `Classical.choice` and `Quot.sound`.
- A token scan of the three source files outside comments and strings found no `sorry` in the
  proof files and no `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe` or
  `ofReduceBool`. `Challenge.lean` contains one `sorry` by design.
- `lake comparator --paranoid --inadvisably-no-sandbox`: accepted by Lean's paranoid kernel,
  `lean4lean`, `nanoda`, `con-leche`, `con-ron` and Lean's default kernel
  ([checks/comparator-paranoid.txt](checks/comparator-paranoid.txt)). The sandbox needs
  bubblewrap, which runs only on Linux; the run checked our own files. A checker who does not
  trust these files should run `lake comparator` with the sandbox.

## Relation to the research record

The proof was written by OpenAI Codex (model `gpt-6-astra`) on 24 October 2026 and checked by the
Lean kernel; the sharpness file reuses the five-cycle proofs of the record's later formalization of
all its results. This copy differs from the record's file in one place: in `editDistance`, the
proof that the set of costs is nonempty is the named lemma `editCosts_nonempty` instead of an
inline proof term. Under Lean's module system an inline proof becomes a private lemma whose name
contains the module name, and `lake comparator` then reports that the definition differs between
the challenge and the solution. The value of `editDistance` does not depend on this proof.
