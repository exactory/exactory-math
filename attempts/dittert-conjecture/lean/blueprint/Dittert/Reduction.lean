import Dittert.Obligations
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Analysis.Normed.Module.FiniteDimension
import Mathlib.LinearAlgebra.Matrix.Permanent

/-!
# Reduction to boundary maximizers

Lemma chain for `Dittert.reduction : Reduction`. The informal proof is in
`attack/reduction-to-boundary/study/problem.md`; the lemma structure is in `REDUCTION-NOTES.md`.
-/

namespace Dittert

open Matrix Finset BigOperators

variable {n : ℕ}

/-! ### 1. Continuity and compactness -/

/-- `Φ` is continuous in the entries. -/
theorem continuous_Phi : Continuous (fun A : Matrix (Fin n) (Fin n) ℝ => Phi A) := by
  unfold Phi rowSum colSum Matrix.permanent
  fun_prop

/-- `K_n` is compact: closed (equalities and inequalities of continuous functions) and bounded
(every entry lies in `[0, n]`). -/
theorem entry_le_totalSum (A : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i j, 0 ≤ A i j) (i j : Fin n) :
    A i j ≤ totalSum A := by
  unfold totalSum
  calc A i j ≤ ∑ c, A i c := Finset.single_le_sum (fun c _ => hA i c) (Finset.mem_univ j)
    _ ≤ ∑ r, ∑ c, A r c := Finset.single_le_sum (fun r _ => Finset.sum_nonneg fun c _ => hA r c) (Finset.mem_univ i)

theorem isCompact_feasible : IsCompact {A : Matrix (Fin n) (Fin n) ℝ | Feasible A} := by
  have hbox : IsCompact (Set.pi Set.univ fun _ : Fin n => Set.pi Set.univ fun _ : Fin n => Set.Icc (0 : ℝ) n) :=
    isCompact_univ_pi fun _ => isCompact_univ_pi fun _ => isCompact_Icc
  refine hbox.of_isClosed_subset ?_ ?_
  · have h1 : IsClosed {A : Matrix (Fin n) (Fin n) ℝ | ∀ i j, 0 ≤ A i j} := by
      simp only [Set.ofPred_forall]
      exact isClosed_iInter fun i => isClosed_iInter fun j =>
        isClosed_le continuous_const ((continuous_apply j).comp (continuous_apply i))
    have h2 : IsClosed {A : Matrix (Fin n) (Fin n) ℝ | totalSum A = n} := by
      refine isClosed_eq ?_ continuous_const
      unfold totalSum; fun_prop
    exact h1.inter h2
  · intro A hA
    simp only [Set.mem_pi, Set.mem_univ, true_implies, Set.mem_Icc]
    intro i j
    exact ⟨hA.1 i j, hA.2 ▸ entry_le_totalSum A hA.1 i j⟩

/-- The uniform matrix `J_n / n`. -/
noncomputable def uniform (n : ℕ) : Matrix (Fin n) (Fin n) ℝ := Matrix.of fun _ _ => 1 / (n : ℝ)

/-- The uniform matrix is feasible. -/
theorem feasible_uniform (hn : 1 ≤ n) : Feasible (uniform n) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  refine ⟨fun _ _ => by simp only [uniform, Matrix.of_apply]; positivity, ?_⟩
  simp [totalSum, uniform, Finset.sum_const, Finset.card_univ, Fintype.card_fin]
  try field_simp

/-- A maximizer of `Φ` on `K_n` exists. -/
theorem exists_maximizer (hn : 1 ≤ n) : ∃ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A := by
  obtain ⟨A, hA, hmax⟩ := isCompact_feasible.exists_isMaxOn ⟨uniform n, feasible_uniform hn⟩
    continuous_Phi.continuousOn
  exact ⟨A, hA, fun B hB => hmax hB⟩

/-! ### 2. The value at the uniform matrix -/

/-- `per (J_n / n) = n! / n^n`: every permutation contributes `(1/n)^n`. -/
theorem permanent_uniform (hn : 1 ≤ n) : (uniform n).permanent = gamma n := by
  unfold Matrix.permanent uniform gamma
  simp only [Matrix.of_apply, Finset.prod_const, Finset.card_univ, Fintype.card_fin,
    Finset.sum_const, Fintype.card_perm, nsmul_eq_mul]
  rw [one_div, inv_pow]
  field_simp

