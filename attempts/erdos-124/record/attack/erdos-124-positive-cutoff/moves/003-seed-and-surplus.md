# Move 3: separate the seed from the forward surplus

Date: 2026-09-06. Source: node-000001, move 3, pass 1.
Strategy: strengthen-and-generalise, step 4.
Entry: strengthen-the-inductive-hypothesis.
Status: an elementary conditional extension argument and a failed early-seed
attempt. The full C1 and Erdős 124 claims remain open. Independent result
acceptance has not occurred.

## The strengthened state

Retain the notation of move 1. For a nondecreasing positive sequence a_i, put
S_m=sum_{i<=m}a_i and T_m=FS(a_1,...,a_m). Track both a represented central
interval and the forward surplus

    E_m = inf_{r>=m}(S_r-a_{r+1}).

The infimum is allowed to be minus infinity. It is not a value that a finite
test is assumed to compute. The strengthened seed condition is

    S_m >= 2L,
    [L,S_m-L] intersect Z is contained in T_m,
    E_m >= 2L-1.

Under these hypotheses, the central interval survives all later steps. At
step r, the surplus inequality gives a_{r+1} <= S_r-2L+1. Thus the two known
integer intervals [L,S_r-L] and [L+a_{r+1},S_{r+1}-L] overlap or are adjacent.
Their union is [L,S_{r+1}-L]. Its length strictly increases by a_{r+1}>0.
Also E_{r+1}>=E_r, since its infimum is over a smaller set. This proves the
inductive step with both components preserved and the represented interval
strictly enlarged. Positivity ensures S_r tends to infinity, so the condition
also implies eventual completeness of the sequence.

This is a conditional Brown-type interval argument. It proves neither the
existence of a suitable seed nor the asserted lower bound on E_m.

## Exact surplus for the labelled power streams

Let sigma=sum_{d in D}1/(d-1), let

    C = sum_{d in D}d^k/(d-1) + sum_{(d,j) in F}d^j,

and suppose q=a_{m+1} exceeds every deleted value in F (use zero as the maximum
when F is empty). For each base d, let x_d be the first remaining power of d
not used in the prefix. Then x_d>=q, min_d x_d=q, and every deleted occurrence
of that base lies below x_d. The powers of base d below x_d have total
(x_d-d^k)/(d-1). Subtracting the deleted occurrences gives exactly

    S_m = sum_{d in D} x_d/(d-1) - C,
    S_m-q = (sigma-1)q + sum_{d in D}(x_d-q)/(d-1) - C.          (1)

Each stream is handled separately, so coincident powers are counted with
their original multiplicity. A prefix that ends among equal values is also
covered: the unprocessed streams still have x_d=q.

Equation (1) implies

    S_m-a_{m+1} >= (sigma-1)a_{m+1}-C.                         (2)

For sigma>1, the same constant C applies to every later prefix. Therefore

    (sigma-1)a_{m+1} >= C+2L-1                               (3)

is sufficient to guarantee E_m>=2L-1. This follows because later next terms
are no smaller. Thus, at strict reciprocal mass, a single represented seed
interval beyond all deletions, together with (3), is a finite sufficient
certificate for the infinite extension. The analytical inequality covers the
whole tail; no unchecked finite range is substituted for it.

The certificate still includes an actual represented seed. Inequality (3)
alone does not create one. No existence theorem for such a seed is claimed.

At sigma=1, equation (1) instead leaves the required condition

    sum_{d in D}(x_d-q)/(d-1) >= C+2L-1

at every later prefix. The elementary bound (2) is only -C in this case and
does not supply the needed positive surplus. No statement that gcd(D)=1
settles this condition is made here.

## Exact check on the test family

For D={3,4,7}, k=1 and F empty, sigma=1 and C=4. At prefixes 4,5,6 the next
power vectors (x_3,x_4,x_7) and surplus values are respectively

    m=4: (27,16,49), q=16, S_m-q=23-16=7;
    m=5: (27,64,49), q=27, S_m-q=39-27=12;
    m=6: (81,64,49), q=49, S_m-q=66-49=17.

Substitution into (1) gives the same values: 11-4=7, 16-4=12, and 21-4=17.
These three substitutions are hand checks of the identity, not a search.

## The early-seed attempt fails

The attempted base was the first central interval found in move 2, namely
[9,14] at prefix 4, with L=9. Its required surplus is 2L-1=17, but its next
surplus is only 7. The base does not satisfy the strengthened invariant.

The first unused-term repair appends 16. The maximal central interval becomes
[19,20], so repairing the endpoint loss would require L=19. Its required
surplus is 37, but the next surplus is 12. The second repair appends 27; the
new midpoint 33 is absent, so there is no nonempty central interval at all.
Neither repair initializes the strengthened invariant.

There is also a permanent reason that the original endpoint loss cannot be
repaired by waiting. Move 2 proves that 18 is absent from the prefix ending
in 16, and every later term is at least 27. Hence 18 is absent from the full
tail. Any eventual central-prefix interval with L<=18 would eventually
contain 18, so no such L can work. Similarly 33 is absent from the prefix
ending in 27 and every later term is at least 49; consequently C1 for this
particular tail requires L>=34. The published last exception 581 would give
the stronger necessary L>=582, but that published computation is not needed
for either hand-checked obstruction.

The strategy's base-failure signal fires for this early-seed attempt after
the two explicit repairs. It does not refute C1, does not prohibit a later
seed with a larger L, and does not refute eventual completeness. The C1
successor remains relevant precisely because it must construct such a seed
independently of the first small central interval.

## Result classification and next hypothesis

The mathematical output is the conditional extension criterion (1)-(3) and
the exact failure of this attempted base. The interval mechanism and geometric
sum calculation are elementary applications of the methods already recorded
in the primary-source study, not a claimed new completeness theorem.

The move pays obligations: the seed must still be produced, and the critical
case needs a stronger all-future estimate than (2). A separate exact-scope
record is needed before treating any strict-mass criterion as an accepted
lemma contributing to C1. No assumption is silently added to either root.

Next hypothesis: choose the endpoint loss and seed scale together, after
accounting for permanent small omissions, instead of propagating the first
available interval. Investigate the admitted C1 successor without abandoning
the full original objective or granting new budget.
