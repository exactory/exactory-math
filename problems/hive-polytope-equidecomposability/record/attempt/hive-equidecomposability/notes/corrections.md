# Corrections to earlier wording in this record

Journal lines and pinned studies are immutable; the corrections below are recorded here and
in the strategy assessments that cite them.

1. Move 2, journal output: "N1 is as hard as the target in general (Turner-Wu ...)" is
   withdrawn. N1 (the Ehrhart form) is a consequence of the root statement, hence weaker, and
   Turner-Wu's examples (pairs of Ehrhart-equivalent rational polygons that are not finitely
   equidecomposable) show only that Ehrhart equivalence does not imply equidecomposability in
   general; they say nothing about relative difficulty and nothing about hives. What the
   failure signal of move 2 records is just that a verified instance of the weaker consequence
   decides nothing about the root at that instance.

2. Study `study/attack-the-negative-side.md`, hits table, row for Ghodsi 2026: "a disproof of
   the consequence N4 or of the statement through negative monomial coefficients is excluded
   there" is withdrawn. Nonnegativity of the monomial coefficients of the stretched polynomial
   is neither the numerator statement N4 nor a necessary condition for the polynomial to be the
   Ehrhart polynomial of a lattice polytope (lattice polytopes with negative Ehrhart
   coefficients exist), so computed monomial positivity excludes no disproof route of this
   record. Nothing in the attack depends on the withdrawn remark.

3. Move 2 note, first version: the parenthetical claim that the other reading of the border
   convention is obtained by the reflection (x, y) -> (y, x) followed by adding x - 2y was
   wrong (the border labels do not transform correctly) and was replaced before any review by
   the derivation in Section 8 of `proofs/smallest-instance.md`.

4. `proofs/smallest-instance.md`, Section 7 (the accepted version, digest
   77b6c8b78027b723a543519143ae4bd5812e2b243adeb35f643be4fc8b1b50c8): the phrase "as the
   defining inequalities of P_+, P_- and Q are homogeneous" is inaccurate (x <= 1 and z <= 1
   are not homogeneous). The dilation compatibility holds anyway: the pieces of tP are the
   dilates of the pieces of P, U is linear, and the integral translation of Section 6 is
   scaled by t, as the independent reviewer of the checkpoint noted. The accepted text is
   left unchanged; the correction is recorded here.
