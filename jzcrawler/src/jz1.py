# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:08:13 2015

@author: SiddhuJz
"""
import networkx as nx
import matplotlib.pyplot as plt
import json
import os
    
def generate_graph(file_path, file_name, extension):
    data_str = open(file_path, "r").read()
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
        #if(G.has_edge(u, v, key=0)):
        #if(0):
        #    print(G.get_edge_data(u, v, key=0))
        #    #wt = G[u][v]['weight']
        #    wt = G[u][v][0]['weight']
        #    #wt = 1        
        #    print(x)
        #    wt = wt + 1
        #    print(wt)
        #    G.add_edge(u, v, key=0, weight=wt)
        #else, add a new edge between the nodes
        #else:
            #G.add_edge(u, v, weight=1)
            #G.add_edge(u, v)
        G.add_edge(u, v)
    
    #Draw Graph
    #nx.draw(G)
    
    if not os.path.exists(os.path.dirname("./" + file_name + "/network/network_" + file_name + ".graphml")):
        os.makedirs(os.path.dirname("./" + file_name + "/network/network_" + file_name + ".graphml"))
    if not os.path.exists(os.path.dirname("./" + file_name + "/graph/graph_" + file_name + ".pdf")):
        os.makedirs(os.path.dirname("./" + file_name + "/graph/graph_" + file_name + ".pdf"))

    file = open("./" + file_name + "/network/network_" + file_name + ".graphml", 'w')
    file.close()
    file = open("./" + file_name + "/network/network_" + file_name + ".gml", 'w')
    file.close()
    file = open("./" + file_name + "/network/network_" + file_name + ".gexf", 'w')
    file.close()
    file = open("./" + file_name + "/network/network_" + file_name + ".edgelist", 'w')
    file.close()
    file = open("./" + file_name + "/network/network_" + file_name + ".yaml", 'w')
    file.close()
    file = open("./" + file_name + "/network/network_" + file_name + ".gpickle", 'w')
    file.close()
    
    nx.write_graphml(G, "./" + file_name + "/network/network_" + file_name + ".graphml")
    nx.write_gml(G, "./" + file_name + "/network/network_" + file_name + ".gml")
    nx.write_gexf(G, "./" + file_name + "/network/network_" + file_name + ".gexf")
    nx.write_edgelist(G, "./" + file_name + "/network/network_" + file_name + ".edgelist")
    nx.write_yaml(G, "./" + file_name + "/network/network_" + file_name + ".yaml")
    nx.write_gpickle(G, "./" + file_name + "/network/network_" + file_name + ".gpickle")
    plt.savefig("./" + file_name + "/graph/graph_" + file_name + ".pdf")
    #plt.show()

#Main - Start
file_list = []
#file_list.append("./Output/CarverCollegeofMedicine.json")
#file_list.append("./Output/CollegeofDentistry.json")
#file_list.append("./Output/CollegeofEducation.json")
#file_list.append("./Output/CollegeofEngineering.json")
#file_list.append("./Output/CollegeofLaw.json")
#file_list.append("./Output/CollegeofLiberalArtsandSciences.json")
#file_list.append("./Output/CollegeofNursing.json")
#file_list.append("./Output/CollegeofPharmacy.json")
#file_list.append("./Output/CollegeofPublicHealth.json")
#file_list.append("./Output/ContinuingEducation.json")
#file_list.append("./Output/GraduateCollege.json")
#file_list.append("./Output/TheUniversityofIowa.json")
#file_list.append("./Output/TippieCollegeofBusiness.json")
#file_list.append("./Output/UniversityCollege.json")

file_list.append("./Output/CarverCollegeofMedicine.json")
file_list.append("./Output/CollegeofDentistry.json")
file_list.append("./Output/CollegeofEducation.json")
file_list.append("./Output/CollegeofEngineering.json")
file_list.append("./Output/CollegeofLaw.json")
file_list.append("./Output/CollegeofLiberalArtsandSciences.json")
file_list.append("./Output/CollegeofNursing.json")
file_list.append("./Output/CollegeofPharmacy.json")
file_list.append("./Output/CollegeofPublicHealth.json")
file_list.append("./Output/ContinuingEducation.json")
file_list.append("./Output/GraduateCollege.json")
file_list.append("./Output/TheUniversityofIowa.json")
file_list.append("./Output/TippieCollegeofBusiness.json")
file_list.append("./Output/UniversityCollege.json")

for file in file_list:
    base=os.path.basename(file)
    arr = os.path.splitext(base)
    print("Generating %s" % arr[0])
    generate_graph(file, arr[0], arr[1])
    #print file_name    
    print("Done Generating %s" % arr[0])
    
