module

public import Mathlib

public section

/-!
# Edit-distance stability of Nosal's inequality, coefficient 3

Formal statement and proof of the theorem of `../paper/` (Theorem 1):

For every finite simple triangle-free graph `G` with `m` edges and adjacency spectral radius
`λ`, the minimum number of edge insertions and deletions that turn `G` into a complete
bipartite graph `K_{S,T}` (disjoint `S, T ⊆ V`, possibly empty, every other vertex isolated)
is at most `3 (m - λ^2)`.

The definitions below fix the meaning of the statement. `Challenge.lean` repeats them, and the
theorem statement, with the proof replaced by `sorry`; `lake comparator` checks that the two agree.
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

lemma editDistance_le_editCost (G : SimpleGraph V) [DecidableRel G.Adj]
    (S T : Finset V) (hST : Disjoint S T) :
    editDistance G ≤ editCost G S T := by
  apply Finset.min'_le
  apply Finset.mem_image.mpr
  exact ⟨(S, T), by simp [disjointPairs, hST], rfl⟩

@[simp] lemma editCost_empty (G : SimpleGraph V) [DecidableRel G.Adj] :
    editCost G ∅ ∅ = G.edgeFinset.card := by
  simp [editCost, bicliqueEdges, Finset.symmDiff_def]

lemma editDistance_le_card_edges (G : SimpleGraph V) [DecidableRel G.Adj] :
    editDistance G ≤ G.edgeFinset.card := by
  simpa using editDistance_le_editCost G ∅ ∅ (by simp)

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

/-- An eigenvector of an eigenvalue of maximum absolute value suffices for the proof. -/
lemma exists_spectral_vector (G : SimpleGraph V) [DecidableRel G.Adj] [Nonempty V] :
    ∃ (μ : ℝ) (x : V → ℝ), |μ| = spectralRadius G ∧
      (∑ u, x u ^ 2) = 1 ∧
      ∀ u, (∑ v ∈ G.neighborFinset u, x v) = μ * x u := by
  obtain ⟨i, _, hi⟩ := Finset.exists_mem_eq_sup' (s := (univ : Finset V))
    univ_nonempty (fun i => |(adjMatrix_isHermitian G).eigenvalues i|)
  refine ⟨(adjMatrix_isHermitian G).eigenvalues i,
    ⇑((adjMatrix_isHermitian G).eigenvectorBasis i), ?_, ?_, ?_⟩
  · simpa only [spectralRadius, dite_eq_left (inferInstance : Nonempty V)] using hi.symm
  · rw [← EuclideanSpace.real_norm_sq_eq]
    simp [(adjMatrix_isHermitian G).eigenvectorBasis.orthonormal.1 i]
  · intro u
    have h := congrFun ((adjMatrix_isHermitian G).mulVec_eigenvectorBasis i) u
    simpa only [SimpleGraph.adjMatrix_mulVec_apply, Pi.smul_apply, smul_eq_mul] using h

lemma neighborFinset_disjoint_of_adj (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) {u v : V} (huv : G.Adj u v) :
    Disjoint (G.neighborFinset u) (G.neighborFinset v) := by
  rw [Finset.disjoint_left]
  intro z hzu hzv
  have huz := (G.mem_neighborFinset u z).mp hzu
  have hvz := (G.mem_neighborFinset v z).mp hzv
  exact (G.isIndepSet_neighborSet_of_triangleFree hG u) huv huz hvz.ne hvz

lemma biclique_pair_injOn (S T : Finset V) (hST : Disjoint S T) :
    Set.InjOn (fun p : V × V => s(p.1, p.2)) (↑(S ×ˢ T) : Set (V × V)) := by
  intro p hp q hq hpq
  rcases mem_product.mp hp with ⟨hpS, hpT⟩
  rcases mem_product.mp hq with ⟨hqS, hqT⟩
  rcases Sym2.eq_iff.mp hpq with h | h
  · exact Prod.ext h.1 h.2
  · exact False.elim (Finset.disjoint_left.mp hST hpS (h.1.symm ▸ hqT))

