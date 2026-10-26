import Dittert.Obligations
import Mathlib.Topology.Instances.Matrix

/-!
# Hall domination

This module proves `HallDomination` from `Dittert.Obligations`: for a nonnegative `n × n` real
matrix `A` and `λ > 0`, the cut condition
`λ (|I| + |J| - n) ≤ ∑_{i ∈ I} ∑_{j ∈ J} A i j` for every `I, J` with `|I| + |J| > n`
yields a doubly stochastic `B` with `λ B ≤ A` entrywise.

The proof is the augmenting-path argument for a maximum flow with real capacities.

* A *flow* is a matrix `F` with `0 ≤ F ≤ A` entrywise and every row and column sum at most `λ`
  (`FlowSet`). The flows form a nonempty compact set, so `totalSum` attains a maximum on it
  (`exists_max_flow`).
* Residual reachability is the inductive predicate `Reach`: a row with slack is reachable, a
  column `j` is reachable from a reachable row `i` with `F i j < A i j`, and a row `i` is
  reachable from a reachable column `j` with `0 < F i j`.
* Every derivation of `Reach` yields a direction matrix `D` (`AugSpec`) whose positive entries
  sit on unsaturated edges, whose negative entries sit on positive edges, and whose row and
  column sums are the indicator of the start row and of the end vertex. For a maximal flow,
  every reachable column is saturated (`le_colSum_of_reach`), since otherwise `F + ε D` is a
  flow with a larger total for small `ε > 0` (`exists_better_flow`).
* Counting the total over the reachable rows `I` and reachable columns `J` and applying the cut
  condition to `(I, Jᶜ)` shows that a maximal flow has every row and column sum equal to `λ`
  (`max_flow_saturated`). Then `B = F / λ` is doubly stochastic and `λ B = F ≤ A`.
-/

namespace Dittert

open Matrix Finset BigOperators Filter Topology

variable {n : ℕ}

/-! ### Row, column and total sums -/

theorem totalSum_eq_sum_rowSum (F : Matrix (Fin n) (Fin n) ℝ) :
    totalSum F = ∑ i, rowSum F i := rfl

theorem totalSum_eq_sum_colSum (F : Matrix (Fin n) (Fin n) ℝ) :
    totalSum F = ∑ j, colSum F j := by
  unfold totalSum colSum
  exact Finset.sum_comm

theorem rowSum_add (F G : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) :
    rowSum (F + G) i = rowSum F i + rowSum G i := by
  simp [rowSum, Finset.sum_add_distrib]

theorem rowSum_sub (F G : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) :
    rowSum (F - G) i = rowSum F i - rowSum G i := by
  simp [rowSum, Finset.sum_sub_distrib]

theorem rowSum_smul (c : ℝ) (F : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) :
    rowSum (c • F) i = c * rowSum F i := by
  simp [rowSum, Finset.mul_sum]

theorem colSum_add (F G : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) :
    colSum (F + G) j = colSum F j + colSum G j := by
  simp [colSum, Finset.sum_add_distrib]

theorem colSum_sub (F G : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) :
    colSum (F - G) j = colSum F j - colSum G j := by
  simp [colSum, Finset.sum_sub_distrib]

theorem colSum_smul (c : ℝ) (F : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) :
    colSum (c • F) j = c * colSum F j := by
  simp [colSum, Finset.mul_sum]

theorem totalSum_add (F G : Matrix (Fin n) (Fin n) ℝ) :
    totalSum (F + G) = totalSum F + totalSum G := by
  simp [totalSum_eq_sum_rowSum, rowSum_add, Finset.sum_add_distrib]

theorem totalSum_smul (c : ℝ) (F : Matrix (Fin n) (Fin n) ℝ) :
    totalSum (c • F) = c * totalSum F := by
  simp [totalSum_eq_sum_rowSum, rowSum_smul, Finset.mul_sum]

/-! ### The indicator and the single-entry matrix -/

/-- The indicator of the index `i`: `ind i a = 1` if `a = i` and `0` otherwise. -/
def ind (i a : Fin n) : ℝ := if a = i then 1 else 0

