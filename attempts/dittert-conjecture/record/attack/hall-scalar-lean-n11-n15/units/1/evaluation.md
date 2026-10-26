# Independent stage-8 evaluation

Date: 2026-09-05.

Current decision: PASS after the reference correction and narrow recheck recorded below. The scalar mathematics, statement fidelity, finite coverage, and disclosed trust boundary pass this review. The initial decision was FAIL solely because of the broken evidence reference recorded as F1. This is an assessment of the formalisation unit, not a numerical paper score or a publication recommendation.

## Review scope and method

I independently read `unit.json`, `draft.md`, `position.md`, `journal-excerpt.jsonl`, `study/problem.md`, `novelty.md`, and the two referenced deterministic packages. I read the installed math-solver stage-8 and CASHOUT self-check instructions. I used `study/final-review.md` only for its recorded commands, exit statuses, axiom outputs, and source hashes. Its verdict is not the basis of this decision. I did not run Lean, rebuild dependencies, perform heavy computations, or inspect the separate manuscript under preparation.

I recomputed the SHA256 hashes of the seven final Lean source files. Every hash agrees with the execution record; the two copies of `Definitions.lean` and `Finite.lean` are identical. Both actual `result.json` files report `pass` and list exactly `propext`, `Classical.choice`, and `Quot.sound`. This is source and recorded-execution review, not a new execution of the formal checks.

## Initial finding and resolution

### F1. Medium, resolved: the full novelty ledger reference did not resolve

`novelty.md` identifies the full ledger as `../../../scratch/lean-novelty-2026-09-05.md`. Relative to that file, this points outside the Dittert research root to `exactory-research/scratch/lean-novelty-2026-09-05.md`, which does not exist. The actual file exists at the research root's `scratch/lean-novelty-2026-09-05.md`. The reference in `novelty.md` must therefore be `../../scratch/lean-novelty-2026-09-05.md`.

`study/problem.md` uses `../../../scratch/lean-novelty-2026-09-05.md`, which is correct relative to that study file, but describes it as relative to the attack. Replace that description with "relative to this file". These are two manifestations of the same inconsistent reference base.

Stage 8 requires every reference to resolve. Since `unit.json` cites these records as its novelty evidence, the unit should return for this narrow correction before receiving a pass. No change to the theorem or Lean source is requested. The ledger itself was not rereviewed in this bounded unit assessment, and locating it does not certify the adequacy of the literature search.

Resolution on 2026-09-05: the coordinator changed `novelty.md` to `../../scratch/lean-novelty-2026-09-05.md`, explicitly relative to that file, and changed `study/problem.md` to say its reference is relative to that file. I reread both corrected lines and checked that both resulting paths resolve to the existing 17,860-byte ledger at the research root's `scratch/lean-novelty-2026-09-05.md`. F1 is closed. The historical finding above is preserved to explain the initial failure. No Lean execution was performed for this recheck, and no claim of publication novelty follows from resolving the reference.

## Statement and evidence checks

The draft preserves all quantifiers in `unit.json`: natural `11 <= n <= 15`, natural `a,b` with `0 < a+b < n`, and every real `u <= 1`. The consequence quantifies over arbitrary real `P` and `delta`; no unmentioned nonnegativity assumptions are introduced. The formulas for gamma, the proper-case M and C, and both marginal orientations agree with `Definitions.lean`. On this domain, the natural subtractions have their intended ordinary integer values, and all gamma arguments and displayed denominators are valid.

The mathematical evidence mapping is complete:

| Draft claim | Evidence |
| --- | --- |
| Exact rational formulas and piecewise cases | `formal-check-1/Definitions.lean` |
| Positive M, C, and `4*C*(M-gamma)-(n*M)^2` | `Finite.lean`, `finite_n11` through `finite_n15`, and `all_good` |
| Strict scalar positivity for every real `u <= 1` | `Main.lean`, `quadratic_positive` and `scalar_positive` |
| Inconsistency of the three scalar bounds | `Main.lean`, `scalar_exclusion`, and `Audit.lean`, `hall_scalar_certificate` |
| Exact normalized cardinality and universal coverage | `Finite.lean`, `case_counts`, `total_case_count`, and `finite_certificate`; independently targeted by `formal-check-2/result.json` |
| Standard-axiom execution and unchanged final sources | Both `result.json` files, the execution section of `study/final-review.md`, and the hashes checked in this review |

The completed-square identity is correct. Positive C and discriminant make its quadratic strictly positive for every real u. Bernoulli applies under the stated `u <= 1`; multiplication preserves its direction because M is positive. Combining these facts yields the stated polynomial inequality. Adding the two lower bounds then contradicts `P+delta <= gamma(n)`.

For each dimension the number of proper ordered pairs is `(n-1)*(n-2)/2`, giving 45, 55, 66, 78, and 91, totaling 335. One normalized marginal per dimension gives the five Lean-proved counts 46, 56, 67, 79, and 92, totaling 340. The original marginal orientations contribute `2*(n-1)` per dimension, totaling 120, so the original domain has 455 cases. The draft correctly identifies 455 as an external combinatorial count. Formal coverage follows from `all_good`, including both marginal orientations, and does not confuse that count with the normalized cardinality.

## External references and contribution

I resolved the two external citations on 2026-09-05. [Nascimento's pinned repository](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701) identifies the stated author and presents its material as working proofs. [Li, Xiong, and Yang, arXiv:2607.29191v2](https://arxiv.org/abs/2607.29191v2) has the stated authors and explicitly reports Lean verification for dimension 4. These identifiers support the draft's attribution and rejection of a first-Dittert-formalization claim. Resolving them is not an independent certification of the full matrix proofs.

The claim is about an exhibited formal artifact with a quantified theorem, not merely an account of research activity. CASHOUT explicitly permits a standalone formalisation. The underlying mathematical scalar argument is prior work and would not qualify here as a new mathematical theorem. The contribution can be assessed as a limited verification technical note, with direct formulas, finite coverage, and real-variable composition. The bounded searches with rate limits and unrelated results cannot establish priority, absence of prior implementations, general publication novelty, or journal significance. The draft and position note disclose these limitations adequately.

The draft also correctly states that the second package is a snapshot of the same finite proof, that no clean rebuild of all Mathlib dependencies or alternate-kernel check was performed, and that the matrix reductions, full cut `(0,0)`, and dimensions outside 11 through 15 are not certified. Negative u belongs to the scalar theorem's domain and supplies no new matrix interface. There are no unresolved findings in the reviewed unit. With F1 corrected and its references checked again, this unit passes stage 8 within this limited scope.
