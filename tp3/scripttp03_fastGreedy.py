# Script TP03 fast greedy

###### Modulos
import networkx as nx
import matplotlib.pyplot as plt

###### Grafo
G= nx.read_gml('dolphins.gml')

###### Generar lista de edges de "dolphins.gml"
edges = nx.write_edgelist(G,"Dolphins_edge_list.txt")
filEdges = open("Dolphins_edge_list.txt", "r").readlines()	

edgeList = []
for a in range(len(filEdges)):
	edgeLine = filEdges[a].split()
	tupla = (edgeLine[0],edgeLine[1])
	edgeList.append(tupla)

print(edgeList)
#nx.draw(G,with_labels=True)
#plt.show()


###### Definir comunidades mediante el metodo fast_greedy
comus = nx.algorithms.community.greedy_modularity_communities(G, weight=None)

###### Definir all_nodes y community_lists
all_nodes = []
for x in range(len(comus)):
	lista = list(comus[x])
	all_nodes = all_nodes + lista

	# Defino node_community_lists
	globals()['node_list_community%s' % x] = lista
	print(globals()['node_list_community%s' % x])
	#print(len(globals()['node_list_community%s' % x]))
	#print("\n")
	

###### Calculo de modularidad
q = nx.algorithms.community.modularity(G,comus)
print(q)


###### Armar grafo con comunidades
G3 = nx.Graph()
for n in all_nodes:
    G3.add_node(n)
for from_loc, to_loc in edgeList:
    G3.add_edge(from_loc, to_loc)


pos = nx.kamada_kawai_layout(G3) 

nx.draw(G3, pos, edge_color='k',  with_labels=True,font_weight='light', node_size= 80, width= 0.9)


colores = 'bygcm'

for c in range(len(colores)):
	print(colores[c])
	print(colores)

#For each community list, draw the nodes, giving it a specific color.
nx.draw_networkx_nodes(G3, pos, nodelist=node_list_community1, node_color='b', node_size= 80)
nx.draw_networkx_nodes(G3, pos, nodelist=node_list_community2, node_color='y', node_size= 80)
nx.draw_networkx_nodes(G3, pos, nodelist=node_list_community3, node_color='g', node_size= 80)
#nx.draw_networkx_nodes(G3, pos, nodelist=node_list_community4, node_color='c', node_size= 80)
#nx.draw_networkx_nodes(G3, pos, nodelist=node_list_community5, node_color='m', node_size= 80)

plt.savefig('fast_greedy.png')
plt.show()









