# Kernel verification of two near-zero polynomial inequalities

For every real u in [0,1/400], the literal polynomial p_8(u) in DEFINITIONS.md is strictly positive, and for every real u in [0,1/500], the literal polynomial p_9(u) is strictly positive. The Lean theorem near_zero_certificate proves this conjunction using only propext, Classical.choice and Quot.sound. Evidence: deterministic/formal-check-1/result.json and axioms.log.

The polynomial is defined by gamma=n!/n^n, kappa=(n-2)!*((n-2)/(n-1)^2)^(n-2), L=kappa*(1+1/(2*n^2)), E=1-(2-gamma)*u, H=(1-gamma)*u, T=E-H/(n-1), F=(1-u)*(1+u/(n-1))^(n-1), and p_n=(2-gamma+L*(1-u)^n-F)*E^n-(E+H)*T^(n-1). Definitions.lean implements these formulas directly.

After x=400*u or x=500*u, the degree-16 or degree-18 polynomial has an explicit homogeneous expansion with 17 or 19 strictly positive rational coefficients. Each identity is proved after unfolding the actual formula, using norm_num and ring. Every summand is nonnegative on [0,1]; for x<1 the first is positive, and at x=1 the last is positive. The final proof applies the checked identities and exact rescaling. Evidence: Certificate8.lean, Certificate9.lean, Main.lean and PROOF.md.

The Python generator proposes proof data but contributes no premise or axiom. The first source check found one implementation slip, a missing noncomputable declaration, which was repaired. The intentionally incomplete initial theorem was rejected by the axiom gate. All final principal declarations have the standard axiom list. Evidence: INITIAL_RED_GATE.md, ATTEMPTS.md and axioms.log.

These inequalities are an existing part of the local Hall coverage argument, whose mathematical provenance is recorded in study/problem.md and the inherited coverage proof. Earlier Bernstein formalization includes DOI 10.1017/S0960129511000090 and DOI 10.1007/s10817-012-9256-3. Earlier Dittert Lean work includes arXiv:2607.29191v2. No priority claim is made.

The theorem covers precisely the two near-zero polynomials. The remaining n8,n9 support intervals, tail arguments, matrix reduction, and all n7 formal cases are outside this artifact.
