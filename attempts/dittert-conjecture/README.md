# Dittert's conjecture for 5 ≤ n ≤ 15

| | |
|---|---|
| Claim | For every integer $n$ with $5 \le n \le 15$ and every real $n \times n$ matrix $A$ with nonnegative entries whose entries sum to $n$, with row sums $r_i$ and column sums $c_j$: $\Phi(A) = \prod_i r_i + \prod_j c_j - \operatorname{per}(A) \le 2 - n!/n^n$, and equality holds if and only if every entry of $A$ equals $1/n$. |
| Outcome | Proved, in the record's words "an attributed computer-assisted proof with cited classical theorems and exact arithmetic". Standard: exact integer and rational computation for every finite check, cited published theorems for the analytic inputs, and independent AI review. It is not journal peer review and not a full Lean formalization. The theorem and its principal proof were already public in unrefereed form (see Attribution below), and the record claims no novelty for the theorem; the $n = 5, 6$ certificates used here are the record's own. |
| Formal verification | Lean 4, partial. Kernel-checked with only `propext`, `Classical.choice` and `Quot.sound`: four building blocks of the matrix proof (reduction to boundary maximizers, Hall domination, the Gurvits permanent floors, a complementary-minor entropy lemma), the scalar layer of the Hall argument for $11 \le n \le 15$, two near-zero polynomials for $n = 8, 9$, a scalar quadratic lemma, and the sign of Kafidov's final inequality at $n = 15, 16$. The arithmetic of the $n = 5, 6$ certificates is checked with `native_decide` (computational evidence). The full theorem `Dittert.dittert_5_15` is not proved in Lean. Details: [lean/README.md](lean/README.md). |
| Related problem | None. Sibling attempt: [a quantitative van der Waerden inequality](../quantitative-van-der-waerden/README.md). |
| Made by | exactory math-solver harness (objective `dittert-conjecture`; the Lean work is the managed objective `objective-000001`), 2026-09-03 to 2026-09-07. |

Notation used below: $K_n$ is the set of nonnegative real $n \times n$ matrices with entry sum $n$; $U_n = J_n/n$ is the matrix with every entry $1/n$; $\gamma_n = n!/n^n$; $\lVert \cdot \rVert_F$ is the Frobenius norm; $m_n = (n-2)!\,((n-2)/(n-1)^2)^{n-2}$ is the Knopp–Sinkhorn minimum of the permanent over doubly stochastic matrices with a zero entry (the later records call it $\kappa_n$). Van der Waerden's inequality (Egorychev and Falikman, 1981) states $\operatorname{per}(B) \ge \gamma_n$ for every doubly stochastic $B$, with equality only at $U_n$. AM–GM is the inequality of arithmetic and geometric means.

The record lists earlier proofs for $n = 2$ (Sinkhorn 1984) and $n = 3$ (Hwang 1987), and 2026 preprints for $n = 4$ (Li, Xiong and Yang, arXiv:2607.29191), $n = 16$ (Kafidov, arXiv:2607.19439) and $n \ge 17$ (Pang, arXiv:2606.01531). The first novelty search of the record (2026-09-03) found nothing in print for $5 \le n \le 15$. The later completion attack found a public, unrefereed proof chain covering these dimensions in Pedro Paulo Marques do Nascimento's repository, and the Lean study found a prior $n = 5$ Lean formalization (`arthurborgesdev/dittert-conjecture-n5`, using `native_decide`).

## Results

