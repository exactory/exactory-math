# Independent evaluation: formalisation unit of node hall-domination

Unit under evaluation: the claim of node hall-domination (obligation-000007 of the admitted root decomposition) as the Lean theorem `Dittert.hall_domination` with requested type `Dittert.HallDomination`, checked with `propext`, `Classical.choice` and `Quot.sound` only; form "formalisation"; evidence `deterministic/formal-check-1`; no mathematical novelty claimed (the max-flow / Hall domination criterion is classical).

Records read: `records/result.json`, `records/inspection.log`, `records/journal.jsonl`, `records/claim.md` (this directory). Sources read: the staged project `scratch/stage-hall/formal-check-1` (`step.json`, `lean-toolchain`, `lakefile.toml`, `lake-manifest.json`, `Dittert.lean`, `Dittert/Basic.lean`, `Dittert/Obligations.lean`, `Dittert/Hall.lean` in full, `build-stage.log`), which the coordinator states is unchanged since my input review, and `scratch/hall-work/Dittert/HALL-NOTES.md`. My own axiom audit was run in a scratchpad copy of the staged project with `lake env lean` (no `lake update`).

## 1. Does the Lean statement match the claim quantifier by quantifier

The claim (`claim.md`): for every integer n >= 1, every n by n real matrix A with nonnegative entries, and every real lambda > 0 such that for all subsets I of the rows and J of the columns with |I| + |J| > n the sum of the entries of A over I x J is at least lambda (|I| + |J| - n), there exists an n by n doubly stochastic real matrix B with lambda B_ij <= A_ij for all i and j.

The Lean statement (`Dittert/Obligations.lean`, lines 22-27, byte-identical to the blueprint draft):

```
def HallDomination : Prop :=
  ∀ n : ℕ, 1 ≤ n → ∀ A : Matrix (Fin n) (Fin n) ℝ, (∀ i j, 0 ≤ A i j) →
    ∀ lam : ℝ, 0 < lam →
      (∀ I J : Finset (Fin n), n < I.card + J.card →
        lam * ((I.card : ℝ) + (J.card : ℝ) - (n : ℝ)) ≤ cutSum A I J) →
      ∃ B ∈ doublyStochastic ℝ (Fin n), ∀ i j, lam * B i j ≤ A i j
```

with `cutSum A I J = ∑ i ∈ I, ∑ j ∈ J, A i j` (`Dittert/Basic.lean` line 63) and `doublyStochastic ℝ (Fin n)` Mathlib's set of real n by n matrices with nonnegative entries and every row and column sum equal to 1 (`Mathlib/Analysis/Convex/DoublyStochasticMatrix.lean`; the proof uses its characterisation `mem_doublyStochastic_iff_sum` at `Hall.lean` line 377).

Correspondence:

| Claim | Lean |
|---|---|
| for every integer n >= 1 | `∀ n : ℕ, 1 ≤ n →` |
| every n by n real matrix A with nonnegative entries | `∀ A : Matrix (Fin n) (Fin n) ℝ, (∀ i j, 0 ≤ A i j) →` |
| every real lambda > 0 | `∀ lam : ℝ, 0 < lam →` |
| such that for all subsets I of the rows and J of the columns with \|I\| + \|J\| > n | `∀ I J : Finset (Fin n), n < I.card + J.card →` |
| the sum of the entries of A over I x J is at least lambda (\|I\| + \|J\| - n) | `lam * ((I.card : ℝ) + (J.card : ℝ) - (n : ℝ)) ≤ cutSum A I J` (the subtraction is over the reals, so no truncation) |
| there exists an n by n doubly stochastic real matrix B | `∃ B ∈ doublyStochastic ℝ (Fin n),` |
| with lambda B_ij <= A_ij for all i and j | `∀ i j, lam * B i j ≤ A i j` |

Every quantifier of the claim has a counterpart with the same range and order, and none is added or dropped. The theorem `Dittert.hall_domination : HallDomination` is declared at `Dittert/Hall.lean` line 372, and `inspection.log` line 2 prints `Dittert.hall_domination : Dittert.HallDomination`.

## 2. Does the evidence support it

