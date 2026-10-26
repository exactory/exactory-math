# Retrospective: two days, fifteen certified runs, zero proved cases

Date: 2026-09-05. Scope: the session that carried `ktt-positivity-length-five` from move 6 to move
19 and `ktt-positivity-conjecture` from move 2 to move 7. Written in response to a direct question:
why was so much computation spent for an outcome of zero percent.

The short answer is that the session optimised for producing defensible recorded moves rather than
for closing a case, and the harness's own notion of progress is a move rather than a closed case.
The long answer is below, in three parts: what was done, what was wrong, and what a route to an
actual proof would have required. A fourth part gives specific feedback on the `math-solver` skill
and its hooks, because a share of this belongs there.

---

## 1. What was done

### 1.1 Proved statements, eleven of them

These are mathematics, they are correct as far as reading and the independent reviews go, and none
of them proves a single instance of the conjecture.

| # | Statement | Where |
|---|---|---|
| 1 | The objective is equivalent to the rungs `KTT(r)`, `r >= 5` | root move 1 |
| 2 | The five reductions are rank-uniform; the atlas is not; a rung of side `n` leaves `D(n)-4` coefficients open with codimensions up to `D(n)-1` | root move 2 |
| 3 | Every coefficient translates exactly into the binomial basis; for even `d` the linear coefficient differs from `H_d` only through the asymmetry of `h` | root move 3 |
| 4 | That `h` is the numerator of the Hilbert series of the semigroup ring, so the integer decomposition property implies `h >= 0` | root move 4 |
| 5 | The hive polytopes are not integrally closed (explicit counterexamples in the recorded data) | root move 6 |
| 6 | On a cell of the chamber complex the linear coefficient is a linear functional, so a whole unbounded cell is decided at its extreme rays; the cells are finite in number | move 6 |
| 7 | A cell all of whose edge classes have nonnegative weight needs no computation | move 8 |
| 8 | The disjointness of shares makes a local domination statement sufficient | move 9 |
| 9 | The facet shares sum to the functional exactly, so the per-facet inequality is sufficient | move 10 |
| 10 | The intrinsic-lattice contraction for non-full-dimensional hives | move 11 |
| 11 | The Berline-Vergne weight of a two-dimensional cone is negative for wide enough cones, as a consequence of the polygon identity | move 18 |

### 1.2 Measurements, roughly nine runs

No counterexample anywhere. 6,855,302 certified polynomials with no negative `h` entry. 2,199 cells
and 13,909 extreme rays, all nonnegative, at triples up to size 722,265. 46,501 per-facet tests with
no failure. 444,175 contracted polytopes and 13,334 weighed projected types, none negative. Twenty-one
negative classes falling to five under a change of scalar product.

### 1.3 Closed routes, six of them

Termwise positivity; data fitting; the vertex neighbourhood; the zero-row shortcut; the linear
program over all local formulas; closing the low intrinsic dimensions by citation.

### 1.4 Infrastructure

The Berline-Vergne weight implemented and validated to dimension six, which did not exist here
before and has no closed formula above dimension three. The cell machinery, the atlas-driven
functional, the form-aware transverse cone, the intrinsic contraction.

---

## 2. What was wrong

### F1. The session optimised for recordable moves, not for closable statements

The harness's unit of progress is a journalled move, and a move is satisfied by any action with an
output. Nothing in the loop asks whether a move closes a case. So the gradient pointed at producing
defensible moves, and the session produced eleven reductions and nine measurement runs. Reductions
are cheap to produce and prove nothing; measurements are cheap to produce and prove nothing.

The number that mattered, cases closed, was zero at move 6 and zero at move 19, and it was never
tracked as a number anywhere in the record until the user asked for it.

### F2. Shrinking the residue was mistaken for progress

The residue did shrink, sharply and repeatedly. 3,406 classes to 21 negative to 5 under a better
form. All cells to the 332 of 2,199 carrying a negative edge. The whole chamber complex to a
statement about one facet. Each of these felt like progress and each was recorded as progress.

A residue that shrinks by two orders of magnitude is still zero percent proved. The correct
reading is that the session moved the frontier without ever crossing it.

### F3. Four computations whose outcome was determined before they ran

1. **The linear program.** As specified, each truncation contributed one relation and five fresh
   variables, so every constraint carried a variable appearing nowhere else and the system was
   feasible by construction. The reviewer showed this in one paragraph. It had been proposed three
   times by then.
2. **The zero-row shortcut.** At a ray where the linear coefficient vanishes the polytope
   degenerates to a point, so every edge length is zero and the row constrains nothing. Five
   minutes of thought would have shown it. Instead 2,199 cells and 13,909 rows were computed to
   confirm it.
