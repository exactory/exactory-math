#!/usr/bin/env python3
"""Which small triangulated 2-spheres satisfy the combinatorial hypotheses that the reported
Sidorenko counterexample uses for its 13-vertex sphere?

Usage: small_spheres.py SPEC.json RESULTS_DIR

The spec names the plantri binary, the vertex range and Table 1 of the counterexample. For every
triangulation T of the 2-sphere with n vertices (plantri, all isomorphism classes), the program
computes
  (a) whether color refinement on the vertex-face incidence graph H(T), started from the two part
      colours, ends with all vertices distinct (the hypothesis of the pinning lemma, Lemma 3.4);
  (b) whether three Hamiltonian cycles of T cover every edge of T (the hypothesis behind the bit
      labels: each cycle splits the faces into two triangulated disks with Hamiltonian boundary,
      and a pair's two faces differ at a bit position exactly when the pair lies on that cycle;
      three cycles covering 3n - 6 edges with 3n edge slots force some pair onto two cycles).
A vertex of degree at least 7 rules out (b), because each Hamiltonian cycle uses two edges at
every vertex. The program reports counts per n, every triangulation with n <= 12 that satisfies
both (a) and (b), and whether the 13-vertex sphere of Table 1 satisfies both.
"""
import json
import os
import subprocess
import sys

import networkx as nx


def parse_plantri_ascii(line):
    n_text, body = line.split(" ", 1)
    n = int(n_text)
    rotations = [[ord(c) - ord("a") for c in group] for group in body.strip().split(",")]
    assert len(rotations) == n
    faces = set()
    for v, rot in enumerate(rotations):
        d = len(rot)
        for i in range(d):
            faces.add(tuple(sorted((v, rot[i], rot[(i + 1) % d]))))
    return n, rotations, sorted(faces)


def colour_refinement_discrete(n, faces):
    # vertices 0..n-1 are points, n..n+F-1 are faces
    nbrs = [[] for _ in range(n + len(faces))]
    for j, f in enumerate(faces):
        for v in f:
            nbrs[v].append(n + j)
            nbrs[n + j].append(v)
    colour = [0] * n + [1] * len(faces)
    while True:
        signature = [(colour[u], tuple(sorted(colour[w] for w in nbrs[u]))) for u in range(len(nbrs))]
        palette = {s: i for i, s in enumerate(sorted(set(signature)))}
        new = [palette[s] for s in signature]
        if len(set(new)) == len(set(colour)):
            return len(set(new)) == len(nbrs)
        colour = new


def hamiltonian_cycles(n, adj, edge_index):
    """All Hamiltonian cycles, each once, as edge bitmasks."""
    cycles = []
    path = [0]
    visited = 1

    def extend(v, visited):
        if len(path) == n:
            if 0 in adj[v] and path[1] < path[-1]:
                mask = 0
                for a, b in zip(path, path[1:] + [0]):
                    mask |= 1 << edge_index[(min(a, b), max(a, b))]
                cycles.append(mask)
            return
        for w in adj[v]:
            if not visited >> w & 1:
                path.append(w)
                extend(w, visited | 1 << w)
                path.pop()

    extend(0, visited)
    return cycles


def three_cycle_cover(num_edges, cycles):
    """Return three cycle indices whose union is every edge, or None."""
    full = (1 << num_edges) - 1
    if len(cycles) == 0:
        return None
    through = [0] * num_edges  # bitset over cycle indices
    for ci, mask in enumerate(cycles):
        m = mask
        while m:
            low = m & -m
            e = low.bit_length() - 1
            through[e] |= 1 << ci
            m ^= low
    counts = [bin(t).count("1") for t in through]
    if min(counts) == 0:
        return None
    e0 = min(range(num_edges), key=lambda e: counts[e])

    def indices(bits):
        while bits:
            low = bits & -bits
            yield low.bit_length() - 1
            bits ^= low

    for c1 in indices(through[e0]):
        rest1 = full & ~cycles[c1]
        # choose the uncovered edge with fewest cycles through it
        e1 = min((e for e in range(num_edges) if rest1 >> e & 1), key=lambda e: counts[e])
        for c2 in indices(through[e1]):
            rest2 = rest1 & ~cycles[c2]
            if rest2 == 0:
                return (c1, c2, c2)
            cand = (1 << len(cycles)) - 1
            m = rest2
            while m and cand:
                low = m & -m
                cand &= through[low.bit_length() - 1]
                m ^= low
            if cand:
                c3 = (cand & -cand).bit_length() - 1
                return (c1, c2, c3)
    return None