- `result.json`: `status` `pass`, `theorem` `Dittert.hall_domination`, `axioms` `[propext, Classical.choice, Quot.sound]`, `reason` `null`; `output_head` reproduces the five lines of `inspection.log`.
- `inspection.log`: the printed type `Dittert.hall_domination : Dittert.HallDomination` between the type markers, then `'Dittert.hall_domination' depends on axioms: [propext, Classical.choice, Quot.sound]` and `'exactory_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]`. The statement of `exactory_correspondence` is not in the copied records; what the records show is that the executor's correspondence declaration between the checked theorem and the requested type carries only the three standard axioms.
- My audit in a copy of the staged project, with `import Dittert.Hall` only: `'Dittert.hall_domination' depends on axioms: [propext, Classical.choice, Quot.sound]` and `#check` elaborating `Dittert.hall_domination : Dittert.HallDomination`. This agrees with the controlled result and with `HALL-NOTES.md`, which records the same axiom line from `AuditHall.lean`.
- The staged sources on the path of the declaration (`Dittert/Hall.lean` -> `Dittert/Obligations.lean` -> `Dittert/Basic.lean` -> Mathlib) contain no `sorry`, `axiom`, `native_decide`, `decide +native`, `implemented_by`, `extern` or `admit` (grep over every Lean file of the staged tree; the only matches are the stubs in `Dittert.lean` lines 17-26 and `Dittert/Bridges.lean` lines 30, 35, 40, and a comment in `Dittert/Scalar/Defs11.lean` line 17). `Hall.lean` imports only `Dittert.Obligations` and `Mathlib.Topology.Instances.Matrix`. `build-stage.log` records `Dittert.Hall` built in 4.9 s with no warning.
- The proof (393 lines, read in full) is the argument the node's study proposed: the flow set (`0 ≤ F ≤ A`, row and column sums at most lam) is closed, contained in a compact box and contains the zero flow, so `totalSum` attains a maximum (`exists_max_flow`); residual reachability is the inductive predicate `Reach`; `augSpec_of_reach` builds a direction matrix by induction on a derivation; `exists_better_flow` augments by a small positive step; `le_colSum_of_reach` saturates every reachable column at a maximal flow; `max_flow_saturated` counts the total over the reachable rows and columns, applies the cut condition to `(I, Jᶜ)` when `n < |I| + |Jᶜ|` and nonnegativity otherwise, and turns `lam * n ≤ totalSum F` into saturation of every row and column; the theorem takes `B = F / lam`.
- Toolchain and dependencies: `leanprover/lean4:v4.33.1`; `lake-manifest.json` pins Mathlib at `0df444a360eaa60ab8c11dca51a86af692955474` and lists only Mathlib's inherited packages; `lakefile.toml` requires only mathlib.
- `journal.jsonl`: one move on walk `verify-formally-with-lean4`, entry `formalise-while-fresh`, steps `["formal-check-1"]`, `closes` `true`, `failure_signal_fired` `false`, `problem_changed` `false`; the recorded action describes the lemma chain that `Dittert/Hall.lean` contains, and the recorded output (393 lines, no sorry, standard axioms) matches the check.
- `claim.md` names checkpoint-000002 (milestone target-proof, move 1) and acceptance-000002 (obligation-000007, standard lean-kernel, status accepted).

The evidence supports the unit's statement: the declaration named in the statement has the requested type, its axiom set is exactly the permitted one, and the proof text contains no escape hatch.

## 3. Scope and assumptions

- Scope: every natural n >= 1, every nonnegative real n by n matrix, every real lam > 0 satisfying the cut condition over all pairs of row and column subsets. The hypothesis `1 ≤ n` is bound as `_hn` at `Hall.lean` line 373 and not used, as `HALL-NOTES.md` notes; the theorem is stated with it because the obligation is. The tight-cut consequence (the complementary block of a minimising cut vanishes in B) is not part of the theorem, by the node's design; the bridges derive it from double stochasticity and domination.
- Assumptions: none. The theorem has no hypotheses beyond those in the Prop, the node declares no assumption ids, and no ported or third-party Lean code is used; the proof depends on Mathlib only (compactness of products of closed intervals, `IsCompact.exists_isMaxOn`, filter lemmas for the augmentation step, `Finset.sum_eq_sum_iff_of_le`, `mem_doublyStochastic_iff_sum`).
- The unit claims no mathematical novelty: the statement is the classical dominated-doubly-stochastic criterion (max-flow / min-cut for real capacities; the node's study cites it as Li's theorem via Cheon-Wanless Lemma 2.2). This is consistent with the form "formalisation".

## 4. Defects

None that affect the verdict. Two remarks:

1. The staged root module `Dittert.lean` (line 18) still declares `theorem hall_domination : HallDomination := by sorry` under the same fully qualified name, in a module that does not import `Dittert.Hall`. It is off the inspected path (the executor imports exactly `Dittert.Hall`, and the printed axiom set confirms the real theorem was inspected), but an inspection that imported the library root would report `sorryAx` for the same name, as my copy audit with `import Dittert` showed. The stub should be removed when the module is wired into the root.
2. The copied records do not include the statement of `exactory_correspondence`, only its axiom line; the correspondence between the checked declaration and the requested type is therefore verified here through the printed type line and my own `#check`, not through reading that theorem.

## 5. Verdict

Accept. The Lean theorem `Dittert.hall_domination : Dittert.HallDomination` states the node's claim quantifier by quantifier, the controlled check passed with exactly `propext`, `Classical.choice` and `Quot.sound`, the same result was reproduced in an independent copy, and the sources on the declaration's path contain no `sorry`, axiom or native evaluation.
