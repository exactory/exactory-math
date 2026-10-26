# Independent review of C1 move 1

Date: 2026-09-06.
Source: `attack/erdos-124-central-prefix/moves/001-joint-seed-and-finite-preamble.md`.
Reviewer: host session `01a078c1-781b-7580-9bcf-aaa4625cf458`.

Finding: the stated implications and finite-deletion equivalences are correct.
No substantive mathematical error was found. C2 itself remains unproved.

1. The C2-to-C1 induction is valid. The future surplus bound gives
   L+a_{r+1}<=S_r-L+1 at every later step. The represented interval and its
   translate therefore join, preserving the same L without reusing a label.
   The seed condition S_m>=2L ensures nonemptiness.

2. The finite-preamble argument is correct. Since b_i tends to infinity,
   only finitely many tail occurrences lie below or at any preamble value.
   Thus every sufficiently late union prefix contains all of B and an initial
   tail segment, even with interleaving and ties. The union ordering can retain
   the tail's tie order; permuting equal-valued labels does not change its
   subset sums. Selecting none or all of B gives the two stated intervals.
   For nonempty intervals their exact adjacency condition is
   P+L<=U_t-L+1, equivalently U_t>=P+2L-1. Their union is then
   [L,P+U_t-L]. Eventual nonemptiness follows from U_t tending to infinity.
   If B is empty, the threshold alone permits the vacuous case U_t=2L-1;
   taking t later also ensures U_t>=2L. This does not affect the lemma.

3. After all of B has appeared, the next union term is b_{t+1}, so its surplus
   is exactly P+U_t-b_{t+1}. Since P>=0, a tail bound
   U_t-b_{t+1}>=2L-1 transfers to every sufficiently late union prefix.
   The interval and surplus requirements can consequently hold from one
   common starting prefix onward.

4. Choosing K>=k above every deleted exponent gives a disjoint partition by
   labels into the untouched cutoff-K tail and the stated finite B. It does
   not imply numerical separation between these parts, which the preamble
   lemma does not require. For C1, the cutoff-K instance directly supplies
   the required tail intervals. For C2, its cutoff-K instance first supplies
   those intervals by induction and supplies the future surplus bound.
   Choose a union prefix late enough for both lifted properties, a nonempty
   seed, and its next value to exceed every deleted value. Such a prefix
   exists because the remaining terms tend to infinity. All later prefixes
   preserve the requirements. Conversely, arbitrary-F C1 or C2 includes
   F empty. Both equivalences therefore hold with every positive cutoff
   retained. The forward proofs explicitly use the cutoff-K instance.

This review establishes no converse C1-to-C2 and no existence of a C2 seed.
It makes no novelty claim and grants no controller acceptance or budget credit.
No mathematical computation process was run and no controller or native file
was modified.
