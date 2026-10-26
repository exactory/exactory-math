# Move 2: a central interval can disappear under extension

Date: 2026-09-06. Source: node-000001, move 2, pass 1.
Strategy: strengthen-and-generalise, step 3.
Entry: test-strengthenings-by-counterexample.
Status: exact hand checks of the proposed mechanism; no counterexample to C1
or to the original eventual-completeness claim.

## Purpose and scope

Test whether merely finding a nonempty central interval is a stable seed for
C1. Use the smallest published equality example D={3,4,7}, cutoff k=1, and
F empty. Its bases are distinct, their gcd is 1, and
1/2+1/3+1/6=1. The first six labelled occurrences have distinct values

    3, 4, 7, 9, 16, 27.

Only these six terms are checked. This is a necessary diagnostic of the
proposed append operation, performed by hand, not an enumeration program or
an extension of a tested range.

## Prefix of length four

For (3,4,7), the subset sums are exactly

    T_3={0,3,4,7,10,11,14}.

Adding 9 gives T_4=T_3 union (9+T_3), with total S_4=23. Its central interval
[9,14] has the explicit representations

    9=9, 10=3+7, 11=4+7,
    12=3+9, 13=4+9, 14=3+4+7.

The integer 8 is not in T_3 and is below 9, so 8 is not in T_4. Complement
symmetry gives 15 not in T_4. Thus [9,14] is the maximal central interval.
It has length 6, less than the next term 16. The sufficient append condition
already fails at this seed.

## Prefix of length five

Now S_5=39. The integers 19=16+3 and 20=16+4 are represented.
The integer 18 is not represented: without 16, including 9 would require
9 in T_3, which is absent, while excluding 9 gives at most 14; with 16 it
would require 2, which is absent. Complement symmetry excludes 21.
Consequently the maximal central interval is [19,20], of length 2.

In particular, appending an unused term can shrink the central interval even
though the subset-sum set itself only grows. Its centre and total also change.

## Prefix of length six

Now S_6=66. Its midpoint 33 is not represented.

- If 27 is used, the remaining sum must be 6. No subset of the other positive
  terms has sum 6: 7,9,16 are too large, and subsets of {3,4} give 0,3,4,7.
- If 27 is not used but 16 is used, the remainder must be 17. Without 9,
  {3,4,7} totals only 14. With 9, the remaining sum must be 8, absent from T_3.
- If neither 27 nor 16 is used, the maximum available sum is 23.

Every nonempty integer interval [L,66-L] contains 33. Therefore this prefix
has no nonempty represented central interval, for any L.

## Interpretation and failure signal

The hypothesis "a nonempty central interval is enough to continue the
induction through unused terms" is false even in an admissible equality
family. The exact sufficient length condition from move 1 cannot be omitted.
Two additional terms after the first central seed do not repair this example:
the central interval first shrinks and then disappears.

This does not refute C1. C1 permits a later m_0, and the original claim permits
finitely many omitted integers. In particular, 33 being absent from these six
terms is not a claim that 33 has no representation from the full tail, nor a
claim of infinitely many omissions. BEGL96 already proves eventual coverage
for this family's cutoff 1.

The entry's no-counterexample failure signal fires for C1: this finite check
does not reach its unknown asymptotic thresholds, and C1 still implies the
unresolved original target. Step 4 must supply an invariant with an actual
seed and all-future control. No solver run occurred, and no theorem acceptance
or budget renewal follows from this diagnostic.
