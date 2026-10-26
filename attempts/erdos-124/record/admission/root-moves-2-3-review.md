# Independent mathematical review of root moves 2 and 3

Date: 2026-09-06.
Reviewed: `attack/erdos-124-positive-cutoff/moves/002-small-prefix-test.md`
and `003-seed-and-surplus.md` in the same directory.
Reviewer: host session `01a078c1-781b-7580-9bcf-aaa4625cf458`.

Finding: no substantive mathematical error under the inherited positive-integer
conventions. Two wording clarifications are noted below. This is a mathematical
review, not formal controller acceptance.

1. The displayed T_3 is exact.
   S_4=23 and the representations of 9 through 14 are correct; missing 8 and
   complement symmetry exclude 15, proving maximality of [9,14]. Likewise,
   S_5=39, the proof that 18 is absent is exhaustive, and symmetry excludes 21,
   so [19,20] is the maximal central interval. At S_6=66, the three cases for
   33 are exhaustive: using 27 requires unavailable 6; using 16 without 27
   requires unavailable 17; using neither permits at most 23. Every nonempty
   integer central interval contains 33. These are also global omissions:
   after the prefix ending at 16, all terms are at least 27>18; after the
   prefix ending at 27, all terms are at least 49>33. Positivity therefore
   excludes any later representation of either number. Eventual central
   coverage requires L>=19 and, more strongly, L>=34. Move 2's decision not to
   assert global absence is consistent with Move 3 proving it.

2. Once q exceeds every deleted value, the
   prefix contains precisely the powers from d^k up to, but excluding, x_d
   in each base stream, minus that stream's deleted occurrences. The geometric
   total is (x_d-d^k)/(d-1), so both identities (1) and bound (2) are correct
   with the stated C. If a prefix ends inside a tie, each unprocessed tied
   stream has x_d=q; a processed tied stream has its next power instead.
   Separate summation over labels preserves multiplicity without omission or
   double use. For the test family, C=4; all three next-power vectors and
   the surplus values 7, 12, 17 check exactly.

3. A represented nonempty seed and
   E_m>=2L-1 give the append inequality at every r>=m. The two translated
   integer intervals overlap or are adjacent, and their union has endpoints
   L and S_{r+1}-L. Also E_{r+1}>=E_r. For sigma>1, every later q_r>=q remains
   above all deletions, and (2)-(3) give
   S_r-a_{r+1}>=(sigma-1)q_r-C>=(sigma-1)q-C>=2L-1.
   This proves the claimed infinite propagation. A finite seed certificate
   must still include S_m>=2L and representations of every integer in the
   seed interval. The numerical threshold alone neither supplies a seed nor
   proves C1. No finite verification process is authorized by this observation.

4. The initial L=9 requires surplus 17 but has only 7.
   The first repair's L=19 requires 37 but has only 12. The second repair
   lacks any nonempty central interval. These facts invalidate this attempted
   initialization. Failure of the sufficient inequality alone is not generally
   a coverage obstruction. The explicit omissions here justify the stated
   failures, while remaining compatible with later seeds at larger L, C1,
   and eventual completeness. The cited exception 581 is unnecessary for
   these deductions.

Wording clarifications: Move 3, line 12, should explicitly say "a nondecreasing
sequence of positive integers" and retain integer L>=0 when presenting the
criterion independently. At lines 73-79, "required condition" means required
by this sufficient surplus invariant, not proved necessary for C1 or the root.

C1, seed existence, and the equality-case extension obligation remain
unsettled. No mathematical search or experiment was performed, and no
controller or native file was edited. This review grants no proof acceptance,
renewal, or extra allowance; the reported three used moves and zero runs remain
on the account shared by the root and child.
