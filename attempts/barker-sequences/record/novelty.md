# Novelty check

Statement checked (the claim of `problem.json`): for every u in the Borwein-Mossinghoff list L of 237,807 integers, no Barker sequence of length 4u^2 exists.

## Queries (by statement, not by name)

| date | source | query | hits |
|---|---|---|---|
| 2026-09-02 | arXiv | `ti:"Barker sequences" OR ti:"circulant Hadamard"` (date order) | 14; the only one about the list is 1306.0045 |
| 2026-09-02 | arXiv | `"Wieferich" AND ("circulant Hadamard" OR "Barker")` | 1306.0045 only |
| 2026-09-02 | arXiv | `ti:"anti-field-descent"` | none (paper not on arXiv) |
| 2026-09-02 | Semantic Scholar | citations of 1306.0045 (27) and of the anti-field-descent paper (16) | Leung-Schmidt 2016 (DOI 10.1016/j.jcta.2015.11.005) is the only paper that acts on the list |
| 2026-09-02 | Crossref | DOIs 10.1112/S1461157013000223, 10.1016/j.jcta.2015.11.005, 10.1007/s10623-011-9493-1 | records confirmed |
| 2026-09-02 | zbMATH Open | `ti:Barker py:2015-2026`; `au:Gallardo ti:circulant Hadamard` | Schmidt-Willms 2016, Willms 2021, Yu 2023 (none touches the list); Gallardo's 2014 claims exist only as arXiv records |
| 2026-09-02 | web search | "Barker sequence length lower bound 4*10^33"; "anti-field-descent Barker 8125 open cases" | no later bound than Leung-Schmidt 2016 found |
| 2026-09-02 | Wayback Machine | captures of cecm.sfu.ca/~mjm/WieferichBarker (2009-2016) and wayback.cecm.sfu.ca/~mjm/WieferichBarker (2021) | the data page was last modified 2013-05-31; it records no elimination beyond the 2014 paper |
| 2026-09-02 | formal-conjectures | code search "Barker", "circulant Hadamard" | both conjectures formalised and tagged research open |

## Verdict

- The statement for the whole of L is not in the literature: 229,682 of the 237,807 values are settled by Leung-Schmidt 2016 (Theorem 6.3); 8,125 are open, and their list is unpublished.
- The statement for the 19 values with n <= 10^50 and for the whole range 13 < n <= 4*10^33 is in the literature (Leung-Schmidt 2016, Table 1 and Theorem 6.4).
- Nothing in print applies Turyn's test to the values with Omega(u) >= 9, Leung-Schmidt 2012 Thm 3.1 to Omega(u) >= 7, or Leung-Schmidt 2016 Theorem 6.1 in its general form, to the survivors.
- The attack continues on the claim as stated; the residue it works on is the 8,125 survivors, which it must first reconstruct. Unit-level queries are recorded below when units are declared.
