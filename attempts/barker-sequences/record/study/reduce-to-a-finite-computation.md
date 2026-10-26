# Strategy-level study: reduce-to-a-finite-computation on the Barker list L

Date: 2026-09-02 (local). This record answers how the statement was finitised and computed before, on this problem and its circulant Hadamard neighbour, and settles the three things step 1 of the plan asks for: the last value settled by computation with its encoder and solver, whether each certificate had an independent checker, and the residue in print with where its completeness argument stopped.

## 1. Queries run

| # | source | query | date | result |
|---|---|---|---|---|
| 1 | arXiv API | `abs:"self-conjugate" AND (abs:Hadamard OR abs:Barker OR abs:"difference set")`, date order, 25 max | 2026-09-02 | 2 papers; 2608.22936 (signed difference sets, 2026) does not touch circulant Hadamard orders |
| 2 | zbMATH Open | `ti:"circulant Hadamard" py:2012-2026` | 2026-09-02 | 13 records; the computational ones are Leung-Schmidt 2012 and Logan-Mossinghoff 2017; the rest are unrefereed claims (Orozco Lopez, Morris, Gallardo 2014) or unrelated (block-circulant, complex, determinantal) |
| 3 | Crossref | `query.bibliographic=circulant Hadamard matrices open cases self-conjugacy Barker`, 8 rows | 2026-09-02 | nothing computational beyond the records already held (a 2005 thesis 10.5353/th_b3121182 on cyclic Menon difference sets, block-circulant and complex variants) |
| 4 | Semantic Scholar | citations of DOI 10.1007/s10623-011-9493-1 (Leung-Schmidt 2012) | 2026-09-02 | 2 records: Gallardo 2016 (Electron. J. Combin., DOI 10.37236/5237) and an unrelated matrix-completion paper |
| 5 | the problem-level study (`study/problem.md`) | the same sources, queried by statement | 2026-09-02 | the three computational papers (Mossinghoff 2009, Borwein-Mossinghoff 2014, Leung-Schmidt 2016) and the data files |

## 2. Hits worth reading

| identifier | what it did for the finite computation | read |
|---|---|---|
| Mossinghoff 2009 (DOI 10.1007/s10623-009-9301-3), Section 3 | the finitisation: F(m) = m^2 is forced for m <= 10^15 (the product over primes of (1 - 1/q)^-1 stays below 1.7), so each prime p of m needs a source q (Wieferich pair or p dividing ord_{m/q}(q)); the candidates are induced subgraphs of the directed graph D with every vertex of positive indegree; cycles by Tarjan's algorithm, augmentation by a bounded recursion, the final F(m) check in Maple; Turyn's test applied by hand with explicit (r, s, j) | full text |
| Borwein-Mossinghoff 2014 (arXiv:1306.0045), Sections 3-4 | the same pipeline with D(10^16.5); Turyn's test in Sage for Omega(u) <= 8, Thm 3.1 for Omega(u) <= 6, Thm 3.5 for all; the list L published as data; the incompleteness of L above 4*10^33 stated by the authors | full text |
| Leung-Schmidt 2016 (DOI 10.1016/j.jcta.2015.11.005), Section 6 and Tables 1-2 | Theorem 6.3 run on all 237,807 values (229,682 eliminated) and on the 1371 circulant Hadamard cases (423 eliminated); Table 1 lists, for the 19 cases n <= 10^50, the certificate (p, q^b, d, q^4b, ord_p(q), max, LHS/RHS); the survivors' data "available upon request"; Remark 6.2 gives the parameter search: every p, m as large as (101) allows, t with ord_p(t) as large as (102) allows | full text of Sections 1, 2, 6 |
| Leung-Schmidt 2012 (DOI 10.1007/s10623-011-9493-1), Remarks 3.3 and 3.7 and Example 3.2 | Theorem 3.1 rules out 135 and Theorem 3.5 22 of Mossinghoff's 1576 circulant Hadamard cases u <= 10^13; the triples [u, w, m] and quadruples [u, p, m, r] are on Schmidt's data page https://personal.ntu.edu.sg/bernhard/CW/CW.html | full text |
| Mossinghoff's data files (Wayback capture 2021-07-18) | `CHM_Exclusions.txt`: 22 circulant Hadamard values eliminated by Turyn's test after the 2012 paper, with no certificate printed; `Top19_BarkerCands.txt`, `Omega4/5/6_BarkerCands.txt`: the values that passed every test | read |
| Gallardo 2016 (Electron. J. Combin. 23(1) P1.59, DOI 10.37236/5237) | a refereed paper citing Leung-Schmidt 2012; its statements concern a duality operator and special cases of Ryser's conjecture; not a computation on L (see the problem-level study for Gallardo's unrefereed 2014 claims) | abstract requested; recorded here as a hit to be read if a route through it opens |

