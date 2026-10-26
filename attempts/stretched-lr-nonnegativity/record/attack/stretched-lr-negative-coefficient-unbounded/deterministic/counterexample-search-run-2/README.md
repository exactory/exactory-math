# counterexample-search-run-2: the transportation-polytope image family (class S4)

Date: 2026-09-04. Entry: test-strengthenings-by-counterexample (plan step 4 of
attack-the-negative-side), action 2: small instances of a translated statement. Step kind:
counterexample search run (structured enumeration of a finite family).

## The translated statement

Ferudun 2026 (Section 6, "The general frontier") records that realising k disjoint horizontal
strips as a skew shape identifies the lattice points of a k x N transportation polytope
T(r, c) with the Littlewood-Richardson tableaux of a fixed triple, compatibly with dilation;
for k = 3 the example r = (3, 3, 3), c = (2, 1^7) is the triple lam = (9, 6, 3),
mu = (9, 9, 7, 6, 5, 4, 3, 2, 1), nu = (15, 12, 9, 7, 6, 5, 4, 3, 2, 1) (their notation,
1050 tableaux). So "every k x N transportation polytope with integer margins is Ehrhart
positive" is a statement implied by King-Tollu-Toumazet positivity, and a transportation
polytope with a negative Ehrhart coefficient would refute the conjecture. The tool
`transport.py` (margin equations and nonnegativity, Normaliz) reproduces the published
values for that example: L(1) = 1050, a_1 = 2157/280, minimal coefficient
128114573/29059430400 (a 40-minute computation, dimension 14), and the Birkhoff polytope
B_3 (1 + 9t/4 + 15t^2/8 + 3t^3/4 + t^4/8); its counts at t = 1, 2, 3 agree with a brute-force
contingency-table count on four families.

## Families enumerated (`run_all.sh`, every pair of sorted margins up to the total)

| family | margins total | pairs | dimension | negatives | minimal coefficient ratio to the unimodular simplex | time |
|---|---|---|---|---|---|---|
| 3 x 4 | <= 16 | 2,297 | <= 6 | 0 | 60/49 (r = (2,1,1), c = (1,1,1,1)) | 11 s |
| 3 x 5 | <= 14 | 995 | <= 8 | 0 | 2975/2283 | 32 s |
| 3 x 6 | <= 12 | 280 | <= 10 | 0 | 9996/7381 | 171 s |
| 4 x 4 | <= 14 | 1,356 | <= 9 | 0 | 9100/7129 | 172 s |
| 4 x 5 | <= 11 | 227 | <= 12 | 0 | 9625/6617 | 2,189 s |
| 5 x 5 | <= 8 | 15 | <= 16 | 0 | 3628625/2436559 (the Birkhoff polytope B_5, r = c = (1^5); its leading coefficient 188723/836911595520 is the known volume of B_5) | 8,607 s |

A first 5 x 5 run with total <= 9 (40 pairs) computed 34 pairs in 2.5 hours and was stopped
at the six heaviest; its record file was deleted by mistake before it was read, so nothing
from it is claimed. The family was rerun with total <= 8 (`t5x5`).

Every polynomial has period 1 (transportation polytopes with integer margins are lattice
polytopes) and every coefficient is at least 1.2 times the unimodular-simplex value; the
minima are attained at the smallest margins (near the Birkhoff-type polytopes).

## Independent check (`check.sh`)

For a seeded sample of pairs (and every family's minimal-ratio pair), a brute-force
contingency-table count at t = 1, 2 (and t = 3 when the count is below 10^7), written from
the definition with no polytope code, must equal the recorded polynomial's values; the
summaries' pair counts must equal the number of records.

## What the run decided

Evidence: no k x N transportation polytope in these families has a negative Ehrhart
coefficient, so the strip transfer produces no counterexample from them; the family behaves
like the 3 x 8 family of Ferudun 2026 (positive, minima near the unit-margin members).

## Correction (2026-09-04)

The strip construction of Ferudun 2026 is stated for three disjoint horizontal strips, that is
for 3 x N transportation polytopes; the sentence above that extends it to k x N was this
record's own generalisation and is not in print. The 3 x 4, 3 x 5 and 3 x 6 families of this
run are established images of Littlewood-Richardson polytopes; the 4 x 4, 4 x 5 and 5 x 5
families are transportation polytopes searched as neighbouring polytopes, and a negative member
among them would refute the conjecture only if the construction extends to four or five rows.
