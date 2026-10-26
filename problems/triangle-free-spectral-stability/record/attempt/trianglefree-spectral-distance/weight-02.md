# Move 2: a signed spectral auxiliary vector

The coefficient-three claim remains unresolved. The calculations below suggest a uniform coefficient fifteen and an asymptotic coefficient three. They require a separate exact claim and independent proof acceptance before being treated as accepted branch results. They do not rely on numerical probes.

## Why the positive-vector cut estimate is insufficient

Let x be a unit positive Perron vector and let E contain b deleted edges. Put z=x^T A(E)x. Using x in the Rayleigh principle after deletion gives

    D(G) <= 3xi-2b+6 lambda z-3z^2

whenever lambda-z is nonnegative. To recover coefficient three this argument would need 6 lambda z-3z^2 <= 2b. For a neighbourhood cut in C5, x is constant, b=1, lambda=2, and z=2/5. The left side is 108/25, which exceeds two. This sufficient inequality is false even on the proposed equality graph. Thus merely using the original Perron vector after the cut does not repair the separate estimates.

## Enlarge the auxiliary-vector choice

Write the adjacency eigenvalues as lambda=lambda_1 >= ... >= lambda_n=-mu. For a nonempty triangle-free graph, lambda>0 and 0<mu<=lambda. Triangle-freeness gives trace(A^3)=0, while trace(A^2)=2m. Summing positive and negative cubes yields

    lambda^3 <= sum_{lambda_i<0} |lambda_i|^3
             <= mu sum_{lambda_i<0} lambda_i^2
             <= mu (2m-lambda^2).

Therefore mu >= lambda^3/(2m-lambda^2). This argument does not require connectivity.

Choose a real unit eigenvector y for -mu. Let F contain precisely the edges of G with one endpoint in {y>0} and the other in {y<0}; all remaining vertices and edges are handled by deletion. F is bipartite. Write b=m-e(F). Let P be the sum y_u y_v over edges whose endpoints have the same nonzero sign, and Q the sum |y_u y_v| over opposite-sign edges. Zero-coordinate edges contribute zero. Then

    -mu = 2P-2Q,
    |y|^T A(F)|y| = 2Q = mu+2P >= mu.

Because |y| has norm one, lambda(F)>=mu. Apply the fully read bipartite editing theorem (Lemma 4.3 of arXiv:2609.20225v2). The triangle inequality for symmetric difference gives

    D(G) <= b+3(e(F)-lambda(F)^2)
         <= 3(m-mu^2)-2b
         <= 3(m-mu^2).

Let r=lambda^2/m, which lies in (0,1] by Nosal. If r<1, then

    m-mu^2 <= m [1-r^3/(2-r)^2]
            = (m-lambda^2)(r^2+4)/(2-r)^2
            <= 5(m-lambda^2).

The last inequality follows from 5(2-r)^2-(r^2+4)=4(r-1)(r-4)>=0 for 0<=r<=1. If r=1, the preceding lower bound gives mu>=lambda; hence mu=lambda and the same conclusion is zero. Empty graphs have D=0. The resulting candidate theorem is

    D(G) <= 15(m-lambda^2).

The gain over the first move is linear dependence on xi, uniform in graph order. The exact coefficient fifteen is an upper bound, not a sharpness assertion. The inequality follows from a recent bipartite theorem and elementary spectral calculations; no claim of historical novelty is made before literature review.

## Asymptotic refinement from the same vector

Put delta=lambda^2-mu^2>=0. The coarse estimate above gives delta<=4xi. Remove one eigenvalue lambda and one eigenvalue -mu from the spectrum. The sum of squares of the remaining eigenvalues is

    S=2m-lambda^2-mu^2=2xi+delta<=6xi.

The trace-cube identity and the elementary norm inequality sum |a_i|^3 <= (sum a_i^2)^(3/2) give

    lambda^3-mu^3 <= S^(3/2).

Also lambda^3-mu^3 >= lambda(lambda^2-mu^2), because the difference of the two sides is mu^2(lambda-mu)>=0. Therefore

    delta <= (6xi)^(3/2)/lambda.

Combining with the signed-cut bound yields, for lambda>0,

    D(G) <= 3xi + 18 sqrt(6) xi^(3/2)/lambda.

In particular, along any sequence with xi/m tending to zero and positive deficit, this gives limsup D(G)/xi <= 3. This is an asymptotic estimate and does not establish the exact inequality D<=3xi for any nonzero deficit.

## Remaining question

The signed-cut proof leaves 3delta-2b and the slack in the bipartite edit bound. A sharp joint estimate would have to use that slack or a different target. The root claim is not replaced by coefficient fifteen or by the asymptotic statement. The exact coefficient-fifteen and asymptotic assertions will be recorded as a separate branch from the preserved checkpoint, with their assumptions and source dependency unchanged.