/-- `Φ (J_n / n) = 2 - γ_n`. -/
theorem rowSum_uniform (hn : 1 ≤ n) (i : Fin n) : rowSum (uniform n) i = 1 := by
  have hn' : (n : ℝ) ≠ 0 := by exact_mod_cast (Nat.one_le_iff_ne_zero.mp hn)
  simp [rowSum, uniform, Finset.sum_const, Finset.card_univ, Fintype.card_fin, hn']

theorem colSum_uniform (hn : 1 ≤ n) (j : Fin n) : colSum (uniform n) j = 1 := by
  have hn' : (n : ℝ) ≠ 0 := by exact_mod_cast (Nat.one_le_iff_ne_zero.mp hn)
  simp [colSum, uniform, Finset.sum_const, Finset.card_univ, Fintype.card_fin, hn']

theorem phi_uniform (hn : 1 ≤ n) : Phi (uniform n) = 2 - gamma n := by
  unfold Phi
  simp only [rowSum_uniform hn, colSum_uniform hn, Finset.prod_const_one, permanent_uniform hn]
  ring

/-- `IsUniform A` says exactly that `A` is the uniform matrix. -/
theorem isUniform_iff_eq_uniform (A : Matrix (Fin n) (Fin n) ℝ) : IsUniform A ↔ A = uniform n := by
  constructor
  · intro h
    ext i j
    rw [h i j]
    rfl
  · rintro rfl i j
    rfl

/-! ### 3. Mixing two rows -/

/-- The mixing of rows `i` and `k` with parameter `t`: row `i` becomes `(1-t) A i + t A k`, row
`k` becomes `t A i + (1-t) A k`, the other rows are unchanged. -/
noncomputable def mixRows (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) (t : ℝ) : Matrix (Fin n) (Fin n) ℝ :=
  fun r c => if r = i then (1 - t) * A i c + t * A k c
    else if r = k then t * A i c + (1 - t) * A k c else A r c

/-- The entries of the mixing, row by row. -/
theorem mixRows_apply_self (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) (t : ℝ) (c : Fin n) :
    mixRows A i k t i c = (1 - t) * A i c + t * A k c := by
  simp [mixRows]

theorem mixRows_apply_other (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ)
    (c : Fin n) : mixRows A i k t k c = t * A i c + (1 - t) * A k c := by
  simp [mixRows, hik.symm]

theorem mixRows_apply_of_ne (A : Matrix (Fin n) (Fin n) ℝ) {i k r : Fin n} (hri : r ≠ i) (hrk : r ≠ k)
    (t : ℝ) (c : Fin n) : mixRows A i k t r c = A r c := by
  simp [mixRows, hri, hrk]

/-- A sum over `Fin n` split at two distinct indices. -/
theorem sum_eq_add_add_sum_erase_erase (f : Fin n → ℝ) {i k : Fin n} (hik : i ≠ k) :
    ∑ r, f r = f i + f k + ∑ r ∈ (univ.erase i).erase k, f r := by
  rw [add_assoc, Finset.add_sum_erase _ _ (Finset.mem_erase.mpr ⟨hik.symm, Finset.mem_univ k⟩),
    Finset.add_sum_erase _ _ (Finset.mem_univ i)]

/-- A product over `Fin n` split at two distinct indices. -/
theorem prod_eq_mul_mul_prod_erase_erase (f : Fin n → ℝ) {i k : Fin n} (hik : i ≠ k) :
    ∏ r, f r = f i * f k * ∏ r ∈ (univ.erase i).erase k, f r := by
  rw [mul_assoc, Finset.mul_prod_erase _ _ (Finset.mem_erase.mpr ⟨hik.symm, Finset.mem_univ k⟩),
    Finset.mul_prod_erase _ _ (Finset.mem_univ i)]

/-- Away from rows `i` and `k` the entries of the mixing are those of `A`. -/
theorem sum_erase_erase_mixRows (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) (t : ℝ) (c : Fin n) :
    ∑ r ∈ (univ.erase i).erase k, mixRows A i k t r c = ∑ r ∈ (univ.erase i).erase k, A r c := by
  refine Finset.sum_congr rfl fun r hr => ?_
  rw [Finset.mem_erase, Finset.mem_erase] at hr
  exact mixRows_apply_of_ne A hr.2.1 hr.1 t c

/-- Mixing keeps every column sum. -/
theorem colSum_mixRows (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) (c : Fin n) :
    colSum (mixRows A i k t) c = colSum A c := by
  unfold colSum
  rw [sum_eq_add_add_sum_erase_erase (fun r => mixRows A i k t r c) hik,
    sum_eq_add_add_sum_erase_erase (fun r => A r c) hik, mixRows_apply_self,
    mixRows_apply_other A hik, sum_erase_erase_mixRows]
  ring

/-- Mixing keeps the total sum. -/
theorem totalSum_mixRows (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    totalSum (mixRows A i k t) = totalSum A := by
  unfold totalSum
  calc (∑ r, ∑ c, mixRows A i k t r c) = ∑ c, ∑ r, mixRows A i k t r c := Finset.sum_comm
    _ = ∑ c, ∑ r, A r c := Finset.sum_congr rfl fun c _ => colSum_mixRows A hik t c
    _ = ∑ r, ∑ c, A r c := Finset.sum_comm

/-- The two mixed row sums. -/
theorem rowSum_mixRows_self (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    rowSum (mixRows A i k t) i = (1 - t) * rowSum A i + t * rowSum A k := by
  unfold rowSum mixRows
  simp [Finset.mul_sum, Finset.sum_add_distrib]

theorem rowSum_mixRows_other (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    rowSum (mixRows A i k t) k = t * rowSum A i + (1 - t) * rowSum A k := by
  unfold rowSum mixRows
  simp [hik.symm, Finset.mul_sum, Finset.sum_add_distrib]

theorem rowSum_mixRows_of_ne (A : Matrix (Fin n) (Fin n) ℝ) {i k r : Fin n} (hri : r ≠ i) (hrk : r ≠ k)
    (t : ℝ) : rowSum (mixRows A i k t) r = rowSum A r := by
  unfold rowSum mixRows
  simp [hri, hrk]

/-- The mixing at `t = 0` is `A`. -/
theorem mixRows_zero (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) : mixRows A i k 0 = A := by
  ext r c
  unfold mixRows
  by_cases hri : r = i
  · subst hri; simp
  · by_cases hrk : r = k
    · subst hrk; simp [hri]
    · simp [hri, hrk]

/-- Swapping the roles of `i` and `k` is the parameter `1 - t`, up to the row swap. -/
theorem mixRows_symm (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) (t : ℝ) :
    mixRows A i k (1 - t) = (mixRows A i k t).submatrix (Equiv.swap i k) id := by
  ext r c
  simp only [Matrix.submatrix_apply, id_eq]
  by_cases hri : r = i
  · rw [hri, Equiv.swap_apply_left]
    by_cases hik : i = k
    · rw [hik, mixRows_apply_self, mixRows_apply_self]
      ring
    · rw [mixRows_apply_self, mixRows_apply_other A hik]
      ring
  · by_cases hrk : r = k
    · have hik : i ≠ k := fun h => hri (hrk.trans h.symm)
      rw [hrk, Equiv.swap_apply_right, mixRows_apply_other A hik, mixRows_apply_self]
      ring
    · rw [Equiv.swap_apply_of_ne_of_ne hri hrk, mixRows_apply_of_ne A hri hrk,
        mixRows_apply_of_ne A hri hrk]

/-! #### The permanent along the mixing line -/

/-- The permanent of a matrix with column `j` replaced by `w`, as a linear form in `w`. -/
theorem permanent_updateCol_eq (M : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) (w : Fin n → ℝ) :
    (updateCol M j w).permanent =
      ∑ σ : Equiv.Perm (Fin n), w (σ j) * ∏ c ∈ univ.erase j, M (σ c) c := by
  unfold Matrix.permanent
  refine Finset.sum_congr rfl fun σ _ => ?_
  rw [← Finset.mul_prod_erase univ _ (Finset.mem_univ j), updateCol_self]
  congr 1
  refine Finset.prod_congr rfl fun c hc => ?_
  rw [updateCol_ne (Finset.ne_of_mem_erase hc)]

/-- The permanent is additive in one column. -/
theorem permanent_updateCol_add (M : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) (u v : Fin n → ℝ) :
    (updateCol M j (u + v)).permanent = (updateCol M j u).permanent + (updateCol M j v).permanent := by
  simp only [permanent_updateCol_eq, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- The permanent is additive in one row. -/
theorem permanent_updateRow_add (M : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) (u v : Fin n → ℝ) :
    (updateRow M j (u + v)).permanent = (updateRow M j u).permanent + (updateRow M j v).permanent := by
  rw [← permanent_transpose, ← updateCol_transpose, permanent_updateCol_add, updateCol_transpose,
    updateCol_transpose, permanent_transpose, permanent_transpose]

/-- The mixing as two row updates. -/
theorem mixRows_eq_updateRow (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    mixRows A i k t =
      updateRow (updateRow A i ((1 - t) • A i + t • A k)) k (t • A i + (1 - t) • A k) := by
  ext r c
  by_cases hrk : r = k
  · rw [hrk, updateRow_self, mixRows_apply_other A hik]
    simp
  · rw [updateRow_ne hrk]
    by_cases hri : r = i
    · rw [hri, updateRow_self, mixRows_apply_self]
      simp
    · rw [updateRow_ne hri, mixRows_apply_of_ne A hri hrk]

/-- Replacing row `k` by row `i` and row `i` by row `k` swaps the two rows. -/
theorem updateRow_updateRow_eq_swap (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) :
    updateRow (updateRow A k (A i)) i (A k) = A.submatrix (Equiv.swap i k) id := by
  ext r c
  simp only [Matrix.submatrix_apply, id_eq]
  by_cases hri : r = i
  · rw [hri, updateRow_self, Equiv.swap_apply_left]
  · rw [updateRow_ne hri]
    by_cases hrk : r = k
    · rw [hrk, updateRow_self, Equiv.swap_apply_right]
    · rw [updateRow_ne hrk, Equiv.swap_apply_of_ne_of_ne hri hrk]

/-- The permanent along the mixing line: `per A + t (1 - t) (per A_{k ← i} + per A_{i ← k} - 2 per A)`,
where `A_{k ← i}` is `A` with row `k` replaced by row `i`. -/
theorem permanent_mixRows (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    (mixRows A i k t).permanent = A.permanent + t * (1 - t) *
      ((updateRow A k (A i)).permanent + (updateRow A i (A k)).permanent - 2 * A.permanent) := by
  have hswap : (updateRow (updateRow A k (A i)) i (A k)).permanent = A.permanent := by
    rw [updateRow_updateRow_eq_swap A i k, permanent_permute_cols]
  have h1 : updateRow (updateRow A k (A i)) i (A i) = updateRow A k (A i) := by
    have := updateRow_eq_self (updateRow A k (A i)) i
    rwa [updateRow_ne hik] at this
  have h2 : updateRow (updateRow A k (A k)) i (A i) = A := by
    rw [updateRow_eq_self, updateRow_eq_self]
  have h3 : updateRow (updateRow A k (A k)) i (A k) = updateRow A i (A k) := by
    rw [updateRow_eq_self]
  rw [mixRows_eq_updateRow A hik t]
  simp only [permanent_updateRow_add, permanent_updateRow_smul]
  rw [updateRow_comm A hik, updateRow_comm A hik]
  simp only [permanent_updateRow_add, permanent_updateRow_smul, h1, hswap, h2, h3]
  ring

/-! #### The row and column products along the mixing line -/

/-- The row product along the mixing line. -/
theorem prod_rowSum_mixRows (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    ∏ r, rowSum (mixRows A i k t) r = ∏ r, rowSum A r +
      t * (1 - t) * ((rowSum A i - rowSum A k) ^ 2 * ∏ r ∈ (univ.erase i).erase k, rowSum A r) := by
  have hrest : ∏ r ∈ (univ.erase i).erase k, rowSum (mixRows A i k t) r =
      ∏ r ∈ (univ.erase i).erase k, rowSum A r := by
    refine Finset.prod_congr rfl fun r hr => ?_
    rw [Finset.mem_erase, Finset.mem_erase] at hr
    exact rowSum_mixRows_of_ne A hr.2.1 hr.1 t
  rw [prod_eq_mul_mul_prod_erase_erase (rowSum (mixRows A i k t)) hik,
    prod_eq_mul_mul_prod_erase_erase (rowSum A) hik, hrest, rowSum_mixRows_self A hik,
    rowSum_mixRows_other A hik]
  ring

/-- The column product is constant along the mixing line. -/
theorem prod_colSum_mixRows (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    ∏ c, colSum (mixRows A i k t) c = ∏ c, colSum A c :=
  Finset.prod_congr rfl fun c _ => colSum_mixRows A hik t c

/-- `Φ` of the mixing is a quadratic polynomial in `t` symmetric under `t ↦ 1 - t`:
there is `α` with `Φ (mixRows A i k t) = Φ A + α * t * (1 - t)` for every `t`. -/
theorem phi_mixRows_quadratic (A : Matrix (Fin n) (Fin n) ℝ) {i k : Fin n} (hik : i ≠ k) :
    ∃ α : ℝ, ∀ t : ℝ, Phi (mixRows A i k t) = Phi A + α * t * (1 - t) := by
  refine ⟨(rowSum A i - rowSum A k) ^ 2 * ∏ r ∈ (univ.erase i).erase k, rowSum A r -
    ((updateRow A k (A i)).permanent + (updateRow A i (A k)).permanent - 2 * A.permanent),
    fun t => ?_⟩
  unfold Phi
  rw [prod_rowSum_mixRows A hik t, prod_colSum_mixRows A hik t, permanent_mixRows A hik t]
  ring

/-! #### Feasibility near `t = 0` and the vanishing of the quadratic coefficient -/

/-- Every entry of the mixing is continuous in `t`. -/
theorem continuous_mixRows_entry (A : Matrix (Fin n) (Fin n) ℝ) (i k r c : Fin n) :
    Continuous fun t : ℝ => mixRows A i k t r c := by
  by_cases hri : r = i
  · simp only [mixRows, if_pos hri]
    fun_prop
  · by_cases hrk : r = k
    · simp only [mixRows, if_neg hri, if_pos hrk]
      fun_prop
    · simp only [mixRows, if_neg hri, if_neg hrk]
      exact continuous_const

/-- For a positive matrix, the mixing stays feasible for all `t` in an open interval around `0`. -/
theorem feasible_mixRows_of_pos (A : Matrix (Fin n) (Fin n) ℝ) (hA : Feasible A)
    (hpos : ∀ r c, 0 < A r c) {i k : Fin n} (hik : i ≠ k) :
    ∃ ε > 0, ∀ t : ℝ, |t| < ε → Feasible (mixRows A i k t) := by
  have hev : ∀ᶠ t in nhds (0 : ℝ), ∀ r c, 0 < mixRows A i k t r c := by
    rw [Filter.eventually_all]
    intro r
    rw [Filter.eventually_all]
    intro c
    have h0 : (0 : ℝ) < mixRows A i k 0 r c := by
      rw [mixRows_zero]
      exact hpos r c
    exact Filter.Tendsto.eventually_const_lt h0 (continuous_mixRows_entry A i k r c).continuousAt
  obtain ⟨ε, hε, hball⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨ε, hε, fun t ht => ?_⟩
  have hmem : ∀ r c, 0 < mixRows A i k t r c := hball (by rw [Real.dist_eq, sub_zero]; exact ht)
  exact ⟨fun r c => (hmem r c).le, by rw [totalSum_mixRows A hik]; exact hA.2⟩

/-- At a positive maximizer the quadratic coefficient vanishes: `Φ` is constant on the mixing line. -/
theorem phi_mixRows_const (A : Matrix (Fin n) (Fin n) ℝ) (hA : IsMaximizer A)
    (hpos : ∀ r c, 0 < A r c) {i k : Fin n} (hik : i ≠ k) (t : ℝ) :
    Phi (mixRows A i k t) = Phi A := by
  obtain ⟨α, hα⟩ := phi_mixRows_quadratic A hik
  obtain ⟨ε, hε, hfeas⟩ := feasible_mixRows_of_pos A hA.1 hpos hik
  have hle : ∀ s : ℝ, |s| < ε → α * s * (1 - s) ≤ 0 := by
    intro s hs
    have := hA.2 _ (hfeas s hs)
    rw [hα s] at this
    linarith
  set s : ℝ := min (ε / 2) (1 / 2) with hs
  have hs0 : 0 < s := lt_min (by positivity) (by norm_num)
  have hs1 : s ≤ 1 / 2 := min_le_right _ _
  have hsε : s < ε := (min_le_left _ _).trans_lt (by linarith)
  have h1 := hle s (by rw [abs_of_pos hs0]; exact hsε)
  have h2 := hle (-s) (by rw [abs_neg, abs_of_pos hs0]; exact hsε)
  have hp : 0 < s * (1 - s) := by nlinarith
  have hq : 0 < s * (1 + s) := by nlinarith
  have hα0 : α = 0 := by
    apply le_antisymm
    · nlinarith
    · nlinarith
  rw [hα t, hα0]
  ring

/-! #### Following the mixing line to the boundary -/

/-- Every entry of the mixing is affine in `t`, with slope the entry of `mixRows A i k 1 - A`. -/
theorem mixRows_apply_eq_add_mul (A : Matrix (Fin n) (Fin n) ℝ) (i k : Fin n) (t : ℝ) (r c : Fin n) :
    mixRows A i k t r c = A r c + t * (mixRows A i k 1 r c - A r c) := by
  by_cases hri : r = i
  · rw [hri, mixRows_apply_self, mixRows_apply_self]
    ring
  · by_cases hrk : r = k
    · have hik : i ≠ k := fun h => hri (hrk.trans h.symm)
      rw [hrk, mixRows_apply_other A hik, mixRows_apply_other A hik]
      ring
    · rw [mixRows_apply_of_ne A hri hrk, mixRows_apply_of_ne A hri hrk]
      ring

/-- If rows `i` and `k` of a positive matrix differ, some parameter `t` makes the mixing
nonnegative with a zero entry (follow the line to the first vanishing entry). -/
theorem exists_boundary_mixRows (A : Matrix (Fin n) (Fin n) ℝ) (hpos : ∀ r c, 0 < A r c)
    {i k : Fin n} (hik : i ≠ k) (hne : ∃ c, A i c ≠ A k c) :
    ∃ t : ℝ, (∀ r c, 0 ≤ mixRows A i k t r c) ∧ ∃ r c, mixRows A i k t r c = 0 := by
  -- `D r c` is the slope of the entry `(r, c)` along the line.
  set D : Fin n → Fin n → ℝ := fun r c => mixRows A i k 1 r c - A r c with hD
  have haff : ∀ t r c, mixRows A i k t r c = A r c + t * D r c :=
    fun t r c => mixRows_apply_eq_add_mul A i k t r c
  -- The entries with negative slope.
  set S : Finset (Fin n × Fin n) := univ.filter fun p => D p.1 p.2 < 0 with hS
  have hSne : S.Nonempty := by
    obtain ⟨c, hc⟩ := hne
    rcases lt_or_gt_of_ne hc with h | h
    · refine ⟨(k, c), Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩⟩
      simp only [hD, mixRows_apply_other A hik]
      linarith
    · refine ⟨(i, c), Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩⟩
      simp only [hD, mixRows_apply_self]
      linarith
  -- The entry that vanishes first.
  obtain ⟨p₀, hp₀, hmin⟩ := S.exists_min_image (fun p => A p.1 p.2 / (-D p.1 p.2)) hSne
  have hD₀ : D p₀.1 p₀.2 < 0 := (Finset.mem_filter.mp hp₀).2
  refine ⟨A p₀.1 p₀.2 / (-D p₀.1 p₀.2), fun r c => ?_, p₀.1, p₀.2, ?_⟩
  · rw [haff]
    by_cases hrc : D r c < 0
    · have hle : A p₀.1 p₀.2 / (-D p₀.1 p₀.2) ≤ A r c / (-D r c) :=
        hmin (r, c) (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hrc⟩)
      have hneg : 0 < -D r c := by linarith
      rw [le_div_iff₀ hneg] at hle
      linarith
    · have hrc' : 0 ≤ D r c := not_lt.mp hrc
      have ht : 0 ≤ A p₀.1 p₀.2 / (-D p₀.1 p₀.2) := div_nonneg (hpos _ _).le (by linarith)
      have := mul_nonneg ht hrc'
      linarith [hpos r c]
  · have hne0 : D p₀.1 p₀.2 ≠ 0 := hD₀.ne
    have hkey : A p₀.1 p₀.2 / (-D p₀.1 p₀.2) * D p₀.1 p₀.2 = -A p₀.1 p₀.2 := by
      rw [div_mul_eq_mul_div, div_neg, mul_div_assoc, div_self hne0, mul_one]
    rw [haff, hkey]
    ring

/-! ### 4. Transposition -/

theorem totalSum_transpose (A : Matrix (Fin n) (Fin n) ℝ) : totalSum Aᵀ = totalSum A := by
  unfold totalSum
  simp only [Matrix.transpose_apply]
  exact Finset.sum_comm

theorem feasible_transpose (A : Matrix (Fin n) (Fin n) ℝ) : Feasible Aᵀ ↔ Feasible A := by
  unfold Feasible
  rw [totalSum_transpose]
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨fun i j => h1 j i, h2⟩
  · rintro ⟨h1, h2⟩; exact ⟨fun i j => h1 j i, h2⟩

theorem phi_transpose (A : Matrix (Fin n) (Fin n) ℝ) : Phi Aᵀ = Phi A := by
  unfold Phi rowSum colSum
  simp only [Matrix.transpose_apply, Matrix.permanent_transpose]
  ring

theorem isMaximizer_transpose (A : Matrix (Fin n) (Fin n) ℝ) : IsMaximizer Aᵀ ↔ IsMaximizer A := by
  unfold IsMaximizer
  rw [feasible_transpose, phi_transpose]

/-! ### 5. Assembly -/

/-- Under the positivity hypothesis every maximizer has all rows equal: two different rows give,
along the mixing line, a maximizer with a zero entry. -/
theorem rows_eq_of_maximizer
    (hpos : ∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A → ∀ i j, 0 < A i j)
    (A : Matrix (Fin n) (Fin n) ℝ) (hA : IsMaximizer A) (i k c : Fin n) : A i c = A k c := by
  by_contra hne
  have hik : i ≠ k := by
    rintro rfl
    exact hne rfl
  obtain ⟨t, hnonneg, r, c', hzero⟩ := exists_boundary_mixRows A (hpos A hA) hik ⟨c, hne⟩
  have hfeas : Feasible (mixRows A i k t) :=
    ⟨hnonneg, by rw [totalSum_mixRows A hik]; exact hA.1.2⟩
  have hmax : IsMaximizer (mixRows A i k t) :=
    ⟨hfeas, fun B hB => by rw [phi_mixRows_const A hA (hpos A hA) hik t]; exact hA.2 B hB⟩
  exact (hpos _ hmax r c').ne' hzero

/-- If no maximizer has a zero entry, every maximizer has all rows equal and all columns equal,
hence is uniform. -/
theorem maximizer_uniform (hn : 2 ≤ n)
    (hpos : ∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A → ∀ i j, 0 < A i j)
    (A : Matrix (Fin n) (Fin n) ℝ) (hA : IsMaximizer A) : IsUniform A := by
  have hrow : ∀ i k c, A i c = A k c := rows_eq_of_maximizer hpos A hA
  have hcol : ∀ r c c', A r c = A r c' := fun r c c' =>
    rows_eq_of_maximizer hpos Aᵀ ((isMaximizer_transpose A).mpr hA) c c' r
  have h0 : 0 < n := by omega
  set i₀ : Fin n := ⟨0, h0⟩ with hi₀
  have hall : ∀ r c, A r c = A i₀ i₀ := fun r c => (hrow r i₀ c).trans (hcol i₀ c i₀)
  have hsum : totalSum A = (n : ℝ) * ((n : ℝ) * A i₀ i₀) := by
    unfold totalSum
    rw [Finset.sum_congr rfl fun r _ => Finset.sum_congr rfl fun c _ => hall r c]
    simp [Finset.sum_const, Finset.card_univ, Fintype.card_fin]
  have htot : (n : ℝ) * ((n : ℝ) * A i₀ i₀) = n := hsum.symm.trans hA.1.2
  have hn0 : (n : ℝ) ≠ 0 := by positivity
  intro r c
  rw [hall r c, eq_div_iff hn0]
  have h1 : (n : ℝ) * ((n : ℝ) * A i₀ i₀ - 1) = 0 := by linear_combination htot
  rcases mul_eq_zero.mp h1 with h | h
  · exact absurd h hn0
  · linear_combination h

/-- Obligation `reduction`. -/
theorem reduction : Reduction := by
  intro n hn hpos A hA
  have hn1 : 1 ≤ n := by omega
  obtain ⟨M, hM⟩ := exists_maximizer hn1
  have hMeq : M = uniform n := (isUniform_iff_eq_uniform M).mp (maximizer_uniform hn hpos M hM)
  have hPhiM : Phi M = 2 - gamma n := by
    rw [hMeq]
    exact phi_uniform hn1
  refine ⟨by rw [← hPhiM]; exact hM.2 A hA, ?_, ?_⟩
  · intro hPhiA
    exact maximizer_uniform hn hpos A
      ⟨hA, fun B hB => by rw [hPhiA, ← hPhiM]; exact hM.2 B hB⟩
  · intro hAu
    rw [(isUniform_iff_eq_uniform A).mp hAu]
    exact phi_uniform hn1

end Dittert
