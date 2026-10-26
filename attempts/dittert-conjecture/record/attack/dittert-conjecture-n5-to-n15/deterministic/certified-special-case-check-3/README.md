# certified-special-case-check-3: where the published analytic route stops, exactly

Step kind: certified special-case check (two independent exact implementations agree).
Run 2026-09-03 under move 9 (ladder-the-parameter).

## Statement checked

For 4 <= n <= 17, the sign of

    K_n = m_n - gamma_n - n^3 m_n^2 / (4 (1 - gamma_n)),

gamma_n = n!/n^n, m_n = (n-2)! ((n-2)/(n-1)^2)^{n-2}. K_n > 0 is the final inequality of
the n = 16 proof of arXiv:2607.19439 (its (4.3)), and every other step of that proof
holds for all n > 3 (the Knopp-Sinkhorn value needs n > 3; the dilation needs
n gamma_n/(1 - gamma_n) < 1, recorded as `t_below_one`, true for all n >= 4). So K_n > 0
proves Dittert's conjecture at n by the published argument, and K_n <= 0 means that
argument does not reach n.

## Result (`kafidov-threshold.json`)

K_n > 0 exactly for n = 16, 17 and K_n <= 0 exactly for 4 <= n <= 15. The ratio
r_n = (m_n - gamma_n)/(n^3 m_n^2/(4(1-gamma_n))): 0.029 (4), 0.023 (5), 0.022 (6), 0.025 (7),
0.031 (8), 0.044 (9), 0.065 (10), 0.104 (11), 0.172 (12), 0.298 (13), 0.535 (14),
0.98712 (15), 1.869 (16), 3.618 (17).

## Implementations

- `run.py`: Python `fractions.Fraction`, exact; writes the JSON with K_n as an exact
  rational string.
- `check.sh` -> `check.py`: python-flint `fmpq`, exact, independent of the fractions
  module; compares the exact K_n string and its sign with the record, and confirms the
  sign in 80-digit mpmath arithmetic with a margin check |K_n| > 1e-60.

Trusted base: Python integers, python-flint, mpmath.

## What it decides

The exact stopping point of the analytic route in print: n = 15 misses by a factor
0.98712 of the required value (1.3 percent), and each dimension down needs roughly a
factor 1.9 more. It is the "current value" row of the ladder of move 8.
