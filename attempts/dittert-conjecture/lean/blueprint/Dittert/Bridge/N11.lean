import Dittert.Bridge.Common
import Dittert.Scalar.Defs11

/-!
# The dimensional argument for `11 ≤ n ≤ 15`

For a maximizer `A` of `Φ` on `K_n` with a zero entry we derive `False`, following
`attack/hall-n8-n15-branch-coverage/PROOF.md` sections 2 to 5 and the plan in
`Dittert/BRIDGE11-NOTES.md`:

* `λ` is the Hall parameter (`hallLambda`), positive by the localization and at most `1`;
  `u = 1 - λ`; `HallDomination` gives a doubly stochastic `B` with `λ B ≤ A`, so
  `per A ≥ (1 - u)^n per B` and the zero of `A` persists in `B`.
* A minimizing cut `(I, J)` with `a = |Iᶜ|`, `b = |Jᶜ|` is full (`λ = 1`), marginal (exactly one
  of `a`, `b` is zero) or proper. Each case gives `per B ≥ M`, `γ_n - per A ≥ C u²` for the
  constants `M = floor n a b`, `C = curvature n a b` of `Dittert.Scalar.Defs11`, and
  `ScalarCertificates11` says `M (1-u)^n + C u² > γ_n`, contradicting `per A ≤ γ_n`.
* The marginal case with `a = 0` is the case `b = 0` for the transpose.

The dimension is written `n + 1` throughout because `stationarity` is stated on `Fin (n + 1)`.
-/

namespace Dittert

open Matrix Finset BigOperators

variable {n : ℕ}

/-! ### 1. The scalar dictionary: `HallScalar` constants as reals -/

theorem hallScalar_gamma_cast (k : ℕ) : ((HallScalar.gamma k : ℚ) : ℝ) = gamma k := by
  simp [HallScalar.gamma, gamma]

theorem hallScalar_rectangle_cast (n a b : ℕ) :
    ((HallScalar.rectangle n a b : ℚ) : ℝ) = gamma (n - a) * gamma (n - b) / gamma (n - a - b) := by
  simp [HallScalar.rectangle, hallScalar_gamma_cast]

/-- The one-zero floor `κ_n = γ_{n-1}² / γ_{n-2}` as it appears in `GurvitsFloors`, `11 ≤ n ≤ 15`. -/
theorem hallScalar_oneZero_cast (hn11 : 11 ≤ n) (hn15 : n ≤ 15) :
    ((HallScalar.oneZero n : ℚ) : ℝ) = gamma (n - 1) * gamma (n - 1) / gamma (n - 1 - 1) := by
  interval_cases n <;> norm_num [HallScalar.oneZero, gamma, Nat.factorial]

theorem hallScalar_floor_marginal (n a : ℕ) : HallScalar.floor n a 0 = HallScalar.oneZero n := by
  unfold HallScalar.floor
  rw [if_pos (Or.inr rfl)]

theorem hallScalar_floor_proper (n a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b) :
    HallScalar.floor n a b = HallScalar.rectangle n a b := by
  unfold HallScalar.floor
  rw [if_neg (by omega)]

theorem hallScalar_curvature_marginal_cast (hn : 1 ≤ n) (a : ℕ) :
    ((HallScalar.curvature n a 0 : ℚ) : ℝ) =
      7 * n / (16 * ((n : ℝ) - 1)) * (1 + (1 - gamma n) ^ 2) := by
  unfold HallScalar.curvature
  rw [if_pos (Or.inr rfl)]
  push_cast [Nat.cast_sub hn, hallScalar_gamma_cast]
  ring

theorem hallScalar_curvature_proper_cast (a b : ℕ) (ha : 1 ≤ a) (hb : 1 ≤ b) (hab : a + b ≤ n) :
    ((HallScalar.curvature n a b : ℚ) : ℝ) =
      7 * n * ((n : ℝ) - a - b) ^ 2 / (16 * ((a : ℝ) * (n - a) + b * (n - b))) := by
  unfold HallScalar.curvature
  rw [if_neg (by omega)]
  push_cast [Nat.cast_sub (by omega : b ≤ n - a), Nat.cast_sub (by omega : a ≤ n),
    Nat.cast_sub (by omega : b ≤ n)]
  ring

/-! ### 2. Inclusion-exclusion for cuts -/

