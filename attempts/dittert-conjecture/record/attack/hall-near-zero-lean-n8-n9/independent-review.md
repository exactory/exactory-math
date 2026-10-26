# Independent review of the n=8,9 near-zero formalization

Date: 2026-09-05. Verdict: PASS for the exact bounded scalar claim and its local formalisation unit. No blocking or corrective mathematical finding was identified.

This is a separate review from the earlier n=11,...,15 scalar audit. The reviewer did not write the n=8,9 implementation or draft. Before reviewing, I read the installed math-solver Codex README, shared workflow including Stage 8, and CASHOUT.md. I inspected the current problem, definitions, proof, attempts, studies, unit, draft, position, journal excerpt, complete formal package, and recorded results. I then reran verification rather than adopting the author's verdict. The author checkpoint CP-29b31b7c95983bc7 was left unchanged, including its historical independent-review-pending status.

## Exact claim and formula fidelity

`Main.lean:4` proves exactly

```text
(forall u : Real, 0 <= u -> u <= 1/400 -> 0 < p 8 u)
and
(forall u : Real, 0 <= u -> u <= 1/500 -> 0 < p 9 u).
```

These are closed intervals. There is no supplied coefficient list, coefficient-positivity hypothesis, strict upper-endpoint restriction, numerical tolerance, matrix premise, or unmentioned denominator condition.

`Definitions.lean:7` through line 17 implement the formula in `DEFINITIONS.md` term by term. Gamma is `n!/n^n`; kappa is `(n-2)!*((n-2)/(n-1)^2)^(n-2)`; lower is kappa times `1+1/(2*n^2)`. All relevant divisions are real-field divisions. Natural subtraction occurs in factorial arguments and powers, and has the intended value at n=8 and n=9. The remaining differences use real arithmetic. There is no local arithmetic replacement or alternative factorial implementation.

I compared this with the inherited `hall-n8-n15-branch-coverage/PROOF.md`, Section 6, and `deterministic/certified-witness-chain-1/independent_coverage.py`, particularly `base_polys` at line 189, `near_poly` at line 199, `quantities` at line 223, and `near_literal` at line 234. The literal polynomial is exactly the one constructed by `near_poly`.

The distinction between the numerator H and the inherited rational quantity h is essential and is correct here. In the inherited checker, h=H/E, whereas Lean's `NearZero.h` is H. For E nonzero,

```text
(1+H/E)*(1-H/((n-1)*E))^(n-1)*E^n
  = (E+H)*(E-H/(n-1))^(n-1)
  = (E+H)*T^(n-1).
```

Thus the stated polynomial equals `near_literal`, which multiplies the inherited near-zero deficit expression by E^n. The formula has not replaced H/E by H inside the original deficit expression; it has correctly cleared the denominators. The formal theorem itself concerns the polynomial and does not divide by E.

For the informal connection on these intervals, `0<gamma<1` gives `E>=1-2u>=199/200>0`, and `0<=H/E<=1/398<n-1`. These elementary bounds justify the inherited checker's denominator domain at both dimensions. This review does not assert that those domain bounds or the matrix application are additional Lean theorems in this package.

## Identity, coefficients, and endpoints

`Certificate8.lean:31` and `Certificate9.lean:33` prove literal identities for every real x, without interval or coefficient assumptions. They unfold `p`, its defining constants, factorials, and the actual certificate expression, then use `norm_num` and `ring`. These are proof-producing tactics checked by Lean. The Python generator is not an imported premise.

The certificates use the unnormalized basis `x^k*(1-x)^(N-k)`, with N=16 and N=18. Their displayed constants already include the binomial factor relative to normalized Bernstein coefficients. I added `study/independent_coefficient_review.py`, which does not import or execute `generate_certificate.py`. It computes the inherited `near_poly` through its separate Bernstein arithmetic and compares `choose(N,k)*b_k` against every actual rational constant parsed from the Lean source. All 17 and 19 constants, exponents, and metadata entries match exactly and are strictly positive. The leading coefficients after expansion are nonzero, confirming exact degrees 16 and 18. The script also checks four rational evaluation points per interval against `near_literal`; these evaluations are regression checks, not the proof of the full polynomial identity. The full identity is supplied by Lean.

