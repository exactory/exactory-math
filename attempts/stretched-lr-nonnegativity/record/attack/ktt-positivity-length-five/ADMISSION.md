# Admission record

Governed by `misc/math-solver-interim-directive.md` of 2026-09-05, applied from the moment it was
issued, which was after journal move 10 of this attack. Moves 6 to 10 are classified here after
the fact, as section 7 of the directive requires; nothing is restarted and nothing is discarded.

## The root obligation this attack serves

The root is `ktt-positivity-conjecture`, the complete King-Tollu-Toumazet statement for every
length and every size. Its move 1 reduced it to the rungs `KTT(r)` for `r >= 5`, of which there
are infinitely many. This attack is the rung `r = 5` and nothing more. Proving it leaves every
rung above five open, and the reduction of the root to the rungs is itself proved, not assumed.

Within the rung, Ferudun 2026 settles every coefficient of a full-dimensional five-part hive
except the linear one, so the attack's obligation is exactly two things:

- **O-A**: `a1 >= 0` for every full-dimensional five-part hive polytope.
- **O-B**: every coefficient of every non-full-dimensional five-part hive, by the
  intrinsic-lattice contraction, which is still owed.

## Classification of the work already done

| Move | Step | Category | Which root obligation it serves | What could not proceed without it |
|---|---|---|---|---|
| 6 | `certified-special-case-check-3` | 1, necessary main progression | O-A | The rung had no formulation free of the size of the triple; the reduction to the extreme rays of a cell is what removed it |
| 7 | `enumeration-run-2` | 1, necessary main progression | O-A | The cell functional was computable only through Ehrhart, whose cost grows with the size, so no full-dimensional cell was reachable |
| 8 | `certified-special-case-check-4` | 1, necessary main progression | O-A | The residue was the whole chamber complex; the proved lemma that a cell of nonnegative classes needs no computation is what cut it |
| 9 | `certified-special-case-check-5` | 1, decision-guiding, necessary | O-A | The choice of neighbourhood for a local argument was undecided; the vertex neighbourhood is now excluded by explicit failures |
| 10 | `certified-special-case-check-6` | 1, decision-guiding, necessary | O-A | The local statement had no form whose shares sum to the functional exactly; the per-facet form does |

None of these was reviewed in advance, because the directive did not yet exist. They are recorded
here as executed work with their outcomes, not as approved future work.

### Accounting of runs and retries, as section 5 requires

| Move | Runs launched | Note |
|---|---|---|
| 6 | 6 trial runs and 1 recorded run of `run.py`, 2 runs of `check.sh` | the trials were development of the same bounded task; the second `check.sh` followed a correction of the checker, which had wrongly failed a non-simplicial cell |
| 7 | 3 trial runs and 1 recorded run, 3 runs of `check.sh` | the checker was corrected twice: once to bound the hive enumeration, once to add the closed-formula check on the newly computed weights |
| 8 | 1 trial run and 1 recorded run, 1 run of `check.sh` | |
| 9 | 1 trial run and 1 recorded run, 1 run of `check.sh` | the trial measured only the vertex neighbourhood; the recorded run measured both |
| 10 | 1 trial run and 1 recorded run, 1 run of `check.sh` | |

No job was run outside the journal to gain a move. Every run belongs to the move that names its
step, and no move was started before the previous one was journalled.

## What is proved and what is measured

Proved, as mathematical statements with no sampling in them:

- **P1** (root move 1): the objective holds if and only if every rung `KTT(r)`, `r >= 5`, holds.
- **P2** (move 6): on a cell of the chamber complex `a1` is a linear functional of the boundary
  triple, so `a1 >= 0` on the whole cell if and only if that functional is nonnegative at the
  cell's extreme rays; and the cells are finite in number.
- **P3** (move 8): the lattice length of an edge is nonnegative on the cell, so a cell all of
  whose edge classes have nonnegative weight satisfies `l >= 0` with no computation.
- **P4** (move 9): the shares of distinct negative edges are disjoint parts of the positive sum,
  so the local domination statement implies `l >= 0`.
- **P5** (move 10): the facet shares add up to the functional exactly, so the per-facet
  inequality implies `l >= 0`.

Measured, exact rational computation over a sample, and not a proof of anything universal:

- **M1** (moves 5 and 8): 21 negative classes among the 5,142 weights held.
- **M2** (moves 6 and 7): 2,199 cells, 13,909 extreme-ray evaluations, none negative.
- **M3** (move 8): 332 of 2,199 cells carry a negative-weight edge; margin at least 249.
- **M4** (move 9): the vertex neighbourhood fails 106 of 14,899 tests; the facet neighbourhood
  fails none, with margin at least 83.6.
- **M5** (move 10): the per-facet inequality fails none of 46,501 tests, with margin at least
  17.1.

No measurement above is offered as coverage of any part of the objective. The proved statements
P1 to P5 are reductions; they do not by themselves settle any case.

## Open obligations, exactly

- **O-A** is open. Its residue is: the cells that carry an edge of a negative-weight class. The
  per-facet inequality would discharge it, and is unproved.
- **O-B** is open and untouched.
- The root's rungs `r >= 6` are open and untouched.

## Proposal awaiting review

**Target.** For each facet type occurring among the facets already built, compute exactly the cone
of edge-length vectors the facet can take as the boundary triple ranges over the cell, and decide
the per-facet inequality on the whole of that cone rather than at the ambient cell's rays.

**Category.** 1, necessary main progression, and a decision-guiding experiment.

**The blocked decision.** Whether the per-facet inequality is a statement about a facet type at
all. If the inequality holds on the whole length cone of a type, the statement is type-by-type and
a full enumeration of facet types becomes the route to O-A. If it holds at the achievable rays but
fails elsewhere on the length cone, the type data is not sufficient and the cell must re-enter the
statement. If it fails outright, the per-facet route is dead.

**What cannot proceed without it.** The per-facet route has no proof path until this is decided,
and the alternative is to enumerate the cells carrying a negative-weight edge, whose number is
unknown.

**Why the finite domain is sufficient.** The question is about the form of the statement, not
about coverage. A single type whose length cone breaks the inequality settles the decision
negatively; agreement across the types seen supports the type-by-type form without proving it.

**Outcomes and continuations.** Holds on every length cone: continue by enumerating the facet
types of a five-part hive polytope, which is the coverage task for O-A. Holds only at achievable
rays: retreat to the cell-level residue of move 8 and look for the extra constraints the cell
imposes. Fails: record the failure, retreat to the checkpoint of move 8, and take the cell
enumeration instead.

**Checkpoint condition.** A per-type verdict with counts and the worst ratio on the length cone.

**Retreat condition.** A single type whose length cone breaks the inequality, or the length-cone
computation exceeding the allowance.

**Finite resource allowance.** One run, at most 45 minutes of wall time, single threaded, plus one
checker run and at most two corrections of the checker.

**Independent review.** Requested 2026-09-05, one reviewer, as section 2 requires for a main
progression proposal. Not self-approved. The decision and its reasoning are appended below when
the reviewer reports; until then no new computation is launched for this proposal.

## Amendment of 2026-09-05, before any run, on new evidence from the existing records

Re-reading `certified-special-case-check-6/facets.jsonl`, which is recorded output and needed no
new run, the margin of the per-facet inequality is not stable. Grouped by the number of edges of
the cell:

