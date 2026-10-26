"""Exploratory exhaustive edit distances; numerical eigenvalues are not proofs."""

import itertools
import json
from pathlib import Path

import networkx as nx
import numpy as np


def distance(graph):
    n = len(graph)
    edges = list(graph.edges())
    best = len(edges)
    for labels in itertools.product(range(3), repeat=n):
        a = labels.count(1)
        b = labels.count(2)
        cross = sum({labels[u], labels[v]} == {1, 2} for u, v in edges)
        best = min(best, len(edges) + a * b - 2 * cross)
    return best


records = []
for index, graph in enumerate(nx.graph_atlas_g()):
    if graph.number_of_edges() == 0 or any(nx.triangles(graph).values()):
        continue
    lam = float(np.linalg.eigvalsh(nx.to_numpy_array(graph))[-1])
    deficit = graph.number_of_edges() - lam * lam
    edits = distance(graph)
    records.append({"atlas_index": index, "n": len(graph), "m": graph.number_of_edges(),
                    "lambda": lam, "deficit": deficit, "distance": edits,
                    "ratio": edits / deficit if deficit > 1e-10 else None,
                    "bipartite": nx.is_bipartite(graph), "edges": list(graph.edges())})
Path("results").mkdir(exist_ok=True)
Path("results/atlas.json").write_text(json.dumps({
    "scope": "Every unlabeled triangle-free simple graph with 1 to 7 vertices in NetworkX atlas, excluding empty graphs.",
    "distance_method": "Exact enumeration of all assignments to two parts and isolated vertices.",
    "spectral_method": "NumPy float64 eigvalsh; tolerance 1e-10, exploratory only.",
    "records": records,
    "largest_ratios": sorted((r for r in records if r["ratio"] is not None), key=lambda r:r["ratio"], reverse=True)[:20]
}, indent=2) + "\n")
print(json.dumps({"graphs": len(records), "max_ratio": max(r["ratio"] or 0 for r in records)}))
