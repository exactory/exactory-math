# Independent evaluation: formalisation unit of node gurvits-floors

Unit under evaluation: the claim of node gurvits-floors (obligation-000008 of the admitted root decomposition) as the Lean theorem `Dittert.gurvits_floors` with requested type `Dittert.GurvitsFloors`, checked with `propext`, `Classical.choice` and `Quot.sound` only; form "formalisation"; evidence `deterministic/formal-check-1`; no mathematical novelty claimed (van der Waerden and the Gurvits rectangle floor are known theorems), with the ported development attributed under Apache-2.0.

Records read: `records/result.json`, `records/inspection.log`, `records/journal.jsonl`, `records/claim.md` (this directory). Sources read: the staged project `scratch/stage-floors/formal-check-1` (`step.json`, `lean-toolchain`, `lakefile.toml`, `lake-manifest.json`, `Dittert.lean`, `Dittert/Basic.lean`, `Dittert/Obligations.lean`, `Dittert/Floors.lean`, `Dittert/Floors/Analytic.lean`, `Dittert/Floors/Chain.lean` in full, `Dittert/FLOORS-NOTES.md`, `build-stage.log`, `LICENSE`, `NOTICE`), which the coordinator states is unchanged since my input review; the port record `scratch/maths-pub-port/PORT-NOTES.md` and `AXIOMS.txt`. My own axiom audit was run in a scratchpad copy of the staged project with `lake env lean` (no `lake update`).

## 1. Does the Lean statement match the claim quantifier by quantifier

The claim (`claim.md`): for every integer n >= 1 and every n by n doubly stochastic real matrix B: per(B) >= n!/n^n; and for all integers a, b >= 1 with a + b <= n - 1, if there are a rows and b columns of B whose a x b block of entries is zero, then per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b), where gamma(k) = k!/k^k.

The Lean statement (`Dittert/Obligations.lean`, lines 31-36, byte-identical to the blueprint draft):

```
def GurvitsFloors : Prop :=
  ∀ n : ℕ, 1 ≤ n → ∀ B ∈ doublyStochastic ℝ (Fin n),
    gamma n ≤ B.permanent ∧
    ∀ a b : ℕ, 1 ≤ a → 1 ≤ b → a + b ≤ n - 1 →
      ∀ I J : Finset (Fin n), I.card = a → J.card = b → HasZeroBlock B I J →
        gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ B.permanent
```

with `gamma k = (k.factorial : ℝ) / (k : ℝ) ^ k` (`Dittert/Basic.lean` line 38), `HasZeroBlock B I J = ∀ i ∈ I, ∀ j ∈ J, B i j = 0` (lines 66-67), `B.permanent` Mathlib's `Matrix.permanent`, and `doublyStochastic ℝ (Fin n)` Mathlib's set of real n by n matrices with nonnegative entries and unit row and column sums.

Correspondence:

| Claim | Lean |
|---|---|
| for every integer n >= 1 | `∀ n : ℕ, 1 ≤ n →` |
| every n by n doubly stochastic real matrix B | `∀ B ∈ doublyStochastic ℝ (Fin n),` |
| per(B) >= n!/n^n | `gamma n ≤ B.permanent` |
| for all integers a, b >= 1 with a + b <= n - 1 | `∀ a b : ℕ, 1 ≤ a → 1 ≤ b → a + b ≤ n - 1 →` (natural subtraction; with n >= 1 this is the integer condition, and it forces n - a - b >= 1) |
| if there are a rows and b columns of B whose a x b block is zero | `∀ I J : Finset (Fin n), I.card = a → J.card = b → HasZeroBlock B I J →` (universal over the witnesses, which is the same as the existential hypothesis) |
| then per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b) | `gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ B.permanent` |

Every quantifier of the claim has a counterpart with the same range and order, and none is added or dropped. The theorem `Dittert.gurvits_floors : GurvitsFloors` is declared at `Dittert/Floors.lean` line 214; its first conjunct is the port's `GurvitsUnconditional.egorychev_falikman` applied to the unpacked membership, its second is `Floors.rect_floor` (lines 161-207), whose hypotheses are exactly those of the second conjunct. `inspection.log` line 2 prints `Dittert.gurvits_floors : Dittert.GurvitsFloors`.

## 2. Does the evidence support it

