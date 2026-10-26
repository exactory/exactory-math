# Plan

1. Reconstruct all Hall-cut and marginal-support reductions from definitions.
   Record a complete, signed and endpoint-aware coverage proof and identify
   the exact imported permanent floors.
2. Add a lightweight exact independent checker for all ordered cut cases,
   scalar domains, and the marginal support/interval cover. Include mutation
   regressions rejecting omitted cases, omitted endpoints, and unjustified
   localizations. Compare with separately implemented source certificates.
3. Consolidate the argument, save an immutable checkpoint, and prepare the
   unit package for a fresh independent reader assigned by the parent.

Every mathematical move uses certify-the-finite-residue-by-computation under
reduce-to-a-finite-computation. No heavy matrix computations, full Mathlib
builds, or further agents will be started without coordination.

