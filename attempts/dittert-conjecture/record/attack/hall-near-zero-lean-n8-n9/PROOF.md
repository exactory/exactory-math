# Literal near-zero polynomial positivity

Let p_n be the real polynomial in DEFINITIONS.md. Then p_8(u)>0 for every real u in [0,1/400], and p_9(u)>0 for every real u in [0,1/500].

For (n,d)=(8,400) or (9,500), set x=d*u and N=2*n. The explicit rational coefficients c_k in candidate-data.json satisfy c_k>0 and

`p_n(x/d) = sum_{k=0}^N c_k*x^k*(1-x)^(N-k)`.

This identity is not inferred from sample evaluations or from an external coefficient computation. In Certificate8.lean and Certificate9.lean, identity8 and identity9 unfold the literal p definition, normalize factorials and rational arithmetic with norm_num, and prove the full polynomial identity with ring. Lean checks the resulting proof terms. The power-basis Python generator only proposes certificate constants and source code; it is outside the proof's trusted base.

For 0<=x<1, all terms are nonnegative and the k=0 term is strictly positive, since c_0>0 and 1-x>0. For x=1, only the final term survives, and c_N>0 is verified exactly. These are positive8 and positive9. In Main.lean, 0<=u<=1/d implies 0<=d*u<=1. Applying the corresponding identity and positivity theorem, followed by the exact equality (d*u)/d=u, proves the conjunction near_zero_certificate.

The deterministic formal-check-1/result.json is pass. The final theorem's transitive axioms are exactly propext, Classical.choice and Quot.sound. Every coefficient comparison, identity, endpoint and rescaling obligation is inside the formal theorem. The formula uses E and H as polynomial expressions, so no division by E occurs and no omitted nonzero-denominator premise is needed.

This verifies the near-zero polynomial portion of the known n8,n9 marginal argument in ../hall-n8-n15-branch-coverage/PROOF.md, section 6. It does not prove that arbitrary matrices supply the scalar hypotheses, the support intervals [1/400,1/20] and [1/500,3/100], their monotone tails, or any n7 case. It is not a new mathematical Dittert theorem.