- `result.json`: `status` `pass`, `theorem` `Dittert.gurvits_floors`, `axioms` `[propext, Classical.choice, Quot.sound]`, `reason` `null`; `output_head` reproduces the five lines of `inspection.log`.
- `inspection.log`: the printed type `Dittert.gurvits_floors : Dittert.GurvitsFloors` between the type markers, then `'Dittert.gurvits_floors' depends on axioms: [propext, Classical.choice, Quot.sound]` and `'exactory_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]`. The statement of `exactory_correspondence` is not in the copied records; what they show is that the executor's correspondence declaration carries only the three standard axioms.
- My audit in a copy of the staged project, with `import Dittert.Floors` only: `'Dittert.gurvits_floors' depends on axioms: [propext, Classical.choice, Quot.sound]` and `#check` elaborating `Dittert.gurvits_floors : Dittert.GurvitsFloors`. This agrees with the controlled result and with the build record in `FLOORS-NOTES.md`.
- The sources on the path of the declaration (`Dittert/Floors.lean` -> `Dittert/Floors/Chain.lean` -> `Dittert/Floors/Analytic.lean` -> `Dittert/Obligations.lean` -> `Dittert/Basic.lean`, plus the `GurvitsPort` modules and Mathlib) contain no `sorry`, `axiom`, `native_decide`, `decide +native`, `implemented_by`, `extern` or `admit`: a grep over every Lean file of the staged Dittert tree matches only the stubs in `Dittert.lean` lines 17-26 and `Dittert/Bridges.lean` lines 30, 35, 40 and a comment in `Scalar/Defs11.lean` line 17, and the same grep over the 17 port modules matches only comments (`LorentzianGenerator.lean` line 10, `NewtonInequalities.lean` lines 16 and 626).
- The proof (919 new lines, read in full) is the argument the journal describes: the van der Waerden conjunct by the ported theorem; for the rectangle floor, `hstable_of_limit` (a nonzero polynomial that is, along every complex line, the limit as a positive real parameter tends to 0 from above of nonvanishing polynomials is H-stable; minimum modulus principle `Complex.eventually_eq_or_eq_zero_of_isLocalMin_norm` on a closed disc, uniform closeness from Heine-Cantor), `restrict_zero_hstable`, `leadingCoeff_hstable`, `nonDegenerate_of_natDegree_pos` feeding the port's `hstable_pderiv_of_nonDegenerate`, `hstable_reduce`; the chain with the J-degree bound `JDegBd` preserved by `reduce` with the bound decreased by one, the port's `stone12` with the exact degree from `classFac_hstable` and `Gc_antitone`, the port's `gurvitsBound` for the remaining variables, `prod_Gc_ratio` from `prod_G_one`; `rect_floor` with the column permutation `exists_perm_front`, the J-degree bound `jDegBd_rowPoly` from the zero block, capacity 1 from `LemmaB6.cap_rowProd_eq_one_of_doublyStochastic`, and the top coefficient `per B` from `FaceBounds.coeff_topIdx_rowPoly` and `permanent_permute_rows`.
- Toolchain and dependencies: `leanprover/lean4:v4.33.1`; `lake-manifest.json` pins Mathlib at `0df444a360eaa60ab8c11dca51a86af692955474` with only its inherited packages; `lakefile.toml` requires only mathlib, with the two default targets `Dittert` (roots `Dittert`, `Dittert.Floors`) and `GurvitsPort`. `build-stage.log` records the standalone build completed successfully (3460 jobs): the port modules built with their own axiom-audit info lines (every printed declaration at the three standard axioms, `pertRow` at none), `Dittert.Floors.Analytic`, `Dittert.Floors.Chain` and `Dittert.Floors` built without warnings, and the only `sorry` warnings are the stubs of `Bridges.lean` and `Dittert.lean`.
- `journal.jsonl`: one move on walk `verify-formally-with-lean4`, entry `formalise-while-fresh`, steps `["formal-check-1"]`, `closes` `true`, `failure_signal_fired` `false`, `problem_changed` `false`; the recorded action matches the lemma chain of the three modules, and the recorded output (922 new lines counting the audit file, no `sorry`, standard axioms) matches the check and `FLOORS-NOTES.md`.
- `claim.md` names checkpoint-000003 (milestone target-proof, move 1) and acceptance-000003 (obligation-000008, standard lean-kernel, status accepted) and says the frozen inputs are 37 artifacts of the staged project; the staged tree I listed holds 38 entries outside `.lake` including `.gitignore` and `build-stage.log`, so the count is consistent with one of those two being excluded; I did not receive the artifact list itself.

