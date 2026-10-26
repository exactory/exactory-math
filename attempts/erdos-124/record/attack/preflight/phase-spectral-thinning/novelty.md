# Bounded novelty record: strict-mass phase-aware thinning

Date: 2026-09-08. Exact prospective statement:

For every nonempty finite set D of distinct integers at least 4 with gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>1, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit an explicitly recursive infinite sequence Q of distinct remaining labels with strictly increasing numerical values q_i, such that its actual complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), every base d in D occurs infinitely often in Q with bounded gaps between its selected exponents, and sum_i ||beta q_i||^2=infinity for every nonzero beta in R/Z; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers with a terminating witness procedure, each label used at most once and coincident values from distinct labels retained separately.

## Search record

All20 dated queries and visible returned hits are in QUERY_LOG.md and
sources/query-batch-{1,2,3,4,5,6}.txt, except that batch1's filename explicitly
marks its visible empty-result record. Problem first-tier floor:1--5.
Constructive-method first-tier floor:6--10. Queries11--20 cover primary
recurrence, all-tail thickness, strict mass and neighbouring min-three,
zero-cutoff and equality questions. The searches used domain indices,
not exhaustive registry APIs. Unit-level exact-statement queries are
still required if a proof candidate later stands.

## Results and reading limits

- BEGL96, DOI:10.4064/aa-77-2-133-138: full local extracted text read in this
  preflight; its fixed finite-base general conjecture is not proved there.
- Bergelson--Simmons, arXiv:1507.02208v2: targeted compact-group footnote
  read, not a complete fresh reading of the paper.
- Li--Oprocha--Ye--Zhang, arXiv:1504.08191v1,
  DOI:10.1017/etds.2016.5: abstract, relevant definitions and Lemma2.1(2)
  read from the primary HTML. Full HTML downloaded, not fully read.
  The recurrence interface is classical, not a new result of this attack.
- Griesmer, arXiv:2507.10512v1: exact FS-mean transfer inherited from
  accepted12 and11. The primary main theorem remains trusted literature.
- Grivaux--Roginskaya, arXiv:1202.3113: abstract only; not imported.
- Problem124 and125 pages and discussions: formulation and alignment
  leads only, not independent proof dependencies.
- Star Fleet #254 support allocation: the inherited
  ../../erdos-124-cyclic-spectral-thinning/study/RELATED_REPORT.md was
  reread. Its displayed abundance hypothesis and unverified formal status
  are retained. No novelty claim for general support allocation is made.

## Exact contribution being tested

Accepted CP25 gives the same fixed-gap spectral partition only when the
removable mass-one core has gcd one. This new statement would eliminate
that condition on the entire strict-mass minimum-four gcd-one domain.
It requires a new phase-sensitive preservation lemma, not a new
whole-base partition constant. No improvement is recorded as proved yet.

No exact solution of the prospective statement was identified.
The search stops at the fixed20 queries, with the remaining uncertainty
and source-reading boundaries above. It does not settle equality,
arbitrary half-mass units, a disjoint thick-plus-reserve theorem, T_4=1
or the original all-positive-cutoff completeness claim.