1. Dittert's conjecture holds for every $5 \le n \le 15$, with equality only at $U_n$. The assembled proof is [record/attack/dittert-branch-complete-audit/PROOF.md](record/attack/dittert-branch-complete-audit/PROOF.md). It combines:
   - for $n = 5, 6$, the record's own certificates (results 2 and 3);
   - for $n = 7$, Hongyuan Lu's Hall, stationarity and entropy argument in Nascimento's reconstruction, re-derived in [COVERAGE_PROOF.md](record/attack/hall-n7-branch-coverage/COVERAGE_PROOF.md) and checked by a new exact program over all 6476 Hall cuts, 28 cut-size types and 62 closed leaf rectangles, which also rejects 94 omission mutations;
   - for $8 \le n \le 15$, Nascimento's Hall-cut argument, re-derived in [hall-n8-n15-branch-coverage/PROOF.md](record/attack/hall-n8-n15-branch-coverage/PROOF.md) and checked by a new exact program over 596 omitted-size pairs, 428 ordered scalar cases and 9 interval polynomials, with 65 regression tests;
   - a dimension-free proof that every entrywise positive global maximizer is $U_n$ ([BRANCH_TRANSPORT.md](record/attack/dittert-branch-complete-audit/BRANCH_TRANSPORT.md), section 3).

   The independent review is [study/independent-review.md](record/attack/dittert-branch-complete-audit/study/independent-review.md). It found "no unresolved analytic branch, missing Hall cut, unjustified sign choice, or incomplete interval cover". The predecessor assembly, [dittert-completion-tree/PROOF.md](record/attack/dittert-completion-tree/PROOF.md), has its own review, [final-evaluation.md](record/attack/dittert-completion-tree/study/final-evaluation.md).

2. For every $A \in K_5$: $\Phi(U_5) - \Phi(A) \ge \frac{32}{3125} \lVert A - U_5 \rVert_F^2$. Proof: an exact rational sum-of-squares identity, [units/1/draft.md](record/attack/dittert-conjecture-n5-to-n15/units/1/draft.md), certificate in `certified-special-case-check-1`. Standard: exact computation in two implementations; the first is exact throughout, the second checks one Gram matrix by a floating-point Cholesky factorization with a rigorous error bound.

3. For every $A \in K_6$: $\Phi(U_6) - \Phi(A) \ge \frac{128}{46656} \lVert A - U_6 \rVert_F^2$. Proof: [units/2/draft.md](record/attack/dittert-conjecture-n5-to-n15/units/2/draft.md), certificate in `certified-special-case-check-2`. Standard: the identity and the two multiplier Gram matrices are checked exactly. The $8436 \times 8436$ main Gram matrix is positive semidefinite by an exact integer certificate (`certified-special-case-check-4`, diagonal-dominance slack 1691794048955) and, separately, by a floating-point Cholesky factorization with the rigorous error bound of Higham (Accuracy and Stability of Numerical Algorithms, 2nd ed., Theorem 10.3).

4. Theorem R, a conditional reduction ([study/route-a-reduction-theorem.md](record/attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md), checked by a second reader in [units/3/evaluation.md](record/attack/dittert-conjecture-n5-to-n15/units/3/evaluation.md)). Let $n \ge 4$, $h_n = \sqrt{2\gamma_n}$, $\theta_n = 1 - h_n$, $\kappa_n = 1/((1-\gamma_n)(1 - 2h_n/3))$ and $c_n = 2\sqrt{\gamma_n \kappa_n}/\theta_n$. Let $\lambda_2(A) = 1 - \sigma_2(D_r^{-1/2} A D_c^{-1/2})$, where $\sigma_2$ is the second singular value and $D_r$, $D_c$ are the diagonal matrices of row and column sums. If every $A \in K_n$ with a zero entry and $\Phi(A) \ge 2 - \gamma_n$ has $\lambda_2(A) \ge c_n$ (the hypothesis $G(n, c_n)$), then Dittert's conjecture holds at $n$. The record gives $c_7 = 0.183$ down to $c_{15} = 0.0035$. The hypothesis was not proved (see What did not work).

5. The final inequality of Kafidov's $n = 16$ proof, $m_n - \gamma_n - n^3 m_n^2/(4(1-\gamma_n)) > 0$, holds for $n = 16, 17$ and fails for $4 \le n \le 15$; at $n = 15$ the ratio of its two sides is 0.98712. Standard: exact rational arithmetic in two implementations (`certified-special-case-check-3`); the signs at $n = 15$ and $n = 16$ are also proved in Lean.

