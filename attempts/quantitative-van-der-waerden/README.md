# A quantitative van der Waerden inequality

| | |
|---|---|
| Claim | For every integer $n \ge 2$ and every doubly stochastic real $n \times n$ matrix $B$: $\operatorname{per}(B) \ge \frac{n!}{n^n}\left(1 + \tfrac{1}{4} \lVert B - J_n/n \rVert_F^2\right)$, where $J_n$ is the all-ones matrix and $\lVert \cdot \rVert_F$ the Frobenius norm. |
| Outcome | Partially proved. Proved for every $n \ge 2$ with the constant $1/(2n)$ in place of $1/4$, in the stronger form $\operatorname{per}(B) \ge \frac{n!}{n^n} \exp(\lVert B - J_n/n \rVert_F^2/(2n))$; proved with the sharp constant $1/4$ at $n = 3$ (and with constant 1 at $n = 2$). The claim with $1/4$ is open for $n \ge 4$; a multi-start numerical search at $n = 3, \dots, 9$ found no counterexample. Standard: written proofs, read by the coordinating agent and re-checked by an independent numerical reimplementation; the $n = 3$ identity is checked in exact rational arithmetic. Not Lean, not peer review. |
| Formal verification | None completed. The $n = 3$ case is encoded in Lean (`lean/QvdW3b.lean`); the rewritten file was never run, and an earlier version failed in its Schur lemma. |
| Related problem | None. The attack was made for the [Dittert attempt](../dittert-conjecture/README.md). |
| Made by | exactory math-solver harness (objective `dittert-conjecture`, attack `quantitative-van-der-waerden`, 6 moves), 2026-09-04. |

Notation: $\gamma_m = m!/m^m$; $E = B - J_n/n$; for a column $j$ of $B$, $d_j = \lVert \mathrm{col}_j(B) - \mathbf{1}/n \rVert^2$, and $d'_i$ is the same quantity for row $i$; $g(k) = ((k-1)/k)^{k-1}$, so that $\gamma_n = \gamma_{n-1}\, g(n)$; $K(v) = \prod_s (1 - v_s)^{1 - v_s}$ for a probability vector $v$, with $0^0 = 1$. $Q(c)$ denotes the claim with the constant $c$ in place of $1/4$. The capacity of a polynomial $p$ in $m$ variables with nonnegative coefficients is $\operatorname{cap}(p) = \inf_{x > 0} p(x)/(x_1 \cdots x_m)$, and for a matrix $A$, $\operatorname{cap}(A) = \inf_{x > 0} \prod_i (Ax)_i / \prod_j x_j$. A polynomial is H-stable if it has no zero when every variable has positive real part. AM–GM is the inequality of arithmetic and geometric means.

The claim restates, without any spectrum, the barrier met by the record's spectral route to Dittert's conjecture. Result 7 below is its application to that conjecture.

## Results

1. Theorem 1 (one column). For every $n \ge 2$, every doubly stochastic $B$ and every column $j$, $\operatorname{per}(B) \ge \gamma_{n-1} K(\mathrm{col}_j(B))$, and the same for every row. Equality holds whenever the column is uniform on its support, for example at the Knopp–Sinkhorn face minimizers and at $(I + C_3)/2$, where $C_3$ is the cyclic permutation matrix. Proof: [record/units/1/draft.md](record/units/1/draft.md) and [record/study/route-capacity.md](record/study/route-capacity.md), sections 2.1 to 2.3. The record states that it contains the Knopp–Sinkhorn bound and refines Gurvits's degree bound.

