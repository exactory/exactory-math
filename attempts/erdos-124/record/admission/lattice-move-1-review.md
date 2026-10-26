# Independent review of the lattice-aware image

Date: 2026-09-06.
Reviewed: `attack/erdos-124-lattice-aware/moves/001-lattice-aware-image.md`,
the node's `problem.json`, Astels's cited definition and theorem passages,
and the installed 0.34.1 entry and strategy instructions.
Reviewer: host session `01a078c1-781b-7580-9bcf-aaa4625cf458`.

The analytical equivalence and thickness upper bound are correct. T remains
unproved. The failure-flag interpretation needs the qualification below, and
the problem metadata contains outdated or ambiguous statements.

1. The exact identity is valid because D is finite and Minkowski sums of the
   error intervals give [-E,E]. Each A_d still uses only finitely many powers
   with exponents at least k. Different bases remain separate summands even
   when their contributions have equal numerical values. Admissibility makes
   D nonempty, so epsilon_d=3/(4|D|) is defined. No closure, infinite digit
   expansion, or changed cutoff is introduced.

2. For a root threshold N, every real x>=N is within 1/2 of an integer n>=N.
   Conversely, an integer n within 3/4 of an integer representable z equals z.
   Thus the two quantified assertions are equivalent, with the reverse
   threshold ceil(X). The window 1/2<=E<1 correctly separates the half-line
   covering requirement from exact integer recovery. It supplies an equivalent
   reformulation and does not establish the image assertion.

3. Astels's definition explicitly permits finitely many gaps
   (`sources/astels-thesis.txt:778`). The compact thickenings therefore fall
   within that generalized definition. Since 0 and d^k are the first two
   centers and epsilon_d<1, their intervening gap has length d^k-2epsilon_d>0.
   In every derivation, the bridge split removing this gap has left child
   [-epsilon_d,epsilon_d]: no earlier gap can cut that leftmost component.
   The definition takes the smaller child-to-gap ratio and then an infimum
   over bridges, followed by a supremum over derivations (text lines 915-934).
   Hence the uniform upper bound survives that supremum. Normalization gives
   gamma<=2epsilon_d/d^k, and summing gives
   sum gamma<=2E/min_d(d^k)<2/3<1 for every finite depth vector.

4. This excludes only the sum-gamma-at-least-one hypothesis in the specified
   direct application of Astels Theorem 3.1.3 to the full compact-prefix
   thickenings. It is not an absence-of-intervals theorem and says nothing
   decisive about T, grouped bases, selected components, or other arguments.
   The additional whole-hull hypotheses cannot rescue this particular use
   once the thickness hypothesis fails.

5. `failure_signal_fired=false` is defensible for a reduction-only move.
   The installed `entries/change-the-ambient-space.md:22` allows an equivalent
   image with a proved pullback; its failure conditions at line 26 are not
   established merely by this one sufficient condition being unavailable.
   The structure is retained and the pullback loses nothing. Listing three
   maps does not establish that every candidate's available theory has failed.
   `strategies/reduce-and-translate.md:104` explicitly recognizes a reduction
   with the image unproved. However, entry Action 4 at line 18 asks for a proof
   of the image, and that action remains unfulfilled. This must not be reported
   as a completed image proof or successful engine import. If this were instead
   treated as an attempted Astels import, the strategy's missing-hypothesis
   failure condition at lines 96-98 would apply. The file's explicit choice
   to record a mapping diagnostic and leave T open supports the narrower flag
   interpretation; it does not authorize ignoring a later failure signal.

The statements in `problem.json:21` about no recorded category equivalence and,
especially, `problem.json:22` about no known exact continuous equivalence should
be qualified to refer to the earlier model or earlier acceptance status. As
written, they conflict with or obscure the same file's recorded exact image T.
The absence of a root proof or a new uniform numerical threshold remains valid.

This is informal independent checking. It grants no controller acceptance,
novelty, budget credit, or permission to bypass a reservation or journal guard.
No mathematical process was run and the proof and node files were not edited.