| edges | cells | worst ratio of positive share to negative share |
|---|---|---|
| about 64 | 27 | 157.07 |
| about 128 | 131 | 222.27 |
| about 256 | 101 | 22.51 |
| about 512 | 73 | 17.12 |

The small cells built at box triples have worst ratio 157.07 and median 325.36; the large cells
built at generic triples have worst ratio 17.12 and median 100.54. So the margin falls by about an
order of magnitude as the edge count grows eightfold, and the eight tightest cases are all among
the largest cells.

This weakens the reading of move 10. "No failure in 46,501 tests" was true, and it stays true, but
it is not evidence that the inequality holds with room to spare: the room shrinks with the
complexity of the cell, and nothing measured bounds it away from one.

**The proposal above is therefore withdrawn in its stated form and replaced.** Deciding whether
the inequality is a statement about a facet type is the wrong first question while it is not known
whether the inequality survives at all at higher complexity.

### Replacement proposal awaiting review

**Target.** Search for a cell whose per-facet inequality fails, by driving the cell complexity up:
sample cells with as many edges as the vertex cap allows, measure the worst per-facet ratio, and
record the trend against the edge count.

**Category.** 1, necessary main progression and decision-guiding.

**The blocked decision.** Whether the per-facet route to O-A is viable. The route rests on an
unproved inequality whose measured margin is falling with complexity.

**Outcomes and continuations.** A failing facet refutes the per-facet form; the route is dead, the
proved sufficiency of move 10 stands but is vacuous, and the retreat is to the residue of move 8,
which is unaffected. A margin that stops falling, or falls to a positive limit, supports the
inequality and makes the type-level question the next one. A margin that keeps falling without a
failure decides nothing and the allowance ends the task.

**What cannot proceed without it.** Investing in the facet-type enumeration, which is the
expensive coverage task for O-A, cannot be justified while the inequality itself is in doubt.

**Why the finite domain is sufficient.** One failing facet settles the decision negatively and is
a complete answer. No amount of passing cells proves the inequality, and the record will say so.

**Checkpoint condition.** Either a failing facet with its cell and triple, or a recorded trend of
the worst ratio against the edge count over at least three complexity bands.

**Retreat condition.** The allowance is spent with no failure and no stabilised trend.

**Finite resource allowance.** One run, at most 40 minutes of wall time, single threaded, plus one
checker run and at most two corrections of the checker.

**Independent review.** The reviewer of the withdrawn proposal has been sent this amendment and
judges the replacement. Not self-approved. No computation is launched until the decision is
recorded here.

### A prediction the replacement proposal must be judged against

Stated before any run, so that the experiment decides something rather than observing a pattern.

The recorded worst ratio falls from 157.07 at cells of about 64 edges to 17.12 at about 512, a
factor of 9.2 while the edge count grows by 8. The median worst ratio falls from 325.36 on the
small cells to 100.54 on the large ones, a factor of 3.2 over the same range. Two readings are
possible and the run must separate them.

- **Extreme-value reading.** The minimum is taken over more facets in a larger sample, so the worst
  case falls without the underlying quantity moving. Against this reading stands the fall of the
  median, which is not an order statistic of that kind.
- **Trend reading.** The negative share grows with the number of negative edges on a facet while
  the positive share does not keep pace, so the ratio falls roughly as the inverse of the edge
  count. On that reading a cell of about 5,000 edges has ratio near one and a cell of about 10,000
  edges fails.

The proposal therefore predicts: pushing the edge count from about 500 to a few thousand either
produces a failing facet, which refutes the per-facet form, or shows the ratio levelling off,
which refutes the trend reading and leaves the extreme-value reading. Either outcome decides the
route. A run that neither fails nor levels off spends the allowance and is recorded as
undecided, not as support.

The vertex cap of 220 used in `enumeration-run-2` bounds the edge count, so raising it is part of
the proposal and is the reason the allowance is stated in wall time rather than in cells.

## Tasks left open in the harness but superseded

The harness action list still carries two items that later moves made moot. They are left open
rather than marked done, because they were never carried out, and they are recorded here so that
a resumed session does not take them up again.

- Task 7, the vertex-sum identity as a cheap source of equations for the codimension-five weights.
  Superseded by move 3, which closed the data-fitting route by an exact rank computation, and by
  move 5, which computed the weights directly from the recursion instead of fitting them.
- Task 9, the rank-five instance of Ferudun's (HTE) as a finite linear program. Superseded by move
  6, which changed the route: the termwise question about a single local formula stopped being the
  bottleneck once the rung was reduced to the extreme rays of a cell. The question itself remains
  open and unanswered, and is not claimed either way.

## Independent review, 2026-09-05, and the record it corrects

One reviewer, as section 2 requires for a main-progression proposal. Verdict on the withdrawn
proposal: **REJECT**. Verdict on the replacement: **ACCEPT WITH AMENDMENTS**, nine of them. The
findings below are the reviewer's; the responses are this record's.

### The withdrawn proposal was vacuous, not merely mistimed

The reviewer's reason is decisive and is recorded so that nobody proposes the same computation
again. For a fixed cell `C` with extreme rays `r_1, ..., r_k` and a fixed facet `F`, the map
`b -> (len_e(b))_e` is linear, so the set of length vectors `F` takes as `b` ranges over `C` is
exactly `cone(L(r_1), ..., L(r_k))`. The per-facet inequality is a linear functional of that
vector, so it holds on the whole of that cone if and only if it holds at the images of the cell's
rays, which is what `certified-special-case-check-6` already tested at every ray of every built
cell. Taking a union over cells of one type changes nothing, a linear functional nonnegative on
finitely many cones being nonnegative on their conic hull. So both of the withdrawn proposal's
negative branches were unreachable and its outcome was fixed in advance at zero failures. The
amendment above credited it as a sound question mistimed; that was too kind and is corrected here.

### Corrections to the claims this record made

1. **"Order of magnitude" was overstated.** The worst ratio is a minimum and falls with the number
   of tests in a band by construction. The four bands carry 545, 3,203, 17,394 and 25,359 facet
   ray tests. The per-band medians, which carry no such bias, are 273.77, 325.36, 120.83 and
   83.93, a factor of about 3, not of ten. The effect is real and smaller than stated.
2. **The trend is confounded.** All 159 low-band cells come from `certified-special-case-check-3`,
   built at box triples with cell ranks 3 to 8; all 173 high-band cells come from
   `enumeration-run-2`, built at generic triples with rank 14. Edge count, cell rank and
   construction route move together in this data and cannot be separated by regrouping it.
3. **"Vacuous" was the wrong word** for what a failing facet would do to move 10. The implication
   P5 stays true and its hypothesis is met by every cell measured, so it remains a valid
   sufficient condition wherever it holds; what a failure removes is its use as a universal proof
   of O-A.
4. **The retreat set was incomplete.** Move 9's facet-neighbourhood domination is a different
   grouping, proved sufficient by P4, with a larger measured margin, 83.6 over 14,899 tests. A
   move-10 failure does not touch it. The retreat is therefore to move 9's grouping first and to
   move 8's residue second, and move 8's residue is unenumerated and of unknown size, so it is a
   retreat to a place with no route rather than to a prepared successor.
5. **The banding rule** used above is the floor power of two of the cell's edge count, over the
   332 cells that carry a negative edge. The reviewer reproduced the table exactly from
   `facets.jsonl`.

### Corrections to the record itself

