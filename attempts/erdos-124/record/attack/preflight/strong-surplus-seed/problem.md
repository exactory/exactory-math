# Problem study: almost-linear surplus and central seeds

## Queries

See sources/queries.md for the exact queries, date, saved replies and access
limitations. The bounded study was conducted on 2026-09-07.

## Exact proposed statement

For every nondecreasing locally finite infinite sequence (a_i) of positive integers with bounded numerical multiplicity, if every tail has gcd one and its finite subset sums meet every residue class modulo every positive integer, liminf_{X->infinity} (log 2)#{i:a_i<=X}/log X>1, sum_i ||alpha a_i||^2=infinity for every irrational real alpha (where ||x|| is distance to the nearest integer), and (S_m-a_{m+1})/a_{m+1}^beta tends to positive infinity for every real beta with 0<beta<1, where S_m=sum_{i=1}^m a_i, then there exist integers L>=0 and m_0>=1 such that for every m>=m_0, S_m>=2L and every integer in [L,S_m-L] is a subset sum of a_1,...,a_m using each labelled index at most once.

This is a separately posed sufficient principle on abstract sequences,
not the original pure-power claim and not an assertion that the principle
is true. A counterexample would reject only this proposed inference.

## Hits worth reading

- Burr and Erdos, Completeness properties of perturbed sequences,
  Journal of Number Theory 13 (1981), 446-455,
  DOI 10.1016/0022-314X(81)90036-6. Relevant Sections 1-3 read from the
  primary PDF; printed pp.448 and 450 visually checked. Full source saved.
- BEGL96, DOI 10.4064/aa-77-2-133-138, and Bergelson-Simmons,
  arXiv:1507.02208v2, are inherited background on pure powers and
  disjoint-supply completeness. No theorem from them is presumed to
  settle the new abstract assertion.
- Predecessor checkpoint-000009 is an accepted qualitative surplus theorem
  for actual admissible power streams. The new all-sublinear-power
  growth hypothesis is stronger and is not proved for those streams
  merely by that acceptance.
- The earlier translated-power example in
  erdos-124-central-prefix/moves/002-translated-power-barrier.md has
  only logarithmic endpoint surplus. It does not test the new hypothesis.

## Constraints on the plan

Burr-Erdos Section 2 creates incomplete perturbations through an irrational
norm-summability obstruction, which the new claim expressly excludes.
Its Section 3 completeness lemmas require disjoint subsequences: one
with arbitrarily long represented intervals and another with bounded
prefix deficit. Their disjointness cannot be discarded.

The exact question is whether strengthening the surplus to dominate
every fixed sublinear power can rescue the previously rejected abstract
seed argument while retaining all its arithmetic and counting conditions.
Any candidate must be checked along all prefixes, not just favourable
block endpoints. Raw label counts must not be confused with the number
of distinct numerical sums.

A proposed structured counterexample uses repeated geometric blocks
with a slowly varying positive relative perturbation. Adjacent blocks
are linked by an affine identity with constant one to preserve strong
arithmetic non-obstruction. A base-digit coefficient encoding is a
candidate way to control the actual numerical support. The formula and
all limits remain hypotheses until a reserved move proves them.

The root-connected proposal must keep three distinct obligations:
this abstract inference, the stronger profile for actual pure-power
streams, and the implication bridge to C1. It is useful to test the
inference before spending effort on the stronger profile. Refuting it
cannot refute C1 or the original root.

## Stop reason

Fixed query count reached. No exact theorem for this conjunction was
found. The methods are related to classical perturbation constructions;
standalone publication novelty is not claimed.

