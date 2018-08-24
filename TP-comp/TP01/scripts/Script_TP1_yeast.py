#!/usr/bin/env python 
# Script TP1


# Modulos ###########
import networkx as nx
import matplotlib.pylab as plt


# Files ###################
archive_bin="/home/andrest/TP01/data_TP1/yeast_Y2H.txt"
archive_lit="/home/andrest/TP01/data_TP1/yeast_LIT.txt"
archive_mul="/home/andrest/TP01/data_TP1/yeast_AP-MS.txt"


archive_lit2=open("/home/andrest/TP01/data_TP1/yeast_LIT.txt", "r").readlines()
archive_mul2=open("/home/andrest/TP01/data_TP1/yeast_AP-MS.txt", "r").readlines()
archive_bin2=open("/home/andrest/TP01/data_TP1/yeast_Y2H.txt", "r").readlines()

Results = open("/home/andrest/TP01/Results.txt", "w")
############################



# Cantidad de enlaces #################
lbin = len(archive_bin2)
lmul = len(archive_mul2)
llit = len(archive_lit2)

Results.write("Enlaces lit:	" + str(llit) + "/n" + "Enlaces bin:	" + str(lbin) +"/n" + "Enlaces mul:	" + str(lmul) + "/n")
#######################################



def ldata(archive):
        f=open(archive)
	data=[]
	for line in f:
		line=line.strip()
		col=line.split()
		data.append(col)	
	return data

lista_mul = ldata(archive_mul)
lista_bin = ldata(archive_bin)
lista_lit = ldata(archive_lit)



Gmul = nx.Graph()
Gbin = nx.Graph()
Glit = nx.Graph()

Gmul.add_edges_from(lista_mul)
Gbin.add_edges_from(lista_bin)
Glit.add_edges_from(lista_lit)

#nx.draw(Gmul, with_labels=True, font_weight='bold')


# Numero de nodos
nodes_mul=Gmul.number_of_nodes()
nodes_bin=Gbin.number_of_nodes()
nodes_lit=Glit.number_of_nodes()

print ("Number of nodes mul:	" + str(nodes_mul))
print ("Number of nodes bin:	" + str(nodes_bin))
print ("Number of nodes lit:	" + str(nodes_lit))

Results.write("Nodos lit:	" + str(nodes_lit) + "/n" + "Nodos bin:	" + str(nodes_bin) +"/n" + "Nodos mul:	" + str(nodes_mul) + "/n")



#plt.show()





Results.close()