6. Move 11 was not in the classification table. It is added below.
7. The move-11 journal entry says its O-B proposal "is recorded as a proposal in `ADMISSION.md`".
   At the time it was not; only harness task 15 named it. The journal is harness-owned and is not
   edited, so the discrepancy is recorded here and the proposal is written below, which makes the
   claim true from now on.
8. The reviewer read `SEARCH_TREE.md` before its move 10 and move 11 updates and reported it two
   moves stale. It was brought current during the review and now carries both moves, the
   checkpoint for move 10 and the caveat on the margin.
9. One reviewer statement needs correction in the other direction. `enumeration-run-2` recorded no
   Ehrhart cross-check inside the run, because every swept triple exceeded the size cap; but its
   checker did cross-check ten of those same phase-B cells against the Ehrhart quasi-polynomial at
   their ray sums, with no mismatch. The step therefore has ten independent Ehrhart checks of
   phase-B cells, not none.

### Classification of move 11

| Move | Step | Category | Which root obligation it serves | What could not proceed without it |
|---|---|---|---|---|
| 11 | none, a derivation | 1, necessary main progression | O-B | The non-full-dimensional half of the rung had no statement at all; it is now the same problem in the intrinsic lattice, with only the atlas missing |

### The amended proposal, as approved

Category 1, decision-guiding. Target: a facet whose per-facet inequality fails, sought where the
margin is smallest. Amendments 1 to 8 of the review are incorporated as follows.

- **Checkpoint condition.** Either a failing facet, reported with its cell, triple, facet and the
  ray that breaks it, or at least one new complexity band strictly above the current top band,
  that is cells of more than 684 edges, containing at least 20 cells and at least 2,000 facet ray
  tests. The four existing bands do not count.
- **Statistics.** Per band, over old and new data together: cells, facet ray tests, worst ratio and
  median ratio. The median is the headline; the minimum is reported beside it and is not used
  alone.
- **Confounding.** High-edge cells are built from both sources, perturbations of box triples and
  generic points of the hive cone, so that edge count and construction route are separated. If the
  run cannot produce high-edge cells from the box-triple side, the record says the trend cannot be
  attributed to complexity alone.
- **Targeting.** The search starts from the eight recorded tightest cells, of 364 to 666 edges, and
  their facets, and records per tested facet the number of negative edges on it and their classes,
  which `facets.jsonl` does not carry today.
- **Retreat.** Move 9's facet-neighbourhood grouping first, move 8's unenumerated residue second.
- **Allowance.** One run of at most 40 minutes of wall time, single threaded, with a vertex cap
  raised from 320 to 600, plus one checker run and at most two corrections of the checker. Trial
  and development runs count against the 40 minutes. Expected yield at that cap, extrapolating
  from the 2,242 seconds `enumeration-run-2` spent for 193 cells at cap 320 and from the quadratic
  cost of edge enumeration, is tens of cells rather than hundreds. A no-hit outcome does not
  replenish the allowance and is recorded as undecided.
- **What is not claimed.** No number of passing facets proves the inequality.

### The O-B proposal, awaiting review

**Target.** Enumerate the transverse cone types of edges of five-part hive polytopes of intrinsic
dimension 3, 4 and 5 in the projected lattice, and decide the signs of their weights.

**Category.** 2, exact proof coverage: success discharges obligation O-B outright for the
dimensions where the weights are nonnegative, and identifies exactly the residue where they are
not, without weakening any statement.

**Which root obligation.** O-B, the non-full-dimensional half of the rank-five rung.

**What cannot proceed without it.** O-B has no residue at all until the list exists; move 11
reduced the problem to it and stopped there.

**Why the finite domain is sufficient.** The list is the complete set of types that occur, not a
sample, for the dimensions enumerated; a type that occurs and has negative weight is a genuine
part of the residue and a dimension whose types are all nonnegative is discharged.

**Outcomes.** All weights nonnegative at a given intrinsic dimension: that dimension of O-B is
closed by the nonnegative-class lemma. Some negative: the residue is those types, and the
machinery of moves 8 to 10 applies to them unchanged.

**Checkpoint condition.** A per-dimension verdict with the type counts and the sign census.

**Retreat condition.** The enumeration at intrinsic dimension 5 exceeding the allowance, in which
case dimensions 3 and 4 are reported alone.

**Finite resource allowance.** One run of at most 60 minutes, single threaded, plus one checker
run. Trial runs count against it.

**Independent review.** Not requested yet. Not started.

## Second independent review, 2026-09-05, and the predictions registered before the results

The reviewer was sent the prediction section and returned ACCEPT WITH AMENDMENTS again, with nine
amendments and one correction of its own earlier report. This is written while
`enumeration-run-3` is running and before any band table from it has been read.

### What the reviewer established from the recorded data

- **The clean statistic obeys an inverse law almost exactly.** Median edge count 148 with median
  per-cell worst ratio 325.36 on the `certified-special-case-check-3` cells, against 486 and
  100.54 on the `enumeration-run-2` cells: the edge count rises by 3.28 and the ratio falls by
  3.24, so the product is 48,153 against 48,862, constant to two percent. The median is immune to
  the order-statistic objection, so the trend reading is supported on the statistic that matters.
- **The order-statistic effect is real on top of it.** The worst-to-median gap widens with the
  number of tests in a band: 1.74, 1.46, 5.4, 4.9 against 545, 3,203, 17,394 and 25,359 tests. So
  the two readings are not exclusive; both are present, and this record's earlier framing of them
  as a choice was wrong.
- **The failure prediction was an extrapolation of the contaminated statistic.** Worst ratio 17.12
  at 632 edges gives worst times edges about 10,800 and predicts failure near 10,000 edges; the
  clean statistic predicts the median reaching one only near 48,000 edges. The nearer figure was
  the wrong one to plan against.
- **That target is unreachable.** Edges scale as about 3.7 times the vertex count, so 5,000 edges
  needs about 1,150 vertices and 10,000 about 2,265, against 220 actually reached, with the edge
  pass quadratic in the vertex count. Forty minutes will not get there.
- **A third reading, provenance.** Every low-band cell is a rank 3 to 8 cell from
  `certified-special-case-check-3` and every high-band cell a rank-14 cell from
  `enumeration-run-2`, so the ratio may track cell rank or construction route rather than edge
  count.
- The reviewer withdrew its own earlier figure of a vertex cap of 320; the recorded cap was 220
  and the maximum vertex count over all 2,199 cells is exactly 220.

### Registered before the results are read

The running step builds cells in the band the reviewer identifies as discriminating, about 240 to
400 vertices and roughly 900 to 1,500 edges; the first cells it has produced are at 865 and 983
edges, and no band table has been computed yet.

- **Trend reading predicts** the band median near 40, that is the product of the median and the
  edge count staying near 48,500.
- **Extreme-value reading predicts** the band median staying near 100, with only the minimum
  drifting downward.
- **Provenance reading predicts** the band median tracking the cell rank rather than the edge
  count, so that high-edge cells built from perturbed box triples behave differently from
  high-edge cells built at generic points. The run builds both, so this is testable.
- A band median between 40 and 100 separates nothing and is recorded as undecided.

### Amendments incorporated, and the one that follows this run

Amendments on statistics, provenance, targeting, the retreat set and the wording are incorporated
here and in the step's own record; the failure target of 5,000 to 10,000 edges is dropped as a run
target and kept only as the statement of where the trend reading predicts failure. The banding
rule is the floor power of two of the cell's edge count. The vertex cap of this run is 600. Trial
runs count against the allowance, and this step had none: the script was written once and launched
once. An undecided outcome does not replenish the allowance.

