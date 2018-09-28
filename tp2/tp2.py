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
archive_bin="./dataset/yeast_Y2H_copy.txt"
archive_mul="./dataset/yeast_AP-MS_copy.txt"
archive_lit="./dataset/yeast_LIT_copy.txt"
archive_reg="./dataset/yeast_LIT_Reguly_copy.txt"

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
"""
# nos quedamos solo con los 2 primeros elementos de cada sub-lista
lista_reg_limpio = []
for i in lista_reg:
    lista_reg_limpio.append([i[0], i[1]])
"""
print(lista_reg)

"""
Greg = nx.Graph()
Greg.add_edges_from(lista_reg_limpio)

# Calcular numero de nodos ##############
# Utilizamos la funcion 'number_of_nodes' de Networkx
nodes_bin=Gbin.number_of_nodes()
nodes_mul=Gmul.number_of_nodes()
nodes_lit=Glit.number_of_nodes()
nodes_reg=Greg.number_of_nodes()

# Calcular numero de enlaces ##############
# Utilizamos la funcion 'number_of_edges' de Networkx
lbin = Gbin.number_of_edges()
lmul = Gmul.number_of_edges()
llit = Glit.number_of_edges()
lreg = Greg.number_of_edges()

# El grado medio para cada grafo
# Utilizamos la formula descripta arriba
avDegree_bin = 2*lbin/nodes_mul
avDegree_mul = 2*lmul/nodes_bin
avDegree_lit = 2*llit/nodes_lit
avDegree_reg = 2*lreg/nodes_reg

# Calculo del promedio de los clusterings locales (<Ci>) mediante la funcion 'average_clustering' de Networkx
ci_bin = nx.average_clustering(Gbin)
ci_mul = nx.average_clustering(Gmul)
ci_lit = nx.average_clustering(Glit)
ci_reg = nx.average_clustering(Greg)

# Imprimir tabla con todos los resultados del Problema 1

print ("\t\tred_bin\t\tred_mul\t\tred_lit\t\tred_reg\n" \
      + "=======================================================================\n" \
      + "Nodos\t\t%d\t\t%d\t\t%d\t\t%d\n" %(nodes_bin, nodes_mul, nodes_lit, nodes_reg)  \
      + "Enlaces\t\t%d\t\t%d\t\t%d\t\t%d\n" %(lbin, lmul, llit, lreg) \
      + "<k>\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\n" % (avDegree_bin, avDegree_mul, avDegree_lit, avDegree_reg) \
      + "<C>\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\n" % (ci_bin, ci_mul, ci_lit, ci_reg))
"""
