# Formal blueprint

1. Definitions.gamma, kappa, lower, e, h, t, f, and p implement DEFINITIONS.md literally using real arithmetic.
2. State near_zero_certificate as the conjunction of two universally quantified strict inequalities on the full closed intervals.
3. For each explicit homogeneous expansion, prove positivity on 0<=x<=1. When x<1, the k=0 term is strictly positive and every other term is nonnegative; when x=1, exact arithmetic proves positivity of the final coefficient. Mathlib's positivity tactic constructs this elementary proof directly, so no separately assumed generic Bernstein lemma is needed.
4. Produce rational homogeneous Bernstein coefficients for p_n(x/d), with y=1-x, and prove the polynomial identity by kernel-supported rational normalization and ring arithmetic.
5. Apply the basis theorem to each explicit identity, then rescale u. The final theorem proves the actual formula and intervals, without coefficient assumptions.
