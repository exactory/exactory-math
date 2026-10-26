#!/usr/bin/env python3
"""Essential Horn inequalities and the King-Tollu-Toumazet factorisation.

KTT factorisation theorem (King, Tollu, Toumazet, J. Combin. Theory Ser. A 116 (2009)
314-333; stated as Theorem 1.3 in Cho, Jung, Moon, DMTCS proc. AJ (2008) 483-494):
let lam, mu, nu be partitions of length at most n with c^{lam}_{mu nu} > 0 (here lam is
the large partition, |lam| = |mu| + |nu|).  If some (I, J, K) in R^n_r with r < n satisfies
    sum_{k in K} lam_k = sum_{i in I} mu_i + sum_{j in J} nu_j,
then c^{lam}_{mu nu} = c^{lam_K}_{mu_I nu_J} * c^{lam_{K^c}}_{mu_{I^c} nu_{J^c}} and the
stretched polynomials factorise the same way, P = P_1 P_2 (the equality is homogeneous,
so it survives stretching).  R^n_r is the set of triples of r-subsets of {1..n} with
c^{pi(K)}_{pi(I) pi(J)} = 1, where pi(I) = (i_r - r, ..., i_1 - 1) for I = {i_1 < ... < i_r}.

A triple with no such saturated essential inequality is primitive (KTT 2006, Def. 4.1).
"""
from __future__ import annotations

import itertools
import json
import os
from functools import lru_cache
from typing import List, Sequence, Tuple

import numpy as np


def _pi(I: Sequence[int]) -> Tuple[int, ...]:
    r = len(I)
    parts = tuple(I[r - 1 - k] - (r - k) for k in range(r))  # (i_r - r, ..., i_1 - 1)
    return tuple(p for p in parts if p > 0)


@lru_cache(maxsize=None)
def essential_triples(n: int) -> List[Tuple[Tuple[int, ...], Tuple[int, ...], Tuple[int, ...]]]:
    """R^n_r for all 1 <= r < n, as (I, J, K) with 1-based indices."""
    import lrcalc  # type: ignore

    cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"horn-essential-{n}.json")
    if os.path.exists(cache):
        return [tuple(tuple(x) for x in t) for t in json.load(open(cache))]
    out = []
    for r in range(1, n):
        subsets = list(itertools.combinations(range(1, n + 1), r))
        for I in subsets:
            a = _pi(I)
            for J in subsets:
                b = _pi(J)
                sab = sum(a) + sum(b)
                for K in subsets:
                    g = _pi(K)
                    if sum(g) != sab:
                        continue
                    if int(lrcalc.lrcoef(list(g), list(a), list(b))) == 1:
                        out.append((I, J, K))
    json.dump(out, open(cache, "w"))
    return out


class HornChecker:
    """Vectorised saturation test for a fixed n."""

    def __init__(self, n: int):
        self.n = n
        trips = essential_triples(n)
        self.trips = trips

        def mask(S):
            m = 0
            for s in S:
                m |= 1 << (s - 1)
            return m

        self.I = np.array([mask(t[0]) for t in trips], dtype=np.int64)
        self.J = np.array([mask(t[1]) for t in trips], dtype=np.int64)
        self.K = np.array([mask(t[2]) for t in trips], dtype=np.int64)
        # subset-sum table builder
        self.bits = np.array([[(m >> b) & 1 for b in range(n)] for m in range(1 << n)], dtype=np.int64)

    def subset_sums(self, p: Sequence[int]) -> np.ndarray:
        v = np.array(list(p) + [0] * (self.n - len(p)), dtype=np.int64)
        return self.bits @ v

    def saturated(self, lam, mu, nu) -> List[int]:
        """Indices of essential triples (I, J, K) with lam_K = mu_I + nu_J."""
        sl, sm, sn = self.subset_sums(lam), self.subset_sums(mu), self.subset_sums(nu)
        hit = sl[self.K] == sm[self.I] + sn[self.J]
        return list(np.nonzero(hit)[0])

    def is_primitive(self, lam, mu, nu) -> bool:
        return not self.saturated(lam, mu, nu)

    def factors(self, lam, mu, nu, idx: int):
        """The two factor triples for essential triple number idx."""
        I, J, K = self.trips[idx]
        n = self.n
        lam_p = list(lam) + [0] * (n - len(lam))
        mu_p = list(mu) + [0] * (n - len(mu))
        nu_p = list(nu) + [0] * (n - len(nu))
        Ic = [i for i in range(1, n + 1) if i not in I]
        Jc = [j for j in range(1, n + 1) if j not in J]
        Kc = [k for k in range(1, n + 1) if k not in K]
        sub = lambda p, S: tuple(x for x in (p[s - 1] for s in S) if x > 0)
        return (sub(lam_p, K), sub(mu_p, I), sub(nu_p, J)), (sub(lam_p, Kc), sub(mu_p, Ic), sub(nu_p, Jc))


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    trips = essential_triples(n)
    from collections import Counter

    print(n, len(trips), dict(sorted(Counter(len(t[0]) for t in trips).items())))