lemma card_bicliqueEdges (S T : Finset V) (hST : Disjoint S T) :
    (bicliqueEdges S T).card = S.card * T.card := by
  rw [bicliqueEdges, card_image_of_injOn (biclique_pair_injOn S T hST), card_product]

lemma card_inter_bicliqueEdges (G : SimpleGraph V) [DecidableRel G.Adj]
    (S T : Finset V) (hST : Disjoint S T) :
    ((G.edgeFinset ∩ bicliqueEdges S T).card : ℝ) =
      ∑ a ∈ S, ∑ b ∈ T, G.adjMatrix ℝ a b := by
  have heq : G.edgeFinset ∩ bicliqueEdges S T =
      ((S ×ˢ T).filter (fun p => G.Adj p.1 p.2)).image (fun p => s(p.1, p.2)) := by
    calc
      _ = (bicliqueEdges S T).filter (fun e => e ∈ G.edgeFinset) := by
        ext e
        simp [and_comm]
      _ = _ := by
        simp only [bicliqueEdges, filter_image, SimpleGraph.mem_edgeFinset,
          SimpleGraph.mem_edgeSet]
  rw [heq, card_image_of_injOn ((biclique_pair_injOn S T hST).mono
    (by intro p hp; exact (mem_filter.mp hp).1))]
  calc
    _ = ∑ p ∈ S ×ˢ T, if G.Adj p.1 p.2 then (1 : ℝ) else 0 :=
      (Finset.sum_boole _ _).symm
    _ = _ := by rw [Finset.sum_product]; rfl

lemma card_symmDiff_real {α : Type*} [DecidableEq α] (S T : Finset α) :
    ((symmDiff S T).card : ℝ) = S.card + T.card - 2 * (S ∩ T).card := by
  have hd : Disjoint (S \ T) (T \ S) := by
    rw [disjoint_left]
    intro a ha hb
    exact (mem_sdiff.mp ha).2 (mem_sdiff.mp hb).1
  have hS : ((S \ T).card : ℝ) + (S ∩ T).card = S.card := by
    exact_mod_cast card_sdiff_add_card_inter S T
  have hT : ((T \ S).card : ℝ) + (S ∩ T).card = T.card := by
    exact_mod_cast (by simpa [inter_comm] using card_sdiff_add_card_inter T S)
  rw [Finset.symmDiff_def, card_union_of_disjoint hd, Nat.cast_add]
  linarith

lemma editCost_eq (G : SimpleGraph V) [DecidableRel G.Adj]
    (S T : Finset V) (hST : Disjoint S T) :
    (editCost G S T : ℝ) = (G.edgeFinset.card : ℝ) + (S.card : ℝ) * T.card -
      2 * ∑ a ∈ S, ∑ b ∈ T, G.adjMatrix ℝ a b := by
  rw [editCost, card_symmDiff_real, card_bicliqueEdges S T hST, Nat.cast_mul,
    card_inter_bicliqueEdges G S T hST]

/-- Multiplication by the adjacency matrix, written as a neighbourhood sum. -/
noncomputable def neighborSum (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : V → ℝ) (u : V) : ℝ := ∑ v ∈ G.neighborFinset u, f v

/-- The number of common neighbours, regarded as a real number. -/
noncomputable def codegree (G : SimpleGraph V) [DecidableRel G.Adj] (u z : V) : ℝ :=
  neighborSum G (fun v => G.adjMatrix ℝ v z) u

lemma editCost_neighbors (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) {u v : V} (huv : G.Adj u v) :
    (editCost G (G.neighborFinset u) (G.neighborFinset v) : ℝ) =
      (G.edgeFinset.card : ℝ) + (G.degree u : ℝ) * G.degree v -
        2 * neighborSum G (codegree G u) v := by
  rw [editCost_eq G _ _ (neighborFinset_disjoint_of_adj G hG huv)]
  simp only [SimpleGraph.card_neighborFinset_eq_degree]
  have hs : (∑ a ∈ G.neighborFinset u, ∑ b ∈ G.neighborFinset v,
      G.adjMatrix ℝ a b) = neighborSum G (codegree G u) v := by
    simp only [neighborSum, codegree]
    exact Finset.sum_comm
  rw [hs]

