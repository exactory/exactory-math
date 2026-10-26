# certified-special-case-check-4: census of coefficient ratios and h*-vectors over the box

Date: 2026-09-04. Written at stage 8, after the independent reader of the unit drafts asked for
a recorded count behind the near-miss claims (the READMEs of runs 2 to 4 recorded the minimal
ratio and the number of volume-2 few-point polytopes, not that every other polynomial has every
coefficient at least the simplex value, nor that the ratio 24/25 occurs only in dimension 4).
Step kind: certified special-case check (exact rational arithmetic in two independent
implementations over a finite list). Not a journal move: the attack was stalled; the step only
tabulates the polynomials the journalled runs computed.

## Inputs

The 6,855,302 polynomial records of `enumeration-run-2` (1,334,669; coefficient strings and
the vertex count `nverts`), `enumeration-run-3` (4,217,762) and `enumeration-run-4`
(1,302,871): every canonical triple of largest length 5 or 6 with c >= 3 and dim H >= 3, and
every primitive one of largest length 7, in the box (length <= 7, size <= 30).

## What is computed (`census.py`)

For each polynomial P of degree D, from its coefficients alone and in exact rational
arithmetic: s_k = [t^k] binom(t + D, D), the coefficients of the unimodular D-simplex (by
expanding the product (t + 1)...(t + D)/D!); the ratios a_k / s_k for k = 1..D and their
minimum; the normalized volume V = D! a_D; the h*-vector h*_i = sum_{j <= i} (-1)^j
binom(D + 1, j) P(i - j). Outputs: `census.summary.json` (per number of parts: the counts of
polynomials, of minimal ratio < 1 and of minimal ratio = 24/25; the histogram of
(D, h*, V, minimal ratio) over the polynomials with minimal ratio < 1; the number of
polynomials with h*_1 = 0, that is with exactly D + 1 lattice points, per (D, V); the largest V
among those and among the polynomials with c <= D + 2; at 5 parts the vertex counts of the
polynomials with minimal ratio < 1) and `census.below1.jsonl` (every polynomial with minimal
ratio < 1). 796 s on 6 workers.

## Result

| parts | polynomials | ratio < 1 | of which ratio 24/25 | keys of the ratio < 1 records (D; h*; V; minimal ratio: count) | largest V with D + 1 points | largest V with c <= D + 2 |
|---|---|---|---|---|---|---|
| 5 | 1,334,669 | 304 | 304 | (4; 1,0,1,0,0; 2; 24/25): 304, all with 7 vertices | 2 | 3 |
| 6 | 4,217,762 | 4,186 | 3,088 | (4; 1,0,1,0,0; 2; 24/25): 3,088; (5; 1,0,1,0,0,0; 2; 44/45): 1,098 | 2 | 10 |
| 7 | 1,302,871 | 2,979 | 151 | (4; 1,0,1,0,0; 2; 24/25): 151; (5; 1,0,1,0,0,0; 2; 44/45): 1,632; (6; 1,0,1,0,0,0,0; 2; 799/812): 1,196 | 2 | 10 |

So exactly 7,469 computed polynomials have a coefficient below the simplex value, all with
D + 1 lattice points, normalized volume 2 and h*-vector (1, 0, 1, 0, ...), in dimensions 4, 5
and 6 with minimal ratios 24/25, 44/45 and 799/812 (the linear-coefficient ratios are 24/25,
134/137 and 145/147; in dimensions 5 and 6 another coefficient is relatively smaller). Every
other computed polynomial has every coefficient at least the simplex value; the minimal ratio
over the box's computed polynomials is 24/25. The polynomials with D + 1 lattice points have
normalized volume 1 (unimodular) or 2 and nothing larger; counts per (D, V) are in the summary.
Every polynomial with a coefficient below the simplex value has exactly D + 1 lattice points and volume 2; among the polynomials with at most D + 2 lattice points the largest normalized volume is 3 at 5 parts and 10 at 6 and 7 parts, and those with exactly D + 2 points, like every polynomial of volume other than 2, have every coefficient at least the simplex value.

Correction to the earlier records: runs 1 to 4 called the volume-2 few-point polytopes "empty
non-unimodular simplices" from their Ehrhart polynomial (that of an empty lattice simplex of
volume 2); the vertex counts of run 2 show that at 5 parts each of the 304 has 7 vertices, so at 5 parts they are not simplices; runs 3 and 4 recorded no vertex counts; run 1's sample (`enumeration-run-1`, field `nverts`) holds 12 six-part and 28 seven-part ones (dimensions 4 and 5, with 7 and 8 vertices, so not simplices), and the rest, including every dimension-6 one, are not known either way. Nothing in the record depends on their being simplices.

## Independent check (`check.sh` -> `check.py`, `result.json`)

The second implementation recomputes everything from the raw records by different formulas
(the simplex coefficients as unsigned Stirling numbers of the first kind, s_k = c(D+1, k+1)/D!;
the h*-vector by D + 1 successive multiplications of the value series by (1 - z)), rebuilds
every aggregate of `census.summary.json` and the histogram of `census.below1.jsonl`, and
compares. Trusted base: Python integers and Fractions and the records of runs 2 to 4 (whose
polynomials checks 1 to 3 certify).

## What the step decided

The near-miss structure of the box's computed polynomials, as a census with two agreeing
implementations: the statements of the Result section above, and nothing about the polytopes of
dimension at most 2 or the factorised 7-part products, which are outside the records.

Result of the check: `result.json` status pass (2026-09-04); the second implementation rebuilt every
aggregate of the census and the below-1 histogram with 0 disagreements.
