# Linear and asymptotic spectral editing bounds

This is the analytical proof candidate for the exact claim of node-000002. Independent acceptance is pending. It does not prove the original coefficient-three claim or assert historical priority.

## Statement and dependency

Let G be any finite simple triangle-free graph, let m=e(G), let lambda be its adjacency spectral radius (zero for the empty vertex set), and put xi=m-lambda^2. For disjoint subsets A,B of V(G), the graph K_{A,B} has every edge between A and B and no other edge on V(G); empty parts are allowed. Set

    D(G) = min_{A cap B = empty} |E(G) symmetric-difference E(K_{A,B})|.

Then

    D(G) <= 15 xi.

When lambda>0, the stronger small-deficit estimate is

    D(G) <= 3 xi + 18 sqrt(6) xi^(3/2)/lambda.

Consequently, for every sequence of such graphs with xi>0 and xi/m tending to zero, limsup D(G)/xi<=3. Also D(C5)=3 and e(C5)-lambda(C5)^2=1, so any universal coefficient in D(G)<=C xi must be at least three.

The non-elementary input is Lemma 4.3 of Yongtao Li, Lele Liu and Bo Ning, *The spectral Erdos book theorem: sharp bounds and stability*, arXiv:2609.20225v2. For every bipartite graph H it gives

    D(H) <= 3(e(H)-lambda(H)^2).

The pinned full text and its proof are in study/problem.md. The same source states the classical Nosal inequality lambda(G)^2<=e(G) for triangle-free graphs. Thus xi>=0. The remaining ingredients are real symmetric matrix spectral theory, the Rayleigh principle, trace identities and explicit finite graph counting. No numerical eigenvalue or exploratory computation is used.

## A sign cut preserving the least eigenvalue

If m=0, take an empty part. Then D(G)=xi=0, and the first assertion follows. This includes the empty vertex set. Conversely, if lambda=0, the real adjacency matrix has all eigenvalues zero and trace(A^2)=2m=0, so this case is already covered.

Assume m>0. Write the adjacency eigenvalues as lambda=lambda_1>=...>=lambda_n=-mu. Then lambda>0. Since trace(A)=0, at least one eigenvalue is negative, so mu>0. Nonnegativity of A and the Perron spectral-radius theorem give mu<=lambda, without requiring connectivity.

Choose a real unit eigenvector y for -mu. Define F on V(G) by retaining exactly those edges whose endpoints have opposite nonzero signs in y. It is bipartite, with the zero-coordinate vertices isolated. Let b=m-e(F). Let P be the sum of y_u y_v over same-sign edges, and Q the sum of |y_u y_v| over opposite-sign edges, counting each unordered edge once. Thus P>=0. Edges incident to a zero coordinate contribute zero. We have

    -mu = y^T A(G)y = 2P-2Q,
    |y|^T A(F)|y| = 2Q = mu+2P >= mu.

Since |y| is still a unit vector, lambda(F)>=mu. For any complete-bipartite target, the triangle inequality for symmetric difference bounds its distance from G by b plus its distance from F. Minimizing over targets and applying the bipartite lemma gives

    D(G) <= b + D(F)
         <= b + 3(e(F)-lambda(F)^2)
         <= 3(m-mu^2)-2b
         <= 3(m-mu^2).                                      (1)

All graphs and targets here retain the same vertex set. Disconnected graphs and isolates therefore need no component reduction.

## A uniform linear coefficient

Triangle-freeness gives trace(A^3)=0, because a simple graph's closed walks of length three correspond to its triangles. Hence the positive and negative eigenvalue cubes balance. Using trace(A^2)=2m,

    lambda^3 <= sum_{lambda_i<0} |lambda_i|^3
             <= mu sum_{lambda_i<0} lambda_i^2
             <= mu(2m-lambda^2).

The last inequality only discards positive squared eigenvalues other than the chosen lambda. Its denominator is positive, so

    mu >= lambda^3/(2m-lambda^2).

