# certified-special-case-check-6: the per-facet inequality

Date: 2026-09-05. Entry: average-a-local-inequality-over-neighbourhoods.

## The inequality

Every edge `f` lies on `c(f)` facets. Give each facet `F` containing `f` the amount
`w(f) * len(f) / c(f)`. Summed over the facets these shares are exactly the functional, nothing
left over and nothing counted twice. So `a_1 >= 0` follows as soon as every facet pays for its own
negative edges:

    sum over the negative edges e on F of |w(e)| * len(e) / c(e)
        <=  sum over the positive edges f on F of w(f) * len(f) / c(f).

This is a statement about one facet. It mentions no cell, no chamber complex and no size, and it is
stronger than the neighbourhood statement of `certified-special-case-check-5` because a facet is
smaller than the union of the facets through an edge. Both sides are linear on a cell, so the test
is decided at the extreme rays.

## Result (`facets.summary.json`, `facets.jsonl`, `result.json` status pass)

| | |
|---|---|
| cells | 2,199 |
| facets seen | 28,691 |
| facets carrying a negative edge, and so tested | 2,556 |
| ray tests | 46,501 |
| tests where a facet fails to pay | 0 |
| cells with a failing facet | 0 |
| smallest ratio of the positive share to the negative share | 4730093/276213, about 17.1 |
| largest ratio | 659966507/279048 |
| ray values that disagree with the step that built the cell | 0 |

Every facet pays. The tightest case is a facet of the hive polytope at
`(147770, 147594, 105002, 70327, 61221)`, `(106246, 91584, 45436, 31078)`,
`(100523, 84659, 41706, 30682)`, one of the large cells; the small cells of
`certified-special-case-check-3` are far from tight, their worst ratio being about 157. Only 2,556
of the 28,691 facets carry a negative edge at all.

## What this says and does not

The conjecture it makes plausible implies the rung, because the shares add up to the functional
exactly. The evidence is 46,501 exact rational tests with no failure. The facets tested are those
of the cells this project has built; the number of facet types of a five-part hive polytope is
finite and has not been enumerated here, so this is evidence and not a proof.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `facets.jsonl`, every field recomputed.
2. The count of cells carrying a negative edge against `certified-special-case-check-4`: 332 on
   both sides.
3. On 20 sampled cells recomputed from the polytope: the facet shares add up at every ray to the
   value the step that built the cell recorded from a different route, which is what makes the
   per-facet form sufficient, 0 disagreements; and every facet carrying a negative edge pays for it
   at every ray, 0 failures.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of `enumeration-run-1`
and `enumeration-run-2`, Python integers and Fractions, and the local Euler-Maclaurin formula.
