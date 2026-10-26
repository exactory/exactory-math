# Problem study: exact pure-power seed production

Date: 2026-09-07. Proposed target: obligation-000008.
Predecessor: node-000005, checkpoint-000009, accepted as acceptance-000002.
This is a pre-admission study, not a journal move or a proof.

## Queries and source access

The exact requests and stored response paths are recorded in sources/queries.md.
The first-tier problem sweep queried arXiv for pure powers and subset sums,
Semantic Scholar for pure-power subset-sum completeness, Crossref for the
BEGL title, zbMATH for complete sequences and powers, and the live Erdos 124
page. Semantic Scholar returned 429; it is not counted as a successful search.
The second-tier web sweep used three combinations of pure powers, subset sums,
completeness, Fourier, and local limit theorems. It located Fan's 2026 preprint.

## Sources worth reading

1. BEGL96, DOI 10.4064/aa-77-2-133-138. The introduction, main theorem, and
   final examples in the existing sources/begl1996.txt were inspected in this
   investigation. The full all-positive-cutoff statement is the conjecture;
   cutoff-dependent finite subsets of an infinite base set and k=1 examples
   do not supply the present fixed-D all-k seed lemma. Registry metadata and
   the zbMATH review were freshly checked.
2. The saved canonical sources/124.lean was read again. The intended root is
   Erdos124.erdos124.ne_zero: every natural k!=0, finite D, every base at least
   3, reciprocal mass at least one, collective gcd one, and eventual membership
   in the labelled sum of base-digit sets. Natural k!=0 is k>=1. Finset D gives
   distinct bases; different base coordinates remain separately usable. The
   live web page contains a denominator-index typo d_r in one display; the
   canonical statement and BEGL96 use the sum over d in D. Neither that typo
   nor the solved exponent-zero assertion replaces the immutable root.
3. Bergelson and Simmons, arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016.
   Section 2, including Main Theorem 2.1, the Cassels comparison, Lemmas 2.11
   and 2.12, and the complete proof of Main Theorem 2.1, was re-read in the
   saved text. The exact disjoint supplies are indispensable to that argument.
   It controls integer sums, unlike a real-image dimension assertion, but it
   does not establish the needed supplies at reciprocal mass one.
4. Steve Fan, Strongly complete sets and a conjecture of Erdos,
   arXiv:2607.14071v1 (2026-07-15), saved as sources/fan2026.html. Sections 1
   and 2, through the proof of Corollary 2.5, were inspected. Its finite-support
   refinement reduces four components to three, but still requires three
   disjoint infinite components with bounded prefix deficit, one having the
   required norm divergence. The rho-adic theorem has an additional uniform
   block-count hypothesis. Neither prerequisite has been established for all
   admissible pure-power streams. This is a new method source, not a claimed
   solution of Erdos 124 or independently verified root evidence.
5. J. W. S. Cassels, On the representation of integers as the sums of distinct
   summands taken from a fixed set, Acta Sci. Math. 21 (1960), 111-124,
   zbMATH document 3345481. The registry review and the statements in the
   primary papers above were inspected, not Cassels's full paper. Its circle
   method gives a neighbouring integer-coefficient positivity result under
   dyadic growth divided by log log tending to infinity and squared-norm
   divergence. A fixed finite union of power streams has bounded dyadic counts,
   so that theorem cannot simply be invoked for this problem.

The arXiv problem query's sole hit, arXiv:2603.17132v1, concerns Hilbert cubes
contained in the set of pure powers, not coverage by sums of prescribed power
streams. Only its abstract was inspected and it supplies no target theorem.

## Constraints on the planned attack

The accepted surplus theorem resolves the late propagation inequality once
one fixed endpoint loss and a compatible represented seed are available.
The seed itself retains the substantive coverage difficulty. The new record
will target that exact existing obligation, not a smaller computational proxy.

The previous early-seed repairs, normalized real-image projections, and generic
arithmetic-plus-surplus inference have recorded obstructions. The latter has
an accepted counterexample. None is restarted without a changed mechanism.

A finite generating polynomial retains every exponent and every labelled
factor, and its integer coefficients record exact numerical representation
counts. Circle-method coefficient estimates therefore provide a genuinely
integer-valued destination to examine. The planned study does not assert a
Gaussian local limit, useful Fourier decay, or positivity. Those are precisely
the applicability and proof obligations of the new attempt.

## Stop reason and novelty status

The fixed sweep of five first-tier sources plus the recorded focused web
queries is complete, including the stated access failure. No exact seed
theorem was located. This does not establish novelty. Any later surviving
theorem will require its own novelty check. No mathematical program was run,
and no new proof, counterexample, or formalization is claimed by this study.
