#!/usr/bin/env python3
"""Independent Littlewood-Richardson counter by the classical lattice-word rule.

c^{lam}_{mu,nu} = number of semistandard skew tableaux of shape lam/mu with content
nu whose reverse reading word (rows top to bottom, each row right to left) is a
lattice word.  Row r is encoded by its multiplicity vector m_r = (m_{r,1..k}),
sum m_r = lam_r - mu_r.  With S_r(i) = mu_r + m_{r,1} + ... + m_{r,i} (last column
of row r holding an entry <= i) and C_r(i) = m_{1,i} + ... + m_{r,i}:
  column strictness:  S_r(i) <= S_{r-1}(i-1) for all i >= 1 (S_{r-1}(0) = mu_{r-1});
  lattice word:       C_r(i+1) <= C_{r-1}(i) for all r, i >= 1.
This file shares no code with hivepoly.py (no hive, no polytope, no Normaliz).
"""
from __future__ import annotations

import sys
from functools import lru_cache
from typing import Sequence, Tuple


def count_lr_tableaux(lam: Sequence[int], mu: Sequence[int], nu: Sequence[int]) -> int:
    lam = tuple(x for x in lam if x)
    mu = tuple(x for x in mu if x)
    nu = tuple(x for x in nu if x)
    if sum(lam) != sum(mu) + sum(nu):
        return 0
    n = len(lam)
    k = len(nu)
    mu_p = tuple(mu) + (0,) * (n - len(mu))
    if len(mu) > n or any(mu_p[r] > lam[r] for r in range(n)):
        return 0
    if k > n:
        return 0
    rows = [lam[r] - mu_p[r] for r in range(n)]

    def compositions(total: int, parts: int, caps: Tuple[int, ...]):
        """All (m_1..m_parts) with sum = total and m_i <= caps[i]."""
        if parts == 0:
            if total == 0:
                yield ()
            return
        for first in range(min(total, caps[0]) + 1):
            for rest in compositions(total - first, parts - 1, caps[1:]):
                yield (first,) + rest

    sys.setrecursionlimit(10000)

    @lru_cache(maxsize=None)
    def rec(r: int, prev_m: Tuple[int, ...], content: Tuple[int, ...]) -> int:
        # rows 0..r-1 placed; prev_m is row r-1's multiplicities; content = C_{r-1}
        if r == n:
            return 1 if content == tuple(nu) else 0
        remaining = tuple(nu[i] - content[i] for i in range(k))
        total = rows[r]
        count = 0
        # S_{r-1}(i-1): last column with entry <= i-1 in row r-1
        if r == 0:
            prev_S = None
        else:
            prev_S = [mu_p[r - 1]]
            for i in range(k):
                prev_S.append(prev_S[-1] + prev_m[i])
        for m in compositions(total, k, remaining):
            # lattice: C_r(i+1) <= C_{r-1}(i)
            ok = True
            for i in range(k - 1):
                if content[i + 1] + m[i + 1] > content[i]:
                    ok = False
                    break
            if not ok:
                continue
            if r > 0:
                S = mu_p[r]
                for i in range(k):
                    S += m[i]
                    if m[i] and S > prev_S[i]:   # S_r(i) <= S_{r-1}(i-1)
                        ok = False
                        break
                if not ok:
                    continue
            else:
                if any(m[i] for i in range(1, k)):
                    continue
            new_content = tuple(content[i] + m[i] for i in range(k))
            count += rec(r + 1, m, new_content)
        return count

    return rec(0, (0,) * k, (0,) * k)


if __name__ == "__main__":
    import json

    lam, mu, nu = (json.loads(a) for a in sys.argv[1:4])
    t = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    print(count_lr_tableaux([t * x for x in lam], [t * x for x in mu], [t * x for x in nu]))
