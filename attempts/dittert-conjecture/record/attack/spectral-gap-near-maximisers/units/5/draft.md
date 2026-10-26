# Where the spectral route to Dittert's conjecture stops

**Form.** Barrier. **Venue.** On the path, as the statement of where the path stops. Every route
in `study/routes-rubric.md` reduces to the one missing statement named in section 3.

## 1. Theorem R and its two thresholds

Theorem R closes Dittert's conjecture at `n` once every `A in K_n` with a zero entry and
`phi(A) >= 2 - gamma_n` has spectral gap at least `c_n`. Two separate steps set that threshold.

- **The non-negativity condition (N)** of its Lemma 2, which the corrected competitor must satisfy.
  It needs `lambda_2 >= bar c_N = 2 sqrt(gamma_n kappa_n) / theta_n`.
- **The final contradiction**, which needs `lambda_2 >= bar c_C = 2 m_n kappa_n / theta_n`.

`c_n` is the larger of the two, and their ratio is

    bar c_N / bar c_C = 1 / sqrt(gamma_n kappa_n),

which is 12.1 at `n = 7`, 51.7 at `n = 10`, 576.8 at `n = 15` and 6555 at `n = 20`
(`study/binding-constraint.py`). So condition (N) is binding everywhere on the open range, by up
to three orders of magnitude.

The reason is structural, not an artefact of the proof. The margins `u = 1 - r` have size
`sqrt(delta)`, so the linear correction `alpha` has size `sqrt(delta) / lambda_2` and
non-negativity costs a square root, while the contradiction is linear in `delta`.

## 2. What the best chain in the record reaches

Against `bar c_C`, the crude Cheeger-and-blocks chain proves `lambda_2 >= 1/(2 n^4)` and settles
`n >= 15`; with a block capacity bound `exp(-C eps)` in place of `(1 - eps)^n` it settles
`n >= 10` for `C = 2` and `n >= 12` for `C = 4`. Against `bar c_N` it settles nothing below
`n = 35`.

Move 7 refined the chain: in the hard branch the spectral gap is bounded above by 0.562 at
`n = 7`, 0.0635 at `n = 10`, 1.2e-3 at `n = 15` and 1.7e-5 at `n = 20`, so Cheeger gives a
conductance of at most `sqrt(2 lambda_2)` and a cut mass of at most `n sqrt(2 lambda_2)`, and the
block bound on the Sinkhorn scaling closes the case when `K_max(n) > n^4 / theta_n`, which happens
from about `n = 23`. Ten dimensions gained, and still short of 7 to 15.

That refinement is currently illusory and the record says so: the spectral upper bound it uses
comes from Theorem R's Lemma 2 and therefore carries condition (N), which is exactly what fails
when `lambda_2` is small.

## 3. The barrier

Move 8 split the argument into three interfaces. Interface (i), the entropy competitor, is closed
and tight, so no gain is available there. Interface (iii) is closed, a theorem. Interface (ii) is
open, and moves 3 to 7 established what it does not need:

- not a better competitor, because the Sinkhorn scaling already attains the minimum of the
  relative entropy;
- not only a non-negativity fix, because the effective-resistance lemma of unit 1 does not remove
  condition (N) on its own and the truncation repair enlarges the margins it repairs;
- not a universal constant, because a block-diagonal direction makes the margins vanish to first
  order while the scaling cost does not (unit 2, section 3).

What is left is one statement.

> **The barrier.** A lower bound on `per(A)` that is strong exactly when `cap(A)` is small, that
> is, when `A` is quantitatively near-decomposable.

Every bound in the record degrades in that regime. Unit 3 shows the permanent side has no room
left at either extremal: the exact van der Waerden Hessian closes the interior and Knopp-Sinkhorn
closes the boundary. So the bound has to come from the capacity side, and the same gap sits on the
capacity side of Gurvits and Leake, arXiv:1804.04351, whose bounds degrade where the capacity is
small.

## 4. Why this is a barrier and not a task list

The dichotomy of unit 2, section 4 is exhaustive. Either `cap(A) >= gamma_n / m_n`, in which case
`per(A) >= cap(A) m_n >= gamma_n` contradicts `per(A) = gamma_n - delta` with `delta > 0` and the
case closes; or `-log cap(A) > log(m_n / gamma_n)`, and in that branch the permanent lower bound
has to take over. There is no third branch, the permanent side is saturated, and the only
candidate for the second branch has threshold `n >= 23` against a target of 7 to 15.

## 5. References

- Gurvits and Leake, *Counting Matchings via Capacity Preserving Operators*, arXiv:1804.04351.
- Knopp and Sinkhorn, *Minimum permanents of doubly stochastic matrices with at least one zero
  entry*, Linear and Multilinear Algebra 11 (1982) 351-355.
- Cheon and Wanless, *An update on Minc's survey of open problems involving permanents*, Linear
  Algebra and its Applications 436 (2012) 1197-1218.
- Theorem R, its Lemmas 2 and 3, and the constants:
  `attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md`.

## 6. Ledger

Bound quality: the refined chain improves the threshold from `n >= 35` to `n >= 23` and the target
range is 7 to 15, so the improvement is real and insufficient. Obligations: the barrier statement
of section 3, and the removal of condition (N), which the move-7 improvement silently assumed.
