module

public import TriangleFreeEdit

-- The definitions of `TriangleFreeEdit` have unexposed bodies under the module system;
-- `decide` on the five-cycle needs them.
import all TriangleFreeEdit

public section

/-!
# The coefficient 3 cannot be lowered

The five-cycle `C₅` is triangle-free, has 5 edges, spectral radius 2 and edit distance 3. Hence
`D(C₅) = 3 (e(C₅) - λ(C₅)²)` with deficit `e(C₅) - λ(C₅)² = 1 > 0`, and no coefficient below 3
bounds `D` by a multiple of the deficit for every finite triangle-free graph.

The spectral radius of `C₅` is computed from a positive eigenvector: if `A y = μ y` with `y > 0`,
then every eigenvalue `ν` of `A` satisfies `|ν| ≤ μ` (compare an eigenvector of `ν` with `y` at an
index that maximises `|w v| / y v`).
-/

open Finset BigOperators TriangleFreeEdit
open scoped Classical

namespace TriangleFreeSharpness

variable {V : Type*} [Fintype V] [DecidableEq V]

private lemma abs_eigenvalue_le_radius (G : SimpleGraph V) [DecidableRel G.Adj]
    [Nonempty V] (μ : ℝ)
    (hμ : Module.End.HasEigenvalue (G.adjMatrix ℝ).toEuclideanLin μ) :
    |μ| ≤ spectralRadius G := by
  have hm : μ ∈ spectrum ℝ (G.adjMatrix ℝ) := by
    rw [← Matrix.spectrum_toLpLin (A := G.adjMatrix ℝ) 2]
    exact hμ.mem_spectrum
  rw [(adjMatrix_isHermitian G).spectrum_real_eq_range_eigenvalues] at hm
  obtain ⟨i, rfl⟩ := hm
  simpa only [TriangleFreeEdit.spectralRadius, dite_eq_left (inferInstance : Nonempty V)] using
    (Finset.le_sup' (fun i => |(adjMatrix_isHermitian G).eigenvalues i|)
      (Finset.mem_univ i))

private lemma hasEigenvalue_of_neighbor_sum (G : SimpleGraph V) [DecidableRel G.Adj]
    (x : V → ℝ) (hx : ∃ v, x v ≠ 0) (μ : ℝ)
    (hμ : ∀ v, ∑ w ∈ G.neighborFinset v, x w = μ * x v) :
    Module.End.HasEigenvalue (G.adjMatrix ℝ).toEuclideanLin μ := by
  apply Module.End.hasEigenvalue_of_hasEigenvector
    (x := WithLp.toLp 2 x)
  constructor
  · rw [Module.End.mem_eigenspace_iff]
    ext v
    simpa only [Matrix.toLpLin_apply, PiLp.toLp_apply,
      SimpleGraph.adjMatrix_mulVec_apply, PiLp.smul_apply, smul_eq_mul] using hμ v
  · obtain ⟨v, hv⟩ := hx
    intro h
    exact hv (congrArg (fun z : EuclideanSpace ℝ V => z v) h)

