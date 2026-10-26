# Problem study: a minimum-preserving reciprocal core

Date: 2026-09-07. Scope: an auxiliary finite-set selection lemma, not the
positive-cutoff representation conjecture.

## Exact proposed statement

For every nonempty finite set D of distinct integers at least 3, put m=min D
and sigma(D)=sum_{d in D} 1/(d-1). If gcd(D)=1 and sigma(D)>=1, there is a
subset E of D containing m with gcd(E)=1 and 1<=sigma(E)<1+1/m.

The original root is still the all-D, all-positive-cutoff eventual
representation assertion. Its canonical declaration is
Erdos124.erdos124.ne_zero in the saved sources/124.lean, from
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/124.lean.
This auxiliary statement has no known canonical formal declaration. Its
quantifiers do not claim any representation theorem or finite tail reduction.

## Queries, hits, and reading status

The following fixed query set was run for this statement and the proposed
minimal-seed and greedy-extension method.

1. arXiv through web: site:arxiv.org minimal coprime set reciprocal sums greedy
   subset gcd. The relevant terminology hit was Pongsriiam, Relatively Prime
   Sets, Divisor Sums, and Partial Sums, arXiv:1306.4891. The abstract was opened
   and read, not the full paper. It counts gcd-one subsets and partial sums of
   those counts; it does not state the proposed reciprocal selection bound.
   Other returned abstracts on subset sums and GCD sums did not match the
   selection statement and are not theorem inputs.
2. Semantic Scholar through web: site:semanticscholar.org coprime subsets
   reciprocal sum minimal. The returned graph-eigenvalue item concerned
   reciprocal distances, not this statement. No matching theorem was found.
3. zbMATH through web: site:zbmath.org coprime sets reciprocal sums minimal.
   Serial-index results did not supply an exact theorem or review for this
   selection statement.
4. Problem database through web: site:erdosproblems.com/124 "1" "d-1".
   The problem thread returned the known distinction between zero and
   positive cutoff. The displayed statement typo discussed there does not
   change the saved canonical positive-cutoff claim. No core-selection
   theorem was identified. A direct open of /124 returned an internal error.
5. Crossref through web: site:api.crossref.org "relatively prime" "sets".
   No exact matching bound was returned.
6. Crossref API, query.bibliographic=minimal relatively prime sets reciprocal
   sum, rows=3. Hits were On Relatively Prime Sets Counting Functions
   (10.1515/integ.2010.039), On Relatively Prime Sets
   (10.1515/integ.2009.029), and A Remark on Relatively Prime Sets
   (10.1515/9783110298161.714). Metadata and the available short abstracts
   concern counting relatively prime subsets, not this bound. Full texts
   were not read. The raw response is sources/crossref.json in this directory.
7. General web: "minimal" "gcd" "sum" "1/(d-1)".
   No matching theorem was identified.
8. General web: "gcd" "reciprocal" "subset" "greedy".
   Von Korff, Classification of greedy subset-sum-distinct-sequences,
   DOI 10.1016/S0012-365X(02)00875-0, concerns reciprocal sums of infinite
   sequences avoiding a residue, not selecting a gcd-one core of D. Only
   the returned abstract/excerpts were inspected. No result is imported.
   Unverified claimed solutions and unrelated search hits were excluded.

Primary background is the canonical repository statement and the cited
Pongsriiam abstract. The previously inspected BEGL96 paper,
DOI 10.4064/aa-77-2-133-138, remains background for the root, not proof of
this lemma. Search response excerpts are preserved in sources/queries.txt.

## Constraints on the proposed proof

Deleting a base may break gcd one, so stopping a reciprocal sum at its first
crossing of one does not alone establish the claim. The method must first
supply a gcd-one subset that includes m and has reciprocal mass below one.
Minimality of that subset may provide distinct prime witnesses to the
indispensability of its other elements. This is a proposed proof mechanism,
not a theorem established by this study.

Once such a seed is available, adding unused bases preserves gcd one and
the distinguished minimum. Every added base is greater than m. The seed
bound and the last increment are the two precise obligations to prove in
the admitted move. All D are symbolic inputs; no sample or enumeration is
proposed as evidence.

The claim is an elementary auxiliary reduction. The search does not support
a claim of standalone novelty or publishable significance. An accepted proof
would leave the restricted representation theorem and its bridge open.

## Stop reason

The fixed eight-query set was completed. It supplied terminology and ruled
out importing unrelated counting or greedy-sequence results. No exact
solution was located, and no exhaustive novelty claim is made.
