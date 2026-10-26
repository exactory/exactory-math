# Independent Stage 8 draft evaluation

Decision: pass.

The draft's exact statement matches `unit.json`, and every mathematical
claim is supported by the complete proof at
`moves/001-sparse-signed-blocks.md`, interpreted relative to the attack
workspace. No blocking mathematical or exposition gap was found.

## Independence, materials, and evaluation boundary

I am the reader who did not write this draft or its proof. The host identity
observed in this review session is `<user>`, and the observed
`CODEX_THREAD_ID` is `01a07cc4-30a4-7380-94da-867436c06ecc`.
Both differ from the recorded proposal author's respective identifiers.

I applied Stage 8 of the already-read shared math-solver SKILL.md and read
the complete CASHOUT.md, including its unit requirements and self-check.
For this evaluation I read `unit.json`, `draft.md`, `position.md`,
`journal-excerpt.jsonl`, and `study/unit-novelty.md`. I compared them with
the full proof and prescribed origin materials independently reviewed in
the preceding RESULT review. I did not read any other reader's review or
the producer conversation.

This is a local draft evaluation. It does not provide a ResultAudit, accept
a controller result, or certify publication novelty. The separate RESULT
review approved a counterexample only to obligation-000013 and remains
bound to corrected checkpoint-000015 with full stored digest
`281085bbf548201f3de67dd6cf0b51a6c760e0e30d23c6aee5d61fe5a80d7a28`.
This evaluation does not alter that review, its public specification, or
the checkpoint. The earlier limitation on independent digest recomputation
also remains unchanged; no new hash or service audit is claimed here.

## Exact statement and unit consistency

A direct text comparison confirms that the entire statement under the
draft's Statement heading is exactly equal to `unit.json.statement`.
It is an existence claim exhibiting a sequence, not a report of activity.
The form `counterexample` is appropriate. The evidence field points to the
self-contained proof reviewed above. The unit lists move 1 and an empty
cost ledger; the supplied excerpt contains move 1 with `costs_paid: []`
and `steps: []`. Comparison of the read text confirms that the excerpt
equals the prescribed producer journal. This text comparison is not a
fresh raw-byte digest or reservation audit.

The unit's existential statement is deliberately stronger than merely
negating the auxiliary universal implication: it records additional
properties of the same exhibited sequence. Each additional property is
proved, as detailed below. This does not broaden the target of the
separate RESULT acceptance beyond obligation-000013.

Native `check-unit` passing before draft creation is reported by the user.
I did not rerun that command or infer mathematical correctness from it.

## Claim-by-claim comparison

Line numbers in the left column refer to `draft.md`. Proof references
refer to `moves/001-sparse-signed-blocks.md`.

| Draft claim | Evidence and assessment |
| --- | --- |
| Statement, line 5: infinite, nondecreasing, locally finite positive integers with numerical multiplicity two | Proof Section 1, especially (7), gives `3^j <= v_j < 2*3^j < 3^(j+1) <= v_(j+1)`. Exactly two copies are assigned to each level, and different levels have different values. This proves the stated properties and the exact multiplicity. |
| Construction and replacement, lines 13-22 | The formulas reproduce proof (1) without changes to the parameter ranges, starting level, coefficients, or endpoint subtraction. The disjoint closed blocks ensure that all interior b_j equal v_j. Proof (6) establishes upward replacement at every endpoint, and (7) gives the quoted bounds. |
| Baseline surplus, lines 24-26 | The range m >= 8 and constant `1/3` agree exactly with proof (4). The floor losses, reciprocal identity, geometric sum, and initial inequality were checked in the independent full-proof review. |
| First seed and restricted minimality, lines 28-29 | Proof Section 2 excludes starts t = 1 and 2 because k_t = 0, and t = 3 because successive closed blocks overlap at 8. Starting at t = 4 works. The draft preserves the schedule restriction and makes no global minimality claim. |
| Legal unit, signed integers, and positive intervals, lines 31-36 | Proof Section 3 supplies disjoint P_t and Q_t with signed excess 1 and exactly 4t+1 labels. Arbitrarily many later disjoint blocks remain after every cutoff. Choosing P_t or Q_t gives every integer in an interval N through N+r; combining finitely many signed units with the appropriate orientation represents any signed integer. The empty signed sum represents zero. No label is reused. |
| Every-tail gcd and modular coverage, lines 37-38 | Proof Section 4 uses a legal unit to force gcd one. Infinitely recurring residues generate the full cyclic group, or a later tail would have a nontrivial common divisor. Coefficients can be made nonnegative modulo the modulus and realized by distinct available occurrences. The construction works for every tail and every positive modulus. |
| Every noninteger real multiplier, lines 40-46 | Proof Section 5 uses the exact unit identity and Cauchy-Schwarz to give the displayed bound for all noninteger alpha, with `||alpha||^2 > 0`. Pairwise disjoint supports and the divergent sum of `1/(4t+1)` prove the assertion. This includes rational nonintegers as well as irrationals. The proof also retains the assertion after finite deletion. |
| Surplus for every fixed beta and every prefix, lines 48-52 | Proof (8) and (9) give the quoted level estimates. Combined with the upper bound for v_m, proof (14) and (15) diverge for each fixed beta in (0,1). Both the prefix before the first copy and the prefix before the second copy are treated in Section 6; the latter adds v_m to the surplus without changing the denominator. There is no uniform-in-beta or beta = 1 claim. |
| Strict labelled counting ratio, lines 54-55 | Proof (16) counts exactly two labels per level and uses the geometric bounds to obtain `A(X) = 2 log X/log 3 + O(1)`. The resulting ratio is `log 4/log 3 > 1`, as stated. |
| Coefficient encoding and numerical support, lines 56-63 | Proof (10) encodes finitely supported digits c_j in {0,1,2} uniquely in T and bounds their numerical sum below by 9T. A vector producing a positive sum at most X therefore has `1 <= T <= floor(X/9)`. This bounds the number of such vectors, hence also the number of distinct numerical sums. It does not require an injection from labels or from numerical sums into arbitrary representations. Collisions only decrease the count. Proof (17) holds for every real X >= 0. |
| No fixed central loss, lines 65-68 | Proof Section 7 shows that hypothetical fixed L and m_0 represent each integer n >= L by taking a sufficiently late prefix with total at least n+L. Since n >= L, this also ensures total at least 2L. Positivity permits such prefixes. Cofiniteness contradicts the numerical support bound, including when L = 0. |
| Auxiliary scope and analytical status, lines 72-83 | Proof Section 8 explicitly restricts the counterexample to the auxiliary inference and disclaims a pure-power instance, any pure-power profile or bridge, original objective closure, and certificate or Lean checking. The draft preserves those distinctions and presents the literature check with its limitations. |

