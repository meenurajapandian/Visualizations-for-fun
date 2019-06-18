import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

# Read the full network as G
G = nx.read_gml('user_friends.gml')

largest = max(nx.connected_components(G), key=len)
L = G.subgraph(largest)

nx.set_node_attributes(L, dict(L.degree()), 'Degree')

for u in L.nodes():
    if L.node[u]['Degree'] == 1:
        L.remove_node(u)

plt.figure()
pos = nx.spring_layout(L)
edges = nx.draw_networkx_edges(L, pos=pos, alpha=0.2)
xy = np.array(list(pos.values()))

xmax, ymax = xy.max(axis=0)
xmin, ymin = xy.min(axis=0)

plt.xlim(xmin-0.1, xmax+0.1)
plt.ylim(ymin-0.1, ymax+0.1)
plt.savefig('First_attempt.png')
