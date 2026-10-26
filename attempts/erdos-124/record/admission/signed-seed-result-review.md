# Independent RESULT review of the signed-tail counterexample

Decision: approve the analytical counterexample to obligation-000013.
There are no unresolved mathematical objections. This review concerns
node-000009, move 1, and corrected checkpoint-000015, reported at revision 175.
It is a result review, not proposal review, publication-novelty assessment,
formal certification, controller acceptance, or a ResultAudit.

## Reviewer and materials

The observed host identity from `id -un` is `<user>`. The observed
`CODEX_THREAD_ID` is `01a07cc4-30a4-7380-94da-867436c06ecc`.
These differ, respectively, from the proposal author's
`codex-root-01a07806` and
`session-01a07806-b2c5-7163-86d2-92fd0ef5cf33`.
I reviewed the proof independently in this context. I did not read any
previous review or producer conversation.

I read the installed Codex README, the complete shared math-solver SKILL.md,
and SEARCH.md's review/provenance, checkpoint/result-review, and immutable
evidence sections before inspecting the evidence. The mathematical source
was the complete 343-line `attack/erdos-124-signed-tail-seed/moves/001-sparse-signed-blocks.md`.
All proof line references below refer to that file.

The remaining prescribed materials were the analytical manifest,
`admission/checkpoint-signed-seed-001.json`, its explicitly supplied correction
`admission/checkpoint-signed-seed-002.json`, the admitted proposal,
`units/consolidation.md`, and the producer's `journal.jsonl`.
Consolidation supplied exposition only. No other mathematical source was used.

## Snapshot identity and limits of the metadata check

This review and the accompanying public acceptance specification bind:

- Complete stored checkpoint-000015 digest:
  `281085bbf548201f3de67dd6cf0b51a6c760e0e30d23c6aee5d61fe5a80d7a28`.
- Exact Claim digest:
  `361cec84057a818f1be5992d977c22111e2901adf1398a5c0cf507ac72c77166`.
- Canonical manifest digest:
  `0b42c83546348c27ec19dc869518f46540ea445cfb9dd008acf8dd4690e5107f`.
- Raw proof digest:
  `477181b9f756c38046d89b82700641169272c5551e2d6cd798dc6508e17cec9b`.
- Raw journal-prefix digest:
  `57e4d4cdaa16c678f40257cc83108d7d80f604eb9fcb2dcfeebbc4fb80674ccd`.

The full stored subject is the corrected input's `checkpoint` object with
`id: "checkpoint-000015"` and `verification_status: "pending"` added.
It is not the wrapper containing `inputs`, and not checkpoint-000014.
JSON digest identities use sorted compact canonical JSON; artifact and
journal identities use raw bytes.

Structural comparison of the read JSON confirms that the corrected Claim
equals both the proposal's Claim and its signed-tail-seed decomposition
Claim. Compared with the first checkpoint input, only `what_changed` and
`remaining_obligation_ids` changed. The latter removes exactly
obligation-000004 and obligation-000007. Claim, origin, evidence references,
milestone, and next hypothesis are unchanged. This is a metadata correction
with no new mathematical or budget credit. The relevant service status is
`accepted`, not `proved`; I did not independently query service state.

The manifest declares one analytical proof artifact, the counterexample
outcome, empty dependency and route-binding lists, empty external
dependencies, and null verification. The corrected checkpoint names that
manifest and node-000009's move 1. The journal contains that closing move,
an empty mathematical `steps` list, and the matching analytical description.

Independent digest recomputation was limited: the installed PreToolUse hook
refused the direct `shasum -a 256` command for the proof and journal as an
unsupported managed shell operation. I did not bypass or retry the refusal
through another implementation. Consequently the digests above are supplied
identities, not freshly recomputed hashes. I rely on the expressly reported
service validation of the input identity and reserved journal origin; the
service must perform its required immutable-evidence/freshness audit before
acceptance. The structural checks and mathematical review do not themselves
claim to authenticate frozen bytes or create a journal reservation.

## Extension, estimates, and legal supports

Lines 12-41 define an unambiguous infinite sequence. For t >= 5,
`k_t - m_(t-1) = 2^(t-1) - 2t` is positive initially at t = 5 and
stays positive by the stated induction. Also k_4 = 8 and m_4 = 16.
Thus the closed blocks are disjoint, none of their interiors is an earlier
modified endpoint, and substituting v_j for b_j in each interior is valid.
Equation (2) follows exactly from (1), with no error term.

I checked the full baseline estimate at lines 43-75. There are m-2 terms in
the floor sum, and `2 sum_(j=2)^(m-1) 3^j = 3^m - 9`, so the loss
`-9 - 2(m-2)` in the initial bound is correct. Multiplication by j*m^2
reduces the reciprocal identity at line 55 to `(m-j)^2`, proving its sign.
The j = m-1 term alone supplies the second lower bound at line 61.
Combining these gives precisely
`(2/3)3^m/m^2 - 2m - 5 - 9/m`.

