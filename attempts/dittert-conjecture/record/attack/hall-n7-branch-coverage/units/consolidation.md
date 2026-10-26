# Consolidation of the attributed n=7 coverage argument

The proposition in problem.json is established by COVERAGE_PROOF.md and the passed deterministic/certified-special-case-check-1. Its scope is every boundary global maximizer at n=7, including every minimizing cut and every support pattern. This child does not claim the n=8..15 result or positive-maximizer classification.

The steps that needed explicit justification were: positivity of the Hall scale before division, both scale endpoints, canonicalization of all ordered cuts, zero deviations, zero core entries and minors in entropy, positivity of the denominator before clearing it, N>0 before squaring, the u=0 and s=0 energy endpoints, and retention of both subdivision children. Each is now explicit in the proof.

The original small/large marginal entropy split is replaceable by the same AM-GM bound for all s>0. This removes an unnecessary branch question while keeping all feasible matrices. The proof still needs the bivariate finite alternatives; no computation-free replacement or second independent mathematical route has been established. The new independent implementation uses direct binomial restriction at each leaf, an arithmetic route different from the generator's de Casteljau subdivision.

The check enumerates all 6,476 subset-pair cuts, including the full and all marginal cuts. All 62 closed leaf boxes are certified; 94 omissions are rejected. Complete prefix closure and exact geometry establish a cover of the continuous square. Node counts and endpoint probes are supplementary diagnostics and are not premises of completeness.

The underlying method and theorem are already attributed to Lu and Nascimento. This is an audit and exposition, not a new discovery or an independent second proof. It therefore produces no new publication unit. The exact reproducible certificate, proof, and lineage remain the evidence returned to the parent. A fresh independent review is being arranged by the parent, separately from these authored deductions.
