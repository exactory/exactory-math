# Branch-complete proof package

Start with [PROOF.md](PROOF.md). It retains the original inequality and
unique equality case for every5<=n<=15. The proof of why the old missing
Sinkhorn branch is also covered is [BRANCH_TRANSPORT.md](BRANCH_TRANSPORT.md).
The two native children contain their full dimension-specific arguments,
new exact checkers and complete coverage certificates.

## Replay the new finite checks

Run from the Dittert research workspace, sequentially:

```sh
export PATH=<home>/.codex/plugins/cache/exactory-ai/exactory/0.33.1/bin:"$PATH"
exactory-math verify certificate hall-n7-branch-coverage certified-special-case-check-1
exactory-math verify certificate hall-n8-n15-branch-coverage certified-witness-chain-1
```

Both wrappers set one numerical-library thread and nice15 for mathematical
processes. The coordinator reran both commands after reading the complete
checker code, and each exited0 with result.json status pass. This replay
does not rebuild the inherited large n5,6 Gram matrices. The prior permanent
floor checks remain in dittert-completion-tree; the independent reviewer
also reran the small n8,9,10 two-zero floor calculations during this audit.

## Evidence scope

This is an attributed exact computer-assisted proof using cited classical
theorems, not a claim of new theorem novelty, a full Lean formalization,
or a journal referee decision. The old near-decomposable permanent-bound
method remains a separate open question. Its scalar large-cost region is
not declared nonexistent; no actual boundary global maximizer can lie
there because the new Hall proof excludes every such maximizer.

## Durable research history

The cross-attack index is ../SEARCH_TREE.md. LINEAGE.md identifies the
predecessor checkpoint, the stronger acceptance question and its failure
signal. The original completion snapshot CP-49692413fac97be7 is preserved
unchanged. A corrected PDF parameter assumption is documented in
SOURCE_CORRECTION.md; the old wording remains visible as historical text.
No research result was committed or published externally.
