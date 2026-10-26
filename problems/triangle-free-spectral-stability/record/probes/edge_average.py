"""Screen the edge-neighbourhood averaging route on triangle-free graphs."""
import json
from pathlib import Path
import networkx as nx
import numpy as np

records=[]
graphs=[(f"atlas-{i}",g) for i,g in enumerate(nx.graph_atlas_g())]
for n in [10,15,20,30,50]:
 for seed in range(30):
  rng=np.random.default_rng(101*n+seed)
  g=nx.empty_graph(n)
  pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
  rng.shuffle(pairs)
  for i,j in pairs:
   if rng.random()<0.3 and not set(g[i])&set(g[j]):g.add_edge(i,j)
  graphs.append((f"random-{n}-{seed}",g))
for name,g in graphs:
 m=g.number_of_edges()
 if not m or any(nx.triangles(g).values()):continue
 a=nx.to_numpy_array(g); lam=float(np.linalg.eigvalsh(a)[-1]);xi=m-lam**2
 if xi<1e-9:continue
 a2=a@a; tr4=float(np.sum(a2*a2));b=sum(g.degree[u]*g.degree[v] for u,v in g.edges)
 ds=[]
 for u,v in g.edges:
  x=set(g[v]);y=set(g[u]);cross=sum(int(a[i,j]) for i in x for j in y)
  ds.append(m+len(x)*len(y)-2*cross)
 assert abs(sum(ds)-(m*m+b-tr4))<1e-7
 records.append(dict(name=name,n=len(g),m=m,xi=xi,mean_ratio=sum(ds)/m/xi,min_ratio=min(ds)/xi,edges=list(g.edges)))
Path("results").mkdir(exist_ok=True)
Path("results/edge-average.json").write_text(json.dumps(dict(scope="Atlas and 150 seeded greedy triangle-free random graphs. Floating-point spectral screening only.",records=records),indent=2)+"\n")
print(json.dumps(dict(count=len(records),max_mean=max(records,key=lambda r:r["mean_ratio"]),max_min=max(records,key=lambda r:r["min_ratio"]))))
