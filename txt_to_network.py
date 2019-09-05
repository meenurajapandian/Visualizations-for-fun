import networkx as nx

G = nx.Graph()
line_count = 0
with open("roadNet-PA.txt","r") as f:
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    content = f.readlines()
    for x in content:
        y = str.split(x)
        G.add_edge(y[0],y[1])
        line_count +=1


nx.write_gml(G, 'road.gml')