The comparison `3^m >= 12m^3` holds at m = 8 because 6561 >= 6144;
its consecutive ratio is at least `3(8/9)^3 > 1`.
For m >= 8, `2m >= 5 + 9/m` (the left side is at least 16 and the
right side at most 49/8). Hence subtracting the error term from (3)
leaves at least `3^m/(3m^2)`, as in (4). No asymptotic estimate is
being used to justify an unverified initial range.

For (5), the strict bound b_j < 2*3^j gives
`2 sum_(j=2)^(k-1) b_j < 2(3^k-9) < 2*3^k` when k > 2;
for k = 2 the empty sum directly satisfies (5).
The delta identity subtracts the old prefix of b, not v, and is exact.
With m = 2^t and k = m-2t, the inequality needed at line 91 is
equivalent to `12(4/9)^t <= 1`. The stated value at t = 4 is
3072/6561 < 1, and the expression decreases thereafter. Therefore
`delta_t >= 3^m/(6m^2)-1 >= 2m-1 > 0` for m >= 16.
This establishes every upward replacement, not just positivity.

At an endpoint, the upper geometric bound is
`v_m < 4 sum_(j=2)^(m-1) 3^j = 2(3^m-9) < 2*3^m`.
Together with upward replacement this proves all of (7). In particular
adjacent levels have strictly different values, the sequence ordered by
levels is nondecreasing, every value occurs exactly twice, all terms are
positive integers, and v_j >= 3^j proves local finiteness.

Lines 108-124 handle both possible kinds of level. At an unmodified
level, the current b_m is unchanged and every earlier replacement is
nonnegative, so (8) follows. At a modified endpoint, the interior terms
cancel exactly using (2), leaving the earlier v prefix plus 1. Its lower
bound is `2 sum_(j=2)^(k-1) 3^j + 1 = 3^k-8`.
Since k >= 8 implies 3^k >= 16, (9)'s halving bound is valid. Earlier
replacements are retained and cannot invalidate either estimate.

For lines 169-184, the 2t interior levels contribute exactly 4t distinct
positive-side labels, and the endpoint contributes one negative-side label.
The identity is therefore a legal signed unit with support size 4t+1.
P_t and Q_t are disjoint, and different t use disjoint closed level blocks.
Since k_t tends to infinity, every occurrence cutoff, including one between
two equal copies, precedes all these supports for sufficiently large t.
This proves the exact quantified legal-unit antecedent.

## Tail arithmetic and norm divergence

Lines 186-196 correctly give additional properties of this same sequence.
For any positive integer r and any cutoff, choose r later blocks. Replacing
P_t by Q_t increases the positive subset sum by exactly 1 independently in
each block. The r+1 sums N through N+r all occur. For any prescribed signed
integer z, use |z| distinct blocks with the appropriate orientation; zero
uses the empty signed sum. These assertions respect every label and do not
assert a fixed central loss.

The gcd argument at lines 200-201 is valid for every tail: any positive
common divisor must divide the legal signed sum 1. For modular coverage,
there are finitely many residue classes, so the classes that occur only
finitely often can all be removed by one finite further cutoff. The remaining
classes R must generate the full cyclic group. Indeed the inverse image in
Z of any proper subgroup of Z/hZ is gZ for a divisor g > 1 of h; this
follows from the least positive element and integer division. Such a subgroup
would make all terms in that later tail divisible by g, contradicting its
gcd one. This is an elementary cyclic-group fact, not an undeclared theorem
dependency.

An integer combination of residues can be made nonnegative by reducing each
coefficient modulo h. Infinite availability in each class permits selection
of the required finite number of distinct labels. Residue zero can use the
empty subset, or h distinct occurrences of any one class if a nonempty sum
is desired. Thus the proof covers every tail and every positive modulus,
including h = 1. The interval assertion also directly implies modular
coverage by taking at least h consecutive represented integers.

Lines 221-242 prove the norm assertion for every noninteger alpha, which is
stronger than the required irrational assertion. Apply the triangle
inequality for distance to Z to alpha times the exact signed identity, then
apply Cauchy-Schwarz to its 4t+1 nonnegative distances. This gives (13) with
the strictly positive constant ||alpha||^2. Disjoint supports allow their
squared contributions to be added without duplication. Finally
`1/(4t+1) >= 1/(5t)` and the harmonic series diverges. Deleting finitely
many occurrences removes no sufficiently late block, so the same argument
holds in every tail. Growing supports alone would not suffice; the proof
supplies exactly the necessary divergent reciprocal-length bound.

## Every fixed beta and every occurrence prefix

