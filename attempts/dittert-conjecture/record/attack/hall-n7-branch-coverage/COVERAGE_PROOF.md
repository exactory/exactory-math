# Complete dimension-seven boundary coverage

This is an independent reconstruction of the n=7 coverage argument attributed to Hongyuan Lu and reconstructed by Pedro Paulo Marques do Nascimento. It is not a claim of a new theorem. Pinned references and the exact statement are in problem.json and study/problem.md. The earlier audit's verdict is not used as a premise.

## Proposition and proof obligations

Let A be any nonnegative real 7 by 7 matrix with total sum 7 and at least one zero entry. Suppose A globally maximizes Phi(A), the row product plus the column product minus the permanent, on that simplex. Then the following exhaustive case analysis gives a contradiction. Its finite obligations are the six ordinary margins, six sign margins, the univariate W polynomial, and three simultaneous bivariate alternatives defined below. These are checked by the local deterministic certificate, independently of the previous PASS record.

Only the global-maximizer hypothesis supplies stationarity. The finite certificate does not claim stationarity for arbitrary near-maximizers. No matrix scaling fixed point, convergence basin, or choice of a small root is assumed.

Write g=7!/7^7=720/117649, R=product(r_i)=1-rho, C=product(c_j)=1-sigma, H=per(A)=g-delta. Comparing A to the uniform matrix and applying AM-GM gives

    0 <= rho, sigma; rho+sigma <= delta <= g; R,C >= 1-g > 0.

All line sums are therefore positive. These statements include delta=0 and delta=g. Subsequent deductions either exclude these endpoints or remain valid there.

## Localization before Hall division

For a nonempty proper row subset of size k with sum k+e, grouped AM-GM and the binary relative-entropy integral give, for e>0,

    2e^2/7 <= 7 D(k/7 || (k+e)/7)
             <= -log R <= rho/(1-delta).

The first inequality follows by bounding the denominator u(1-u) by 1/4 in the integral. For e<0 apply the same bound to the complementary subset, whose excess is -e. The column version uses sigma. Since

    1/47^2 > g/[14(1-g)],

every proper subset excess satisfies |e|<7/47<3/20. In particular every line sum exceeds 40/47>17/20. An empty subset has excess exactly zero. This reasoning never divides by a Hall scale.

For all I,J with p=|I|+|J|-7>0 define

    theta = min s_A(I,J)/p,    tau=1-theta.

There are finitely many cuts. The full cut gives theta<=1 and entry nonnegativity gives theta>=0. For any minimizing cut, let a=7-|I|, b=7-|J|, e=sum(I^c rows)-a, f=sum(J^c columns)-b, x=s_A(I^c,J^c). Inclusion-exclusion is exact:

    p tau = e+f-x <= e_+ + f_+ < 14/47 < 1.

Thus tau<1 and theta>0, including the putative theta=0 endpoint in the contradiction. Hall's capacitated max-flow criterion now supplies a doubly stochastic B with theta B<=A. For every minimizing cut,

    s_B(I,J)-s_B(I^c,J^c)=p,
    s_B(I,J)<=s_A(I,J)/theta=p.

Therefore B[I^c,J^c]=0 and B[I,J]=A[I,J]/theta entrywise. All original zeros also persist in B. Multiple minimizing cuts and nonunique B cause no problem: these conclusions hold for any such choice.

If tau=0, total mass forces A=B. A doubly stochastic matrix having a zero satisfies per(B)>=kappa=v_6 G(6)>g, by the rectangular-zero bound with a=b=1, contradicting H<=g. Hence 0<tau<1. A full minimizing cut has a=b=0 and forces tau=0, so it has already been excluded.

The permanent inputs used here follow from Gurvits capacity extraction: v_k=k!/k^k, G(k)=v_k/v_(k-1), and

    per(B) >= L(a,b)=v_(7-a) v_(7-b)/v_p

for any a by b zero block, a,b,p>=1. The degree bounds when extracting its b column variables are 7-a,6-a,...,p+1: each extracted variable uses a distinct row outside the zero block, and every remaining term has at most 7-a-h such row factors. Positive capacity and stability persist, so every extraction applies. This proves the bound without any hypothesis on the rest of the zero pattern.

## Exhaustive cut and sign partition

The nonnegative integers a,b obey a+b<=6. Transposition swaps (a,e) and (b,f). Row/column permutations just rename subsets. Thus the following list includes every ordered cut, up to that explicit symmetry:

| Class | Canonical sizes | Complete domain |
| --- | --- | --- |
| Full | (0,0) | tau=0, already impossible |
| Marginal | (0,b), 1<=b<=6 | every feasible e=0, f; tau>0 forces f>0 |
| Proper ordinary | (1,1),(1,2),(1,3),(1,4),(2,2),(2,3) | all signs; p>=2 |
| Proper single bridge, mixed | (1,5),(2,4),(3,3) | e<=0 or f<=0 |
| Proper single bridge, positive | same three pairs | e>0 and f>0 |

