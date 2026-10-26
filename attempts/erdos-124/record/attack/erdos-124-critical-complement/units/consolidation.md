# Consolidation of the critical-complement proof

Node: node-000022, closing move1. This is the unmetered closing entry
consolidate-the-proof, not another research move or an accepted result.
The complete quantitative proof is moves/001-critical-complement.md.

## Exact theorem

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there are an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, and V=D minus R has min V>=4, sigma(V)=1, contains multiplicatively independent integers a,b, and satisfies H_V(x)>x for every real x>1, where p_d(x) is the least nonnegative integer power of d at least x and H_V(x)=sum_{d in V}(p_d(x)-1)/(d-1), every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each labelled pair used at most once and coincident numerical values retained separately.

## Steps inspected and replacements

The difficult interfaces are the shrinking phase tolerance, three-scale
deletion estimate, signed orientation of positive return times, and
computability of one Q_0 independent of the later state.

A qualitative compact-return argument from CP27 does not control a tolerance
depending on the selected height. It is replaced in move1 Section6 by classical
simultaneous Dirichlet approximation, the selected two-logarithm lower bound,
and a difference of two positive returns whose order is proved. Unsigned
Dirichlet alone is not used as the sign assertion.

The critical equality removes CP27's positive mass delta. Move1 Section2
replaces it with a quantitative normalized H_V margin: the external logarithm
bound separates two independent next powers, and the explicit H_V hypothesis
provides the exact bounded-scale integer margin. These estimates have
different roles; neither is assumed to imply the other.

The scale boundary Z(q)=(1+log q)^(2A+2) joins the normalized estimate to
the unscaled remote tail. The original dyadic epsilon decays faster than
every inverse power of log log q but slower than every inverse power of
log q. This is precisely what allows both preservation and signed recurrence.
The fixed Q_0 is selected using eventually monotone explicit inequalities,
not by an unrecorded uniformity assumption.

No executed computation requires replacement. The general H_V test has an
impractical bound, so the supplied small input is certified separately by
hand. Its all-cutoff conclusion, not its known cutoff-one special case,
demonstrates additional coverage.

## Rewritten proof with the interfaces visible

Fix D,R,V,k,F as in the theorem. Keep the original V supply P_V and set
C=sum_d d^k/(d-1)+value(F_V), g=ceil(C), M=max V.
All sums count labels separately. Only one V label q is removed for each
signed unit; W is the sum of every earlier removed value.

First, r mutually disjoint signed-unit pairs positively represent an
interval [H,H+r]. A disjoint reserve meeting every g-integer nonnegative
interval combines with r=g-1 pairs to represent every n>=H+g-1.
This is the amplification law before a seed is asserted.

Next fix an independent pair a,b in V. For z>1 the next powers p_a(z),
p_b(z) have positive exponents and are unequal. Gouillon2006,
DOI10.5802/jtnb.537, Section2 and Corollary2.3, with rational integer
algebraic bases and the exact real logarithms, implies for computable
A and lambda depending only on V

    H_V(z)-z >= lambda z/(1+log z)^A-1.

The permitted explicit choices are A=40000M^2 and
lambda=[(M-1)4^(1000A)(2M+3)^A]^-1, as derived in the complete proof.
For every z>1, H_V(z)=H_V(ceil z), and H_V at an integer is an integer.
The strict hypothesis therefore also gives H_V(z)-z>=1.
These two bounds yield a positive computable kappa with

    H_V(z)-z >= kappa z/(1+log z)^A  for every z>1.       (a)

Put L=2A+2, Z(q)=(1+log q)^L and
nu(q)=kappa/[1+L log(1+log q)]^A.
The exact dyadic tolerance satisfies
epsilon(q)<=2 exp(-sqrt((log 2)log(1+log q))).
Choose the single computable Q_0(V) from the monotone inequalities in
move1 Section3, so for q>Q_0

    (M+2)epsilon(q)<nu(q)/2,
    sqrt(q)nu(q)>2,
    kappa(1+log q)^(L-A)/(L+1)^A>2.

Also Q_0>=16M^2 and log Q_0>=A. This choice precedes all unit supports.

Consider any finite correction list satisfying the exact rule(E).
At any x>0 with a selected value at most x, use its latest value q and
the entire earlier W. Growth gives C+W+1<sqrt(q).
All selected anchors are above d^k, and all their preceding powers
are below q.

For q<=x<=(1+epsilon)q, take those preceding powers and the promised
additional anchor strictly below q. This collection excludes the
current correction. After paying F_V and W its weight is at least
(2-2epsilon)q-C-W>=x-C. This directly includes the endpoint x=q.

