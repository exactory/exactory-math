# Certified n=7 coverage and strict inequalities

Input: the fixed rational constants and polynomials in ../../COVERAGE_PROOF.md, plus the pinned source at ../../../dittert-completion-tree/study/external-proof/n6-n7. The source remains unchanged.

generate_manifest.py runs the primary exact n=7 checks and emits all closed leaf rectangles, binary paths, branch labels and coefficient minima. check_manifest.py imports neither the generator nor the pinned implementations. It rebuilds the polynomials from the rational formulas using SymPy, substitutes each leaf rectangle directly by the binomial theorem, and computes the Bernstein coefficients on that rectangle. It uses no de Casteljau subdivision. Agreement of these direct restrictions with the generator checks both exact arithmetic and the full branch interpretation.

The independent checker enumerates every pair of subsets of seven indices, selects exactly the cuts with |I|+|J|>7, and compares the complete cut-type map. It verifies a prefix-free full binary tree, exact area, absence of interior overlaps, and every endpoint/junction cell for each closed root square. The prefix and geometry arguments give continuous coverage; junction probes alone are not the proof. It rejects every single-leaf removal, every tree removal, every type removal, and a missing-sign predicate mutation.

Every finite inequality uses exact integers/rationals. Tolerance is zero; positivity is strict. The range is n=7, six ordinary margins, six mixed sign configurations, W on [0,3/20], and G>0 or (N>0 and F>0) on [0,3/20]^2 for (a,b)=(1,5),(2,4),(3,3). No value beyond n=7 is asserted. The trusted implementation base is CPython, fractions, SymPy exact polynomial arithmetic, and the reviewed short checker. This is an exact computer-assisted proof, not a kernel-checked real-matrix proof.

Run ./check.sh, sequentially at nice 15 with one numerical-library thread. The harness records status in result.json. manifest.json and independent-result.json preserve the full certificate and independently evaluated leaf bounds.
