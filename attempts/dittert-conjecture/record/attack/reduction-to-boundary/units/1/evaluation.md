# Independent evaluation: formalisation unit of node reduction-to-boundary

Unit under evaluation: the claim of node reduction-to-boundary (obligation-000006 of the admitted root decomposition) as the Lean theorem `Dittert.reduction` with requested type `Dittert.Reduction`, checked with `propext`, `Classical.choice` and `Quot.sound` only; form "formalisation"; evidence `deterministic/formal-check-1`; no mathematical novelty claimed.

Records read: `records/result.json`, `records/inspection.log`, `records/journal.jsonl`, `records/claim.md` (this directory). Sources read: the staged project `scratch/stage-reduction/formal-check-1` (`step.json`, `lean-toolchain`, `lakefile.toml`, `lake-manifest.json`, `Dittert.lean`, `Dittert/Basic.lean`, `Dittert/Obligations.lean`, `Dittert/Reduction.lean` in full, `build-stage.log`), which the coordinator states is unchanged since my input review, and `scratch/reduction-work/Dittert/REDUCTION-NOTES.md`. My own axiom audit was run in a scratchpad copy of the staged project with `lake env lean` (no `lake update`).

## 1. Does the Lean statement match the claim quantifier by quantifier

The claim (`claim.md`): for every integer n >= 2, if every n by n real matrix with nonnegative entries and total entry sum n that attains the maximum of Phi(A) = prod_i r_i(A) + prod_j c_j(A) - per(A) over that set has all entries positive, then Phi(A) <= 2 - n!/n^n for every such matrix A, with equality if and only if every entry of A equals 1/n.

The Lean statement (`Dittert/Obligations.lean`, lines 16-18, byte-identical to the blueprint draft):

```
def Reduction : Prop :=
  ∀ n : ℕ, 2 ≤ n →
    (∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A → ∀ i j, 0 < A i j) → Statement n
```

with, from `Dittert/Basic.lean`:

- `rowSum A i = ∑ j, A i j`, `colSum A j = ∑ i, A i j`, `totalSum A = ∑ i, ∑ j, A i j` (lines 21-27);
- `Phi A = (∏ i, rowSum A i) + (∏ j, colSum A j) - A.permanent` (lines 30-31), where `A.permanent` is Mathlib's `Matrix.permanent` over the reals;
- `Feasible A = (∀ i j, 0 ≤ A i j) ∧ totalSum A = n` (lines 34-35);
- `gamma n = (n.factorial : ℝ) / (n : ℝ) ^ n` (line 38);
- `IsUniform A = ∀ i j, A i j = 1 / (n : ℝ)` (line 45);
- `Statement n = ∀ A, Feasible A → Phi A ≤ 2 - gamma n ∧ (Phi A = 2 - gamma n ↔ IsUniform A)` (lines 48-50);
- `IsMaximizer A = Feasible A ∧ ∀ B, Feasible B → Phi B ≤ Phi A` (lines 59-60).

Correspondence:

| Claim | Lean |
|---|---|
| for every integer n >= 2 | `∀ n : ℕ, 2 ≤ n →` (the integers at least 2 are the naturals at least 2) |
| every n by n real matrix with nonnegative entries and total entry sum n that attains the maximum of Phi over that set | `∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A →` (`Feasible A` is nonnegative entries and total sum n; the second conjunct is maximality over the feasible set) |
| has all entries positive | `∀ i j, 0 < A i j` |
| Phi(A) = prod r_i + prod c_j - per(A) with r_i, c_j the row and column sums | `Phi`, `rowSum`, `colSum`, `Matrix.permanent` |
| then Phi(A) <= 2 - n!/n^n for every such matrix A | `Statement n`: `∀ A, Feasible A → Phi A ≤ 2 - gamma n` |
| with equality if and only if every entry of A equals 1/n | `Phi A = 2 - gamma n ↔ IsUniform A` |

Every quantifier of the claim has a counterpart with the same range and the same order, and no quantifier is added or dropped. The theorem `Dittert.reduction : Reduction` is declared at `Dittert/Reduction.lean` line 486, and `inspection.log` line 2 prints `Dittert.reduction : Dittert.Reduction`.

## 2. Does the evidence support it

