# Move 3: the joint sign-cut remainder

The root remains unresolved. This analytical move retains the savings discarded in the accepted supporting proof. It supplies no new accepted theorem or computational evidence.

Use the notation of the accepted proof: xi=m-lambda^2, least eigenvalue -mu, sign-cut graph F and b=m-e(F). Put

    delta=lambda^2-mu^2,
    r=lambda(F)^2-mu^2,
    s=3(e(F)-lambda(F)^2)-D(F).

The Rayleigh argument gives r>=0 and the published bipartite lemma gives s>=0. Symmetric difference gives the exact certificate bound

    D(G)<=b+D(F)=3xi+3delta-2b-3r-s.                 (1)

Thus 2b+3r+s>=3delta would suffice for this certificate. It is not established in general. Substituting the definition of s shows that this sufficient condition is exactly b+D(F)<=3xi. Introducing the slack therefore does not by itself give a new estimate for it. In particular, an inequality proved only by substituting this same target bound would be circular.

There is a small-deficit sufficient condition already implicit in the accepted proof. If b>=1 and 3delta<=2, then the nonnegative terms r and s make (1) at most 3xi. If b=0, G=F is bipartite and the published theorem applies. Combining this observation with the accepted estimate delta<=(6xi)^(3/2)/lambda gives a possible restricted quantitative route. No separately reviewed special-case claim or historical novelty is asserted here. The remaining task is to control the finite positive-deficit regime without assuming this sufficient condition.

The five-cycle illustrates why the slack cannot simply be dropped. Choose a least eigenvector with no zero coordinates. Its sign cut retains four edges and is P5, so b=1. The least spectral magnitude of C5 is mu=(1+sqrt(5))/2, and lambda(P5)^2=3. The latter follows from the path eigenvector with coordinates (1,sqrt(3),2,sqrt(3),1), whose adjacency image is sqrt(3) times that vector. Bipartite symmetry or the positive-vector Perron theorem identifies its spectral radius.

For P5, a target K_{2,2} on four vertices requires one added edge and deletion of the remaining end edge, giving D(P5)<=2. Distance zero is impossible because P5 is not complete bipartite with isolates. Distance one is also impossible: a target must then have either three or five edges. A three-edge complete bipartite target is a star K_{1,3}, which is absent from P5; a five-edge target would require six vertices. Thus D(P5)=2. Consequently s=3(4-3)-2=1, and

    3delta-2b-3r = 1,
    3delta-2b-3r-s = 0.

The full certificate recovers the exact value three here. Retaining the exact cut radius but only the universal bipartite edit bound still gives four. This is a concrete loss of that displayed composition, not a limitation of all sign-cut arguments or of spectral methods. The next step must estimate or avoid the graph-dependent slack, rather than count its definition as progress.

The global coefficient remains fifteen, with the previously accepted asymptotic estimate unchanged. The analytical improvement is the explicit joint certificate and its exact equality-case accounting. No finite cutoff, complete counterexample family or proof of the root follows.
