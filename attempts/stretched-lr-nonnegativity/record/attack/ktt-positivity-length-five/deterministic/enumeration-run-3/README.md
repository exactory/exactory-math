# enumeration-run-3: a search for a failing facet, and what the margin actually tracks

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, steps 1 and 3. Approved with
amendments by two independent reviews of 2026-09-05, recorded in `../../ADMISSION.md`.

## Why this ran

`certified-special-case-check-6` found no failure of the per-facet inequality in 46,501 tests, but
its margin fell with the complexity of the cell, and the record read that as evidence that the
inequality might be false at higher complexity. Two readings were possible and were registered in
advance: a real downward trend, which predicted a band median near 40 in the band of about 900 to
1,500 edges; and an order-statistic effect, the minimum falling because more facets are tested,
which predicted a band median near 100. A third reading, that the ratio tracks the construction
route rather than the edge count, was also registered.

## Phase one: the search

Cells above the top band already measured, built from both sources so that edge count and
construction route are separated, with the vertex cap raised from 220 to 600.

| | |
|---|---|
| cells tested | 242 |
| of them above 684 edges | 70, being 38 generic and 32 from perturbed box triples |
| facet ray tests | 206,072, of which 157,814 above 684 edges |
| failing facets | 0 |
| largest cell | 1,127 edges |
| worst ratio found | 14.89 |

Bands, old and new data together, banded by the floor power of two of the cell's edge count:

| band | cells | facet ray tests | worst | lower quartile | median | upper quartile |
|---|---|---|---|---|---|---|
| 64 | 28 | 657 | 62.77 | 268.60 | 273.77 | 281.40 |
| 128 | 149 | 5,420 | 58.09 | 304.45 | 325.36 | 365.34 |
| 256 | 183 | 36,185 | 22.51 | 75.12 | 131.22 | 236.26 |
| 512 | 211 | 178,865 | 14.89 | 46.98 | 83.93 | 141.51 |
| 1,024 | 3 | 31,446 | 23.43 | | 27.14 | |

On the registered criterion this is undecided. The top band's median of 27.14 is below the trend
reading's 40, but it rests on three cells. The 70 cells above 684 edges have medians 63.73 when
built at a generic point and 93.48 when built from a perturbed box triple, both between the two
predictions, and the difference between them at matched edge count is the provenance effect the
third reading named.

The run was stopped at its allowance with one cell in progress. Its 242 recorded cells are
complete; `summarise.py` is the summary block of `run.py`, run separately over those records.

## Phase two: what the margin tracks

The trend reading's stated mechanism is that the negative share grows with the number of negative
edges on a facet. `facets.jsonl` records no per-facet detail, so the mechanism had never been
tested and the whole extrapolation rested on the cell's total edge count, a proxy. `refacet.py`
re-ran the facet computation over the 2,199 cells already built, recording per facet that carries
a negative edge how many it carries.

A first pass of this stopped at its time budget after 2,119 cells, omitting the last 80, all of
them from `enumeration-run-2` and all among the largest, which held 664 of the 2,556 facets that
carry a negative edge. An independent review found the truncation. The tables below are the full
population; the truncated ones are kept as `per-facet.truncated.jsonl` and
`per-facet.truncated.summary.json` and are superseded.

| negative edges on the facet | facets | median ratio | worst |
|---|---|---|---|
| 1 | 1,782 | 634.43 | 17.12 |
| 2 | 538 | 423.19 | 24.00 |
| 3 | 167 | 346.64 | 28.40 |
| 4 | 50 | 203.12 | 22.51 |
| 5 | 14 | 333.69 | 39.95 |
| 6 | 4 | 102.38 | 17.77 |
| 7 | 1 | 280.43 | 280.43 |

| the cell's edge count | facets | median ratio |
|---|---|---|
| 64 | 135 | 717.20 |
| 128 | 793 | 617.00 |
| 256 | 839 | 533.13 |
| 512 | 789 | 462.55 |

The median ratio spreads by a factor of 6.20 across the per-facet negative-edge count and by 1.55
across an eightfold growth in the cell's edge count. The count is the proximate driver. Two bins
break the trend and are not smoothed over: five negative edges gives 333.69, above the value at
four, and the single facet with seven gives 280.43, above the value at six.

