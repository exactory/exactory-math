#!/usr/bin/env python3
"""Count canonical triples per stratum (n, N) and how many have c >= 3 (lrcalc only)."""
import sys, time
from multiprocessing import Pool
sys.path.insert(0, 'tools')
from scan import partitions, contained, canonical, lr_coef

def work(args):
    n_parts, N, lam = args
    tot = 0; c3 = 0; cs = 0
    for m in range(1, N):
        for mu in partitions(m, n_parts, lam[0]):
            if not contained(mu, lam): continue
            for nu in partitions(N - m, n_parts, lam[0]):
                if nu > mu or not contained(nu, lam): continue
                can = canonical(lam, mu, nu)
                if can is None: continue
                if max(len(can[0]), len(can[1]), len(can[2])) != n_parts: continue
                tot += 1
                c = lr_coef(*can)
                if c >= 3: c3 += 1
    return (n_parts, N, tot, c3)

if __name__ == '__main__':
    n_parts = int(sys.argv[1]); sizes = [int(x) for x in sys.argv[2].split(',')]
    jobs = [(n_parts, N, lam) for N in sizes for lam in partitions(N, n_parts) if len(lam) <= n_parts]
    t0 = time.time()
    agg = {}
    with Pool(10) as pool:
        for n, N, tot, c3 in pool.imap_unordered(work, jobs, chunksize=4):
            a = agg.setdefault((n, N), [0, 0]); a[0] += tot; a[1] += c3
    for k in sorted(agg): print(k, 'canonical', agg[k][0], 'c>=3', agg[k][1], flush=True)
    print('time', round(time.time() - t0, 1))
