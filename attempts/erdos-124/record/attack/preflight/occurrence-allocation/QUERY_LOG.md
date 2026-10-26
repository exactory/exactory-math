# Occurrence-allocation preflight query log

Date: 2026-09-08. Status: pre-admission literature study only.
Stop reason: fixed24 discovery queries or registry requests reached. Source
opens and inspection of identified primary results follow this sweep.
Failed or noisy searches are not successful metadata checks.

1. arXiv. Query: `site:arxiv.org "complete" "sublacunary" "subset sums"`. Outcome: No useful new target result.

2. Semantic Scholar. Query: `site:semanticscholar.org "complete" "powers" "Fourier" sums`. Outcome: Unrelated search hits; none imported.

3. Crossref. Query: `site:api.crossref.org "Bergelson" "Simmons" "Complete"`. Outcome: No usable registry record.

4. zbMATH. Query: `site:zbmath.org "Complete" "Sublacunary" sets`. Outcome: No useful exact hit.

5. Erdos database. Query: `site:erdosproblems.com/124 "powers"`. Outcome: No new theorem used; direct page later returned403.

6. General web. Query: `"Fourier-Stieltjes" "sparse" "sumsets"`. Outcome: No target-completeness result imported.

7. arXiv. Query: `site:arxiv.org "Complete, dispersing, and syndetic sets"`. Outcome: Empty; this guessed title was not the actual Bergelson-Simmons title.

8. Semantic Scholar. Query: `site:semanticscholar.org "Complete, dispersing, and syndetic sets"`. Outcome: Empty.

9. zbMATH. Query: `site:zbmath.org "Complete, dispersing"`. Outcome: Empty.

10. General web. Query: `Bergelson Simmons "complete" "syndetic" sets`. Outcome: Author-hosted primary PDF and Fan's existing paper.

11. General web. Query: `"subset sums" "density one" "complete" sequence`. Outcome: No applicable new local-limit or completeness implication.

12. General web. Query: `"rigidity" "Kazhdan" "powers" sequence partition`. Outcome: Related general ergodic material, no applicable allocation theorem.

13. General web. Query: `"Strongly complete sets and a conjecture of Erdos" Fan`. Outcome: arXiv2607.14071, author's publications page; rechecked version3.

14. arXiv. Query: `site:arxiv.org "pure powers" "complete" sums`. Outcome: Mostly unrelated objects; no solution of the target.

15. General web. Query: `"sumsets" "FS-means" "cofinite"`. Outcome: No direct one-supply theorem imported.

16. General web. Query: `"pure powers" "subset sums" completeness`. Outcome: Hilbert cubes contained in pure powers, not sums of prescribed power streams; excluded.

17. General web. Query: `"Cantor" "local limit theorem" convolution integers`. Outcome: A self-conformal random-walk local-limit paper has a different limit variable and hypotheses; not an integer-coefficient estimate here.

18. General web. Query: `"missing digit" "sumsets" "integers" coprime`. Outcome: Same-base and real-fractal results; no occurrence-preserving mixed-base lift.

19. Crossref API. Query: `https://api.crossref.org/works?query.bibliographic=New%20examples%20of%20complete%20sets%20Bergelson%20Simmons&rows=3`. Outcome: URL rejected by web access boundary; no successful metadata verification.

20. Semantic Scholar API. Query: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2507.10512?fields=title,year,externalIds,citations.title,citations.externalIds`. Outcome: URL rejected by web access boundary; no citing-set verification.

21. zbMATH API. Query: `https://api.zbmath.org/v1/document/_search?search_string=ti%3Acomplete%20%26%20au%3Asimmons`. Outcome: URL rejected by web access boundary.

22. General web. Query: `"complete sequences" "Folkman" ratio`. Outcome: Primary Graham discussion and lead to van Doorn2602.23394.

23. General web. Query: `"complete" "subset sums" "limsup" "2"`. Outcome: Dense-sequence results have polynomial-scale count conditions not established for fixed power streams.

24. General web. Query: `"completeness" "sum of distinct" "ratio" sequence`. Outcome: van Doorn2602.23394 discovered via a secondary page; only the primary paper used.

Primary follow-up opens: arXiv2607.14071v3, Erdos124 (403), arXiv2602.23394v1 abstract and HTML. The raw response packets for the later query batches are retained in sources/. The first noisy sweep produced no imported result; its requests and disposition are recorded above. No arbitrary search code or mathematical program ran.
