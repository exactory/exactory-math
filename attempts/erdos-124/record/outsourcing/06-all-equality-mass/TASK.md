# Challenge 06: prove every critical reciprocal-equality case

Packet version: 1. Prepared: 2026-09-07.
Priority: primary. Type: high-risk analytical proof attempt.
Return one self-contained English response. This is not a finite search task.

## Exact target

For every finite set D of distinct integers d>=3 satisfying

    gcd(D)=1,
    sum_{d in D}1/(d-1)=1,

and every integer k>=1, prove that there is N(D,k) such that every integer
n>=N(D,k) is a finite sum of powers d^j, d in D and j>=k, with each labelled
pair (d,j) used at most once. Equal numerical values from different labels
remain separately available.

No bound on D or k, no pairwise-coprimality assumption, and no exponent-zero
terms are allowed. N may be ineffective. This is the complete critical part
of the original objective with reciprocal mass at least one. Its proof would
be a major result on the actual problem, but the strict-mass regime would
still require its own argument.

The family D={3,4,7} is an illustration, not the task's full scope. A proof
for that family, or for k=1, must be labelled as a narrower result. Do not
assume that admissible equality sets have already been reduced to a finite
classification.

## Accepted result that removes one obstruction

For every such D,k, even after deleting any finite set F of labelled
occurrences, let the sorted remaining stream be a_1,a_2,... and
S_m=sum_{i<=m}a_i. The project has an independently reviewed analytical proof
that

    S_m-a_{m+1}->+infinity.

This is checkpoint-000009, acceptance-000002, node-000005 move 1. It may be
used as a supplied lemma. Its proof imports finite-rank equation finiteness:
Evertse, Schlickewei and Schmidt,
[arXiv:math/0409604](https://arxiv.org/abs/math/0409604),
[DOI 10.2307/3062133](https://doi.org/10.2307/3062133).
It does not provide a positive linear surplus or an effective threshold.

The mechanism of the supplied lemma is specific to powers. A prime dividing
one base but not another prevents equality of their positive powers. For
each bounded nonzero difference, finite-rank equation finiteness permits
only finitely many exponent pairs. The selected next powers therefore
separate by an amount tending to infinity.

With q_m=a_{m+1}, next unused powers x_d(m), and

    C=sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j,

the exact identity beyond all deletions is

    S_m-q_m=sum_{d in D}(x_d(m)-q_m)/(d-1)-C.

All terms in the sum are nonnegative. Separation of the chosen pair forces
divergence. There is no extra term (sigma(D)-1)q_m at equality. Supplying
that term without proof would change the problem.

## Missing mechanism and proposed direction

The central difficulty is to turn the exact relations among the geometric
streams into a represented interval with bounded endpoint loss. The known
surplus already permits propagation once such a compatible interval exists.
One sufficient new theorem would say that, for each D,k, there is a fixed
integer L>=0 and arbitrarily large m such that

    S_m>=2L,
    [L,S_m-L] intersect Z subset FS(a_1,...,a_m).

Choose m after the surplus threshold for this fixed L. Adjoining each later
power joins [L,S_r-L] and its translate by a_{r+1}; the inequality
S_r-a_{r+1}>=2L-1 makes these integer intervals adjacent or overlapping.
Their union grows without bound. Check this deduction if using the route.

Seek an exact multiscale integer-covering argument that exploits reciprocal
equality together with the impossibility of persistent exact alignment of
all base streams. The key advance must explain why large numerical holes
cannot survive. Lack of alignment alone, a real interval, or divergence of
the next-power gaps does not already establish that conclusion.

Alternative analytical approaches are welcome. Concentrate the one-shot
attempt on one concrete new lemma or invariant and push it to a proof or
an exact obstruction, rather than surveying many possible methods.

## Known failures and scope checks

- Gcd one and all modular subset-sum residues do not give eventual coverage.
- An accepted counterexample outside the pure-power class satisfies strong
  arithmetic and counting conditions and surplus exceeding every fixed
  sublinear power of the next term, but remains incomplete. A generic
  sequence theorem using only those properties cannot settle this task.
- A represented interval whose loss grows with the prefix does not supply
  one fixed L. Its threshold may move faster than the proposed seed.
- Bounds on ||alpha d^j||, real transversality, or symbolic digit entropy need
  a justified passage to exact integer representations.
- A proof at strict reciprocal mass does not extend to equality by continuity:
  bases are integers and the final conclusion concerns an infinite discrete tail.
- Checking large finite prefixes or all small equality sets does not prove
  the target. A finite reduction must first prove why nothing remains outside it.

Background: BEGL96, *Complete sequences of sets of integer powers*,
[DOI 10.4064/aa-77-2-133-138](https://doi.org/10.4064/aa-77-2-133-138).
Any literature solution or new imported theorem needs its exact quantifiers
and hypotheses checked, especially the dependence of the base set on k.

## Required deliverable

Return the exact theorem established, the full proof or first unresolved
inference, references actually inspected, actual model/tools when known,
and the precise remaining root scope. Distinguish a partial result from
the all-equality theorem, and validity from publication novelty. A claim
of falsity requires an admissible D,k and infinitely many proved omissions.
An obstruction to an auxiliary lemma is not a root counterexample.

No proof-percentage gain is credited before verification. Do not launch
mathematical programs, other agents, or controller mutations. The packet is
an external challenge, not an admitted native attack. If filesystem access
is available, write only this packet's `results/RESULT.md` or a distinct run
filename there; preserve all previous results and accepted artifacts.
