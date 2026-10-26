# C1 move 1: joint seed choice and finite-preamble lifting

Date: 2026-09-06. Source: node-000002, move 1, pass 1.
Strategy: strengthen-and-generalise, step 2.
Entry: strengthen-the-target.
Status: candidate C2 and elementary implications, pending result acceptance.
The first-small-interval initialization is not repeated.

## Candidate and passage operations

For each D,k,F in C1, choose the endpoint loss L and the starting index m
together. Require L>=0 and m>=1 to be integers, with

    a_{m+1} > max({d^j : (d,j) in F} union {0}),
    S_m >= 2L,
    [L,S_m-L] intersect Z contained in T_m,
    S_r-a_{r+1} >= 2L-1 for every r>=m.                      (C2)

There is no upper bound on L or m in this candidate, and neither is chosen
from the first small represented interval. Each occurrence has its original
label. These choices avoid the particular obstruction recorded in the root
attempt, without assuming that a different seed exists.

Appending a term preserves the interval by the length inequality and keeps
every remaining future inequality. Raising the lower cutoff and deleting
finitely many occurrences are covered by the quantifiers over k and F, with
new constants allowed. Deleting a base or changing the integer lattice is
not an operation used by this argument.

## Deduction C2 implies C1

At every r>=m, the two represented integer intervals
[L,S_r-L] and [L+a_{r+1},S_{r+1}-L] join, because
L+a_{r+1}<=S_r-L+1. Induction gives [L,S_r-L] contained in T_r for all r>=m.
This is C1 with m_0=m. The new interval length grows by the positive integer
a_{r+1}, and no occurrence is reused.

C2 is still unproved. It has added an all-future bound, not removed the seed
obligation. No converse from C1 to C2 is claimed in this move.

## A finite-preamble lemma

Let B be a finite multiset of positive integers with total P, and let b_i
be an infinite nondecreasing sequence of positive integers tending to infinity,
retaining all multiplicities. This local finiteness ensures that the ordered
union has a prefix containing all of B. Suppose that, for every sufficiently
large t, the subset sums
of b_1,...,b_t contain [L,U_t-L], where U_t=sum_{i<=t}b_i and L is a fixed
nonnegative integer.

Order the union of B and the sequence by value, retaining labels. Beyond the
last occurrence from B, every prefix consists of B and an initial t terms of
the b-sequence. Its subset sums contain both

    [L,U_t-L] and [P+L,P+U_t-L],

by selecting none or all of B. Since U_t tends to infinity, eventually
U_t>=P+2L-1. The two intervals then join, yielding

    [L,P+U_t-L].

This proves central-prefix coverage of the union with the same L. Interleaving
the finite preamble and the tail before this stage causes no problem; every
prefix after all preamble terms still contains an initial segment of the
ordered tail. Ties are treated as separate occurrences.

If the tail also satisfies U_t-b_{t+1}>=2L-1 for all sufficiently large t,
then the union's later surplus equals P+U_t-b_{t+1} and satisfies the same
inequality. Thus the seed-plus-surplus property lifts as well.

## Reduction of finite deletions to uniform cutoffs

For fixed D,k,F, choose an integer K>=k greater than every exponent in F.
The remaining occurrences split into the entire uniform-cutoff-K tail and
the finite multiset

    B={(d,j): d in D, k<=j<K, (d,j) not in F},

interpreted by their values and labels. If C1 is known for every uniform
cutoff with F empty, its cutoff-K instance and the preamble lemma prove C1
for this D,k,F. Conversely, the all-F assertion includes F empty. Therefore
the all-positive-cutoff version of C1 with F empty is equivalent to its
all-finite-deletions version.

The same equivalence holds for C2. Its cutoff-K instance first propagates
the tail's central intervals. The preamble lemma supplies the union's
interval and surplus after a sufficiently late prefix; choose that prefix
also beyond every deleted value. It then meets all clauses of C2. The reverse
implication again takes F empty.

This is not the false assertion that finite deletion preserves an arbitrary
complete sequence. The hypothesis explicitly supplies the desired property
for every later uniform cutoff before adding back a finite preamble.

## Costs and unresolved obligations

The move pays object, implication and obligations for replacing the attacked
target C1 by C2. Only C2 implies C1 is established; the all-future bound and
actual seed remain unproved. The finite-preamble lemma is an elementary
interval-union argument, not a claimed new completeness theorem.

The precise simplification is that a proof of C2 may focus on F empty while
retaining every positive cutoff. This does not reduce the range of D or
discard reciprocal equality. Small hand tests of the joint seed criterion
are next; no computational process has been run or admitted.
