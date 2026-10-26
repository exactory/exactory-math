# Independent CASHOUT evaluation of unit 1

Decision: pass for the exact local analytical theorem at the reviewed standard. The draft's mathematical statement matches unit.json and its complete argument is supported by the designated proof. There is no unresolved mathematical blocking objection. This is a local evaluation, not root closure, formal verification, a publication-priority certificate or a controller acceptance audit.

Reviewer actor and directly observed thread attestation: `01a07f04-836f-7e51-a610-6b8d4bd3672d`, source `host`. The actual actor ID was supplied by the operator; `printenv CODEX_THREAD_ID` independently returned that value. Both required fields differ from author actor `/root` and author attestation `01a07806-b2c5-7163-86d2-92e8e272b9eb`. I did not write the proof or delegate the review. The detailed mathematical and provenance audit is `attack/admission/common-radix-result-review.md`, relative to the study root.

## Statement and evidence matching

The opening sentence of draft.md, read with line breaks as whitespace, states the same proposition as unit.json, problem.json and checkpoint-000022. It requires finite distinct bases at least 3, gcd(D)=1, an existential common radix B>=2 with finite nonempty A, R={B^a:a in A} contained in D, nonempty C disjoint from R, sigma(R)>=1/2, gcd({B} union C)=1 and sigma(D minus (R union C))>=1. Its conclusion quantifies over every k>=1 and every finite labelled deletion F before choosing N, then represents every n>=N by a finite positive subset of remaining labels. Numerical coincidences do not identify labels.

The unit's evidence path `moves/001-common-radix-reserve.md` supplies the argument reproduced in draft Sections 1-9. I read both fully and compared their mathematical content directly. The draft changes the title and omits the move's introductory administrative metadata; its mathematical chain and scope qualifications agree with the proof. No successful machine byte comparison is claimed.

| Draft claim | Evidence and independent finding |
| --- | --- |
| Fresh signed units plus a disjoint fixed-gap reserve imply eventual completeness | Proof Sections 1 and 7. Taking g-1 disjoint pairs yields every H+t, and a reserve sum in the specified g-integer interval supplies the complement. |
| The normalized R tail represents B^L Z with signed coefficients | Sections 2-3. The label map is injective; strict-prefix geometric sums imply w<=2W+1, including ties and half-mass equality. |
| Correction labels give a fresh exact signed unit | Section 4. Recurrence and collective gcd give a positive z congruent to 1; the signed R lattice represents 1-z. Increasing K avoids both signs of every prior pair and all forbidden labels. |
| The positive reserve has a finite gap fixed before amplification | Sections 5-6. Strict-power prefix sums, finite deletion loss M and the union-of-translates gap induction give g=ceil(M), including sigma(U)=1. |
| All positive cutoffs, finite deletions and coincident labels are retained | Sections 3-7. Original exponents remain at least k; R,C,U have disjoint base labels and every final support is finite. |
| Additional scope with 4,8,32 and no16 below total mass2 | Section 8. The least-M harmonic construction has reserve mass in [1,6/5); 331/651+1/4+6/5=25499/13020<2. |
| Larger radices are vacuous and no separate collective-coprimality advance is asserted | Section 8. B/(B-1)^2<=4/9 for B>=4, and the B=3 tail without 3 has mass at most1/4. |

The first-pair construction works for either sign of the lattice coefficient. The first weight, repeated weight1 labels, exact-power exclusion, nonnegative interval endpoint, zero-pair case, and arbitrary finite forbidden support are all handled. The gap is independent of all later seed choices. The proof does not claim completeness from signed units alone.

## CASHOUT self-check and form

The statement is one quantified mathematical claim, not a report of activity. All of its hypotheses are explicit. The substantive contribution is the positive-tail theorem for variable common-radix seed families with an untouched reserve. Its elementary signed-prefix component is not claimed new.

The permitted literature record identifies no exact prior theorem or short deduction from an identified prior theorem covering this full structural statement. The old fixed-alphabet results alone do not cover the no16 example. This establishes additional scope relative to the supplied comparison claims. It does not establish that nobody has proved the result: the saved searches are limited web-index queries and no exhaustive priority review was authorized or performed. Publication-level novelty remains unverified.

