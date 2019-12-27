import networkx as nx

G1 = nx.Graph()
with open("road.txt", "r") as f:
    content = f.readlines()
    for x in content:
        y = str.split(x,',')
        G1.add_edge(int(y[0]), int(y[1]))
