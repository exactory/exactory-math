# Persistent King-Tollu-Toumazet search tree

Original objective, unchanged: prove or refute that for all integer partitions lam, mu, nu with
|lam| = |mu| + |nu| and c^{lam}_{mu nu} > 0, every coefficient of the stretched
Littlewood-Richardson polynomial P(t) = c^{t lam}_{t mu, t nu} is nonnegative (King, Tollu and
Toumazet 2004). The FrontierMath problem that started the project is the restriction of the
negation to partitions of length at most 7 and size at most 30; that restriction is answered and
does not replace the objective. All artifacts are local and English.

## Cross-attack index

| Attack | Exact scope | Logical predecessor and checkpoint | Relationship | Status and evidence | Next unresolved question |
|---|---|---|---|---|---|
| stretched-lr-polynomial-negative-coefficient | The FrontierMath box: some triple of length <= 7 and size <= 30 has a negative coefficient | Original root of the project | Root (restricted negation) | Finished; refuted. `units/1` a proof by computation for length <= 6 (two independent programs), `units/2` evidence for the whole box; census `deterministic/certified-special-case-check-4` | The 7-part part rests on one solver; a second Ehrhart solver would make the box a theorem |
| stretched-lr-negative-coefficient-unbounded | The conjecture itself, attacked from the negative side (direction false assumed) | The box attack, historical evidence retained | Alternative route (opposite direction) | Finished; no counterexample. `units/1` sampled classes beyond the box, `units/2` necessary conditions on any counterexample | Sampling has no reach beyond the searched ranges; the positive side was never attempted |
| ktt-positivity-conjecture | The complete original objective, attacked from the positive side (direction true, mode certificate) | Both finished attacks; CP-26ae5b08da7c023a | Continuation / alternative route | Open, stage 5, 7 moves of 24. Move 1 reduces the objective to the rungs. Move 2: the reductions are rank-uniform, the atlas is not, and a rung's residue grows quadratically. Moves 3 and 4 translate every coefficient into the binomial basis and identify that basis as a Hilbert-series numerator. Move 5 finds no negative h entry in 6,855,302 polynomials. Move 6 shows from the same data that the family is not integrally closed, so the sufficient condition is not what produces that nonnegativity. Move 7 proposes the mechanism that would, Ehrhart equivalence to a lattice polytope, and names the three inequalities that would falsify it | Do the recorded h vectors satisfy Stanley's inequality, Hibi's lower bound and h_d at most h_1 |
| ktt-positivity-length-five | Every triple of length at most five, at every size (the rank-five rung) | ktt-positivity-conjecture, native child opened at its move 1; CP-8a910f43849d4e75 | Special case (one rung of the ladder in the number of parts) | Open, stage 5, 19 moves of 24, pass 3 at 3 of 8, **halted at the user's request with the record complete**. Proved: the cell reduction, the nonnegative-class lemma, the sufficiency of local domination and of the per-facet inequality, the intrinsic-lattice contraction. Measured: no failing facet in 252,573 tests; the weight route's residue is five classes under the best form; and no projected type at intrinsic dimension three or four is negative, over 444,175 contracted polytopes and 13,334 weighed types, smallest weight 1/120 (`enumeration-run-5`, pass) | Weigh the 25,565 types at intrinsic dimension five, then the codimension-two atlas that intrinsic dimension four still lacks for a_2 |

## Checkpoints

| Identifier | Date | Source | What it snapshots |
|---|---|---|---|
| CP-23ba531cae2da172 | 2026-09-05 | the two finished attacks at their closing states | the box result, the census, the beyond-box samples, and the necessary conditions on a counterexample |
| CP-c8649a4002111252 | 2026-09-05 | ktt-positivity-conjecture move 1, ktt-positivity-length-five move 2 | the reduction to rungs, the rank-five residue, the validated local-formula extraction, and the measured size of the codimension-five problem |
| CP-c93c0010ce8db952 | 2026-09-05 | ktt-positivity-length-five move 3 | the isometry merge of the edge types, and the exact rank computation that closes the data-fitting route for the codimension-five weights |
| CP-ab6345d441118247 | 2026-09-05 | ktt-positivity-length-five move 5 | the Berline-Vergne weight implemented and validated to dimension five, and the codimension-five atlas with its five negative classes realised by explicit hive polytopes |
| CP-2613c3501f780549 | 2026-09-05 | ktt-positivity-length-five move 6 | the reduction of the rung to the extreme rays of the cells of the chamber complex, and 1,347 certified cells, one of them full dimensional |
| CP-78bfc6911cf19f3e | 2026-09-05 | ktt-positivity-length-five move 7 | the cell functional from the local formula, agreeing with the Ehrhart route on 9,145 rays, and 193 certified full-dimensional cells at triples up to size 722,265 |
| CP-54b3d749d5e2d74d | 2026-09-05 | ktt-positivity-length-five move 8 | the residue cut to the cells carrying a negative-weight edge, 332 of 2,199, with the margin measured at 249 and the negative-class count corrected to 21 of 5,142 |
| CP-e959305ef796a2ee | 2026-09-05 | ktt-positivity-length-five move 9 | the discharging rule, the failure of the vertex neighbourhood, and the facet neighbourhood dominating every negative edge in 14,899 tests |
| CP-a87df22c74550dbb | 2026-09-05 | ktt-positivity-length-five move 10 | the per-facet form of the inequality, whose shares sum to the functional exactly, holding in all 46,501 tests with margin at least 17.1 |
| CP-032306798c58d0b3 | 2026-09-05 | ktt-positivity-length-five move 11 | the intrinsic-lattice contraction, which turns the non-full-dimensional rung into the same problem one dimension lower, with the atlas as the only missing input |
| CP-3469cc65d6741516 | 2026-09-05 | ktt-positivity-length-five move 12 | the search that found no failing facet at higher complexity, and the identification of the per-facet negative-edge count, not the cell size, as what moves the margin |
| CP-92219cbb107bdd48 | 2026-09-05 | ktt-positivity-length-five move 13 | the correction that the cell's size acts on the margin through the count rather than not at all, with both effects sized |
| CP-2033bd9f31b6e9e5 | 2026-09-05 | ktt-positivity-conjecture moves 2 and 3 | the rank-uniformity audit, and the exact translation of every coefficient into the binomial basis |
| CP-26ae5b08da7c023a | 2026-09-05 | ktt-positivity-conjecture move 5 | the sign census of the h vectors over the whole box, no negative entry, and the statement of how little that earns |
| CP-8dff598654f5dc84 | 2026-09-05 | ktt-positivity-length-five move 14 | the repair of a truncated mechanism pass and of an extrapolation wrong by four orders of magnitude, with the corrected full-population tables |
| CP-fc310d6db40ac3f2 | 2026-09-05 | ktt-positivity-length-five move 15 | the scalar product as a free parameter, the A_6 form passing the vertex-sum gate, and the weight code validated in dimension six |
| CP-27216bd31dcaae53 | 2026-09-05 | ktt-positivity-length-five move 16 | the form screen: the residue of the weight route drops from twenty-one classes to five, with the module validated at codimension five |
| CP-b2f6b2b9b3ae485c | 2026-09-05 | ktt-positivity-length-five moves 17 and 18 | the zero-row shortcut shown vacuous, the linear program closed with its obstruction, and the weight shown negative already in dimension two |
| CP-8a910f43849d4e75 | 2026-09-05 | ktt-positivity-length-five move 19 | the projected atlas of the non-full-dimensional hives: no negative type at intrinsic dimension three or four, and the session's stopping point with the next steps written down |

