# Position of unit 1

**On the path or off to the side.** On the path. Theorem R closes Dittert's conjecture at `n`
once the spectral gap of a hypothetical counterexample clears `c_n`, and the record established
at move 1 that the binding half of `c_n` is the non-negativity condition (N) of Theorem R's
Lemma 2, by a factor of 12.1 at `n = 7` rising to 6555 at `n = 20`. This lemma attacks exactly
that half.

**Prior best it improves.** Theorem R's own Lemma 3(c), which bounds the potentials by
`sqrt(2) |(u; v)|_2 / (theta_n lambda_2)`. That bound carries `1 / lambda_2`, so it converts a
margin of size `sqrt(delta)` into a condition on `lambda_2` that scales as `sqrt(delta)`. The
resistance bound carries no `1 / lambda_2` at all: it is linear in `delta` and entrywise. Where
both apply it is up to 60 times smaller, measured over 24 random cases in
`study/reff-bound-check.py`.

**What it does not do, and why the unit says so.** It removes condition (N) only at entries with
`a_ij >= Phi`. Two statements would extend it to every entry, and move 4 refuted both on the
natural relaxation: the smallest positive entry reaches 3.6e-28 at `n = 6` while the permanent
stays at 1.05 `gamma_n`, and truncating the entries below `Phi` moves the margins by at least
`n^1.5 sqrt(2)` times the margin it repairs. The unit states the lemma and both refutations
together because the refutations are what tell the next reader not to try them.
