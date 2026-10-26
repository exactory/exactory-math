/-
# Analytic closure lemmas for H-stability

The port `GurvitsPort` (DCPRevere/maths-pub, commit 0a1cb0a14fefe85668365d448f9bbaf4dd89d458,
Apache-2.0; see `../../../maths-pub-port/PORT-NOTES.md` and `AXIOMS.txt`) proves that
H-stability (`Gurvits.HStable`: no zero on the open RIGHT half-space) survives `∂₀` on the
hypothesis `HStableOrbit.NonDegenerate`, and it never sets a variable to `0`.  The rectangle
floor needs both closures on the homogeneous chain, so this file proves them:

* `hstable_of_limit` — the one analytic argument.  A nonzero polynomial that is, along every
  complex line, the limit of nonvanishing polynomials (as a real parameter `s → 0⁺`) is
  H-stable.  Minimum modulus principle on a small closed disc, uniform closeness from
  Heine–Cantor.
* `restrict_zero_hstable` — `x₀ := 0` preserves H-stability when the result is nonzero; the
  specialised variable is the positive real `s`, so the limit stays inside the half-space.
* `leadingCoeff_hstable` — the leading `x₀`-coefficient of a nonzero H-stable polynomial is
  H-stable (the reversed expansion `s ^ D · q(1/s, ·)`).  This gives
  `nonDegenerate_of_natDegree_pos`, the explicit `NonDegenerate` lemma.
* `hstable_reduce` — `GurvitsInduction.reduce` preserves H-stability when the result is nonzero.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Complex.AbsMax
import Mathlib.Analysis.Calculus.Deriv.Polynomial
import Mathlib.Topology.Algebra.MvPolynomial
import Mathlib.Topology.UniformSpace.HeineCantor
import Mathlib.Algebra.MvPolynomial.Funext
import Mathlib.Algebra.Polynomial.Roots
import GurvitsPort.HStableClass

open MvPolynomial

namespace Dittert.Floors.Analytic

/-! ## §1  Polynomials along a complex line, and continuity of `aeval` -/

/-- Evaluating a `ℂ[X]`-valued substitution at `t` is the substitution of the values. -/
theorem eval_aeval_poly {k : ℕ} (G : Fin k → Polynomial ℂ) (p : MvPolynomial (Fin k) ℝ)
    (t : ℂ) :
    Polynomial.eval t (MvPolynomial.aeval G p)
      = MvPolynomial.aeval (fun i => Polynomial.eval t (G i)) p := by
  induction p using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq]
  | mul_X p i hp => simp [hp]

/-- `w ↦ aeval w p` is continuous on `Fin k → ℂ`. -/
theorem continuous_aeval {k : ℕ} (p : MvPolynomial (Fin k) ℝ) :
    Continuous fun w : Fin k → ℂ => MvPolynomial.aeval w p := by
  have h : (fun w : Fin k → ℂ => MvPolynomial.aeval w p)
      = fun w => MvPolynomial.eval w (MvPolynomial.map (algebraMap ℝ ℂ) p) := by
    funext w
    rw [MvPolynomial.aeval_def, MvPolynomial.eval₂_eq_eval_map]
  rw [h]
  exact MvPolynomial.continuous_eval _

/-- A real point evaluates through the complex `aeval` as the cast of the real value. -/
theorem aeval_ofReal {k : ℕ} (x : Fin k → ℝ) (p : MvPolynomial (Fin k) ℝ) :
    MvPolynomial.aeval (fun j => (x j : ℂ)) p = ((MvPolynomial.eval x p : ℝ) : ℂ) := by
  induction p using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq]
  | mul_X p i hp => simp [hp]

/-! ## §2  The analytic core -/

/-- **The limit lemma.**  Let `g ≠ 0`, and let `F s` (`s : ℝ`) be a jointly continuous family
with `F 0 = aeval · g`, each `F s` a polynomial along every complex line, and each `F s` with
`s > 0` nonvanishing on the open right half-space.  Then `g` is H-stable.

