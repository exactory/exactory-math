# Evaluation of unit 1

Read against the evidence package (`unit.json`, `study/removing-condition-N.md`,
`study/reff-bound-check.py`, `journal-excerpt.md`) under the self-check in CASHOUT.md.

## Statement matches `unit.json`

Yes, quantifier by quantifier. `unit.json` quantifies over non-negative `n x n` matrices with a
connected bipartite support graph; the draft's section 1 opens with exactly that hypothesis. Both
inequalities of (*) appear in both, in the same order. Both carry the consequence for condition
(N) at entries with `a_ij >= Phi`, and both carry the two refutations. Nothing in the draft is
outside the statement.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| The lemma (*) | Proof in section 1, four lines, Cauchy-Schwarz plus Rayleigh monotonicity | yes |
| 24 of 24 numerical cases hold | `study/reff-bound-check.py`, which prints `allok` | yes |
| Up to 60 times tighter than Lemma 3(c) | same script, `worst_ratio` | yes |
| The new bar 0.105 / 7.6e-3 / 1.3e-3 / 9.0e-5 | `study/removing-condition-N.md`, move 3 output | yes |
| Smallest entry 2.9e-2 / 3.6e-28 / 9.3e-29 / 5.6e-4 | `study/entrywise-lower-bound.py`, move 4 output | yes |
| Truncation error factor `n^1.5 sqrt(2)` | `study/removing-condition-N.md`, move 4 output | yes |
| Binding factor 12.1 at `n = 7`, 6555 at `n = 20` | `study/binding-constraint.py`, cited as unit 5 | yes |

## Every reference resolves

Cheon and Wanless 2012 is in `known` of `problem.json` with its journal, volume, and pages.
Theorem R is cited to a path inside this repository, which is correct, since it is unpublished;
the draft says so rather than implying a reference exists.

## Findings

1. **The heuristic `a_min ~ 1/n` in section 2 is a heuristic, and the draft says so.** It is
   labelled as such at its only occurrence, and section 4 then refutes the bound it stands for.
   This is the honest ordering and no change is needed, but a reader who stops at section 2 would
   take the four numbers as bounds. Kept because section 4 is short and immediately follows.
2. **The caveat at the end of section 4 is required and present.** Without it the two refutations
   read as statements about near-maximisers, which they are not: they are statements about a
   relaxation. Checked against move 4's own output, which records the same caveat.
3. **No claim in the draft lacks evidence.** No claim was removed.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
