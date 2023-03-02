import networkx as nx
import matplotlib.pyplot as plt
import os
from get_communities import get_communities

G = nx.Graph()
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('final_code', 'final_code\datasets\code_test_case.txt')
edge_file =  open(dir,'r')
edge_list = edge_file.readlines()
for edge in edge_list:
    edge = edge.split()
    G.add_node(int(edge[0]))
    G.add_node(int(edge[1]))
    G.add_edge(int(edge[0]), int(edge[1]))
G = G.to_undirected()

CS = get_communities(G)

# nx.draw(G, with_labels = True)
# plt.show()

