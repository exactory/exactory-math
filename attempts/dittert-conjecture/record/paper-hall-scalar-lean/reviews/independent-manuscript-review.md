# Independent technical manuscript review

Date: 2026-09-05.

Current disposition: PASS for the scalar main text after resolution of M1 and M2. Any subsequent exceptional-polynomial appendix remains pending separate delta review. No mathematical error or unsupported quantitative result was found in the current main text. This is an independent technical source review by a separate assistant agent, not journal peer review, a numerical paper evaluation, or a certification of publication novelty.

## Scope

The reviewed main text is the six-page manuscript in `draft/main.tex`, SHA256 `d41eca86f43e6c89cbbe2e35088eddfb2f0022a2fb5a875aa9146867bfebe248`. I compared it with `evidence/claims.json`, all five Lean source modules in `evidence/lean/`, the package configuration and manifest, both result records, `FinalScalarAxiomAudit.lean`, `final-review.md`, `resource-measurements.json`, and the bibliography and literature records. I used the previous formal review's execution data and hashes as evidence, not its verdict as a substitute for reading the sources.

No Lean execution, dependency rebuild, numerical experiment, or PDF rendering was performed in this review. The coordinator is responsible for inspecting the rendered pages. A future exceptional-polynomial appendix is not part of this review; any later delta must be recorded separately.

## Findings

### M1. Medium: the portable package retains nonportable reproduction instructions

Section 5 describes `evidence/lean/` as the portable package. Its copied README still presupposes the original attack workspace:

- Line 15 refers to `problem.json`, which is absent from the distributed directory.
- Lines 31 through 35 give `exactory-math verify lean hall-scalar-lean-n11-n15 formal-check-1`. This targets the original `attack/` layout, not the paper directory supplied to a reader.
- Line 35 invokes `initial-red-result.json`, which is absent from the paper package.
- Line 45 points to `../../study/resource-measurements.json`, which does not exist in this layout. The supplied data are at `../resource-measurements.json` relative to the README.

The manuscript's own command block builds the project, but does not execute the supplied four-declaration axiom audit. The necessary audit file exists, so the defect is documentation, not an absent proof.

Replace the portable README's operational instructions with paths that resolve within this paper package. After building, the following command from `evidence/lean/` addresses the supplied audit file:

```sh
nice -n 15 lake env lean -j1 -M2048 ../FinalScalarAxiomAudit.lean
```

Retain `LEAN_NUM_THREADS=1` and explain the expected four standard-axiom closures. Mark the Exactory invocations and original paths in the copied historical review as historical provenance, not standalone replay instructions. Link the present `../final-review.md`, `../resource-measurements.json`, and `../../draft/main.tex` where appropriate. Either provide the initial rejected skeleton record or describe it as an original-workspace record that is not needed for the final theorem. The full and finite-only historical checks can remain distinct, but their original harness layout must not be implied to exist in the portable paper package.

### M2. Low: the local comparison baseline lacks a concrete source identifier

Section 1 says the main additions are relative to a "pre-existing local scalar quadratic lemma." The evidence README names `DittertScalar`, but the paper package supplies neither that earlier source nor a stable path and hash identifying it. The present additions are visible in the final code, but the historical comparison cannot be reconstructed from this package alone.

Supply a precise provenance reference for the local baseline, or replace the historical comparison with a direct description of the modules and obligations implemented here. This does not affect attribution of the mathematics to Nascimento or correctness of the final theorem.

## Mathematical fidelity

Theorem 1, its corollary, and the two supporting lemmas match the actual Lean source. The domain is exactly natural `11 <= n <= 15`, natural `0 < a+b < n`, and real `u <= 1`. No lower bound on u appears in the statement or proof. P and delta are arbitrary real variables, subject only to the three displayed inequalities. The gamma, proper rectangle, marginal floor, proper curvature, and marginal curvature formulas agree with `Definitions.lean`. The manuscript correctly addresses positivity of denominators and the agreement of natural subtraction with the intended integer differences on the stated domain.

The finite predicate proves M positive, C positive, and `4*C*(M-gamma)-(n*M)^2` positive. The finite declarations use `decide +kernel` on explicit definitions rather than accepting an external table. `reduced_good` embeds every allowed proper pair into `Fin 15`, and `all_good` covers both marginal orientations by equality of the formulas. The completed-square identity and its sign deduction are correct. Bernoulli under `u <= 1` gives the needed lower bound, and multiplying by positive M yields strict scalar positivity. Adding the two lower bounds proves the relaxed-budget contradiction.

The coverage table is arithmetically correct. The proper counts are 45, 55, 66, 78, and 91. The uncompressed marginals contribute 20, 22, 24, 26, and 28. Adding one normalized marginal in each dimension gives 46, 56, 67, 79, and 92, totaling 340; retaining all marginals gives 65, 77, 90, 104, and 119, totaling 455. The text correctly distinguishes the named Lean cardinality results from the external combinatorial count of 455. Universal formal coverage does not depend on the explanatory count.

The tests and their import chain are described accurately. Their values `gamma 3 = 2/9` and u equal to 0, 1, and -2 match the supplied fixtures. They supplement the universally quantified proof.