theorem sum_ind (i : Fin n) : ∑ a, ind i a = 1 := by
  simp [ind]

/-- The matrix with the single entry `1` at position `(i, j)`. -/
def single (i j : Fin n) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun a b => if a = i ∧ b = j then 1 else 0

theorem single_apply (i j a b : Fin n) :
    single i j a b = if a = i ∧ b = j then 1 else 0 := rfl

theorem rowSum_single (i j a : Fin n) : rowSum (single i j) a = ind i a := by
  by_cases h : a = i <;> simp [rowSum, single_apply, ind, h]

theorem colSum_single (i j b : Fin n) : colSum (single i j) b = ind j b := by
  by_cases h : b = j <;> simp [colSum, single_apply, ind, h]

/-! ### Flows -/

/-- The flows below `A` with parameter `lam`: `0 ≤ F ≤ A` entrywise, every row sum and every
column sum at most `lam`. -/
def FlowSet (A : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) : Set (Matrix (Fin n) (Fin n) ℝ) :=
  {F | (∀ i j, 0 ≤ F i j) ∧ (∀ i j, F i j ≤ A i j) ∧
    (∀ i, rowSum F i ≤ lam) ∧ (∀ j, colSum F j ≤ lam)}

theorem zero_mem_flowSet {A : Matrix (Fin n) (Fin n) ℝ} (hA : ∀ i j, 0 ≤ A i j) {lam : ℝ}
    (hlam : 0 ≤ lam) : (0 : Matrix (Fin n) (Fin n) ℝ) ∈ FlowSet A lam :=
  ⟨fun i j => by simp, fun i j => by simpa using hA i j,
    fun i => by simpa [rowSum] using hlam, fun j => by simpa [colSum] using hlam⟩

theorem isClosed_flowSet (A : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) : IsClosed (FlowSet A lam) := by
  have h1 : IsClosed {F : Matrix (Fin n) (Fin n) ℝ | ∀ i j, 0 ≤ F i j} := by
    simp only [Set.ofPred_forall]
    exact isClosed_iInter fun _ => isClosed_iInter fun _ =>
      isClosed_le continuous_const (by fun_prop)
  have h2 : IsClosed {F : Matrix (Fin n) (Fin n) ℝ | ∀ i j, F i j ≤ A i j} := by
    simp only [Set.ofPred_forall]
    exact isClosed_iInter fun _ => isClosed_iInter fun _ =>
      isClosed_le (by fun_prop) continuous_const
  have h3 : IsClosed {F : Matrix (Fin n) (Fin n) ℝ | ∀ i, rowSum F i ≤ lam} := by
    simp only [Set.ofPred_forall]
    exact isClosed_iInter fun _ => isClosed_le (by unfold rowSum; fun_prop) continuous_const
  have h4 : IsClosed {F : Matrix (Fin n) (Fin n) ℝ | ∀ j, colSum F j ≤ lam} := by
    simp only [Set.ofPred_forall]
    exact isClosed_iInter fun _ => isClosed_le (by unfold colSum; fun_prop) continuous_const
  have hset : FlowSet A lam = {F | ∀ i j, 0 ≤ F i j} ∩ {F | ∀ i j, F i j ≤ A i j} ∩
      {F | ∀ i, rowSum F i ≤ lam} ∩ {F | ∀ j, colSum F j ≤ lam} := by
    ext F
    simp only [FlowSet, Set.mem_ofPred_eq, Set.mem_inter_iff]
    tauto
  rw [hset]
  exact ((h1.inter h2).inter h3).inter h4

theorem flowSet_subset_box (A : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) :
    FlowSet A lam ⊆ (Set.pi Set.univ fun i => Set.pi Set.univ fun j => Set.Icc 0 (A i j) :
      Set (Matrix (Fin n) (Fin n) ℝ)) := by
  intro F hF
  exact Set.mem_univ_pi.mpr fun i => Set.mem_univ_pi.mpr fun j => ⟨hF.1 i j, hF.2.1 i j⟩

