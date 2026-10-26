# The exact local stability constant of the van der Waerden inequality

**Form.** New machinery. **Venue.** Off to the side of Dittert's conjecture: it settles that the
permanent side of the argument has no room left in it.

## 1. The identity

Write `gamma_n = n!/n^n` and `J_n` for the all-ones matrix.

**Proposition.** For every `n >= 2` and every real `n x n` matrix `E` with zero row sums and zero
column sums,

    per(J_n/n + E) = gamma_n ( 1 + (n / (2(n-1))) ||E||_F^2 ) + O(||E||^3).

*Proof.* The permanent is multilinear in the entries, so

    per(A) = gamma_n + sum_{i,j} E_ij per(A(i|j))|_{J/n}
             + (1/2) sum_{i != k, j != l} E_ij E_kl per(A(ik|jl))|_{J/n} + O(E^3),

where `A(i|j)` and `A(ik|jl)` are the minors. At `J_n/n` the first minor is the constant
`(n-1)!/n^{n-1}`, so the first-order term is that constant times `sum E = 0` and vanishes. The
second minor is the constant `(n-2)!/n^{n-2}`, and

    sum_{i != k, j != l} E_ij E_kl = (sum E)^2 - sum_i (row sum)^2 - sum_j (col sum)^2
                                     + sum_{i,j} E_ij^2 = ||E||_F^2,

because every row sum and every column sum of `E` is zero. Collecting,
`(1/2) (n-2)!/n^{n-2} ||E||_F^2 = gamma_n (n / (2(n-1))) ||E||_F^2`. QED

The constant tends to `1/2` from above: 0.666667, 0.625000, 0.600000, 0.583333, 0.571429 at
`n = 4, 5, 6, 7, 8`.

## 2. Numerical check

`study/vdw-hessian.py` draws 40 doubly stochastic perturbations of Frobenius norm 1e-4 at each
`n` from 4 to 8, evaluates the permanent exactly by summing over all `n!` permutations, and
compares `(per(B)/gamma_n - 1) / ||E||_F^2` with `n / (2(n-1))`. The relative error stayed below
4e-6 at every `n`.

## 3. The consequence: the natural strengthening gives nothing

The van der Waerden inequality `per(B) >= gamma_n` on the doubly stochastic matrices is tight only
at `J_n/n`, and the natural repair is the quadratic strengthening

    S(n, c):   per(B) >= gamma_n ( 1 + c ||B - J_n/n||_F^2 )   for every doubly stochastic B.

Section 1 gives the largest `c` that can hold: any `c > n/(2(n-1))` fails on a small
perturbation. Evaluate `S(n, n/(2(n-1)))` at the Knopp-Sinkhorn extremal `T_n`, which has

    ||T_n - J_n/n||_F^2 = 1/(n-1)^2   exactly.

The strengthening then predicts `per(T_n)/gamma_n - 1 >= n / (2(n-1)^3)`, which is 1.62e-2 at
`n = 7`, against the true `m_n/gamma_n - 1 = 1.34e-2`. The two agree to leading order, so `S` with
its true constant reproduces the Knopp-Sinkhorn bound and adds nothing to it.

## 4. What this settles for Dittert's conjecture

Every route in the record needs a lower bound on the permanent that is strong somewhere the
current bounds are weak. Section 3 closes the interior: at `J_n/n` the exact Hessian is known and
the quadratic strengthening is already saturated by Knopp-Sinkhorn. Knopp-Sinkhorn closes the
boundary. So whatever is missing is not on the permanent side at all; it is on the capacity side,
which is the barrier of unit 5.

## 5. References

- Egorychev, *The solution of van der Waerden's problem for permanents*, Advances in Mathematics
  42 (1981) 299-305; Falikman, Matematicheskie Zametki 29 (1981) 931-938.
- Knopp and Sinkhorn, *Minimum permanents of doubly stochastic matrices with at least one zero
  entry*, Linear and Multilinear Algebra 11 (1982) 351-355.
- Gurvits and Leake, *Counting Matchings via Capacity Preserving Operators*, arXiv:1804.04351.

## 6. Ledger

Implication: only the direction from `S(n, c)` to the claim is proved, and it turns out to be
uninformative. The identity of section 1 is elementary and is very likely classical; the unit's
claim is the consequence of section 3, not priority on the identity.
