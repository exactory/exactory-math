# No matrix with a small spectral gap reaches the Dittert ceiling, at n = 5 to 12

**Form.** Computational evidence. **Venue.** On the path: it is the only direct test of the
spectral hypothesis Theorem R needs, and it covers eight of the eleven dimensions Dittert's
conjecture leaves open.

## 1. The statement and why it is the contrapositive

Write `K_n` for the non-negative `n x n` matrices of total sum `n`, `gamma_n = n!/n^n`,
`phi(A) = prod_i r_i + prod_j c_j - per(A)` for the Dittert functional, and
`lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2})` for the spectral gap of the weighted
bipartite graph of `A`. Theorem R needs

    G(n, c_n):  every A in K_n with a zero entry and phi(A) >= 2 - gamma_n
                has lambda_2(A) >= c_n,    c_n = 2 sqrt(gamma_n kappa_n) / theta_n.

`G(n, c_n)` cannot be tested by sampling its hypothesis set, and the reason is structural.
Dittert's conjecture says `phi <= 2 - gamma_n` on `K_n` with equality only at `J_n/n`, which has
no zero entry. So the hypothesis set of `G(n, c_n)` is exactly the set of counterexamples to
Dittert's conjecture at `n`: it is conjecturally empty, and Theorem R uses `G` in the only way an
empty hypothesis can be used, inside a proof by contradiction. Two consequences follow, and both
constrain any future work here.

1. A search for a counterexample to `G` is a search for a counterexample to Dittert's conjecture.
   Cheon and Wanless report that none is known at any `n`.
2. `G` must be proved from `phi(A) >= 2 - gamma_n` alone and never from Dittert's conjecture, or
   Theorem R becomes circular.

The contrapositive has a large constraint set and can be tested:

    maximise  phi(A)   over  A in K_n  with a zero entry  and  lambda_2(A) <= c_n.

A maximum strictly below `2 - gamma_n` is `G(n, c_n)` at that `n`.

## 2. The computation

`deterministic/numerical-optimisation-run-1` runs it. `phi` uses a vectorised Ryser permanent over
all `2^n` column subsets. `A` is parametrised as `exp(theta)` with the `(0,0)` entry fixed at zero
and the matrix rescaled to total sum `n`, so every iterate is in `K_n` with a zero by
construction. The spectral constraint enters as a penalty of 50 on the excess. L-BFGS-B,
multi-start, from random starts at four spreads and from near-decomposable starts, seeded with
20260904, so the run reproduces exactly. `check.sh` re-runs the search and fails if any shortfall
is non-positive; `result.json` records `pass`.

## 3. Result

| n | `c_n` | ceiling `2 - gamma_n` | max `phi` | shortfall | `lambda_2` there |
|---|---|---|---|---|---|
| 5 | 0.5430 | 1.9616000000 | 1.9565537054 | 5.0e-3 | 0.5430 |
| 6 | 0.3018 | 1.9845679012 | 1.9764416253 | 8.1e-3 | 0.3018 |
| 7 | 0.1761 | 1.9938801010 | 1.9850341986 | 8.8e-3 | 0.1761 |
| 8 | 0.1054 | 1.9975967407 | 1.9936488466 | 3.9e-3 | 0.1054 |
| 9 | 0.0640 | 1.9990633433 | 1.9962920186 | 2.8e-3 | 0.0051 |
| 10 | 0.0392 | 1.9996371200 | 1.9985104455 | 1.1e-3 | 0.0049 |
| 11 | 0.0241 | 1.9998600941 | 1.9994072562 | 4.5e-4 | 0.0044 |
| 12 | 0.0148 | 1.9999462768 | 1.9997650942 | 1.8e-4 | 0.0043 |

At `n = 5` to 8 the optimiser drives `lambda_2` exactly to `c_n`: the spectral constraint is
active, and it is the constraint that holds `phi` down rather than an artefact of the
parametrisation. At `n = 9` to 12 the best point found sits at `lambda_2` near 0.005, far inside
the constraint, and fewer starts were run there.

## 4. What this is and is not

It is not a proof. A multi-start local optimiser gives a lower bound on the true constrained
maximum, so a positive shortfall does not establish that the true maximum is below the ceiling.
It is the negative result the search was for: no point with a small spectral gap and a high `phi`
was found under the schedule the run fixes. At `n = 9` to 12 the weaker reading applies: those
four rows show that no near-decomposable matrix reaches the ceiling, not that the constrained
maximum was found.

Two of the eight dimensions, `n = 5` and `n = 6`, are proved outright by the sibling attack's
exact sum-of-squares certificates, so the evidence here is corroboration there and new at
`n = 7` to 12.

A first version of the search used the doubly stochastic polytope and was discarded: on it van der
Waerden makes `per <= gamma_n` hold only at `J_n/n`, which has no zero, so that constraint set is
empty for a reason unrelated to the spectral gap. `K_n` is the domain, and the margins are free
there.

## 5. References

- Cheon and Wanless, *An update on Minc's survey of open problems involving permanents*, Linear
  Algebra and its Applications 436 (2012) 1197-1218, Section 4.
- Sinkhorn, *A problem related to the van der Waerden permanent theorem*, Linear and Multilinear
  Algebra 16 (1984) 167-173, for `n = 2`.
- Hwang, for `n = 3`.
- Theorem R and `c_n`: `attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md`.

## 6. Ledger

Obligations: `G(n, c_n)` itself, at every `n`. This unit is evidence for it and not a proof of it.