theorem isCompact_flowSet (A : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) :
    IsCompact (FlowSet A lam) :=
  (isCompact_univ_pi fun _ => isCompact_univ_pi fun _ => isCompact_Icc).of_isClosed_subset
    (isClosed_flowSet A lam) (flowSet_subset_box A lam)

/-- A flow of maximal total exists. -/
theorem exists_max_flow (A : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i j, 0 ≤ A i j) (lam : ℝ)
    (hlam : 0 ≤ lam) :
    ∃ F ∈ FlowSet A lam, ∀ G ∈ FlowSet A lam, totalSum G ≤ totalSum F := by
  have hcont : Continuous (totalSum : Matrix (Fin n) (Fin n) ℝ → ℝ) := by
    unfold totalSum
    fun_prop
  obtain ⟨F, hF, hmax⟩ := (isCompact_flowSet A lam).exists_isMaxOn
    ⟨0, zero_mem_flowSet hA hlam⟩ hcont.continuousOn
  exact ⟨F, hF, fun G hG => isMaxOn_iff.mp hmax G hG⟩

/-! ### Residual reachability -/

/-- Residual reachability for the flow `F` below `A` with parameter `lam`. A row with slack is
reachable; a column `j` is reachable from a reachable row `i` when the edge `(i, j)` is
unsaturated; a row `i` is reachable from a reachable column `j` when `F i j` is positive. -/
inductive Reach (A F : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) : Fin n ⊕ Fin n → Prop
  | slack (i : Fin n) : rowSum F i < lam → Reach A F lam (Sum.inl i)
  | col (i j : Fin n) : Reach A F lam (Sum.inl i) → F i j < A i j → Reach A F lam (Sum.inr j)
  | row (i j : Fin n) : Reach A F lam (Sum.inr j) → 0 < F i j → Reach A F lam (Sum.inl i)

/-- The direction matrix of a residual walk from a row `s` with slack to the vertex `v`:
positive entries only on unsaturated edges, negative entries only on positive edges, row sums
`ind s - (ind i if v = inl i)`, and column sums `ind j if v = inr j`. -/
def AugSpec (A F : Matrix (Fin n) (Fin n) ℝ) (lam : ℝ) (v : Fin n ⊕ Fin n) : Prop :=
  ∃ s : Fin n, rowSum F s < lam ∧ ∃ D : Matrix (Fin n) (Fin n) ℝ,
    (∀ a b, 0 < D a b → F a b < A a b) ∧ (∀ a b, D a b < 0 → 0 < F a b) ∧
    (∀ a, rowSum D a = ind s a - Sum.elim (fun i => ind i a) (fun _ => 0) v) ∧
    (∀ b, colSum D b = Sum.elim (fun _ => 0) (fun j => ind j b) v)

theorem augSpec_of_reach {A F : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ} {v : Fin n ⊕ Fin n}
    (h : Reach A F lam v) : AugSpec A F lam v := by
  induction h with
  | slack i hi =>
    refine ⟨i, hi, 0, fun a b h => by simp at h, fun a b h => by simp at h,
      fun a => ?_, fun b => ?_⟩
    · simp [rowSum]
    · simp [colSum]
  | col i j _ hij ih =>
    obtain ⟨s, hs, D, hpos, hneg, hrow, hcol⟩ := ih
    refine ⟨s, hs, D + single i j, fun a b h => ?_, fun a b h => ?_, fun a => ?_, fun b => ?_⟩
    · rw [Matrix.add_apply, single_apply] at h
      split_ifs at h with hab
      · obtain ⟨rfl, rfl⟩ := hab
        exact hij
      · exact hpos a b (by linarith)
    · rw [Matrix.add_apply, single_apply] at h
      split_ifs at h with hab
      · exact hneg a b (by linarith)
      · exact hneg a b (by linarith)
    · rw [rowSum_add, rowSum_single, hrow a]
      simp
    · rw [colSum_add, colSum_single, hcol b]
      simp
  | row i j _ hij ih =>
    obtain ⟨s, hs, D, hpos, hneg, hrow, hcol⟩ := ih
    refine ⟨s, hs, D - single i j, fun a b h => ?_, fun a b h => ?_, fun a => ?_, fun b => ?_⟩
    · rw [Matrix.sub_apply, single_apply] at h
      split_ifs at h with hab
      · exact hpos a b (by linarith)
      · exact hpos a b (by linarith)
    · rw [Matrix.sub_apply, single_apply] at h
      split_ifs at h with hab
      · obtain ⟨rfl, rfl⟩ := hab
        exact hij
      · exact hneg a b (by linarith)
    · rw [rowSum_sub, rowSum_single, hrow a]
      simp
    · rw [colSum_sub, colSum_single, hcol b]
      simp

