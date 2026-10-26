# Challenge 05: prove all strict reciprocal-mass cases

Packet version: 1. Prepared: 2026-09-07.
Priority: primary. Type: high-risk analytical proof attempt.
Return one self-contained English response. Do not substitute a computation.

## Exact target

For every finite set D of distinct integers d>=3 with gcd(D)=1 and

    sigma(D)=sum_{d in D}1/(d-1)>1,

and every integer k>=1, prove that there exists an integer N(D,k) such that
every integer n>=N(D,k) has a representation

    n=sum_{d in D}sum_{j in S_d}d^j,

where S_d is a finite subset of {k,k+1,...}. Each labelled pair (d,j) can be
used once; equal values from different pairs remain separately available.

There is no fixed lower bound on sigma(D)-1. D, its cardinality, its largest
base, and k are not bounded. The cutoff cannot determine a new enlarged base
set. Gcd one is collective, not pairwise coprimality. No effectivity for N is
required. Do not introduce exponent-zero terms, negative coefficients, or
perturbed powers.

A complete proof would settle the entire strict-mass portion of the original
objective sigma(D)>=1. It would leave precisely the equality regime within
that objective. This is a major scope target, not a request to certify a
single base set or additional finite cutoff.

## Starting information

Sort the power stream as a_1,a_2,...; put S_m=sum_{i<=m}a_i and q_m=a_{m+1}.
With epsilon=sigma(D)-1>0 and

    C(D,k)=sum_{d in D}d^k/(d-1),

the geometric-sum identity gives, for every prefix,

    S_m-q_m>=epsilon q_m-C(D,k).

Thus the all-future extension surplus is already available. It does not prove
the existence of a represented seed. One sufficient route is to produce L,m
with all three properties

    S_m>=2L,
    [L,S_m-L] intersect Z subset FS(a_1,...,a_m),
    epsilon q_m>=C(D,k)+2L-1.

At every later prefix the last inequality still holds, so adjoining the next
label joins overlapping or adjacent integer intervals. Their upper endpoints
tend to infinity. Recheck this conditional deduction if using it. L and m
must be chosen compatibly; neither condition can be assumed after the other.

An independently accepted auxiliary lemma says that, for m=min D, one can
select E subset D containing m with gcd(E)=1 and

    1<=sigma(E)<1+1/m.

This is checkpoint-000008, acceptance-000001. It is a selection result only.
It does not guarantee sigma(E)>1 when sigma(D)>1. In particular, reducing to
E must not silently import the still-unsolved equality case into a proof
advertised as independent of that case.

## Requested conceptual advance

Exploit the positive but arbitrarily small reciprocal excess to prove exact
integer completeness. One ambitious direction is a covering argument that
turns that excess into shrinking numerical holes while respecting each power
label. Another is a structural decomposition that leaves enough disjoint
terms both for large-scale coverage and for eliminating arithmetic holes.
Any term allocation must be justified quantitatively even as epsilon tends
to zero; the same labels cannot serve several incompatible roles.

Choose and pursue one substantive approach. A general outline that names
an unproved expansion or transversality lemma as its final step is not a proof.
An alternative direct method that avoids seed intervals is welcome.

Known limitations to address:

- Positive real dimension, a real interval, or density of normalized sums
  does not by itself imply exact representation of every large integer.
- Surplus and gcd one do not by themselves force completeness of arbitrary
  integer sequences. Preserve and use the actual pure-power structure.
- Even full modular coverage plus strong counting and irrational-norm
  conditions can fail with all-sublinear-power surplus in abstract streams.
  No general theorem covering positive linear surplus is supplied here.
- A theorem for sigma(D)>=1+epsilon_0 with one fixed epsilon_0>0 leaves
  the near-critical strict range unproved. State that narrower result honestly.
- Proving a result for bases up to a fixed bound, for finitely many k, or for
  a base set that grows with k does not establish this claim.

## Primary references

BEGL96, *Complete sequences of sets of integer powers*,
[DOI 10.4064/aa-77-2-133-138](https://doi.org/10.4064/aa-77-2-133-138),
provides the original framework. Its cutoff-dependent finite subsets from
an infinite base set do not fix the given D for all cutoffs.

Bergelson and Simmons, *New examples of complete sets, with connections to a
Diophantine theorem of Furstenberg*,
[arXiv:1507.02208v2](https://arxiv.org/abs/1507.02208v2),
[DOI 10.4064/aa8221-10-2016](https://doi.org/10.4064/aa8221-10-2016),
contains completeness criteria involving disjoint supplies. Check the exact
statement and each allocation assumption; do not assume that a total
reciprocal mass just above one supplies several disjoint required blocks.

State whether you inspected a source or are only giving a literature lead.
Do not claim publication novelty from the absence of a remembered theorem.

## Deliverable and research boundary

Give your exact theorem, proof, imported results with checked hypotheses,
and consequence for the original all-D problem. A sharp new intermediate
lemma or an explicit obstruction after a serious attempt is useful when
the full theorem is out of reach. Name all remaining assumptions and cases.
If offering a counterexample to the target, it must be an admissible fixed
D,k with a proof of infinitely many missing integers, not a finite omission
or a counterexample to a broader abstract statement.

Record actual model/tools when known. Do not report a proof-completion
percentage for an unverified candidate. This is one analytical response,
not a benchmark or a request for brute force. Do not launch mathematical
programs, other agents, or controller mutations. This packet is not an
admitted research node. Save only to this packet's `results/RESULT.md` or a
unique result filename, preserving previous results and source evidence.