The tail quantifiers in the opening statement are supported even under the
stronger reading that both modular coverage and arbitrarily long positive
intervals are required in every tail. The proof establishes that reading,
and the draft explicitly restates it in lines 31-38. For positive residue
zero, a nonempty subset may be obtained from a sufficiently long represented
positive interval, so this does not depend on treating the empty subset
as a positive sum.

The proof's stronger signed-integer assertion means: for each tail and
each integer z, there is a finite legal signed representation, with its
support allowed to depend on both. Likewise, the interval location and
support may depend on the tail and requested length. Neither the unit nor
the draft turns these into one fixed support, one uniform seed, or fixed
central-prefix coverage.

## References, position, and novelty limits

The draft is a concise exposition accompanied by an explicitly identified
complete proof, not a claim that its compressed argument independently
contains every estimate. Its section references all correspond to the
actual proof sections. Its literature reference identifies
`study/unit-novelty.md`, which was supplied and read. No mathematical
claim in the draft relies on an external citation or an unavailable theorem.

The position note identifies the result as an internal auxiliary route
counterexample and identifies Graham by DOI
`10.1215/S0012-7094-64-03126-6` as motivation only. The predecessor
comparison is historical positioning, not a premise of this construction.
I did not inspect the predecessor proof or Graham's paper in this
prescribed-material evaluation and do not independently certify those
historical attributions. They supply no missing mathematical dependency.

The novelty note records five first-tier requests and three focused
queries, with explicit limitations: a rate-limited response, bibliographic
records without full-text readings, a review rather than the underlying
primary theorem, and search excerpts. It explicitly avoids an exhaustive
priority conclusion. The draft makes the appropriately limited statement
that a bounded check is documented and standalone publication novelty and
broad significance are not established. I have checked that the supplied
note supports this description; I have not independently revalidated its
raw responses, searched the literature, or resolved a publication-priority
question. Those actions are unnecessary for the requested proof-to-draft
comparison and are not claimed by this pass.

The single unit properly groups the properties of one construction rather
than treating its consequences as separate results. The counterexample
does not establish a profile for a finite pure-power base set. The draft's
reference to the original quantifiers remaining open is consistent with
leaving the original universal objective unresolved; it supplies no
negative claim about already known or accepted special cases.

## Conclusion

Pass for this exact draft and unit statement. No draft revision is required
for mathematical fidelity, quantifiers, evidence attribution, or scope.
Publication novelty and external historical attribution are not certified.
Result acceptance remains a separate service action bound to the corrected
checkpoint-000015; this local evaluation changes no controller status.

Only this evaluation file was written for the additional task. No
mathematical program, solver, finite enumeration, compilation, certificate,
Lean run, Exactory controller command, or native mutation was performed.
