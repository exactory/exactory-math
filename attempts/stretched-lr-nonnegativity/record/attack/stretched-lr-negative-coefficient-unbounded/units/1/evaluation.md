# Evaluation, unit 1 (author self-check against the evidence package, 2026-09-05)

Verdict: PASS, with the qualification that this pass was made by the author against the package
and not by an independent reader (the three reader passes of the sibling attack's units consumed
the session's usage budget; the user asked for economy). Every claim below was re-derived from
the step directories' summaries, `result.json` files and READMEs, not from memory.

## Statement

- `draft.md` Section 1 restates `unit.json` `statement` clause by clause (the sampled classes
  with their counts, no negative coefficient, the polytopes below the simplex value with their
  h*-vectors, volumes and ratios, the volume-3 polytope with its triple and ratio). The abstract
  carries the same content.
- `form` counterexample-or-computational-evidence fits: samples with checkers, no proof for the
  unsampled parts of the classes.

## Evidence and numbers

Every step named has `result.json` status pass: `counterexample-search-run-1` (second run of the
checker, 2026-09-05), `-2`, `-3`, `-4` (rewritten record file), `-5`, `-6`.

- Counts: 300,000 + 100,000 (`s1.summary.json`, `s1full.summary.json`, `recorded`); 5,170 =
  2,297 + 995 + 280 + 1,356 + 227 + 15 (run 2 `result.json`); 40,000 (`s2.summary.json`); 1,799
  (`s3.summary.json`, rebuilt from the readable records, note in the README); 3,000 + 2,000 +
  1,000 twice (`e5`-`e7`, `f5`-`f7` summaries). 453,799 = 400,000 + 40,000 + 1,799 + 6,000 + 6,000.
- Checker lines: run 1 "tableau-polytope encoding agrees on 400000 of 400000; lrcalc agrees ...
  on 400000; lrcalc pins 336404 of the 336404 records with P(6) <= 2000000; third
  implementation: 30 records, 0 mismatches" (its `result.json`); run 5 "6000 of 6000 ... pins
  5907 of the 5907"; run 6 "6000 of 6000 ... pins 5968 of the 5968; records with c = dim + 1:
  4602, largest normalized volume 2"; run 3 "lrcalc agrees at t = 1 on 40000 of 40000; ... 1500 of
  1500 sampled"; run 4 "1799 of 1799; ... 1500 of 1500"; run 2 "78 pairs recounted from the
  definition" (13 per family). All as the draft states.
- Minima: run 1 `min_a1` 157/60 (full-dimensional file) and 11/6 (all dimensions), `min_ratio`
  157/147 and 1; run 3 per-dimension minima 761/280, 3827/1260, 2843/840 (recomputed from the
  records in the run's README); run 6 `min_ratio` 24/25 in all three files; run 5 `min_ratio` 1;
  run 4 `min_ratio` 393/406 at lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1), nu = (3,2,2,1)
  (`s3.summary.json`, `min_ratio_at`).
- The below-1 records: run 6, 13 (5 parts, D = 4, V = 2, 24/25), 13 + 31 (6 parts, D = 4 and 5,
  24/25 and 44/45), 23 + 17 + 15 (7 parts, D = 4, 5, 6, 24/25, 44/45, 799/812), 112 in all; run
  4, 3 (D = 6, V = 2, 799/812) + 2 (D = 7, V = 2, 927/938) + 1 (D = 6, V = 3, 393/406); runs 1, 3,
  5: none (minimal ratio 1). Tabulated from the records by the author (the run READMEs carry
  the same numbers); not a separate checked census, which the draft does not claim.
- The volume-3 polytope: P(1) = (240 + 572 + 524 + 255 + 75 + 13 + 1)/240 = 1680/240 = 7 = c;
  P(2) = (240 + 1144 + 2096 + 2040 + 1200 + 416 + 64)/240 = 7200/240 = 30; h*_1 = 7 - 7 = 0,
  h*_2 = 30 - 49 + 21 = 2; volume 6!/240 = 3; a_1 = 572/240 = 143/60 = 49/20 - 2/30. The ratio
  393/406 at t^2: a_2 = 524/240 = 131/60 against s_2 = 203/90: (131/60)/(203/90) = 393/406.
  Correct. The threshold "h*_2 > H_6 30 = 73.5": from a_1 = H_6 - h*_2/30 < 0. Correct.
- Wall times: 817.3 + 1438.5 (run 1), 14,830.4 (run 3), 20,129 (run 4, log line), 100.3 +
  220.0 + 7154.0 = 7,474 (run 5), 910.0 + 2404.8 + 5811.3 = 9,126 (run 6). Match.

## References

Every entry carries an identifier in the record: BP03, CL18, Fe21, LL22, MM19 in
`study/reduce-and-translate.md` and `study/prove-the-barrier-first.md` and in `problem.json`
known (the Ehrhart-theory entry added 2026-09-05); CJM08 (doi:10.46298/dmtcs.3592, the box
attack's novelty record and this attack's inherited known); DW02, Fe26, Ik16, KT99, KTW04, KTT04,
KTT06, KTT09, Ra04, Sh17, No (`problem.json` known, including the identifier entries copied
from the box attack on 2026-09-05). Every key used in the text has an entry and every entry is
used.

## Self-check

- One sentence: yes (`unit.json`, long).
- A claim, not activity: yes (the sampled classes contain no negative coefficient; the below-1
  polynomials are exactly these; the volume-3 polytope exists with these properties).
- Follows from known literature in a few lines: no.
- Novelty record cited: `unit.json` `novelty` and Section 2 name `novelty.md` and the queries.
- On the path: yes (`position.md`).
- Every claim points to a proof or a run: yes, each to a run with `result.json` pass or to the
  sibling attack's finished units.

## Findings requiring a change

None. Two limits are stated in the draft rather than fixed: the below-1 tabulation is the
author's from the records (no separate checker), and the 8-part run's summary was rebuilt after
the run was stopped.