`positive8` at line 35 and `positive9` at line 37 establish strict positivity on all of [0,1]. For x<1, the k=0 term is positive, including x=0; every other term is nonnegative. For x=1, the separately checked last term is positive. `Main.lean` rescales x=400*u or x=500*u, proves both bounds on x, rewrites the exact identities, and proves `(d*u)/d=u`. No endpoint is omitted.

The independent coefficient check also verified that the unit's journal excerpt is exactly the selected full-journal move and that `candidate-data.json` agrees with the actual Lean constants. The JSON and external arithmetic remain auxiliary evidence; the final theorem does not assume their correctness.

## Fresh commands and results

Every Lean or Exactory shell invocation exported the following environment separately:

```sh
export PATH=<home>/.codex/plugins/cache/exactory-ai/exactory/0.33.1/bin:<elan>/bin:$PATH
export LEAN_NUM_THREADS=1
```

Commands ran sequentially in the sole mathematical computation slot, using cached dependencies. From the research root:

```sh
/usr/bin/time -l nice -n 15 exactory-math verify lean hall-near-zero-lean-n8-n9 formal-check-1
```

From `deterministic/formal-check-1`:

```sh
/usr/bin/time -l nice -n 15 lake env lean -j1 -M2048 Audit.lean
```

From the research root:

```sh
/usr/bin/time -l nice -n 15 python3 attack/hall-near-zero-lean-n8-n9/study/independent_coefficient_review.py
```

Finally, from the formal package:

```sh
/usr/bin/time -l ./replay.sh
```

The replay script itself applies `nice -n 15` to each Lean command. It builds Definitions, Certificate8, Certificate9, and Main sequentially, then executes Audit.lean with explicit `-j1 -M2048`. The package configuration applies these flags to proof compilation. The harness's separate lightweight axiom-print subprocess uses its built-in invocation without explicit memory flags; the direct audit and replay audit supply the explicitly constrained checks. This is already disclosed in ATTEMPTS.md and the package README.

| Check | Result | Wall seconds | User seconds | System seconds | Maximum RSS, bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| Fresh harness | pass, exit 0 | 21.14 | 2.11 | 6.98 | 1507786752 |
| Direct Audit.lean | exit 0 | 7.77 | 1.18 | 3.78 | 1506852864 |
| Independent coefficient review | pass, exit 0 | 0.10 | 0.04 | 0.02 | 14630912 |
| Standalone replay.sh | exit 0 | 31.84 | 3.77 | 13.35 | 1506197504 |

The freshly regenerated `result.json` records `status: pass`, `theorem: near_zero_certificate`, and `reason: null`. Both direct audit executions printed exactly:

