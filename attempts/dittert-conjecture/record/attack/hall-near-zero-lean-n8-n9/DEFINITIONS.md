# Exact polynomial

For n in {8,9}, define gamma=n!/n^n, kappa=(n-2)!*((n-2)/(n-1)^2)^(n-2), L=kappa*(1+1/(2*n^2)), E(u)=1-(2-gamma)*u, H(u)=(1-gamma)*u, T(u)=E(u)-H(u)/(n-1), V(u)=1-u, F(u)=V(u)*(1+u/(n-1))^(n-1), and

`p_n(u)=(2-gamma+L*V(u)^n-F(u))*E(u)^n-(E(u)+H(u))*T(u)^(n-1)`.

All divisions are real-field divisions. The target intervals are [0,1/400] for n=8 and [0,1/500] for n=9. Strict positivity includes both endpoints. This is exactly near_poly in the inherited independent checker. Dividing E powers in near_literal yields the same formula where E is nonzero. This theorem directly concerns the polynomial and requires no division by E.