theorem sum_rowSum_compl (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) :
    ∑ i ∈ Iᶜ, rowSum A i = cutSum A Iᶜ J + cutSum A Iᶜ Jᶜ := by
  unfold cutSum rowSum
  rw [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun i _ => (Finset.sum_add_sum_compl J (A i)).symm

theorem sum_colSum_compl (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) :
    ∑ j ∈ Jᶜ, colSum A j = cutSum A I Jᶜ + cutSum A Iᶜ Jᶜ := by
  unfold cutSum colSum
  calc ∑ j ∈ Jᶜ, ∑ i, A i j = ∑ j ∈ Jᶜ, (∑ i ∈ I, A i j + ∑ i ∈ Iᶜ, A i j) :=
        Finset.sum_congr rfl fun j _ => (Finset.sum_add_sum_compl I fun i => A i j).symm
    _ = ∑ j ∈ Jᶜ, ∑ i ∈ I, A i j + ∑ j ∈ Jᶜ, ∑ i ∈ Iᶜ, A i j := Finset.sum_add_distrib
    _ = ∑ i ∈ I, ∑ j ∈ Jᶜ, A i j + ∑ i ∈ Iᶜ, ∑ j ∈ Jᶜ, A i j := by
        congr 1 <;> exact Finset.sum_comm

theorem totalSum_eq_four_cuts (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) :
    totalSum A = cutSum A I J + cutSum A I Jᶜ + cutSum A Iᶜ J + cutSum A Iᶜ Jᶜ := by
  unfold totalSum cutSum
  rw [← Finset.sum_add_sum_compl I (fun i => ∑ j, A i j)]
  have hI : ∀ i, ∑ j, A i j = ∑ j ∈ J, A i j + ∑ j ∈ Jᶜ, A i j :=
    fun i => (Finset.sum_add_sum_compl J (A i)).symm
  simp only [hI, Finset.sum_add_distrib]
  ring

/-- Inclusion-exclusion: `s_A(I, J) = n - ∑_{Iᶜ} r_i - ∑_{Jᶜ} c_j + s_A(Iᶜ, Jᶜ)`. -/
theorem cutSum_eq_of_feasible (A : Matrix (Fin n) (Fin n) ℝ) (hA : Feasible A) (I J : Finset (Fin n)) :
    cutSum A I J = n - ∑ i ∈ Iᶜ, rowSum A i - ∑ j ∈ Jᶜ, colSum A j + cutSum A Iᶜ Jᶜ := by
  have h1 := sum_rowSum_compl A I J
  have h2 := sum_colSum_compl A I J
  have h3 := totalSum_eq_four_cuts A I J
  rw [hA.2] at h3
  linarith

theorem cutSum_nonneg (A : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i j, 0 ≤ A i j) (I J : Finset (Fin n)) :
    0 ≤ cutSum A I J :=
  Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => hA i j

theorem card_compl_cast (I : Finset (Fin n)) : (Iᶜ.card : ℝ) = n - I.card := by
  rw [Finset.card_compl, Fintype.card_fin,
    Nat.cast_sub (Finset.card_le_univ I |>.trans_eq (Fintype.card_fin n))]

/-! ### 3. Positivity of the Hall parameter at a maximizer -/

/-- The row excess of any subset of at most `n - 1` rows is at most `1/10` in absolute value. -/
theorem row_excess_small (hn8 : 8 ≤ n) (hn15 : n ≤ 15) (A : Matrix (Fin n) (Fin n) ℝ)
    (hA : IsMaximizer A) (S : Finset (Fin n)) (hS : S.card ≤ n - 1) :
    |∑ i ∈ S, rowSum A i - S.card| ≤ 1 / 10 := by
  rcases Nat.eq_zero_or_pos S.card with h0 | hpos
  · rw [Finset.card_eq_zero] at h0
    subst h0
    norm_num
  · exact (localization hn8 hn15 (rowSum A) (rowSum_pos_of_maximizer (by omega) A hA) hA.1.2
      (rowProd_ge (by omega) A hA) S hpos hS).le

theorem col_excess_small (hn8 : 8 ≤ n) (hn15 : n ≤ 15) (A : Matrix (Fin n) (Fin n) ℝ)
    (hA : IsMaximizer A) (S : Finset (Fin n)) (hS : S.card ≤ n - 1) :
    |∑ j ∈ S, colSum A j - S.card| ≤ 1 / 10 := by
  rcases Nat.eq_zero_or_pos S.card with h0 | hpos
  · rw [Finset.card_eq_zero] at h0
    subst h0
    norm_num
  · exact (localization hn8 hn15 (colSum A) (colSum_pos_of_maximizer (by omega) A hA)
      (by rw [← totalSum_eq_sum_colSum]; exact hA.1.2) (colProd_ge (by omega) A hA) S hpos hS).le

/-- Every cut sum of a maximizer is positive: `s_A(I, J) = p - e - f + t > p - 1/5 > 0`. -/
theorem cutSum_pos_of_maximizer (hn8 : 8 ≤ n) (hn15 : n ≤ 15) (A : Matrix (Fin n) (Fin n) ℝ)
    (hA : IsMaximizer A) (I J : Finset (Fin n)) (hIJ : n < I.card + J.card) : 0 < cutSum A I J := by
  have hIn : I.card ≤ n := (Finset.card_le_univ I).trans_eq (Fintype.card_fin n)
  have hJn : J.card ≤ n := (Finset.card_le_univ J).trans_eq (Fintype.card_fin n)
  have hie := cutSum_eq_of_feasible A hA.1 I J
  have hI := row_excess_small hn8 hn15 A hA Iᶜ (by rw [Finset.card_compl, Fintype.card_fin]; omega)
  have hJ := col_excess_small hn8 hn15 A hA Jᶜ (by rw [Finset.card_compl, Fintype.card_fin]; omega)
  rw [card_compl_cast] at hI hJ
  have ht := cutSum_nonneg A hA.1.1 Iᶜ Jᶜ
  have hp : (n : ℝ) + 1 ≤ I.card + J.card := by exact_mod_cast hIJ
  have hI' := (abs_le.mp hI).2
  have hJ' := (abs_le.mp hJ).2
  linarith

theorem hallLambda_pos (hn8 : 8 ≤ n) (hn15 : n ≤ 15) (A : Matrix (Fin n) (Fin n) ℝ)
    (hA : IsMaximizer A) : 0 < hallLambda (by omega) A := by
  obtain ⟨p, hp, hmin⟩ := exists_min_cut (by omega) A
  rw [← hmin]
  unfold cutRatio
  have hp' := mem_cuts.mp hp
  apply div_pos (cutSum_pos_of_maximizer hn8 hn15 A hA p.1 p.2 hp')
  have : (n : ℝ) < p.1.card + p.2.card := by exact_mod_cast hp'
  linarith

/-! ### 4. Cuts with all columns, and transposition -/

/-- A cut with all columns has ratio the average row sum over `I`. -/
theorem cutRatio_row_cut (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) (hJ : Jᶜ = ∅) :
    cutRatio A (I, J) = (∑ i ∈ I, rowSum A i) / I.card := by
  have hJc : (J.card : ℝ) = n := by
    have h := Finset.card_add_card_compl J
    rw [hJ, Finset.card_empty, Fintype.card_fin, add_zero] at h
    exact_mod_cast h
  have hrow : ∀ i, ∑ j ∈ J, A i j = rowSum A i := by
    intro i
    have h := Finset.sum_add_sum_compl J (A i)
    rw [hJ, Finset.sum_empty, add_zero] at h
    exact h
  unfold cutRatio cutSum
  simp only [hJc, hrow]
  congr 1
  ring

/-- The cut `({i}, univ)` has ratio `r_i`. -/
theorem cutRatio_singleton_row (A : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) :
    cutRatio A ({i}, Finset.univ) = rowSum A i := by
  rw [cutRatio_row_cut A {i} Finset.univ (by simp), Finset.sum_singleton, Finset.card_singleton]
  simp

theorem singleton_row_mem_cuts (i : Fin n) : ({i}, (Finset.univ : Finset (Fin n))) ∈ cuts n := by
  rw [mem_cuts]
  simp only [Finset.card_singleton, Finset.card_univ, Fintype.card_fin]
  omega

/-- A minimizing cut with all columns is attained by a single row: some `r_{i0} = λ`. -/
theorem exists_row_eq_hallLambda (hn : 1 ≤ n) (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n))
    (hJ : Jᶜ = ∅) (hIJ : (I, J) ∈ cuts n) (hmin : cutRatio A (I, J) = hallLambda hn A) :
    ∃ i0, rowSum A i0 = hallLambda hn A := by
  have hJn : J.card ≤ n := (Finset.card_le_univ J).trans_eq (Fintype.card_fin n)
  have hI : I.Nonempty := by
    rw [← Finset.card_pos]
    have hc := mem_cuts.mp hIJ
    simp only at hc
    omega
  have hIc : (0 : ℝ) < I.card := by exact_mod_cast hI.card_pos
  rw [cutRatio_row_cut A I J hJ, div_eq_iff hIc.ne'] at hmin
  have hsum : ∑ i ∈ I, rowSum A i ≤ ∑ i ∈ I, hallLambda hn A := by
    rw [Finset.sum_const, nsmul_eq_mul, hmin]
    ring_nf
    exact le_refl _
  obtain ⟨i0, _, hle⟩ := Finset.exists_le_of_sum_le hI hsum
  refine ⟨i0, le_antisymm hle ?_⟩
  rw [← cutRatio_singleton_row A i0]
  exact hallLambda_le_cutRatio hn A _ (singleton_row_mem_cuts i0)

theorem cutRatio_transpose (A : Matrix (Fin n) (Fin n) ℝ) (p : Finset (Fin n) × Finset (Fin n)) :
    cutRatio Aᵀ (p.2, p.1) = cutRatio A p := by
  unfold cutRatio cutSum
  simp only [Matrix.transpose_apply]
  congr 1
  · exact Finset.sum_comm
  · ring

theorem swap_mem_cuts {p : Finset (Fin n) × Finset (Fin n)} : (p.2, p.1) ∈ cuts n ↔ p ∈ cuts n := by
  simp only [mem_cuts]
  omega

theorem hallLambda_transpose (hn : 1 ≤ n) (A : Matrix (Fin n) (Fin n) ℝ) :
    hallLambda hn Aᵀ = hallLambda hn A := by
  have key : ∀ M : Matrix (Fin n) (Fin n) ℝ, hallLambda hn Mᵀ ≤ hallLambda hn M := by
    intro M
    unfold hallLambda
    apply Finset.le_inf'
    intro p hp
    rw [← cutRatio_transpose M p]
    exact hallLambda_le_cutRatio hn Mᵀ (p.2, p.1) (swap_mem_cuts.mpr hp)
  refine le_antisymm (key A) ?_
  have := key Aᵀ
  rwa [Matrix.transpose_transpose] at this

/-! ### 5. The three cut cases -/

/-- The common data of every case: `n + 1 ∈ [11, 15]`, a maximizer with a zero entry, the Hall
parameter `λ ∈ (0, 1]`, the dominated doubly stochastic `B` with the persisting zero. -/
structure CaseData (n : ℕ) where
  A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ
  hA : IsMaximizer A
  i₀ : Fin (n + 1)
  j₀ : Fin (n + 1)
  h0 : A i₀ j₀ = 0
  B : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ
  hB : B ∈ doublyStochastic ℝ (Fin (n + 1))
  hAB : ∀ i j, hallLambda (Nat.succ_pos n) A * B i j ≤ A i j

theorem hn1 (n : ℕ) : 1 ≤ n + 1 := Nat.succ_pos n

/-- The final scalar contradiction. -/
theorem scalar_contradiction (P M C u γ : ℝ) (N : ℕ) (hP : M * (1 - u) ^ N ≤ P)
    (hδ : C * u ^ 2 ≤ γ - P) (hcert : 0 < C * u ^ 2 + M * (1 - u) ^ N - γ) : False := by
  linarith

/-- The persisting zero gives `per B ≥ κ_{n+1}` (the one-zero floor). -/
theorem permanent_B_ge_oneZero (hF : GurvitsFloors) (hn11 : 11 ≤ n + 1) (hn15 : n + 1 ≤ 15)
    (D : CaseData n) (hl : 0 < hallLambda (hn1 n) D.A) :
    ((HallScalar.oneZero (n + 1) : ℚ) : ℝ) ≤ D.B.permanent := by
  have hB0 : ∀ i j, 0 ≤ D.B i j := fun _ _ => nonneg_of_mem_doublyStochastic D.hB
  have hBz : D.B D.i₀ D.j₀ = 0 := zero_of_dominated D.A D.B _ hl hB0 D.hAB D.i₀ D.j₀ D.h0
  rw [hallScalar_oneZero_cast hn11 hn15]
  refine (hF (n + 1) (hn1 n) D.B D.hB).2 1 1 le_rfl le_rfl (by omega) {D.i₀} {D.j₀}
    (Finset.card_singleton _) (Finset.card_singleton _) ?_
  intro i hi j hj
  rw [Finset.mem_singleton] at hi hj
  rw [hi, hj]
  exact hBz

/-- The full case: `λ = 1` is impossible. -/
theorem full_case (hF : GurvitsFloors) (hS : ScalarCertificates11) (hn11 : 11 ≤ n + 1)
    (hn15 : n + 1 ≤ 15) (D : CaseData n) (hl : hallLambda (hn1 n) D.A = 1) : False := by
  have hB0 : ∀ i j, 0 ≤ D.B i j := fun _ _ => nonneg_of_mem_doublyStochastic D.hB
  have hPB := permanent_ge_of_dominated D.A D.B _ (by rw [hl]; norm_num) hB0 D.hAB
  rw [hl, one_pow, one_mul] at hPB
  have hfloor := permanent_B_ge_oneZero hF hn11 hn15 D (by rw [hl]; norm_num)
  have hPγ := permanent_le_gamma_of_maximizer (hn1 n) D.A D.hA
  have hcert := hS (n + 1) 1 0 hn11 hn15 (by omega) (by omega) 0 (by norm_num)
  rw [hallScalar_floor_marginal, hallScalar_gamma_cast] at hcert
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, mul_zero, sub_zero, one_pow,
    mul_one, zero_add] at hcert
  linarith

/-- The stationarity identity summed along row `i0` with weights `a_{i0 j}`:
`R + C q - P = r_{i0} Φ` with `q = ∑_j a_{i0 j} / c_j`. -/
theorem row_stationarity_sum (hn : 2 ≤ n + 1) (A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (hA : IsMaximizer A) (i0 : Fin (n + 1)) :
    (∏ r, rowSum A r) + (∏ c, colSum A c) * (∑ j, A i0 j / colSum A j) - A.permanent
      = rowSum A i0 * Phi A := by
  have hr : rowSum A i0 ≠ 0 := (rowSum_pos_of_maximizer hn A hA i0).ne'
  have hkey : ∀ j, A i0 j * ((∏ r, rowSum A r) / rowSum A i0 + (∏ c, colSum A c) / colSum A j
      - (minor A i0 j).permanent) = A i0 j * Phi A := by
    intro j
    rcases (hA.1.1 i0 j).lt_or_eq with h | h
    · rw [stationarity hn A hA i0 j h]
    · rw [← h, zero_mul, zero_mul]
  have hsum := Finset.sum_congr rfl fun j (_ : j ∈ Finset.univ) => hkey j
  rw [← Finset.sum_mul] at hsum
  simp only [mul_add, mul_sub, Finset.sum_add_distrib, Finset.sum_sub_distrib] at hsum
  have e1 : ∑ j, A i0 j * ((∏ r, rowSum A r) / rowSum A i0) = ∏ r, rowSum A r := by
    rw [← Finset.sum_mul]
    change rowSum A i0 * _ = _
    field_simp
  have e2 : ∑ j, A i0 j * ((∏ c, colSum A c) / colSum A j) =
      (∏ c, colSum A c) * ∑ j, A i0 j / colSum A j := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  have e3 : ∑ j, A i0 j * (minor A i0 j).permanent = A.permanent := (permanent_expand_row A i0).symm
  rw [e1, e2, e3] at hsum
  exact hsum

/-- The marginal case with all columns: a row `i0` with `r_{i0} = λ` is impossible. -/
theorem marginal_case (hF : GurvitsFloors) (hS : ScalarCertificates11) (hn11 : 11 ≤ n + 1)
    (hn15 : n + 1 ≤ 15) (D : CaseData n) (hl : 0 < hallLambda (hn1 n) D.A)
    (hl1 : hallLambda (hn1 n) D.A ≤ 1) (i0 : Fin (n + 1))
    (hr0 : rowSum D.A i0 = hallLambda (hn1 n) D.A) : False := by
  have hn2 : 2 ≤ n + 1 := by omega
  have hn8 : 8 ≤ n + 1 := by omega
  obtain ⟨A, hA, i₀, j₀, h0, B, hB, hAB⟩ := D
  simp only at hl hl1 hr0
  set lam := hallLambda (hn1 n) A with hlam
  set u := 1 - lam with hu
  have hu0 : 0 ≤ u := by linarith
  have hu1 : u ≤ 1 := by linarith
  set γ := gamma (n + 1) with hγ
  have hγ1 : γ < 1 := gamma_lt_one hn2
  set R := ∏ r, rowSum A r with hR
  set C := ∏ c, colSum A c with hC
  set P := A.permanent with hP
  have hΦ : Phi A = R + C - P := rfl
  have hΦge : 2 - γ ≤ Phi A := phi_maximizer_ge (hn1 n) A hA
  have hR1 : R ≤ 1 := rowProd_le_one A hA.1
  have hC1 : C ≤ 1 := colProd_le_one A hA.1
  have hC0 : 0 < C := Finset.prod_pos fun c _ => colSum_pos_of_maximizer hn2 A hA c
  have hP0 : 0 ≤ P := permanent_nonneg A hA.1.1
  have hPγ : P ≤ γ := permanent_le_gamma_of_maximizer (hn1 n) A hA
  have hbudget := deficit_budget (hn1 n) A hA
  -- the weighted stationarity sum
  set q := ∑ j, A i0 j / colSum A j with hq
  have hsum := row_stationarity_sum hn2 A hA i0
  rw [hr0, hΦ] at hsum
  -- q > 0
  have hex : ∃ j, 0 < A i0 j := by
    by_contra hcon
    push Not at hcon
    have : rowSum A i0 = 0 := Finset.sum_eq_zero fun j _ => le_antisymm (hcon j) (hA.1.1 i0 j)
    linarith
  obtain ⟨j₁, hj₁⟩ := hex
  have hq0 : 0 < q := by
    refine lt_of_lt_of_le (div_pos hj₁ (colSum_pos_of_maximizer hn2 A hA j₁)) ?_
    exact Finset.single_le_sum
      (fun j _ => div_nonneg (hA.1.1 i0 j) (colSum_pos_of_maximizer hn2 A hA j).le) (Finset.mem_univ j₁)
  -- q ≤ E(u) = 1 - (2 - γ) u
  have hRP : 1 - γ ≤ R - P := by linarith
  have hCq : C * q ≤ C * (1 - (2 - γ) * u) := by
    have h3 : u * (C * (1 - γ)) ≤ u * (R - P) :=
      mul_le_mul_of_nonneg_left (by nlinarith) hu0
    have h4 : C * q = (1 - u) * (R + C - P) - (R - P) := by rw [hu]; linarith
    nlinarith
  have hqE : q ≤ 1 - (2 - γ) * u := le_of_mul_le_mul_left hCq hC0
  have hE0 : 0 < 1 - (2 - γ) * u := lt_of_lt_of_le hq0 hqE
  -- a column `j` with `a_{i0 j} > 0` and `c_j ≥ λ / q`
  have hstrict : ∀ j, 0 < A i0 j → colSum A j < lam / q → A i0 j * (q / lam) < A i0 j / colSum A j := by
    intro j hj hcj
    have hc := colSum_pos_of_maximizer hn2 A hA j
    rw [lt_div_iff₀ hq0] at hcj
    rw [lt_div_iff₀ hc]
    have h1 : q / lam * colSum A j < 1 := by
      rw [div_mul_eq_mul_div, div_lt_one hl]
      linarith
    calc A i0 j * (q / lam) * colSum A j = A i0 j * (q / lam * colSum A j) := by ring
      _ < A i0 j * 1 := mul_lt_mul_of_pos_left h1 hj
      _ = A i0 j := mul_one _
  have hcol : ∃ j, 0 < A i0 j ∧ lam / q ≤ colSum A j := by
    by_contra hcon
    push Not at hcon
    have hlt : ∑ j, A i0 j * (q / lam) < ∑ j, A i0 j / colSum A j := by
      apply Finset.sum_lt_sum
      · intro j _
        rcases (hA.1.1 i0 j).lt_or_eq with h | h
        · exact (hstrict j h (hcon j h)).le
        · rw [← h, zero_mul, zero_div]
      · exact ⟨j₁, Finset.mem_univ _, hstrict j₁ hj₁ (hcon j₁ hj₁)⟩
    rw [← Finset.sum_mul] at hlt
    have : (∑ j, A i0 j) * (q / lam) = q := by
      change rowSum A i0 * _ = _
      rw [hr0]
      field_simp
    linarith
  obtain ⟨j, hj, hcj⟩ := hcol
  have hcj' : 1 + (1 - γ) * u ≤ colSum A j := by
    have h6 : lam / (1 - (2 - γ) * u) ≤ lam / q := div_le_div_of_nonneg_left hl.le hq0 hqE
    have h7 : 1 + (1 - γ) * u ≤ lam / (1 - (2 - γ) * u) := by
      rw [le_div_iff₀ hE0, hu]
      nlinarith [mul_nonneg (mul_nonneg (sub_nonneg.mpr hγ1.le) (by linarith : (0 : ℝ) ≤ 2 - γ))
        (sq_nonneg u)]
    linarith
  -- the deficit bounds on the singleton row and the singleton column
  have hD1 := deficit_bound hn8 hn15 (rowSum A) (rowSum_pos_of_maximizer hn2 A hA) hA.1.2
    (rowProd_ge (hn1 n) A hA) {i0} (by simp) (by simp; omega)
  have hD2 := deficit_bound hn8 hn15 (colSum A) (colSum_pos_of_maximizer hn2 A hA)
    (by rw [← totalSum_eq_sum_colSum]; exact hA.1.2) (colProd_ge (hn1 n) A hA) {j} (by simp)
    (by simp; omega)
  simp only [Finset.sum_singleton, Finset.card_singleton, Nat.cast_one, mul_one] at hD1 hD2
  rw [hr0] at hD1
  set K := 7 * ((n + 1 : ℕ) : ℝ) / (16 * (((n + 1 : ℕ) : ℝ) - 1)) with hK
  have hK0 : 0 ≤ K := by
    rw [hK]
    have : (1 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by exact_mod_cast (by omega : 1 ≤ n + 1)
    apply div_nonneg (by positivity)
    linarith
  have hsq : ((1 - γ) * u) ^ 2 ≤ (colSum A j - 1) ^ 2 :=
    pow_le_pow_left₀ (mul_nonneg (sub_nonneg.mpr hγ1.le) hu0) (by linarith) 2
  have hD2' : K * ((1 - γ) * u) ^ 2 ≤ 1 - C := le_trans (mul_le_mul_of_nonneg_left hsq hK0) hD2
  have hlam_u : lam - 1 = -u := by rw [hu]; ring
  rw [hlam_u, neg_sq] at hD1
  -- per B ≥ κ, per A ≥ (1 - u)^(n+1) per B
  have hB0 : ∀ i j, 0 ≤ B i j := fun _ _ => nonneg_of_mem_doublyStochastic hB
  have hPB := permanent_ge_of_dominated A B lam hl.le hB0 hAB
  have hfloor := permanent_B_ge_oneZero hF hn11 hn15 ⟨A, hA, i₀, j₀, h0, B, hB, hAB⟩ hl
  simp only at hfloor
  have hpow : 0 ≤ lam ^ (n + 1) := pow_nonneg hl.le _
  have hM : ((HallScalar.oneZero (n + 1) : ℚ) : ℝ) * (1 - u) ^ (n + 1) ≤ P := by
    have : (1 - u) = lam := by rw [hu]; ring
    rw [this]
    nlinarith [mul_le_mul_of_nonneg_left hfloor hpow]
  -- the certificate
  have hcert := hS (n + 1) (n + 1 - 1) 0 hn11 hn15 (by omega) (by omega) u hu1
  rw [hallScalar_floor_marginal, hallScalar_gamma_cast, hallScalar_curvature_marginal_cast (hn1 n)]
    at hcert
  rw [← hK] at hcert
  have hδ : K * (1 + (1 - γ) ^ 2) * u ^ 2 ≤ γ - P := by
    have : K * (1 + (1 - γ) ^ 2) * u ^ 2 = K * u ^ 2 + K * ((1 - γ) * u) ^ 2 := by ring
    rw [this]
    linarith
  exact scalar_contradiction P _ _ u γ (n + 1) hM hδ hcert

/-- Weighted Cauchy-Schwarz: `(e + f)² / (α + β) ≤ e²/α + f²/β`. -/
theorem sq_add_div_le (e f α β : ℝ) (hα : 0 < α) (hβ : 0 < β) :
    (e + f) ^ 2 / (α + β) ≤ e ^ 2 / α + f ^ 2 / β := by
  have key : e ^ 2 / α + f ^ 2 / β - (e + f) ^ 2 / (α + β) =
      (e * β - f * α) ^ 2 / (α * β * (α + β)) := by
    field_simp
    ring
  have : 0 ≤ (e * β - f * α) ^ 2 / (α * β * (α + β)) := by positivity
  linarith

/-- The proper case: a minimizing cut omitting `a ≥ 1` rows and `b ≥ 1` columns is impossible. -/
theorem proper_case (hF : GurvitsFloors) (hS : ScalarCertificates11) (hn11 : 11 ≤ n + 1)
    (hn15 : n + 1 ≤ 15) (D : CaseData n) (hl : 0 < hallLambda (hn1 n) D.A)
    (hl1 : hallLambda (hn1 n) D.A ≤ 1) (I J : Finset (Fin (n + 1))) (hIJ : (I, J) ∈ cuts (n + 1))
    (hmin : cutRatio D.A (I, J) = hallLambda (hn1 n) D.A) (ha : 1 ≤ Iᶜ.card) (hb : 1 ≤ Jᶜ.card) :
    False := by
  have hn2 : 2 ≤ n + 1 := by omega
  have hn8 : 8 ≤ n + 1 := by omega
  obtain ⟨A, hA, i₀, j₀, h0, B, hB, hAB⟩ := D
  simp only at hl hl1 hmin
  -- the sizes
  obtain ⟨a, ha_def⟩ : ∃ a, Iᶜ.card = a := ⟨_, rfl⟩
  obtain ⟨b, hb_def⟩ : ∃ b, Jᶜ.card = b := ⟨_, rfl⟩
  rw [ha_def] at ha
  rw [hb_def] at hb
  have hIn : I.card ≤ n + 1 := (Finset.card_le_univ I).trans_eq (Fintype.card_fin _)
  have hJn : J.card ≤ n + 1 := (Finset.card_le_univ J).trans_eq (Fintype.card_fin _)
  have hIa : I.card + a = n + 1 := by
    have := Finset.card_add_card_compl I
    rw [Fintype.card_fin, ha_def] at this
    exact this
  have hJb : J.card + b = n + 1 := by
    have := Finset.card_add_card_compl J
    rw [Fintype.card_fin, hb_def] at this
    exact this
  have hcut := mem_cuts.mp hIJ
  simp only at hcut
  have hab : a + b ≤ n + 1 - 1 := by omega
  have hab' : a + b + 1 ≤ n + 1 := by omega
  -- real forms of the sizes
  have hIa' : (I.card : ℝ) = ((n + 1 : ℕ) : ℝ) - a := by
    have : ((I.card + a : ℕ) : ℝ) = ((n + 1 : ℕ) : ℝ) := by rw [hIa]
    push_cast at this ⊢
    linarith
  have hJb' : (J.card : ℝ) = ((n + 1 : ℕ) : ℝ) - b := by
    have : ((J.card + b : ℕ) : ℝ) = ((n + 1 : ℕ) : ℝ) := by rw [hJb]
    push_cast at this ⊢
    linarith
  have ha1 : (1 : ℝ) ≤ a := by exact_mod_cast ha
  have hb1 : (1 : ℝ) ≤ b := by exact_mod_cast hb
  have hab1 : (a : ℝ) + b + 1 ≤ ((n + 1 : ℕ) : ℝ) := by exact_mod_cast hab'
  -- the zero block of `B`, the floor, the domination
  have hblock := zero_block_of_min_cut (hn1 n) A B hA.1.1 hB hl hAB I J hIJ hmin
  have hfloor := (hF (n + 1) (hn1 n) B hB).2 a b ha hb hab Iᶜ Jᶜ ha_def hb_def hblock
  have hB0 : ∀ i j, 0 ≤ B i j := fun _ _ => nonneg_of_mem_doublyStochastic hB
  have hPB := permanent_ge_of_dominated A B _ hl.le hB0 hAB
  have hpow : 0 ≤ hallLambda (hn1 n) A ^ (n + 1) := pow_nonneg hl.le _
  -- the budget and the deficit bounds on `Iᶜ` and `Jᶜ`
  have hPγ := permanent_le_gamma_of_maximizer (hn1 n) A hA
  have hbudget := deficit_budget (hn1 n) A hA
  have hD1 := deficit_bound hn8 hn15 (rowSum A) (rowSum_pos_of_maximizer hn2 A hA) hA.1.2
    (rowProd_ge (hn1 n) A hA) Iᶜ (by omega) (by omega)
  have hD2 := deficit_bound hn8 hn15 (colSum A) (colSum_pos_of_maximizer hn2 A hA)
    (by rw [← totalSum_eq_sum_colSum]; exact hA.1.2) (colProd_ge (hn1 n) A hA) Jᶜ (by omega)
    (by omega)
  rw [ha_def] at hD1
  rw [hb_def] at hD2
  -- inclusion-exclusion
  have ht := cutSum_nonneg A hA.1.1 Iᶜ Jᶜ
  have hie := cutSum_eq_of_feasible A hA.1 I J
  have hAIJ : cutSum A I J = hallLambda (hn1 n) A * (((n + 1 : ℕ) : ℝ) - a - b) := by
    unfold cutRatio at hmin
    simp only at hmin
    rw [div_eq_iff (by rw [hIa', hJb']; apply ne_of_gt; linarith)] at hmin
    rw [hmin, hIa', hJb']
    ring
  -- the certificate
  have hcert := hS (n + 1) a b hn11 hn15 (by omega) (by omega) (1 - hallLambda (hn1 n) A)
    (by linarith)
  rw [hallScalar_floor_proper _ _ _ ha hb, hallScalar_rectangle_cast, hallScalar_gamma_cast,
    hallScalar_curvature_proper_cast (n := n + 1) a b ha hb (by omega)] at hcert
  -- abbreviations
  set N : ℝ := ((n + 1 : ℕ) : ℝ) with hN
  set lam := hallLambda (hn1 n) A with hlam
  set u := 1 - lam with hu
  set γ := gamma (n + 1) with hγ
  set R := ∏ r, rowSum A r with hR
  set C := ∏ c, colSum A c with hC
  set P := A.permanent with hP
  set e := ∑ i ∈ Iᶜ, rowSum A i - a with he
  set f := ∑ j ∈ Jᶜ, colSum A j - b with hf
  set ν := gamma (n + 1 - a) * gamma (n + 1 - b) / gamma (n + 1 - a - b) with hν
  have hu0 : 0 ≤ u := by linarith
  have hlu : lam = 1 - u := by rw [hu]; ring
  have hp0 : 0 < N - a - b := by linarith
  have hpu : (N - a - b) * u ≤ e + f := by
    have : (N - a - b) * u = e + f - cutSum A Iᶜ Jᶜ := by
      rw [hu, he, hf]
      linarith
    linarith
  have ha0 : (a : ℝ) ≠ 0 := ne_of_gt (by linarith)
  have hb0 : (b : ℝ) ≠ 0 := ne_of_gt (by linarith)
  have hNa : N - a ≠ 0 := ne_of_gt (by linarith)
  have hNb : N - b ≠ 0 := ne_of_gt (by linarith)
  have hα : 0 < (a : ℝ) * (N - a) := mul_pos (by linarith) (by linarith)
  have hβ : 0 < (b : ℝ) * (N - b) := mul_pos (by linarith) (by linarith)
  have hD1' : 7 * N / 16 * (e ^ 2 / ((a : ℝ) * (N - a))) ≤ 1 - R := by
    have : 7 * N / (16 * (a : ℝ) * (N - a)) * e ^ 2 = 7 * N / 16 * (e ^ 2 / ((a : ℝ) * (N - a))) := by
      field_simp
    rw [← this]
    exact hD1
  have hD2' : 7 * N / 16 * (f ^ 2 / ((b : ℝ) * (N - b))) ≤ 1 - C := by
    have : 7 * N / (16 * (b : ℝ) * (N - b)) * f ^ 2 = 7 * N / 16 * (f ^ 2 / ((b : ℝ) * (N - b))) := by
      field_simp
    rw [← this]
    exact hD2
  have hcs := sq_add_div_le e f _ _ hα hβ
  have hef : ((N - a - b) * u) ^ 2 ≤ (e + f) ^ 2 :=
    pow_le_pow_left₀ (mul_nonneg hp0.le hu0) hpu 2
  have hden : 0 < (a : ℝ) * (N - a) + b * (N - b) := by linarith
  have h3 : 0 ≤ 7 * N / 16 := by positivity
  have hδ : 7 * N * (N - a - b) ^ 2 / (16 * ((a : ℝ) * (N - a) + b * (N - b))) * u ^ 2 ≤ γ - P := by
    calc 7 * N * (N - a - b) ^ 2 / (16 * ((a : ℝ) * (N - a) + b * (N - b))) * u ^ 2
        = 7 * N / 16 * (((N - a - b) * u) ^ 2 / ((a : ℝ) * (N - a) + b * (N - b))) := by
          field_simp
      _ ≤ 7 * N / 16 * ((e + f) ^ 2 / ((a : ℝ) * (N - a) + b * (N - b))) :=
          mul_le_mul_of_nonneg_left (div_le_div_of_nonneg_right hef hden.le) h3
      _ ≤ 7 * N / 16 * (e ^ 2 / ((a : ℝ) * (N - a)) + f ^ 2 / ((b : ℝ) * (N - b))) :=
          mul_le_mul_of_nonneg_left hcs h3
      _ = 7 * N / 16 * (e ^ 2 / ((a : ℝ) * (N - a))) + 7 * N / 16 * (f ^ 2 / ((b : ℝ) * (N - b))) := by
          ring
      _ ≤ (1 - R) + (1 - C) := add_le_add hD1' hD2'
      _ ≤ γ - P := hbudget
  have hM : ν * (1 - u) ^ (n + 1) ≤ P := by
    rw [← hlu]
    calc ν * lam ^ (n + 1) = lam ^ (n + 1) * ν := by ring
      _ ≤ lam ^ (n + 1) * B.permanent := mul_le_mul_of_nonneg_left hfloor hpow
      _ ≤ P := hPB
  exact scalar_contradiction P ν _ u γ (n + 1) hM hδ hcert

/-! ### 6. Assembly: no maximizer has a zero entry -/

/-- The row-cut reduction: from a minimizing cut with all columns to a row `i0` with `r_{i0} = λ`. -/
theorem marginal_case_of_cut (hF : GurvitsFloors) (hS : ScalarCertificates11) (hn11 : 11 ≤ n + 1)
    (hn15 : n + 1 ≤ 15) (D : CaseData n) (hl : 0 < hallLambda (hn1 n) D.A)
    (hl1 : hallLambda (hn1 n) D.A ≤ 1) (I J : Finset (Fin (n + 1))) (hJ : Jᶜ = ∅)
    (hIJ : (I, J) ∈ cuts (n + 1)) (hmin : cutRatio D.A (I, J) = hallLambda (hn1 n) D.A) : False := by
  obtain ⟨i0, hi0⟩ := exists_row_eq_hallLambda (hn1 n) D.A I J hJ hIJ hmin
  exact marginal_case hF hS hn11 hn15 D hl hl1 i0 hi0

/-- The transposed case data. -/
def CaseData.transpose (D : CaseData n) : CaseData n where
  A := D.Aᵀ
  hA := (isMaximizer_transpose D.A).mpr D.hA
  i₀ := D.j₀
  j₀ := D.i₀
  h0 := by rw [Matrix.transpose_apply]; exact D.h0
  B := D.Bᵀ
  hB := transpose_mem_doublyStochastic_iff.mpr D.hB
  hAB := fun i j => by
    rw [Matrix.transpose_apply, Matrix.transpose_apply, hallLambda_transpose]
    exact D.hAB j i

/-- A maximizer in dimension `n + 1 ∈ [11, 15]` with a zero entry does not exist. -/
theorem no_zero_of_maximizer (hH : HallDomination) (hF : GurvitsFloors) (hS : ScalarCertificates11)
    (hn11 : 11 ≤ n + 1) (hn15 : n + 1 ≤ 15) (A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (hA : IsMaximizer A) (i₀ j₀ : Fin (n + 1)) (h0 : A i₀ j₀ = 0) : False := by
  have hn8 : 8 ≤ n + 1 := by omega
  have hl : 0 < hallLambda (hn1 n) A := hallLambda_pos hn8 hn15 A hA
  have hl1 : hallLambda (hn1 n) A ≤ 1 := hallLambda_le_one (hn1 n) A hA.1
  obtain ⟨B, hB, hAB⟩ := hH (n + 1) (hn1 n) A hA.1.1 _ hl
    (fun I J hIJ => cut_condition_hallLambda (hn1 n) A hA.1.1 I J hIJ)
  let D : CaseData n := ⟨A, hA, i₀, j₀, h0, B, hB, hAB⟩
  by_cases hfull : hallLambda (hn1 n) A = 1
  · exact full_case hF hS hn11 hn15 D hfull
  obtain ⟨⟨I, J⟩, hIJ, hmin⟩ := exists_min_cut (hn1 n) A
  by_cases ha0 : Iᶜ.card = 0
  · have hI : Iᶜ = ∅ := Finset.card_eq_zero.mp ha0
    by_cases hb0 : Jᶜ.card = 0
    · -- the full cut: ratio `1`
      have hJ : Jᶜ = ∅ := Finset.card_eq_zero.mp hb0
      exfalso
      apply hfull
      rw [← hmin, cutRatio_row_cut A I J hJ]
      have hIc : (I.card : ℝ) = (n + 1 : ℕ) := by
        have h := Finset.card_add_card_compl I
        rw [hI, Finset.card_empty, Fintype.card_fin, add_zero] at h
        exact_mod_cast h
      have hrows : ∑ i ∈ I, rowSum A i = ((n + 1 : ℕ) : ℝ) := by
        have h := Finset.sum_add_sum_compl I (rowSum A)
        rw [hI, Finset.sum_empty, add_zero] at h
        rw [h]
        exact hA.1.2
      rw [hrows, hIc, div_self (by positivity)]
    · -- all rows, `b ≥ 1` columns omitted: transpose
      have hmin' : cutRatio D.transpose.A (J, I) = hallLambda (hn1 n) D.transpose.A := by
        show cutRatio Aᵀ (J, I) = hallLambda (hn1 n) Aᵀ
        rw [hallLambda_transpose]
        exact (cutRatio_transpose A (I, J)).trans hmin
      have hl' : 0 < hallLambda (hn1 n) D.transpose.A := by
        show 0 < hallLambda (hn1 n) Aᵀ
        rw [hallLambda_transpose]; exact hl
      have hl1' : hallLambda (hn1 n) D.transpose.A ≤ 1 := by
        show hallLambda (hn1 n) Aᵀ ≤ 1
        rw [hallLambda_transpose]; exact hl1
      exact marginal_case_of_cut hF hS hn11 hn15 D.transpose hl' hl1' J I hI
        (swap_mem_cuts.mpr hIJ) hmin'
  · by_cases hb0 : Jᶜ.card = 0
    · have hJ : Jᶜ = ∅ := Finset.card_eq_zero.mp hb0
      exact marginal_case_of_cut hF hS hn11 hn15 D hl hl1 I J hJ hIJ hmin
    · exact proper_case hF hS hn11 hn15 D hl hl1 I J hIJ hmin (by omega) (by omega)

/-- Every maximizer in dimension `11 ≤ n ≤ 15` is entrywise positive. -/
theorem maximizer_pos (hH : HallDomination) (hF : GurvitsFloors) (hS : ScalarCertificates11)
    (hn11 : 11 ≤ n) (hn15 : n ≤ 15) (A : Matrix (Fin n) (Fin n) ℝ) (hA : IsMaximizer A)
    (i j : Fin n) : 0 < A i j := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  rcases (hA.1.1 i j).lt_or_eq with h | h
  · exact h
  · exact (no_zero_of_maximizer hH hF hS hn11 hn15 A hA i j h.symm).elim

end Dittert
