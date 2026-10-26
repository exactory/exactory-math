# Evaluation of unit 4

Read against the evidence package (`unit.json`, `deterministic/numerical-optimisation-run-1` with
its `README.md`, `search.py`, `check.py`, `check.sh` and `result.json`, and `journal-excerpt.md`)
under the self-check in CASHOUT.md.

## Statement matches `unit.json`

Yes. `unit.json` asserts that at each `n` from 5 to 12 the maximum of `phi` over `K_n` with a zero
and `lambda_2 <= c_n`, found by multi-start L-BFGS-B under a fixed seed, is strictly below
`2 - gamma_n`, lists the eight shortfalls, and says the constraint is active at `n = 5` to 8. The
draft's section 3 carries the same eight rows in the same order and section 3's closing paragraph
carries the activity claim.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| The eight shortfalls | `deterministic/numerical-optimisation-run-1/result.json`, status `pass`, and the run's `README.md` | yes |
| The constraint is active at `n = 5` to 8 | the `lambda_2 there` column of the same run | yes |
| The hypothesis set of `G` is the counterexample set of Dittert at `n` | move 1's output | yes |
| Every numerical test here is a test of a relaxation | move 4's output | yes |
| No search over `K_n` at `n >= 4` in print | unit-level novelty query, 2026-09-04 | yes |
| `n = 5` and `n = 6` proved outright | sibling attack, `deterministic/certified-special-case-check-1` and `-2`, both `pass` | yes |

## Every reference resolves

Cheon and Wanless 2012 and Sinkhorn 1984 are in `known` of `problem.json` with journal, volume,
and pages. Hwang is in `known` for `n = 3`. Theorem R is cited to a repository path, correctly,
since it is unpublished.

## Findings

1. **The unit lists moves 1 and 4, and the run was made after the walk closed at move 11.** The
   draft does not hide this and `position.md` states it in its own section. The two moves listed
   are the ones that produced the statement being tested, not the ones that ran it. A reader
   comparing `journal-excerpt.md` with the run's timestamps will see the difference, and the
   record explains it rather than leaving it to be discovered.
2. **The form is right.** `counterexample-or-computational-evidence`, not a proof form. Section 4
   states the limitation in the first sentence rather than in a footnote, and separates the strong
   reading (`n = 5` to 8) from the weak one (`n = 9` to 12).
3. **The discarded first version is reported.** A draft that showed only the successful
   parametrisation would leave the next reader to rediscover why the doubly stochastic polytope is
   the wrong domain. Section 4 keeps it.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
