# Lean projects

Every project uses the toolchain `leanprover/lean4:v4.33.1`. All except `certificates-n5-n6` depend on Mathlib `v4.33.1`, commit `0df444a360eaa60ab8c11dca51a86af692955474`, pinned in `lake-manifest.json`. No project includes its `.lake/` directory; `lake exe cache get` downloads the Mathlib build. "Standard axioms" below means that `#print axioms` lists only `propext`, `Classical.choice` and `Quot.sound`.

The description, harness verdict (`result.json`) and logs of each step stay in the record, at the path given in the second column.

| Folder | Step in the record | Main declarations | Status as the record states it |
|---|---|---|---|
| `kafidov-threshold/` | `record/attack/dittert-conjecture-n5-to-n15/deterministic/formal-check-1` | `kafidov_inequality_16 : 0 < kafidovK 16`, `kafidov_fails_15 : kafidovK 15 < 0`, where `kafidovK n` is the quantity whose positivity is the final inequality (4.3) of arXiv:2607.19439; `dittert_five`, `dittert_five_stability` | pass: `kafidov_inequality_16` has standard axioms. `dittert_five` (Dittert at $n = 5$) and `dittert_five_stability` (the constant 32/3125) are stated and proved by `sorry`. |
| `certificates-n5-n6/` | `.../formal-check-2` | `certOK56_true : certOK56 () = true`, the arithmetic of the $n = 5$ and $n = 6$ certificates (orbits, Gram matrices, positive semidefiniteness, coefficient identity) in core Lean without Mathlib | status `evidence`: the proof is `native_decide`, so the axioms include `certOK56_true._native.native_decide.ax_1_1`. The $8436 \times 8436$ main Gram matrix at $n = 6$ is checked by a floating-point Cholesky factorization with Higham's bound. The step from these checks to the matrix theorem is not formalized. |
| `scalar-interface/` | `record/attack/dittert-completion-tree/deterministic/certified-special-case-check-4` | `DittertScalar.positive_quadratic`, `DittertScalar.exclusion` | pass: both have standard axioms. A scalar lemma only; the matrix proof does not depend on it. |
| `hall-scalar-n11-n15/` | `record/attack/hall-scalar-lean-n11-n15/deterministic/formal-check-1` | `HallScalar.scalar_positive`: for natural $11 \le n \le 15$ and $0 < a + b < n$ and every real $u \le 1$, $C u^2 + M (1-u)^n - \gamma_n > 0$ with the rational constants of `Definitions.lean`; `HallScalar.scalar_exclusion`; `hall_scalar_certificate` | pass: standard axioms, confirmed by an independent final review (`study/final-review.md`). Scalar layer only; the matrix reduction and the full cut are not formalized. |
| `hall-scalar-n11-n15-finite/` | `.../formal-check-2` | `HallScalar.finite_certificate` (340 normalized cases) | pass: standard axioms. Same `Definitions.lean` and `Finite.lean` as the previous project, audited separately. |
| `near-zero-n8-n9/` | `record/attack/hall-near-zero-lean-n8-n9/deterministic/formal-check-1` | `near_zero_certificate`: $p_8(u) > 0$ for every real $u \in [0, 1/400]$ and $p_9(u) > 0$ for every real $u \in [0, 1/500]$, with $p_n$ as in `DEFINITIONS.md` of that attack | pass: `near_zero_certificate` and the four lemmas `NearZero.identity8`, `positive8`, `identity9`, `positive9` have standard axioms. |
| `blueprint/` | `record/scratch/lean-draft` (the blueprint of the managed objective `objective-000001`) | `Dittert.Root`, the statement of the whole claim over `Matrix (Fin n) (Fin n) ℝ` with `Matrix.permanent`; the obligation statements in `Dittert/Obligations.lean`; proofs of several obligations | partial, see the next section. `Dittert.dittert_5_15` depends on `sorry`. |

## The blueprint

`Dittert/Basic.lean` defines the statement and `Dittert/Obligations.lean` the shared obligations. `Dittert.lean` assembles `Dittert.dittert_5_15 : Root` from the obligations and bridges; its docstring states that `#print axioms Dittert.dittert_5_15` reports `sorryAx` until every node is proved. In this copy, `Dittert.lean` declares seven obligations with `sorry` (`core_entropy`, `maximizer_zero_pattern`, `two_zero_floor`, `scalar_certificates_7`, `scalar_certificates_8`, `scalar_certificates_11`, `case_5_6`), and `Dittert/Bridges.lean` proves `bridge_assembly` and `bridge_11` and leaves `bridge_7` and `bridge_8` as `sorry`.

Accepted by the controller under its lean-kernel policy (standard axioms; harness results in `record/attack/<node>/deterministic/formal-check-1/`). The files listed are byte-identical to the files the controller froze for the accepted step:

