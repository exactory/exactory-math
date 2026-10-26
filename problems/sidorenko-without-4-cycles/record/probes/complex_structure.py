#!/usr/bin/env python3
"""Structure of the triple system of the reported Sidorenko counterexample.

Usage: complex_structure.py TABLE.json RESULTS_DIR

Checks, from Table 1 alone: the pair-face incidences and the opposite-face columns; the link of
every point (a 2-regular graph; a single cycle at every point makes the complex a closed surface);
the Euler characteristic and orientability; whether, for each bit position and value, the faces of
that class form a triangulated disk whose boundary is a Hamiltonian cycle of the point graph;
which pairs lie on which boundary cycles; planarity of the point graph; and the automorphism
groups of the incidence graph H and of the point graph.
"""
import itertools
import json
import os
import sys

import networkx as nx
from networkx.algorithms import isomorphism


def load(path):
    data = json.load(open(path))
    faces = {row[0]: tuple(sorted(row[1])) for row in data["faces"]}
    opposite = {row[0]: row[2] for row in data["faces"]}
    bits = {row[0]: row[3] for row in data["faces"]}
    return data, faces, opposite, bits


def link_cycles(point, faces):
    link = nx.Graph()
    for f in faces.values():
        if point in f:
            a, b = [x for x in f if x != point]
            link.add_edge(a, b)
    degrees = sorted(set(d for _, d in link.degree()))
    return link, degrees, nx.number_connected_components(link)


def orientable(faces):
    # Try to orient every face so that each pair is traversed in opposite directions by its two faces.
    face_ids = sorted(faces)
    orient = {face_ids[0]: faces[face_ids[0]]}
    queue = [face_ids[0]]

    def directed_edges(tri):
        a, b, c = tri
        return {(a, b), (b, c), (c, a)}

    pair_faces = {}
    for j, f in faces.items():
        for p in itertools.combinations(f, 2):
            pair_faces.setdefault(frozenset(p), []).append(j)
    while queue:
        j = queue.pop()
        for p in itertools.combinations(faces[j], 2):
            for k in pair_faces[frozenset(p)]:
                if k == j:
                    continue
                cand = faces[k]
                options = [cand, (cand[0], cand[2], cand[1])]
                good = [o for o in options if not (directed_edges(o) & directed_edges(orient[j]))]
                if k in orient:
                    if directed_edges(orient[k]) & directed_edges(orient[j]):
                        return False
                    continue
                if not good:
                    return False
                orient[k] = good[0]
                queue.append(k)
    return len(orient) == len(faces)


