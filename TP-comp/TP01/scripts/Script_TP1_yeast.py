#!/usr/bin/env python 


# Script TP1


# Modulos ###########
from __future__ import division
import networkx as nx
import matplotlib.pylab as plt
#####################


# Files ###################
archive_bin="../data_TP1/yeast_Y2H.txt"
archive_lit="../data_TP1/yeast_LIT.txt"
archive_mul="../data_TP1/yeast_AP-MS.txt"


archive_lit2=open("../data_TP1/yeast_LIT.txt", "r").readlines()
archive_mul2=open("../data_TP1/yeast_AP-MS.txt", "r").readlines()
archive_bin2=open("../data_TP1/yeast_Y2H.txt", "r").readlines()

Results = open("../Results_TP1.txt", "w")
############################


# Cantidad de enlaces #################
lbin = len(archive_bin2)
lmul = len(archive_mul2)
llit = len(archive_lit2)

# Escribir resultados en outputFile
Results.write("\t\tbin\t\tlit\t\tmul\n")
Results.write("Enlaces\t" + str(llit) + "\t" + str(lbin) +"\t" + str(lmul) + "\n")

#######################################


# Grafos ######################

# Funcion leer input files
def ldata(archive):
        f=open(archive)
	data=[]
	for line in f:
		line=line.strip()
		col=line.split()
		data.append(col)	
	return data

# Generar lista para c/input file
lista_mul = ldata(archive_mul)
lista_bin = ldata(archive_bin)
lista_lit = ldata(archive_lit)

# Generar grafos
Gmul = nx.Graph()
Gbin = nx.Graph()
Glit = nx.Graph()

# Agregar enlaces en cada grafo
Gmul.add_edges_from(lista_mul)
Gbin.add_edges_from(lista_bin)
Glit.add_edges_from(lista_lit)

lbin_var = Gbin.number_of_edges()
lmul_var = Gmul.number_of_edges()
llit_var = Glit.number_of_edges()

# Calcular numero de nodos ##############
nodes_mul=Gmul.number_of_nodes()
nodes_bin=Gbin.number_of_nodes()
nodes_lit=Glit.number_of_nodes()

# Escribir resultados en outputFile
Results.write("Nodos\t" + str(nodes_lit) + "\t" + str(nodes_bin) +"\t" + str(nodes_mul) + "\n")
#Results.write("Nodos lit:	" + str(nodes_lit) + '\n' + "Nodos bin:	" + str(nodes_bin) +'\n' + "Nodos mul:	" + str(nodes_mul) + '\n')
##########################################


# Calcular el grado medio para cada grafo #######################
# Grado medio c = 2m/n , donde m=No de enlaces y n=No de nodos

avDegree_mul = 2*lmul/nodes_mul
avDegree_bin = 2*lbin/nodes_bin
avDegree_lit = 2*llit/nodes_lit

Results.write("<k>\t\t%.2f\t%.2f\t%.2f\n" % (avDegree_lit, avDegree_bin, avDegree_mul) )
#Results.write("<k>\t" + str(avDegree_lit) + "\t" + str(avDegree_bin) +"\t" + str(avDegree_mul) + "\n")
#Results.write("<k> lit:	" + str(avDegree_lit) + '\n' + "<k> bin:	" + str(avDegree_bin) +'\n' + "<k> mul:	" + str(avDegree_mul) + '\n')

# Grados maximo y minimo

D_grados_mul = Gmul.degree()
grados_mul = D_grados_mul.values()
kmax_mul = max(grados_mul)
kmin_mul = min(grados_mul)
kmean_mul = sum(grados_mul) / float(len(grados_mul))

D_grados_bin = Gbin.degree()
grados_bin = D_grados_bin.values()
kmax_bin = max(grados_bin)
kmin_bin = min(grados_bin)
kmean_bin = sum(grados_bin) / float(len(grados_bin))

D_grados_lit = Glit.degree()
grados_lit = D_grados_lit.values()
kmax_lit = max(grados_lit)
kmin_lit = min(grados_lit)
kmean_lit = sum(grados_lit) / float(len(grados_lit))
"""
print(kmax_mul)
print(kmin_mul)
print(kmean_mul)
print(avDegree_mul)
"""

Results.write("k max\t%.2f\t%.2f\t%.2f\n" % (kmax_lit, kmax_bin, kmax_mul) )
Results.write("k min\t%.2f\t%.2f\t%.2f\n" % (kmin_lit, kmin_bin, kmin_mul) )

densidad_bin = nx.density(Gbin)
densidad_lit = nx.density(Glit)
densidad_mul = nx.density(Gmul)

Results.write("density\t%.4f\t%.4f\t%.4f\n" % (densidad_lit, densidad_bin, densidad_mul) )

c_global_lit = nx.transitivity(Glit)
c_global_bin = nx.transitivity(Gbin)
c_global_mul = nx.transitivity(Gmul)

ci_lit = nx.average_clustering(Glit)
ci_bin = nx.average_clustering(Gbin)
ci_mul = nx.average_clustering(Gmul)


Results.write("C global\t%.4f\t%.4f\t%.4f\n" % (c_global_lit, c_global_bin, c_global_mul) )
Results.write("C_i\t\t%.4f\t%.4f\t%.4f\n" % (ci_lit, ci_bin, ci_mul) )

giant_lit = max(nx.connected_component_subgraphs(Glit), key=len)

diam_lit = nx.diameter(giant_lit)
print(diam_lit)

print(nx.connected_component_subgraphs(Glit))

#diam_bin = nx.diameter(Gbin)
#diam_mul = nx.diameter(Gmul)

#Results.write("Diametro\t%.4f\t%.4f\t%.4f\n" % (diam_lit, diam_bin, diam_mul) )

Results.close()