The result lies on a route toward the original problem but does not cover the root's complementary configurations. The position note names obligation-000032 and the earlier comparison acceptance IDs without treating them as proof dependencies. This is an appropriate local `full-proof` form because the exact admitted node claim is proved. Relative to the original objective it remains a structural special case.

The unit lists move1 and an empty cost ledger. The supplied journal and its excerpt both describe the same single constructive closing move, contain no deterministic steps and have empty `costs_paid`. The claimed ledger therefore matches the supplied evidence. No `object` or `obligations` cost is concealed by changing the theorem statement. Native reservation validity and check-unit digest validation remain service checks; I did not run them.

The CASHOUT full-proof requirements are addressed as follows. The complete local argument is present, with its lemmas proved and elementary arithmetic foundations used normally. There are no deterministic runs on which the proof depends. Independent verification here is the independent analytical ResultReview required by the checkpoint's `reviewed` proof policy; no certificate or Lean verification record exists or is asserted. The formal/certificate-specific evidence fields described in CASHOUT cannot be reported as satisfied by a build or checker, and this evaluation confers neither stronger standard. The consolidation record names the formerly delicate transitions, explains their replacements, and restates the argument. No second proof or formalization was performed. The closing problem record states direction `true` and mode `construction`, consistent with the proof. This interpretation preserves SEARCH.md's express analytical reviewed route and the task's prohibition on mathematical execution.

## Reference resolution and source limits

The full reading inventory and exact limits are in the companion result-review report. All fourteen manifest artifacts and all four unit-level raw input/response files were read. REFERENCE_PATHS.md resolves historical relative source paths from `attack/preflight/common-radix-reserve/`.

- The classical weighing-source mention in draft Section9 resolves through problem.json and study/problem.md to Bolker, Feuer and Zara, *Balance weighing: variations on a theme*, Mathematics Magazine 94(5), December2021, `https://www.cs.umb.edu/~eb/weighing.pdf`. The complete saved excerpt was read; lines82-162 contain the relevant classical criteria. The present proof supplies its own induction and does not import the source's other claims.
- The original positive-cutoff statement resolves to `Erdos124.erdos124.ne_zero` in `https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/124.lean`. The complete saved94-line response was read. Its per-base exponent subsets preserve labels across bases. Its unproved declarations are statement references only.
- The background BEGL96 citation resolves in the study to *Complete sequences of sets of integer powers*, Acta Arithmetica77(2),133-138, DOI `10.4064/aa-77-2-133-138`, Zbl `0863.11014`. Relevant saved zbMATH metadata was inspected. I did not read its complete paper or independently validate its DOI through a live resolver; it is not a mathematical dependency of this unit.
- The local comparisons resolve to acceptance-000006, acceptance-000007 and acceptance-000008, whose exact statements appear in the prescribed review context. I used those statements only, without opening their reviews. Checkpoint20/node15 resolves to the pending predecessor proof path named in REFERENCE_PATHS.md; it was not opened or relied on as accepted evidence.
- The unit-level methodological report resolves to `https://www.starfleetmath.com/`, problem254, saved source lines200-319. Its displayed shell-divergence hypothesis fails for any finite union of the present pure-power streams, which has at most |D| labels per dyadic shell. Its claimed external verification was not checked and supplies no proof evidence here.

The draft's source mentions resolve through this local evidence package. A publication could improve its self-contained bibliography, but that is an editorial matter and not an unresolved mathematical or local source-matching defect. The current addendum in novelty.md explicitly supersedes its preserved preflight status paragraph. Neither those historical status descriptions nor incidental outside verification claims are evidence of present controller acceptance.

## Remaining limits

No mathematical objection remains within the exact reviewed claim. The automatic math-solver PreToolUse hook rejected attempted direct `shasum` and `diff` inspections before execution. No independent file hash or byte comparison was obtained, and no bypass was attempted. The controller must still audit supplied digest bindings, frozen bytes, journal provenance and acceptance policy. This review does not itself certify those checks.

No author conversation, scratchpad, other review or progress report was inspected. No mathematical program, finite enumeration, native lifecycle command, controller command or external formal project ran. The original mass-one objective, arbitrary-base half-mass assertion, complementary cases, implication bridges, formal verification if separately required, and exhaustive publication novelty remain outside this pass.
