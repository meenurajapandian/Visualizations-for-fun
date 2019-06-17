import csv
import sys
import networkx as nx


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

nx.write_gml(G,'user_friends.gml')

print("Number of nodes in the full graph: ", G.number_of_nodes())
print("Number of edges in the full graph: ", G.number_of_edges())
