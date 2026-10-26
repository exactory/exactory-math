# numerical-optimisation-run-1: boundary gaps of the Dittert functional

Step kind: numerical optimisation run (evidence, not a proof). Run 2026-09-03 under
move 2 (predict-the-value-and-test-it-numerically) of the walk.

## What was run

`run.py 5 6`: for n = 5 and n = 6, maximise phi(A) = prod r_i + prod c_j - per(A) over
the face F_n = {A in K_n : a_11 = 0} by L-BFGS-B on a softmax parametrisation of the
free entries (numerical gradients), from 201 (n = 5) and 121 (n = 6) starts: the
Knopp-Sinkhorn extremal T_n and random perturbations of it at four scales
(0.02, 0.1, 0.3, 1.0), seed 20260903. Ryser's formula for the permanent. n = 7 was
started and abandoned (each start took minutes with numerical gradients); it is
not covered.

## Result (optima.json)

| n | max phi on F_n (numerical) | 2 - gamma_n | g_n = 2 - gamma_n - max | m_n - gamma_n | g_n / (m_n - gamma_n) |
|---|---|---|---|---|---|
| 5 | 1.960449218750 | 1.961600000000 | 1.151e-3 | 1.151e-3 | 1.0000 |
| 6 | 1.984271360000 | 1.984567901235 | 2.965e-4 | 2.965e-4 | 1.0000 |

At both n the optimiser found is the Knopp-Sinkhorn extremal T_n itself (R = C = 1,
per = m_n to 8 digits): the maximum of phi on the face is 2 - m_n, and lowering the
row or column products to reduce the permanent never pays. So the boundary gap of
the conjecture at n = 5 and 6 equals the full Knopp-Sinkhorn gap m_n - gamma_n
(5.3 percent of gamma_5, 1.9 percent of gamma_6), and every matrix on the face has
phi < 2 - gamma_n by that margin, numerically.

Prediction tested: that the trade-off between the products and the permanent could
push a face point above 2 - m_n. The numerics say it cannot at n = 5, 6.

## Independent check

`check.sh` runs `check.py`: it rationalises the recorded optimiser (denominators up to
10^12), renormalises it exactly onto the face, and re-evaluates R, C, per and phi in
exact rational arithmetic with a direct permutation sum (no code shared with
run.py); it requires agreement with the recorded value to 1e-9 and the same sign of
the gap. Trusted base: Python's fractions module.

## What it decides

Nothing by itself. It bounds the slack available to route A at n = 5, 6 and shows
the extremal structure on the face is T_n. The maximum found is a lower bound on
the true face maximum; the true value could be larger only at a point every start
missed.
