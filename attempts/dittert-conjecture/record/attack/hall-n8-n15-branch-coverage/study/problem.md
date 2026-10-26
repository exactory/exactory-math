# Study for an independent branch-coverage audit

Date: 2026-09-05. This is a user-requested verification of an already recorded
proof, not an attempt to claim a new theorem or restart an exhausted attack.

## Queries and sources

One statement-oriented query was run per first-tier source through web search:
- arXiv: `site:arxiv.org Dittert boundary maximizers permanent Hall cut eight nine`.
- Semantic Scholar: `site:semanticscholar.org Dittert nonnegative matrices permanent maximizers`.
- Crossref: `site:search.crossref.org Dittert permanent nonnegative matrices`.
- zbMATH: `site:zbmath.org Dittert permanent`.

The arXiv query returned Zhekai Pang, arXiv:2606.01531, whose abstract claims
the range n>=17. The other three searches returned no relevant new result.
Irrelevant search hits were discarded. These search-index results are not a
complete database search and do not justify a novelty assertion. No problem
database or canonical formal statement was identified for this audit claim.

The same narrow statement and computational-method search is served by
these queries at both problem and strategy level: Hall boundary exclusion
and its exact finite inequalities. The primary method source is already
archived at
`../dittert-completion-tree/study/external-proof`, pinned to
https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701.
The source proof and code will be read as proof material during the moves.
Existing analytic audits were read to identify claimed interfaces and
potential omissions; their verdicts are not accepted as evidence.

## Constraints learned

The pinned source already claims the entire mathematical range. Consequently
no original mathematical novelty is claimed here. The audit's concrete
additional obligation is to independently establish that every cut,
denominator domain, marginal support count, and real interval is covered.
The old Sinkhorn branch gap makes a second local smallness assumption
unacceptable unless derived independently for every Hall cut.

The proof has a finite rational residue and therefore fits
reduce-to-a-finite-computation. The source contains exact polynomial
certificates, allowing a small independent coverage checker. The parent
separately owns the common permanent-floor dependency. This child must state
that interface explicitly and must not silently replace it by reviewer PASS.

Stop reason: the fixed count of four first-tier source queries was reached.
The requested scope is verification of the pinned proof, so the study does
not expand into an unrelated literature survey.

