module

public import Mathlib

public section

/-!
# Edit-distance stability of Nosal's inequality, coefficient 3

Formal statement of the problem (the challenge; its proof is `sorry`):

For every finite simple triangle-free graph `G` with `m` edges and adjacency spectral radius
`λ`, the minimum number of edge insertions and deletions that turn `G` into a complete
bipartite graph `K_{S,T}` (disjoint `S, T ⊆ V`, possibly empty, every other vertex isolated)
is at most `3 (m - λ^2)`.

The definitions below fix the meaning of the statement. A solution states the same theorem
with these definitions unchanged; `lake comparator` checks that it does.
-/

open Finset Matrix BigOperators
open scoped Classical

set_option linter.unusedSectionVars false
set_option linter.unusedVariables false

namespace TriangleFreeEdit

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The edge set of the complete bipartite graph with parts `S` and `T`, as unordered pairs.
When `S` and `T` are disjoint no pair is a loop. -/
def bicliqueEdges (S T : Finset V) : Finset (Sym2 V) :=
  (S ×ˢ T).image (fun p => s(p.1, p.2))

/-- The cost of editing `G` into `K_{S,T}` on the vertex set `V`: the size of the symmetric
difference of the two edge sets. -/
def editCost (G : SimpleGraph V) [DecidableRel G.Adj] (S T : Finset V) : ℕ :=
  (symmDiff G.edgeFinset (bicliqueEdges S T)).card

/-- The pairs of disjoint parts; nonempty because `(∅, ∅)` is one of them. -/
def disjointPairs (V : Type*) [Fintype V] [DecidableEq V] : Finset (Finset V × Finset V) :=
  (Finset.univ : Finset (Finset V × Finset V)).filter (fun p => Disjoint p.1 p.2)

lemma disjointPairs_nonempty : (disjointPairs V).Nonempty :=
  ⟨(∅, ∅), by simp [disjointPairs]⟩

/-- The edit costs over all pairs of disjoint parts form a nonempty set. A named lemma, so that the
body of `editDistance` refers to it directly instead of to an automatically generated private
proof whose name depends on the module; `lake comparator` can then match the definition. -/
lemma editCosts_nonempty (G : SimpleGraph V) [DecidableRel G.Adj] :
    ((disjointPairs V).image (fun p => editCost G p.1 p.2)).Nonempty :=
  Finset.Nonempty.image disjointPairs_nonempty _

/-- `D(G)`: the minimum edit cost over all pairs of disjoint parts, empty parts allowed. -/
noncomputable def editDistance (G : SimpleGraph V) [DecidableRel G.Adj] : ℕ :=
  ((disjointPairs V).image (fun p => editCost G p.1 p.2)).min' (by exact editCosts_nonempty G)

/-- The adjacency matrix over `ℝ` is Hermitian (real symmetric). -/
lemma adjMatrix_isHermitian (G : SimpleGraph V) [DecidableRel G.Adj] :
    (G.adjMatrix ℝ).IsHermitian := by
  exact Matrix.isHermitian_iff_isSymm.mpr (G.isSymm_adjMatrix)

/-- The spectral radius of `G`: the largest absolute value of an eigenvalue of its adjacency
matrix over `ℝ`; `0` when `V` is empty. -/
noncomputable def spectralRadius (G : SimpleGraph V) [DecidableRel G.Adj] : ℝ :=
  if h : Nonempty V then
    (Finset.univ : Finset V).sup' Finset.univ_nonempty
      (fun i => |(adjMatrix_isHermitian G).eigenvalues i|)
  else 0

/-- The claim of the problem: `D(G) ≤ 3 (m - λ^2)` for every finite simple triangle-free graph.
`G.CliqueFree 3` is the absence of triangles. -/
theorem editDistance_le_three_deficit (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) :
    (editDistance G : ℝ) ≤ 3 * ((G.edgeFinset.card : ℝ) - (spectralRadius G) ^ 2) := by
  sorry

end TriangleFreeEdit