## 3. What was learned, as constraints on the plan

1. The last value settled by computation. On L: every value with Omega(u) <= 6 has had all six tests of BM 2014 plus Theorem 6.3; Omega(u) <= 8 has had Turyn's test; all 237,807 have had Thm 3.5, Theorem 5, Corollary 3, Theorem 7 and Theorem 6.3. The encoder and solver: hand-written Sage (Turyn) and Maple (F(m)) scripts, unpublished; Leung-Schmidt name no system. So the settled part of L is exactly: the 229,682 values of Theorem 6.3 (whose certificates are unpublished except 19 + 20 examples) and, inside the survivors, nothing.
2. Independent checkers. None in print. Every elimination on L rests on one unpublished implementation. A certificate (the parameter tuple) is short and can be re-verified by a separate program with exact arithmetic; this attack must supply that checker itself.
3. The residue in print. The residue is the 8,125 survivors of Theorem 6.3, not published; the attack reconstructs it from L by re-implementing Theorem 6.3 with the parameter search of Remark 6.2, and the reconstruction is validated by the published count 229,682 and the published smallest survivor 30109*1128713*2167849*268813277. Its completeness argument is the list itself: every u < 5*10^49 built from the graph D(10^16.5) that passes Corollary 3, Theorem 5 and Theorem 7 is in L (BM 2014, Section 4.2); L's own completeness stops at 4*10^33, which the units must state.
4. Routes not to duplicate. Theorem 6.3 as published (u/m a prime power) is the route in print; the attack applies it only to reconstruct the residue. Turyn's test on Omega(u) <= 8, Thm 3.1 on Omega(u) <= 6 and Thm 3.5 everywhere are in print; the attack's contribution is these tests on the survivors with Omega(u) >= 9 (respectively >= 7), and Theorem 6.1 in general form.
5. Tool the route needs and this problem has. Every test needs multiplicative orders modulo the 148 primes of L (all < 4.7*10^11) and modulo their squares: p - 1 factors by trial division at once, so orders are exact; self-conjugacy needs only the 2-adic valuation of ord_q(p), which is the number of squarings of p^((q-1)/2^s) modulo q until 1. So the exponential enumeration of divisor pairs that stopped BM 2014 at Omega(u) <= 8 can be replaced by an enumeration over prime supports with exponents fixed at their maximum (Turyn's bound is monotone in the exponents once the prime supports are fixed, since self-conjugacy modulo q^e for odd q does not depend on e >= 1 and 4 never divides s when every prime of r is 1 mod 4), which is 2^omega(u) <= 2^15 subsets per value.
6. A value already settled by computation that bounds the plan. The 19 values with n <= 10^50 are settled, so the smallest open n is 4u^2 with u = 30109*1128713*2167849*268813277 = 19804304830012264298738041 (n about 1.57*10^51); any unit stating a range must start above 10^50.

## 4. Stop reason

The queries ran dry: the arXiv self-conjugacy query and the Crossref bibliographic query returned nothing new across the sources, after the zbMATH and Semantic Scholar queries had returned only records already held.
