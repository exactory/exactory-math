# Move 1: exact support accounting for switch amplification

Date: 2026-09-07. Node: node-000008, erdos-124-carry-seed.
Strategy: make-the-proof-constructive. Entry: seed-and-amplify, first application.
This is an analytical construction ledger and conditional lemma. It is not a
proof of the root and has not received independent result acceptance.

## 1. A maximum-gap identity

Let R=(r_1,r_2,...) be an infinite nondecreasing locally finite sequence of
positive integers. Occurrences are labelled, so numerical ties are allowed.
Write T_j=sum_{i<=j}r_i, T_0=0, and let C be its finite subset sums including 0.
If

    K = sup_{j>=1}(r_j-T_{j-1}) < infinity,

then K is a positive integer and is exactly the largest difference between
consecutive elements of C.

Here is a proof, including both directions. For a finite prefix define G_j
as the largest distance between consecutive subset sums, with G_0=0.
The next subset-sum set is the union of the old set and its translate by
r_{j+1}. Its two convex hulls are [0,T_j] and [r_{j+1},T_j+r_{j+1}].
Inside either hull the old mesh has gaps at most G_j. If the hulls are disjoint,
the only additional gap has size r_{j+1}-T_j. If they overlap, the endpoints
belong to the union and no gap crossing an endpoint can increase this bound.
Thus

    G_{j+1} <= max(G_j, r_{j+1}-T_j).

Induction gives G_j<=K. Any two consecutive elements of C both occur in a
sufficiently long finite prefix, so their gap is at most K.

Conversely, the integer-valued supremum K is attained, and K>=r_1>=1.
Choose j with r_j-T_{j-1}=K. Both T_{j-1} and r_j belong to C. A subset sum
using only earlier occurrences is at most T_{j-1}; a subset sum using any
later occurrence is at least r_j. Hence these are consecutive elements
of C, with gap K. This proves the identity.

This is a Brown-type maximum-gap argument, not a claimed new general
completeness theorem. It does not assert that gcd one or bounded K makes K=1.

## 2. The exact deletion cost

Now let A=(a_i) be the labelled power stream for fixed admissible D and k,
with S_m=sum_{i<=m}a_i and S_0=0. Let V be a finite set of occurrence indices,
and put

    W_m = sum_{i in V, i<=m} a_i,
    W = sum_{i in V} a_i,
    R = A with V removed.

At a retained index i, the sum of preceding retained terms is S_{i-1}-W_{i-1}.
Section 1 therefore gives the exact maximum subset-sum gap of R as

    K_V = sup_{i notin V}(a_i-S_{i-1}+W_{i-1}).                 (1)

The accepted all-future surplus theorem at checkpoint-000009 makes this
quantity finite: after the last removed index, W_{i-1}=W is constant while
S_{i-1}-a_i tends to positive infinity. The finitely many earlier indices
cause no difficulty. Consequently the supremum is a maximum of finitely
many positive candidates. This is an existence statement, not an effective
bound on which indices must be checked.

No extra copies of a numerical value are used. All sums in (1) count the
original occurrence labels.

## 3. Legal switches and their gain

Take finitely many pairs (P_t,Q_t) of finite allowed occurrence sets.
Within a pair assume P_t and Q_t are disjoint, and assume the unions
P_t union Q_t are pairwise disjoint over t. Put

    h_t = sum(Q_t)-sum(P_t) > 0,
    B = sum_t sum(P_t),
    H = sum_t h_t,
    V = union_t(P_t union Q_t).

Choosing exactly one side from each pair gives only legal positive
assignments. Their represented values include exactly

    B + FS(h_1,...,h_s).

Assume the positive h_t have been ordered so that

    h_1=1,
    h_t <= 1 + sum_{u<t}h_u   for every t>=2.                 (2)

The finite Brown induction proves FS(h_1,...,h_s)=[0,H] intersect Z.
Thus the switch choices represent every integer in [B,B+H].
Their total reserved weight is exactly

    W = 2B + H.                                             (3)

Equation (3) measures the support cost that a signed identity alone hides.
The negative sides are never negative final summands. They are alternative
positive assignments, and their total B contributes twice to W-H.

## 4. A sufficient certificate with the residual stream included

Under the hypotheses of Section 3, suppose

    K_V <= H+1.                                             (4)

Then every integer n>=B is a legal subset sum from A.

For x=n-B>=0, choose the largest c in FS(R) with c<=x. Such c exists because
0 is available and the set is discrete. If c' is the next subset sum, then
c'-c<=K_V, so 0<=x-c<=K_V-1<=H. The switch assignments represent B+(x-c);
the residual stream represents c; their occurrence supports are disjoint.
Their union represents n.

The +1 in (4) matters. H is the span of the integer interval, which contains
H+1 integers. Adjacent translated intervals need not overlap in the reals.

Combining (1), (3), and (4), the sufficient condition is exactly

    S_{i-1}-a_i + (W-W_{i-1}) >= 2B-1
        for every retained index i.                        (5)

After the last reserved index this becomes

    S_{i-1}-a_i >= 2B-1.                                    (6)

Checkpoint-000009 guarantees (6) eventually for any already fixed B, including
reciprocal equality. It does not guarantee (5) at the preceding retained
indices for a constructed V. Increasing the size or height of V changes B,
W, and those earlier obligations. There is no legitimate interchange of
these quantifiers.

For fixed V, the method covers every integer starting at B if and only if
the union [B,B+H]+FS(R) has no gap there, equivalently (4). Failure of (4)
does not refute eventual completeness with a larger threshold, nor does it
exhaust other representations available in FS(V).

## 5. Why a fixed buffer cannot absorb all its own choices

Let U be the finite low-coordinate set removed from a zero-cutoff system.
Its subset sums contain 0 and its total C=sum(U)>0. If V is another finite
support set of total W, then FS(V)+FS(U) has minimum 0 and maximum W+C.

There is no integer translation t such that

    t + FS(V) + FS(U) is contained in FS(V),

because the left side has diameter W+C, whereas the right side has diameter W.
The zero-cutoff decomposition

    FS(all zero-cutoff labels) = FS(R) + FS(V) + FS(U)

therefore cannot be turned into positive-cutoff coverage by a universal
replacement confined to that one finite V which handles every one of its
old choices. A construction must select representations depending on the
target, control the remaining stream as in (5), or use a genuinely varying
support family. This is only a failure of that overstrong buffer rule.

## 6. The constructive question that remains

The amplification is valid, and exact support accounting is now explicit.
The unresolved task is to construct legal pairs satisfying (2) and (5) for
every admissible D and every positive k. No such pair family has been
constructed in this move.

Disjoint small-difference identities of uncontrolled height would not suffice:
their negative-side cost B and removed-prefix cost W_m enter (5). Neither
modular coverage nor signed representability proves the support compatibility
or that inequality. The old early central seed and the Gaussian approximation
supply none of these missing data.

The next application should test whether actual variable-length power
identities can satisfy this support ledger. It must first use exact algebraic
structure to control their cost, and must not run an unbounded seed search.
If that cannot produce a seed or changes the ledger without a gain, the
constructive failure signal applies. The full root remains open.

No mathematical program, certificate checker, or formal build was run.
The move changes the working direction to true and mode to construction.
It records the switch seed and its support-cost bound as undischarged obligations.