In the mixed class tau>0 and x>=0 rule out e<=0 and f<=0 simultaneously. Thus exactly one deviation is positive. The zero axes are included in the mixed cases. The corner e=f=0 is impossible for tau>0. The positive class maps into the full closed square [0,3/20]^2, so expanding its domain for certification does not omit an endpoint.

Every nonfull cut is marginal or proper by a,b>=0; a proper cut has p>=2 or p=1. These alternatives do not depend on individual zero counts or connectivity. In particular additional zeros, partial decomposability, vanishing minors, and absent core entries are not omitted classes. Hall positivity already applies to all of them, and the entropy proof below permits zeros.

## Ordinary and mixed exclusions

Retaining the maximum of u(1-u) on the localized positive-excess interval gives e_+^2 <= alpha_k rho/(1-delta), where

    alpha_k = 14(k/7+1/47)(1-k/7-1/47)  if k<=3,
              2k(7-k)/7                if k>=4,
    alpha_0=0.

For k<=3 the interval stays below 1/2; for k>=4 it stays above 1/2, so the respective upper and initial endpoints give these constants. Joint Cauchy-Schwarz yields

    tau^2 <= c delta/(1-delta),
    c=(alpha_a+alpha_b)/p^2.

For mixed p=1 cases use c=alpha_b when e<=0 and c=alpha_a when f<=0. This covers both sign orientations even when a=b. Since every alpha_k<7/2, the ordinary cases have tau<5/24. Mixed cases have tau<=e_++f_+<3/20.

On 0<=t<=T<1, the binomial remainder gives

    (1-t)^7 >= 1-7t+(21-35T)t^2.

Use (T,lambda)=(5/24,329/24) for ordinary cuts and (3/20,63/4) for mixed cuts. Since delta >= (1-g)tau^2/c, completing the square proves

    H-L(1-tau)^7 <= -M(L,c,lambda),
    M = L-g-49L^2/[4(lambda L+(1-g)/c)].

The six ordinary and six mixed M are strictly positive by exact rational checks. The denominator is positive because L,c,lambda,1-g are positive. The opposite inequality H>=L(1-tau)^7 follows entrywise, giving a contradiction for every tau in the intervals, including their endpoints. The minimization is over all real tau, so it selects no solution branch.

## Marginal cuts for all six complement sizes

Assume a=0. The p selected columns have total p theta and each has total at least theta, so every one has total theta and is saturated entrywise. Their averaged probability column in B is beta. Put s=sum(beta_i-1/7)^2 and D=1-sum beta_i/r_i. The normalized variation multiplying all selected columns by z and scaling the whole matrix back to total mass 7 is feasible on both sides of z=1. Every matching uses exactly p selected entries. Differentiation gives

    D=tau(C-H)/(theta R) >= (1-g)tau/theta >0.

The inequality uses C-H=Phi(A)-R>=1-g and R<=1. Every division is by a positive number.

Let y_i=1-1/r_i. Integration of r-1-log r, with r_i>17/20, gives

    rho >= (1-g)(17/20)^2 sum y_i^2/2 > sum y_i^2/3.

Strictness follows from D>0. Harmonic mean gives sum y_i<=0. Hence D<=sum(beta_i-1/7)y_i, D^2<=s sum y_i^2, and s>0. Therefore rho>D^2/(3s).

At least one saturated column has squared displacement >=s. Column entropy, valid for nonnegative doubly stochastic matrices by smoothing, gives H>=g theta^7 exp(s/2). Put q=theta^7. For every s>0, without a small-entropy assumption,

    rho+gq exp(s/2)-g
      > D^2/(3s)+gq s/2+g(q-1)
      >= D sqrt(2gq/3)+g(q-1).

This is positive if (2/3)(1-g)^2(1-tau)^5 > g[(1-(1-tau)^7)/tau]^2. Localization gives 0<tau<3/20. On this interval the bracket is positive and at most 7-21tau+35tau^2. The stronger sufficient polynomial

    W(t)=(2/3)(1-g)^2(1-t)^6-g(7-21t+35t^2)^2

has all degree-six Bernstein coefficients positive on [0,3/20]. Thus the left side above is positive, contradicting H<=g-rho. This argument covers all s>0 and all p=1,...,6. No s>=s_0 or s<=s_0 branch is selected. s=0 was explicitly ruled out before division.

## Positive single-bridge cuts

Use a<=b, a+b=6, m=7-a, ell=7-b, d=a, t=e+f. On the closed certificate square e,f in [0,3/20], m-e and ell-f are >=37/20, and 1-t>=7/10. Write

    Pa=(1+e/a)^a(1-e/m)^m, Pb=(1+f/b)^b(1-f/ell)^ell,
    ur=Pa-R>=0, uc=Pb-C>=0,
    K=g-2+Pa+Pb, u=delta-(2-Pa-Pb)>=ur+uc>=0, H=K-u,
    A0=L(a,b)(1-t)^7>0.

The core B[I,J] has mass one. Its row and column marginals xi,zeta are probability vectors; let s_I,s_J be their squared distances from the respective uniform distributions and s=s_I+s_J. The p=1 complementary-minor entropy argument gives per(B)>=L exp(s/2): every matching uses exactly one core entry and weighted AM-GM applies to those entries. Complementary minors on positive marginal support are positive by Birkhoff decomposition. Zero-exponent factors are justified by smoothing; an O(epsilon log epsilon) estimate handles vanishing minors. Thus arbitrary zero core entries are allowed.