The reviewer's cheapest decisive test is amendment 2 and it is not in the running step: re-run the
facet pass over the 2,199 cells already built while recording, per tested facet, the number of
negative edges on it, their classes and both shares. `facets.jsonl` carries no per-facet detail
for passing facets, so the trend reading's stated mechanism, that the negative share grows with
the number of negative edges on a facet, has never been tested and the extrapolation rests on a
proxy variable. It costs about eight minutes against the 478 seconds the whole facet pass took.
**It is added to this move's allowance as a second phase, to be run immediately after the first,
inside the same forty minutes.**

### Corrections to the wording, as required

"The proved sufficiency of move 10 stands but is vacuous" is withdrawn wherever it appears above.
The correct statement: a failing facet would show that the per-facet inequality is not universally
true, so it cannot prove O-A, while remaining a valid sufficient condition on every cell where it
holds. The retreat set in full: move 9's facet-neighbourhood domination, proved sufficient by P4
with margin 83.6 over 14,899 tests, survives a move-10 failure and is the first retreat; move 8's
residue is the second, and it is unenumerated and of unknown size.

## Proposal for move 14, awaiting review: change the weight rather than the argument

**Where this comes from.** Every route the attack has taken since move 8 works around the same
twenty-one negative classes: the discharging rule, the facet neighbourhood, the per-facet
inequality, the counting of negative edges per facet. All of them accept the Berline-Vergne weight
as given and argue that the positive weights outweigh it. There is a different move available. The
nonnegative-class lemma P3 says that if every class has nonnegative weight then the coefficient is
nonnegative on every cell with no computation at all. So the question is whether some other valid
local formula has no negative class.

**The concrete family.** The Berline-Vergne construction takes a positive-definite scalar product
on the ambient space and builds the weight from orthogonal projections with respect to it. The
project's own tool takes exactly that as input: `tools/bvweight.py` computes the weight from a set
of rays and a Gram matrix. Varying the Gram matrix therefore walks a family of weight assignments
at no new implementation cost. Whether every member of that family is a valid local formula is the
first thing the run must establish, not assume, and the test is the one the project already has:
the local formula must reproduce the certified linear coefficient of hive polytopes exactly.

**Target.** For the twenty-one classes of negative Berline-Vergne weight, and for the 5,142 classes
the project holds, decide whether a single positive-definite form on the rank-six lattice makes
every weight nonnegative, or show that the negativity of some class is invariant along the family.

**Category.** 1, necessary main progression. Success closes the full-dimensional half of the
rank-five rung outright through P3, with no cell, no facet and no counting. Failure of the whole
family is a barrier statement about the Berline-Vergne construction and redirects the attack to
the local formulas that are not of that form.

**The blocked decision.** Whether to keep working around the negative classes or to remove them.
Every move from 8 to 13 has been the former, and the record has never asked the latter.

**What cannot proceed without it.** Nothing in the current route is blocked; this is an
alternative that would make the current route unnecessary, which is why it is worth the move
rather than a further refinement of the counting.

**Why the finite domain is sufficient.** One form that makes all held weights nonnegative is a
complete answer for the classes held; one class whose weight stays negative for every form tested
is evidence and not a proof of invariance, and the record will say which.

**Outcomes.** A form with no negative class: verify it reproduces certified coefficients, then P3
closes the residue for every cell whose classes are held, and the remaining obligation becomes the
completeness of the class list rather than the sign of the weights. Some class negative for every
form tested: record the search extent and return to the per-facet route with a barrier note. The
validity test failing for forms other than the standard one: the family is not available and the
proposal ends there, which is itself worth knowing.

**Checkpoint condition.** A validity verdict for a non-standard form, and a sign census over the
twenty-one negative classes for the forms tested.

**Retreat condition.** The validity test fails for every non-standard form, or the allowance is
spent without a sign change.

**Finite resource allowance.** One run of at most 30 minutes, single threaded, trials counted; one
checker run and at most two corrections.

**Independent review.** Requested. Not self-approved. No computation until the decision is
recorded here.

### Two facts established before the review returns, one of which is a cost the proposal omitted

