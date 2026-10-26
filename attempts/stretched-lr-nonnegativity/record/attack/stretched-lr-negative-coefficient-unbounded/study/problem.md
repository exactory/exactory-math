# Problem-level study: the King-Tollu-Toumazet positivity conjecture (unbounded)

Date: 2026-09-04. This attack continues the box attack in the sibling workspace
`attack/stretched-lr-polynomial-negative-coefficient` (same directory, opened 2026-09-03),
whose problem-level study (`study/problem.md`, 17 queries) and novelty record cover the same
statement without the box. The queries and hits below are those records plus the queries
run since; the fetched documents stay under the sibling's `study/sources/`.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| U0 | the sibling attack's record | `study/problem.md` queries Q1-Q17 (arXiv Q1-Q3, Semantic Scholar citations of KTT 2004 and of 2607.22301, Crossref, zbMATH, MathOverflow, web search, the Epoch page and PDF, the ktt-positivity repository, Mathlib code search) | 2026-09-03 | no counterexample in print; conjecture open; positivity proved for length <= 4 |
| U1 | zbMATH Open | `Ehrhart positivity negative coefficients` and documents 7040477, 8137114, 7079186, 902723871, 7064989 | 2026-09-03 | the negative-Ehrhart families in print (sibling `study/reduce-and-translate.md`) |
| U2 | Crossref and Semantic Scholar | DOI 10.1016/j.jcta.2008.06.005 (KTT 2009 factorisation); DOI 10.46298/dmtcs.3592 (Cho-Jung-Moon 2008) | 2026-09-03 | the factorisation theorem's statement (Theorem 1.3 of the DMTCS paper, PDF read in full) |
| U3 | the sibling attack's computations | enumeration-run-2, -3, -4 and certified-special-case-check-1 | 2026-09-03/04 | the box (length <= 7, size <= 30) has no negative coefficient: 6,855,302 polynomials, none negative; the 5-part part pinned by two implementations |
| U4 | arXiv API | every query since Q3 | 2026-09-03/04 | refused (HTTP 503 rate limit); items reached through arxiv.org/abs pages and zbMATH |

Formal statement: none (not an Erdos problem; no Mathlib definition of the objects).

## 2. Hits worth reading

Those of the sibling record (Ferudun 2026 and its repository, full text; KTT 2004/2006/2009;
Knutson-Tao; Derksen-Weyman; Rassart; Ikenmeyer; Sherman; De Loera-McAllister; the Epoch
PDF; Jochemko-Menon 2026; Liu-Tsuchiya 2019; Liu-Xin-Zhang 2026; Castillo et al. 2018;
Hibi-Higashitani-Tsuchiya-Yoshida 2019; Cho-Jung-Moon 2008), plus what the box attack
produced: the h*-expansion of a_1 (a negative linear coefficient needs h*-mass at even or
high indices against small h*_1 and small odd entries), the observation that inside the box
the only sub-simplex structures are volume-2 empty simplices (coefficient ratio 24/25), and
the observation that the minimal a_1 per dimension is exactly the unimodular-simplex value
H_D wherever those simplices are absent.

## 3. What was learned, as constraints on the plan

1. The claim is open; no argument reaches it either way. The recorded routes: the local
   Berline-Vergne formula (positive side, stuck at (HTE)); exhaustive and random search
   (negative side, no hit up to the box and in Ferudun's ~4 x 10^8-triple search); one
   transfer route (transportation polytopes), valid but landing in a positive family.
2. Settled ranges the negative side must avoid: length <= 4; the box length <= 7 and
   size <= 30; c <= 2; for full-dimensional 5-part hives everything but a_1.
3. Structure to exploit on the negative side: piecewise linearity of a_1 in (lam, mu, nu)
   (Rassart), so a chamber with a negative a_1 has integer points of every size and the
   search can move along a_1's descent directions instead of enumerating; the KTT
   factorisation, so only primitive triples matter; the h*-expansion, so the negative-leaning
   shapes are few lattice points against large volume, which the box shows do not occur
   below volume 2 at any dimension up to 13.
4. Tools in hand: `tools/hivepoly.py` (Normaliz Ehrhart polynomials, milliseconds to
   seconds), `tools/horn.py` (essential Horn triples and primitivity), `tools/descent.py`
   (a_1 descent, first version), lrcalc and `tools/lrtableaux.py` as independent counters.
5. Routes not to duplicate: the 3 x 8 transportation family; random small-size sampling at
   5 parts; anything inside the box.

## 4. Stop reason

The sibling's tier-one floor and tier-two sources were reached on 2026-09-03; the queries
since (zbMATH, Crossref, Semantic Scholar) added the negative-Ehrhart families and the
factorisation theorem's statement; the arXiv API stayed rate-limited; the last two productive
sources changed nothing about the state of the claim.
