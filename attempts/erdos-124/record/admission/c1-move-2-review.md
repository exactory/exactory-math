# Independent review of the translated-power barrier

Date: 2026-09-06.
Reviewed: `attack/erdos-124-central-prefix/moves/002-translated-power-barrier.md`,
its `study/arithmetic-seed-barrier.md`, and G in `problem.json.shape.neighbours`.
Reviewer: host session `01a078c1-781b-7580-9bcf-aaa4625cf458`.

Finding: the analytical construction refutes G in its exact stated generic
scope. No mathematical error was found. This is an independent mathematical
review, not controller proof acceptance.

1. The sequence has all the required structural properties: positive integer
   values, nondecreasing order, local finiteness, divergence to infinity, and
   bounded numerical multiplicity q-1. At a block endpoint its surplus is
   (q-1)t-q^k-1. At an interior prefix it is that endpoint surplus plus
   s(q^(m+1)+1), for 0<=s<q-1. The endpoint lower bounds tend to infinity,
   proving convergence along every prefix, not merely a subsequence. Beyond
   all finite deletions, corresponding prefix totals differ by the fixed
   deleted sum and have the same next term, so the conclusion survives.

2. The adjacent-value gcd calculation is correct. Evenness of q is essential
   to gcd(2,q-1)=1, and every tail contains adjacent exponent values. The
   stronger modular claim also follows. Modulo h, finitely many residue
   classes occur only finitely often. Past their last occurrence, any g>1
   dividing h and all recurrent residues would divide an entire suffix,
   contradicting the every-tail gcd hypothesis. Thus recurrent residues generate Z/hZ.
   Nonnegative combinations suffice in this finite group, and their infinitely
   many occurrences supply distinct labels. This proves every residue is
   represented in each prescribed tail, without a uniform representation bound.

3. Irrational squared-norm divergence is proved correctly. Convergence would
   force ||b_j alpha|| to zero. The exact recurrence
   q*b_j-b_(j+1)=q-1 then forces ||(q-1)alpha||=0, impossible for irrational
   alpha. Repeated labels multiply the sum by q-1; finite deletion cannot
   remove divergence. The conclusion holds for each irrational alpha and
   each tail, without requiring a bound uniform in alpha.

4. The labelled count is
   (q-1)(floor(log_q(X-1))-k+1) for sufficiently large X. It gives the stated
   exponent (q-1)log(2)/log(q)>1, equal to 3/2 at q=4. Here A(X) counts
   occurrences, and 2^A(X) counts choices of labels. Different choices can
   produce the same coefficient at an exponent and the same numerical sum.

5. Each coefficient c_j lies in {0,...,q-1}, so these coefficients are exactly
   the base-q digits of t. Consequently the numerical image is precisely
   {q^k*t+s_q(t): t>=0}, including zero from the empty subset. Every positive
   image value at most X has 1<=t<=floor(X/q^k). Counting these possible inputs
   proves the asserted upper bound even if different inputs collide. Hence
   upper density is at most q^(-k)<1; no equality or injectivity is needed.
   Infinitely many omissions follow. Eventual central-prefix coverage would
   make the full subset-sum set cofinite, giving the required contradiction.
   The sample block totals and endpoint surpluses also check correctly.

The ruled-out seed is a nonempty central interval paired with the required
all-future surplus threshold for that same L. The argument does not rule out
every temporary central interval. Nor does it refute pure-power C1 or C2:
G explicitly drops that structure, and the construction supplies translated
powers with repeated labels rather than an admissible finite D and its
base-exponent occurrences. No assumption that all C1 instances satisfy G's
premises is needed or established.

No novelty is certified and no controller acceptance or budget credit is
granted. No finite mathematical execution was performed. The proof and
controller files were left unchanged.
