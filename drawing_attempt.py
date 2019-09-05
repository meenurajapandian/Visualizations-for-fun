import sys
import csv
import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from networkx.drawing.nx_pydot import write_dot

csv.field_size_limit(sys.maxsize)

# Read the full network as G
#G = nx.read_gml('user_friends.gml')


G = nx.Graph()
with open('yelp_academic_dataset_user.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
            if row[0] != 'None':
                    #row[0] - friends row[11] - user_id
                    friends = row[0].split(', ')
                    user = row[11]
                    for friend in friends:
                        G.add_edge(user, friend)


largest = max(nx.connected_components(G), key=len)
L = G.subgraph(largest).copy()

del G

nx.set_node_attributes(L, dict(L.degree()), 'Degree')

one_degree = []
for u in L.nodes():
    if L.node[u]['Degree'] == 1:
        one_degree.append(u)
    if L.node[u]['Degree'] > 14900:
        one_degree.append(u)

L.remove_nodes_from(one_degree)
write_dot(L, 'dotfileyelp.dot')

plt.figure()
pos = nx.spring_layout(L)
edges = nx.draw_networkx_edges(L, pos=pos, alpha=0.2)
xy = np.array(list(pos.values()))

xmax, ymax = xy.max(axis=0)
xmin, ymin = xy.min(axis=0)

plt.xlim(xmin-0.1, xmax+0.1)
plt.ylim(ymin-0.1, ymax+0.1)
plt.savefig('First_attempt.png')
