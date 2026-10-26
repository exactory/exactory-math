# Query record for the signed-tail seed inference

Date: 2026-09-07. These are read-only source queries, not mathematical runs.
All response files are in sources/ under this directory. A 429 is an access
limitation, not a negative literature result. The fixed preflight ceiling is
one query per first-tier source at each of the problem and strategy levels,
plus the focused second-tier queries and primary-source follow-up below.

## First-tier problem queries

- arXiv: all:"subset sums" AND all:"signed" AND all:"complete", max 5.
  Hits: arXiv:2608.16598v1 (discrete chemical perception, unrelated);
  arXiv:2110.01732v7 (Wasserstein distance to a polytope, unrelated).
- Semantic Scholar: complete sequences signed tail subset sums, limit 5.
  HTTP/JSON 429. No claims inferred from this response.
- Crossref: complete sequences signed tail subset sums, rows 5.
  Hits: 10.1112/mtk.12091 (Large signed subset sums);
  10.47443/dml.2021.0019 (cryptography, unrelated);
  10.4064/aa8133-3-2016 (On the subset sums of exponential type sequences);
  10.22541/au.177368891.19811728/v1 and 10.2139/ssrn.7215159
  (unrelated results). Raw records preserve full metadata.
- zbMATH: ti:"signed sums" & ti:sequence.
  Hit: zbMATH 6147070, Chen Feng-Juan and Yong-Gao Chen,
  Signed sums of terms of a sequence, Proc. AMS 141 (2013), 1105-1111,
  DOI 10.1090/S0002-9939-2012-11397-8. A review exists but its text was
  withheld in the API response. Bibliographic metadata only.
- Problem database: https://www.erdosproblems.com/124.
  The positive-cutoff problem remains marked open; the zero-cutoff proof
  and the fixed {3,4,7}, k=1 result are distinct. The displayed d_r typo
  is corrected by the canonical source sources/124.lean at the study root.
  That Lean file was read completely.

## First-tier strategy queries

- arXiv: all:"complete sequences" AND (all:"counterexample" OR
  all:"perturbation" OR all:"subset sums"), max 5.
  Hits: arXiv:2104.14766v1 (Conlon, Fox, Pham, Subset sums, completeness
  and colorings, abstract read); arXiv:2304.01777v1 (modular subset sums);
  arXiv:2608.05002v1 (biomedicine, unrelated);
  cond-mat/0106547v2 (unrelated to this quantified inference).
- Semantic Scholar: complete sequences perturbation signed identities.
  Requested more than 60 seconds after the first 429; again 429.
  No further retry. This is an explicit study limitation.
- Crossref: Complete sequences of polynomial values, rows 3.
  Hit: 10.1215/S0012-7094-64-03126-6, plus two unrelated book parts.
  Raw response preserves all three records.
- zbMATH: ti:"Complete sequences of polynomial values".
  Hit: zbMATH 3193832, Zbl 0119.04201, Graham (1964).
  No editorial review text was provided by this API response.
- Problem database: https://www.erdosproblems.com/forum/thread/124.
  Read the mathematical discussion of the difference between zero and
  positive cutoffs. Its source explains why the zero-cutoff proof does
  not discharge the original objective.

## Focused second-tier queries and primary follow-up

General web queries run on this date:
complete sequences signed integers tails;
complete sequences nearly Graham Burr Erdos;
subset sums every tail differences complete;
signed sums sequence complete integers -polynomial -phylogenetic -mtDNA -broadcast;
nearly complete Sigma-sequence mathematics;
weakly complete sequences tail -graph;
Signed sums of terms of a sequence Chen 2013 theorem;
On the subset sums of exponential type sequences abstract;
site:erdosproblems.com/124 powers complete;
site:erdosproblems.com/forum/thread/124 signed.

The relevant hits were Graham (1964), Chen and Chen (2013), the Schissel
complete-sequence discussion, the Erdős problem page, and Chen, Fang and
Hegyvári (2016). No returned record states the exact conjunction of
every-tail legal unit identities, the full arithmetic profile, all
sublinear-power surplus bounds and fixed-loss central coverage.

Primary follow-up:
- Graham, DOI 10.1215/S0012-7094-64-03126-6. Saved PDF at
  ../../../sources/graham1964.pdf relative to this directory. The correct
  location relative to the research root is sources/graham1964.pdf.
  Pages 275-278 were visually read, including full proofs of Lemmas 1
  and 4. The whole article was not read. Lemma 4 supplies long
  progressions from fixed signed differences in every tail; Lemma 1
  requires a separate interleaved supply for its completeness argument.
- https://www.ams.org/journals/proc/2013-141-04/S0002-9939-2012-11397-8/
  failed in the web reader. No theorem imported from Chen and Chen.
- https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/173/2/91561/on-the-subset-sums-of-exponential-type-sequences
  was read on the publisher site, abstract only. It treats a common
  dilation base with a finite coefficient sequence, with a density bound
  when the coefficient count is at least p-1, and a Fibonacci-family
  completeness result. This is not the proposed general inference.
  DOI 10.4064/aa8133-3-2016.

The fixed count was reached. Access limitations prevent an exhaustive
novelty assertion. No publication priority or root solution is claimed.
