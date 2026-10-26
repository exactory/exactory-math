# Legacy n=6 checker exit regression

This check tests the actual final exit gate in the older n=6 integer Gram
checker. Negative slack must terminate unsuccessfully; zero and positive
slack must be accepted. The AST extraction executes the real suffix after
the final computed-slack assignment and omits only the expensive matrix
generation and multiplication. It does not replace the gate with a mock.

The initial run failed exactly the negative-slack test with SystemExit not
raised; see before-fix.txt. The production script now raises SystemExit
when slack<0 and prints EXACT PSD PASS only otherwise. The fresh run and
harness result certify this gate behavior, not a fresh n=6 matrix theorem.

The full original n=6 computation is preserved at
study/inherited-n6-exact-psd.log relative to this attack. It reports exact
diagonal-dominance slack 1691794048955 and EXACT PSD PASS. The existing
verified floating-point Cholesky route independently supports n=6 under its
documented IEEE-754/LAPACK backward-error assumptions. The integer residual
route uses FLINT and Python integers, even though candidate generation uses
floating-point estimates and fixed-width integers. The two roles must not
be confused. No large Gram computation was rerun here.
