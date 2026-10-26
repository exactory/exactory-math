# Move 1: an exact lattice-aware real sumset image

Node: node-000003. Strategy: reduce-and-translate.
Entry: change-the-ambient-space. Reserved at controller revision 55.
Status: analytical reduction and method diagnostic, not a proof of the root.

## Relation and candidate maps

The original relation is n = sum_d a_d, with
A_d = {sum_{j in F} d^j : F is a finite subset of {k,k+1,...}}.
Each A_d contains zero. A numerical value contributed by different bases remains
a separate summand.

The study selected three maps for comparison:
1. Infinite fractional digit Cantor sets and their continuous sum. This is the
   already recorded Newhouse connection; a real interval alone has no integer
   pullback after deleting low digits.
2. Small real neighborhoods of the actual integer digit sets. The rounding
   estimate can preserve equality exactly, and compact truncations lie in the
   domain of the inspected thickness theorem. This is the selected map.
3. The product of representation polynomials. Its support preserves exact
   representability, but raw coefficients or choice counts must not be confused
   with positivity at every required exponent. No new coefficient theorem is
   asserted here.

## Exact image and both implications

Let r=|D|. Fix epsilon_d=3/(4r), so E=sum_d epsilon_d=3/4.
Define C_d=A_d+[-epsilon_d,epsilon_d] in the real line.

The translated target T is:
For every admissible D and k, the real set sum_d C_d contains a right half-line.

Minkowski addition of intervals gives the exact identity
sum_d C_d = (sum_d A_d)+[-3/4,3/4].
There is no closure operation or infinite choice in this identity. Every point
uses one finite digit selection for each of finitely many bases.

If the root holds with integer threshold N, every real x>=N lies within 1/2
of an integer n>=N. Then n belongs to sum_d A_d, and x belongs to sum_d C_d.
Thus the root implies T.

Conversely, suppose [X,infinity) is contained in sum_d C_d. For every integer
n>=ceil(X), choose z in sum_d A_d with |n-z|<=3/4. Both n and z are integers,
so n=z. This proves every required integer representation, hence T implies
the root. No labels are identified. The same fixed error allocation works
for every k.

This is an equivalent image, not a proof of T. The window 1/2<=E<1 is important:
E>=1/2 makes a cofinite integer set cover a real half-line after thickening;
E<1 makes integer membership in the thickening imply exact representation.

## Why the direct compact-prefix thickness test is unavailable

Fix integers M_d>=k, and replace A_d by its finite-prefix set A_{d,M_d}.
For this diagnostic allow any positive epsilon_d with E=sum epsilon_d<1,
not just the equal allocation above. Put
C_{d,M_d}=A_{d,M_d}+[-epsilon_d,epsilon_d].

The first two points of A_{d,M_d} are 0 and d^k, with none between them.
Since d^k>=3 and epsilon_d<1, the interval
G_d=(epsilon_d,d^k-epsilon_d) is a nonempty complementary gap.
Its length is d^k-2epsilon_d.

In any binary gap-removal derivation of C_{d,M_d}, when G_d is removed,
the left child is exactly [-epsilon_d,epsilon_d]. There are no other gaps
to its left, so its length is 2epsilon_d, regardless of the ordering of other
gap removals. Consequently that derivation has thickness at most
2epsilon_d/(d^k-2epsilon_d). Taking the supremum over derivations preserves
this upper bound. With gamma=tau/(1+tau), monotonicity gives
gamma(C_{d,M_d})<=2epsilon_d/d^k.

Therefore
sum_d gamma(C_{d,M_d}) <= 2E/min_d(d^k) < 2/3 < 1.

The bound holds for every cutoff depth vector. Astels's sufficient condition
sum gamma>=1 cannot apply directly to these full compact-prefix thickenings.
Increasing the prefix length does not repair that missing hypothesis.

This does not show that the sum has no intervals. It already contains small
intervals by construction. Nor does it exclude selected components, grouped
bases, another thickness notion, a different theorem, or a lattice-specific
argument. It excludes only the stated direct use of this sufficient condition.
Astels's whole-hull conditions need not be checked once its thickness condition
already fails.

## Source and novelty scope

The generalized Cantor definition allows finitely many complementary gaps.
The thickness definition is in Astels's 1999 Waterloo thesis, printed
pages 18-22, and the sufficient sumset theorem is Theorem 3.1.3, printed
pages 25-26: https://hdl.handle.net/10012/351.
The saved text at sources/astels-thesis.txt was reread at those passages.
The upper bound above uses the definition directly, not an unverified
thickness computation or a numerical experiment.

Supplementary searches on 2026-09-06 were:
- General web: "Cantor" "thickening" "integer" "thickness".
- General web: "finite" "digit sets" "thickness" "Astels".

The returned material included Yavicoli and Yu on omitted digits, a thickness
survey, and unrelated physical-fractal pages. No theorem from those hits is
imported; no exact theorem settling this image was located. The first-tier
problem and strategy searches are in this node's preserved studies.
This is a diagnostic within the admitted root translation, not a novel
standalone barrier claim or a controller-accepted theorem.

## Remaining work and plan handoff

T remains open and equivalent to the root. The pullback loses no quantitative
integer gap, but the available continuous theorem does not prove the selected
image. The next applicable plan step is the universal class reduction:
question 4 is no and question 5 is yes. The solution-map step is therefore
inapplicable. Question 7 is no, so no vocabulary-free engine import is scheduled.
Any narrower family result must receive its own exact branch record before
being treated as an independently developed result.
