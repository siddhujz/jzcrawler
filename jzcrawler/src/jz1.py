# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:08:13 2015

@author: SiddhuJz
"""
import networkx as nx
import matplotlib.pyplot as plt
import json
    
data_str = open("./Output/UniversityCollege.json", "r").read()
data = json.loads(data_str)
print(len(data))
#with open("./Output/UniversityCollege.json") as data_file:
#    data = json.load(data_file)
#pprint(data)

G = nx.MultiDiGraph()

#for x in range(0, len(data)):
for x in range(0, len(data)):
    u = data[x]['toUrl']
    v = data[x]['fromUrl']

    #Check if there is an existing node, if not, add a new node
    if(not(G.has_node(u))):
        G.add_node(u)
    #Check if there is an existing node, if not, add a new node
    if(not(G.has_node(v))):
        G.add_node(v)
    #Check if there is an existing edge between the nodes
    #if yes, increment the weight of the edge
    if(G.has_edge(u, v)):
        print(G.get_edge_data(u, v))
        #wt = G[u][v]['weight']
        wt = G[u][v][0]['weight']
        #wt = 1        
        print(x)
        wt = wt + 1
        print(wt)
        G.add_edge(u, v, weight=wt)
    #else, add a new edge between the nodes
    else:
        G.add_edge(u, v, weight=1)
    #G.add_edge(u, v)

nx.draw(G)
nx.write_gml(G, 'network.gml')
plt.savefig("graph.pdf")
#plt.show()