lemma neighborSum_eq_sum (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : V → ℝ) (u : V) :
    neighborSum G f u = ∑ v, G.adjMatrix ℝ u v * f v := by
  exact (G.adjMatrix_dotProduct u f).symm

lemma neighborSum_twice (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : V → ℝ) (u : V) :
    neighborSum G (neighborSum G f) u = ∑ z, codegree G u z * f z := by
  simp only [neighborSum_eq_sum, codegree, Finset.mul_sum, Finset.sum_mul, mul_assoc]
  exact Finset.sum_comm

lemma sum_editCost_neighbors (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    neighborSum G (fun v => (editCost G (G.neighborFinset u) (G.neighborFinset v) : ℝ)) u =
      (G.degree u : ℝ) * G.edgeFinset.card +
        (G.degree u : ℝ) * neighborSum G (fun v => (G.degree v : ℝ)) u -
        2 * ∑ z, codegree G u z ^ 2 := by
  have hcost : (∑ v ∈ G.neighborFinset u,
      (editCost G (G.neighborFinset u) (G.neighborFinset v) : ℝ)) =
      ∑ v ∈ G.neighborFinset u, ((G.edgeFinset.card : ℝ) +
        (G.degree u : ℝ) * G.degree v - 2 * neighborSum G (codegree G u) v) := by
    apply Finset.sum_congr rfl
    intro v hv
    exact editCost_neighbors G hG ((G.mem_neighborFinset u v).mp hv)
  change (∑ v ∈ G.neighborFinset u, _) = _
  rw [hcost]
  simp only [sum_sub_distrib, sum_add_distrib, sum_const, nsmul_eq_mul,
    SimpleGraph.card_neighborFinset_eq_degree, ← Finset.mul_sum]
  change _ - 2 * neighborSum G (neighborSum G (codegree G u)) u = _
  rw [neighborSum_twice]
  simp only [sq, neighborSum]

lemma degree_mul_editDistance_le (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    (G.degree u : ℝ) * editDistance G ≤
      (G.degree u : ℝ) * G.edgeFinset.card +
        (G.degree u : ℝ) * neighborSum G (fun v => (G.degree v : ℝ)) u -
        2 * ∑ z, codegree G u z ^ 2 := by
  rw [← sum_editCost_neighbors G hG u]
  have h := Finset.sum_le_sum (s := G.neighborFinset u)
    (f := fun _ => (editDistance G : ℝ))
    (g := fun v => (editCost G (G.neighborFinset u) (G.neighborFinset v) : ℝ))
    (fun v hv => (by
      exact_mod_cast editDistance_le_editCost G _ _
        (neighborFinset_disjoint_of_adj G hG ((G.mem_neighborFinset u v).mp hv))))
  simpa only [sum_const, nsmul_eq_mul, SimpleGraph.card_neighborFinset_eq_degree,
    neighborSum] using h

lemma adj_entry_symm (G : SimpleGraph V) [DecidableRel G.Adj] (u v : V) :
    G.adjMatrix ℝ u v = G.adjMatrix ℝ v u := by
  simp only [SimpleGraph.adjMatrix_apply, G.adj_comm]

lemma sum_adj_eq_degree (G : SimpleGraph V) [DecidableRel G.Adj] (u : V) :
    (∑ v, G.adjMatrix ℝ u v) = (G.degree u : ℝ) := by
  simpa [neighborSum] using (neighborSum_eq_sum G (fun _ => 1) u).symm

lemma codegree_eq_zero_of_adj (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) {u z : V} (huz : G.Adj u z) : codegree G u z = 0 := by
  unfold codegree neighborSum
  apply Finset.sum_eq_zero
  intro v hv
  have hvz : ¬ G.Adj v z := by
    intro hvz
    exact Finset.disjoint_left.mp (neighborFinset_disjoint_of_adj G hG huz)
      hv ((G.mem_neighborFinset z v).mpr hvz.symm)
  simp [SimpleGraph.adjMatrix_apply, hvz]

lemma codegree_add_le_degree (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) {z w : V} (hzw : G.Adj z w) :
    codegree G u z + codegree G u w ≤ (G.degree u : ℝ) := by
  have hd := neighborFinset_disjoint_of_adj G hG hzw
  calc
    _ = ∑ a ∈ G.neighborFinset u, (G.adjMatrix ℝ a z + G.adjMatrix ℝ a w) := by
      simp only [codegree, neighborSum, sum_add_distrib]
    _ ≤ ∑ _a ∈ G.neighborFinset u, (1 : ℝ) := by
      apply Finset.sum_le_sum
      intro a _
      have hn : ¬ (G.Adj a z ∧ G.Adj a w) := by
        rintro ⟨haz, haw⟩
        exact Finset.disjoint_left.mp hd ((G.mem_neighborFinset z a).mpr haz.symm)
          ((G.mem_neighborFinset w a).mpr haw.symm)
      by_cases haz : G.Adj a z <;> by_cases haw : G.Adj a w <;>
        simp_all [SimpleGraph.adjMatrix_apply]
    _ = _ := by simp

lemma adj_triangle_mul_eq_zero (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u z w : V) :
    G.adjMatrix ℝ u z * G.adjMatrix ℝ u w * G.adjMatrix ℝ z w = 0 := by
  by_cases huz : G.Adj u z
  · by_cases huw : G.Adj u w
    · have hzw : ¬ G.Adj z w := fun h =>
        (G.isIndepSet_neighborSet_of_triangleFree hG u) huz huw h.ne h
      simp [SimpleGraph.adjMatrix_apply, hzw]
    · simp [SimpleGraph.adjMatrix_apply, huw]
  · simp [SimpleGraph.adjMatrix_apply, huz]

/-- Indicator of an oriented edge whose two endpoints lie outside `N(u)`. -/
noncomputable def residualWeight (G : SimpleGraph V) [DecidableRel G.Adj]
    (u z w : V) : ℝ :=
  G.adjMatrix ℝ z w * (1 - G.adjMatrix ℝ u z) * (1 - G.adjMatrix ℝ u w)

lemma sum_residualWeight (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    (∑ z, ∑ w, residualWeight G u z w) =
      2 * ((G.edgeFinset.card : ℝ) - neighborSum G (fun v => (G.degree v : ℝ)) u) := by
  have hentry (z w : V) : residualWeight G u z w =
      G.adjMatrix ℝ z w - G.adjMatrix ℝ u z * G.adjMatrix ℝ z w -
        G.adjMatrix ℝ u w * G.adjMatrix ℝ z w := by
    unfold residualWeight
    linear_combination adj_triangle_mul_eq_zero G hG u z w
  have hcol (w : V) : (∑ z, G.adjMatrix ℝ z w) = (G.degree w : ℝ) := by
    calc
      _ = ∑ z, G.adjMatrix ℝ w z := Finset.sum_congr rfl (fun z _ => adj_entry_symm G z w)
      _ = _ := sum_adj_eq_degree G w
  have hleft : (∑ z, ∑ w, G.adjMatrix ℝ u z * G.adjMatrix ℝ z w) =
      neighborSum G (fun v => (G.degree v : ℝ)) u := by
    simp only [← Finset.mul_sum, sum_adj_eq_degree, neighborSum_eq_sum]
  have hright : (∑ z, ∑ w, G.adjMatrix ℝ u w * G.adjMatrix ℝ z w) =
      neighborSum G (fun v => (G.degree v : ℝ)) u := by
    rw [Finset.sum_comm]
    simp only [← Finset.mul_sum, hcol, neighborSum_eq_sum]
  have htotal : (∑ z, (G.degree z : ℝ)) = 2 * (G.edgeFinset.card : ℝ) := by
    exact_mod_cast G.sum_degrees_eq_twice_card_edges
  simp_rw [hentry, sum_sub_distrib]
  rw [hleft, hright]
  simp only [sum_adj_eq_degree, htotal]
  ring

lemma codegree_defect_eq (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    neighborSum G (neighborSum G (fun v => (G.degree v : ℝ))) u -
        (∑ z, codegree G u z ^ 2) =
      ∑ z, ∑ w, residualWeight G u z w * codegree G u z := by
  rw [neighborSum_twice, ← sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro z _
  have hc : codegree G u z = ∑ w, G.adjMatrix ℝ z w * G.adjMatrix ℝ u w := by
    rw [codegree, neighborSum_eq_sum]
    apply Finset.sum_congr rfl
    intro w _
    rw [adj_entry_symm G w z]
    ring
  have hcut : (∑ w, G.adjMatrix ℝ z w * (1 - G.adjMatrix ℝ u w)) =
      (G.degree z : ℝ) - codegree G u z := by
    simp only [mul_sub, mul_one, sum_sub_distrib, sum_adj_eq_degree, ← hc]
  have hk : (1 - G.adjMatrix ℝ u z) * codegree G u z = codegree G u z := by
    by_cases huz : G.Adj u z
    · rw [codegree_eq_zero_of_adj G hG huz]
      ring
    · simp [SimpleGraph.adjMatrix_apply, huz]
  calc
    codegree G u z * (G.degree z : ℝ) - codegree G u z ^ 2 =
        codegree G u z * (∑ w, G.adjMatrix ℝ z w * (1 - G.adjMatrix ℝ u w)) := by
      rw [hcut]
      ring
    _ = _ := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro w _
      unfold residualWeight
      calc
        _ = G.adjMatrix ℝ z w * (1 - G.adjMatrix ℝ u w) *
            ((1 - G.adjMatrix ℝ u z) * codegree G u z) := by rw [hk]; ring
        _ = _ := by ring

/-- Lemma 1 of the informal proof, without introducing a separate `Z_u`. -/
lemma codegree_defect_le (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    neighborSum G (neighborSum G (fun v => (G.degree v : ℝ))) u -
        (∑ z, codegree G u z ^ 2) ≤
      (G.degree u : ℝ) *
        ((G.edgeFinset.card : ℝ) - neighborSum G (fun v => (G.degree v : ℝ)) u) := by
  rw [codegree_defect_eq G hG u]
  have hswap : (∑ z, ∑ w, residualWeight G u z w * codegree G u w) =
      ∑ z, ∑ w, residualWeight G u z w * codegree G u z := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro z _
    apply Finset.sum_congr rfl
    intro w _
    unfold residualWeight
    rw [adj_entry_symm G w z]
    ring
  have htwice : 2 * (∑ z, ∑ w, residualWeight G u z w * codegree G u z) =
      ∑ z, ∑ w, residualWeight G u z w * (codegree G u z + codegree G u w) := by
    simp only [mul_add, sum_add_distrib]
    rw [hswap]
    ring
  have hb : (∑ z, ∑ w, residualWeight G u z w * (codegree G u z + codegree G u w)) ≤
      ∑ z, ∑ w, residualWeight G u z w * (G.degree u : ℝ) := by
    apply Finset.sum_le_sum
    intro z _
    apply Finset.sum_le_sum
    intro w _
    by_cases hzw : G.Adj z w
    · have hr : 0 ≤ residualWeight G u z w := by
        unfold residualWeight
        simp only [SimpleGraph.adjMatrix_apply]
        split_ifs <;> norm_num
      exact mul_le_mul_of_nonneg_left (codegree_add_le_degree G hG u hzw) hr
    · simp [residualWeight, SimpleGraph.adjMatrix_apply, hzw]
  simp only [← Finset.sum_mul] at hb
  rw [sum_residualWeight G hG u, ← htwice] at hb
  nlinarith only [hb]

lemma neighborSum_self_adjoint (G : SimpleGraph V) [DecidableRel G.Adj]
    (f g : V → ℝ) :
    (∑ u, f u * neighborSum G g u) = ∑ u, g u * neighborSum G f u := by
  simp only [neighborSum_eq_sum, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro u _
  apply Finset.sum_congr rfl
  intro v _
  rw [adj_entry_symm G v u]
  ring

/-- Uniform-weight Cauchy–Schwarz, inequality (4) of the informal proof. -/
lemma energy_le_degreeSum (G : SimpleGraph V) [DecidableRel G.Adj] (y : V → ℝ) :
    (∑ v, neighborSum G y v ^ 2) ≤
      ∑ u, y u ^ 2 * neighborSum G (fun v => (G.degree v : ℝ)) u := by
  calc
    _ ≤ ∑ v, (G.degree v : ℝ) * neighborSum G (fun u => y u ^ 2) v := by
      apply Finset.sum_le_sum
      intro v _
      simpa only [neighborSum, SimpleGraph.card_neighborFinset_eq_degree] using
        (sq_sum_le_card_mul_sum_sq (s := G.neighborFinset v) (f := y))
    _ = _ := neighborSum_self_adjoint G (fun v => (G.degree v : ℝ)) (fun u => y u ^ 2)

/-- Degree-weight Cauchy–Schwarz. Neighbours always have positive degree, so isolated
vertices cause no division issue in the pointwise inequality. -/
lemma energy_le_weighted_degreeSum (G : SimpleGraph V) [DecidableRel G.Adj] (y : V → ℝ) :
    (∑ v, neighborSum G y v ^ 2) ≤
      ∑ u, (y u ^ 2 / (G.degree u : ℝ)) *
        neighborSum G (neighborSum G (fun v => (G.degree v : ℝ))) u := by
  have hpoint (v : V) : neighborSum G y v ^ 2 ≤
      neighborSum G (fun u => (G.degree u : ℝ)) v *
        neighborSum G (fun u => y u ^ 2 / (G.degree u : ℝ)) v := by
    unfold neighborSum
    refine Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul _ ?_ ?_ ?_
    · intro u _
      exact Nat.cast_nonneg _
    · intro u _
      exact div_nonneg (sq_nonneg _) (Nat.cast_nonneg _)
    · intro u hu
      have hdu : (G.degree u : ℝ) ≠ 0 := by
        exact_mod_cast (ne_of_gt (((G.mem_neighborFinset v u).mp hu).degree_pos_right))
      rw [mul_comm (G.degree u : ℝ), div_mul_cancel₀ _ hdu]
  calc
    _ ≤ ∑ v, neighborSum G (fun u => (G.degree u : ℝ)) v *
        neighborSum G (fun u => y u ^ 2 / (G.degree u : ℝ)) v :=
      Finset.sum_le_sum (fun v _ => hpoint v)
    _ = _ := neighborSum_self_adjoint G (neighborSum G (fun u => (G.degree u : ℝ)))
      (fun u => y u ^ 2 / (G.degree u : ℝ))

lemma local_degree_bound (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (u : V) :
    2 * neighborSum G (neighborSum G (fun v => (G.degree v : ℝ))) u +
        (G.degree u : ℝ) * editDistance G ≤
      (G.degree u : ℝ) *
        (3 * (G.edgeFinset.card : ℝ) - neighborSum G (fun v => (G.degree v : ℝ)) u) := by
  nlinarith only [codegree_defect_le G hG u, degree_mul_editDistance_le G hG u]

lemma weighted_local_bound (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (x : V → ℝ)
    (hx : ∀ u, G.degree u = 0 → x u = 0) (u : V) :
    2 * (x u ^ 2 / (G.degree u : ℝ)) *
        neighborSum G (neighborSum G (fun v => (G.degree v : ℝ))) u +
      x u ^ 2 * (editDistance G : ℝ) +
      x u ^ 2 * neighborSum G (fun v => (G.degree v : ℝ)) u ≤
      3 * (G.edgeFinset.card : ℝ) * x u ^ 2 := by
  by_cases hd : G.degree u = 0
  · simp [hx u hd]
  · have hd' : (G.degree u : ℝ) ≠ 0 := by exact_mod_cast hd
    have h := mul_le_mul_of_nonneg_left (local_degree_bound G hG u)
      (div_nonneg (sq_nonneg (x u)) (Nat.cast_nonneg (G.degree u)))
    simp only [mul_add, ← mul_assoc, div_mul_cancel₀ _ hd'] at h
    nlinarith only [h]

lemma editDistance_add_three_energy_le (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) (x : V → ℝ) (hnorm : (∑ u, x u ^ 2) = 1)
    (hx : ∀ u, G.degree u = 0 → x u = 0) :
    (editDistance G : ℝ) + 3 * (∑ v, neighborSum G x v ^ 2) ≤
      3 * (G.edgeFinset.card : ℝ) := by
  have hsum := Finset.sum_le_sum (s := (univ : Finset V))
    (fun u _ => weighted_local_bound G hG x hx u)
  simp only [sum_add_distrib, mul_assoc, ← Finset.mul_sum, ← Finset.sum_mul,
    hnorm, mul_one, one_mul] at hsum
  linarith only [hsum, energy_le_degreeSum G x, energy_le_weighted_degreeSum G x]

lemma eigenvector_zero_of_degree_zero (G : SimpleGraph V) [DecidableRel G.Adj]
    (μ : ℝ) (hμ : μ ≠ 0) (x : V → ℝ)
    (heig : ∀ u, neighborSum G x u = μ * x u) {u : V} (hu : G.degree u = 0) :
    x u = 0 := by
  have hN : G.neighborFinset u = ∅ := Finset.card_eq_zero.mp
    (by simpa only [SimpleGraph.card_neighborFinset_eq_degree] using hu)
  have h := heig u
  rw [neighborSum, hN, Finset.sum_empty] at h
  exact (mul_eq_zero.mp h.symm).resolve_left hμ

lemma eigenvector_energy (G : SimpleGraph V) [DecidableRel G.Adj]
    (μ : ℝ) (x : V → ℝ) (hnorm : (∑ u, x u ^ 2) = 1)
    (heig : ∀ u, neighborSum G x u = μ * x u) :
    (∑ v, neighborSum G x v ^ 2) = μ ^ 2 := by
  simp only [heig, mul_pow, ← Finset.mul_sum, hnorm, mul_one]

/-- The theorem of `PROOF.md`: `D(G) ≤ 3 (m - λ^2)` for every finite simple triangle-free
graph. `G.CliqueFree 3` is the absence of triangles. -/
theorem editDistance_le_three_deficit (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG : G.CliqueFree 3) :
    (editDistance G : ℝ) ≤ 3 * ((G.edgeFinset.card : ℝ) - (spectralRadius G) ^ 2) := by
  by_cases hr : spectralRadius G = 0
  · have hD : (editDistance G : ℝ) ≤ (G.edgeFinset.card : ℝ) := by
      exact_mod_cast editDistance_le_card_edges G
    rw [hr]
    nlinarith only [hD, Nat.cast_nonneg (α := ℝ) G.edgeFinset.card]
  have hV : Nonempty V := by
    by_contra hV
    exact hr (by simp [spectralRadius, hV])
  let : Nonempty V := hV
  obtain ⟨μ, x, habs, hnorm, heig⟩ := exists_spectral_vector G
  have hμ : μ ≠ 0 := by
    intro hμ
    apply hr
    rw [← habs, hμ, abs_zero]
  have hx : ∀ u, G.degree u = 0 → x u = 0 := fun u hu =>
    eigenvector_zero_of_degree_zero G μ hμ x heig hu
  have h := editDistance_add_three_energy_le G hG x hnorm hx
  rw [eigenvector_energy G μ x hnorm heig] at h
  have hsq : μ ^ 2 = spectralRadius G ^ 2 := by
    simpa only [habs] using (sq_abs μ).symm
  rw [hsq] at h
  linarith only [h]

end TriangleFreeEdit
