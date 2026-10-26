# certified-special-case-check-1: the local Ehrhart formula extraction, validated on five-part hives

Date: 2026-09-05. Entry: predict-the-value-and-test-it-numerically, actions 1 and 2 (the
prediction that the local formula, transferred to the rational hive polytope, reproduces the
recorded coefficients, tested on a stratified set of polytopes). Step kind: certified
special-case check, two independent computations of the same quantities compared exactly.

## What is computed (`run.py` over `localform.py`)

For each of the first 2,000 full-dimensional (dim H = 6) five-part records of
`enumeration-run-2` of the box attack, the top three Ehrhart coefficients are recomputed from the
face data of the hive polytope,

    a_6 = relvol(P),
    a_5 = (1/2) sum over the facets F of relvol(F),
    a_4 = sum over the codimension-two faces F of alpha(u_F, v_F) relvol(F),

where relvol is Normaliz's `Volume` of the face divided by the factorial of its dimension, u_F
and v_F are the extreme rays of the face's normal cone among the outward primitive normals of the
facets containing it, and alpha is the closed weight of a two-dimensional transverse cone
(Castillo-Liu Lemma 3.3, in the form recorded in the replay repository of Ferudun 2026). The
identity is the McMullen local formula transferred to the rational polytope by the period-one
dilation lemma; the run tests it against coefficients computed by a different route, Normaliz's
Ehrhart series, which the box attack independently pinned with lrcalc.

The run also records the data the codimension-five step needs: every edge of every polytope with
its lattice length and the set of outward normals of the facets containing it, which is its
transverse cone type.

## Result (`validation.summary.json`, `result.json` status pass)

| | |
|---|---|
| polytopes | 2,000 (full-dimensional, five parts, size <= 30) |
| agreeing on a_6, a_5, a_4 | 2,000 |
| mismatches | 0 |
| edges | 133,188 |
| distinct edge types | 8,305 |
| type sizes (number of facets through the edge) | 5: 3,876; 6: 3,023; 7: 1,036; 8: 332; 9: 29; 10: 9 |
| facets per polytope | 8 (770 polytopes), 11 to 24 (the rest), maximum 24 |

The 27 primitive rhombus normals of N_5 are recovered as the union of all outward normals, which
matches the source's count.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against the files it describes: record count, type count, edge count, zero
   mismatches.
2. The right-hand sides against the certified data: for 200 seeded random records the linear
   coefficient stored here equals the one recorded by `enumeration-run-2`, whose polynomials were
   pinned independently by lrcalc counts with exact interpolation.
3. The edge extraction by a different method: for 20 seeded random polytopes the edges are
   recomputed from Normaliz's face lattice at codimension five with Normaliz's own volume for
   each one-dimensional face, and compared with the run's vertex-pair extraction as multisets of
   (normal set, lattice length): 0 mismatches. The run's method (vertex pairs whose common tight
   facets have rank five, with the length read from the primitive direction vector) shares no
   code with it.
4. The weight formula against its self-test, rewritten in the checker: the vertex weights of the
   unit square and of the unimodular triangle each sum to the Ehrhart constant term 1.

Trusted base: Normaliz 3.11 through PyNormaliz (two different computations: the Ehrhart series
and the face volumes), Python integers and Fractions, the local formula and the dilation lemma as
cited, and the certified coefficients of the box attack.

## What the step decided

The extraction is correct: the local formula, the outward-normal convention, the relative-volume
convention and the codimension-two weight together reproduce three coefficients of 2,000 hive
polytopes exactly, so the same machinery can be trusted at codimension five, where the weight is
unknown. It also fixes the size of the problem there: the linear coefficient of these 2,000
polytopes is a sum over 133,188 edges falling into 8,305 types, so the linear system that would
determine the weights from the recorded coefficients has 2,000 equations and 8,305 unknowns and
is underdetermined by a factor of four. The types are not independent, however: the weight is an
invariant of the transverse cone up to lattice isometry, and a first invariant, the Gram matrix
of the normal set up to permutation, already collapses the 8,305 types to 2,628 classes (the
3,876 types of size five to 1,288). Whether that collapse is legitimate has to be decided by
exhibiting explicit lattice isometries, which is the next step's work.
