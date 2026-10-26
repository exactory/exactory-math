# The sharp constant of the quantitative van der Waerden inequality, measured

**Form.** Computational evidence. **Venue.** On the path: it fixed the constant of the claim.

## 1. Statement

For n = 3 to 9, the minimum over the Birkhoff polytope of
r(B) = (per(B)/gamma_n - 1) / ||B - J_n/n||_F^2, found by multi-start Nelder-Mead on the Sinkhorn
parametrisation B = Sinkhorn(exp(theta)) with a fixed seed, is at least 1/4, both globally and on
a grid of distances from the centre; the measured sharp constants are

    c*(n) = 0.250000, 0.333333, 0.418403, 0.460519, 0.486709, 0.497450   (n = 3, ..., 8),

increasing toward 1/2, against the local upper bound n/(2(n-1)) = 0.75 down to 0.571; and the
minimiser at n = 3, 4, 5 is (I + C_n)/2.

## 2. Method

deterministic/numerical-optimisation-run-1: a vectorised Ryser permanent; 60 down to 18 starts
per n at four entry spreads; an 8-point profile of the minimum of r at fixed distance t from the
centre, by a penalty on |  ||B - J/n||_F - t  |; and the explicit families T_n, (I + C_n)/2 and
blockdiag(J_k/k, J_{n-k}/(n-k)). check.py asserts every value found is at least 1/4 and every
global minimum is at most the local upper bound; result.json records the pass.

## 3. What the run shows

- The claim with 1/4 is tight at n = 3 and gets easier with n.
- (I + C_n)/2 is the extremal family at n = 3, 4, 5, matching hand computation: per = 2^(1-n)
  and ||(I + C_n)/2 - J_n/n||_F^2 = 2n(1/2 - 1/n)^2 + (n-2)/n give 1/4, 1/3, 0.418403 exactly. At
  n = 6 it gives 0.5125, above the minimum, so a different matrix takes over; at n = 7, 8 the
  minimiser has no zero entry.
- The distance profile has its minimum at intermediate distance: near the centre the ratio rises
  to the local value n/(2(n-1)), at the vertices to order n. A counterexample would have to live
  in a middle annulus, which the search covers.
- The constant n/(2(n-1)) fails globally from n = 3 on (study/qvdw-test.py: slack -5.6e-2 at
  n = 3 down to -1.9e-4 at n = 7).

## 4. What it is not

A multi-start local optimiser gives an upper bound on the true minimum, so c*(n) as reported is
an upper bound on the sharp constant and the absence of a value below 1/4 is evidence, not
proof. The claim is proved at n = 3 (unit 3) and with the constant 1/(2n) at every n (unit 2).

## 5. Ledger

Constructivity: the extremal family and the constant are measured, not proved.
