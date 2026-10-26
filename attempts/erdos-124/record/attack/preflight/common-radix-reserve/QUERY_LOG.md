# Query log for common-radix reserve preflight

Date: September 8, 2026. All requests used the session web search with the listed domain filters. No claim is made that an unavailable direct database API was searched exhaustively.

## Problem

- Source: arxiv.org. Query: `"powers" "complete sequences" "common radix"`.
- Source: semanticscholar.org. Query: `"signed" "powers" "complete sequences"`.
- Source: zbmath.org. Query: `"powers" "complete sequences" "signed"`.
- Source: api.crossref.org. Query: `"common radix" "complete sequences"`.
- Source: erdosproblems.com. Query: `"124" "powers" "complete" "signed"`.
- Source: general web. Query: `"complete sequences" "powers" "reserve"`.
- Source: general web. Query: `"signed" "powers" "common radix"`.
- Source: general web. Query: `"4, 8, 32" "complete" powers`.

## Constructive method

- Source: arxiv.org. Query: `"signed" "weights" "powers" construction`.
- Source: semanticscholar.org. Query: `"complete sequences" "powers" construction`.
- Source: zbmath.org. Query: `"complete sequences" "integer powers"`.
- Source: api.crossref.org. Query: `"Balance weighing" "variations on a theme"`.
- Source: erdosproblems.com. Query: `"124" "powers" "construction" "cutoff"`.
- Source: general web. Query: `"signed subset sums" "powers" "lattice"`.
- Source: general web. Query: `"complete sequences" "powers" "1/2"`.

## Saved responses and relevant reading

- sources/radixReserveProblem0.json: the first four domain queries returned no results.
- sources/radixReserveProblem1.json: Erdos domain and general discovery, mostly unrelated radix software, elementary series questions and other subjects; no exact hit.
- sources/radixReserveStrategy0.json: zbMATH metadata recovered the1996 pure-power paper, Zbl0863.11014; other displayed results concerned graphs, biology or software. The aggregate response was not a full-paper read.
- sources/radixReserveStrategy1.json: classical completeness and fixed-degree or Fibonacci power results, plus the previously known original conjecture. These are not the exact structural tail theorem. General-wiki and OEIS snippets are discovery only, not proof dependencies.
- sources/query-inputs.json: exact date, query arrays and filters.

The primary author weighing source is in ../binary-block-reserve/sources/binaryWeightPrimary.json and was reread through line162. The canonical original source is in ../mass-partition/sources/canonical-124-reading.txt and its complete94 displayed lines were reread. The inherited node15 proof is ../../erdos-124-half-tail-structure/moves/001-stable-tail-structure.md, pinned by checkpoint20. Each of its relevant common-radix steps was read and author-checked before this proposal. It is not independently accepted evidence.

The generalized common-radix signed-only neighbour and the fixed-alphabet positive neighbours were included in the signed/powers and common-radix queries at the same five sources. No separate exact hit was found. Search response dates are not assumed to be publication dates. The fixed count is eight problem queries and seven method queries. No finite mathematics was executed.