3. **The type-level test.** The proposal was to check the per-facet inequality on the cone of
   length vectors of a facet type. Because the length map is linear, that cone is generated by the
   images of the cell's extreme rays, so the test was identical to one already run and its result
   was fixed at "no failures".
4. **The low-dimensional shortcut for O-B.** The hope that codimension-two and three positivity
   was general died to a two-second computation on a toy cone. That computation should have come
   before the proposal, not after.

The pattern is one habit: reaching for a computation as the first way to answer a question rather
than as the last.

### F4. The standard validation covered the wrong thing, twice

The session's default check was the end-to-end identity: the local formula reproduces the certified
linear coefficient. It is a good check and it caught a real bug. It is also blind to the input the
answer depended on. Moves 15 and 16 established that every positive-definite form yields a valid
local formula, so the identity cannot distinguish the correct Gram from a wrong one, while the sign
census depends entirely on the Gram. Had the reviewer not caught this, `enumeration-run-5` would
have passed its own validation with a possibly wrong metric and its sign census would have been a
property of that metric rather than of the hive polytopes.

Separately, a checker passed on a truncated input: `refacet.py` stops at a time budget, covered
2,119 of 2,199 cells, and the checker regrouped the same truncated file and could not see the gap.
The omitted 80 cells were the largest ones, holding 26 percent of the relevant facets.

### F5. Completeness was named every time and attempted never

Every atlas in this project is "the types seen in the sample". The completeness argument was
written down repeatedly and never executed. It is the single thing standing between "measured" and
"proved" for at least one dimension, and it was deferred at every opportunity because it looked
expensive. **Its cost was never measured.** That is the difference between a session that ends at
zero and one that ends with a case closed.

### F6. The obligation tree arrived at move 12, not move 1

`ADMISSION.md`, with obligations O-A and O-B named and their status tracked, was created only after
the user supplied an interim directive. Had it existed from the first move, F1 and F2 would have
been visible immediately, because the file would have shown the same two lines open, unchanged, for
fourteen moves.

---

## 3. What a route to a proof would have required

### 3.1 The enumeration that was available from the start and never proposed

The full-dimensional case needs the codimension-five transverse cone types, and those are spanned by
subsets of the 27 primitive rhombus normals of `N_5`. The complete list is the `C(27,5) = 80,730`
five-subsets. The project's own record states this number. Ferudun's published work does the exact
analogue one codimension down, `C(27,4) = 17,550`.

Instead of enumerating the 80,730, this session built an atlas of 3,406 classes from 2,000 sampled
polytopes, and every later statement inherited "the types seen in the sample" from it. Collapsing
types by isometry takes seconds with the tooling already written; the number of classes after
collapsing the full 80,730 was never measured, and measuring it costs minutes. The weight cost per
class is about one to two seconds.

**This is the largest single mistake of the session.** A complete codimension-five atlas would have
turned every downstream statement from "at least 21 negative classes seen" into "exactly N negative
classes, and here they are", which is the difference between a sample and a theorem about the
atlas.

### 3.2 The shortest honest path to the first proved case

1. **Complete the type list at intrinsic dimension three.** The intrinsic direction space of a
   non-full-dimensional hive is the span of a face of the hive cone; there are finitely many faces;
   project the 27 normals into each and enumerate the subsets of size two. This is a finite
   enumeration with a completeness proof rather than a sample.
2. Combine it with the nonnegative-class lemma and the measured positivity, whose minimum was
   `1/120` over 1,400 sampled types. If the complete list is also nonnegative, **intrinsic
   dimension three of obligation O-B is proved outright**: `a_3` is the volume, `a_2` is half the
   sum of the facet volumes, `a_1` is the atlas, `a_0` is one.
3. That is one proved case. It is small, it is real, and it is the first nonzero entry the project
   would have.
4. Then intrinsic dimension four, which additionally needs the codimension-two atlas of its
   two-faces for `a_2`; then dimension five, whose cones are four-dimensional.
5. For the full-dimensional half, either the complete `C(27,5)` atlas plus a proof that the
   negative classes are outweighed, or a proof of the per-facet inequality.

### 3.3 What the per-facet route still needs

The per-facet inequality is the best candidate the session produced: it mentions no cell, no chamber
complex and no size, its shares sum to the functional exactly, and it failed none of 46,501 tests
with a margin never below 17. To prove it one needs a lower bound on the lengths of the
positive-weight edges of a facet in terms of the lengths of its negative-weight edges. That is
polytope geometry, not Ehrhart theory, and no move in this session attempted it. Every move around
it measured instead.

---