def analyse(n, faces):
    G = nx.Graph()
    for f in faces:
        for a, b in ((f[0], f[1]), (f[0], f[2]), (f[1], f[2])):
            G.add_edge(a, b)
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    edge_index = {e: i for i, e in enumerate(edges)}
    degrees = [G.degree(v) for v in range(n)]
    adj = [sorted(G.neighbors(v)) for v in range(n)]
    discrete = colour_refinement_discrete(n, faces)
    cover = None
    num_cycles = None
    if max(degrees) <= 6:
        cycles = hamiltonian_cycles(n, adj, edge_index)
        num_cycles = len(cycles)
        found = three_cycle_cover(len(edges), cycles)
        if found is not None:
            cover = [[list(edges[e]) for e in range(len(edges)) if cycles[c] >> e & 1] for c in found]
    return {"degrees": sorted(degrees), "max_degree": max(degrees), "colour_refinement_discrete": discrete,
            "hamiltonian_cycles": num_cycles, "three_cycle_cover": cover, "graph": G}


def main():
    spec_path, results = sys.argv[1], sys.argv[2]
    os.makedirs(results, exist_ok=True)
    spec = json.load(open(spec_path))
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(spec_path)))
    plantri = os.path.join(workspace, spec["plantri"])
    table = json.load(open(os.path.join(workspace, spec["table1"])))
    s13_faces = sorted(tuple(sorted(row[1])) for row in table["faces"])
    s13 = analyse(13, s13_faces)
    summary = {"plantri_sha256": spec["plantri_sha256"], "per_n": {}, "s13_table1": {
        "colour_refinement_discrete": s13["colour_refinement_discrete"],
        "has_three_cycle_cover": s13["three_cycle_cover"] is not None,
        "hamiltonian_cycles": s13["hamiltonian_cycles"], "degrees": s13["degrees"]}}
    examples = []
    s13_found_in_enumeration = None
    for n in range(spec["n_min"], spec["n_max"] + 1):
        out = subprocess.run([plantri, str(n), "-a"], capture_output=True, text=True, check=True).stdout
        lines = [line for line in out.splitlines() if line.strip()]
        stats = {"triangulations": len(lines), "max_degree_at_most_6": 0, "colour_refinement_discrete": 0,
                 "three_cycle_cover": 0, "both": 0}
        for index, line in enumerate(lines):
            _, _, faces = parse_plantri_ascii(line)
            info = analyse(n, faces)
            stats["max_degree_at_most_6"] += info["max_degree"] <= 6
            stats["colour_refinement_discrete"] += info["colour_refinement_discrete"]
            stats["three_cycle_cover"] += info["three_cycle_cover"] is not None
            both = info["colour_refinement_discrete"] and info["three_cycle_cover"] is not None
            stats["both"] += both
            if both and n <= spec["list_up_to_n"]:
                examples.append({"n": n, "plantri_index": index, "plantri_ascii": line, "faces": [list(f) for f in faces],
                                 "degrees": info["degrees"], "hamiltonian_cycles": info["hamiltonian_cycles"],
                                 "three_cycle_cover": info["three_cycle_cover"]})
            if n == 13 and s13_found_in_enumeration is None and info["degrees"] == s13["degrees"]:
                if nx.is_isomorphic(info["graph"], s13["graph"]):
                    s13_found_in_enumeration = {"plantri_index": index, "both": both}
        summary["per_n"][str(n)] = stats
        print(json.dumps({"n": n, **stats}), flush=True)
    summary["s13_in_plantri_n13"] = s13_found_in_enumeration
    summary["smallest_n_with_both"] = min((e["n"] for e in examples), default=None)
    json.dump(summary, open(os.path.join(results, "summary.json"), "w"), indent=1, sort_keys=True)
    json.dump(examples, open(os.path.join(results, "examples.json"), "w"), indent=1)
    print(json.dumps({"summary": summary}, sort_keys=True))


if __name__ == "__main__":
    main()
