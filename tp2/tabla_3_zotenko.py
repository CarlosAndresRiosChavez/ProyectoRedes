from __future__ import division
import networkx as nx
import matplotlib.pylab as plt
import numpy as np

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

lista_esenciales = ldata("./dataset/Essential_ORFs_paperHe_curado.txt")

dict_grados_bin = Gbin.degree()
dict_grados_mul = Gmul.degree()
dict_grados_lit = Glit.degree()
dict_grados_reg = Greg.degree()

lista_grados_bin = sorted(dict_grados_bin.items(), key=lambda kv: kv[1])
lista_grados_mul = sorted(dict_grados_mul.items(), key=lambda kv: kv[1])
lista_grados_lit = sorted(dict_grados_lit.items(), key=lambda kv: kv[1])
lista_grados_reg = sorted(dict_grados_reg.items(), key=lambda kv: kv[1])

# armamos un subconjunto de cada lista que solo conserve aquellos nodos que son esenciales

def subconjunto_ess(lista):
    sublista = []
    for x in lista:
        for y in lista_esenciales:
            if (x[0] == y[0]):
                sublista.append(x)
    return sublista
	
esenciales_bin = subconjunto_ess(lista_grados_bin)
#degree_sequence = sorted(nx.degree(Gbin).values(),reverse=True) # degree sequence
#dmax = max(degree_sequence)

"""
# armo la secuencia de grados
secuencia_grados = []
for i in range(dmax):
    for j in esenciales_bin:
        if i == j[1]:
            secuencia_grados.append(i)
            pass
         
print(secuencia_grados)
"""
grado_esenciales = []
for e in esenciales_bin:
    grado_esenciales.append(e[1])
    
#print(esenciales_bin)
#print(grado_esenciales)

plt.hist(grado_esenciales, bins = np.arange(min(grado_esenciales), max(grado_esenciales) + 1))
plt.xlabel('grado de nodos esenciales')
plt.grid()
plt.show()
