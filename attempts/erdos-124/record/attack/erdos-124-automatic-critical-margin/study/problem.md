# Problem study: automatic critical normalized margin

## 1. Queries

For every nonempty finite set V of distinct integers at least 4 with sum_{d in V}1/(d-1)=1 and containing a multiplicatively independent pair, H_V(x)>x holds for every real x>1, where p_d(x) is the least nonnegative integer power of d at least x and H_V(x)=sum_{d in V}(p_d(x)-1)/(d-1).

The exact question, its zero-cutoff completeness neighbour and its critical-prefix geometry were studied in QUERY_LOG.md. Ten attempts on2026-09-08 include all five tier-one sources and five secondary searches. Query strings, every returned result set and access failures are preserved. This is the new problem-level study, not reuse of a completed CP28 novelty conclusion.

## 2. Hits and reading

The original Erdős124 discussion gives tsaf's geometric zero-cutoff argument and Alexeev's linked Lean source. Its actual algebraic_gap statement bounds a lower next weight by one plus the geometric prefix total. The sorted sequence includes one separate value1 per base. This exact theorem and its proof do not state the stronger H_V(x)>x requirement and do not preserve arbitrary positive cutoffs automatically.

Primary source: https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos124b.lean . Selected declarations and proof text were read through the raw source. The theorem is a literature result, not independently rebuilt here. The discussion is https://www.erdosproblems.com/forum/thread/124 , with the explicit proof by tsaf at08:10 on30Nov2025.

Kovač and Tao, On several irrationality problems for Ahmes series, arXiv2406.17593v4, DOI10.1007/s10474-025-01528-0, Theorem2.3 and complete Section4 proof, provide the directly linked continuous subseries comparison. They assume strict reciprocal mass above one, choose a positive epsilon while preserving that strictness, and work with reciprocal Lambert terms. Their printed proof does not discharge the equality-one integer margin. The initially opened v2 has different content and is not used as this theorem.

BEGL1996, DOI10.4064/aa-77-2-133-138, Sections1-3, remains the primary original positive-cutoff source. The copied canonical FormalConjectures/ErdosProblems/124.lean distinguishes its open positive-cutoff statement from the solved zero-cutoff statement. It contains placeholders and is not a formal proof input. Our exact H_V auxiliary claim has no separate formal declaration located by this study. The original controller claim preserves all finite D, gcd one, all positive cutoffs and occurrence labels. Neither the webpage's apparent d_r typo nor an auxiliary H_V decision changes it.

Accepted local predecessor CP28, checkpoint-000028, acceptance-000015, proof Sections2 and9, already supplies the quantitative independent-pair tail estimate, the complete finite test for each fixed V, and the hand certificate V={4,5,6,7,21}. Those are inherited facts, not new theorem candidates in this study. CP9's qualitative all-future surplus additionally requires its stated gcd-one hypotheses and is not a replacement.

## 3. Constraints on the proposed route

The elementary geometric-prefix identity is an exact, source-backed starting point for a focused counterexample-structure question. The proposed analytical route is to assume the first failure of strictness, examine the first unused powers, their divisibility and distinct-base reciprocal-mass identity, and try to exclude their extremal configuration or obtain a genuinely new exact restriction. This is a plan, not a derived condition or a proof that the route works.

A correct proof of the displayed universal assertion would remove CP28's explicit H_V premise for every critical complement in its other structural domain. A correct counterexample would reject that automatic extension only, not original eventual completeness. The common-radix half-mass supply and all broader root obligations would remain. An isolated reproof of Brown's inequality, the inherited finite test or CP28's hand example is not substantive new progress.

No general strictness theorem, counterexample, useful new parameter bound or mathematical computation was obtained during this study. The credible part is the exact discrete equality-case question tied to a reviewed application. Its feasibility must be tested in a separately admitted, reserved analytical entry, with at most three applications and immediate failure on no compression or an unusable residual range. The primary continuous theorem supplies a boundary comparison, not a shortcut through equality.

Compared with the older mixed-base half-mass and proper one-supply routes, this question has a precise scalar predicate and explicit local application. It does not repair their missing legal support operations and is not selected because it guarantees a checkpoint. Retain all seven failures and the completed attack histories.

## 4. Stop

The fixed ten-attempt cap was reached. No exact prior resolution was found among the inspected results, with the access and reading limitations in QUERY_LOG.md. This is not an exhaustive novelty claim. Separate admission is warranted only for the exact displayed statement and the bounded equality-case operation. No native execution has begun, no account is reset, and a failure to obtain new compression must be recorded rather than relabelled as progress.