For each fixed beta in (0,1), division of (8) by the upper bound
`(2*3^m)^beta` gives (14). The logarithm of its lower bound is
`(1-beta)m log 3 - 2 log m` plus a constant, which tends to infinity.
At endpoints, division of (9) by `(2*3^(2^t))^beta` gives exactly
`2^(-beta-1) 3^((1-beta)2^t-2t)`, as in (15).
Its exponent tends to infinity because 2^t/t tends to infinity.
Both claims allow a threshold depending on beta. They assert no uniform
threshold as beta approaches 1 and no conclusion at beta = 1.

For any requested lower bound, only finitely many unmodified levels and
finitely many endpoint levels fail the corresponding bound. Combining these
finite exceptions proves the limit along all levels. Before the first copy
of level m there are exactly 2(m-2) occurrences and the surplus is E_m^v.
Before the second copy there are 2(m-2)+1 occurrences and the surplus is
E_m^v + v_m with the same denominator v_m^beta. These exhaust all prefixes.
The finitely many initial levels, including the empty prefix if considered,
do not affect the limit. Thus every occurrence prefix satisfies the exact
almost-linear surplus antecedent for every fixed beta in the required range.

## Label count, numerical support, and the contradiction

For large X, the number of present levels is bounded below by
`floor(log_3(X/2))-1` and above by `floor(log_3 X)-1`.
Each contributes exactly two labels, so (16) has the claimed limit
`2 log 2/log 3 = log 4/log 3 > 1`. This verifies the strict labelled
counting hypothesis.

Lines 126-134 and 289-301 separately control numerical support. A finite
label subset determines a finite vector with c_j in {0,1,2}. These are
canonical ternary digits after shifting the starting exponent by two;
uniqueness follows successively by reducing modulo 3 and dividing by 3.
Thus T(c) identifies the coefficient vector, with trailing zero digits
understood as part of the same finitely supported vector. Since v_j >= 3^j,
the numerical sum is at least 9T(c).

Every vector producing a positive sum at most X consequently has a distinct
integer T(c) in [1,floor(X/9)]. Hence there are at most floor(X/9) such
vectors. Mapping those vectors to their numerical sums is a surjection onto
the represented positive integers at most X, so collisions can only reduce
that count. This proves (17) for every real X >= 0, including X < 1.
There is no assumed injection from labelled subsets to sums and no use of
the abundant labels as a lower bound for numerical support. The upper
asymptotic density is at most 1/9, so the positive support is not cofinite.

For any hypothetical integers L >= 0 and m_0 >= 1 satisfying the conclusion,
fix an integer n >= L. Positivity and infinitely many terms imply S_m tends
to infinity, so some m >= m_0 has S_m >= n+L and S_m >= 2L. Then n is in
[L,S_m-L] and the hypothesized prefix coverage represents it. This would
represent every integer n >= L in the global finite subset-sum set, making
it cofinite and giving density 1, contrary to (17). This contradiction
includes L = 0. It disproves the exact existential conclusion for this
sequence and therefore refutes the admitted universal implication.

## Seed checks, dependencies, and final scope

The minimality statements at lines 142-165 and 314-319 are valid with their
explicit template restriction. Starting the prescribed consecutive schedule
at t = 1 or 2 gives a start of 0; starting at t = 3 forces the overlap
B_3 = [2,8] and B_4 = [8,16]. Starting at t = 4 works by the proved
disjointness law. One complete block is the smallest nonempty number of
complete scheduled blocks. Levels 2 through 16 with the B_4 endpoint
replacement satisfy the upward estimate, legal unit identity, and surplus
at least 3^8-8. This is not minimality among arbitrary sequences or arbitrary
partial seeds. For integer-base templates q >= 2 with q-1 copies, q = 2
has label exponent exactly 1 while q = 3 has exponent log 4/log 3 > 1;
there is no smaller intervening integer base.

The stated limitations are consistent with the proof. At an endpoint the
retained-prefix surplus is at most `2*3^k+1`, while the next term is at
least 3^m, so its ratio to the next term tends to zero as m-k = 2t grows.
No positive linear-scale surplus follows. Extra copies would remove the
digit-range argument, and a convergent reciprocal support-length sum would
not prove norm divergence by (13). The support-count deficit survives each
extension because the digit range and v_j >= 3^j survive each extension.

The construction uses only the elementary identities and inequalities
checked above. No mathematical dependency on Graham, the predecessor
construction, an accepted result, a certificate, or a formal theorem is
required. Empty dependency_ids and route_bindings are appropriate and match
the manifest. The analytical classification and reviewed proof policy match
the exact admitted Claim. I ran no mathematical program, solver, finite
enumeration, compilation, certificate, or Lean check, and issued no Exactory
controller or native mutation.

Approval applies only to the counterexample for obligation-000013. It does
not decide the original pure-power objective, C1 for pure powers, any
pure-power profile, or any implication bridge. The accompanying JSON is the
requested public specification for subsequent service use; this review does
not itself accept a result or change any obligation's status.