/-! ### Augmentation -/

/-- A residual walk into a column with slack produces a flow with a larger total. -/
theorem exists_better_flow {A F : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ} (hF : F ∈ FlowSet A lam)
    {j : Fin n} (hspec : AugSpec A F lam (Sum.inr j)) (hj : colSum F j < lam) :
    ∃ G ∈ FlowSet A lam, totalSum F < totalSum G := by
  obtain ⟨hF0, hFA, hFr, hFc⟩ := hF
  obtain ⟨s, hs, D, hpos, hneg, hrow, hcol⟩ := hspec
  simp only [Sum.elim_inr, sub_zero] at hrow hcol
  have hev : ∀ᶠ eps in 𝓝[>] (0 : ℝ), 0 < eps ∧ eps < lam - rowSum F s ∧
      eps < lam - colSum F j ∧
      ∀ a b, 0 ≤ F a b + eps * D a b ∧ F a b + eps * D a b ≤ A a b := by
    refine eventually_mem_nhdsWithin.and
      (((eventually_lt_nhds (by linarith)).filter_mono nhdsWithin_le_nhds).and
      (((eventually_lt_nhds (by linarith)).filter_mono nhdsWithin_le_nhds).and ?_))
    rw [eventually_all]
    intro a
    rw [eventually_all]
    intro b
    rcases lt_trichotomy (D a b) 0 with hlt | heq | hgt
    · have hq : 0 < F a b / (-D a b) := div_pos (hneg a b hlt) (by linarith)
      filter_upwards [eventually_mem_nhdsWithin,
        (eventually_lt_nhds hq).filter_mono nhdsWithin_le_nhds] with eps heps hlt'
      have heps' : 0 < eps := Set.mem_Ioi.mp heps
      rw [lt_div_iff₀ (by linarith)] at hlt'
      have hprod := mul_neg_of_pos_of_neg heps' hlt
      constructor <;> linarith [hFA a b]
    · refine Eventually.of_forall fun eps => ?_
      rw [heq, mul_zero, add_zero]
      exact ⟨hF0 a b, hFA a b⟩
    · have hq : 0 < (A a b - F a b) / D a b := div_pos (by linarith [hpos a b hgt]) hgt
      filter_upwards [eventually_mem_nhdsWithin,
        (eventually_lt_nhds hq).filter_mono nhdsWithin_le_nhds] with eps heps hlt'
      have heps' : 0 < eps := Set.mem_Ioi.mp heps
      rw [lt_div_iff₀ hgt] at hlt'
      have hprod := mul_pos heps' hgt
      constructor <;> linarith [hF0 a b]
  obtain ⟨eps, heps, hs', hj', hab⟩ := hev.exists
  refine ⟨F + eps • D, ⟨fun a b => ?_, fun a b => ?_, fun a => ?_, fun b => ?_⟩, ?_⟩
  · rw [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
    exact (hab a b).1
  · rw [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
    exact (hab a b).2
  · rw [rowSum_add, rowSum_smul, hrow a]
    unfold ind
    split_ifs with h
    · subst h
      linarith
    · linarith [hFr a]
  · rw [colSum_add, colSum_smul, hcol b]
    unfold ind
    split_ifs with h
    · subst h
      linarith
    · linarith [hFc b]
  · rw [totalSum_add, totalSum_smul, totalSum_eq_sum_rowSum D]
    simp only [hrow, sum_ind]
    linarith

/-- For a maximal flow, every reachable column is saturated. -/
theorem le_colSum_of_reach {A F : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ} (hF : F ∈ FlowSet A lam)
    (hmax : ∀ G ∈ FlowSet A lam, totalSum G ≤ totalSum F) {j : Fin n}
    (h : Reach A F lam (Sum.inr j)) : lam ≤ colSum F j := by
  by_contra hlt
  obtain ⟨G, hG, hFG⟩ := exists_better_flow hF (augSpec_of_reach h) (not_le.mp hlt)
  exact absurd (hmax G hG) (not_le.mpr hFG)

/-! ### Counting at a maximal flow -/

/-- Under the cut condition, a maximal flow has every row sum and column sum equal to `lam`. -/
theorem max_flow_saturated {A : Matrix (Fin n) (Fin n) ℝ} (hA : ∀ i j, 0 ≤ A i j) {lam : ℝ}
    (hlam : 0 < lam)
    (hcut : ∀ I J : Finset (Fin n), n < I.card + J.card →
      lam * ((I.card : ℝ) + (J.card : ℝ) - (n : ℝ)) ≤ cutSum A I J)
    {F : Matrix (Fin n) (Fin n) ℝ} (hF : F ∈ FlowSet A lam)
    (hmax : ∀ G ∈ FlowSet A lam, totalSum G ≤ totalSum F) :
    (∀ i, rowSum F i = lam) ∧ (∀ j, colSum F j = lam) := by
  classical
  obtain ⟨hF0, hFA, hFr, hFc⟩ := hF
  set I : Finset (Fin n) := univ.filter fun i => Reach A F lam (Sum.inl i) with hI
  set J : Finset (Fin n) := univ.filter fun j => Reach A F lam (Sum.inr j) with hJ
  have hJsat : ∀ j ∈ J, colSum F j = lam := fun j hj =>
    le_antisymm (hFc j) (le_colSum_of_reach ⟨hF0, hFA, hFr, hFc⟩ hmax (mem_filter.mp hj).2)
  have hIsat : ∀ i ∉ I, rowSum F i = lam := by
    intro i hi
    refine le_antisymm (hFr i) (not_lt.mp fun h => hi ?_)
    exact mem_filter.mpr ⟨mem_univ _, Reach.slack i h⟩
  have hIJc : ∀ i ∈ I, ∀ j ∉ J, F i j = A i j := by
    intro i hi j hj
    refine le_antisymm (hFA i j) (not_lt.mp fun h => hj ?_)
    exact mem_filter.mpr ⟨mem_univ _, Reach.col i j (mem_filter.mp hi).2 h⟩
  have hIcJ : ∀ i ∉ I, ∀ j ∈ J, F i j = 0 := by
    intro i hi j hj
    refine le_antisymm (not_lt.mp fun h => hi ?_) (hF0 i j)
    exact mem_filter.mpr ⟨mem_univ _, Reach.row i j (mem_filter.mp hj).2 h⟩
  have hcardI : (I.card : ℝ) + (Iᶜ.card : ℝ) = n := by
    have h := Finset.card_add_card_compl I
    rw [Fintype.card_fin] at h
    exact_mod_cast h
  have hcardJ : (J.card : ℝ) + (Jᶜ.card : ℝ) = n := by
    have h := Finset.card_add_card_compl J
    rw [Fintype.card_fin] at h
    exact_mod_cast h
  have h1 : totalSum F = ∑ i ∈ I, rowSum F i + (Iᶜ.card : ℝ) * lam := by
    rw [totalSum_eq_sum_rowSum, ← Finset.sum_add_sum_compl I]
    congr 1
    rw [Finset.sum_congr rfl fun i hi => hIsat i (Finset.mem_compl.mp hi), Finset.sum_const,
      nsmul_eq_mul]
  have h2 : ∑ i ∈ I, rowSum F i = ∑ i ∈ I, ∑ j ∈ J, F i j + cutSum A I Jᶜ := by
    unfold cutSum
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [rowSum, ← Finset.sum_add_sum_compl J]
    congr 1
    exact Finset.sum_congr rfl fun j hj => hIJc i hi j (Finset.mem_compl.mp hj)
  have h3 : ∑ i ∈ I, ∑ j ∈ J, F i j = (J.card : ℝ) * lam := by
    rw [show ∑ i ∈ I, ∑ j ∈ J, F i j = ∑ j ∈ J, ∑ i ∈ I, F i j from Finset.sum_comm]
    have hcolJ : ∀ j ∈ J, ∑ i ∈ I, F i j = lam := by
      intro j hj
      rw [← hJsat j hj, colSum, ← Finset.sum_add_sum_compl I,
        Finset.sum_eq_zero fun i hi => hIcJ i (Finset.mem_compl.mp hi) j hj, add_zero]
    rw [Finset.sum_congr rfl hcolJ, Finset.sum_const, nsmul_eq_mul]
  have hcut0 : 0 ≤ cutSum A I Jᶜ :=
    Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => hA i j
  have htot : lam * n ≤ totalSum F := by
    rw [h1, h2, h3]
    have e1 : lam * (I.card : ℝ) + lam * (Iᶜ.card : ℝ) = lam * n := by
      rw [← mul_add, hcardI]
    have e2 : lam * (J.card : ℝ) + lam * (Jᶜ.card : ℝ) = lam * n := by
      rw [← mul_add, hcardJ]
    by_cases hc : n < I.card + Jᶜ.card
    · have hIJ := hcut I Jᶜ hc
      linarith
    · have hc' : (I.card : ℝ) + (Jᶜ.card : ℝ) ≤ n := by exact_mod_cast not_lt.mp hc
      have hle : lam * ((I.card : ℝ) + (Jᶜ.card : ℝ)) ≤ lam * n :=
        mul_le_mul_of_nonneg_left hc' hlam.le
      linarith
  have hn : ∑ _i : Fin n, lam = n * lam := by
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  constructor
  · intro i
    have hrow_le : ∑ i, rowSum F i ≤ ∑ _i : Fin n, lam := Finset.sum_le_sum fun i _ => hFr i
    have hsum : ∑ i, rowSum F i = ∑ _i : Fin n, lam := by
      rw [totalSum_eq_sum_rowSum] at htot
      linarith
    exact (Finset.sum_eq_sum_iff_of_le fun i _ => hFr i).mp hsum i (mem_univ _)
  · intro j
    have hcol_le : ∑ j, colSum F j ≤ ∑ _j : Fin n, lam := Finset.sum_le_sum fun j _ => hFc j
    have hsum : ∑ j, colSum F j = ∑ _j : Fin n, lam := by
      rw [totalSum_eq_sum_colSum] at htot
      linarith
    exact (Finset.sum_eq_sum_iff_of_le fun j _ => hFc j).mp hsum j (mem_univ _)

/-! ### The theorem -/

theorem hall_domination : HallDomination := by
  intro n _hn A hA lam hlam hcut
  obtain ⟨F, hF, hmax⟩ := exists_max_flow A hA lam hlam.le
  obtain ⟨hrow, hcol⟩ := max_flow_saturated hA hlam hcut hF hmax
  refine ⟨Matrix.of fun i j => F i j / lam, ?_, fun i j => ?_⟩
  · rw [mem_doublyStochastic_iff_sum]
    refine ⟨fun i j => ?_, fun i => ?_, fun j => ?_⟩
    · simp only [Matrix.of_apply]
      exact div_nonneg (hF.1 i j) hlam.le
    · simp only [Matrix.of_apply]
      have h := hrow i
      unfold rowSum at h
      rw [← Finset.sum_div, h, div_self hlam.ne']
    · simp only [Matrix.of_apply]
      have h := hcol j
      unfold colSum at h
      rw [← Finset.sum_div, h, div_self hlam.ne']
  · simp only [Matrix.of_apply]
    rw [mul_div_cancel₀ _ hlam.ne']
    exact hF.2.1 i j

end Dittert
