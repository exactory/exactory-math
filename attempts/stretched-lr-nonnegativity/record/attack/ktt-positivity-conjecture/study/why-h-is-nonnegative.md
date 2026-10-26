# Why the h vectors might be nonnegative: a mechanism, and what would test it

Date: 2026-09-05. A derivation with one citation, no run.

## The question move 6 left

Move 5 found no negative entry in the h vectors of 6,855,302 certified polynomials. Move 6 showed
that the sufficient condition of move 4, integral closure, fails for the family: there are hive
polytopes with exactly `D + 1` lattice points and normalized volume two, and those are not
integrally closed. Nor are they lattice polytopes, since they have seven vertices and five lattice
points. So neither of the two routes that would explain nonnegative h applies, and the observation
is unexplained.

## A mechanism that would explain it

Two elementary steps and one citation.

1. **Ehrhart equivalence transports h.** The vector h is determined by the polynomial alone, by the
   basis change of move 3. So if a rational polytope `P` has the same Ehrhart polynomial as some
   lattice polytope `Q`, then `h(P) = h*(Q)`, and Stanley's theorem gives `h*(Q) >= 0`
   unconditionally, with no integral closure anywhere in it.
2. **Scissors congruence gives Ehrhart equivalence.** Cutting a polytope into pieces and moving
   them by affine maps that preserve the lattice does not change the number of lattice points in
   any dilate, provided the pieces are taken half-open so that nothing is counted twice or lost.
   So a rational polytope that is scissors congruent, in that lattice-preserving sense, to a
   lattice polytope has the same Ehrhart polynomial as it.
3. **The literature connects period collapse to exactly that.** Haase and McAllister,
   "Quasi-period collapse and GL_n(Z)-scissors congruence in rational polytopes",
   arXiv:0709.4070, take up quasi-period collapse, which is what the hive polytopes exhibit: their
   Ehrhart quasi-polynomials are polynomials although their vertices are rational
   (Derksen-Weyman). The paper's abstract states that the phenomenon is poorly understood and that
   the known cases had been handled by ad hoc methods; the title names the connection this
   derivation uses. The citation is to the title and the abstract as retrieved on 2026-09-05; no
   numbered statement of theirs is relied on.

Putting the three together: **if the five-part hive polytopes are lattice-preserving scissors
congruent to lattice polytopes, then both the period collapse and the nonnegative h follow, and
neither integral closure nor lattice vertices are needed.** That is a mechanism consistent with
everything the record holds and it is not proved here.

## What would test it, cheaply, on data already held

Ehrhart equivalence to a lattice polytope forces more than nonnegativity: it forces h to satisfy
every inequality that h*-vectors of lattice polytopes satisfy. Three are standard and are
computable from the recorded h vectors with no polytope construction:

- Stanley's inequality: the partial sums from the bottom are at most the partial sums from the top,
  `h_0 + ... + h_i <= h_s + h_(s-1) + ... + h_(s-i)` for every `i`, with `s` the degree.
- Hibi's lower bound: `h_1 <= h_i` for `1 <= i <= d - 1`, when `h_d` is nonzero.
- `h_d <= h_1`.

Each is a necessary condition for the mechanism. A single record violating one refutes the
mechanism for that polytope outright, which would be a sharper result than the nonnegativity census
and would be reached the same way. Records that satisfy all three support the mechanism without
proving it, and the record would say so, because a nonnegative census over a family containing
lattice polytopes carries less information than it looks, as move 5 already states.

## What this does not do

It does not prove the conjecture, and it does not bear on it directly: Reeve's tetrahedron is a
lattice polytope, so it satisfies every inequality above, and its linear coefficient is negative
for large parameter. The mechanism would explain the h census and nothing more.
