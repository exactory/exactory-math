# Position of unit 3

**On the path or off to the side.** Off to the side, deliberately, and that is its value. The
attack asked whether the permanent side of the argument had any room left in it. This unit
answers no, and answers it exactly rather than by estimate.

**Prior best it improves.** The van der Waerden inequality `per(B) >= gamma_n` is tight only at
`J_n/n`, and the natural repair is a quadratic strengthening
`per(B) >= gamma_n (1 + c ||B - J_n/n||_F^2)`. This unit computes the largest `c` that can
possibly hold, `n / (2(n-1))`, in closed form, and then shows that with that constant the
strengthening predicts `per(T_n) / gamma_n - 1` at the Knopp-Sinkhorn extremal to leading order:
1.62e-2 against the true 1.34e-2 at `n = 7`. So the strengthening reproduces Knopp-Sinkhorn and
adds nothing.

**What follows for the attack.** The permanent side is already as strong as it can be, both at
the interior extremal (this exact Hessian) and at the boundary (Knopp-Sinkhorn). Whatever is
missing is on the capacity side, which is what unit 5 states as the barrier.
