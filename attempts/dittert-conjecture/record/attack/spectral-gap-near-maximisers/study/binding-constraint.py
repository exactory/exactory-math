"""Which constraint in Theorem R actually fixes the constant c_n, and what would each
candidate route need?

Theorem R needs the spectral gap to clear two separate bars:

  (N)  the nonnegativity condition of Lemma 2, |alpha_i + beta_j| <= 1, which the proof
       discharges by  c >= c_N := 2 sqrt(gamma_n kappa_n) / theta_n;
  (C)  the final contradiction  m_n - gamma_n <= delta (2 m_n kappa_n/(theta_n c) - 1) < 0,
       which needs only  c > c_C := 2 m_n kappa_n / theta_n.

If (N) is the binding one, then a technical improvement to Lemma 2 -- a competitor whose
correction stays nonnegative under a weaker hypothesis -- lowers the bar the spectral routes
have to clear, without touching the mathematics of the contradiction.

The table also prints what the Cheeger-and-blocks route (R1) delivers:
  crude   lambda_2 >= 1/(2 n^4)     (block capacity bounded by (1 - eps)^n)
  refined lambda_2 >= 1/(2 C^2 n^2) (block capacity bounded by exp(-C eps)), C = 2 and 4,
and marks the dimensions each version would settle against each bar.
"""
import math

print(f"{'n':>3} {'gamma_n':>10} {'c_N (N)':>10} {'c_C (contra)':>12} {'ratio':>7} "
      f"{'R1 crude':>10} {'R1 C=2':>10} {'R1 C=4':>10} | vs c_N | vs c_C")
for n in range(7, 21):
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    h = math.sqrt(2 * g)
    th = 1 - h
    kap = 1 / ((1 - g) * (1 - 2 * h / 3))
    cN = 2 * math.sqrt(g * kap) / th
    cC = 2 * m * kap / th
    r1a = 1 / (2 * n ** 4)
    r1b = 1 / (2 * 4 * n ** 2)
    r1c = 1 / (2 * 16 * n ** 2)
    def mark(x):
        return ("N" if x >= cN else "-") + ("C" if x >= cC else "-")
    print(f"{n:>3} {g:>10.3e} {cN:>10.3e} {cC:>12.3e} {cN/cC:>7.1f} "
          f"{r1a:>10.3e} {r1b:>10.3e} {r1c:>10.3e} |  {mark(r1a)} {mark(r1b)} {mark(r1c)}")
print("\nmark: first letter = clears the (N) bar, second = clears the contradiction bar.")
print("A route only has to clear the bar that is actually binding; today that is (N).")