## Execution and quantitative claims

The five copied source hashes exactly match those recorded in `evidence/final-review.md`. Both actual result files report `pass`, with `propext`, `Classical.choice`, and `Quot.sound`. The separate audit file prints all four named closures and checks the public theorem types. The installed toolchain and Mathlib revision stated in the manuscript agree with the actual toolchain and manifest. The local source contains no proof hole, custom arithmetic definition replacing standard operations, or extra axiom declaration.

The resource table faithfully reproduces the two selected coordinator observations: 36.05 seconds and 1,713,913,856 bytes for the standalone finite build/audit, and 20.74 seconds and 1,534,099,456 bytes for the real-theorem build/audit with finite proofs cached. These are distinct from the later independent review timings, which the manuscript does not conflate with them. The thread, niceness, memory ceiling, platform, shared-load, and incremental-build descriptions agree with the recorded data. No performance superiority, total development time, clean-build measurement, or total cost is inferred.

The wording about independent execution describes recorded separate reviewer executions. It does not constitute external peer review. The manuscript correctly distinguishes a separately audited target from an independent arithmetic implementation and discloses reliance on the installed kernel, standard axioms, and cached library environment.

## Attribution, references, and limitations

The Nascimento and Lu repository links resolve at their stated commits. The manuscript attributes the scalar argument to Nascimento's working proof and does not present that repository as a peer-reviewed or completely formalized result. The prior dimension-four statement is supported by [Li, Xiong, and Yang's version-2 abstract](https://arxiv.org/abs/2607.29191v2), which explicitly reports Lean verification. The [Cheon and Wanless publisher abstract](https://www.sciencedirect.com/science/article/pii/S0024379510004490) supports the limited structural background stated in Section 1, and [Pang's primary abstract](https://arxiv.org/abs/2606.01531) supports the adjacent scaling context.

The comparison with [Siddique and Mian](https://arxiv.org/abs/2607.26413) is supported by its description of independent rational replay and a proved-sound Lean checker. The [Cambridge Bernstein abstract](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/abs/formal-study-of-bernstein-coefficients-and-polynomials/838EFF245D1E341FE599AAF6789C2486) supports the de Casteljau attribution. The [NASA Bernstein library page](https://shemesh.larc.nasa.gov/fm/pvs/Bernstein/) identifies the Muñoz and Narkawicz formalization. [Lean's official citation guidance](https://lean-lang.org/lean4/doc) and [the Mathlib community page](https://leanprover-community.github.io/) corroborate the infrastructure references. Some direct DOI browser fetches failed, so these primary publisher, author, or project pages supplied the corroboration. This review did not audit the complete proofs or code of those external works.

The bibliography's registry record acknowledges the 2012 online-publication versus 2013 issue-year distinction for Muñoz and Narkawicz. The manuscript makes no argument based on that year. No fabricated reference or material mischaracterization was identified in the main text.

The manuscript explicitly leaves the Hall minorant, matrix permanent floors, stationarity and support arguments, marginal row selection, full cut `(0,0)`, and equality characterization outside Lean. It also excludes dimensions outside 11 through 15 and does not transfer the negative-u scalar extension to a matrix claim. These limitations are consistent with the source and evidence map. A limited formalization technical note is distinguishable from a new mathematical theorem. The reported bounded literature searches cannot establish priority or general publication novelty, and the manuscript does not claim either.

The main mathematical text passes this technical review. Resolve M1 and the minor provenance issue M2, then record a narrow documentation recheck before treating the manuscript and its portable evidence as ready for handoff.

## Recheck 1: portable reproduction correction

The coordinator revised the portable README and the manuscript's Section 5. I reread both changes without running Lean. The current `main.tex` SHA256 is `b862b0bca5ba718a57744e2bda8cdadc1b9102c235ceebb3bbb3c7fe75571f41`.

The README now supplies the actual relative paths to the manuscript, source map, final review, and resource observations. It gives the supplied audit file's correct relative path, explicitly sets the one-thread environment and Lean memory flags, distinguishes the historical `result.json` from a fresh build, and states that the initial rejected skeleton is not in the portable package. It removes the unusable Exactory replay command. Section 5 now includes the same direct four-declaration audit command. M1 is closed as a documentation finding; this recheck does not claim that the relocated package was freshly executed. M2 remains unchanged.

## Recheck 2: provenance and resource-scope correction

The coordinator replaced the Section 1 comparison with a direct implementation description and removed the unidentifiable `DittertScalar` comparison from the portable README. The retained Nascimento attribution is unchanged. I reread these edits; they resolve M2 without altering any mathematical claim. The current `main.tex` SHA256 is `0015e8cfdd88a0006e986744a17fa7d0a47f8b21ecba5be9251b5c01036e1f77`.

The resource claim in `evidence/claims.json` now applies the explicit thread and memory flags to proof builds and explicit direct audits. Section 5 separately states that the harness's lightweight axiom printer lacks those explicit command-line limits. This is the correct scope for the flags shown in the package configuration and supplied direct-audit command. The earlier general resource discussion in this review should be read with this narrower distinction; it does not establish explicit command-line limits for every internal harness subprocess. The measured wall times and RSS values are unchanged and remain observations of complete recorded invocations.

Both manuscript findings are closed. No Lean execution was performed during either documentation recheck. The scalar main text passes this technical source review. Any later n8/n9 appendix requires its own claim and evidence comparison.

## Recheck 3: near-zero appendix and portable package delta

Decision: PASS for the expanded manuscript's technical claim fidelity, including the new appendix. This resolves the appendix-pending status recorded above. No new corrective finding was identified. The reviewed `main.tex` SHA256 is `04f46947afaa73da217202785c7843e93af84c82d74876844c43f550e8368db6`.

I read the actual appendix and its changes to the abstract and scope discussion, all five near-zero Lean files, `DEFINITIONS.md`, `PROOF.md`, the portable README and replay script, `result.json`, `axioms.log`, the independent review record, and the three new entries in the now 15-entry claim map. I did not execute Lean or the Python generator. I checked that the five copied Lean source hashes agree exactly with the independently reviewed originals:

| Source | SHA256 |
| --- | --- |
| `Definitions.lean` | `1ba5f8d9c77c4d07718ab5c05965f6b648a7ac699e56433a8068aabbbd0fb1e8` |
| `Certificate8.lean` | `e9a8150d7ae343378262c085b01f4561ee0c46a2d22bc8ee572cf5a2d18b9b55` |
| `Certificate9.lean` | `b11616a9c226167abea841fe967327258e106dbdd7dc2e6191f2b4fee5f09701` |
| `Main.lean` | `29b31b7c95983bc76bbaba0f1a9e33cbdcfd639036b8e1e5d9241185a94152a5` |
| `Audit.lean` | `bcabdca362a842d47f1f53ff7b773fdb50c495b4372875dad061d532c061a451` |

The appendix defines gamma, kappa, L, E, H, T, F, and p exactly as `Definitions.lean` does for n equal to 8 or 9. In particular, H is the polynomial numerator `(1-gamma)*u`, and the last term is `(E+H)*T^(n-1)`. It has not substituted H for the rational source quantity H/E without clearing denominators. The theorem concerns the literal polynomial, has no division by E, and therefore has no omitted E-nonzero premise. The two intervals are precisely the closed intervals `[0,1/400]` and `[0,1/500]` in `near_zero_certificate`.

The expansion uses `x^k*(1-x)^(2*n-k)`. The manuscript correctly says that binomial factors are absorbed into the coefficients. All 17 and 19 displayed rational constants in the two Lean certificate files have positive numerators and denominators; their exponent pairs run through k equal to 0 through 16 and 0 through 18. The two initial coefficients printed in the appendix agree exactly with the actual constants. The text claims homogeneous basis degrees 16 and 18, which are the degrees present in those expressions.

The identity declarations quantify over every real x, unfold the literal p, normalize the factorials and constants with `norm_num`, and close the identities with `ring`. The positivity declarations handle x less than 1 using a positive k=0 term and nonnegative remaining terms, and handle x=1 separately with the positive last term. Thus x=0 and x=1 are both included. The rescalings x=400u and x=500u, both inequalities for x, and `(d*u)/d=u` match `Main.lean`. Neither an identity assumption nor a coefficient-sign assumption survives into the final conjunction. The generator is accurately described as outside the trusted proof.

The recorded final harness result is `pass`, and the actual axiom log names all five declarations with exactly `propext`, `Classical.choice`, and `Quot.sound`. The copied independent-review record contains fresh harness, direct-audit, and sequential-replay execution evidence as well as the separate 36-coefficient comparison. This manuscript review checks the use of that evidence and source fidelity; it does not claim a new execution of those checks. The axiom log's earlier timing is not presented in the appendix as the independent review's later timing.

The near-zero README's standalone inputs and paper-relative references resolve. `replay.sh` uses the caller's PATH, sets `LEAN_NUM_THREADS=1`, builds Definitions, Certificate8, Certificate9, and Main sequentially with the configured limits, and invokes the supplied `Audit.lean` using explicit `-j1 -M2048`. It does not require the original attack tree or Exactory. The README distinguishes recorded results from new replay output, explicitly requires inspection of the five expected axiom closures, and labels the copied attack notes' old paths as historical provenance. The manuscript accurately describes replay as a build and audit rather than an independent proof algorithm or an automated classifier of arbitrary future axiom lists.

The abstract, related-work paragraph, appendix, and final scope discussion agree: these are two separately bounded near-zero polynomial certificates. They do not establish full n=8 or n=9 scalar coverage, support intervals, monotone tails, support compression, matrix reductions, or an n=7 result. They are not inputs to the n=11 through n=15 positivity theorem. Existing Bernstein formalizations remain acknowledged; no generic checker, subdivision theorem, de Casteljau implementation, new mathematical theorem, or priority conclusion is claimed. The review disclosure now explicitly identifies separate assistant agents and does not imply external human peer review.

The expanded manuscript passes this technical source review with the earlier findings closed. Rendered-page inspection and the coordinator's relocated replay remain separate verification activities and are not claimed as work performed by this reviewer.
