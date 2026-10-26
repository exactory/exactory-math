"""The check: the constrained maximum of phi stays strictly below the Dittert ceiling.

Runs `search.py` on n = 5 to 12 with its fixed seed and asserts that at every n the best
`phi(A)` found, over `A in K_n` with a zero entry and `lambda_2(A) <= c_n`, is strictly below
`2 - gamma_n`.  That inequality is G(n, c_n) at that `n`: a matrix with a spectral gap below
`c_n` does not reach the Dittert ceiling.

This is computational evidence, not a certificate.  A maximum over a non-convex domain found by
a multi-start local optimiser is a lower bound on the true maximum, so a positive shortfall here
does not prove the true maximum is below the ceiling.  What it does show is the negative result
the search was for: no point with a small spectral gap and a high `phi` was found, over the
multi-start schedule `search.py` fixes.

The run is reproducible: `search.py` seeds its generator with 20260904 and L-BFGS-B is
deterministic, so the numbers repeat exactly.
"""
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NS = [5, 6, 7, 8, 9, 10, 11, 12]

out = subprocess.run(
    [sys.executable, str(HERE / "search.py"), *map(str, NS)],
    cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True,
).stdout
print(out)

rows = {}
for line in out.splitlines():
    parts = line.split()
    if len(parts) == 7 and parts[0].isdigit():
        n, c_n, ceiling, best, shortfall, lam, _starts = parts
        rows[int(n)] = (float(ceiling), float(best), float(shortfall), float(lam), float(c_n))

failures = []
for n in NS:
    if n not in rows:
        failures.append("n = %d: no row in the search output" % n)
        continue
    ceiling, best, shortfall, lam, c_n = rows[n]
    if abs(ceiling - (2 - math.factorial(n) / n ** n)) > 1e-9:
        failures.append("n = %d: ceiling %.12f is not 2 - gamma_n" % (n, ceiling))
    if lam > c_n + 1e-9:
        failures.append("n = %d: the reported point violates lambda_2 <= c_n" % n)
    if shortfall <= 0:
        failures.append("n = %d: shortfall %.3e is not positive; G(n, c_n) is refuted here"
                        % (n, shortfall))

if failures:
    print("FAIL")
    for f in failures:
        print("  " + f)
    raise SystemExit(1)
print("PASS: the constrained maximum of phi stayed strictly below 2 - gamma_n at n = %s"
      % ", ".join(map(str, NS)))
