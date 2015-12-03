# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:52:14 2015

@author: SiddhuJz
"""

import networkx as nx

# First read graphml-files into Python and Networkx (duplicate variables as necessary)
graph_list = []
graph_list.append(nx.read_graphml("./TheUniversityofIowa/network/network_TheUniversityofIowa.graphml"))
graph_list.append(nx.read_graphml("./CarverCollegeofMedicine/network/network_CarverCollegeofMedicine.graphml"))
graph_list.append(nx.read_graphml("./CollegeofDentistry/network/network_CollegeofDentistry.graphml"))
graph_list.append(nx.read_graphml("./CollegeofEducation/network/network_CollegeofEducation.graphml"))
graph_list.append(nx.read_graphml("./CollegeofEngineering/network/network_CollegeofEngineering.graphml"))
graph_list.append(nx.read_graphml("./CollegeofLaw/network/network_CollegeofLaw.graphml"))
graph_list.append(nx.read_graphml("./CollegeofLiberalArtsandSciences/network/network_CollegeofLiberalArtsandSciences.graphml"))
graph_list.append(nx.read_graphml("./CollegeofNursing/network/network_CollegeofNursing.graphml"))
graph_list.append(nx.read_graphml("./CollegeofPharmacy/network/network_CollegeofPharmacy.graphml"))
graph_list.append(nx.read_graphml("./CollegeofPublicHealth/network/network_CollegeofPublicHealth.graphml"))
graph_list.append(nx.read_graphml("./ContinuingEducation/network/network_ContinuingEducation.graphml"))
graph_list.append(nx.read_graphml("./GraduateCollege/network/network_GraduateCollege.graphml"))
graph_list.append(nx.read_graphml("./TippieCollegeofBusiness/network/network_TippieCollegeofBusiness.graphml"))
graph_list.append(nx.read_graphml("./UniversityCollege/network/network_UniversityCollege.graphml"))

# Create a new graph variable containing all the previous graphs
#merge_graph = nx.compose_all(graph_list)

# write the merged graphml files-variable into a new merged graphml file
#nx.write.graphml(merge_graph, "./merged_file.graphml", encoding="utf-8", prettyprint=True)

#for graph in graph_list:
#    if graph == nx.read_graphml("./TheUniversityofIowa/network/network_TheUniversityofIowa.graphml"):
#        merge_graph = graph
#    else:
#        merge_graph = nx.compose(merge_graph, graph)
#        nx.write.graphml(merge_graph, "./merged_file.graphml", encoding="utf-8", prettyprint=True)
        
merge_graph = graph_list[0]

for i in range(1, graph_list.count):
    merge_graph = nx.compose(merge_graph, graph_list[i])
    nx.write.graphml(merge_graph, "./merged_file" + i + ".graphml", encoding="utf-8", prettyprint=True)