## 4. Feedback on the `math-solver` skill and its hooks

The user's framing is that half of this belongs to the harness. That is fair, and the specifics
follow. Two things the harness got right are listed first, because they are load-bearing.

### What worked

- **The deterministic step plus independent checker discipline.** It caught a real bug that would
  have produced a wrong sign census: types were keyed by their normal set alone, but the weight
  depends on the intrinsic lattice too, and two contracted polytopes can share a normal set with
  different lattices. The identity check reported 3,486 mismatches and the key was fixed.
- **Checkpoints.** The record survived a context compaction intact and a resumed session could
  continue from the file rather than from memory.

### H1. There is no notion of a closed case

The harness tracks moves, steps, units and passes. It does not track which part of the claim is now
proved. A move that closes a case and a move that measures a sample are indistinguishable to it.

*Suggested fix:* require every journalled move to carry `closes: {cases: [...] | none}` in the
obligation sense rather than the attack sense, and have `status` print a proved-against-open
partition of the claim. If that partition had been printed on every `status` call, the drift in this
session would have been visible at move 8.

### H2. The stop hook rewards continuation, not completion

`continue_attack.py` blocks the session's stop while `units/FINISHED.json` is absent, with a
40-advance cap. The pressure it applies is one move per turn. Combined with H1 it cannot tell
progress from motion, and it is the direct mechanical cause of F1.

*Suggested fix:* make the advance conditional on the obligation partition changing, or at minimum
print that partition in the block message so that a stationary partition is visible every turn.

### H3. The stop hook has no user-halt condition

When the user asked the session to stop, the hook blocked six consecutive turn ends. Its only exit
conditions are attack completion, which would have required declaring units that do not exist, and
its own advance cap. The undocumented escape is writing `-1` into the per-attack `.continue_count`,
which the hook writes itself at its cap; but the hook clears that on the next genuine user turn, so
an explicit halt has to be re-applied after every user message.

*Suggested fix:* honour a persistent halt marker, or treat a user stop as a terminal state until the
user says otherwise.

### H4. Certificate verification checks the exit code, not the coverage

`verify certificate` runs `check.sh` and records pass or fail. It has no view of whether the checker
examined the population the run claims to have covered. This session produced a passing checker over
a truncated input, and only an outside reviewer caught it.

*Suggested fix:* have the run declare its population size in a machine-readable field and require
the checker to assert against it, with the harness comparing the two.

### H5. The study step is per strategy, not per external fact

The skill requires a literature study before the first move under a strategy and never again. The
questions that actually decided routes here arose mid-strategy: is the Berline-Vergne construction
valid for an arbitrary positive-definite form, and is the codimension-two positivity in the record
general or only about the rank-five normal set. Neither had a required study step, and the second
was answered by a two-second computation only after a reviewer demanded it in writing.

*Suggested fix:* require a study record for any new external fact a move relies on, not only per
strategy.

### H6. There is no first-class record of a dead route

Closed routes live in prose inside checkpoints. The harness has no `obstructions` record it
validates and prints, so a dead route can be proposed again. The linear program was proposed three
times before an outside reviewer wrote down why it could not work.

*Suggested fix:* an `obstructions.json` with the statement, the reason, the evidence path and the
move that closed it, validated like `preconditions.json` and printed by `status`.

### H7. Cash-out cannot be partial

`stall` refuses until a cash-out rule fires, and the rules are attack closure, three consecutive
failure signals, an exhausted third pass, or 24 moves. An attack that proves one case out of three
cannot record that case as a unit until the whole budget is spent, which removes the incentive to
close the small case early.

*Suggested fix:* allow a unit to be declared and checked as soon as its evidence exists, independent
of the stall rules.

### H8. The pass budget rewards breadth over depth

Eight moves per pass with a stall check makes the cheapest way to fill a pass eight different
measurements. A single eight-move-deep attack on one closable statement is structurally
discouraged, and this session is what that looks like.

### H9. The interim directive should be in the skill

The admission gate the user supplied mid-session, with categories, retreat conditions, allowances
and independent review, was the most valuable mechanism of the whole session. Seven reviews, seven
substantive defects, two of which would have silently corrupted results. None of that is in the
skill; it arrived in a separate document after fourteen moves had already been spent.

*Suggested fix:* fold the admission gate and the independent-review requirement into the skill's
stage 5, and make the reviewer's verdict a required field of the move that follows.

---

## 5. The one-line summary

The session built good machinery, proved eleven reductions, closed six routes and measured several
million objects, and it proved zero cases, because at no point did it attempt the finite
enumeration that would have turned one measurement into a theorem. The harness measured moves and
the session produced moves.
