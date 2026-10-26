# Problem-level study: Barker lengths n = 4u^2 for u in the Borwein-Mossinghoff list L

Date of the study: 2026-09-02 (local), sources under `../_sources/` (relative to the attack root).

## 1. Queries run

| # | source | query | date | result |
|---|---|---|---|---|
| 1 | arXiv (API through the arxiv MCP tool) | `ti:"Barker sequences" OR ti:"circulant Hadamard"`, sorted by date | 2026-09-02 | 14 papers (2012-2024) |
| 2 | arXiv | `"Wieferich" AND ("circulant Hadamard" OR "Barker")` | 2026-09-02 | 1 paper: 1306.0045 |
| 3 | arXiv | `ti:"anti-field-descent"` | 2026-09-02 | 0 papers (the paper is not on arXiv) |
| 4 | arXiv | `au:Schmidt AND au:Leung AND (descent OR "circulant Hadamard" OR Barker)` | 2026-09-02 | request timed out; not repeated because the paper was found through Crossref and the author's site |
| 5 | Semantic Scholar | relevance search "Wieferich pairs and Barker sequences II" | 2026-09-02 | HTTP 429 (rate limit); replaced by the citation call below |
| 6 | Semantic Scholar | citations of paper 7ef8496b217dc3d99f73bedb494a454e74ab65f5 (Borwein-Mossinghoff 2014) | 2026-09-02 | 27 citing records |
| 7 | Semantic Scholar | citations of paper c8367eb2f9b0fc8ea4957047c3c13ccfc78b5bb1 (Leung-Schmidt 2016) | 2026-09-02 | 16 citing records |
| 8 | Crossref | `works/10.1112/S1461157013000223`, `works/10.1016/j.jcta.2015.11.005`, `works/10.1007/s10623-011-9493-1` | 2026-09-02 | venue, pages, year, cited-by counts (12, 11, 22) |
| 9 | zbMATH Open | `ti:Barker py:2015-2026` | 2026-09-02 | 10 records, 3 on Barker sequences |
| 10 | zbMATH Open | `au:Gallardo ti:circulant Hadamard` | 2026-09-02 | 5 records (2 arXiv-only) |
| 11 | web search | "Mossinghoff WieferichBarker Barker sequence candidates data"; "Mossinghoff Double Wieferich circulant Hadamard"; "Barker sequence length lower bound improved 4*10^33"; "Leung Schmidt New restrictions on possible orders of circulant Hadamard matrices pdf"; "BarkerCandidates100"; "anti-field-descent Barker 8125 open cases" | 2026-09-02 | data page URL, Logan-Mossinghoff 2017 reference, LS12 and LS16 PDFs on the author's site |
| 12 | Wayback Machine CDX | `cecm.sfu.ca/~mjm/WieferichBarker/*` (all captures), `wayback.cecm.sfu.ca/~mjm/WieferichBarker/*` | 2026-09-02 | the data files; `BarkerCandidates100.txt.gz` exists only in the capture 20210718130442 of the second host |
| 13 | formal-conjectures repository | `gh search code "Barker"`, `gh search code "circulant Hadamard"` in google-deepmind/formal-conjectures | 2026-09-02 | `FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean`, `FormalConjectures/Arxiv/2402.13202/CirculantHadamard.lean` |
| 14 | problem database | none: the problem has no database of its own (it is not an Erdős problem) | 2026-09-02 | - |

## 2. Hits worth reading