Proof: at a hypothetical zero `w₀` of `g` in the half-space, take a complex line through `w₀`
on which `g` is not identically zero, a closed disc around `0` on that line inside the
half-space and free of other zeros of `g`, and a positive `s` at which `F s` is closer to `g`
on the disc than half the minimum of `‖g‖` on the circle.  The minimum of `‖F s‖` on the disc
is then attained inside, and the minimum modulus principle makes `F s` constant or zero. -/
theorem hstable_of_limit {k : ℕ} {g : MvPolynomial (Fin k) ℝ} (hg : g ≠ 0)
    {F : ℝ → (Fin k → ℂ) → ℂ}
    (hcont : Continuous fun p : ℝ × (Fin k → ℂ) => F p.1 p.2)
    (hpoly : ∀ (s : ℝ) (w₀ v : Fin k → ℂ), ∃ ψ : Polynomial ℂ,
      ∀ t : ℂ, Polynomial.eval t ψ = F s (fun j => w₀ j + t * v j))
    (hzero : ∀ w : Fin k → ℂ, F 0 w = MvPolynomial.aeval w g)
    (hne : ∀ s : ℝ, 0 < s → ∀ w : Fin k → ℂ, (∀ j, 0 < (w j).re) → F s w ≠ 0) :
    Gurvits.HStable g := by
  intro w₀ hw₀ hg0
  -- a point where `g` does not vanish
  obtain ⟨x₁, hx₁⟩ : ∃ x : Fin k → ℝ, MvPolynomial.eval x g ≠ 0 := by
    by_contra hcon
    refine hg (MvPolynomial.funext fun x => ?_)
    rw [map_zero]
    by_contra h
    exact hcon ⟨x, h⟩
  have hw₁ : MvPolynomial.aeval (fun j => (x₁ j : ℂ)) g ≠ 0 := by
    rw [aeval_ofReal]
    exact_mod_cast hx₁
  set v : Fin k → ℂ := fun j => (x₁ j : ℂ) - w₀ j with hvdef
  -- the line polynomial of `g` through `w₀` in the direction `v`
  obtain ⟨φ, hφ⟩ := hpoly 0 w₀ v
  have hφeval : ∀ t : ℂ, Polynomial.eval t φ
      = MvPolynomial.aeval (fun j => w₀ j + t * v j) g := by
    intro t
    rw [hφ, hzero]
  have hφ0 : Polynomial.eval 0 φ = 0 := by
    rw [hφeval]
    simpa using hg0
  have hφ1 : Polynomial.eval 1 φ ≠ 0 := by
    rw [hφeval]
    have hfun : (fun j => w₀ j + 1 * v j) = fun j => (x₁ j : ℂ) := by
      funext j
      simp [hvdef]
    rw [hfun]
    exact hw₁
  have hφne : φ ≠ 0 := by
    rintro rfl
    simp at hφ1
  -- the half-space is open along the line
  have hU : IsOpen {t : ℂ | ∀ j, 0 < (w₀ j + t * v j).re} := by
    have hrepr : {t : ℂ | ∀ j, 0 < (w₀ j + t * v j).re}
        = ⋂ j, {t : ℂ | 0 < (w₀ j + t * v j).re} := by
      ext t
      simp
    rw [hrepr]
    exact isOpen_iInter_of_finite fun j =>
      isOpen_lt continuous_const (Complex.continuous_re.comp (by fun_prop))
  obtain ⟨r₁, hr₁, hball₁⟩ := Metric.isOpen_iff.mp hU 0 (by simpa using hw₀)
  -- the zero of `φ` at `0` is isolated
  have hfin : ({t : ℂ | φ.IsRoot t} \ {0}).Finite :=
    (Polynomial.finite_setOfPred_isRoot hφne).subset Set.sdiff_subset
  have hopen₂ : IsOpen ({t : ℂ | φ.IsRoot t} \ {0})ᶜ := hfin.isClosed.isOpen_compl
  obtain ⟨r₂, hr₂, hball₂⟩ := Metric.isOpen_iff.mp hopen₂ 0 (by simp)
  -- the radius
  have hmin : 0 < min r₁ r₂ := lt_min hr₁ hr₂
  set r : ℝ := min r₁ r₂ / 2 with hrdef
  have hr : 0 < r := half_pos hmin
  have hr₁' : r < r₁ := by
    have := min_le_left r₁ r₂
    rw [hrdef]
    linarith
  have hr₂' : r < r₂ := by
    have := min_le_right r₁ r₂
    rw [hrdef]
    linarith
  have hhalf : ∀ t : ℂ, ‖t‖ ≤ r → ∀ j, 0 < (w₀ j + t * v j).re := fun t ht =>
    hball₁ (by rw [Metric.mem_ball, dist_zero_right]; linarith)
  have hφsphere : ∀ t : ℂ, ‖t‖ = r → Polynomial.eval t φ ≠ 0 := by
    intro t ht hzero'
    have hmem : t ∈ ({t : ℂ | φ.IsRoot t} \ {0})ᶜ :=
      hball₂ (by rw [Metric.mem_ball, dist_zero_right, ht]; exact hr₂')
    have ht0 : t ≠ 0 := by
      rintro rfl
      rw [norm_zero] at ht
      exact hr.ne ht
    exact hmem ⟨hzero', ht0⟩
  -- the minimum of `‖φ‖` on the circle is positive
  have hsph : ((r : ℂ)) ∈ Metric.sphere (0 : ℂ) r := by
    rw [Metric.mem_sphere, dist_zero_right, Complex.norm_of_nonneg hr.le]
  obtain ⟨t₀, ht₀, hmin₀⟩ := (isCompact_sphere (0 : ℂ) r).exists_isMinOn ⟨(r : ℂ), hsph⟩
    (φ.continuous.norm.continuousOn)
  have ht₀r : ‖t₀‖ = r := by
    rw [Metric.mem_sphere, dist_zero_right] at ht₀
    exact ht₀
  set m : ℝ := ‖Polynomial.eval t₀ φ‖ with hmdef
  have hm : 0 < m := norm_pos_iff.mpr (hφsphere t₀ ht₀r)
  have hm_le : ∀ t : ℂ, ‖t‖ = r → m ≤ ‖Polynomial.eval t φ‖ := fun t ht =>
    hmin₀ (by rw [Metric.mem_sphere, dist_zero_right]; exact ht)
  -- uniform closeness on the closed disc, from Heine–Cantor
  set K : Set (ℝ × ℂ) := Set.Icc (0 : ℝ) 1 ×ˢ Metric.closedBall (0 : ℂ) r with hKdef
  have hK : IsCompact K := isCompact_Icc.prod (isCompact_closedBall 0 r)
  have hG : Continuous fun p : ℝ × ℂ => F p.1 (fun j => w₀ j + p.2 * v j) := by
    have hinner : Continuous
        fun p : ℝ × ℂ => ((p.1, fun j => w₀ j + p.2 * v j) : ℝ × (Fin k → ℂ)) :=
      continuous_fst.prodMk
        (continuous_pi fun j => continuous_const.add (continuous_snd.mul continuous_const))
    exact hcont.comp hinner
  have hK' : UniformContinuousOn (fun p : ℝ × ℂ => F p.1 (fun j => w₀ j + p.2 * v j)) K :=
    hK.uniformContinuousOn_of_continuous hG.continuousOn
  obtain ⟨δ, hδ, hδ'⟩ := Metric.uniformContinuousOn_iff.mp hK' (m / 2) (by positivity)
  set s : ℝ := min δ 1 / 2 with hsdef
  have hs : 0 < s := half_pos (lt_min hδ one_pos)
  have hs1 : s ≤ 1 := by
    have := min_le_right δ 1
    rw [hsdef]
    linarith
  have hsδ : s < δ := by
    have := min_le_left δ 1
    rw [hsdef]
    linarith
  have hclose : ∀ t : ℂ, ‖t‖ ≤ r →
      ‖F s (fun j => w₀ j + t * v j) - Polynomial.eval t φ‖ < m / 2 := by
    intro t ht
    have hmem₁ : ((s, t) : ℝ × ℂ) ∈ K :=
      ⟨⟨hs.le, hs1⟩, by rw [Metric.mem_closedBall, dist_zero_right]; exact ht⟩
    have hmem₂ : ((0, t) : ℝ × ℂ) ∈ K :=
      ⟨⟨le_rfl, zero_le_one⟩, by rw [Metric.mem_closedBall, dist_zero_right]; exact ht⟩
    have hdist : dist ((s, t) : ℝ × ℂ) (0, t) < δ := by
      rw [Prod.dist_eq, dist_self, Real.dist_eq, sub_zero, abs_of_pos hs, max_eq_left hs.le]
      exact hsδ
    have := hδ' _ hmem₁ _ hmem₂ hdist
    rw [dist_eq_norm] at this
    rw [hφeval, ← hzero]
    exact this
  -- the approximating polynomial along the line
  obtain ⟨ψ, hψ⟩ := hpoly s w₀ v
  have hψne : ∀ t : ℂ, ‖t‖ ≤ r → Polynomial.eval t ψ ≠ 0 := fun t ht => by
    rw [hψ]
    exact hne s hs _ (hhalf t ht)
  have hψclose : ∀ t : ℂ, ‖t‖ ≤ r →
      ‖Polynomial.eval t ψ - Polynomial.eval t φ‖ < m / 2 := fun t ht => by
    rw [hψ]
    exact hclose t ht
  have hψ0 : ‖Polynomial.eval 0 ψ‖ < m / 2 := by
    have := hψclose 0 (by rw [norm_zero]; exact hr.le)
    rwa [hφ0, sub_zero] at this
  have hψsphere : ∀ t : ℂ, ‖t‖ = r → m / 2 < ‖Polynomial.eval t ψ‖ := by
    intro t ht
    have h1 := hm_le t ht
    have h2 := hψclose t ht.le
    have h3 := norm_sub_norm_le (Polynomial.eval t φ) (Polynomial.eval t ψ)
    rw [norm_sub_rev] at h3
    linarith
  -- the minimum of `‖ψ‖` on the closed disc is attained inside
  obtain ⟨t₁, ht₁, hmin₁⟩ := (isCompact_closedBall (0 : ℂ) r).exists_isMinOn
    ⟨0, by rw [Metric.mem_closedBall, dist_self]; exact hr.le⟩ (ψ.continuous.norm.continuousOn)
  have ht₁r : ‖t₁‖ ≤ r := by
    rw [Metric.mem_closedBall, dist_zero_right] at ht₁
    exact ht₁
  have hψt₁ : ‖Polynomial.eval t₁ ψ‖ < m / 2 :=
    lt_of_le_of_lt (hmin₁ (by rw [Metric.mem_closedBall, dist_self]; exact hr.le)) hψ0
  have ht₁lt : ‖t₁‖ < r := by
    rcases lt_or_eq_of_le ht₁r with h | h
    · exact h
    · exact absurd (hψsphere t₁ h) (not_lt.mpr hψt₁.le)
  have hloc : IsLocalMin (norm ∘ fun t : ℂ => Polynomial.eval t ψ) t₁ :=
    (hmin₁.on_subset Metric.ball_subset_closedBall).isLocalMin
      (Metric.isOpen_ball.mem_nhds (by rw [Metric.mem_ball, dist_zero_right]; exact ht₁lt))
  rcases Complex.eventually_eq_or_eq_zero_of_isLocalMin_norm
      (Filter.Eventually.of_forall fun z => ψ.differentiableAt) hloc with hev | h0
  · -- `ψ` is constant near `t₁`, hence constant, which contradicts the circle bound
    obtain ⟨ρ, hρ, hρ'⟩ := Metric.eventually_nhds_iff.mp hev
    have hconst : ψ = Polynomial.C (Polynomial.eval t₁ ψ) := by
      apply Polynomial.eq_of_infinite_eval_eq
      have hinj : Set.InjOn (fun x : ℝ => t₁ + (x : ℂ)) (Set.Ioo 0 ρ) := by
        intro x _ y _ hxy
        have hxy' : t₁ + (x : ℂ) = t₁ + (y : ℂ) := hxy
        exact_mod_cast add_left_cancel hxy'
      refine Set.Infinite.mono ?_ ((Set.infinite_image_iff hinj).mpr (Set.Ioo_infinite hρ))
      rintro _ ⟨x, ⟨hx0, hxρ⟩, rfl⟩
      simp only [Set.mem_ofPred_eq, Polynomial.eval_C]
      apply hρ'
      rw [dist_eq_norm, add_sub_cancel_left, Complex.norm_of_nonneg hx0.le]
      exact hxρ
    have hval : Polynomial.eval (r : ℂ) ψ = Polynomial.eval t₁ ψ := by
      conv_lhs => rw [hconst]
      rw [Polynomial.eval_C]
    have := hψsphere (r : ℂ) (Complex.norm_of_nonneg hr.le)
    rw [hval] at this
    linarith
  · exact hψne t₁ ht₁r h0

/-! ## §3  The `x₀`-expansion, through the port's `lineRestrict` -/

/-- The coefficients of the port's `lineRestrict` are the complex evaluations of the
`x₀`-coefficients. -/
theorem coeff_lineRestrict {k : ℕ} (q : MvPolynomial (Fin (k + 1)) ℝ) (z : Fin k → ℂ) (i : ℕ) :
    (HStableDerivative.lineRestrict q z).coeff i
      = MvPolynomial.aeval z ((finSuccEquiv ℝ k q).coeff i) := by
  rw [HStableDerivative.lineRestrict, Polynomial.coeff_map, MvPolynomial.aeval_def,
    MvPolynomial.eval₂_eq_eval_map]
  congr 1
  ext m
  rw [MvPolynomial.coeff_map, finSuccEquiv_coeff_coeff, finSuccEquiv_coeff_coeff,
    HStableDerivative.cpoly, MvPolynomial.coeff_map]

theorem natDegree_lineRestrict_le {k : ℕ} (q : MvPolynomial (Fin (k + 1)) ℝ) (z : Fin k → ℂ) :
    (HStableDerivative.lineRestrict q z).natDegree ≤ (finSuccEquiv ℝ k q).natDegree := by
  refine Polynomial.natDegree_le_iff_coeff_eq_zero.mpr fun N hN => ?_
  rw [coeff_lineRestrict, Polynomial.coeff_eq_zero_of_natDegree_lt hN, map_zero]

/-- The expansion `q(t, z) = ∑ᵢ qᵢ(z) tⁱ`. -/
theorem aeval_cons_eq_sum {k : ℕ} (q : MvPolynomial (Fin (k + 1)) ℝ) (z : Fin k → ℂ) (t : ℂ)
    {D : ℕ} (hD : (finSuccEquiv ℝ k q).natDegree ≤ D) :
    MvPolynomial.aeval (Fin.cons t z) q
      = ∑ i ∈ Finset.range (D + 1),
          MvPolynomial.aeval z ((finSuccEquiv ℝ k q).coeff i) * t ^ i := by
  rw [← HStableDerivative.eval_lineRestrict]
  rw [Polynomial.eval_eq_sum_range' (n := D + 1)
    (lt_of_le_of_lt (le_trans (natDegree_lineRestrict_le q z) hD) (Nat.lt_succ_self D))]
  exact Finset.sum_congr rfl fun i _ => by rw [coeff_lineRestrict]

/-! ## §4  Restriction to `x₀ = 0` -/

/-- **Restriction closure.**  If `f` is H-stable and `f|_{x₀ = 0}` is nonzero, then
`f|_{x₀ = 0}` is H-stable.  The specialised variable is the positive real `s → 0⁺`. -/
theorem restrict_zero_hstable {k : ℕ} {f : MvPolynomial (Fin (k + 1)) ℝ}
    (hf : Gurvits.HStable f) (hne : (finSuccEquiv ℝ k f).coeff 0 ≠ 0) :
    Gurvits.HStable ((finSuccEquiv ℝ k f).coeff 0) := by
  refine hstable_of_limit hne
    (F := fun s w => MvPolynomial.aeval (Fin.cons (s : ℂ) w) f) ?_ ?_ ?_ ?_
  · -- joint continuity
    have hc : Continuous fun p : ℝ × (Fin k → ℂ) => (Fin.cons (p.1 : ℂ) p.2 : Fin (k + 1) → ℂ) := by
      refine continuous_pi fun i => ?_
      refine Fin.cases ?_ (fun j => ?_) i
      · simp only [Fin.cons_zero]
        exact Complex.continuous_ofReal.comp continuous_fst
      · simp only [Fin.cons_succ]
        exact (continuous_apply j).comp continuous_snd
    exact (continuous_aeval f).comp hc
  · -- a polynomial along every line
    intro s w₀ v
    refine ⟨MvPolynomial.aeval (Fin.cons (Polynomial.C (s : ℂ))
      (fun j => Polynomial.C (w₀ j) + Polynomial.X * Polynomial.C (v j))) f, fun t => ?_⟩
    rw [eval_aeval_poly]
    have hfun : (fun i => Polynomial.eval t ((Fin.cons (Polynomial.C (s : ℂ))
        (fun j => Polynomial.C (w₀ j) + Polynomial.X * Polynomial.C (v j)) :
          Fin (k + 1) → Polynomial ℂ) i))
        = (Fin.cons (s : ℂ) (fun j => w₀ j + t * v j) : Fin (k + 1) → ℂ) := by
      funext i
      refine Fin.cases ?_ (fun j => ?_) i
      · simp
      · simp only [Fin.cons_succ, Polynomial.eval_add, Polynomial.eval_C, Polynomial.eval_mul,
          Polynomial.eval_X]
    rw [hfun]
  · -- the value at `s = 0`
    intro w
    show MvPolynomial.aeval (Fin.cons ((0 : ℝ) : ℂ) w) f = _
    rw [Complex.ofReal_zero, ← HStableDerivative.eval_lineRestrict,
      ← Polynomial.coeff_zero_eq_eval_zero, coeff_lineRestrict]
  · -- nonvanishing at positive `s`
    intro s hs w hw
    exact hf _ (HStableDerivative.cons_re_pos (by simpa using hs) hw)

/-! ## §5  The leading coefficient, and non-degeneracy -/

/-- **Leading coefficient closure.**  The leading `x₀`-coefficient of a nonzero H-stable
polynomial is H-stable: it is the limit of `s ^ D · q(1/s, ·)` as `s → 0⁺`. -/
theorem leadingCoeff_hstable {k : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ}
    (hq : Gurvits.HStable q) (hne : finSuccEquiv ℝ k q ≠ 0) :
    Gurvits.HStable ((finSuccEquiv ℝ k q).coeff (finSuccEquiv ℝ k q).natDegree) := by
  set P := finSuccEquiv ℝ k q with hPdef
  set D := P.natDegree with hDdef
  have hlead : P.coeff D ≠ 0 := Polynomial.leadingCoeff_ne_zero.mpr hne
  refine hstable_of_limit hlead
    (F := fun s w => ∑ i ∈ Finset.range (D + 1),
      MvPolynomial.aeval w (P.coeff i) * (s : ℂ) ^ (D - i)) ?_ ?_ ?_ ?_
  · -- joint continuity
    refine continuous_finsetSum _ fun i _ => ?_
    exact ((continuous_aeval (P.coeff i)).comp continuous_snd).mul
      ((Complex.continuous_ofReal.comp continuous_fst).pow _)
  · -- a polynomial along every line
    intro s w₀ v
    refine ⟨∑ i ∈ Finset.range (D + 1),
      MvPolynomial.aeval (fun j => Polynomial.C (w₀ j) + Polynomial.X * Polynomial.C (v j))
        (P.coeff i) * Polynomial.C ((s : ℂ) ^ (D - i)), fun t => ?_⟩
    rw [Polynomial.eval_finsetSum]
    refine Finset.sum_congr rfl fun i _ => ?_
    have hfun : (fun j => Polynomial.eval t
        (Polynomial.C (w₀ j) + Polynomial.X * Polynomial.C (v j)))
        = fun j => w₀ j + t * v j := by
      funext j
      simp only [Polynomial.eval_add, Polynomial.eval_C, Polynomial.eval_mul, Polynomial.eval_X]
    rw [Polynomial.eval_mul, Polynomial.eval_C, eval_aeval_poly, hfun]
  · -- the value at `s = 0`
    intro w
    show ∑ i ∈ Finset.range (D + 1),
      MvPolynomial.aeval w (P.coeff i) * ((0 : ℝ) : ℂ) ^ (D - i) = _
    rw [Finset.sum_eq_single D]
    · simp
    · intro i hi hiD
      have hsub : D - i ≠ 0 := by
        rw [Finset.mem_range] at hi
        omega
      rw [Complex.ofReal_zero, zero_pow hsub, mul_zero]
    · intro h
      exact absurd (Finset.mem_range.mpr (Nat.lt_succ_self D)) h
  · -- nonvanishing at positive `s`: it is `s ^ D · q(1/s, w)`
    intro s hs w hw
    have hsc : (s : ℂ) ≠ 0 := by exact_mod_cast hs.ne'
    have hexp := aeval_cons_eq_sum q w (((s⁻¹ : ℝ)) : ℂ) (le_refl D)
    have hval : (∑ i ∈ Finset.range (D + 1),
        MvPolynomial.aeval w (P.coeff i) * (s : ℂ) ^ (D - i))
        = (s : ℂ) ^ D * MvPolynomial.aeval (Fin.cons (((s⁻¹ : ℝ)) : ℂ) w) q := by
      rw [hexp, Finset.mul_sum]
      refine Finset.sum_congr rfl fun i hi => ?_
      rw [Finset.mem_range] at hi
      rw [Complex.ofReal_inv, pow_sub₀ _ hsc (by omega), inv_pow]
      ring
    show (∑ i ∈ Finset.range (D + 1),
      MvPolynomial.aeval w (P.coeff i) * (s : ℂ) ^ (D - i)) ≠ 0
    rw [hval]
    refine mul_ne_zero (pow_ne_zero _ hsc) ?_
    refine hq _ (HStableDerivative.cons_re_pos ?_ hw)
    simp only [Complex.ofReal_re]
    exact inv_pos.mpr hs

/-- **Non-degeneracy.**  An H-stable polynomial of positive `x₀`-degree satisfies the port's
`HStableOrbit.NonDegenerate`: at every complex point of the open right half-space the line
restriction has positive degree, because its top coefficient is the (H-stable) leading
`x₀`-coefficient evaluated there. -/
theorem nonDegenerate_of_natDegree_pos {k : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ}
    (hq : Gurvits.HStable q) (hd : 0 < (finSuccEquiv ℝ k q).natDegree) :
    HStableOrbit.NonDegenerate q := by
  intro z hz
  have hne : finSuccEquiv ℝ k q ≠ 0 := by
    intro h
    rw [h, Polynomial.natDegree_zero] at hd
    exact lt_irrefl 0 hd
  have hlead := leadingCoeff_hstable hq hne z hz
  have hcoeff : (HStableDerivative.lineRestrict q z).coeff (finSuccEquiv ℝ k q).natDegree ≠ 0 := by
    rw [coeff_lineRestrict]
    exact hlead
  have hle := Polynomial.le_degree_of_ne_zero hcoeff
  exact lt_of_lt_of_le (by exact_mod_cast hd) hle

/-! ## §6  Closure of H-stability under `reduce` -/

/-- `GurvitsInduction.reduce q` is the `x₀ = 0` restriction of `∂₀ q`. -/
theorem reduce_eq_coeff_zero_pderiv {k : ℕ} (q : MvPolynomial (Fin (k + 1)) ℝ) :
    GurvitsInduction.reduce q = (finSuccEquiv ℝ k (pderiv 0 q)).coeff 0 := by
  rw [HStableDerivative.finSuccEquiv_pderiv_zero, Polynomial.coeff_derivative,
    GurvitsInduction.reduce]
  simp

/-- **Closure under `reduce`.**  If `q` is H-stable and `reduce q ≠ 0`, then `reduce q` is
H-stable: `∂₀ q` is H-stable by the port's Gauss–Lucas step on `nonDegenerate_of_natDegree_pos`,
and the restriction to `x₀ = 0` is H-stable by `restrict_zero_hstable`. -/
theorem hstable_reduce {k : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ} (hq : Gurvits.HStable q)
    (hne : GurvitsInduction.reduce q ≠ 0) : Gurvits.HStable (GurvitsInduction.reduce q) := by
  have hres := reduce_eq_coeff_zero_pderiv q
  have hd : 0 < (finSuccEquiv ℝ k q).natDegree := by
    rcases Nat.eq_zero_or_pos (finSuccEquiv ℝ k q).natDegree with h0 | hpos
    · exfalso
      apply hne
      rw [GurvitsInduction.reduce]
      exact Polynomial.coeff_eq_zero_of_natDegree_lt (by omega)
    · exact hpos
  have hder := HStableOrbit.hstable_pderiv_of_nonDegenerate hq
    (nonDegenerate_of_natDegree_pos hq hd)
  rw [hres]
  refine restrict_zero_hstable hder ?_
  rw [← hres]
  exact hne

end Dittert.Floors.Analytic
