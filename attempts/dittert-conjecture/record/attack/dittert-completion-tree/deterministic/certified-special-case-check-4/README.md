# Kernel check of the scalar interface

Blueprint: positive_quadratic proves that c>0 and 4ca-b^2>0 imply
c*u^2+b*u+a>0 for every real u. The exclusion theorem combines this
with permanent>=floor-slope*u, deficit>=curvature*u^2 and
permanent+deficit=gamma to derive False. It covers every real u;
the old least-fixed-point inference is absent.

Only this scalar interface is formalized. The matrix-to-scalar reductions
and dimension-specific inequalities remain the independently audited
computer-assisted proof. This file has no sorry or native evaluation.

The checker invokes the pinned Lean kernel directly against already built
Mathlib libraries from the original local attack, with one worker. It checks
both printed axiom lists exactly. It is recorded as a certificate check,
not as a standalone Lake build, because it deliberately reuses the installed
compiled libraries and does not rebuild the large earlier project. The
full Dittert theorem is not claimed to be formalized by this interface.

The first compilation failed because pos_of_mul_pos_left extracts the
left factor, whereas the proof needed the right factor. Replacing it by
pos_of_mul_pos_right repairs a theorem-application slip, not a mathematical
gap. The failure was not suppressed; successful recompilation and the exact
axiom-list tests are required by check.sh.
