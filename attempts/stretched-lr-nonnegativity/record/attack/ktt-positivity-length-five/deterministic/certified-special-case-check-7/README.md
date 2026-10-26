# certified-special-case-check-7: are the twenty-one negative under every scalar product?

Date: 2026-09-05. Entry: choose-the-auxiliary-weight-or-certificate. Approved with seven
amendments by the fourth independent review of 2026-09-05, recorded in `../../ADMISSION.md`.

## The question

The nonnegative-class lemma closes the full-dimensional half of the rung if no class has negative
weight. Twenty-one of the 5,142 classes the project holds are negative under the standard scalar
product. The Berline-Vergne construction takes any rational positive-definite form, so the question
is whether those twenty-one are negative under every form or only under this one.

## The module, and the two checks it had to pass first

The transverse cone with its lattice is metric-free, but the identification `tools/transverse.py`
uses is not. `transverse_q.py` makes the projection and the Gram depend on the form; the span of
the face is the common kernel of the normals and stays metric-free, and the inequalities are dual
pairings and stay unchanged.

The vertex-sum gate of `enumeration-run-4` does not validate this module: it sums full-dimensional
tangent cones at codimension six, and this module builds codimension-five transverse cones.

- **Recorded weights.** Under the standard form the module reproduces recorded weights exactly: 9
  classes in the run, 6 more on a fresh sample in the checker, 0 mismatches.
- **The codimension-five identity.** The unimodular six-simplex has Ehrhart polynomial `C(t+6,6)`,
  so its linear coefficient is `H_6 = 49/20`, and each of its twenty-one edges has lattice length
  one. The twenty-one transverse cone weights must therefore sum to `49/20`. **Every one of the ten
  forms passes this**, which is the necessary validity test at the codimension that matters.

## Result (`screen.json`, `result.json` status pass)

| form | of the 21, still negative | lifted | of the 10 control classes, gone negative |
|---|---|---|---|
| standard | 21 | 0 | 0 |
| `A_6` | 16 | 5 | 10 |
| `D_6` | 16 | 5 | 10 |
| `E_6` | 18 | 3 | 10 |
| `A_6` dual | 7 | 14 | 2 |
| `D_6` dual | 7 | 14 | 2 |
| `E_6` dual | 7 | 14 | 2 |
| identity plus 1/4 off the diagonal | 5 | 16 | 0 |
| identity plus 1/2 off the diagonal | 5 | 16 | 0 |
| identity minus 1/8 off the diagonal | 21 | 0 | 10 |

412 seconds for ten forms. The negativity is largely an artefact of the standard scalar product and
not wholly: a single small perturbation lifts sixteen of the twenty-one and leaves all ten control
classes positive, while the root-lattice forms trade instead, lifting a few and pushing every
control class negative. Five classes survive every form tried, and the checker recomputed them
under the best form.

## What is not claimed

The control covers **ten of 5,121 positive classes**, so the other 5,111 are unevaluated under
every non-standard form and no form's total negative count is known; "lifts sixteen" is a statement
about the original twenty-one only. Ten forms are a finite sample of a twenty-one-parameter
continuum, so nothing says no form lifts all twenty-one. All ten forms passed the codimension-five
identity, which is the test at the codimension that matters, but only the standard form and `A_6`
passed the codimension-six vertex-sum gate; both are necessary and neither is sufficient, and the
codimension-five test is a single linear equation per form, so a second six-dimensional lattice
polytope with a known linear coefficient should be added. Lifting a representative is not lifting
its class, because a non-standard form breaks the collapse by signed permutations. And a form
lifting all twenty-one would still require re-evaluating the other 5,121 held classes under it.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The recorded counts recomputed from the recorded weight lists: 10 forms, 0 mismatches.
2. The codimension-five identity recomputed for two forms with the simplex's edges derived from
   the polytope by Normaliz instead of from the hand-written normal sets: 21 edges, 0 mismatches.
3. The module against recorded weights on a fresh sample disjoint from the run's: 6 classes, 0
   mismatches.
4. The five classes that survive the best form, recomputed under it: 0 mismatches.

Trusted base: Normaliz 3.11 through PyNormaliz, `tools/bvweight.py`, Berline and Vergne's
construction as cited from the abstract, Python integers and Fractions.
