# Modulos ###########

from __future__ import division
import networkx as nx
import matplotlib.pylab as plt

# Input files #################
# Funcion para leer input files
def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data

# Input file paths
archive_bin="./dataset/yeast_Y2H_curado.txt"
archive_mul="./dataset/yeast_AP-MS_curado.txt"
archive_lit="./dataset/yeast_LIT_copy.txt"
archive_reg="./dataset/yeast_LIT_Reguly_curado.txt"

# Nodos esenciales
# Abrir archivo
l_essential = ldata("./dataset/Essential_ORFs_paperHe_curado.txt")

###### Grafo bin
lista_bin = ldata(archive_bin)
Gbin = nx.Graph()
Gbin.add_edges_from(lista_bin)

###### Grafo mul
lista_mul = ldata(archive_mul)
Gmul = nx.Graph()
Gmul.add_edges_from(lista_mul)

###### Grafo lit
lista_lit = ldata(archive_lit)
Glit = nx.Graph()
Glit.add_edges_from(lista_lit)

###### Grafo reg
lista_reg = ldata(archive_reg)
Greg = nx.Graph()
Greg.add_edges_from(lista_reg)



# Funcion overlap de NODOS #
def overlapEss(lista1, lista2):
	fraction = 0
	longitud = len(lista1) 
	num = 0
	for x in lista1:
		for y in lista2:
			if (x[0] == y[0]):
				num = num + 1
				fraction = num/longitud 
	return fraction
##########################


# FIGURA 1 Red bin #########################

# Calcular numero de nodos ##############
# Utilizamos la funcion 'number_of_nodes' de Networkx
# Numero de nodos
nodes_bin=Gbin.number_of_nodes()

# Lista de nodos
nodes = Gbin.nodes()

# Diccionario de nodos y grados
D_grados_bin = Gbin.degree()

# Lista de nodos y grados
items = D_grados_bin.items()
##print items

# Lista de nodos y grados ordenada
sorted_items = sorted(items, key=lambda tup: tup[1])
##print sorted_items

# Longitud de lista de nodos y grados ordenada
##print len(sorted_items)



# Definir lista para calcular enrichment
#for cutoff in range(0,1000,1):
#
#	corte= int((cutoff/1000)*(len(sorted_items)))
#
#	hubs = sorted_items[-corte:]
#	#print hubs
#
#


corte= int((1)*(len(sorted_items)))

hubs = sorted_items[-corte:]

print l_essential[1]
print (hubs[1])[0]

print "overlap", overlapEss(l_essential, hubs)


