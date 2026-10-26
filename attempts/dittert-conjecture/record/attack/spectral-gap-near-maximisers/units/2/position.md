# Position of unit 2

**On the path or off to the side.** On the path, and it is the cleanest form the problem took in
either attack. `H(n, K)` has no permanent, no spectrum and no simplex in it: it is a statement
about the cost of Sinkhorn scaling alone, and Theorem R is its special case
`K = 1 / (2 theta_n lambda_2(A))`.

**Prior best it improves.** Theorem R itself, as a reduction. Theorem R reduces Dittert's
conjecture at `n` to a spectral hypothesis; this unit reduces it to a scaling hypothesis and
gives the exact threshold `K_max(n)` the hypothesis must beat, so that `K < 1` already settles
every `n >= 7`, `K < 8` settles `n >= 10` and `K < 400` settles `n >= 15`. Against the truth,
the sibling attack's capacity samples give `K` about 0.5, so the hypothesis has a factor of two
of room at `n = 7`, the hardest open dimension.

**What it does not do, and why the unit says so.** The second half of the statement is the
refutation: `H(n, K)` with a `K` uniform over all fully indecomposable matrices is false, so the
reduction is not yet a proof of anything. The restriction that has to be added is precisely that
`A` is not nearly decomposable, which is what `per(A) <= gamma_n` has to supply, and supplying it
is the barrier unit 5 states.
