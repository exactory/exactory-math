# Consolidation: quarter-mass completeness

The local attack closed at move1. This is a proof consolidation,
not independent acceptance.

## Marked steps and replacements

1. The cutoff at base eight could look arbitrary. It is exactly the
   last base whose reciprocal weight exceeds one eighth. Every later
   first-crossing increment automatically gives the strict nine-eighths
   bound. The proof separates only the exceptional earlier increments.
2. A gcd seed can contain large bases before augmentation adds small
   ones. The proof does not assume increasing order of the complete
   construction. At the first large seed choice, a nontrivial gcd
   divides every available small base. The five-row table then shows
   that an early mass crossing is impossible.
3. The minimum-three cases require the least eligible gcd-seed base,
   not an arbitrary coprime base. Explicit alternatives retain this
   rule and stop at the first crossing. In particular, a later eighth
   base is not charged after the crossing at seven.
4. Applying the predecessor theorem at its old threshold would be
   circular or insufficient. The proof instead cites the exact
   intermediate three-component criterion established in its accepted
   evidence. Its deficit, multiplier, finite-correction and support
   hypotheses are all checked before application.

No computational step needed replacement because none was used.

## Consolidated argument

Use the accepted minimum-preserving gcd seed and augment it.
Large last increments are at most one eighth. The small-base
divisibility and first-crossing arguments prove a correction core C
with mass in [1,9/8), for every minimum at least three. The complement
has minimum at least four. Its increasing first crossing gives B1
with mass in [1,9/8). At total mass at least13/4, the remaining B2
has mass greater than one. The accepted occurrence-preserving
three-component criterion proves completeness after every positive
cutoff and finite labelled deletion.

For minimum at least eight, retain the previously accepted3+2/m
threshold. The combined threshold is3+min{1/4,2/m}. The full detailed
proof and exact rational alternatives are in
../moves/001-quarter-mass-completeness.md relative to this file.

## Second route and true scope

No independent second proof was found or claimed. The high-mass
criterion is inherited, not new machinery. The finite selection
argument also proves the uniform minimum-preserving gcd-one core
bound below9/8 and the second-bin lemma for bases at least four.
These are parts of one quantitative application.

No optimality of9/8 or13/4 is claimed. The three-mass method still
does not cover the complete reciprocal-threshold-one objective.
All k,F, labels, and endpoint conditions are retained, but root
obligation1 and complementary obligation20 remain open.

