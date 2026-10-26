#!/usr/bin/env python3
"""The named list of positive-definite forms the screen uses, in order.

Amendment 1 of the fourth review requires the list to be declared before the run. Root-lattice
Gram matrices are chosen because their automorphism groups are large, so a usable collapse of edge
types survives the change of form, which is the point amendment 2 of the third review makes.
"""
from fractions import Fraction

D = 6


def _sym(pairs, diag=2):
    G = [[Fraction(diag if i == j else 0) for j in range(D)] for i in range(D)]
    for i, j in pairs:
        G[i][j] = G[j][i] = Fraction(-1)
    return G


def _inverse(G):
    n = len(G)
    A = [[Fraction(G[i][j]) for j in range(n)] + [Fraction(1 if i == j else 0) for j in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return [row[n:] for row in A]


def named():
    chain = [(i, i + 1) for i in range(D - 1)]
    A6 = _sym(chain)
    D6 = _sym([(0, 1), (1, 2), (2, 3), (3, 4), (3, 5)])
    E6 = _sym([(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)])
    I = [[Fraction(1 if i == j else 0) for j in range(D)] for i in range(D)]
    out = [("standard", I), ("A_6", A6), ("D_6", D6), ("E_6", E6),
           ("A_6 dual", _inverse(A6)), ("D_6 dual", _inverse(D6)), ("E_6 dual", _inverse(E6))]
    for t in (Fraction(1, 4), Fraction(1, 2), Fraction(-1, 8)):
        out.append((f"I plus {t} off the diagonal",
                    [[Fraction(1) if i == j else t for j in range(D)] for i in range(D)]))
    return out