For reciprocal variances V_I,V_J within the core row and column groups, conditional product energy gives V_I<=3ur and V_J<=3uc. Indeed, for z,mu>0,

    z/mu-1-log(z/mu) >= min(z,mu)^2(1/z-1/mu)^2/2.

All line sums and group means exceed 17/20. Sum within each group, cancel the linear terms, and use R,C>=1-g and (1-g)(17/20)^2/2>1/3. This applies whether individual line sums are above or below their group mean.

Let H_k be the permanent contribution using k entries in the opposite a by b block. Such a matching uses 1+k core entries, and 0<=k<=d. Since the core of A equals theta times the core of B, its normalized support-preserving variation gives exactly

    R(sum xi_i/r_i-1)+C(sum zeta_j/c_j-1)
       = [tau H+sum_(k>=1) kH_k]/(1-tau).

The variation scales existing entries, so it is feasible on both sides despite zeros. Every matching of B contributes to H_0, whence H_0>=theta^7 per(B)>=A0 exp(s/2). Now sum kH_k<=d(H-H_0) and tau=t-x<=t. The function ((tau+d)H-dH_0)/(1-tau) is increasing: its derivative numerator is (1+d)H-dH_0>=H>0. H>0 follows already from positive Hall domination and L>0. Thus the right side is at most [(t+d)(K-u)-dA0]/(1-t).

Harmonic mean and Cauchy-Schwarz bound the left side below by R(E-sqrt(s_I V_I))+C(F-sqrt(s_J V_J)), where E=e/(m-e), F=f/(ell-f). Define

    Bcal=Pa E+Pb F-[(t+d)K-dA0]/(1-t),
    c=(t+d)/(1-t)>=max(E,F).

Substitution yields Bcal+cu-Eur-Fuc <= R sqrt(s_I V_I)+C sqrt(s_J V_J). Since u>=ur+uc and R,C<=1, Bcal<=sqrt(3su). If Bcal>0, this gives su>=Bcal^2/3.

On the other hand H=K-u>=A0(1+s/2), so

    su <= 2u(K-A0-u)/A0 <= (K-A0)^2/(2A0).

There is no division by u or s; their zero endpoints are covered. K<A0 is already impossible by H>=A0 and H<=K. K need not be positive everywhere in the enlarged certificate square.

Define the positive denominator Delta=(m-e)(ell-f)(1-t) and rational polynomials

    G=A0-K, N=Delta Bcal,
    Fpoly=2A0 N^2-3(K-A0)^2 Delta^2.

At every point of the whole closed square the finite certificate proves

    G>0 OR (N>0 AND Fpoly>0).

The G alternative gives H>=A0>K>=H. In the second alternative N>0 gives Bcal>0 before squaring, and Fpoly>0 gives Bcal^2/3>(K-A0)^2/(2A0). The bounds on the same product su contradict this. No sign of N is inferred from its square.

## Complete certificate-tree interpretation

Each Bernstein basis function is nonnegative and all sum to one on its closed box. Strictly positive coefficients imply positivity even on its edges and corners. Each nonterminal node splits one coordinate interval at its midpoint and retains both closed children. At each accepted entropy leaf N and Fpoly are both positive over that same entire box. The root is the complete closed square. Finite induction on the tree proves the pointwise alternative everywhere, including subdivision junctions. The proof does not merely compare node counts.

The new manifest records every leaf's path and exact rectangle. Its independent checker rebuilds G,N,Fpoly from the displayed formulas and converts the directly restricted polynomial to Bernstein coefficients. It does not import the generating polynomial code or its de Casteljau routine. Independently enumerating all 128 by 128 subset masks gives all cuts with |I|+|J|>7 and maps each to the explicit table. Prefix closure requires each internal binary node to have both children; a direct rectangle partition check verifies unit area, no interior overlaps, and closed endpoint coverage. Mutation checks must reject a removed leaf and an omitted cut type. Thus accepted aggregate counts are a consequence of the complete certificate, not its input.

## Conclusion and verification boundary

Every hypothesized boundary global maximizer enters one of the cases and yields a strict contradiction. No matrix remains outside the argument due to an omitted scale root, sign case, support pattern, or subdivision branch. The local exact checks passed on 2026-09-05: all 6,476 subset-pair cuts, 28 ordered size types, 62 closed leaves, six ordinary margins, six sign margins, and W were checked. The three trees have (nodes, direct leaves, entropy leaves, depth) equal to (39,10,10,8), (35,9,9,6), and (47,11,13,8). All 94 omission mutations were rejected. See deterministic/certified-special-case-check-1/result.json and independent-result.json. Together with the analytic reductions this establishes the stated proposition.

The common capacity theorem is an explicitly cited mathematical input, not a reviewer verdict. The finite certificate uses exact arithmetic but is not a Lean formalization of the real-matrix theorem. Independent final review of this new proof package remains a separate stage.