- `result.json`: `status` `pass`, `theorem` `Dittert.reduction`, `axioms` `[propext, Classical.choice, Quot.sound]`, `reason` `null`; `output_head` reproduces the five lines of `inspection.log`.
- `inspection.log`: the printed type `Dittert.reduction : Dittert.Reduction` between the type markers, then `'Dittert.reduction' depends on axioms: [propext, Classical.choice, Quot.sound]` and `'exactory_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]`. The statement of `exactory_correspondence` is not in the copied records; what the records show is that the executor's correspondence declaration between the checked theorem and the requested type carries only the three standard axioms.
- My audit in a copy of the staged project, with `import Dittert.Reduction` only: `'Dittert.reduction' depends on axioms: [propext, Classical.choice, Quot.sound]` and `#check` elaborating `Dittert.reduction : Dittert.Reduction`. This agrees with the controlled result and with `REDUCTION-NOTES.md`.
- The staged sources on the path of the declaration (`Dittert/Reduction.lean` -> `Dittert/Obligations.lean` -> `Dittert/Basic.lean` -> Mathlib) contain no `sorry`, `axiom`, `native_decide`, `decide +native`, `implemented_by`, `extern` or `admit` (grep over every Lean file of the staged tree; the only matches are the stubs in `Dittert.lean` lines 17-26 and `Dittert/Bridges.lean` lines 30, 35, 40, and a comment in `Dittert/Scalar/Defs11.lean` line 17). `build-stage.log` records `Dittert.Reduction` built with one unused-variable linter warning and no `sorry` warning.
- Toolchain and dependencies: `leanprover/lean4:v4.33.1`; `lake-manifest.json` pins Mathlib at `0df444a360eaa60ab8c11dca51a86af692955474` (the revision named in `claim.md`) and lists only Mathlib's inherited packages; `lakefile.toml` requires only mathlib.
- `journal.jsonl`: one move on walk `verify-formally-with-lean4`, entry `formalise-while-fresh`, steps `["formal-check-1"]`, `closes` `true`, `failure_signal_fired` `false`, `problem_changed` `false`; the recorded action describes the lemma chain that `Dittert/Reduction.lean` contains (compactness and continuity, the value at the uniform matrix, row mixing with the quadratic in t, the vanishing coefficient at a positive maximizer, the first vanishing entry, transposition, assembly), and the recorded output matches the check.
- `claim.md` names checkpoint-000001 (milestone target-proof, move 1) and acceptance-000001 (obligation-000006, standard lean-kernel, status accepted).

The evidence supports the unit's statement: the declaration named in the statement has the requested type, its axiom set is exactly the permitted one, and the proof text contains no escape hatch.

## 3. Scope and assumptions

- Scope: every natural n >= 2 and every real n by n matrix; the conclusion is conditional on the positivity of every maximizer, as the obligation is. The theorem is a premise of routes r7, r8 and r11 of the root decomposition, which use it for 7 <= n <= 15, inside its range.
- Assumptions: none. The theorem has no hypotheses beyond those in the Prop, the node declares no assumption ids, and no ported or third-party Lean code is used; the proof depends on Mathlib only (compactness in finite dimension, `IsCompact.exists_isMaxOn`, `Matrix.permanent` with `permanent_updateRow_smul`, `permanent_permute_cols` and `permanent_transpose`, `Fintype.card_perm`, `Finset.exists_min_image`, filter lemmas for the open interval of feasibility). Additivity of the permanent in one row, which Mathlib v4.33.1 lacks, is proved inside the module (`permanent_updateCol_eq`, `permanent_updateCol_add`, `permanent_updateRow_add`).
- The unit claims no mathematical novelty: the positive-maximizer statement is known (the node's novelty record cites Hwang 1986), and the mixing proof is the elementary argument recorded in the node's study. This is consistent with the form "formalisation".

## 4. Defects

None that affect the verdict. Three remarks:

1. `Dittert/Reduction.lean` line 160 binds a hypothesis `hik` that `rowSum_mixRows_self` does not use; the build warns about it. No logical effect.
2. The staged root module `Dittert.lean` (line 17) still declares `theorem reduction : Reduction := by sorry` under the same fully qualified name, in a module that does not import `Dittert.Reduction`. It is off the inspected path (the executor imports exactly `Dittert.Reduction`, and the printed axiom set confirms the real theorem was inspected), but an inspection that imported the library root would report `sorryAx` for the same name, as my copy audit with `import Dittert` showed. The stub should be removed when the module is wired into the root.
3. The copied records do not include the statement of `exactory_correspondence`, only its axiom line; the correspondence between the checked declaration and the requested type is therefore verified here through the printed type line and my own `#check`, not through reading that theorem.

## 5. Verdict

Accept. The Lean theorem `Dittert.reduction : Dittert.Reduction` states the node's claim quantifier by quantifier, the controlled check passed with exactly `propext`, `Classical.choice` and `Quot.sound`, the same result was reproduced in an independent copy, and the sources on the declaration's path contain no `sorry`, axiom or native evaluation.
