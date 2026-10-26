"""Check two remarks of the paper: the uniform edge average and the Perron-product average.

For a triangle-free graph and an edge uv, D_uv = m + d(u) d(v) - 2 (A^3)_uv is the cost of the target
K_{N(v),N(u)}. The script
  1. finds the triangle-free graphs on at most 7 vertices whose uniform edge average of D_uv exceeds
     3 xi = 3 (m - lambda^2), and prints the smallest order and the largest excess;
  2. evaluates the Perron-product average (2/lambda) sum_{uv} x_u x_v D_uv on the double star S(8,7)
     (centres of degrees 9 and 8) and compares it with 3 xi = 24 - 6 sqrt 2;
  3. evaluates the uniform average on the 10-vertex graph with graph6 string I?AFvp{^? .
Eigenvalues are computed with mpmath at 50 digits.
"""
import itertools

import mpmath

mpmath.mp.dps = 50


def adjacency(n, edges):
    a = [[0] * n for _ in range(n)]
    for u, v in edges:
        a[u][v] = a[v][u] = 1
    return a


def triangle_free(a, n):
    return not any(a[i][j] and a[j][k] and a[i][k]
                   for i, j, k in itertools.combinations(range(n), 3))


def top_pair(a, n):
    evals, evecs = mpmath.eigsy(mpmath.matrix(a))
    i = max(range(n), key=lambda k: evals[k])
    x = [evecs[r, i] for r in range(n)]
    s = mpmath.sqrt(sum(t * t for t in x))
    sign = 1 if sum(x) >= 0 else -1
    return evals[i], [sign * t / s for t in x]


def edge_costs(a, n, edges):
    deg = [sum(row) for row in a]
    m = len(edges)
    a3 = [[sum(a[u][p] * a[p][q] * a[q][v] for p in range(n) for q in range(n)) for v in range(n)]
          for u in range(n)]
    return {(u, v): m + deg[u] * deg[v] - 2 * a3[u][v] for u, v in edges}


def uniform_excess(n, edges):
    a = adjacency(n, edges)
    lam, _ = top_pair(a, n)
    costs = edge_costs(a, n, edges)
    m = len(edges)
    return mpmath.mpf(sum(costs.values())) / m - 3 * (m - lam ** 2)


def from_graph6(s):
    n = ord(s[0]) - 63
    bits = "".join(f"{ord(c) - 63:06b}" for c in s[1:])
    edges, k = [], 0
    for v in range(1, n):
        for u in range(v):
            if bits[k] == "1":
                edges.append((u, v))
            k += 1
    return n, edges


def main():
    for n in range(2, 8):
        pairs = list(itertools.combinations(range(n), 2))
        worst, count = None, 0
        for mask in range(1, 1 << len(pairs)):
            edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            a = adjacency(n, edges)
            if not triangle_free(a, n):
                continue
            exc = uniform_excess(n, edges)
            if exc > mpmath.mpf("1e-30"):
                count += 1
                if worst is None or exc > worst[0]:
                    worst = (exc, edges)
        print(f"n={n}: graphs with uniform average > 3 xi (labelled): {count}"
              + (f"; largest excess {mpmath.nstr(worst[0], 8)} on edges {worst[1]}" if worst else ""))

    # Double star S(8,7): vertex 0 with leaves 2..9, vertex 1 with leaves 10..16, edge 01.
    n = 17
    edges = [(0, 1)] + [(0, k) for k in range(2, 10)] + [(1, k) for k in range(10, 17)]
    a = adjacency(n, edges)
    lam, x = top_pair(a, n)
    costs = edge_costs(a, n, edges)
    perron = 2 / lam * sum(x[u] * x[v] * c for (u, v), c in costs.items())
    m = len(edges)
    print("S(8,7): lambda^2 =", mpmath.nstr(lam ** 2, 12), "(8 + 2 sqrt 2 =",
          mpmath.nstr(8 + 2 * mpmath.sqrt(2), 12), ")")
    print("S(8,7): Perron-product average =", mpmath.nstr(perron, 12),
          " 3 xi =", mpmath.nstr(3 * (m - lam ** 2), 12),
          " uniform average =", mpmath.nstr(mpmath.mpf(sum(costs.values())) / m, 12),
          " min D_uv =", min(costs.values()))
    weights = sum((x[u] ** 2 / sum(a[u]) + x[v] ** 2 / sum(a[v])) * c for (u, v), c in costs.items())
    print("S(8,7): weighted average with x_u^2/d(u) + x_v^2/d(v) =", mpmath.nstr(weights, 12))

    n, edges = from_graph6("I?AFvp{^?")
    print("I?AFvp{^?: n =", n, "m =", len(edges), "uniform excess =",
          mpmath.nstr(uniform_excess(n, edges), 10))


if __name__ == "__main__":
    main()
