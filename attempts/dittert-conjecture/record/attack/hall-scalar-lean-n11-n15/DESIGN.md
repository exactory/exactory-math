# Hall scalar formalization design

Approved scope: the user's approval on 2026-09-05 of the staged proposal, followed by the explicit request to use exactory:write at the drafting stage.

## First milestone

Prove the exact scalar theorem in problem.json. Encode factorials, powers, rational constants, and the cut predicate directly in Lean. Do not import a Python-generated list of successful values as mathematical premises. Check 335 ordered proper cases and five normalized marginal cases. Prove that every nonfull ordered size pair is represented. Keep the full case a named analytic obligation outside the scalar theorem.

The output theorem quantifies over all real u<=1, hence includes the full intended interval [0,1], both endpoints and any purported large-cost branch after the scalar interfaces have been established. It is not a theorem that every matrix satisfies those interfaces.

## Architecture and trust

One new Lake package under deterministic/formal-check-1. Definitions.lean contains direct rational formulas and predicates. Finite.lean contains the exact finite proof. Main.lean contains the real inequality and infeasibility theorem. Audit.lean composes coverage and the target for the harness. Tests exercise formula values, out-of-scope cases and the theorem's full input domain.

Pin Lean v4.33.1 and Mathlib commit 0df444a360eaa60ab8c11dca51a86af692955474, reusing existing cached dependencies locally without editing their sources. A portable manifest must not depend on absolute local paths. Use one Lean thread, nice15, and a 2048 MB Lean memory ceiling. Do not rebuild Mathlib from source or run another mathematical job concurrently. Preserve logs and wall/user/system time and maximum RSS. No external writes, uploads or Git commits.

No sorry or custom axioms in the final dependency graph. Kernel reduction or proof-producing tactics are required; native_decide does not meet this milestone. Statements and assumptions receive independent review.

## Successors and manuscript

After a verified immutable checkpoint, consider a separate n7..10 attack for exact exceptional polynomials and complete tree coverage. A distinct generic Bernstein checker is a separate claim, not a silent expansion of this attack. If the measured complexity makes that extension disproportionate, preserve the explicit obstruction and write only the achieved theorem.

Use exactory:write for a local English paper, with prior ideation setup if required. The claim is a partial formalization of an attributed existing argument. Check prior formalizations before framing novelty. Draft numerical claims only from an evidence ledger and validate citations through the registry tools. No Zenodo deposit in this task.
