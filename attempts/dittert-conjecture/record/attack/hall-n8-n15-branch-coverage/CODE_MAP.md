# Mathematical cases and executable coverage

The inspected primary source is
../dittert-completion-tree/study/external-proof/unified/verify_unified_reductions.py,
SHA256 aa8fdb21969cb13f0124e4c5bec5c016f39e49d8aea09692f347c6271a21e010.
Relevant source functions were read directly, rather than inferred from logs.

| Source code branch | Mathematical reason | Independent coverage |
| --- | --- | --- |
| cut_rows omits a=b=0 | lambda=1 forces A=B; strict van der Waerden boundary gap | expected_types includes all 8 full cuts; PROOF section 2 |
| cut_rows omits b=0 except a=n-1 | Any minimizing marginal average equals the smallest line | Every nonzero marginal pair in both orientations maps to (n-1,0) |
| cut_rows restricts b<=a | Transposition swaps a,b and preserves C,nu,M | Every ordered proper pair is checked; scalar margins are compared after transpose |
| verify_quadratic_remainder_family skips n<8 | This child covers only n=8,...,15 | Independent main range is exactly range(8,16) |
| verify_cut_table permits two negative rows | Exactly (8,7,0),(9,8,0) need stronger deficits | Independent observed residue must equal that exact set |
| n8 support loop has z=1,...,6 | z=0,n-1,n impossible by stationarity/structure | Full support validator plus analytic proof |
| n9 support loop has only z=7 | U_z increases with z; permanent floor L9 is constant | Full z=1,...,7 domain is validated; compression forbidden at n=8 |
| finite n<=10 uses u<=ubar | Globally proved delta>=C u² and delta<=gamma | Positive ceil-rounded rational enclosure checked on every case |
| n>=11 uses Bernoulli/completed square | Positivity holds for all u in [0,1] | Every n=11,...,15 ordered cut is directly verified |
| n8,n9 finite marginal intervals | D(u) is increasing on every feasible parameter; D(v)>gamma | Explicit denominator/domain checks and tail endpoint inequalities |
| near-zero Sturm endpoints | Source excludes roots and checks both endpoints | Direct-Bernstein coefficients are positive on the whole closed interval |
| support Bernstein intervals | Nonnegative partition of unity includes both endpoints | Independent basis multiplication and degree elevation, all coefficients positive |

The independent checker has no source imports. Its only compressed support
certificate relies on the written monotonicity proof, not a failed loop
case being omitted. Four rational-point polynomial comparisons are
implementation regressions, not the mathematical completeness argument.

Fresh run: deterministic/certified-witness-chain-1/result.json is pass.
Both exact implementations cover the same mathematical finite obligations.
The arithmetic itself found no omitted feasible Hall branch. The separate
old audit error about the Pula--Song--Wanless parameter domain is corrected
in PROOF section 1 and the parent's erratum.

The finite range is explicit. No infinite-dimensional result, no extrapolation
from a tested prefix, and no theorem for n>15 is used in this child.

