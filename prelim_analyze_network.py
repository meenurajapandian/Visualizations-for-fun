import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


# Read the full network as G
G = nx.read_gml('user_friends.gml')

# To make sure encoding has not messed up things
print("Number of nodes in the full graph: ", G.number_of_nodes())
print("Number of edges in the full graph: ", G.number_of_edges())

print("Number of components: ", nx.number_connected_components(G))

largest = max(nx.connected_components(G), key=len)
L = G.subgraph(largest)
print("Number of nodes in largest component: ", L.number_of_nodes())
print("Number of edges in largest component: ", L.number_of_edges())

nodes = []
edges = []
for c in nx.connected_components(G):
    C = G.subgraph(c)
    n = nx.number_of_nodes(C)
    nodes.append(n)
    edges.append(nx.number_of_edges(C))


print("Nodes and edges in different components")
print(nodes)
print(edges)

# Possible plotting of some of the components


# Analyzing the largest component
print("Average Clustering: ",nx.average_clustering(L))
print("Transitivity: ", nx.transitivity(L))

hist_weight = nx.degree_histogram(G)
plt.hist(range(0,len(hist_weight)), len(hist_weight), weights=hist_weight)
plt.savefig('first_try_histogram.png')