The evidence supports the unit's statement: the declaration named in the statement has the requested type, its axiom set is exactly the permitted one, and the proof text and its ported dependencies contain no escape hatch.

## 3. Scope, assumptions and provenance of the ported part

- Scope: every natural n >= 1, every doubly stochastic real n by n matrix, every zero block with a, b >= 1 and a + b <= n - 1. The bridges use a = b = 1 (the one-zero floor kappa_n), the proper cuts, and the z x 1 blocks of dimension 8, all inside the range.
- Assumptions: none. The theorem has no hypotheses beyond those in the Prop, the node declares no assumption ids, and the proof depends on Mathlib and the ported library only. The port's undischarged `def : Prop` `HStableClass.NonDegenerateClass` is not used; the derivative closure goes through `HStableOrbit.hstable_pderiv_of_nonDegenerate` with its hypothesis supplied by the new `nonDegenerate_of_natDegree_pos`, which is the deviation from the brief that `FLOORS-NOTES.md` records (positive capacity alone does not give the port's `NonDegenerate` over complex points).
- Provenance of the ported part: the `GurvitsPort` library is the port of the Gurvits / van der Waerden subset of D C P Revere's `maths-pub` Lean development (commit `0a1cb0a14fefe85668365d448f9bbaf4dd89d458`, Apache-2.0, Zenodo DOI 10.5281/zenodo.21902861). The 17 staged port modules are byte-identical to `scratch/maths-pub-port/GurvitsPort` except for the absent `Audit.lean` (`diff -rq`), and the staged `LICENSE` and `NOTICE` are byte-identical to the port's copies (`diff -q`). `PORT-NOTES.md` records that no statement was changed, that four proof edits repaired Lean/Mathlib drift in two files, that five files carry recorded cuts with `PORT NOTE` comments, and that `AXIOMS.txt` lists 53 goal declarations each at `[propext, Classical.choice, Quot.sound]`. `Dittert/Floors.lean`, `Analytic.lean` and `Chain.lean` name the source, commit and license in their headers. No port file is modified by this unit.
- The unit claims no mathematical novelty: the first conjunct is Egorychev-Falikman as ported, and the rectangle floor is the classical Gurvits extraction recorded in the local audit; the new formal work (the analytic closure lemmas and the degree-tracked chain) formalises known arguments. This is consistent with the form "formalisation".

## 4. Defects

None that affect the verdict. Four remarks:

1. The staged root module `Dittert.lean` (line 19) still declares `theorem gurvits_floors : GurvitsFloors := by sorry` under the same fully qualified name, in a module that does not import `Dittert.Floors`. It is off the inspected path (the executor imports exactly `Dittert.Floors`, and the printed axiom set confirms the real theorem was inspected), but an inspection that imported the library root would report `sorryAx` for the same name, as my copy audit with `import Dittert` showed. The stub should be removed when the module is wired into the root, as was done for `reduction` and `hall_domination` in the bridge-11 stage.
2. The staged `Dittert/Bridges.lean` is the earlier blueprint version (all three dimensional bridges `sorry`, no import of `Dittert.Bridge.N11`) and differs from the draft's current file; it is imported only by the root and is not on the path of `Dittert.Floors`.
3. The copied records do not include the statement of `exactory_correspondence`, only its axiom line; the correspondence between the checked declaration and the requested type is therefore verified here through the printed type line and my own `#check`.
4. The port build emits linter warnings only (unused `simp` arguments, one deprecated `push_neg`, one unused variable, one `<;>` style hint), as `PORT-NOTES.md` already records; none affects the kernel check.

## 5. Verdict

Accept. The Lean theorem `Dittert.gurvits_floors : Dittert.GurvitsFloors` states the node's claim quantifier by quantifier, the controlled check passed with exactly `propext`, `Classical.choice` and `Quot.sound`, the same result was reproduced in an independent copy, the sources on the declaration's path contain no `sorry`, axiom or native evaluation, and the ported part is byte-identical to the audited Apache-2.0 port with its license and notice in the project.
