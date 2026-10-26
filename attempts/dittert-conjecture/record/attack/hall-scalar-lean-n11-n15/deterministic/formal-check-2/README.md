# Finite Hall scalar certificate

The theorem HallScalar.finite_certificate proves direct rational positivity of M, C and the completed-square discriminant for every natural n in11..15 and every a,b with0<a+b<n. The finite computation checks335 ordered proper cases and5 normalized marginals. The same theorem includes a kernel proof that the reduced case counts sum to340, and all_good explicitly transports both marginal orientations and arbitrary natural sizes to the checked family.

Definitions.lean and Finite.lean are a self-contained snapshot of the finite portion of formal-check-1. Their formulas are direct factorial/rational definitions, not Python-generated numeric premises. No external checker is trusted. This is a finite scalar theorem, not a proof of the matrix-derived inequalities or full Dittert.

Lean v4.33.1, Mathlib v4.33.1 pinned by lake-manifest.json. Replay: lake exe cache get if needed, then lake build, then lake env lean on a file importing Finite and printing axioms of HallScalar.finite_certificate. The Exactory formal check performs build and the axiom audit. Native evaluation is not accepted. Locally cached dependency symlinks are optional and excluded from the evidence archive.
