# numerical-optimisation-run-1

**What it decides.** Whether any matrix with a small spectral gap reaches the Dittert ceiling.
For each `n` in 5 to 12 it maximises `phi(A) = prod r_i + prod c_j - per(A)` over `A in K_n`
(non-negative, total sum `n`) with a zero entry and `lambda_2(A) <= c_n`, and asserts the maximum
found is strictly below `2 - gamma_n`. That inequality is G(n, c_n) at that `n`.

**Why the question is this one.** G(n, c_n) quantifies over `A in K_n` with a zero and
`phi(A) >= 2 - gamma_n`, which by Dittert's conjecture is empty, so the statement cannot be
tested by sampling its hypothesis set. The contrapositive can be: maximise `phi` on the region
where `lambda_2` is small, and see whether it reaches the ceiling.

**Method.** `phi` uses a vectorised Ryser permanent over all `2^n` column subsets.
`lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2})` as in Theorem R. `A` is parametrised as
`exp(theta)` with the `(0,0)` entry fixed at zero and the matrix rescaled to total sum `n`, so
every iterate is in `K_n` with a zero by construction. The spectral constraint enters as a
penalty of 50 on the excess. L-BFGS-B, multi-start, from random starts at four spreads and from
near-decomposable starts, seeded with 20260904.

**Result.** Every `n` passed. Maximum `phi` against the ceiling `2 - gamma_n`:

| n | c_n | ceiling | max phi | shortfall |
|---|---|---|---|---|
| 5 | 0.5430 | 1.9616000000 | 1.9565537054 | 5.0e-3 |
| 6 | 0.3018 | 1.9845679012 | 1.9764416253 | 8.1e-3 |
| 7 | 0.1761 | 1.9938801010 | 1.9850341986 | 8.8e-3 |
| 8 | 0.1054 | 1.9975967407 | 1.9936488466 | 3.9e-3 |
| 9 | 0.0640 | 1.9990633433 | 1.9962920186 | 2.8e-3 |
| 10 | 0.0392 | 1.9996371200 | 1.9985104455 | 1.1e-3 |
| 11 | 0.0241 | 1.9998600941 | 1.9994072562 | 4.5e-4 |
| 12 | 0.0148 | 1.9999462768 | 1.9997650942 | 1.8e-4 |

At `n = 5` to `8` the optimiser drives `lambda_2` exactly to `c_n`, so the spectral constraint is
active and is what holds `phi` down. At `n = 9` to `12` the best point found sits at `lambda_2`
near 0.005, far inside the constraint, and fewer starts were run, so those four rows show that no
near-decomposable matrix reaches the ceiling rather than that the constrained maximum was found.

**What this is not.** A multi-start local optimiser gives a lower bound on the true maximum, so a
positive shortfall is evidence and not a certificate. The unit built on this step carries the
form `computational-evidence` for that reason.
