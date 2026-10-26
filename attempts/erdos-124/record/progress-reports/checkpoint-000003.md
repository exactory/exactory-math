# Checkpoint report: checkpoint-000003

Overall proof-completion estimate: 4% (subjective, low confidence).
This retrospective research-planning estimate is not a verified fraction of
the proof, a probability of success, or a fraction of the remaining time.
See [reporting policy](README.md) for its interpretation.

This copy adds the estimate retrospectively; the
[original checkpoint report](../attack/checkpoints/checkpoint-000003-report.md)
remains unchanged. The original snapshot content follows.


Date: 2026-09-06. Source: node-000002, move 1.
Logical predecessor: root checkpoint-000001; later root diagnostics are
preserved in checkpoint-000002. Shared usage: 4 of 24 moves, zero runs.

C1 and the complete original Erdős 124 objective remain open. Candidate C2
asks for a jointly chosen nonempty central seed and an all-future surplus
bound S_r-a_{r+1}>=2L-1. Its elementary implication to C1 is written out;
neither the seed nor the bound is assumed established for all admissible D.

The new simplification is finite-preamble lifting. If a locally finite
ordered sequence of positive integers has eventual central-prefix intervals
[L,U_t-L], adding a finite multiset of total P retains that property. The
sumset contains both [L,U_t-L] and its translate by P. They join when
U_t>=P+2L-1, which eventually holds. The later surplus increases by P as well.

For D,k,F, choose K beyond every deleted exponent. The remaining occurrence
sequence is the full cutoff-K tail plus a finite preamble. Therefore an
all-positive-cutoff proof with F empty supplies the all-finite-deletions
version, both for C1 and C2. The converse simply takes F empty. Multiplicities
and interleaving are retained. This does not assert that deleting terms from
an arbitrary complete sequence preserves completeness.

The argument is elementary and no novelty claim is made. Independent review
is pending at this snapshot, and no controller result acceptance is recorded.
The exact evidence is
`../erdos-124-central-prefix/moves/001-joint-seed-and-finite-preamble.md`;
its frozen manifest is `c1-001-manifest.json`.

Next: test whether abstract surplus and arithmetic conditions can provide
the missing seed, without confusing a count of labelled choices with the
number of distinct represented integers. The pure-power hypothesis and the
critical reciprocal-equality case must remain explicit.
