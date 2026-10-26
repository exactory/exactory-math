"""Explore weighted C5 blow-ups, retaining numerical scope and random seed."""

import itertools
import json
from pathlib import Path

import numpy as np


labels = np.array(list(itertools.product(range(3), repeat=5)))
templates = []
cycle = np.zeros((5, 5))
for i in range(5):
    cycle[i, (i + 1) % 5] = cycle[(i + 1) % 5, i] = 1
for assignment in labels:
    target = np.array([[int({assignment[i], assignment[j]} == {1, 2}) for j in range(5)] for i in range(5)])
    templates.append(np.abs(cycle - target))
templates = np.array(templates)

def inspect(weights):
    m = float(weights @ cycle @ weights / 2)
    root = np.sqrt(weights)
    lam = float(np.linalg.eigvalsh(root[:, None] * cycle * root[None, :])[-1])
    distances = np.einsum("i,kij,j->k", weights, templates, weights) / 2
    k = int(np.argmin(distances))
    deficit = m - lam * lam
    return {"weights": weights.tolist(), "m": m, "lambda": lam,
            "distance": float(distances[k]), "labels": labels[k].tolist(),
            "deficit": deficit, "ratio": float(distances[k] / deficit) if deficit > 1e-10 * m else None}

rng = np.random.default_rng(20261021)
samples = [np.ones(5)]
samples.extend(np.array(w, dtype=float) for w in itertools.product(range(1, 6), repeat=5))
samples.extend(10 ** rng.uniform(-3, 3, 5) for _ in range(10000))
records = [inspect(w) for w in samples]
ranked = sorted((r for r in records if r["ratio"] is not None), key=lambda r:r["ratio"], reverse=True)
Path("results").mkdir(exist_ok=True)
Path("results/cycle_blowups.json").write_text(json.dumps({
    "scope": "All 3125 positive integer weight tuples from 1 through 5, the balanced tuple, and 10000 log-uniform real tuples.",
    "seed": 20261021,
    "method": "All 243 assignments of five whole twin classes to two parts and isolation; float64 spectral radius of symmetric quotient.",
    "limitation": "The whole-class reduction is a mathematical argument to verify separately; numerical eigenvalues do not certify the inequality.",
    "sample_count": len(records), "largest_ratios": ranked[:30],
    "violations_at_1e-7": [r for r in ranked if r["ratio"] > 3 + 1e-7]
}, indent=2) + "\n")
print(json.dumps({"samples": len(records), "max_ratio": ranked[0]["ratio"]}))
