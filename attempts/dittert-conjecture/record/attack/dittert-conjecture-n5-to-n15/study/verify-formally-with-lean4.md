# Strategy study: verify-formally-with-lean4

Written 2026-09-03 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| GitHub code search, google-deepmind/formal-conjectures | `Dittert`; `permanent van der Waerden` | 2026-09-03 | no formal statement of Dittert's conjecture; one unrelated file (ErdosProblems/499.lean) |
| local | `study/fetched/src-2607.29191/main.tex` (section "Formal Verification in Lean", lines 848-1035) and `lstlean.tex` | 2026-09-03 | the n = 4 Lean check: four uses of `native_decide` |
| local | `ls ~/.elan/bin` | 2026-09-03 | a Lean toolchain is installed (elan, lake, lean); no Mathlib project exists in the workspace |

## 2. Hits worth reading

- arXiv:2607.29191, Lean section: the certificate identity and the positive definiteness of the recovered rational Gram matrices (153 x 153 and 136 of 17 x 17) are verified by `native_decide`, i.e. by Lean's compiler evaluating rational arithmetic; the harness classifies such a check as `evidence` (Lean.ofReduceBool in the axiom list).
- Mathlib: no canonical statement of the conjecture; matrices, real numbers, finite sums and products, and `Matrix.det` exist; the permanent is a one-line definition over `Equiv.Perm` (whether Mathlib's `Matrix.permanent` exists in the installed version is to be checked at step 2).

## 3. What was learned, as constraints on the plan

1. **Statement (step 2) is cheap.** The theorem "for all A : Matrix (Fin 5) (Fin 5) R, (all entries >= 0) -> (sum = 5) -> phi(A) <= 2 - 120/3125" is stated in a few lines over Mathlib; the quantitative form with c_1 = 32/3125 likewise.
2. **The finite check (step 4) is the obstacle.** The n = 5 certificate has 4339 rational orbit coordinates defining a 2925 x 2925 and two 325 x 325 matrices; the kernel cannot reduce a 2925 x 2925 rational LDL^T, and even `native_decide` at that size is beyond the n = 4 precedent (153 x 153) by a factor 400 in entries. Two routes: (a) transport the isotypic reduction into Lean (rational projectors as explicit matrices, blocks of size at most 560), which needs the block bases as rational data (about 2925 x 2925 rationals) plus a proof that they span; (b) verify a rational LDL^T certificate of each block with `decide` on small blocks and native evaluation on the large ones. Both are multi-day engineering, and (b) still lands on `evidence` for the large blocks.
3. **What is verifiable now.** The one-rational-inequality residue of the analytic route (Theorem R's final comparison, or Kafidov's K_n > 0 at n = 16) is kernel-checkable by `norm_num`; the n = 5, 6 certificates are not.
4. **Trusted base.** A native evaluation adds Lean.ofReduceBool to the axiom list, which the harness records as `evidence`, the same status as the floating-point-verified step at n = 6.

## 4. Stop reason

The queries ran dry: no formal statement exists to align with, and the two routes to a formal certificate check are engineering items whose cost is documented by the n = 4 precedent.
