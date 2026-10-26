import Mathlib

/-! # Sidorenko's inequality for bipartite patterns without 4-cycles

The densities follow the comparator statement of the reported counterexample (openai/math,
`lean/ComparatorChallenges/SidorenkoCounterexample.lean` at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a): homomorphism density counts all edge-preserving maps,
including noninjective maps, and the edge density of a host on `m` vertices is `2 e(G) / m ^ 2`.
Finite hosts suffice: the finite-host inequality for every host is equivalent to the graphon form.
-/

namespace SidorenkoGirthSix

noncomputable def homCount {V W : Type*} (F : SimpleGraph V) (G : SimpleGraph W) : ℕ :=
  Nat.card {hom : V → W // ∀ left right, F.Adj left right → G.Adj (hom left) (hom right)}

noncomputable def homDensity {V W : Type*} (F : SimpleGraph V) (G : SimpleGraph W) : ℝ :=
  (homCount F G : ℝ) / (Nat.card W : ℝ) ^ Nat.card V

noncomputable def edgeDensity {W : Type*} (G : SimpleGraph W) : ℝ :=
  2 * (Nat.card G.edgeSet : ℝ) / (Nat.card W : ℝ) ^ 2

/-- Every finite bipartite pattern with an edge and without a cycle of length four satisfies
Sidorenko's inequality in every finite simple host. -/
def Statement : Prop :=
  ∀ (n : ℕ) (H : SimpleGraph (Fin n)), H.Colorable 2 → H.edgeSet.Nonempty →
    (∀ (v : Fin n) (p : H.Walk v v), p.IsCycle → p.length ≠ 4) →
    ∀ (m : ℕ) (G : SimpleGraph (Fin m)), 0 < m →
      edgeDensity G ^ Nat.card H.edgeSet ≤ homDensity H G

end SidorenkoGirthSix