| identifier | what it did | read |
|---|---|---|
| arXiv:1306.0045 / DOI 10.1112/S1461157013000223, Borwein-Mossinghoff, LMS J. Comput. Math. 17 (2014) 24-32 | the list L of 237,807 values and Table 100 (which test was run for which Omega(u)); Theorems 2, 4, 5, 6, 7 and Corollary 3 restated | full text (LaTeX source, `_sources/bm2/main`) |
| DOI 10.1007/s10623-009-9301-3, Mossinghoff, Des. Codes Cryptogr. 53 (2009) 149-163 | the directed-graph method; Turyn's test with explicit (r, s, j) witnesses for the 2009 cases | full text (PDF, `_sources/Moss09.txt`) |
| DOI 10.1007/s10623-011-9493-1, Leung-Schmidt, Des. Codes Cryptogr. 64 (2012) 143-151 | Theorems 3.1, 3.5, 3.10; Definition 2.10 of F(m, n) with m_q = 4 * (odd q-free squarefree part) when m is even | full text (PDF from the author's site, `_sources/LS12.txt`) |
| DOI 10.1016/j.jcta.2015.11.005, Leung-Schmidt, J. Combin. Theory Ser. A 139 (2016) 87-131 | the anti-field-descent method; Theorems 3.5, 4.7, 5.4, 6.1, 6.3; Thm 6.4 (no Barker sequence with 13 < n <= 4*10^33); Table 1 (the 19 cases n <= 10^50); 229,682 of the 237,807 cases ruled out by Thm 6.3, survivors unpublished ("available from the authors upon request"), smallest survivor 30109*1128713*2167849*268813277 | full text (PDF from the author's site, `_sources/LS-chdmII.txt`); Sections 1, 2, 6 read in full, Sections 3-5 only the theorem statements |
| DOI 10.1007/s10623-004-1703-7, Leung-Schmidt, Des. Codes Cryptogr. 36 (2005) 171-188 | the field descent method (Theorem 5 of the 2014 paper is its Cor. 4.5) | downloaded (`_sources/LS-field.txt`), not read |
| Mossinghoff's data page, Wayback capture 2021-07-18 of http://wayback.cecm.sfu.ca/~mjm/WieferichBarker/ | the files `BarkerCandidates100.txt.gz` (237,807 values with factorisations), `Top19_BarkerCands.txt`, `Omega4/5/6_BarkerCands.txt`, `CHM_Candidates.txt`, `CHM_Exclusions.txt`, `AllCycles.txt`, the Wieferich-pair files | read; the list validated against Table 100 (counts per Omega(u) identical; 148 distinct primes, largest 462147547073; 64,904 non-squarefree values) |
| arXiv:1501.06035 / DOI 10.1007/s10623-015-0104-4, Schmidt-Willms 2016 | the odd case, new proof | abstract |
| arXiv:2104.00502, Willms 2021 | a symmetry of even-length Barker sequences; no length restriction | abstract |
| DOI 10.5802/crmath.428, Yu 2023 | Barker sequences and the L1 norm of Littlewood polynomials; no length restriction | title and venue |
| J. Combin. Math. Combin. Comput. 101 (2017) 145-156, Logan-Mossinghoff | double Wieferich pairs and circulant Hadamard matrices; the data files `AscWiefPairs_DWPCHM.txt`, `CHM_Candidates_DWPCHM.txt` | title, venue, file headers |
| arXiv:1411.2201, arXiv:1411.2203, Gallardo 2014 | claims that no circulant Hadamard matrix of order 4h^2 exists for 1 < h < 10^13 and that ord_{n/p^a}(p) is odd; zbMATH holds them as arXiv-only records; Leung-Schmidt 2016 still calls u = 11715 the smallest open case | abstracts |
| arXiv:2302.08346 (Morris 2023), arXiv:1907.12683 (Orozco Lopez 2019) | claimed proofs of Ryser's conjecture; no journal record, no citing paper adopts them | abstracts |
| `FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean` | `IsBarkerSequence (a : List Z)`: every entry is 1 or -1, and for every k with 0 < k < a.length, the aperiodic autocorrelation (zipWith product of a and a.drop k, summed) has absolute value at most 1; `barker_conjecture`: IsBarkerSequence a implies a.length <= 13, tagged research open | read in full |
| `FormalConjectures/Arxiv/2402.13202/CirculantHadamard.lean` | `circulant_hadamard_conjecture`: a circulant Hadamard matrix (real entries, `Hadamard.IsHadamard'`) has order at most 4, tagged research open | read in full |

## 3. What was learned, as constraints on the plan

1. Canonical statement. The formal statement is `barker_conjecture` in `BarkerSequence.lean`. Read against `claim` quantifier by quantifier: the claim quantifies over u in L (finite, explicit) and over lists a of +1/-1 entries with a.length = 4u^2, and asserts that some k with 0 < k < a.length has |C_k(a)| >= 2, which is the negation of the second conjunct of `IsBarkerSequence` for that a. So the claim is the conjunction over u in L of the instances "no a with IsBarkerSequence a and a.length = 4u^2" of the contrapositive of `barker_conjecture`. The Lean file's `aperiodicAutocorrelation` sums a_i a_{i+k} over i from 0 to length-1-k, which is the c_k of Borwein-Mossinghoff up to the indexing of the sequence. No misformalisation found.
2. A route already in print. Leung-Schmidt 2016 applied Theorem 6.3 (anti-field-descent, prime-power case u/m = q^b) to all 237,807 values and ruled out 229,682. Re-running Theorem 6.3 is therefore not a result; it is the reconstruction of the unpublished survivor list (8,125 values), and reproducing the published count 229,682 is a validation of the implementation, not a unit.
3. Routes that stopped and where. Turyn's self-conjugacy test (Thm 2 of BM 2014) was run only for Omega(u) <= 8 because the implementation (Sage) enumerated divisor pairs (r, s), exponential in Omega(u). Leung-Schmidt 2012 Thm 3.1 was run only for Omega(u) <= 6 for the same reason. Leung-Schmidt 2012 Thm 3.5 was run on all values (4 eliminated). None of these has been run on the 8,125 survivors of Theorem 6.3 with Omega(u) >= 9 (Turyn) or >= 7 (Thm 3.1). Theorem 6.1 of Leung-Schmidt 2016 (the general form, u/m not a prime power, free integer t) was not applied to the list at all; Remark 6.2 says how the parameters are chosen.
4. Settled ranges. No Barker sequence of length 13 < n <= 4*10^33 (LS 2016 Thm 6.4). The 19 list values with n <= 10^50 are settled (LS 2016 Table 1). The sublist Omega(u) <= 6 (541 values) has had every BM 2014 test; Omega(u) <= 8 has had Turyn's test.
5. Tools. No code was published by either group; BM 2014 names Sage for Turyn's test and Maple (2009) for the F(m) check; LS 2016 names no system. No independent checker exists in print for any of the eliminations. The primes in L are 148 distinct primes, all below 4.7*10^11, so every multiplicative order needed (orders modulo primes and prime squares) is computable by factoring p - 1 by trial division, and the Wieferich and 2-adic-order data can be tabulated once for all 148 primes.
6. Incompleteness caveat. The list L is complete only up to n = 4*10^33 (the graph D(10^16.5) was not extended); clearing part or all of L therefore yields "no Barker sequence of length 4u^2 for these u", not a new lower bound on n. Every unit's statement is about the listed u.
7. Unverified claims. The Gallardo, Morris and Orozco Lopez preprints are not used as known results; if any were correct the statement would already follow, so they are recorded and set aside.

## 4. Stop reason

Every tier-one source was queried at least once (arXiv, Semantic Scholar, Crossref, zbMATH; no problem database exists). The last two queries with new information were the Semantic Scholar citations of Leung-Schmidt 2016 and the zbMATH title search; both returned nothing beyond what the 2016 paper already settles, so the queries ran dry.
