# Cantor-lift preflight query log

Date: 2026-09-07 UTC.
Status: source study in progress, no proposal, admission, or mathematical
move for this route. The high-mass predecessor is independently accepted
as acceptance-000005 at checkpoint-000016. The intended target, if a
substantive plan survives the source audit, is the existing complementary
mass obligation-000017. Its exact Claim is in the controller.

Fixed search count: one query per first-tier source for the problem and
one for the selected prospective reduce-and-translate strategy, plus the
direct primary readings listed below. The discovery queries in
admission/post-mass-literature-triage.md preceded this targeted study.

## Problem-level floor

1. arXiv query: ("complete sequences" AND "integer powers") OR (Cantor AND "subset sums").
   Limit 8, full abstracts. Three results returned: Hegyvári 2307.07237v1
   (directly relevant integer Cantor sums), 2408.07634v3 (packing),
   2410.15880v1 (polynomial factorization). The last two do not address
   the proposed integer representation interface. Saved problem-arxiv.json.
2. Semantic Scholar query: "complete sequences" "integer powers".
   Limit 5. Returned BEGL96, DOI 10.4064/AA-77-2-133-138, and four
   nonmatching generalised-polynomial, Lucas, Fibonacci, and
   second-order-sequence records. Saved problem-semantic.json.
3. Crossref bibliographic query: Complete sequences of sets of integer powers.
   rows=3 through the web reader. A non-retryable unsafe-URL response
   was returned; no successful new metadata lookup is claimed.
4. zbMATH query: ti:"Complete sequences of sets of integer powers".
   The web reader returned a non-retryable unsafe-URL response.
5. Problem database: https://www.erdosproblems.com/124 returned HTTP403.
   Responses for items3-5: problem-crossref-zbmath-database.json.
   No blocked direct operation was retried or wrapped.

## Prospective strategy floor and source discovery

1. arXiv query: (Cantor AND thickness AND sum) OR ti:"arithmetic sums of Cantor-type".
   Limit8, full abstracts, returned8 of9 results. Saved strategy-arxiv.json.
   Hits: Pathak2307.08135v2; Nassiri-Bidaki2602.16667v2;
   Jiang2008.08229v2; Fillman-Tidwell2206.00556v1;
   Damanik-Gorodetski0901.4383v1 and1001.2552v1;
   Peng-Wang-Wang2605.21275v2; Takase2012.11827v1.
   Pathak and the semibounded-sum result are potentially relevant.
   The other abstracts concern related real/spectral geometry, not an
   established integer pure-power lifting theorem. The ninth result
   was not fetched because the fixed response bound was reached.
2. Semantic Scholar query: Cantor sets thickness integer sums Astels Hegyvári.
   Limit5. Rate limited, no retry. Saved strategy-semantic.json.
3. Crossref-targeted indexed web query:
   site:api.crossref.org "Cantor sets and numbers with restricted partial quotients".
4. zbMATH-targeted indexed web query:
   site:zbmath.org "Cantor sets and numbers with restricted partial quotients".
5. Problem-database indexed query: site:erdosproblems.com/124 "Cantor".
   Combined response strategy-web-database.json contains problem-forum
   hits, not a successful Crossref or zbMATH record. The limitation
   is explicit rather than being counted as a registry confirmation.

The forum discovery includes Tao's December2025 note that Gemini had
already pointed out the Newhouse-gap-lemma connection without producing
new direct references or a solution. This is evidence that the analogy
is not new to this investigation. The indexed forum distinguishes the
solved zero-cutoff assertion from the positive-cutoff problem. It is
a discovery/status source, not an imported proof.

## Primary texts read

Astels, Thickness measures for Cantor sets (1999), ERA 5,108-111,
publisher identifier S1079-6762(99)00068-2. The entire short TeX source
was read at
https://ftp.gwdg.de/pub/misc/EMIS/journals/ERA-AMS/1999-01-015/1999-01-015.tex.html.
Its general sum theorem gives an interval when the sum of normalized
thicknesses is at least one; equality with the whole sum of hull
intervals has additional gap-size conditions. The announcement refers
to Theorem2.4 of the longer Astels paper for the proof.
Saved primary source in cantor-primary-reading-04.json.
The longer proof has not yet been read. Do not claim otherwise.

Pathak, arXiv2307.08135v2: abstract, introduction and first theorem
statements read. It describes a real dynamical approximation technique.
No integer lift is supplied by the passages read. Same saved reading
response as above. The entire paper has not been read.

Hegyvári, On arithmetic sums of Cantor-type sequences of integers,
arXiv2307.07237v1: full short HTML paper read, including Theorems2.1
and2.4 and their displayed proofs. Saved hegyvari-2023-reading.json.
Its doubled sumset allows two uses of a sequence term. Its weighted
p>2 result gives long arithmetic progressions for almost every real
parameter, not cofinite distinct pure powers for every fixed finite
base set and positive cutoff. Index conventions and apparent slips in
the HTML proof must not be silently repaired into accepted input.
It is currently a method lead, not a proof dependency.

The thesis landing page and Pathak abstract are saved in
cantor-primary-discovery-03.json. No PDF or raw-file download was run
for this next route.

## Decision still required before admission

A prospective plan must preserve exact occurrence supports, arbitrary
positive cutoffs, and the integer target. A real Cantor interval or
an approximation with bounded nonzero error does not establish a
finite exact integer seed. A common multiplication factor does not
turn every fractional base expansion into legal pure powers.

The previously accepted high-mass criterion uses three genuinely
disjoint supplies. It cannot be applied by feeding the same supply
twice into a sumset theorem. Likewise, Hegyvári's doubled sumset is
not a construction of two legal disjoint copies within this input.

No new Claim or proof result is asserted in this file. Complete the
problem and strategy study, identify a precise new map and its
integer-lifting success/failure condition, and seek independent
proposal review only if that is substantive. Do not admit another
renamed abstract-profile obstruction merely to consume moves.

