# Strategy study: reduce-and-translate at the root

Date: 2026-09-05. The strategy's step 1 asks where the statement has been carried into another
language before, what that bought, and which translations are already in print.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| T1 | arXiv (MCP search) | `"h* vector" AND "Littlewood-Richardson"` | 2026-09-05 | 0 results |
| T2 | arXiv (MCP search) | `"Ehrhart positivity" AND polytope`, 10 of 23 read | 2026-09-05 | the Ehrhart-positivity literature: Liu's survey 1711.09962; Ferroni and Higashitani's exposition of inequalities on Ehrhart and h* coefficients 2307.10852; Castillo, Liu, Nill and Paffenholz on smooth polytopes with negative Ehrhart coefficients and on Berline-Vergne valuations as the tool 1704.05532; Liu and Tsuchiya's non-Ehrhart-positive order polytope in dimension 21, 1806.08403; order polytopes of dimension at most 13 are Ehrhart positive, 2412.07164; Ehrhart positivity for marked order polytopes 2604.08394 and for lattice path matroids 2605.22673 |
| T3 | arXiv (MCP search) | `"stretched" AND ("Littlewood-Richardson" OR "Kostka") AND polynomial`, 10 of 11 read | 2026-09-05 | Thawinrak 2211.06810 (polynomiality, short proof); Rassart and Derksen-Weyman already in the record; McAllister math/0603173 and Gao-Gao 2210.10158 on degrees of stretched Kostka quasi-polynomials; Kirillov 1505.01542 on unimodality and log-concavity of stretched parabolic Kostka polynomials; Coquereaux and Zuber 1706.02793 on hive polytope volumes; King 2101.00984 on stretched Newell-Littlewood coefficients |

Semantic Scholar was rate-limited on the first attempt and was not retried.

## 2. What was learned, as constraints on the plan

1. **The h* basis is the standard language of this question and it has not been pointed at this
   statement.** The Ehrhart-positivity literature works almost entirely in the h* basis, where the
   inequalities that are actually known live (Stanley's nonnegativity, Hibi's lower bound,
   monotonicity, unimodality under extra hypotheses), and Ferroni and Higashitani 2307.10852 is a
   survey of exactly those. Query T1 returned nothing, so no paper found here connects the h*
   vector to stretched Littlewood-Richardson coefficients.
2. **Ehrhart positivity is false in general and the failures are understood.** Liu and Tsuchiya
   exhibit a non-Ehrhart-positive order polytope in dimension 21, and Castillo, Liu, Nill and
   Paffenholz produce smooth polytopes where every coefficient that can be negative is. So a
   translation into the h* basis cannot be expected to make the statement follow from a general
   theorem; it can only make precise what the hive polytopes must satisfy that a general polytope
   need not.
3. **Berline-Vergne valuations are the standard tool on the other side**, and 1704.05532 uses them
   for the same purpose this project does, which supports the choice of route and says the tool is
   not exotic.
4. **The neighbouring stretched families are studied for different properties.** Unimodality and
   log-concavity for stretched parabolic Kostka polynomials (Kirillov), degrees for stretched
   Kostka quasi-polynomials (McAllister, Gao and Gao), volumes of hive polytopes (Coquereaux and
   Zuber). None of these is coefficient positivity for the stretched Littlewood-Richardson
   polynomial, which is the statement here.

## 3. Stop reason

The three questions the strategy's step 1 asks are answered: the destination language is the h*
basis, what it buys is the body of known h* inequalities, and nothing in print applies it to this
statement. The queries ran dry on the specific connection at T1.
