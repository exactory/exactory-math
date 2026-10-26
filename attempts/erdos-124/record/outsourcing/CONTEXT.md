# Shared mathematical context

Prepared: 2026-09-07. Snapshot: controller revision 122.

Current outsourcing priority: packets 04-06 seek high-risk analytical advances
on the original claim. The earlier audit, abstract counterexample, and small
base-set packets are secondary. Packet creation does not change proof status.

## Original objective

Let D be any finite set of distinct integers at least 3 satisfying

    gcd(D) = 1,
    sigma(D) = sum_{d in D} 1/(d-1) >= 1.

For every integer k>=1, prove that there is N(D,k) such that every integer
n>=N(D,k) has a representation

    n = sum_{d in D} sum_{j in S_d} d^j,

where each S_d is a finite subset of {k,k+1,...}. Each pair (d,j) is available
once. Equal numerical powers belonging to different pairs remain separate
labelled occurrences. There is no exponent-zero term, repeated use of a label,
or permission to replace powers by nearby integers.

The full objective remains open in this research. No accepted result below
settles it. Background: [BEGL96](https://doi.org/10.4064/aa-77-2-133-138),
*Complete sequences of sets of integer powers*.

## Definitions and the missing step

Given k and a finite set F of deleted labelled occurrences, sort the remaining
stream as a_1,a_2,... by numerical value and then by base label. Put

    S_m = sum_{i=1}^m a_i,
    FS(a_1,...,a_m) = {sum_{i in I} a_i : I subset {1,...,m}}.

C1 asks for fixed integers L>=0 and m_0>=1 such that

    [L,S_m-L] intersect Z subset FS(a_1,...,a_m)

for every m>=m_0. Its all-D, all-k, all-finite-F statement is not proved.

The local conditional interval argument is simple: if a prefix represents
[L,S_m-L], S_m>=2L, and S_r-a_{r+1}>=2L-1 for every r>=m, adjoining the
next term joins two overlapping or adjacent integer intervals. Iteration
would give completeness. Producing a compatible initial interval is the
missing step. A surplus estimate alone does not produce it. The bridges
have not separately received controller acceptance.

## Accepted auxiliary results at this snapshot

1. For m=min D there is E subset D containing m, with gcd(E)=1 and
   1<=sigma(E)<1+1/m. This is an elementary selection lemma, not a
   representation theorem. Checkpoint-000008, acceptance-000001.
2. For every admissible D,k,F, S_m-a_{m+1} tends to positive infinity,
   including sigma(D)=1. This uses finite-rank equation finiteness of
   Evertse, Schlickewei and Schmidt. Checkpoint-000009, acceptance-000002.
3. An abstract substitute for pure-power structure is false. Two labelled
   copies of each

       b_(2t) = 9^t + floor(9^t/t),
       b_(2t+1) = 3 b_(2t) + 1,       t>=1,

   give tail gcd one and full modular subset-sum coverage, counting growth
   above the binary threshold, squared-norm divergence for every irrational
   multiplier, and (S_m-a_{m+1})/a_{m+1}^beta tending to infinity for every
   fixed 0<beta<1. Yet their numerical subset sums are not cofinite.
   Checkpoint-000010, acceptance-000003. This counterexample is not a
   pure-power stream and does not settle a positive linear relative-surplus
   hypothesis. It supplies no positive premise for the root proof.

These have analytical reviewed status, not Lean or computational certification.
The original proof files retain their historical pre-acceptance headers.
Subsequent acceptance records carry the later status; do not edit the headers.

## Local evidence map

- [Full search-tree index](../attack/SEARCH_TREE.md)
- [Current progress snapshot](../progress-reports/LATEST.md)
- [Surplus proof](../attack/erdos-124-tail-surplus/moves/001-sunit-tail-surplus.md)
- [Abstract counterexample proof](../attack/erdos-124-strong-surplus-seed/moves/001-paired-perturbation.md)
- [Conditional seed propagation](../attack/erdos-124-positive-cutoff/moves/003-seed-and-surplus.md)

Eleven of 24 shared moves have been used, with no reserved moves and no
mathematical runs. The outsourcing packets neither consume a mathematical
move themselves nor authorize unmetered mathematical execution. Their results
must enter through an appropriate reviewed route before being used as evidence.