/-- A positive eigenvector of the adjacency matrix determines the spectral radius. -/
theorem spectralRadius_eq_of_pos_eigenvector (G : SimpleGraph V) [DecidableRel G.Adj]
    [Nonempty V] (y : V → ℝ) (hy : ∀ v, 0 < y v) (μ : ℝ)
    (hμ : ∀ v, ∑ w ∈ G.neighborFinset v, y w = μ * y v) :
    spectralRadius G = μ := by
  classical
  obtain ⟨ν, w, hν, hw, he⟩ := exists_spectral_vector G
  obtain ⟨v₀, _, hv₀⟩ := Finset.exists_max_image (Finset.univ : Finset V)
    (fun v => |w v| / y v) Finset.univ_nonempty
  let t := |w v₀| / y v₀
  have hb (v : V) : |w v| ≤ t * y v :=
    (div_le_iff₀ (hy v)).mp (hv₀ v (Finset.mem_univ v))
  have ht : 0 ≤ t := div_nonneg (abs_nonneg _) (hy v₀).le
  have htpos : 0 < t := by
    by_contra hn
    have ht0 : t = 0 := le_antisymm (le_of_not_gt hn) ht
    have hz (v : V) : w v = 0 := abs_eq_zero.mp
      (le_antisymm (by simpa [ht0] using hb v) (abs_nonneg _))
    simp [hz] at hw
  have heq : t * y v₀ = |w v₀| := div_mul_cancel₀ _ (hy v₀).ne'
  have habspos : 0 < |w v₀| := heq ▸ mul_pos htpos (hy v₀)
  have hbound : |ν| * |w v₀| ≤ μ * |w v₀| := by
    calc
      |ν| * |w v₀| = |∑ v ∈ G.neighborFinset v₀, w v| := by
        rw [he, abs_mul]
      _ ≤ ∑ v ∈ G.neighborFinset v₀, |w v| := abs_sum_le_sum_abs _ _
      _ ≤ ∑ v ∈ G.neighborFinset v₀, t * y v :=
        Finset.sum_le_sum (fun v _ => hb v)
      _ = μ * |w v₀| := by rw [← Finset.mul_sum, hμ, ← heq]; ring
  apply le_antisymm
  · rw [← hν]
    exact (mul_le_mul_iff_left₀ habspos).mp hbound
  · obtain ⟨v⟩ := ‹Nonempty V›
    exact (le_abs_self μ).trans (abs_eigenvalue_le_radius G μ
      (hasEigenvalue_of_neighbor_sum G y ⟨v, (hy v).ne'⟩ μ hμ))

private lemma editDistance_lower_bound {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (k : ℕ)
    (h : ∀ S T, Disjoint S T → k ≤ editCost G S T) : k ≤ editDistance G := by
  unfold editDistance
  apply Finset.le_min'
  intro d hd
  obtain ⟨⟨S, T⟩, hp, rfl⟩ := Finset.mem_image.mp hd
  exact h S T (Finset.mem_filter.mp hp).2

/-- The five-cycle has no triangle. -/
theorem cycle5_triangleFree : (SimpleGraph.cycleGraph 5).CliqueFree 3 := by
  unfold SimpleGraph.CliqueFree
  decide

/-- The five-cycle has 5 edges. -/
theorem cycle5_edges : (SimpleGraph.cycleGraph 5).edgeFinset.card = 5 := by
  decide

set_option maxRecDepth 4096 in
/-- `D(C₅) = 3`: the target `K_{{0},{1,4}}` costs 3, and `decide` checks that every pair of
disjoint parts costs at least 3. -/
theorem cycle5_editDistance : editDistance (SimpleGraph.cycleGraph 5) = 3 := by
  apply le_antisymm
  · have h := editDistance_le_editCost (SimpleGraph.cycleGraph 5) {0} {1, 4}
      (by decide)
    exact h.trans_eq (by decide)
  · apply editDistance_lower_bound
    decide

/-- `λ(C₅) = 2`: the all-ones vector is a positive eigenvector with eigenvalue 2. -/
theorem cycle5_spectralRadius : spectralRadius (SimpleGraph.cycleGraph 5) = 2 := by
  apply spectralRadius_eq_of_pos_eigenvector _ (fun _ => 1) (by intro; norm_num)
  intro v
  simp only [Finset.sum_const, nsmul_eq_mul, mul_one,
    SimpleGraph.card_neighborFinset_eq_degree, SimpleGraph.cycleGraph_degree_three_le,
    Nat.cast_ofNat]

/-- The deficit of the five-cycle: `e(C₅) - λ(C₅)² = 1`. -/
theorem cycle5_deficit :
    ((SimpleGraph.cycleGraph 5).edgeFinset.card : ℝ) -
      spectralRadius (SimpleGraph.cycleGraph 5) ^ 2 = 1 := by
  rw [cycle5_edges, cycle5_spectralRadius]
  norm_num

/-- The five-cycle attains `D = 3 (e - λ²)` with positive deficit. -/
theorem cycle5_equality :
    (editDistance (SimpleGraph.cycleGraph 5) : ℝ) =
      3 * (((SimpleGraph.cycleGraph 5).edgeFinset.card : ℝ) -
        spectralRadius (SimpleGraph.cycleGraph 5) ^ 2) ∧
    0 < ((SimpleGraph.cycleGraph 5).edgeFinset.card : ℝ) -
      spectralRadius (SimpleGraph.cycleGraph 5) ^ 2 := by
  rw [cycle5_deficit, cycle5_editDistance]
  norm_num

/-- The coefficient 3 is sharp: every smaller real coefficient fails on a finite triangle-free
graph, namely the five-cycle. -/
theorem triangleFree_constant_sharp (c : ℝ) (hc : c < 3) :
    ∃ (n : ℕ) (G : SimpleGraph (Fin n)), G.CliqueFree 3 ∧
      c * ((G.edgeFinset.card : ℝ) - spectralRadius G ^ 2) < (editDistance G : ℝ) := by
  refine ⟨5, SimpleGraph.cycleGraph 5, cycle5_triangleFree, ?_⟩
  have h : c * (((SimpleGraph.cycleGraph 5).edgeFinset.card : ℝ) -
      spectralRadius (SimpleGraph.cycleGraph 5) ^ 2) <
      (editDistance (SimpleGraph.cycleGraph 5) : ℝ) := by
    simpa only [cycle5_deficit, cycle5_editDistance, Nat.cast_ofNat, mul_one] using hc
  convert h using 1 <;> congr!

end TriangleFreeSharpness