6. Lean theorems with standard axioms only, listed with their exact status in [lean/README.md](lean/README.md). Among them is the rectangle floor: every doubly stochastic $n \times n$ matrix $B$ with an $a \times b$ zero block, $a, b \ge 1$, $a + b \le n - 1$, has $\operatorname{per}(B) \ge \gamma_{n-a}\gamma_{n-b}/\gamma_{n-a-b}$ (`Dittert.gurvits_floors`). The record calls this bound already known.

Attribution, as the record states it: the $n = 7$ method is due to Hongyuan Lu ([commit 56397b70](https://github.com/lueluelue2006/dittert-n7-extension/tree/56397b70299278b338a286b90361180833dbf983)); the reconstruction and the unified $n \ge 8$ proof are due to Pedro Paulo Marques do Nascimento ([commit 894066bb](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701)). Classical inputs include Gurvits (arXiv:0711.3496), Cheon and Wanless (doi:10.1016/j.laa.2010.08.041) and Pula, Song and Wanless (doi:10.1016/j.laa.2010.08.015).

## Proof in brief

Dimensions 5 and 6. The gap $n^n(2 - \gamma_n - \Phi(A))$ is homogenized to a polynomial $Q$ of degree 6 in the $n^2$ entries $x$, and $D$ is the homogenized $\lVert A - U_n \rVert_F^2$. The certificate is an exact identity $Q - \lambda D = z_3^{T} M_0 z_3 + \sum_{u < v} x_u x_v\, z_2^{T} M_{uv} z_2$ with rational positive semidefinite Gram matrices, where $z_3$ and $z_2$ are the vectors of monomials of degree 3 and 2. Every term on the right is nonnegative on $K_n$, which gives results 2 and 3 with $\lambda = 32$ and $\lambda = 128$. The symmetry group generated by row permutations, column permutations and transposition reduces the Gram matrices to blocks of size at most 16 (main) and 22 (multipliers).

Dimensions 7 to 15. A global maximizer $A$ exists by compactness. Comparison with $U_n$ and AM–GM give, with $\operatorname{per}(A) = \gamma_n - \delta$, $\prod r_i = 1 - \rho$ and $\prod c_j = 1 - \sigma$, the budget $0 \le \rho, \sigma$ and $\rho + \sigma \le \delta \le \gamma_n$. A positive maximizer is uniform. For a boundary maximizer define the Hall parameter $\lambda = \min s_A(I,J)/(\lvert I \rvert + \lvert J \rvert - n)$ over row sets $I$ and column sets $J$ with $\lvert I \rvert + \lvert J \rvert > n$, where $s_A(I,J)$ is the sum of the entries in $I \times J$, and put $u = 1 - \lambda$. Then $0 < \lambda \le 1$, and a max-flow argument gives a doubly stochastic $B$ with $\lambda B \le A$ entrywise, so $\operatorname{per}(A) \ge \lambda^n \operatorname{per}(B)$; a minimizing cut leaves a zero block in $B$.

Every minimizing cut is full, marginal or proper. A full cut gives $A = B$, which van der Waerden's equality case excludes. For the other cuts $B$ has a permanent floor $M$: the rectangle floor $\gamma_{n-a}\gamma_{n-b}/\gamma_{n-a-b}$ from Gurvits's capacity inequality, the one-zero floor $m_n$, and for $8 \le n \le 10$ the two-zero floor $m_n(1 + 1/(2n^2))$. The two-zero floor applies because Cheon–Wanless Theorem 3.7 gives a boundary maximizer two zeros in distinct rows and columns; it rests on Minc's averaging theorem and an exact polynomial check. For $8 \le n \le 15$ a deficit lemma gives $\delta \ge C u^2$ with an explicit $C$ for each cut, and exact rational inequalities such as $M - \gamma_n - n^2 M^2/(4C) > 0$ contradict the budget on every cut except the two marginal cuts at $n = 8, 9$. Those two need stationarity caps and nine interval polynomials (two near-zero and seven support polynomials) with positive Bernstein coefficients. The case $n = 7$ uses Lu's complementary-minor entropy method and three bivariate Bernstein subdivision trees. So no maximizer has a zero entry, and the uniform matrix is the unique maximizer.

## What did not work

1. Exact sum-of-squares certificates beyond $n = 6$. At $n = 7, 8$ the main blocks reach size 83 and the multiplier blocks 2514, and the pair-orbit computation needs about $7 \times 10^{10}$ pairs; from $n = 9$ the blocks are 424 and 22818 and larger. A direct attempt at $n = 7$ exceeded 11 GB within 300 s ([units/5/draft.md](record/attack/dittert-conjecture-n5-to-n15/units/5/draft.md)).
2. The published boundary-exclusion route stops at $n = 16$ (result 5). The record locates the loss in the uniform dilation step, which bounds the capacity $\operatorname{cap}(A) = \inf_{x > 0} \prod_i (Ax)_i / \prod_j x_j$ below by $(1-t)^n$; on the sampled near-doubly-stochastic matrices this bound loses a factor between 400 and 17000.
3. The spectral route through Theorem R (attack `spectral-gap-near-maximisers`, finished with a barrier). Its hypothesis $G(n, c_n)$ was not proved. The non-negativity condition of Theorem R is the binding constraint, by a factor 12.1 at $n = 7$ rising to 6555 at $n = 20$. An effective-resistance bound on the scaling potentials was proved (unit 1) but does not remove that condition: the entrywise lower bound it would need is false on the natural relaxation (smallest entry $3.6 \times 10^{-28}$ at $n = 6$). A reduction to a bound on the Sinkhorn scaling cost $-\log \operatorname{cap}(A)$ in terms of the margins of $A$ was proved (unit 2), and the record shows that no uniform constant works for it. The exact local constant of van der Waerden's inequality at $U_n$ is $n/(2(n-1))$, and a quadratic strengthening with it adds nothing beyond Knopp–Sinkhorn (unit 3). The record names the barrier as "a lower bound on per(A) that is strong exactly when cap(A) is small" (unit 5).
4. The quantitative van der Waerden route (sibling attempt). Its bound with constant $1/(2n)$ excludes only the small-cost branch of a fixed-point inequality. On the afternoon of 2026-09-04 the record claimed that it closes every $n \ge 8$; that was wrong because the solution set has a second, large-cost branch, and the claim was corrected the same evening. What stands is a structure theorem: every counterexample at $n \ge 8$ would be near-decomposable.
5. The final proof does not show that this old large-cost branch is empty. It covers every global maximizer by the Hall case split, with no bound on the old cost ([BRANCH_TRANSPORT.md](record/attack/dittert-branch-complete-audit/BRANCH_TRANSPORT.md), section 1).
6. Lean. The $n = 5, 6$ certificates (Gram matrices of size 2925 and 8436) were not feasible for the kernel as stored, so their check uses `native_decide`; the $n = 5$ matrix theorem is only stated, with `sorry`. The managed Lean objective stopped with 4 of its 17 obligations accepted.
7. Errors found and repaired: an earlier audit read a hypothesis of Pula, Song and Wanless as both parameters greater than 2, where the paper says at least 2 ([SOURCE_CORRECTION.md](record/attack/dittert-branch-complete-audit/SOURCE_CORRECTION.md)); the exact $n = 6$ checker printed a failure without a failing exit status, which was repaired and regression-tested; its complete original log shows positive slack.

## Open questions

As the record states them:

1. A full Lean proof of the theorem. The obligations of `objective-000001` that are not accepted are listed in [record/attack/SEARCH_TREE.md](record/attack/SEARCH_TREE.md). The $n = 5, 6$ case has no Lean route yet. The maximizer zero pattern, the two-zero floor, the $n = 7$ certificates and the bridges for $n = 7$ and $8 \le n \le 10$ were not proved. The scalar certificates for $8 \le n \le 10$ and $11 \le n \le 15$, the bridge for $11 \le n \le 15$ and the assembly bridge were proved in the blueprint but not accepted by the controller when work stopped.
2. Method questions that the record keeps open but no longer needs for the theorem ([record/STATUS.md](record/STATUS.md), tasks T1, T2 and T6): a permanent lower bound for near-decomposable doubly stochastic matrices; the two-column inequality (I2) of the sibling attempt; a 1.3 percent improvement of Kafidov's argument at $n = 15$. An exact certificate at $n = 7$ (task T5) is not needed.
3. $G(n, c_n)$ as a spectral statement in its own right. The record does not reclassify it as proved by the Hall conclusion.
4. Whether the maximum of $\Phi$ on the face $a_{11} = 0$ equals $2 - m_n$ for every $n \ge 4$; numerically it does at $n = 5, 6$.

## How to check

Python: the record used Python 3.13.8 with numpy 2.5.2, scipy 1.18.1, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0, cvxpy 1.9.2 and clarabel 0.11.1 (unit 1 names cvxpy 1.7). Most `check.sh` wrappers call `../../../../.venv/bin/python`, that is a virtual environment at `record/.venv`; the commands below call the scripts directly. Run them one at a time; the record ran them single-threaded at low priority.

Certificates, from `record/attack/dittert-conjecture-n5-to-n15/deterministic/`:

| Check | Command | Expected end of output |
|---|---|---|
| $n = 5$ | `cd certified-special-case-check-1 && python check.py` | `CHECK PASS` (about 25 minutes) |
| $n = 6$ | `cd certified-special-case-check-2 && python check_verified.py certificate6.json` | `CHECK PASS` (518 s, peak memory 17 GB) |
| $n = 6$, exact main Gram | `cd certified-special-case-check-4 && python check.py` | `EXACT PSD PASS`, slack 1691794048955 (about 16 minutes) |
| Kafidov threshold | `cd certified-special-case-check-3 && python check.py` | `positive` only at $n = 16, 17$, then `CHECK PASS` |

The Hall-route checks import Nascimento's verifiers from `record/attack/dittert-completion-tree/study/external-proof`, which is not copied. Clone it there at the pinned commit:

```sh
git clone https://github.com/pedromnasc/dittert-conjecture-proof record/attack/dittert-completion-tree/study/external-proof
git -C record/attack/dittert-completion-tree/study/external-proof checkout 894066bbaa715138c98bf3cb7c6fdb4f39a37701
```

| Check | Directory | Command | Expected |
|---|---|---|---|
| $n = 7$ | `record/attack/hall-n7-branch-coverage/deterministic/certified-special-case-check-1` | `python generate_manifest.py && python check_manifest.py` | last line `{"status": "pass", "cut_mask_count": 6476, "rejected_omissions": 94}` |
| $8 \le n \le 15$ | `record/attack/hall-n8-n15-branch-coverage/deterministic/certified-witness-chain-1` | `sh check.sh` | `Independent direct-Bernstein coverage passed: 596 cut-size pairs, 428 scalar cases, 9 marginal certificates, 65 regressions.` |
| completion checks | `record/attack/dittert-completion-tree/deterministic/certified-special-case-check-1`, `-2`, `-3`, `-5` | `sh check.sh` in each, with a virtual environment at `record/.venv` | the outputs saved next to each script (check `-4` is the Lean scalar lemma, see [lean/README.md](lean/README.md)) |

`check_manifest.py` (on the included `manifest.json`) and `independent_coverage.py` import no code from Nascimento's repository and run without the clone. `generate_manifest.py` rewrites `manifest.json`.

Lean: build commands and expected axiom lists for every project are in [lean/README.md](lean/README.md).

## Contents of this folder

| Path | Content |
|---|---|
| `README.md` | this summary |
| `paper/` | the technical note "Scalar Hall Exclusion in Dimensions 11 through 15: A Partial Lean Formalization" by Ryosuke Shiroshita (`main.pdf`, `main.tex`, `references.bib`, `abstract.txt`), published on Zenodo under CC0 1.0, DOI [10.5281/zenodo.22412449](https://doi.org/10.5281/zenodo.22412449); it covers the Lean results for $11 \le n \le 15$ and the near-zero polynomials |
| `lean/` | seven Lean projects with an index, [lean/README.md](lean/README.md) |
| `record/` | the curated working record in the layout of the original workspace, with an index, [record/README.md](record/README.md) |