## What is proved and what is only measured

The interim directive of 2026-09-05 requires these to be labelled apart. The full ledger, with the
admission record of every bounded computation and the accounting of its runs, is
`attack/ktt-positivity-length-five/ADMISSION.md`. In short:

- Proved, with no sampling in them: the objective is equivalent to the rungs `KTT(r)`, `r >= 5`;
  on a cell of the chamber complex the linear Ehrhart coefficient is a linear functional, so
  nonnegativity on the whole cell is decided at the cell's extreme rays; a cell all of whose edge
  classes have nonnegative weight needs no computation; the local-domination and the per-facet
  inequalities each imply the coefficient is nonnegative, the first by disjointness of shares and
  the second because the facet shares sum to the functional exactly.
- Measured only, exact rational arithmetic over a sample and not coverage of any case: every
  count of cells, rays, facets and margins in the rows above, and the list of 21 negative classes
  among the 5,142 weights held.
- Open, exactly: the rank-five rung for full-dimensional hives, whose residue is the cells that
  carry a negative-weight edge; the rank-five non-full-dimensional hives, now reduced to the same
  problem in the intrinsic lattice with only the atlas missing; and every rung above five. The box
  result of the two finished attacks covers no part of these.
- A caveat on the strongest-looking measurement, and its correction. The per-facet inequality has
  failed none of 252,573 tests, on cells up to 1,127 edges. The per-cell worst ratio does fall
  with the complexity of the cell, from 273.77 to 83.93 in median across the edge-count bands, but
  move 12 showed that this is mostly the order-statistic effect of taking a minimum over more
  facets: at the level of a single facet the median ratio spreads by only 1.60 across an eightfold
  growth of the cell, while it spreads by 4.75 across the number of negative edges on the facet.
  So the quantity the margin depends on is the per-facet negative-edge count, whose observed
  maximum is seven. Nothing proves the inequality, and no number of passing facets can.

## Contribution and failure rules

- A branch result returns to `ktt-positivity-conjecture` with its evidence path, the deduction
  that states what it contributes, and the obligations it leaves. Proving a rung of the ladder
  (for example every triple of length at most 5) leaves every larger length open and does not
  close the objective.
- The two finished attacks contribute negatively: they exclude ranges and classes, and they fix
  the extremal candidates (the polytopes with D + 1 lattice points and normalized volume 2 or 3).
  Their evidence is inherited by reference, and any inherited statement is re-read against the
  new claim before use; the box result is a theorem only for length at most 6.
- Closed routes, with their reason: the data-fitting determination of the codimension-five weights
  (CP-c93c0010ce8db952, `symbolic-computation-run-1`), because each polytope gives one equation
  against hundreds of unknown classes and the classes grow with the sample.
- Closed routes, second: termwise positivity of the Berline-Vergne weight at codimension five
  (CP-ab6345d441118247, `enumeration-run-1`), because five classes that occur as full normal cones
  of edges of explicit five-part hive polytopes have negative weight.
- A failed branch keeps its record and its failure reason. It is revisited only when new
  evidence or a changed assumption addresses the recorded obstruction. The recorded obstructions
  so far: termwise Berline-Vergne positivity fails at codimension 4; sampling cannot reach beyond
  its ranges; no translation in print lands hive polytopes in a family with a positivity theorem.
- A checkpoint is not a cash-out trigger and does not reset a budget. Successor attacks are
  created for a distinct claim, scope or strategy question, never to escape a failure signal.

## Final recombination

The objective is closed only by one of: a proof uniform in the number of parts (the local-formula
or (HTE) route), a counterexample, or an independence result. Rungs of the ladder in the number
of parts accumulate as conditional-or-special-case units and are recombined by the root attack's
statement of what remains open; the current recombination is that the conjecture holds for length
at most 4 at every size (in print), for length at most 6 at size at most 30 (this project), and
for length 7 at size at most 30 relative to one solver.
