#!/usr/bin/env python3
"""Canonical form of a transverse cone type under the isometries of the ambient lattice.

A McMullen local formula assigns to a face a weight depending only on its transverse cone. The
Berline-Vergne weight is built from the lattice together with the standard inner product, so it
is invariant under the isometry group of (Z^d, standard inner product), the signed permutations
of the coordinates: if g is such an isometry then the weight of g.C equals the weight of C. Two
faces whose normal sets differ by a signed permutation therefore carry the same weight, whatever
valid formula is used, and may be identified.

A type here is the set of primitive outward normals of the facets through a face, a set of
vectors with entries in {0, +1, -1}. `canonical(type)` returns the lexicographically least image
of the type under the 2^d d! signed permutations, computed by a backtracking search over the
image of one coordinate at a time with pruning against the best image found so far, so the whole
group is never enumerated. `same_class(t1, t2)` is then equality of canonical forms, and
`witness(t1, t2)` returns an explicit isometry when there is one, so that a merge can be checked
rather than assumed.
"""
from __future__ import annotations

from itertools import permutations
from typing import Dict, List, Optional, Sequence, Tuple

Vec = Tuple[int, ...]
Type = Tuple[Vec, ...]


def _image(t: Sequence[Vec], order: Sequence[int], signs: Sequence[int]) -> Type:
    """The type transformed by the isometry sending coordinate order[j] to position j."""
    return tuple(sorted(tuple(signs[j] * v[order[j]] for j in range(len(order))) for v in t))


def canonical(t: Sequence[Vec]) -> Type:
    """Lexicographically least image of t under the signed permutations of the coordinates."""
    t = tuple(tuple(v) for v in t)
    d = len(t[0])
    best: Optional[Type] = None
    order: List[int] = []
    signs: List[int] = []
    used = [False] * d

    def rec():
        nonlocal best
        k = len(order)
        if k == d:
            img = _image(t, order, signs)
            if best is None or img < best:
                best = img
            return
        for i in range(d):
            if used[i]:
                continue
            for s in (1, -1):
                order.append(i)
                signs.append(s)
                used[i] = True
                # prune: the partial image, sorted, must not exceed the best's prefix
                part = tuple(sorted(tuple(signs[j] * v[order[j]] for j in range(k + 1)) for v in t))
                if best is None or part <= tuple(p[: k + 1] for p in best):
                    rec()
                used[i] = False
                signs.pop()
                order.pop()

    rec()
    assert best is not None
    return best


def witness(t1: Sequence[Vec], t2: Sequence[Vec]) -> Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]]:
    """An explicit isometry (order, signs) carrying t1 to t2, or None."""
    t1 = tuple(tuple(v) for v in t1)
    t2 = tuple(sorted(tuple(v) for v in t2))
    d = len(t1[0])
    if len(t1) != len(t2):
        return None
    for order in permutations(range(d)):
        for mask in range(1 << d):
            signs = tuple(1 if (mask >> j) & 1 == 0 else -1 for j in range(d))
            if _image(t1, order, signs) == t2:
                return order, signs
    return None


def classes(types: Sequence[Sequence[Vec]]) -> Tuple[List[int], Dict[Type, int]]:
    """Assign each type its isometry class index; return the assignment and the class table."""
    table: Dict[Type, int] = {}
    out: List[int] = []
    for t in types:
        c = canonical(t)
        if c not in table:
            table[c] = len(table)
        out.append(table[c])
    return out, table


def _selftest() -> None:
    a = [(1, -1, 0, 0, 0, 0), (0, 1, -1, 0, 0, 0)]
    b = [(0, 0, 0, 1, -1, 0), (0, 0, 0, 0, 1, -1)]           # a shifted to other coordinates
    assert canonical(a) == canonical(b), "a coordinate permutation must not change the class"
    c = [(1, 1, 0, 0, 0, 0), (0, 1, -1, 0, 0, 0)]            # different Gram matrix
    assert canonical(a) != canonical(c), "different inner products must not be identified"
    w = witness(a, b)
    assert w is not None and _image(a, w[0], w[1]) == tuple(sorted(b))
    assert witness(a, c) is None
    print("isotypes selftest: PASS")


if __name__ == "__main__":
    _selftest()
