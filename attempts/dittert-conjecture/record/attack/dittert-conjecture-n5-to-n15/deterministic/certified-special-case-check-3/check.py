"""Second implementation for certified special-case check 3: recompute the sign of
K_n = m_n - gamma_n - n^3 m_n^2/(4(1 - gamma_n)) with python-flint's exact rationals
(fmpq), independently of the fractions module, and compare with kafidov-threshold.json;
also confirm the sign by 80-digit mpmath arithmetic with an explicit margin check
(|K_n| must exceed 1e-60 so that the floating sign is certain).
"""
import json
import sys
from math import factorial

import flint
import mpmath as mp

rec = json.load(open("kafidov-threshold.json"))
mp.mp.dps = 80
ok = True
for n in range(4, 18):
    g = flint.fmpq(factorial(n), n ** n)
    m = flint.fmpq(factorial(n - 2)) * flint.fmpq(n - 2, (n - 1) ** 2) ** (n - 2)
    K = m - g - flint.fmpq(n ** 3) * m * m / (4 * (1 - g))
    sign = "positive" if K > 0 else "not positive"
    gm = mp.mpf(factorial(n)) / mp.mpf(n) ** n
    mm = mp.mpf(factorial(n - 2)) * (mp.mpf(n - 2) / mp.mpf((n - 1) ** 2)) ** (n - 2)
    Km = mm - gm - mp.mpf(n) ** 3 * mm ** 2 / (4 * (1 - gm))
    sign_mp = "positive" if Km > 0 else "not positive"
    agree = sign == rec[str(n)]["K_n_sign"] == sign_mp and abs(Km) > mp.mpf("1e-60") and str(K) == rec[str(n)]["K_n"]
    print(f"n={n:2d}: flint {sign}, mpmath {sign_mp} (|K| = {mp.nstr(abs(Km), 5)}), recorded {rec[str(n)]['K_n_sign']}: {'agree' if agree else 'DISAGREE'}")
    ok &= agree
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
