# certified-special-case-check-4: the sharper residue, and how rare a dangerous cell is

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, steps 1 and 3. Step kind:
certified special-case check, one classification per cell.

## The reduction

On a cell of the chamber complex the functional is

    l(b) = sum over the edges e of  w(class of e) * (lattice length of e)(b),

and the lattice length of an edge is a nonnegative linear function of the boundary triple on the
whole cell, because the edge exists with that length at every triple of the cell. So

**if every edge class of a cell has a nonnegative weight, then l >= 0 on all of that cell, with no
computation at all.**

The residue of the rung is therefore only the cells that carry an edge whose class has a negative
weight. This run classifies every cell the project has built, measures how rare those are and how
much room they have, and records the negative classes over every weight the project holds rather
than over the atlas of `enumeration-run-1` alone.

## Result (`classified.summary.json`, `classified.jsonl`, `negative-classes.json`, `result.json` status pass)

| | |
|---|---|
| cells classified | 2,199 (2,006 from `certified-special-case-check-3`, 193 from `enumeration-run-2`) |
| edges examined | 226,740 |
| edges of a negative-weight class | 732 |
| cells carrying such an edge | 332 |
| cells the reduction settles with no computation | 1,867 |
| ray values that disagree with the two steps that built the cells | 0 |
| smallest ratio of the positive part to the negative part at a ray | 15181/61 |
| classes held | 5,142 |
| negative classes | 21 |
| most negative class weight | -347/109824 |

Two things worth separating. The first is a correction: `enumeration-run-1` found 5 negative
classes among the 3,406 that occur in 2,000 small hive polytopes, and the wider sweep of
`enumeration-run-2` brought the count of classes held to 5,142 and the count of negative ones to
21. The negative classes are not a fixed list of five; they grow with the sample, and
`negative-classes.json` records all 21 with their normals. The two weight files agree on every
class they share.

The second is the measurement. 85 percent of the cells built so far are settled by the reduction
without evaluating anything, and the dangerous ones are dangerous only in principle: at the worst
ray of the worst cell the positive part of the functional is 249 times the negative part. That
cell is the one at the triple (62780, 54763, 54405, 44759, 27943), (19723, 19430, 11042, 9184, 1),
(45337, 45138, 43238, 34944, 16613), and the ratio there is 15181/61.

## What is left

The residue is now the cells that carry a negative-weight edge, which is a smaller set than the
cells, but it is still not enumerated: the number of cells of the rank-five chamber complex is
unknown, and so is the number of them that carry such an edge. What the margin measurement says
is where to look for a proof: a bound of the form "the positive weight adjacent to a
negative-weight edge exceeds it" would close the rung, and the measured factor of 249 is the
first evidence about how much room such a bound has.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `classified.jsonl`, every field recomputed.
2. The negative classes recomputed by canonical form from the weight files of
   `enumeration-run-1` and `enumeration-run-2`, with the check that no class carries two
   different weights across the two files: 5,142 distinct classes, 21 negative, 0 conflicts.
3. The premise of the reduction against the steps that built the cells: every cell classified as
   carrying no negative-weight edge must have a nonnegative value at every extreme ray there, and
   every cell that does carry one must have its worst-ray split equal to one of the recorded ray
   values. 2,199 cells matched, 0 failures.
4. The functional at a point neither this run nor the sweep evaluated: for the eight cells with a
   negative class whose ray sum is smallest, the linear coefficient from the Ehrhart
   quasi-polynomial must equal the sum of the ray values recorded by the step that built the
   cell. 0 mismatches.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of
`enumeration-run-1` and `enumeration-run-2`, Python integers and Fractions, and the local
Euler-Maclaurin formula for rational hive polytopes.
