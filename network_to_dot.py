import networkx as nx

#Import file however you want to

G = nx.read_gml("karate.gml", label='id')
print(nx.number_connected_components(G))

largest = max(nx.connected_components(G), key=len)
L = G.subgraph(largest).copy()

del G

#G = nx.complete_graph(4)
f = open("karate.dot","w+")
f.write("strict graph {\n") #Strict graph stuff

for u in L.nodes():
    f.write(str(u)+'\n')

for u,v in L.edges():
    f.write(str(u) + ' -- ' + str(v) + '\n')

f.write("}")

f.close()