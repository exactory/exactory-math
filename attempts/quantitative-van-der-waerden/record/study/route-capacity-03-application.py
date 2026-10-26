"""Does Q(c) with c = c(n) close the Dittert application?  Re-uses application.py's fixed point
with c = 1/(2n) (what route-capacity.md proves), c = 1/n and c = 1/4 for comparison."""
import math
import sys

sys.argv = [sys.argv[0]]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import application  # noqa: E402  (prints its own table; suppressed)

for label, cfun in [("c = 1/(2n)", lambda n: 1 / (2 * n)), ("c = 1/n", lambda n: 1 / n),
                    ("c = 1/4", lambda n: 0.25)]:
    print(f"\n{label}")
    print(f"{'n':>3} {'c':>9} {'K upper bound':>15} {'lambda_2 >=':>12} {'log(m_n/gamma_n)':>17} "
          f"{'closes':>8} {'margin':>8} {'|alpha+beta| <=':>16}")
    for n in range(5, 21):
        c = cfun(n)
        g, m, th, kap = application.constants(n)
        need = math.log(m / g)
        Kb, lam = application.fixed_point(n, c)
        if Kb is None:
            print(f"{n:>3} {c:>9.5f} {'no fixed point':>15} {'-':>12} {need:>17.6e} {'no':>8}")
            continue
        ab = math.sqrt(2) * math.sqrt(2 * g * kap) / (th * lam)
        ok = Kb < need and ab < 1
        print(f"{n:>3} {c:>9.5f} {Kb:>15.6e} {lam:>12.6f} {need:>17.6e} {'yes' if ok else 'no':>8} "
              f"{need / Kb:>8.2f}x {ab:>16.4f}")
