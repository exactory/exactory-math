#!/usr/bin/env python3
"""Band triangulations and twisted blow-ups of cycles.

Usage: band_triangulations.py SPEC.json RESULTS_DIR

For each k in the spec, the k-vertex band complex has the triangles {c-1, c, c+1}, c in Z_k. The
program records its pair-face counts, its boundary components, its orientability and its Euler
characteristic, and tests whether its vertex-triangle incidence graph is isomorphic to the twisted
blow-up C_k^bowtie (left i adjacent to right j iff j - i in {-1, 0, 1} mod k), the graph that Lee and
Schulke and Kim, Lee and Lee write as C_k with each vertex blown up by an edge. For k = 5 it also tests
whether the incidence graph is K_{5,5} minus a Hamiltonian cycle.
"""
import itertools
import json
import os
import sys

import networkx as nx


def orientable(faces):
    pair_faces = {}
    for j, f in enumerate(faces):
        for p in itertools.combinations(f, 2):
            pair_faces.setdefault(frozenset(p), []).append(j)

    def directed(tri):
        a, b, c = tri
        return {(a, b), (b, c), (c, a)}

    orient = {0: faces[0]}
    stack = [0]
    while stack:
        j = stack.pop()
        for p in itertools.combinations(faces[j], 2):
            for k in pair_faces[frozenset(p)]:
                if k == j:
                    continue
                options = [faces[k], (faces[k][0], faces[k][2], faces[k][1])]
                good = [o for o in options if not (directed(o) & directed(orient[j]))]
                if k in orient:
                    if directed(orient[k]) & directed(orient[j]):
                        return False
                    continue
                if not good:
                    return False
                orient[k] = good[0]
                stack.append(k)
    return True


def main():
    spec = json.load(open(sys.argv[1]))
    results = sys.argv[2]
    os.makedirs(results, exist_ok=True)
    rows = []
    for k in range(spec["k_min"], spec["k_max"] + 1):
        faces = [((c - 1) % k, c, (c + 1) % k) for c in range(k)]
        pair_count = {}
        for f in faces:
            for p in itertools.combinations(f, 2):
                pair_count[frozenset(p)] = pair_count.get(frozenset(p), 0) + 1
        boundary = nx.Graph([tuple(p) for p, c in pair_count.items() if c == 1])
        H = nx.Graph()
        for c, f in enumerate(faces):
            for v in f:
                H.add_edge(("p", v), ("f", c))
        twisted = nx.Graph()
        for i in range(k):
            for d in (-1, 0, 1):
                twisted.add_edge(("L", i), ("R", (i + d) % k))
        row = {"k": k, "pairs": len(pair_count), "pairs_in_two_faces": sum(1 for c in pair_count.values() if c == 2),
               "pairs_in_one_face": sum(1 for c in pair_count.values() if c == 1),
               "boundary_components": nx.number_connected_components(boundary),
               "boundary_component_sizes": sorted(len(c) for c in nx.connected_components(boundary)),
               "euler_characteristic": k - len(pair_count) + k, "orientable": orientable(faces),
               "incidence_isomorphic_to_twisted_blowup": nx.is_isomorphic(H, twisted),
               "incidence_vertices": H.number_of_nodes(), "incidence_edges": H.number_of_edges(),
               "incidence_has_4_cycles": any(len(set(H[u]) & set(H[w])) >= 2 for u in H for w in H if u < w and u[0] == w[0])}
        if k == 5:
            complement = nx.Graph()
            for i in range(5):
                for c in range(5):
                    if not H.has_edge(("p", i), ("f", c)):
                        complement.add_edge(("p", i), ("f", c))
            row["k5_complement_in_K55_is_10_cycle"] = (complement.number_of_nodes() == 10 and
                                                        all(d == 2 for _, d in complement.degree()) and
                                                        nx.is_connected(complement))
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    json.dump(rows, open(os.path.join(results, "bands.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