2. Theorem 2 ($c = 1/(2n)$). For every $n \ge 2$ and every doubly stochastic $B$,
   $\operatorname{per}(B) \ge \gamma_n \exp\left(\max(\max_j d_j, \max_i d'_i)/2\right) \ge \gamma_n \exp\left(\lVert E \rVert_F^2/(2n)\right) \ge \gamma_n \left(1 + \lVert E \rVert_F^2/(2n)\right)$.
   Proof: [record/units/2/draft.md](record/units/2/draft.md), route-capacity.md sections 2.4 and 2.5.

3. The case $n = 3$, sharp. For every doubly stochastic $3 \times 3$ matrix $B$, $\operatorname{per}(B) \ge \frac{2}{9}\left(1 + \frac14 \lVert B - J_3/3 \rVert_F^2\right)$, with equality exactly at $J_3/3$ and at the six row and column permutations of $(I + C_3)/2$; no constant above $1/4$ works at $n = 3$. Proof: [record/units/3/draft.md](record/units/3/draft.md) and [record/study/route-interpolation.md](record/study/route-interpolation.md), Theorem 2.

4. At $n = 2$, $\operatorname{per}(B) = \gamma_2 (1 + \lVert E \rVert_F^2)$ (route-interpolation.md, Theorem 1).

5. A local theorem for every $n \ge 5$ (route-interpolation.md, Theorem 3): with $\delta_E = \lVert E \rVert_F$,
   $\operatorname{per}(B)/\gamma_n - 1 \ge \left[\frac{n}{2(n-1)} - \frac{2n}{3(n-1)(n-2)}\right] \delta_E^2 - \sum_{k=4}^{n} \beta_k \delta_E^k$ with explicit $\beta_k$. So $Q(c)$ holds on a ball $\delta_E \le \rho_n(c)$; for example $\rho_7(1/7) = 0.1098$ and $\rho_7(1/4) = 0.0919$.

6. An $m$-column form, $\operatorname{per}(B) \ge \gamma_{n-m} C_m(V) K(w)$ for an $n \times m$ block $V$ of $B$ whose row sums $w_s$ are all below 1, where $C_m$ is the capacity of the $m$-column polynomial (route-capacity.md, section 2.6). The record calls it proved with an implicit constant, because $C_m$ has no closed form for $m \ge 2$.

7. Application to Dittert's conjecture ([record/units/5/draft.md](record/units/5/draft.md), with Lemma 2' of [record/study/lemma2-prime.md](record/study/lemma2-prime.md)). For $n \ge 8$, if $A$ is a nonnegative $n \times n$ matrix with entry sum $n$, a zero entry and $\prod_i r_i + \prod_j c_j - \operatorname{per}(A) \ge 2 - \gamma_n$, its Sinkhorn scaling $B$ (the doubly stochastic matrix $D_1 A D_2$ with positive diagonal $D_1, D_2$) has scaling cost $-\log \operatorname{cap}(A) \ge K_2(n)$ and $\lambda_2(B) = 1 - \sigma_2(B) \le 1 - \sqrt{2 n K_2(n)}$, where $\sigma_2$ is the second singular value. Here $K_2(n)$ is the second solution of a fixed-point equation (0.047 at $n = 8$, where the bound on $\lambda_2(B)$ is 0.13). In the record's words, "expander counterexamples do not exist"; the near-decomposable case is not excluded.

Measured, not proved:

- Upper bounds on the sharp constant $c^*(n)$ found by multi-start search: 0.250000, 0.333333, 0.418403, 0.460519, 0.486709, 0.497450 at $n = 3, \dots, 8$ ([record/study/qvdw-constant-output.txt](record/study/qvdw-constant-output.txt)), with minimizer $(I + C_n)/2$ at $n = 3, 4, 5$. The latest deterministic run ([result.json](record/deterministic/numerical-optimisation-run-1/result.json)) reports larger values at $n = 6, 7, 8$ (0.471162, 0.489958, 0.514493) and 0.528087 at $n = 9$. Every value found is at least $1/4$.
- The two-column form $\operatorname{per}(B) \ge \gamma_n \exp((d_j + d_l)/2)$ holds numerically at $n = 4, \dots, 7$, with ratio 1 only at the centre; the column-plus-row form is false (`study/two-column-test.py`).

## Proof in brief

Write $p_B(x) = \prod_i \sum_j b_{ij} x_j$, whose coefficient of $x_1 \cdots x_n$ is $\operatorname{per}(B)$. Differentiating once in $x_n$ and setting $x_n = 0$ gives $q(x) = \sum_r v_r \prod_{s \ne r} l_s(x)$, where $v$ is the last column and $l_s$ the row forms without that column. Two weighted AM–GM steps give $q(x) \ge K(v)\, x_1 \cdots x_{n-1}$, so the capacity of $q$ is at least $K(v)$ (Lemma A). Gurvits's theorem for the H-stable polynomial $q$ gives $\operatorname{per}(B) \ge \gamma_{n-1} \operatorname{cap}(q)$ (Lemma B; Gurvits, arXiv:0711.3496, Fact 4.9(2) and Corollary 2.5). This is Theorem 1.

For Theorem 2, $\varphi(t) = (1-t)\log(1-t)$ has $\varphi'' \ge 1$ on $[0, 1)$; Taylor's formula at $t = 1/n$ summed over the coordinates gives $K(v) \ge g(n) \exp(\lVert v - \mathbf{1}/n \rVert^2/2)$ (Lemma C). With $\gamma_{n-1} g(n) = \gamma_n$ and $\lVert E \rVert_F^2 = \sum_j d_j \le n \max_j d_j$ the theorem follows.

For $n = 3$, on doubly stochastic matrices the identity $\operatorname{per}(B)/\gamma_3 - 1 - \frac14 \lVert E \rVert_F^2 = \sum_{\text{rows } b} \left(1 - 4 e_2(b) + 9 e_3(b)\right)$ holds, where $e_2, e_3$ are elementary symmetric functions of the row. Each summand is Schur's expression $\sum x(x-y)(x-z) \ge 0$.

## What did not work

1. One column at a time. Theorem 1 is an equality at sparse uniform columns, so no bound of the form $\gamma_{n-1} F(\text{column})$ gives a constant above about $0.6/n$.
2. Two columns one after the other. The sequential form $\operatorname{cap}(q_{n-2}) \ge g(n-1) e^{d'/2} \operatorname{cap}(q_{n-1})$ is false, with ratio 0.967 at $n = 4$; the gain of a pair is a joint quantity.
3. The joint two-column inequality (I2) (unit 6 and route-capacity.md, "Two-column theorem" and "Drop lemma via the two-scalar reduction"): $C_2(v, v') K(v + v') \ge g(n) g(n-1) \exp((d + d')/2)$ for probability vectors $v, v'$ with $v + v' \le \mathbf{1}$, where $C_2$ is the capacity of the two-column polynomial, $d = \lVert v - \mathbf{1}/n \rVert^2$ and $d' = \lVert v' - \mathbf{1}/n \rVert^2$. It holds numerically, is proved for disjoint supports and near the centre, and was reduced to an elementary inequality (star) with 59 percent numerical room plus an oscillation bound (T) on the optimizer of the two-column capacity. (T) was not proved: every available lower bound on the Hessian of the capacity goes through the smallest column entry, which can be 0.02 on the $n = 7$ region.
4. Interpolation along the segment from $J_n/n$ to $B$ (route-interpolation.md, section 6): one-variable inputs give at most $\exp(\lVert E \rVert_F^2/(2n))$ at the endpoint; inequalities that hold permutation by permutation give a negative constant for every $n \ge 5$; bounding the Taylor tail diagram by diagram gives $54\,\delta_E^2$ where $0.17\,\delta_E^2$ is needed at $n = 7$. The chain through the Holens–Doković inequalities fails at $n = 22$ (Wanless, Linear Algebra Appl. 286 (1999)) and could give at most $Q(1/(n-1)^2)$.
5. The local constant $n/(2(n-1))$ of the Hessian at $J_n/n$ fails globally from $n = 3$ on (slack $-5.6 \times 10^{-2}$ at $n = 3$ down to $-1.9 \times 10^{-4}$ at $n = 7$).
6. The deduction for Dittert's conjecture. Theorem 2 with Lemma 2' gives a fixed-point inequality whose solution set has two branches. On 2026-09-04 the record first reported that it closes every $n \ge 8$; that was wrong, and it was corrected the same evening (unit 5, section 4; [record/study/application.md](record/study/application.md), section 2). Only the small-cost branch is excluded. Section 3 of route-capacity.md is not among the files the record lists as corrected; it still states that every $n \ge 7$ closes, subject to selecting the least fixed point, which is the step that failed.
7. The Lean check of $n = 3$. The builds of `QvdW3.lean` did not finish under a machine load average near 175. The first version of `QvdW3b.lean` ran for 48 minutes and then failed in `schur_three`, "linarith failed" in every branch ([record/deterministic/formal-check-1/lean-direct3.log](record/deterministic/formal-check-1/lean-direct3.log)). The run of the rewritten `QvdW3b.lean` was stopped by request after 14 minutes, and the file has not been run since ([record/deterministic/formal-check-1/README.md](record/deterministic/formal-check-1/README.md) and section 6 of the Dittert record's [STATUS.md](../dittert-conjecture/record/STATUS.md)).

## Open questions

As the record states them (units 5 and 6, route-interpolation.md section 7):

1. $Q(1/4)$ for $n \ge 4$, and $Q(1/n)$, which would put $n = 7$ into the structure theorem of result 7. The record names (I2) as the one inequality left for $Q(1/n)$; for $n = 7$ any two-column bound with constant above 0.36 per column would do.
2. The near-decomposable branch: a bound $\operatorname{per}(B) \ge (1 + c)\gamma_n$ for doubly stochastic $B$ with $\lambda_2(B) \le 0.13$ and $c > K_2(n)$, that is $c > 0.05$ at $n = 8$. The record notes that the block-diagonal value is about $2.5\gamma_n$.
3. At $n = 4$, the degree-4 polynomial inequality that is $Q(1/4)$ was not certified.
4. A local constant uniform in $n$, for example a bound $\lvert \alpha_k \rvert \le C^k \delta_E^k$ on the Taylor coefficients, which needs the cancellation between the Möbius diagrams of route-interpolation.md.
5. The Lean check of the $n = 3$ case.

## How to check

The scripts need Python 3 with numpy, scipy, sympy and mpmath (the record used Python 3.13.8, numpy 2.5.2, scipy 1.18.1, sympy 1.14.0, mpmath 1.3.0). Run them from `record/study/` or the step folder.

| Check | Command | Expected |
|---|---|---|
| Theorems 1 and 2 on random and structured doubly stochastic matrices, $n = 2, \dots, 8$ | `python verify-capacity-claim.py` | minimum ratios at least 1, then `Both statements held in every case: True` |
| the $n = 3$ identity in exact arithmetic | `python route-interpolation-06-exact.py` | the lines of `route-interpolation-06-output.txt` |
| $c^*(n) \ge 1/4$ numerically, $n = 3, \dots, 9$ | in `record/deterministic/numerical-optimisation-run-1`: `python check.py` | ends with `PASS: no ratio below 1/4 at n = 3, 4, 5, 6, 7, 8, 9, ...` |
| the two branches $K_1(n)$, $K_2(n)$ | `python branch-structure.py` | the values quoted in units 5 and 6 (30 digits) |
| Lean, $n = 3$ | in `lean/`: `lake exe cache get`, then `lake env lean QvdW3b.lean` | expected by the record, never observed: no errors and `'qvdw_three' depends on axioms: [propext, Classical.choice, Quot.sound]` |

Each other study script has its output saved next to it as `*-output.txt`.

## Contents of this folder

| Path | Content |
|---|---|
| `README.md` | this summary |
| `lean/` | `QvdW3.lean` and `QvdW3b.lean` (two encodings of the $n = 3$ case), `lakefile.toml`, `lean-toolchain`, `lake-manifest.json` (Lean v4.33.1, Mathlib v4.33.1) |
| `record/` | the curated record of the attack, with an index, [record/README.md](record/README.md); the six unit drafts in `record/units/` are the write-ups of this attempt (there is no separate paper) |
