# numerical-optimisation-run-4: the smallest spectral gap of a near-maximiser with a zero

Step kind: numerical optimisation run (evidence, not a proof). Run 2026-09-03 under
move 10 (ladder-the-parameter, optimise-the-certificate-family-numerically).

## What was optimised

Hypothesis G(n, c) of `study/route-a-reduction-theorem.md` requires
lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2}) >= c for every A in K_n with
phi(A) >= 2 - gamma_n and a zero entry. No such A is known (the conjecture says none
exists), so the run minimises lambda_2 over the relaxation "B doubly stochastic,
b_11 = 0, per(B) <= 1.05 gamma_n" (for a doubly stochastic B, lambda_2 = 1 - sigma_2(B)):
B = Sinkhorn(exp(theta)) with theta_11 = -infinity, objective lambda_2(B) +
50 max(0, per(B)/gamma_n - 1.05), Nelder-Mead from 60/40/25/12 starts at n = 5/6/7/8
(random theta at three spreads, half of them with planted near-block structure),
seed 20260903. `run.py`; results in `gap-minima.json` with the minimising matrices.

## Result

| n | min lambda_2 found (per/gamma_n = 1.05 at the minimiser) | required c_n | ratio |
|---|---|---|---|
| 5 | 0.6971 | 0.6123 | 1.1 |
| 6 | 0.6955 | 0.3233 | 2.2 |
| 7 | 0.7263 | 0.1834 | 4.0 |
| 8 | 0.7327 | 0.1080 | 6.8 |

Every minimiser sits on the constraint per/gamma_n = 1.05: a smaller gap needs a larger
permanent, so on the set G(n, c) actually concerns (per <= gamma_n) the gap found is
larger still. No counterexample to G(n, c_n) was found; at n = 5 the margin is only
10 percent (n = 5 is proved by other means), and it widens quickly with n, in line
with c_n decreasing like sqrt(gamma_n).

## Independent check

`check.sh` runs `check.py`: feasibility of each recorded minimiser (nonnegative, row
and column sums 1 to 1e-8, b_11 = 0), the permanent by a direct sum over permutations,
lambda_2 by numpy's SVD, agreement with the recorded values to 1e-6, the constraint
per/gamma_n <= 1.05, and c_n against its definition.

## What it decides

Nothing exactly; it tests the rung of the ladder on small instances and finds it
consistent, with the margin recorded.