For (1+epsilon)q<x<=qZ(q), write z=x/[(1+epsilon)q].
Each next original power at x is at least (1-epsilon)q p_d(z).
Since H_V(z)+z+1<=(|V|+2)z<=(M+2)z, paying the current q and
all W leaves at least

    x-C+q z[nu(q)-(M+2)epsilon]-W >= x-C.

For x>=qZ(q), the unscaled estimate(a), monotonicity of
x/(1+log x)^A in this range and the last Q_0 inequality give surplus
above 2q, paying W+q. If no selection is at most x, the original
geometric lower bound gives x-C directly. Therefore every finite
allowed correction list retains the exact assertion(P),

    strict prefix weight at x >= x-C  for every x>0.

Ordering the retained labels gives u_i-sum_{j<i}u_j<=C<=g.
Inductively the subset sums of each finite prefix have gaps at most g:
adjoining u_i forms two translates; their intervening gap, if any,
has the displayed bound. The total weight tends to infinity, so the
same g works for the whole reserve.

It remains to produce an eligible correction. The radix mass forces
B=2 or3 because B/(B-1)^2<=4/9 for B>=4. The gcd condition supplies
the prescribed least c in V coprime to B. Such c has an independent
mate e, since dependence with both a and b would make them dependent.

Fix any positive period t. Put theta_d=t log(c)/log(d).
The same quantitative corollary gives

    ||r theta_e|| >= delta_t r^(-A),
    delta_t=[M4^(1000A)(2t+2)^A]^-1,  r>=1.

Classical simultaneous Dirichlet approximation, in the form stated
in Fishman-Simmons2017, DOI10.1007/s00605-016-0983-0, Section1,
gives a return r<=Q^v with errors eta_d of magnitude below 1/Q.
The lower bound forces r>(delta_t Q)^(1/A).
If eta_e>0, it already has the needed lower-anchor sign.

If eta_e<0, take P=(2^(A+1)/delta_t)r^A and obtain another return
s<=P^v with error below 1/P. The denominator lower bound forces s>2r
and 1/P<|eta_e|/2. The positive time u=s-r has a strictly positive
e error, and all its errors are below 2/Q. In either case u tends
to infinity and u<=K_t^v Q^(Av^2), giving polynomially small errors
in u. The c error is exactly zero, so n_c=tu.

For q=c^(tu), the exact epsilon(q) is bounded below by
exp(-sqrt((log 2)log((2tM+2)(u+1)))). This decreases more slowly
than those polynomial errors. At sufficiently late selected times,
|log(d^(n_d)/q)|<=epsilon(q)/2. The relative error is therefore at
most epsilon(q), and the e anchor is strictly below q. All exponents
can be at least k, q above any prescribed T, and epsilon below
1/(100M). This proves the exact(R), not full-torus density.

For the current finite forbidden R supports choose a higher cutoff
K_R and a common aligned modulus m=B^(L_R).
The normalized fresh R weights B^(aj) satisfy w_i<=2T_{i-1}+1
by sigma(R)>=1/2, so signed sums fill every integer.
Thus the original fresh labels represent every multiple of m.
Take t to be the least multiplicative period of c modulo m.
Assertion(R) supplies the next(E) correction q congruent to1 modulo m,
above the full growth threshold and all forbidden V values.

Represent 1-q on fresh R supports and add the one positive q.
Both signs avoid all previous supports. Update W and the forbidden
R supports, without changing the V cutoff, C,g or Q_0.
This extends every finite state, including the first seed.
Repeat g-1 times and apply the initial amplification law.
The resulting threshold N=max(1,H+g-1) proves the full theorem.

All choices have terminating search descriptions, not executed
programs or useful complexity bounds. The exact small example and
complete finite H_V test are in move1 Section9. They are part of
this theorem's significance check, not separate checkpoints.

## Second-route check and generality

No independent second proof of the critical-complement theorem has
been established. The qualitative CP27 recurrence is insufficient
at a height-dependent tolerance. A spectral thinning result does
not supply the same disjoint interval and reserve construction.
Neither is presented as a second proof or an omitted obligation.

The preservation argument actually allows any correction base in V
in each step, independent of modular conditions, as assertion(P)
requires. The recurrence argument only needs an independent mate
of the chosen c; sigma and H_V do not enter that subargument.
These observations explain the proof's interfaces. They are not
separately proposed or accepted generalizations.

The theorem still requires the exact common-radix half-mass and
critical-complement hypotheses. No automatic strict H_V statement,
arbitrary mixed-base half-mass signed unit or root completeness
conclusion has been proved. The cost ledger is empty, and the
candidate awaits independent result review and acceptance.
