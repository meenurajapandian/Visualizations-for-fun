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
                    print(row[0])
            else:
                    no_friends += 1

            line_count += 1


print(G.number_of_nodes())

G_largest = max(nx.connected_components(G), key=len)

print(G_largest.number_of_nodes())

print(line_count)