**The code supports it.** `tools/bvweight.py` takes the Gram matrix as an argument and does its
projections with respect to it (`_Proj`, "orthogonal projection onto the complement of a span,
with respect to a Gram matrix"), so varying the form costs no implementation.

**The classification does not.** The 8,305 edge types were collapsed to 3,406 classes by the
isometries of the standard form, the signed permutations of the six coordinates, because the
Berline-Vergne weight is invariant under them. A form invariant under every sign flip has zero
off-diagonal entries, and one invariant under every coordinate permutation has a constant
diagonal, so the only signed-permutation-invariant forms are the multiples of the standard one,
and the weight is unchanged by scaling. Therefore **any form other than the standard one destroys
the collapse**: under it the weight is a function of the type, not of the class, and the type list
is larger and open, whereas the class list was finite and cheap.

That is a cost the proposal did not state. It does not kill the route, because the twenty-one
negative classes have explicit representative cones and the cheap decisive question is whether one
form makes those twenty-one nonnegative at all, but it changes what a positive answer would mean:
it would remove the negativity for the representatives, not for every type in their classes, and
the obligation of checking the types would then replace the obligation of checking the classes.
The proposal is amended to say so, and its target is narrowed accordingly: decide first whether a
single form makes the twenty-one representative cones nonnegative while keeping a sample of the
currently-positive ones positive. If it cannot, the route ends cheaply and the answer is
independent of the classification question.

### A third fact, which bounds what any such search can hope for

No local formula has nonnegative weights on all cones. If one did, then for every lattice polytope
every Ehrhart coefficient would be a sum of nonnegative terms and so nonnegative, and that is
false: Reeve's tetrahedron with vertices at the origin, `(1,0,0)`, `(0,1,0)` and `(1,1,r)` has
`h*` equal to `(1, 0, r-1, 0)`, so its linear coefficient is `(12 - r)/6`, negative for every
`r > 12`.

So the question the move-14 proposal asks is not whether some formula is nonnegative everywhere,
which is settled in the negative, but whether some formula is nonnegative on the cones that occur
as transverse cones of edges of five-part hive polytopes. That is the right question and it is
what the proposal tests, but it means a positive answer can never come from a general theorem
about local formulas; it has to come from the hive cones being special. The record states this so
that a positive result is not over-read and a negative one is not treated as surprising.

### A fourth fact, from a two-second check on a toy cone

The weight does move with the form, so the family is not trivial. The standard orthant in
dimension three has weight `1/8` under the standard form, which is the known value `2^-d` for a
unimodular cone, and `5/24` under the positive-definite form with diagonal 2 and first
off-diagonals 1. The check used `tools/bvweight.py` on a three-dimensional cone and is recorded
here as accounting rather than as a run.

## Third independent review, 2026-09-05: two defects in executed work, and eleven amendments

Verdict on move 14 as narrowed: ACCEPT WITH AMENDMENTS. The reviewer also audited the executed
moves 12 and 13 and found two defects, both now repaired.

### Defect one, repaired: the mechanism pass was truncated and the record did not say so

`refacet.py` stops at a time budget. Its first pass covered 2,119 of the 2,199 cells, omitting the
last 80, all from `enumeration-run-2` and all among the largest, which carry 664 of the 2,556
facets that hold a negative edge. So the tables that retired the complexity alarm omitted 26
percent of the relevant facets, and exactly the ones where the counts are highest. The step's own
checker regrouped the same truncated file and could not catch it.

Repaired by re-running over all 2,199 cells, 478 seconds. The truncated files are kept as
`per-facet.truncated.jsonl` and `per-facet.truncated.summary.json`. The conclusion is unchanged
and slightly stronger: the median ratio spreads by 6.20 across the per-facet negative-edge count,
against 4.75 on the truncated data, and by 1.55 across an eightfold growth of the cell, against
1.60. The step was re-verified and passes.

### Defect two, repaired: the extrapolated failure point was wrong

The addendum said a cell of order ten million edges. Under the addendum's own fits that is not
what follows: the median margin reaches one at a per-facet count of order 800, and a cell whose
mean count is 800 has of order `2 x 10^11` edges. The ten-million figure came from extrapolating
the worst ratio, which the same document calls an order-statistic artefact. It is withdrawn and
the README now carries the corrected figure, the fit exponents, the ranges the fits are extended
beyond, and the two bins that contradict the trend.

### The eleven amendments to move 14, accepted

1. Name the forms in an ordered finite list before the run: the standard form, the Gram matrices
   of `A_6`, `D_6`, `E_6`, `A_1^6` and their duals, plus stated rational sample points on one or
   two one-parameter paths through the standard form, with a stated stopping rule.
2. Replace "any form other than the standard one destroys the collapse" with the correct
   statement: the collapse by signed permutations is replaced by the collapse under the
   automorphism group of the new form, which is still large for a root-lattice form, `2 * 7!` for
   `A_6` against `2^6 * 6!` for the standard one. That is the reason to choose forms from a named
   list.
3. Gate every candidate form first on the vertex-sum identity, that the weights of the tangent
   cones at the vertices of a lattice polytope sum to one, which is exact and needs no Ehrhart
   computation. That is the project's own superseded task 7. The hive-polytope reproduction test
   is the second gate. Both are necessary and neither is sufficient.
4. Cite the statement in Berline-Vergne that the construction is valid for an arbitrary
   positive-definite form, and check its hypotheses cover rational forms. Do not infer validity
   from the code accepting a Gram matrix.
5. Confirm scale invariance once on a toy cone, since the classification argument rests on it.
6. Specify the positive control as the classes carrying the smallest positive weights held, not a
   random sample, because the negative weights and the smallest positive ones are the same size.
7. Delete "failure of the whole family is a barrier statement about the Berline-Vergne
   construction". A finite sample of a 21-parameter continuum cannot earn it. On failure the
   record may say only that no form in the recorded list works, with the list attached.
8. Register the (HTE) linear program over the whole affine space of local formulas as the
   follow-on that decides what move 14 only probes. It is the project's superseded task 9 and is
   still open and unanswered.
9. Rerun the mechanism pass over all 2,199 cells. Done.
10. Correct the ten-million-edge figure. Done.
11. State the range of every extrapolation beside it. Done.

### The root proposal, as amended

The reviewer cut it to about a quarter. Three of its four tests decide nothing: the asymmetry
inequality is equivalent to the linear coefficient being nonnegative, which the box attack already
certified with two independent programs on this very data, so testing it can only return a pass;
monotonicity is a statement about nested pairs and no pairs are named; Hibi's bound needs a lattice
polytope with an interior point and no decision was stated to hang on it. Only the sign test on the
`h` vector decides anything.

The reviewer also corrected the description of the work: the box attack's
`certified-special-case-check-4/census.py` already computes the full `h` vector of every one of
the 6,855,302 polynomials by exactly the proposed formula, in a run of 796 seconds on 2026-09-04,
and never tests an entry for negativity. Verified here: the file's own header states the formula
and `hstar(coeffs)` is called on every record. So the honest task is to add a sign test and a
minimum-entry field to an existing, independently checked script and re-run it.

Two further corrections enter the root's record. Stanley's theorem gives `h >= 0` unconditionally
for lattice polytopes, so records whose hive polytope happens to be a lattice polytope carry no
information, and a fully nonnegative census is therefore weaker evidence than it looks. And "no
retreat condition needed" is not acceptable: the retreat names the result that sends the work back
to a checkpoint, not the possibility of non-termination.

### Amendment 4 discharged: the citation for an arbitrary rational positive-definite form

Berline and Vergne, "Local Euler-Maclaurin formula for polytopes", arXiv:math/0507256, state the
construction for polytopes in a "rational euclidean space" and build, for every affine rational
polyhedral cone in such a space, the differential operator the formula sums over. The hypothesis
is a rational euclidean structure, not the standard one, so any rational positive-definite form is
admissible and the forms this move uses are rational. The citation is the abstract of the paper as
retrieved on 2026-09-05; the paper's own numbered statement was not read, so the record carries
this as the cited hypothesis rather than as a verified theorem number, and the vertex-sum gate
tests it empirically for each form actually used.

### Move 15 in progress under the approved allowance

Gate one, the vertex-sum identity, is running on four forms: the standard one, twice the standard
one as a control for scale invariance, the `A_6` root-lattice form, and the form with unit diagonal
and every off-diagonal entry one quarter. Each form is tested on the unimodular six-simplex, seven
tangent cones, and on the unit six-cube, sixty-four signed orthants. A six-dimensional weight costs
about 6.3 seconds, so a form costs about seven minutes, and the allowance is stated in wall time.

## Proposal for move 16, awaiting review: the twenty-one classes under a non-standard form

The gate of move 15 is passed, its allowance is spent, and the next phase is a separate run.

**Target.** Evaluate the twenty-one negative-class representative cones, and a positive control
drawn from the classes carrying the smallest positive weights held, under the `A_6` form and under
any other form that passes the gate. Record the full sign vector for each form.

**What has to be built first.** The transverse cone of an edge is metric-free as a cone with a
lattice, but the identification used by `tools/transverse.py` places it in the standard orthogonal
complement of the span of the normals and equips it with the standard Gram. Under a form `Q` the
complement and the Gram are both `Q`-dependent, so the module needs a `Q`-aware version. That is
implementation, not a run, and it is written before the allowance starts.

**Category.** 1, necessary main progression, continuing the programme move 15 opened.

**The blocked decision.** Whether the negativity of the twenty-one classes is an artefact of the
standard scalar product. A form that lifts all twenty-one without pushing the control negative is
the first evidence that it is; a form that lifts none of them, or that trades one for another, is
evidence that it is not.

**Why the finite domain is sufficient.** One form that lifts all twenty-one while keeping the
control positive is a complete answer for those representatives. It is not an answer for their
classes, because a non-standard form breaks the collapse, and the record already states that the
obligation to check types would then replace the obligation to check classes.

**Outcomes.** All twenty-one lifted with the control intact: proceed to the type-level question and
to the hive-polytope reproduction test, which is the second gate. Some class negative for every
form tried: record the list of forms and stop; no claim about the family may be made from a finite
sample of a twenty-one-parameter continuum. A form that lifts some and pushes the control negative:
record the trade, which is itself informative about how tight the weights are.

**Checkpoint condition.** A sign vector over the twenty-one negatives and the control, for every
form tried, with the forms listed.

**Retreat condition.** No form in the list lifts even one of the twenty-one, or the allowance is
spent before the first form is complete. Either returns the attack to CP-fc310d6db40ac3f2 and to
the per-facet route.

**Finite resource allowance.** One run of at most 30 minutes, single threaded; trial runs of the
new module count against it; one checker run and at most two corrections.

**Independent review.** Requested.

## Proposal registered but not yet written up: the linear program over all local formulas

Amendment 8 of the second review and amendment 8 of the third both require this to be registered
as the follow-on that decides what the form family only probes. It is the project's superseded
task 9. The affine space of local formulas at codimension five is larger than the curved
twenty-one-parameter family the form search walks, and the linear program over it decides both
branches: feasible gives an explicit valid formula nonnegative on the hive cones and closes the
residue through the nonnegative-class lemma; infeasible is the genuine barrier for the whole class
that the form search cannot deliver. It needs its own admission record, its own review, and a
statement of how the space of differences is to be represented, which move 3 of this attack found
to be the hard part when it closed the fitting route. It is registered here and is not started.

### How the space of differences would be represented, which is what the linear-program proposal owed

Written as a derivation, so that the proposal can be judged rather than deferred again.

A local formula at codimension `c` assigns a number to each transverse cone type of dimension `c`,
and it is valid when for every lattice polytope `P` the sum over the codimension-`c` faces of the
weight times the relative volume is the corresponding Ehrhart coefficient. Two valid formulas
differ by a `delta` with

    sum over the codimension-c faces F of P of  delta(t(P,F)) * vol(F)  =  0   for every P.

At `c = 5` the cones in question are five-dimensional in a rank-five lattice, and those are exactly
the tangent cones at the vertices of five-dimensional lattice polytopes, where the relative volume
of a vertex is one. So the relations specialise to

    sum over the vertices v of Q of  delta(tangent cone at v)  =  0,  for every five-dimensional
    lattice polytope Q,

which needs no Ehrhart computation and no volume. Relations are generated constructively: given a
five-dimensional cone with primitive rays, choose a linear functional positive on it and cut at a
height that makes the intersections lattice points; the result is a lattice simplex one of whose
vertex cones is the given cone and whose other five vertex cones are new types, each of which
enters the variable set.

**The logic this gives, and its direction.** The generated relations are a subset of all the
relations that define the difference space, so the linear program built from them has a feasible
set at least as large as the true one. Therefore:

- infeasible on the generated relations implies infeasible on the whole difference space, which is
  a genuine barrier for every local formula at codimension five, not only for the Berline-Vergne
  family;
- feasible on the generated relations gives a candidate that satisfies the relations used and may
  fail others, so it is not by itself a valid formula and does not close the rung.

That asymmetry is the reason the linear program is worth running and it is the reason its positive
branch must not be over-read. The record's earlier phrasing of this task, in the superseded task 9,
said "feasible gives the rung", which is wrong for exactly this reason and is corrected here.

The variable set grows as relations are generated, since each truncation introduces five new
types, so the program is finite only once a generation budget is fixed. That budget, and the rule
for choosing which cones to truncate, are what the proposal must state before it can be reviewed.

## Fourth and fifth independent reviews, 2026-09-05: move 16 accepted, the linear program not yet reviewable

### Move 16, ACCEPT WITH AMENDMENTS, seven of them

1. **Reverse the order.** Screen all named forms on the twenty-one representatives and the control
   first, which costs about two minutes per form because these are five-dimensional cones, and
   gate only the forms that lift all twenty-one, because the gate costs about seven and a half
   minutes per form at dimension six. Record explicitly that a lift under an ungated form is not
   evidence until that form passes the gate.
2. **Two exact checks before any recorded result from the new module.** Reproduction of a stated
   sample of the 5,142 recorded weights under the standard form; and the codimension-five identity
   on the unimodular six-simplex, whose Ehrhart polynomial is `C(t+6,6)` so that the sum over its
   twenty-one edges of the transverse-cone weight times the lattice length is `H_6 = 49/20`, run
   under the standard form and under each form used. The second exercises the new path at the
   right codimension against a known closed answer.
3. **The vertex-sum gate does not validate the new module.** It sums full-dimensional tangent cones
   at codimension six; the twenty-one classes are codimension-five transverse cones obtained by
   projecting out the span of the normals. The gate validated the path that is not changing.
4. **The retreat trigger becomes**: no gated form lifts all twenty-one with the control intact. A
   form that lifts twenty of twenty-one leaves the residue exactly where it was, so the earlier
   trigger was too permissive to be a retreat.
5. **A success costs more than the proposal said.** A form lifting all twenty-one still requires
   re-evaluating the other 5,121 held classes under it, since a form that lifts some can push
   others negative. At about a second per five-dimensional class that is on the order of an hour
   and it sits outside this allowance.
6. **Of move 15's four forms exactly one is a usable non-standard form.** The standard form is the
   baseline; twice the standard is an implementation control for scale invariance and could not
   have failed unless the implementation had a scale bug; `A_6` is the only non-standard form that
   passed; the fourth is undecided at sixteen of sixty-four.
7. The citation caveat stands as written, and the codimension-five identity of amendment 2 is the
   empirical substitute for a numbered statement.

### The linear program is not reviewable yet, and two of the reasons are fatal to it as specified

- **As specified it cannot be infeasible.** Each truncation contributes one relation and five brand
  new variables, and a system in which every constraint carries a variable appearing in no other
  constraint and in no sign constraint is feasible by construction. A generation rule that adds
  five fresh types per relation therefore guarantees the answer the record itself calls
  uninformative. Infeasibility is reachable only when truncations land back on types already
  present.
- **"Type" was undefined, and one of the two readings is false.** If a type were a cone up to
  lattice isomorphism, the derivation would be false, and this project's own move 15 refutes it:
  the unimodular six-simplex has seven vertex cones all unimodularly equivalent to the standard
  orthant, and their weights sum to one, not to seven sixty-fourths. So the Berline-Vergne weight
  is not a function of the lattice-isomorphism class. A type must therefore be a cone with its
  lattice up to isometry, and the program needs a canonical form deciding that in rank five, which
  `isotypes.canonical` supplies only for signed permutations of the standard rank-six lattice.
- **The barrier claim needs an averaging argument.** With isometry-invariant deltas, infeasibility
  bars invariant local formulas only. The repair: validity is an affine condition with a fixed
  right-hand side, so convex combinations of valid formulas are valid; the isometry group is
  finite; the hive cone list is closed under it, which is why the classes were merged by signed
  permutations in the first place. Hence if any valid formula is nonnegative on the hive cones,
  its average over the group is an invariant valid formula nonnegative on them, and infeasibility
  of the invariant program is a barrier for every local formula at codimension five.
- **Two further requirements.** The truncation construction gives five new vertex cones only for a
  simplicial cone with five rays, and the atlas contains non-simplicial cones, so the record must
  say what is done with those. And an infeasibility verdict must come with a Farkas certificate, a
  nonnegative rational combination of the constraints exhibiting the contradiction, written to a
  file and checked by the step's own checker, because this is the one result in the attack that
  would be a genuine barrier and a solver's word is not a theorem.

### The generation rule the reviewer requires, replacing the open-ended one

Declare the variable library before generating: the 5,142 held classes plus the unimodular class
plus whatever else is named. Keep only truncations all of whose vertex cones canonicalise into
that library, discard the rest, and report how many truncations were tried against how many were
kept, so the coverage is visible. That makes the program finite from the start with no budget
guesswork and preserves the direction of the logic, since dropping relations only enlarges the
feasible set. Budget: a fixed number of truncation attempts, exact rational arithmetic throughout,
one solve at the end, and a wall-clock cap.

### Ordering, as decided by the reviewer

Move 16, narrowed to the screen, runs first and is the last move of this pass. The linear program
is written up properly with the amendments above and opens the next pass. A feasible outcome from
the program is worth nothing by itself, so the run is worth making only because infeasibility is
reachable under the declared-library rule.

## The linear program, rewritten with the six amendments, awaiting review

This replaces the earlier sketch entirely. Two of the reviewer's findings were fatal to that
version and both are addressed here rather than argued with.

### What a type is, and how equality of types is decided

A **type** is a cone together with its lattice, up to isometry: two pairs `(R, G)` and `(R', G')`
are the same type when some `U` in `GL_5(Z)` satisfies `U^T G' U = G` and carries the ray set of
the first onto that of the second. Lattice isomorphism is the wrong equivalence and this project's
own move 15 refutes it: the unimodular six-simplex has seven vertex cones, all unimodularly
equivalent to the standard orthant, and their weights sum to one rather than to seven sixty-fourths,
so the Berline-Vergne weight is not a function of the isomorphism class.

Equality of types is decided by an explicit search rather than by a canonical form. For a
simplicial cone with five spanning rays, `U` is determined by a bijection of the ray sets, so 120
candidates are tried and each is checked for integrality, for unimodularity and for `U^T G' U = G`.
For a cone with `k > 5` rays the injections of a spanning subset are tried, which is bounded
because `k` is small. A cheap invariant prefilters: the ray count, the multiset of Gram entries and
the determinant of a spanning subset.

### The relations, and why the truncation construction is general

Two valid local formulas differ by a `delta` annihilating every relation; at codimension five the
relations are `sum over the vertices of a five-dimensional lattice polytope of delta(tangent cone)
= 0`. Relations are generated by truncating a cone: choose a functional positive on it and cut at a
height that is a common multiple of the functional's values on the primitive rays, so that the ray
intersections are lattice points. The vertices of the result are the apex, whose tangent cone is the
given cone, and the ray intersections, whose tangent cones the truncation determines. The reviewer
noted this gives five new cones only for a simplicial cone; that is a count, not a limitation. For a
cone with `k` rays it gives `k` new cones, and `k` is small.

### The declared library, which is what makes infeasibility reachable

The earlier rule added five fresh variables per relation, and a system in which every constraint
carries a variable appearing in no other constraint and in no sign constraint is feasible by
construction. So the answer was fixed before the run.

The rule is replaced. **Declare the variable library before generating**: the 5,142 held classes,
each as a type in the sense above. Generate truncations, canonicalise all vertex cones of each, and
**keep a relation only when every one of its cones is already in the library**. Discard the rest.
Report tried against kept, so the coverage is visible. Dropping relations only enlarges the feasible
set, so the direction of the logic is preserved, and the program is finite from the start.

### The logic, and the averaging argument the barrier claim needs

Infeasible on the kept relations implies infeasible on all relations, because the kept ones are a
subset. That bars **isometry-invariant** valid formulas. The step to all valid formulas is an
averaging argument, and it is available: validity is an affine condition with a fixed right-hand
side, so a convex combination of valid formulas is valid; the isometry group of the ambient
lattice with its form is finite; and the hive cone list is stable under it, which is exactly why
the classes were merged by signed permutations. So if any valid formula is nonnegative on the hive
cones, its average over the group is an invariant valid formula nonnegative on them. Hence
infeasibility of the invariant program is a barrier for every local formula at codimension five.

Feasible is recorded as **no barrier found with these relations** and never as progress, because
the kept relations are a subset and a `delta` satisfying them need not be a difference of valid
formulas.

### The program, the budget and the certificate

Variables `delta(sigma)` for `sigma` in the library; equality constraints, one per kept relation;
sign constraints `delta(sigma) >= -w(sigma)` with `w` the recorded Berline-Vergne weight.
Substituting `s = delta + w >= 0` turns it into `A s = A w`, `s >= 0`, a phase-one feasibility
problem in exact rational arithmetic, solved once at the end.

Budget: at most 20,000 truncation attempts, one wall-clock cap of 45 minutes, exact rational
arithmetic throughout, one solve. If more than 5,000 relations survive the keep rule, the run
reports the size and stops rather than starting a solve it cannot finish exactly.

**An infeasibility verdict is not accepted without a Farkas certificate.** Phase one returns
multipliers `y` with `y^T A` nonnegative componentwise and `y^T A w` negative; both are exact
rational statements about recorded matrices, and the step's checker recomputes them from the
recorded `y`, `A` and `w` rather than trusting the solver. This is the one result in the attack
that would be a genuine barrier, so a solver's word is not enough.

### Category, outcomes, retreat, allowance

Category 1, necessary main progression: it decides what the form family of move 16 only probes.
Outcomes: infeasible with a verified certificate is a barrier for every local formula at
codimension five, which closes the weight route and redirects the attack to the per-facet line;
feasible is recorded as no barrier found and the run's coverage, tried against kept, is what the
record carries. Retreat: fewer than fifty relations survive the keep rule, which would mean the
library is too coarse for any sharing to occur, or the solve exceeds the cap. Allowance: one run of
at most 45 minutes, trials counted, one checker run and at most two corrections.

**Independent review.** Requested. Not started.


## Sixth independent review, 2026-09-05: the linear program is closed, and a record defect

### The linear program is closed as a route, with its obstruction written down

The reviewer's verdict is do not run it, and the reason is stated in the Farkas form so that the
route is not proposed a fourth time. Infeasibility of "s nonnegative, A s = A w" holds exactly
when some vector in the row space of A is componentwise nonnegative and pairs negatively with w.
The weight vector has twenty-one negative entries, all between about 1.5e-4 and 3.2e-3, against
roughly 5,121 nonnegative ones, so such a vector must put almost all its mass on those twenty-one
coordinates. Every row of A is the edge-length vector of one hive polytope: nonnegative and spread
over hundreds of classes, of which the negative ones are 732 of 226,740 edge slots, and a facet
carrying a negative edge carries between 137 and 258 positive ones. Concentrating a nonnegative
row-space vector on twenty-one coordinates therefore needs cancellation annihilating thousands of
positive coordinates exactly, and move 3 measured the available freedom at rank 442 against 3,406
unknowns with the class count growing faster than the equation count. That is not a proof of
feasibility and is not offered as one; it is the absence of any mechanism by which infeasibility
could arise, which is what a decision-guiding experiment needs before it runs. Beside it stands
move 17: the zero-row shortcut was tested and is vacuous, because a vanishing linear coefficient at
a ray means the polytope degenerates to a point and every edge length is zero.

### A record defect, found by the reviewer and repaired

Five of the thirteen deterministic steps had no README: checks 5, 6, 7 and 8 and
enumeration-run-4. The cause is mechanical and worth recording. Each of those documents was written
in the same shell command as a harness verification call, and the gate rejected those commands as
unparsable shell text, so the whole command including the heredoc never ran; the verification was
then re-issued alone and the document was not. All five are now written, from the results recorded
in each step's own files, and every step has one. The lesson is one line: never put a document
heredoc in the same command as a harness call, and do not name harness commands inside document
text.

### The remaining moves, as the reviewer ordered them

O-B first, because it is the only category-two item available and the machinery for it exists.
Then the per-facet question. Not move 8's residue, which is unenumerated with no method proposed,
and not the root's question about why the h vectors are nonnegative, which is the root's obligation
and has no success criterion here. The five classes surviving every form stay a recorded conjecture
rather than a target, because no method for proving a weight negative under every positive-definite
form appears anywhere in this record.

The first O-B move has been made and its answer is negative for the shortcut: see
study/low-dimensional-weights-can-be-negative.md. The weight of a two-dimensional cone is already
negative when the cone is wide enough, so the positivity this project holds at codimensions two and
three is about the cones spanned by the twenty-seven rank-five normals and not about all cones of
those dimensions. O-B therefore needs its own atlas at each intrinsic dimension.


## Proposal for moves 19 and 20, awaiting review: the projected atlas of the non-full-dimensional hives

**Where this stands.** Move 11 reduced obligation O-B to the same problem in the intrinsic lattice
one dimension lower. Move 18 removed the shortcut: the weight of a two-dimensional cone is already
negative when the cone is wide enough, so the positivity this project holds at codimensions two and
three is about cones spanned by the twenty-seven rank-five normals and not about all cones of those
dimensions. O-B therefore needs its own atlas at each intrinsic dimension, which is what this
proposes.

**Target.** For the five-part triples whose hive polytope has intrinsic dimension three, four and
five, enumerate the transverse cone types of the edges in the intrinsic lattice, compute their
Berline-Vergne weights, and report the sign census by intrinsic dimension.

**Category.** 2, exact proof coverage. A dimension whose types are all nonnegative is discharged
outright by the nonnegative-class lemma, which move 2 of the root showed is rank-uniform and which
move 11 showed applies verbatim in the intrinsic lattice. A dimension with negative types has an
explicit residue to which moves 8 to 10 apply unchanged.

**What has to be built.** The contraction of move 11, made concrete: translate the polytope by a
lattice point of it, take the lattice of the linear span, express the polytope in a basis of that
lattice, and carry the induced form as the Gram. The transverse cones are then built by
`transverse_q.py`, which already takes a form, with the induced Gram in place of the identity.
Nothing new is needed beyond the coordinate change.

**Why the finite domain is sufficient.** For a given intrinsic dimension the types that occur are
what the residue is; a type that occurs with a negative weight is a genuine part of it, and a
dimension all of whose occurring types are nonnegative is discharged for the triples that produce
them. The record will state, as the full-dimensional atlas does, that the list is the types seen in
the sample and not a proof that no other type occurs.

**Outcomes.** All nonnegative at a dimension: that dimension of O-B closes for the sampled types
and the remaining obligation there is the completeness of the type list. Some negative: the residue
is explicit and the machinery of moves 8 to 10 applies. Either is a decision.

**Checkpoint condition.** A per-dimension type count and sign census, with the negative types
recorded by their normals.

**Retreat condition.** The contraction fails a validation check, meaning the local formula in the
intrinsic lattice does not reproduce the certified coefficients of the contracted polytope; or the
allowance is spent before intrinsic dimension four is complete, in which case the covered
dimensions are reported and named as a prefix.

**Validation before any recorded result**, in the style move 16 was required to use: the local
formula in the intrinsic lattice must reproduce the certified linear coefficient of a sample of
contracted polytopes exactly. That is the same end-to-end identity the full-dimensional case used
and it exercises the contraction, the coordinate change and the induced Gram together.

**Finite resource allowance.** Two runs of at most 30 minutes each, single threaded, trials
counted; one checker run per step and at most two corrections.

**Independent review.** Requested.


## Seventh independent review, 2026-09-05: the O-B proposal, and a validation that cannot see what matters

Verdict: ACCEPT WITH AMENDMENTS. Seven of them, one of which repairs a silent failure mode.

### The validation as proposed is blind to the input the answer depends on

Moves 15 and 16 established that every positive-definite form yields a valid local formula, and all
ten forms reproduced the codimension-five identity at 49/20. So an end-to-end test that the local
formula in the intrinsic lattice reproduces the certified linear coefficient **cannot distinguish
the induced Gram from any other positive-definite form on that lattice**: it tests validity, and
validity is exactly what does not depend on the choice. The sign census does depend on it, and move
16 measured how much, twenty-one negatives under the standard form against five under the identity
plus a quarter. A wrong Gram would pass the proposed validation and the recorded negative types
would be a property of the wrong metric.

The contraction therefore needs direct checks, and they are cheap exact linear algebra: that the
lattice of the linear span is saturated, that the computed basis generates it rather than a
sublattice, and that the Gram is recomputed from the ambient standard inner products of those basis
vectors. The rest of the contraction the reviewer checked and confirmed: move 11's identity does
make the certified coefficient the linear coefficient of the contracted polytope, because a point
of the dilate is integral exactly when its displacement lies in the intersection of the ambient
lattice with the direction space.

One sentence enters the record with it: carrying the induced form is a choice and not forced, so a
later reader must not take the sign census for an invariant of the polytope.

### The category is one, not two

Category two requires that success completely discharge an explicit part of the objective. A list
of the types seen in a sample discharges at best the triples sampled, and the proposal's own
outcome text says so. **The proposal is relabelled category one.** Completeness is available in
principle and is worth recording as the route to category two: the intrinsic direction space is the
span of a face of the hive cone, so there are finitely many, and projecting the twenty-seven
normals for each and taking subsets of size one less than the intrinsic dimension gives a complete
atlas per dimension, the exact analogue of the five-subsets that made the full-dimensional atlas
complete. Whether that is affordable is not yet measured, and the first run measures the type
counts that would decide it.

### The runs are split by stage, not in half

Run one enumerates the projected types at intrinsic dimensions three, four and five, because
enumeration is a coordinate change and is cheap, and weights dimensions three and four, where the
cones are two- and three-dimensional. Run two weights dimension five against the count run one
measures. That keeps the expensive four-dimensional weights out of the cheap run and leaves a
re-planning point between two different decisions.

### Two corrections to the record

**The linear program.** The sentence "it is the absence of any mechanism by which infeasibility
could arise" is stronger than the reviewer can support and is replaced by: no mechanism has been
identified, and the only way to look for one directly is the program itself.

**Move 18 is upgraded from an observation to a consequence.** The earlier paragraph argued only
that a polygon with many vertices cannot have every weight bounded below by a positive constant,
which yields at most that the infimum is zero. The sharp argument uses the identity and one
computed value: the vertex weights of any lattice polygon sum to one, and the thin cone with rays
`(1,0)` and `(100,1)` has weight `343401/40004`, above eight, so any lattice triangle carrying that
cone at a vertex has its other two vertex weights summing to below minus seven, and at least one of
them is negative. Negativity in dimension two is therefore a consequence of the identity, not an
observation. The reviewer also checked three of the table's entries against the same identity: the
unimodular triangle gives `1/4 + 3/8 + 3/8 = 1`, and the quadrilateral with vertices `(0,0)`,
`(1,0)`, `(2,1)`, `(0,1)` gives `1/4 + 1/8 + 3/8 + 1/4 = 1`. Two smaller points stand: "negative as
soon as the cone is wide enough" is six computed values and not a monotonicity law, and the weight
depends on the lattice as well as the angle. The next step's checker recomputes those seven values,
since a route decision now rests on them.

### Budget, stated while six moves remain

The attack stands at 18 moves of 24, pass three at two of eight, so moves 19 to 24 are everything
that remains. Two go to O-B, which leaves four for the per-facet question and the close, and at
least one of those four is reserved now for the honest final statement of what is proved and what
is not.
