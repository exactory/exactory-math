# Strategy study: make-the-proof-constructive

## Queries

The source-by-source searches and saved responses in sources/queries.md
were used for both this exact statement and the constructive method.
Date: 2026-09-07. Semantic Scholar returned 429; no repeated immediate
request was made.

## Hits worth reading

Burr-Erdos, DOI 10.1016/0022-314X(81)90036-6, Section 2 explains a
perturbation obstruction excluded by the present norm-divergence
hypothesis. Lemmas 3.1-3.4 on printed p.450 explain why constructing
adjacent subset sums and keeping a disjoint bounded-gap supply are
different requirements. Those exact hypotheses were read and visually
verified in the primary source.

The earlier local translated-power counterexample suggests retaining a
digit-coefficient encoding. Its constant perturbation is inadequate
because its surplus grows only logarithmically. Reusing it unchanged
would not test the strengthened target.

## Constraints on the constructive plan

A negative answer would be an explicit infinite sequence built from
finite blocks. A candidate template has two labelled copies at each
level j>=2. For t>=1, let

    b_(2t) = 3^(2t) + floor(3^(2t)/t),
    b_(2t+1) = 3 b_(2t) + 1.

These are candidate definitions, not verified conclusions. The
construction operation adjoins the next complete pair of blocks.
The slowly varying relative perturbation is intended to leave a large
positive surplus at pair boundaries; the affine link is intended to
force coprimality and irrational norm divergence. The coefficient
choices at a level are intended to encode base-three digits.

Before using any seed, seed-and-amplify must prove the extension
identities and bounds, ordering, bounded multiplicity, counting
asymptotics, every-tail modular conditions, all irrational parameters,
the all-prefix surplus limits for every beta, and a quantitative
failure of coverage. Any violation of these constraints is an entry
failure, not permission to weaken the target. No finite computation is
admitted; the proposed seed and extension can be checked analytically.

The extremal-candidate step is not selected: no optimum is requested.
The proposed seed branch is the first relevant step after the study.
If it constructs a full counterexample to the exact admitted claim,
Closing applies. Otherwise the remaining constructive steps and failure
signals remain mandatory.

## Stop reason

Fixed query count reached. A specific new perturbation template addresses
the prior logarithmic-surplus obstruction, but its validity remains to be
proved. No source was found establishing every requested condition for
this exact template.
