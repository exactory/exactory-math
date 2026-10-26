# Exact coefficients and the Gaussian obstruction

Source: node-000007, reserved move 1, reduce-and-translate,
change-the-ambient-space. Date: 2026-09-07.

Status: analytical findings awaiting independent review. The seed claim is
not proved. No mathematical program or numerical experiment was run.

## 1. Domain and candidate images

Fix a finite set D of distinct integer bases at least 3, a positive cutoff k,
and a finite set F of deleted labelled occurrences. Order the remaining
occurrences by numerical value and then base label as a_1,a_2,... . Write
S_m = sum_{i=1}^m a_i and T_m = a_m. Equal numerical values with different
labels remain different indices. The stream is infinite and locally finite.

The relation to encode is sum_i epsilon_i a_i = n, with each epsilon_i in
{0,1}. Three candidate descriptions were compared:

1. A finite polynomial and its exact integer coefficient.
2. An exponentially tilted lattice probability and its Fourier coefficient.
3. A normalized real sum or a limiting real distribution.

The third description, on its own, loses lattice support. That failure was
already recorded in earlier work and is not a new result. The first two
descriptions are exact and retain every power factor. They are used below.

## 2. Exact image and pull-back

Define

    P_m(z) = product_{i=1}^m (1+z^{a_i}),
    r_m(n) = [z^n] P_m(z).

Expansion chooses one of 1 and z^{a_i} from every labelled factor. It gives
a bijection between selections of the first m occurrences summing to n and
terms contributing to r_m(n). Thus r_m(n) is a nonnegative integer, and

    r_m(n)>0 if and only if n is a subset sum of a_1,...,a_m.

Complementing all choices also proves r_m(n)=r_m(S_m-n). Therefore the exact
image of the admitted claim is the following assertion, with no change of
quantifiers:

For every admissible D,k,F there is an integer L>=0 such that, for every
integer M>=1, some m>=M satisfies S_m>=2L and r_m(n)>0 for every integer
L<=n<=S_m-L.

Both implications follow from the displayed coefficient equivalence, one
integer and one prefix at a time. In particular L is not permitted to depend
on the selected prefix. This is a lossless reformulation, not a positivity
theorem or a reduction of the substantive difficulty.

For any real t let independent Bernoulli variables B_i have parameters

    p_i(t) = exp(-t a_i)/(1+exp(-t a_i)),
    X_m(t) = sum_i a_i B_i.

The probability of a specified selection summing to n is
exp(-t n)/P_m(exp(-t)). Consequently

    Prob(X_m(t)=n) = r_m(n) exp(-t n)/P_m(exp(-t)).

The normalizing factors are strictly positive. Tilting therefore preserves
support exactly, including at endpoints and with tied numerical values.
The Fourier inversion identity, with e(x)=exp(2 pi i x), is

    Prob(X_m(t)=n)
      = integral_0^1 e(-n theta)
          product_i (1-p_i(t)+p_i(t)e(a_i theta)) d theta.

This follows by multiplying the finite product, then using that the integral
of e(h theta) is 1 for integer h=0 and 0 for every other integer h. There is
no interchange of infinite limits in this identity.

## 3. A uniform obstruction to the ordinary Gaussian route

The following auxiliary assertion holds for every fixed nonempty finite D,
even without the gcd or reciprocal-mass assumptions and after arbitrary
fixed finite labelled deletion. For uniform independent Bernoulli choices,
the centered, variance-normalized variables cannot converge in distribution
to a standard normal variable along any sequence of prefixes tending to
infinity.

Here is a complete analytical argument. Put

    V_m = sum_{i=1}^m a_i^2,
    C_D = sum_{d in D} 1/(1-d^{-2}),
    Y_m = (X_m(0)-S_m/2)/(sqrt(V_m)/2).

For each base d, let b be its largest retained power in this prefix, if any.
Its retained squared powers sum to at most

    b^2 (1+d^{-2}+d^{-4}+...) = b^2/(1-d^{-2})
                               <= T_m^2/(1-d^{-2}).

Deletions can only decrease this sum. Summing over base labels proves

    T_m^2 <= V_m <= C_D T_m^2.

Write epsilon_i=2B_i-1, so that Y_m=sum_i a_i epsilon_i/sqrt(V_m).
The epsilon_i are independent symmetric signs. In the fourth-power
expansion, only terms with each index appearing an even number of times
have nonzero expectation. It follows that

    E[Y_m^4]
      = (sum_i a_i^4 + 6 sum_{i<j} a_i^2 a_j^2)/V_m^2
      = 3 - 2 sum_i a_i^4/V_m^2
      <= 3 - 2/C_D^2 < 3.