## Addendum: the cell's size acts through the count

The count itself grows with the cell, so the size is not absent; it acts through the count.

| cell edge-count band | facets | maximum count | mean count | share with three or more |
|---|---|---|---|---|
| 64 | 135 | 1 | 1.00 | 0.000 |
| 128 | 793 | 3 | 1.10 | 0.001 |
| 256 | 839 | 7 | 1.56 | 0.117 |
| 512 | 789 | 6 | 1.70 | 0.174 |

And inside the 512-edge band alone, with the cell's size held fixed, the count still moves the
margin: median ratio 549.33, 444.80, 315.60, 274.63, 232.67, 102.38 for counts one to six.

## Where the extrapolation actually lands, and how far outside its data

Fitting power laws to the full population: the mean count grows about as the cell's edge count to
the power 0.31, from 1.10 at 128 edges to 1.70 at 512, and the median ratio falls about as the
count to the power 0.94, from 549.33 at one negative edge to 102.38 at six inside the 512-edge
band. Composing them, the median margin reaches one at a per-facet count of order 800, and a cell
whose mean count is 800 would have of order `2 x 10^11` edges.

An earlier version of this addendum said ten million edges. That figure came from extrapolating
the worst ratio rather than the median, and the worst ratio is the order statistic this same run
identifies as an artefact of testing more facets. It is withdrawn.

Both fits run far outside their data and the record says by how much. The count fit spans 1.00 to
1.70 over four bands and is extended to 800. The ratio fit spans counts one to six over six bins,
the last two holding 8 and 4 facets, and is extended to a count of 800. The bins at five and seven
contradict the trend. These are fits, not bounds, and nothing here is a proof.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. Both summaries against their record files, every field recomputed, including the failure count.
2. The band table's rows for the old data recomputed from `certified-special-case-check-6` and
   merged with the new: 4 bands, 0 mismatches.
3. On 8 sampled new cells, the per-facet inequality recomputed from the polytope: 0 worst ratios
   disagreeing, 0 facets failing.
4. The mechanism medians regrouped from `per-facet.jsonl` without trusting the run's grouping:
   spread 4.75 by the per-facet negative-edge count against 1.60 by the cell's edge count.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of
`enumeration-run-1` and `enumeration-run-2`, Python integers and Fractions, and the local
Euler-Maclaurin formula for rational hive polytopes.

## Addendum: the cell's size acts through the count

The reading above, that the driver is the per-facet negative-edge count and not the size of the
cell, is too strong, and `mediation.py` corrects it from the same records with nothing added.

| cell edge-count band | facets | maximum count | mean count | share with three or more |
|---|---|---|---|---|
| 64 | 135 | 1 | 1.00 | 0.000 |
| 128 | 793 | 3 | 1.10 | 0.001 |
| 256 | 547 | 7 | 1.63 | 0.139 |
| 512 | 417 | 6 | 1.77 | 0.201 |

So the count itself grows with the cell. And inside the 512-edge band alone, with the cell's size
held fixed, the count still moves the margin:

| negative edges on the facet | facets | median ratio | worst |
|---|---|---|---|
| 1 | 221 | 589.29 | 38.85 |
| 2 | 112 | 432.29 | 24.00 |
| 3 | 52 | 266.13 | 36.72 |
| 4 | 24 | 234.25 | 34.84 |
| 5 | 5 | 187.78 | 39.95 |
| 6 | 3 | 135.76 | 17.77 |

The correct statement is that the count is the proximate driver and the cell's size acts through
it. Both effects are real and they compose. What does not change is the size of the effects: the
mean count grows about as the cell's edge count to the power 0.35, from 1.10 at 128 edges to 1.77
at 512, and the median ratio falls about as the count to the power 0.85, from 589 at one negative
edge to 136 at six. Composing them, a facet whose margin reaches one needs a count of order two
thousand, and a cell reaching that mean count would need of order ten million edges against the
1,127 built here. The inequality looks robust on this evidence, and it is still unproved.
