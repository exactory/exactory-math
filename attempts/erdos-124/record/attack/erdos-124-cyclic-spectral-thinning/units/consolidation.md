# Consolidation of the cyclic spectral-thinning proof

Date: 2026-09-08. Node: node-000019. Closing move: 1.
Frozen result: checkpoint-000025, evidence manifest
73f908145b8601b3f44dc351f0ac5330620a8e315aefc7e4eaba6484c336cb1e.
This record is a local consolidation, not proof acceptance.

## Statement and rewritten argument

The exact claim remains the statement in problem.json and in Section 1 of
moves/001-cyclic-spectral-thinning.md. That complete proof is the rewritten
argument. It is self-contained for the recursive and spectral estimates;
the explicitly cited Griesmer sumset theorem remains a literature input.

The proof has the following dependency order. Section 2 first proves the
extension invariant for finite prefixes and the actual infinite complement.
Section 3 supplies the smallest nonempty seed and bounds successive
selected exponents. Section 4 excludes every nontrivial character.
Section 5 takes sequential dominated limits for all positive finite Radon
spectral measures before a cluster point. Section 6 applies the exact
sumset theorem to disjoint label supplies. Section 7 proves termination
of the proposed witness procedure without executing it.

## Marked steps and standard replacements

1. The least-power threshold could appear arbitrary. Section 2 identifies
its exact role: the latest selected base has complementary reciprocal mass
at least one, and its earlier powers pay for the cutoff, finite deletion
and previous removed weight. The strict prefix formula, rather than a
total support estimate, proves the fixed gap. A single global weight
subtraction does not retain that estimate for infinite Q and was not used.

2. Passing from prefix deficits to subset-sum gaps could obscure ties.
Section 2.2 replaces an informal mesh assertion with the elementary
two-copy induction, stated for labelled multiplicities and with the
first-prefix and nonnegative endpoint cases included. The constant g
is unchanged.

3. Sparse selection could leave a nontrivial character undetected.
Section 3 uses minimality of the eligible power to bound the growth ratio;
Section 4 then uses the nearest-integer recurrence and collective gcd.
This replaces an unquantified equidistribution assertion. It treats
rational and irrational characters together and gives no uniform decay rate.

4. Character annihilation alone would not justify a full FS-mean.
Section 5 uses the standard spectral integral and sequential dominated
convergence before compactness. Griesmer Lemma 9.5(ii) supplies the
precise interface. The mean is not asserted invariant on every bounded
function.

5. Thickness could be confused with eventual completeness.
Section 6 proves only arbitrarily long intervals using the full-mean
sumset theorem. Section 7 explicitly retains the stronger root claim,
half-mass complement and bridge. The witness procedure is justified by
finite support, not a runtime bound or a finite computation.

## Second-route check

The elementary gap induction replaces the relevant mesh step completely.
It does not replace the full Fourier-Stieltjes sumset theorem. An
elementary disjoint finite-switch argument would need the missing support
charge that ended the earlier carry-seed attempt. No independent second
route to the thickness conclusion has been established. This unit is not
labelled a second proof.

## Generality actually established

The proof keeps the exact admitted finite-base hypotheses, every positive
cutoff and every finite labelled deletion. The active-base set could be
any nonempty gcd-one subset of the removable core; the canonical claim
uses the whole core. The sufficient condition
sigma(D)>=1+1/(min D-1) makes the whole D removable and gives the stated
immediate thickness consequence. These are interpretations of the
same argument, not separately counted results or new research moves.
No complete classification below that criterion is supplied.

## Verification and costs

No mathematical executable or formal check was used. The closing move has
an empty ledger, as permitted for a proof that pays no remaining local
obligation. The native full-proof label concerns only this exact node.
Independent frozen-result review and local draft evaluation remain pending.