| Obligation | Theorem | Files | Node | SHA-256, first 16 hex digits |
|---|---|---|---|---|
| obligation-000006: if every maximizer of $\Phi$ on $K_n$ is entrywise positive, the statement holds at $n$ (every $n \ge 2$) | `Dittert.reduction : Dittert.Reduction` | `Dittert/Reduction.lean` | `reduction-to-boundary` | `6096b1c271b3e49e` |
| obligation-000007: Hall domination, a doubly stochastic $B$ with $\lambda B \le A$ under the cut condition | `Dittert.hall_domination : Dittert.HallDomination` | `Dittert/Hall.lean` | `hall-domination` | `ff0f3b543ac416d1` |
| obligation-000008: van der Waerden and the rectangle floor $\gamma_{n-a}\gamma_{n-b}/\gamma_{n-a-b}$ for doubly stochastic matrices | `Dittert.gurvits_floors : Dittert.GurvitsFloors` | `Dittert/Floors.lean`, `Floors/Analytic.lean`, `Floors/Chain.lean` | `gurvits-floors` | `09232c4f8d901f55`, `1a2ac3a0e0a80196`, `aa234ad2b1077e65` |
| obligation-000009: the complementary-minor entropy lemma | `Dittert.core_entropy : Dittert.CoreEntropy` | `Dittert/Entropy.lean`, `Entropy/AMGM.lean`, `Entropy/Algebra.lean`, `Entropy/Minor.lean` | `core-entropy` (accepted; its cash-out evaluation was pending when work stopped) | `6192eacf7e0595da`, `4306c09c0e5a006c`, `0f51ed008a025526`, `d1865177d548a4b5` |

`Dittert/Basic.lean` (`41590e2575a93f24`) and `Dittert/Obligations.lean` (`5928ea37a1ac324f`) are also identical to the frozen copies.

Proved in the blueprint and reviewed, but not accepted by the controller when work stopped (record/STATUS.md): `Dittert.scalar_certificates_11` (`Dittert/Scalar/Cert11.lean`), `Dittert.scalar_certificates_8` (`Dittert/Scalar/Cert8.lean` and `Dittert/Scalar/Cert/*.lean`; the support certificates were generated by `record/scratch/ctl/gen_support.py`), `Dittert.bridge_11` (`Dittert/Bridges.lean`, `Dittert/Bridge/N11.lean`) and `Dittert.bridge_assembly`. The record reports standard axioms for these four.

Not proved in Lean: the $n = 5, 6$ case (no route), the maximizer zero pattern, the two-zero floor, the $n = 7$ scalar certificates, the bridges for $n = 7$ and $8 \le n \le 10$, and therefore the root theorem.

Not included here, so the blueprint does not build from this folder alone:

- `GurvitsPort/`, the record's port of the Gurvits and van der Waerden part of D. C. P. Revere's maths-pub Lean development ([repository](https://github.com/DCPRevere/maths-pub), commit `0a1cb0a14fefe85668365d448f9bbaf4dd89d458`, Apache-2.0, Zenodo DOI 10.5281/zenodo.21902861) from Lean v4.32.2 to v4.33.1. It is third-party code. The floors and entropy modules import it.
- `Dittert/Bridge/Common.lean`, the record's 795-line module of common bridge lemmas. It is withheld because it contains three theorems (the Laplace expansions `permanent_succ_column_zero`, `permanent_succ_column`, `permanent_succ_row`) ported from `PermanentExpansion.lean` of maths-pub. `Dittert/Bridge/N11.lean` imports it.
- the draft's scratch tests (`TestDecide8*.lean`, `EvalCheck.lean`, `Audit2.lean`).

Two configuration lines were edited in this copy. In `lakefile.toml` the line `packagesDir = ...` was removed, and in `lake-manifest.json` the value of `packagesDir` was changed to `.lake/packages`; both originally pointed to a Mathlib checkout on the machine where the record was made. The `.lean` files are unchanged.

## How to build and check

Each block runs from the project folder. The memory limits come from each `lakefile.toml`; the blueprint sets `-M 16384`.

```sh
# kafidov-threshold: the build warns that dittert_five and dittert_five_stability use sorry
lake exe cache get && lake build
# axioms of the threshold theorems: put the two lines
#   import Main
#   #print axioms kafidov_inequality_16
# in a file Check.lean and run
lake env lean Check.lean
# expected: 'kafidov_inequality_16' depends on axioms: [propext, Classical.choice, Quot.sound]

# scalar-interface: no lakefile; use the Mathlib build of kafidov-threshold
cd ../kafidov-threshold && lake env lean ../scalar-interface/Main.lean
# expected: 'DittertScalar.positive_quadratic' and 'DittertScalar.exclusion' depend on axioms:
#   [propext, Classical.choice, Quot.sound]

# certificates-n5-n6: core Lean only; building the default target runs native_decide
lake build
# about 62 minutes of compiled evaluation in the record; prints
#   'certOK56_true' depends on axioms: [propext, Classical.choice, Quot.sound,
#   certOK56_true._native.native_decide.ax_1_1]

# hall-scalar-n11-n15
lake exe cache get && lake build && lake env lean FinalScalarAxiomAudit.lean
# expected: scalar_positive, scalar_exclusion, finite_certificate and hall_scalar_certificate
#   each depend on axioms: [propext, Classical.choice, Quot.sound]

# hall-scalar-n11-n15-finite
lake exe cache get && lake build
# the harness audited HallScalar.finite_certificate: standard axioms

# near-zero-n8-n9
lake exe cache get && lake build && lake env lean Audit.lean
# expected: five lines, identity8, positive8, identity9, positive9 and near_zero_certificate,
#   each depending on axioms: [propext, Classical.choice, Quot.sound]

# blueprint: only the modules that need neither GurvitsPort nor Bridge/Common
lake exe cache get
lake build +Dittert.Reduction +Dittert.Hall +Dittert.Scalar.Cert11 +Dittert.Scalar.Cert8
lake env lean AuditScalar.lean
# the record reports standard axioms for scalar_certificates_8 and scalar_certificates_11;
# Support9z7.lean took 80 s to build in the record
```

`FinalScalarAxiomAudit.lean` was in `study/` of the attack `hall-scalar-lean-n11-n15`; the record ran it from the project folder with `lake env lean ../../study/FinalScalarAxiomAudit.lean`.
