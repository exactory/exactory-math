# Admission record, root attack

Governed by `misc/math-solver-interim-directive.md` of 2026-09-05. The child attack's record is
`../ktt-positivity-length-five/ADMISSION.md` and carries the shared ledger of what is proved and
what is only measured.

## Classification of the root's moves

| Move | Step | Category | Which root obligation it serves | What could not proceed without it |
|---|---|---|---|---|
| 1 | none, a derivation | 1 | the objective itself | The objective had no decomposition; it is now the rungs KTT(r), r >= 5 |
| 2 | none, a derivation | 1 | the ladder | It was not known whether the rank-five machinery is a plan for the ladder; it is not |
| 3 | none, a derivation | 1 | the objective at every rank | The statement had one language only, the local formula; it now has a second, exact one |
| 4 | none, a derivation | 1 | the objective at every rank | The h vector was a change of basis; it is now the numerator of a Hilbert series, which is where the subject's inequalities are proved |

None of these ran anything, so none needed the gate. The literature searches of move 3 are the
skill's own study step and are recorded in `study/reduce-and-translate.md`.

## Proposal, reviewed 2026-09-05, ACCEPT WITH AMENDMENTS, cut to a quarter

The proposal as first written asked for four tests on the h vectors of every polynomial the
project holds. The review cut it, and the cut is recorded here rather than the original.

**Three of the four tests decide nothing.** The asymmetry inequality of move 3 is, by that move's
own derivation, equivalent to the linear coefficient being nonnegative, and the box attack already
certified that on this very data with two independent programs, so testing it can only return a
pass. Monotonicity is a statement about a nested pair of polytopes and no pairs were named. Hibi's
lower bound needs a lattice polytope with an interior lattice point and no decision was stated to
hang on it.

**The work was also misdescribed.** The box attack's
`../stretched-lr-polynomial-negative-coefficient/deterministic/certified-special-case-check-4/census.py`
already computes the full h vector of every one of the 6,855,302 polynomials by exactly the
formula proposed, `h_i` as the alternating sum of `C(D+1, j)` times `P(i-j)`, in a run of 796
seconds on 2026-09-04, and never tests an entry for negativity. Verified: the file's header states
the formula and `hstar(coeffs)` is called on every record.

**Target, as amended.** Add a sign test and a per-record minimum-entry field to that existing,
independently checked script, and re-run it. Report the count of records with a negative entry, by
index, with the extremal triples.

**Category.** 1, necessary main progression, for the sign test alone.

**The blocked decision.** Whether the translated route can inherit anything. A negative entry
refutes `h >= 0` for this family completely, and by the contrapositive of move 4 it also refutes
the integer decomposition property for that polytope, which is a result in itself.

**What a nonnegative census would and would not mean.** Stanley's theorem gives `h >= 0`
unconditionally for lattice polytopes, so every record whose hive polytope happens to be a lattice
polytope carries no information at all, and the census as designed cannot separate those from the
genuinely rational ones without constructing the polytopes. A fully nonnegative census is
therefore weaker evidence than it looks, and it does not make the classical inequalities
available: what would earn them is a proof that the hive polytopes are integrally closed, which
move 4 shows is sufficient and which is registered below as the question that decides the route's
value.

**The caveat carried forward from move 3.** The hive polytopes are rational, so `h` here is a
basis change of a polynomial and not the h vector of a lattice polytope, and the classical
inequalities do not apply to it without an argument that nothing supplies.

**Certification caveat.** A negative entry among the 1,302,871 seven-part records rests on one
solver and must be re-certified before it is claimed. Lengths up to six are certified by two
independent programs.

**Checkpoint condition.** A sign census over the covered records with the count of negative
entries by index and the extremal triples.

**Retreat condition, which the first version wrongly said was not needed.** A negative entry ends
the classical-inequality route and returns the attack to the local-formula line with the triple
recorded as a barrier note. An exhausted allowance means the record reports exactly which prefix
of the records was covered and says that it is a prefix.

**Finite resource allowance.** One run of at most 20 minutes over the 1,334,669 certified five-part
records, matching the machine the existing census used; trials counted; one checker run. The
existing census needed 796 seconds with a pool over all 6,855,302 records, so the single-threaded
allowance is stated against the five-part subset and not against the whole.

**Independent review.** Accepted with the eight amendments above, all incorporated. Not
self-approved.

## Registered as the question that decides this route's value

Whether the five-part hive polytopes are integrally closed. Move 4 proves that it is sufficient
for `h >= 0`, Reeve's tetrahedron shows it is not necessary, and it is the only thing that would
let the route inherit the subject's inequalities. It is a bounded computational question and needs
its own admission record and review.


## Proposal for root move 8, awaiting review: the h inequalities as a falsification test

**Where this stands.** Move 5 found no negative entry among 6,855,302 h vectors. Move 6 showed the
family is not integrally closed and that the failing polytopes are not lattice polytopes either, so
neither known route explains the census. Move 7 proposed a mechanism that would: Ehrhart
equivalence to a lattice polytope, which follows from lattice-preserving scissors congruence and
which gives nonnegative h by Stanley with no integral closure needed.

**Target.** Test the three standard h-star inequalities on the recorded h vectors: Stanley's
inequality on partial sums, Hibi's lower bound, and h_d at most h_1. Report the count of records
violating each, with the extremal triples.

**Category.** 1, necessary main progression: it is the falsification test of the only mechanism the
record has for the census, and it decides whether that mechanism survives.

**Why it decides something rather than observing a pattern.** Each inequality is a necessary
condition for the mechanism. A single record violating one refutes Ehrhart equivalence to a lattice
polytope for that polytope outright, which is a sharper statement than the census and is reached
the same way. This is not a test that can only pass: the family is rational and none of the three
inequalities is available to it a priori.

**Method.** The h vectors are already computed by the script of
`deterministic/certified-special-case-check-1`. Add the three tests and re-run, as move 5 added the
sign test. No polytope is constructed.

**What a pass would and would not mean.** It would support the mechanism and would not prove it,
and the record must repeat move 5's caveat: records whose hive polytope happens to be a lattice
polytope satisfy all three unconditionally and carry no information, and this test cannot separate
them from the rest without constructing the polytopes.

**Outcomes.** A violation refutes the mechanism for that polytope and is the sharper result. No
violation leaves the mechanism standing as the only candidate explanation, and the next question
becomes whether the scissors congruence can be exhibited rather than inferred.

**Checkpoint condition.** A census of the three inequalities over the covered records, with counts
and extremal triples.

**Retreat condition.** A violation ends the mechanism as an explanation and the record says the
census is unexplained by every route it holds. An exhausted allowance means the covered prefix is
reported as a prefix.

**Finite resource allowance.** One run of at most 20 minutes on the machine the census used, trials
counted; one checker run.

**Independent review.** Requested.