def main():
    table, results = sys.argv[1], sys.argv[2]
    os.makedirs(results, exist_ok=True)
    data, faces, opposite, bits = load(table)
    points = sorted(set(x for f in faces.values() for x in f))
    pair_faces = {}
    for j, f in faces.items():
        for p in itertools.combinations(f, 2):
            pair_faces.setdefault(frozenset(p), []).append(j)
    out = {"points": len(points), "faces": len(faces), "pairs": len(pair_faces)}
    out["every_pair_in_exactly_two_faces"] = all(len(v) == 2 for v in pair_faces.values())
    # Opposite-face columns: entry for {i_a, i_b} names the other face containing that pair.
    mismatches = []
    for j, f in faces.items():
        i1, i2, i3 = f
        for pair, k in zip(((i1, i2), (i1, i3), (i2, i3)), opposite[j]):
            others = [x for x in pair_faces[frozenset(pair)] if x != j]
            if others != [k]:
                mismatches.append({"face": j, "pair": pair, "table": k, "computed": others})
    out["opposite_column_mismatches"] = mismatches
    out["euler_characteristic"] = len(points) - len(pair_faces) + len(faces)
    links = {}
    for v in points:
        link, degrees, components = link_cycles(v, faces)
        links[v] = {"link_vertices": link.number_of_nodes(), "link_degrees": degrees, "components": components}
    out["links"] = links
    out["closed_surface"] = all(l["link_degrees"] == [2] and l["components"] == 1 for l in links.values())
    out["orientable"] = orientable(faces)
    point_graph = nx.Graph()
    point_graph.add_edges_from(tuple(p) for p in pair_faces)
    out["point_degrees"] = {v: point_graph.degree(v) for v in points}
    out["point_graph_planar"] = nx.check_planarity(point_graph)[0]
    # Bit classes: boundary of the class = pairs lying in exactly one face of the class.
    classes = []
    boundary_pairs = []
    for position in range(3):
        for value in "01":
            cls = sorted(j for j in faces if bits[j][position] == value)
            count = {}
            for j in cls:
                for p in itertools.combinations(faces[j], 2):
                    count[frozenset(p)] = count.get(frozenset(p), 0) + 1
            boundary = [tuple(sorted(p)) for p, c in count.items() if c == 1]
            bgraph = nx.Graph()
            bgraph.add_edges_from(boundary)
            covered = sorted(set(x for j in cls for x in faces[j]))
            is_cycle = (bgraph.number_of_nodes() > 0 and all(d == 2 for _, d in bgraph.degree())
                        and nx.is_connected(bgraph))
            dual = nx.Graph()
            dual.add_nodes_from(cls)
            for p, c in count.items():
                if c == 2:
                    a, b = [j for j in cls if set(p) <= set(faces[j])]
                    dual.add_edge(a, b)
            classes.append({"position": position + 1, "value": value, "faces": cls, "size": len(cls),
                            "points_covered": len(covered), "boundary_pairs": sorted(boundary),
                            "boundary_is_single_cycle": is_cycle,
                            "boundary_cycle_length": bgraph.number_of_nodes() if is_cycle else None,
                            "boundary_is_hamiltonian": is_cycle and bgraph.number_of_nodes() == len(points),
                            "dual_graph_is_tree": nx.is_tree(dual)})
            if value == "0":
                boundary_pairs.append(set(map(frozenset, boundary)))
    out["bit_classes"] = classes
    # For each pair: the number of bit positions at which its two faces differ, and whether the pair
    # lies on the boundary cycle of position t (the two answers should agree for a Jordan curve).
    pair_rows = []
    for p, (a, b) in sorted(pair_faces.items(), key=lambda kv: sorted(kv[0])):
        differ = [t + 1 for t in range(3) if bits[a][t] != bits[b][t]]
        on_boundary = [t + 1 for t in range(3) if p in boundary_pairs[t]]
        pair_rows.append({"pair": sorted(p), "faces": [a, b], "positions_differing": differ,
                          "on_boundary_of_position": on_boundary, "a_e": len(differ) / 3})
    out["pairs_detail"] = pair_rows
    out["every_pair_on_some_boundary_cycle"] = all(r["on_boundary_of_position"] for r in pair_rows)
    out["differ_equals_boundary"] = all(r["positions_differing"] == r["on_boundary_of_position"] for r in pair_rows)
    out["pairs_with_a_e_above_one_third"] = [r["pair"] for r in pair_rows if len(r["positions_differing"]) > 1]
    # Incidence graph H and automorphisms.
    H = nx.Graph()
    for v in points:
        H.add_node(("p", v), part=0)
    for j in faces:
        H.add_node(("f", j), part=1)
        for v in faces[j]:
            H.add_edge(("p", v), ("f", j))
    out["H_vertices"] = H.number_of_nodes()
    out["H_edges"] = H.number_of_edges()
    out["H_connected"] = nx.is_connected(H)
    out["H_girth_is_6"] = (nx.girth(H) == 6) if hasattr(nx, "girth") else None
    matcher = isomorphism.GraphMatcher(H, H, node_match=lambda a, b: a["part"] == b["part"])
    autos = 0
    for _ in matcher.isomorphisms_iter():
        autos += 1
        if autos > 10000:
            break
    out["H_part_preserving_automorphisms"] = autos
    m2 = isomorphism.GraphMatcher(point_graph, point_graph)
    pg_autos = 0
    for _ in m2.isomorphisms_iter():
        pg_autos += 1
        if pg_autos > 10000:
            break
    out["point_graph_automorphisms"] = pg_autos
    degree_counts = {}
    for v in points:
        degree_counts[point_graph.degree(v)] = degree_counts.get(point_graph.degree(v), 0) + 1
    out["point_degree_counts"] = degree_counts
    json.dump(out, open(os.path.join(results, "complex-structure.json"), "w"), indent=1, sort_keys=True)
    summary = {k: out[k] for k in ("points", "faces", "pairs", "every_pair_in_exactly_two_faces",
                                   "opposite_column_mismatches", "euler_characteristic", "closed_surface",
                                   "orientable", "point_graph_planar", "every_pair_on_some_boundary_cycle",
                                   "differ_equals_boundary", "pairs_with_a_e_above_one_third", "H_vertices",
                                   "H_edges", "H_connected", "H_part_preserving_automorphisms",
                                   "point_graph_automorphisms", "point_degree_counts")}
    summary["bit_classes"] = [{k: c[k] for k in ("position", "value", "size", "points_covered",
                                                  "boundary_is_single_cycle", "boundary_cycle_length",
                                                  "boundary_is_hamiltonian", "dual_graph_is_tree")} for c in classes]
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
