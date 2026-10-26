# certified-special-case-check-5: local domination, and which neighbourhood is large enough

Date: 2026-09-05. Entry: average-a-local-inequality-over-neighbourhoods.

## The question

`certified-special-case-check-4` cut the residue to the cells carrying an edge of a
negative-weight class. Those cells are unenumerated and of unknown number. A local statement would
avoid enumerating them.

Give each positive-weight edge an equal share of its weighted length to each negative-weight edge
in a chosen neighbourhood of it, and let `share(e)` be what `e` receives. The shares of distinct
negative edges are disjoint parts of the positive sum, so

    share(e) >= |w(e)| * (lattice length of e)   for every negative edge e   =>   a_1 >= 0

on every cell at once. Both sides are linear on a cell, so each test is decided at the extreme
rays. Two neighbourhoods were measured: the **vertex** neighbourhood, the edges sharing a vertex
with `e`, and the **facet** neighbourhood, the edges lying on a facet that contains `e`, which is
the neighbourhood the class of `e` already names.

## Result (`domination.summary.json`, `domination.jsonl`, `result.json` status pass)

| | |
|---|---|
| cells carrying a negative edge | 332 |
| negative edges | 732 |
| ray tests per neighbourhood | 14,899 |
| vertex neighbourhood: failures | 106 |
| vertex neighbourhood: smallest ratio | 0 |
| facet neighbourhood: failures | 0 |
| facet neighbourhood: smallest ratio | 1567265857/18738000, about 83.6 |
| facet neighbourhood: largest ratio | 8425912939/312312 |
| negative edges with no positive vertex neighbour | 0 |

The vertex neighbourhood is not enough and the failure is sharp: at 106 of the 14,899 rays the
share is smaller than the demand, and at the worst of them it is zero, meaning every edge meeting
the negative edge at a vertex has zero length there while the negative edge does not. What rescues
the coefficient is positive weight further away, so no argument confined to the edges through a
vertex can work.

The facet neighbourhood is enough on every test made, by a factor of at least 83.6.

## What this makes plausible, and does not prove

For every five-part hive polytope and every edge whose class has negative weight, the shared
weighted length of the positive-weight edges on a facet through it is at least `|w|` times its
lattice length. That implies the rung by the disjointness of the shares. It needs a lower bound on
the lengths of the edges of a facet in terms of one edge on it, which is geometry rather than
Ehrhart theory. The 14,899 tests cover the cells this project has built and prove nothing.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `domination.jsonl`, every field recomputed.
2. The cell and edge counts against `certified-special-case-check-4`: 332 and 732 on both sides.
3. On 25 sampled cells recomputed from the polytope: the sum over all edges of the weight times
   the lattice length reproduces at every ray the value the step that built the cell recorded from
   a different route, 0 disagreements; the discharging rule is sound, the shares never exceeding
   the positive part, 0 failures; and the facet-neighbourhood share dominates at every ray, 0
   failures.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of `enumeration-run-1`
and `enumeration-run-2`, Python integers and Fractions, and the local Euler-Maclaurin formula for
rational hive polytopes.
