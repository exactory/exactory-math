# Final independent verification and statement review

Review date: 2026-09-05. Workspace: `exactory-research/dittert-conjecture`.

## Verdict

The completed formal artifact passes the requested independent verification. Fresh harness invocations passed for both packages, and a separate direct Lean audit confirmed that `HallScalar.scalar_positive` itself depends only on `propext`, `Classical.choice`, and `Quot.sound`. The completed source contains no proof hole, custom axiom, native evaluation axiom, or local redefinition of arithmetic. No blocking or corrective mathematical finding was identified.

The verified result is the exact scalar claim in `problem.json`: for natural `11 <= n <= 15` and `0 < a+b < n`, with the specified rational constants M and C, every real `u <= 1` satisfies

```text
0 < C*u^2 + M*(1-u)^n - gamma(n).
```

Consequently, the three scalar inequalities `P >= M*(1-u)^n`, `delta >= C*u^2`, and `P+delta <= gamma(n)` cannot hold simultaneously. The finite audit also certifies all normalized cases and their total cardinality 340.

This verifies a finite scalar layer of the Hall argument. It does not formalize the matrix reduction, prove the relevant permanent floors for matrices, derive the deficit bounds from stationarity or optimization, exclude the full minimizing cut, or prove the full Dittert conjecture in Lean.

## Sources and provenance

I re-read the completed `Definitions.lean`, `Finite.lean`, `Main.lean`, `Tests.lean`, and `Audit.lean` in `deterministic/formal-check-1`, both source files in `deterministic/formal-check-2`, both package configurations and manifests, and both actual `result.json` records before and after verification. This review supersedes the earlier snapshot's proof-completion limitation in `study/statement-review.md`; that earlier report is preserved unchanged.

Both package toolchains specify Lean `v4.33.1`. Their manifests pin Mathlib to commit `0df444a360eaa60ab8c11dca51a86af692955474`. Read-only Git checks found both installed Mathlib checkouts at that exact commit and no tracked modifications. The manifests use repository URLs and revisions, not absolute dependency paths.

Source SHA256 values were checked before and after all verification commands and remained identical:

| Source, relative to `deterministic/` | SHA256 |
| --- | --- |
| `formal-check-1/Definitions.lean` | `24d9263bcb77e088f48113aa7e516cd11eb097c583655ac5b543309b11f90f62` |
| `formal-check-1/Finite.lean` | `f3b5d3f788a8a613fba1002c4cc3339d153a3198b4ebdf6cc6b09843f6fc7071` |
| `formal-check-1/Main.lean` | `f568446c9b4ffd533da37b544903acd2fd72c00635f85456516152b6c89c4dbf` |
| `formal-check-1/Tests.lean` | `c83ba0518bd6fcfe5dfd089f07593665f51a2e3391cb201980ef2d48bacaa6f4` |
| `formal-check-1/Audit.lean` | `f349f4fdff4b8e39c24e8cd8277b980a9940a98dc209e4260473cbb55e1f7b1b` |
| `formal-check-2/Definitions.lean` | `24d9263bcb77e088f48113aa7e516cd11eb097c583655ac5b543309b11f90f62` |
| `formal-check-2/Finite.lean` | `f3b5d3f788a8a613fba1002c4cc3339d153a3198b4ebdf6cc6b09843f6fc7071` |

The second package reuses the same finite proof and definitions. It separately audits the finite-family and cardinality theorem; it is not an independently implemented mathematical proof or an independent arithmetic algorithm.

## Fresh verification evidence

The following commands ran sequentially with exclusive use of the Lean computation slot. Every CLI invocation exported the requested environment:

```sh
export PATH=<home>/.codex/plugins/cache/exactory-ai/exactory/0.33.1/bin:<elan>/bin:$PATH
export LEAN_NUM_THREADS=1
```

From the research root, the first invocation was:

```sh
/usr/bin/time -l nice -n 15 exactory-math verify lean hall-scalar-lean-n11-n15 formal-check-1
```

After its completion, the second invocation was:

```sh
/usr/bin/time -l nice -n 15 exactory-math verify lean hall-scalar-lean-n11-n15 formal-check-2
```

Both package configurations set `moreLeanArgs = ["-j", "1", "-M", "2048"]`. The harness implementation was inspected: it runs `lake build` and then imports the configured target module to print the target declaration's transitive axioms. Both commands exited with status 0 and regenerated their package's `result.json` with `status: pass` and `reason: null`.

| Invocation | Audited declaration | Wall seconds | User seconds | System seconds | Maximum RSS, bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| `formal-check-1` harness | `hall_scalar_certificate` | 20.62 | 2.22 | 6.62 | 1493647360 |
| `formal-check-2` harness | `HallScalar.finite_certificate` | 16.00 | 2.16 | 6.67 | 1493909504 |
| Direct Lean audit | Four declarations listed below | 5.24 | 1.09 | 3.38 | 1497120768 |

The harness verdicts were:

```text
pass: hall_scalar_certificate depends on axioms propext, Classical.choice, Quot.sound
pass: HallScalar.finite_certificate depends on axioms propext, Classical.choice, Quot.sound
```

These are fresh verification invocations using existing local dependencies and Lake's build cache. They are not measurements of a clean rebuild of Mathlib or of the complete package from an empty cache. No Mathlib rebuild or download was requested. No source cleanup, manual deletion, or Git mutation was performed.

## Direct audit of the positivity theorem

