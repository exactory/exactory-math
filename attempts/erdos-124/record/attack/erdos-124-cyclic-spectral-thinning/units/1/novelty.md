# Unit-level novelty check

Date: 2026-09-08. The exact statement is units/1/unit.json.

For every nonempty finite set D of distinct integers at least 4, write sigma(D)=sum_{d in D}1/(d-1) and H={h in D:sigma(D minus {h})>=1}; if H is nonempty with gcd(H)=1, then for every integer k>=1 and finite set F of labels (d,j) with d in D and j>=k, there is an explicitly recursive infinite sequence Q of distinct remaining labels, strictly increasing in numerical value q_i, whose complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), such that every h in H occurs infinitely often in Q with bounded gaps between its selected exponents and sum_i ||beta q_i||^2=infinity for every beta in R/Z other than zero; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers, with a terminating witness procedure and each label used at most once.

The problem study, study/QUERY_LOG.md, study/RELATED_REPORT.md and original
novelty.md remain the earlier record. A fixed nine-query unit-level check
used the following strings, with domain filtering for tier-one indices:

1. arxiv.org: "powers" "subset sums" "bounded gaps" "Fourier" cyclic
2. semanticscholar.org: "powers" "subset sums" "thick" cyclic
3. search.crossref.org: "powers" "subset sums" "spectral" "thinning"
4. zbmath.org: "powers" "subset sums" "thick" spectral
5. erdosproblems.com: "124" "cyclic" "powers"
6. General index: "cyclic spectral thinning" powers subset sums
7. General index: "powers" "bounded gaps" "subset sums" Fourier Stieltjes mean
8. General index: the full exact statement above, verbatim.
9. arxiv.org: "Discrete sumsets with one large summand" Griesmer

Batch1 (queries1--3) returned no results. Batch2 (4--7) returned no
matching-domain tier-one result and no exact theorem identified. Its
related hits included the Star Fleet problem254 report, already
classified in study/RELATED_REPORT.md, and dense integer subset-sum
results. Batch3 (8--9) returned the primary Griesmer reference and many
unrelated results, not an identified proof of this exact criterion.
Batch results are combined by the search tool, so no finer attribution
is inferred. The complete returned text is preserved in query-results-1.json
through query-results-3.json.

Griesmer's exact reference is arXiv:2507.10512v1,
https://arxiv.org/pdf/2507.10512v1. Targeted primary reading is pinned in
the CP24 dependency closure. The repeated search returned its abstract.
The local contribution is the recursive occurrence partition, not the
published sumset theorem. https://www.starfleetmath.com/ is an unverified
related report, not a proof dependency. Other snippets were not treated
as complete proofs.

No exact prior theorem was identified within this bounded check. This
is an index search, not a successful traversal of every source API.
Earlier direct-access failures and index limitations remain. The nine-query
limit has been reached. No global novelty or priority certification is claimed.
