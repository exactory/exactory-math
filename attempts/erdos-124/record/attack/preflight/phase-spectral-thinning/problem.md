# Problem study: phase-aware spectral thinning

Date: 2026-09-08. This is a proposal preflight, not a proof.
Predecessor: accepted checkpoint-000025, acceptance-000012, node-000019.
Current controller revision at study completion: 364.

## Exact prospective claim

For every nonempty finite set D of distinct integers at least 4 with gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>1, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit an explicitly recursive infinite sequence Q of distinct remaining labels with strictly increasing numerical values q_i, such that its actual complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), every base d in D occurs infinitely often in Q with bounded gaps between its selected exponents, and sum_i ||beta q_i||^2=infinity for every nonzero beta in R/Z; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers with a terminating witness procedure, each label used at most once and coincident values from distinct labels retained separately.

FS_0 includes the empty subset. Labels, not numerical values, are the
resources. Bounded selected exponent gaps may depend on D,k,F and the base.
The gap g is fixed before the first selection. The claim neither asserts
that FS_0(Q) is thick nor asserts eventual completeness of FS_0(Q union R).

## Queries and exact statement boundary

The complete dated record is QUERY_LOG.md, with 20 fixed queries.
Problem-level first-tier searches are 1--5, constructive-method first-tier
searches are 6--10, and 11--20 test the recurrence tool, the strict-mass
thickness claim and neighbours. These are domain-index and general-web
queries, not exhaustive API traversals. Every returned batch is saved.
The exact claim above combines the studied objects and quantifiers.
A fresh exact-unit search remains required before any candidate unit.

The canonical original is sources/124.lean in the project root,
Erdos124.erdos124.ne_zero in the formal-conjectures repository:
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/124.lean.
The whole local 129-line source was read during this preflight.
Its positive cutoff is unchanged. The original claim covers min D>=3,
sigma(D)>=1 and eventual coverage. This prospective prerequisite covers
min D>=4 and strict mass, and proves only the stated partition and thickness.
It cannot replace the original claim or the full half-mass signed-unit target.

## Primary hits actually inspected

1. Burr, Erdos, Graham and Li, Complete sequences of sets of integer
powers, Acta Arith.77(2),133--138(1996),
DOI:10.4064/aa-77-2-133-138,
https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf.
The local extracted sources/begl1996.txt was read through its end in this
preflight, including the introduction, the bounded-gap argument and the
concluding remarks. The paper states the finite-base conjecture and credits
Pomerance's Diophantine-approximation necessity argument. It does not supply
the proposed all-strict-mass thinning theorem. Its dense-base construction
uses additional disjoint resources. The discussion on page137 treats strict
mass as expected to be easier, not as a proved general sufficiency theorem.
The OCR power ranges in Claim1 are not used as a proof input here.

2. Bergelson and Simmons, New examples of complete sets, with connections
to a Diophantine theorem of Furstenberg, arXiv:1507.02208v2,
https://arxiv.org/abs/1507.02208.
Only the relevant local lines625--655, Claim2.13 and footnote10, were reread
in this preflight. The footnote explains why the closure of a forward
rotation orbit is a compact group. Earlier accepted studies cover its
reserve interface. No complete fresh reading of this paper is claimed.

3. Li, Oprocha, Ye and Zhang, When all closed subsets are recurrent?,
arXiv:1504.08191v1, https://arxiv.org/html/1504.08191v1;
journal DOI:10.1017/etds.2016.5, title later written as
When are all closed subsets recurrent?.
The abstract and Sections2.1--2.3 were inspected selectively in the HTML
rendering, especially the definition of minimal point, positive syndeticity,
and Lemma2.1(2). The full downloaded HTML is saved. The lemma states the
usual all-neighborhood characterization of minimal points by bounded
positive return gaps. Only this elementary interface is used as a source
lead. Its hyperspace results are not imported.

4. Griesmer, Discrete sumsets with one large summand,
arXiv:2507.10512v1, https://arxiv.org/pdf/2507.10512v1.
The exact sequential full Fourier--Stieltjes mean mechanism and the
Corollary4.2(ii) application are inherited from accepted CP25, sections4--6,
and CP24, acceptance-000011. CP25's full proof was reread during this
preflight. The saved primary text is
../ergodic-mass-threshold/sources/griesmer2507.10512v1.txt.
The underlying main Theorem3.17 remains a trusted published input, not a
newly reproved theorem. Character cancellation of an arbitrary mean alone
must not be substituted for its actual hypothesis.

## Secondary hits and neighbouring claims

The problem page and thread, https://www.erdosproblems.com/124 and
https://www.erdosproblems.com/forum/thread/124, give research leads about
near alignment and the zero-cutoff distinction. Their indexed d_r typo is
not adopted. The #125 discussion returned in query20 concerns density
below reciprocal mass one and is a neighbouring warning, not a positive
strict-mass theorem. Zero-cutoff, min D=3 and equality remain distinct.
The Grivaux--Roginskaya arXiv:1202.3113 hit was inspected at abstract level
only. Its r-Bohr recurrence-set problem is not the return-time assertion
needed here, so no result from it is imported.

The general support-allocation report at https://www.starfleetmath.com/
was rediscovered. The inherited CP25 RELATED_REPORT.md records the relevant
#254 excerpt and its unverified formal-proof status. Its growing
dyadic-shell abundance hypothesis does not cover fixed finitely many
power streams. The general allocation idea is not claimed original.
No result from that report is an accepted dependency.

## Constraints on the prospective plan

CP25's exact estimate requires sigma(D minus {h})>=1 for the most recently
selected base h. The new input to test is instead a fixed neighborhood of
simultaneous logarithmic phase alignment. For each cyclic base h, search
successive h-powers q beyond a scale multiple of C plus prior removed weight.
Require a nearby power of every d in D, using exact rational inequalities
around q. The rational tolerance and scale multiplier must be specified
from D before iteration; they may not be supplied by an undecidable oracle.

Classical recurrence is needed on the actual compact orbit closure,
not on the full torus. Rational logarithmic dependencies are permitted.
Bounded return gaps must transfer to bounded selected exponent gaps.
The unresolved mathematical question is whether this operation preserves
the same strict-prefix deficit for every scale, including near numerical
ties. Source recurrence alone does not answer it.

The finite-prefix and infinite-complement invariant must be proved before
declaring a seed or applying the amplification. All spectral and interval
consequences require the same single infinite Q. Full-supply thickness
does not give a separate thick supply disjoint from another bounded-gap
reserve, and no eventual-completeness conclusion follows merely from it.

## Stop and remaining work

The fixed count20 was reached. No exact literature solution was identified
in this bounded search. This is not an originality, priority or exhaustive
novelty certificate. The next lawful step is independent review of a
separate precise proposal under the current inherited account. No
mathematical process was run and no new lemma is claimed by this study.

