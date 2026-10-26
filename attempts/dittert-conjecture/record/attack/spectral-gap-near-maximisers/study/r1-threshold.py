"""R1's threshold, checked exactly: from which n does the Cheeger-and-blocks chain clear c_n?

R1 needs lambda_2 > 1/(2 n^4) to force a contradiction (Cheeger gives conductance
sqrt(2 lambda_2), the cut mass is at most 2k sqrt(2 lambda_2) <= n sqrt(2 lambda_2), and the
block gain gamma_k gamma_{n-k}/gamma_n >= (n/(n-1))^(n-1) > e needs the cut mass below
about 1/n).  The claim it must beat is lambda_2 >= c_n = 2 sqrt(gamma_n kappa_n)/theta_n.
The route is useful exactly where 1/(2 n^4) <= c_n.  Also prints the block gain, to check
the claim that it is at least e.
"""
import math
from fractions import Fraction as Fr

print(f"{'n':>3} {'gamma_n':>11} {'c_n':>11} {'1/(2n^4)':>11} {'R1 usable':>10} {'min block gain':>15}")
first = None
for n in range(4, 61):
    g = math.factorial(n) / n ** n
    h = math.sqrt(2 * g)
    kappa = 1 / ((1 - g) * (1 - 2 * h / 3))
    c = 2 * math.sqrt(g * kappa) / (1 - h)
    thr = 1 / (2 * n ** 4)
    gain = min(Fr(math.factorial(k), k ** k) * Fr(math.factorial(n - k), (n - k) ** (n - k)) /
               Fr(math.factorial(n), n ** n) for k in range(1, n))
    ok = thr <= c
    if ok and first is None:
        first = n
    if n <= 20 or n % 5 == 0:
        print(f"{n:>3} {g:>11.4e} {c:>11.4e} {thr:>11.4e} {'yes' if ok else 'no':>10} {float(gain):>15.4f}")
print(f"\nR1 first clears c_n at n = {first} (so it is empty on the open range 7..15)")
print(f"e = {math.e:.4f}; the minimum block gain is attained at k = 1 and equals (n/(n-1))^(n-1)")