The bound is uniform in m because the largest occurrence contributes T_m^4
to the fourth-power sum. The fixed value of D is essential here.

To rule out convergence in distribution, moments must not be exchanged
without justification. For every real u, the elementary inequality
cosh(u)<=exp(u^2/2) follows by differentiating log cosh(u), using
|tanh(u)|<=|u|, and integrating from zero. Independence now gives

    E[exp(s Y_m)] <= exp(s^2/2),
    Prob(|Y_m|>x) <= 2 exp(-x^2/2),  x>0.

The second inequality follows from Markov's inequality with s=x and s=-x.
For R>0, integration of this tail yields

    E[|Y_m|^4 1_{|Y_m|>R}]
      <= 2 R^4 exp(-R^2/2)
         + 8 integral_R^infinity x^3 exp(-x^2/2) dx.

The right-hand side tends to zero as R tends to infinity, uniformly in m.
The fourth powers are uniformly integrable. Convergence in distribution to
a standard normal variable along any subsequence would therefore force the
fourth moments along that subsequence to converge to 3, contrary to the
uniform strict upper bound. This proves the auxiliary assertion.

This does not rule out non-Gaussian coefficient estimates, Gaussian-shaped
bounds on a limited window that do not imply normal convergence, or a
different tilted asymptotic law. It specifically prevents assuming an
ordinary centered Gaussian limit for these uniform prefix distributions.
It is not a counterexample to the seed or root claim.

## 4. Attempt to retain the power recursion

The exact factor structure is stronger than the moment information. In the
ring of formal integer power series, define the full undeleted factor for
one base by

    H_{d,k}(z) = product_{j>=k} (1+z^{d^j}).

Every coefficient involves only finitely many factors, so the product is
well-defined. Shifting the exponent index proves

    H_{d,k}(z) = (1+z^{d^k}) H_{d,k}(z^d).

For several bases the analogous multivariate series satisfies

    H((z_d)_{d in D})
      = product_{d in D}(1+z_d^{d^k})
          H((z_d^d)_{d in D}).

The univariate representation series is its diagonal substitution z_d=z,
not its multivariate diagonal coefficient. The transformed coordinates
z^d differ with d. Thus this identity does not close a scalar coefficient
recurrence for the diagonal substitution using a single common dilation.
Treating all z^d as one variable would change the actual powers.

For finite prefixes the completely valid scalar recurrence remains

    r_{m+1}(n) = r_m(n) + r_m(n-a_{m+1}),

where coefficients outside [0,S_m] are zero. If the old support contains
[L,S_m-L], its translate provides the adjacent or overlapping second
interval only when S_m-a_{m+1}>=2L-1. The accepted surplus theorem eventually
provides this inequality for a previously fixed L; it supplies no initial
represented interval. Writing this recurrence therefore encounters the
same missing seed, not a new proof of it.

Finite deletion may be removed from the factor notation only by explicitly
omitting the deleted factors. It is never legitimate to divide coefficient
inequalities by a positive polynomial or to infer positivity after deleting
a factor. None of the argument above does so.

## 5. Outcome and successor question

The exact coefficient and tilt translations have proved pull-backs. The
ordinary Gaussian engine has a specific obstruction, proved above for the
actual finite-base power streams. The remaining exact recurrence still
lacks a positivity mechanism, and the real-image alternative still lacks
the integer pull-back. No candidate in this move establishes a useful
coefficient lower bound. The entry's same-ceiling failure signal fires.

The main claim, every input including reciprocal equality, remains open.
No root progress percentage is assigned to a reformulation or to the
Gaussian obstruction. The auxiliary obstruction has not undergone a
statement-specific novelty search or independent result review and is not
presented as a novel standalone theorem.

A distinct next hypothesis is to separate strict reciprocal surplus from
equality. In the strict case a quantitative surplus margin may allow a
macroscopic represented band at a suitably aligned prefix to start permanent
coverage. That prospective statement needs its own exact scope, study,
admission, and proof. It is not established by this move. The equality case
must remain a separate open obligation rather than disappearing from the
original objective.

## References and audit boundary

The inherited problem and strategy studies are copied from
../preflight/pure-power-seed. Their source queries remain at
../preflight/pure-power-seed/sources/queries.md, relative to this attack
directory. The inspected primary completeness criteria are Bergelson and
Simmons, arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016, Section 2, and
Steve Fan, arXiv:2607.14071v1, Sections 1-2. Their missing hypotheses are
documented in those studies; neither is invoked as a theorem proving seed
coverage here. Sections 2-4 above are elementary analytical deductions,
with no numerical, computational, or formal-verification evidence claimed.