```text
'NearZero.identity8' depends on axioms: [propext, Classical.choice, Quot.sound]
'NearZero.positive8' depends on axioms: [propext, Classical.choice, Quot.sound]
'NearZero.identity9' depends on axioms: [propext, Classical.choice, Quot.sound]
'NearZero.positive9' depends on axioms: [propext, Classical.choice, Quot.sound]
'near_zero_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The standalone replay therefore exposes every principal declaration's transitive axiom closure. Its audit prints the lists; it does not itself classify future lists against an allowlist. The fresh Exactory harness supplied that classification for the current final theorem, and this reviewer inspected all five current lists.

No `sorry`, custom axiom, native evaluation axiom, custom arithmetic instance, or local notation replacing arithmetic appears in the final sources or audited dependencies. The `noncomputable` declaration permits definitions over the standard real field and is not a new axiom or an unchecked proof mechanism.

These timings measure cached incremental verification, not clean builds or total development time. No full Mathlib rebuild, download, publication, commit, manual deletion, or checkpoint mutation was performed. The mathematical computation slot was released after the replay completed.

## Pins and reviewed hashes

The toolchain is Lean v4.33.1. The manifest and installed Mathlib checkout both identify commit `0df444a360eaa60ab8c11dca51a86af692955474`; the checkout had no tracked modifications. Proof-source hashes were unchanged across the review checks. SHA256 values follow; package paths are relative to `deterministic/formal-check-1` unless stated otherwise.

| File | SHA256 |
| --- | --- |
| `Definitions.lean` | `1ba5f8d9c77c4d07718ab5c05965f6b648a7ac699e56433a8068aabbbd0fb1e8` |
| `Certificate8.lean` | `e9a8150d7ae343378262c085b01f4561ee0c46a2d22bc8ee572cf5a2d18b9b55` |
| `Certificate9.lean` | `b11616a9c226167abea841fe967327258e106dbdd7dc2e6191f2b4fee5f09701` |
| `Main.lean` | `29b31b7c95983bc76bbaba0f1a9e33cbdcfd639036b8e1e5d9241185a94152a5` |
| `Audit.lean` | `bcabdca362a842d47f1f53ff7b773fdb50c495b4372875dad061d532c061a451` |
| `candidate-data.json` | `01939a753d6c7e4b8d78821f439a86fc8a94cde3eb897e72946bf6fbdd53030a` |
| `generate_certificate.py` | `00a64109a6052c3d11dd16cdb8589fa3870e08473c9210c8fe71683f33b73c3c` |
| `replay.sh` | `4304976434bdb78ecfcd2cbe8e47802f8ce027f004c6de30461659301a4a2218` |
| Attack `DEFINITIONS.md` | `f0996516cfea9f7d09660c0ad66620cd25b81e581bea37c5b86ff5cbbb5b072d` |
| Attack `units/1/unit.json` | `34a09e29ea8c40d1af6785a22278facd20f53d595fe746c19c6ad9e9fe2a7155` |
| Attack `units/1/draft.md` | `eaecaff042468cb92138b1f7b467820c25044ca2f29697473dbce937229f5567` |

The unit hash matches `check-unit.json`. The replay script's local elan PATH prefix is specific to this workstation; a portable copy may use Lean already on PATH. A fresh-machine installation or copied distribution was not tested in this review.

## Draft and references

The detailed Stage 8 evaluation is `units/1/evaluation.md`. The draft statement matches `unit.json` quantifier by quantifier, and all mathematical claims resolve to the complete proof or deterministic package. Its short file references resolve to that package; in particular, `axioms.log` means `deterministic/formal-check-1/axioms.log`.

All three external identifiers were resolved independently on 2026-09-05. Direct DOI opening failed in the web tool, but publisher or author records supplied resolution:

- Yves Bertot, Frederique Guilhot, and Assia Mahboubi, *A formal study of Bernstein coefficients and polynomials*, DOI 10.1017/S0960129511000090. The [Cambridge publisher record](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/838EFF245D1E341FE599AAF6789C2486/S0960129511000090a.pdf/formal_study_of_bernstein_coefficients_and_polynomials.pdf) and the author's publication record identify the stated earlier Bernstein formalization.
- Cesar Munoz and Anthony Narkawicz, *Formalization of Bernstein Polynomials and Applications to Global Optimization*, DOI 10.1007/s10817-012-9256-3. The [Springer publisher record](https://link.springer.com/article/10.1007/s10817-012-9256-3) identifies the PVS formalization.
- Jinhui Li, Beibei Xiong, and Zhengfeng Yang, *A Proof of the Dittert Conjecture in Dimension 4 via an Exact Constrained Sum-of-Squares Certificate*, [arXiv:2607.29191v2](https://arxiv.org/abs/2607.29191v2). The versioned abstract explicitly describes a dimension-four certificate formally verified in Lean.

These references support the limited prior-work descriptions, not the new artifact's polynomial theorem. The theorem is checked locally. No exhaustive priority claim follows from the recorded searches, several of which were rate-limited. The draft makes no such claim.

## Scope and remaining obligations

The result is a complete Lean proof of the specified two polynomial inequalities. It is not a complete formalization of the n=8,9 marginal exclusion or the Dittert matrix theorem. The support intervals, monotone tails, matrix-to-scalar interfaces, and every n=7 case remain separate work. Those omissions are already explicit in the claim, proof, position note, draft, and handoff, so they are not hidden hypotheses or failures of this bounded claim.

The review verifies correctness and statement fidelity of this local formalisation artifact. It does not certify mathematical novelty, publication suitability, or a second independently implemented Lean proof.