Set r=lambda^2/m in (0,1]. Squaring and rearranging gives

    m-mu^2 <= m[1-r^3/(2-r)^2]
            = (m-lambda^2)(r^2+4)/(2-r)^2.                  (2)

The identity follows from (2-r)^2-r^3=(1-r)(r^2+4), and is valid also at r=1. On 0<=r<=1,

    5(2-r)^2-(r^2+4) = 4(r-1)(r-4) >= 0.

Thus (2) is at most 5xi. Combining it with (1) proves D(G)<=15xi. In particular, if xi=0, these inequalities give m-mu^2=0 and D(G)=0, so no division by zero deficit or separate equality classification was used.

## A quantitative small-deficit estimate

Put delta=lambda^2-mu^2>=0. Equation (2) and its coefficient-five bound give

    xi+delta=m-mu^2<=5xi, hence delta<=4xi.

Remove one occurrence of lambda and one occurrence of -mu from the spectrum. They are distinct eigenvalues because both magnitudes are positive. The sum of the squares of the remaining eigenvalues is

    S=2m-lambda^2-mu^2=2xi+delta<=6xi.

The trace-cube identity and the elementary inequality sum |a_i|^3 <= (sum a_i^2)^(3/2) imply

    lambda^3-mu^3 = -sum_remaining lambda_i^3
                 <= sum_remaining |lambda_i|^3
                 <= S^(3/2).

For completeness, the norm inequality follows by bounding each |a_i| by sqrt(S) and summing |a_i|^3<=sqrt(S) a_i^2. It also holds for an empty remainder or S=0. Further,

    (lambda^3-mu^3)-lambda(lambda^2-mu^2)
        = mu^2(lambda-mu) >= 0.

Since lambda>0, it follows that delta <= (6xi)^(3/2)/lambda. Substituting in (1) proves

    D(G) <= 3(xi+delta)
         <= 3xi + 18 sqrt(6) xi^(3/2)/lambda.

Along the sequence in the statement, dividing by xi>0 gives an excess above three bounded by

    18 sqrt(6) sqrt(xi)/lambda
      = 18 sqrt(6) sqrt((xi/m)/(1-xi/m)),

which tends to zero. This proves the asserted limsup. No lower bound in this asymptotic regime is claimed.

## The exact five-cycle witness

The five-cycle is 2-regular. Its constant vector has eigenvalue 2, and the maximum-degree bound gives spectral radius at most 2. Thus lambda(C5)=2, m=5 and xi=1.

For any disjoint A,B in its vertex set, the edit cost equals

    5+|A||B|-2e(A,B).

A two-edge path gives a target K_{1,2} already contained in C5, so D(C5)<=3. For the lower bound, consider the gain 2e(A,B)-|A||B|. Empty parts have gain zero. Interchanging parts if needed, the only positive part-size pairs are

| Part sizes (a,b) | Upper bound on e(A,B) | Upper bound on gain |
|---|---:|---:|
| (1,1) | 1 | 1 |
| (1,2) | 2 | 2 |
| (1,3) | 2 | 1 |
| (1,4) | 2 | 0 |
| (2,2) | 3 | 2 |
| (2,3) | 4 | 2 |

The first four bounds use maximum degree two. Four edges between two pairs would form a four-cycle, absent from C5, proving the fifth bound. For the last pair, a cut cannot contain all edges of an odd cycle, so it contains at most four. These cases exhaust |A|+|B|<=5. Every gain is at most two, so D(C5)>=5-2=3. Therefore D(C5)/xi=3, proving the lower bound on any universal coefficient.

## Loss ledger and remaining obligation

The sign cut replaces the earlier square-root perturbation estimate. Its main loss is the discrepancy delta between the squared largest and least eigenvalue magnitudes. The uniform trace estimate bounds delta by 4xi; the remaining-spectrum estimate improves this to (6xi)^(3/2)/lambda. Discarding b in (1) and possible slack in the bipartite editing theorem are further losses. This proof establishes the full standalone claim but leaves the exact universal inequality D(G)<=3xi unresolved. The C5 witness establishes a global lower bound of three, not asymptotic optimality when xi/m tends to zero.
