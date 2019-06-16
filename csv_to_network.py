import csv
import sys
import networkx as nx
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

csv.field_size_limit(sys.maxsize)

line_count = 0
no_friends = 0
with_friends = 0
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
            else:
                    no_friends += 1

            line_count += 1


print(G.number_of_nodes())
#nx.write_graphml(G, "user_friends.graphml")

largest = max(nx.connected_components(G), key=len)
L = G.subgraph(largest)
print(L.number_of_nodes())
print(L.number_of_edges())

fig = plt.figure()
nx.draw(L, node_color='white', node_size=1500, edge_color='white')
plt.savefig('first_try.png', facecolor='#000000')