I created `study/FinalScalarAxiomAudit.lean` with `apply_patch`. It imports `Audit`, checks the fully quantified public theorem types, prints four transitive axiom closures, and prints the imported arithmetic definitions. With the environment above exported again, I ran this command from `deterministic/formal-check-1`:

```sh
/usr/bin/time -l nice -n 15 lake env lean -j1 -M2048 ../../study/FinalScalarAxiomAudit.lean
```

It exited with status 0. The exact axiom outputs were:

```text
'HallScalar.scalar_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'HallScalar.scalar_exclusion' depends on axioms: [propext, Classical.choice, Quot.sound]
'HallScalar.finite_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
'hall_scalar_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The printed theorem types have precisely the intended natural-size restrictions, `u <= 1`, and, for exclusion, the three displayed scalar inequalities. The printed definitions are the direct factorial, power, rational-division, and piecewise formulas shown in the source. The additional audit directly checks positivity, so the result does not rely solely on inspecting the closure of a conditional infeasibility theorem.

## Final proof and fidelity review

All locations below refer to `deterministic/formal-check-1`, whose source hashes are recorded above.

`Definitions.lean:11` through line 24 match the source argument's gamma, proper rectangle floor, one-zero floor, proper curvature, and marginal curvature. All division is rational division. On `0 < a+b < n`, every omitted-size difference has its intended integer value despite Lean's truncated natural subtraction. In the proper case, the gamma arguments and denominator terms are positive; in the marginal case `n >= 11` makes `n-1` and `n-2` positive. No cast changes the intended formulas. The only local instances are `Decidable` instances inferred for the displayed propositions. There is no local arithmetic instance, custom notation, replacement of the real or rational types, or alternative factorial definition.

`Finite.lean:10`, 16, 22, 28, and 34 use `decide +kernel` to verify `Good` directly for every reduced ordered pair in `Fin 15 × Fin 15`. The criterion includes `M>0`, `C>0`, and `4*C*(M-gamma)-(n*M)^2>0`. It does not import a generated table of successful rational margins as a premise. `reduced_good` at line 57 proves that every permitted natural pair embeds in the actual finite universe, including marginal coordinate 14 at n=15. `all_good` at line 80 covers both marginal orientations and all proper pairs.

The proper counts are 45, 55, 66, 78, and 91, totaling 335. Adding one normalized marginal pair per dimension gives the formally checked counts 46, 56, 67, 79, and 92, totaling 340. Every ordered proper pair is checked, without quotienting by transposition. The uncompressed domain contains 455 ordered natural triples: the 335 proper cases and 120 marginal sizes and orientations. Constant equality proves their coverage; the theorem does not assert that 340 is the uncompressed count.

`Main.lean:6` proves the completed-square lemma using a polynomial identity, square nonnegativity, and positive curvature. `Main.lean:17` obtains the finite criterion, transports its rational inequalities to the reals using `Rat.cast_pos` and `exact_mod_cast`, and applies that lemma. At line 30 it uses Mathlib's `one_add_mul_le_pow`. The installed Mathlib statement at `Mathlib/Algebra/Order/Ring/Pow.lean:100` assumes `-2 <= a`; substituting `a=-u` is justified by the stronger hypothesis `u<=1`. Thus there is no hidden lower bound on u and no unproved assumption about the sign of `(1-u)^n`. Multiplication uses the proved positivity of M. The final nonlinear arithmetic step combines exactly these inequalities.

`Main.lean:35` proves infeasibility by adding the two lower bounds and comparing with the budget. `Audit.lean:4` states the same infeasibility theorem with the explicit hypotheses and delegates to that completed proof. There is no additional hidden matrix premise or unmentioned scalar hypothesis. The previously disclosed temporary `sorry` is absent from the completed source and from all four audited axiom closures.

`Tests.lean:7` checks the hand-derived gamma value `gamma 3 = 2/9`. Lines 9 through 12 check the proper boundary, the excluded `a+b=n` boundary, the normalized marginal pair, and exclusion of the full pair from `Reduced`. Lines 14 through 22 instantiate the public positivity theorem at u=0, u=1, and negative u, including a non-normalized marginal pair in the opposite orientation. These fixtures are elaborated through the `Audit -> Tests -> Main` import chain. They supplement the universally quantified proof; they are not its coverage argument.

## Limitations and findings

There are no unresolved proof holes, axiom-gate failures, statement mismatches, or finite-coverage blockers in this artifact. The scope limitations are substantive and should remain explicit in the README and manuscript:

1. Marginal normalization in `Finite.lean:80` is equality of the defined scalar constants. The source argument selecting a smallest row and deriving the stationarity bound for an actual matrix remains outside Lean.
2. The full pair `(0,0)` is excluded by `0<a+b`. Its analytical matrix exclusion is not supplied by the scalar certificate.
3. The matrix deficit and permanent interfaces, structural exclusions, and all other steps needed to prove a Dittert matrix theorem are not formalized here. The extension to negative u is a scalar polynomial result, not an extension of those analytical matrix interfaces.
4. The dimension range is exactly 11 through 15. No monotonicity argument or result for n=7 through 10 or n>15 is claimed.
5. The trusted foundation includes the installed Lean kernel, the stated standard axioms, and the cached compiled library environment. This review did not rebuild all library dependencies from source or execute a separate proof-assistant kernel.

The defensible final claim is that the specified finite scalar theorem, its infeasibility corollary, and exhaustive normalized finite-family cardinality are verified in Lean under the three printed standard axioms. Describing this as a complete Lean proof of the Dittert conjecture, or describing the second package as an independent implementation, would exceed the verified evidence.
