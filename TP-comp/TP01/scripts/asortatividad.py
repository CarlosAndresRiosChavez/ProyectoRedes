#!/usr/bin/env python

from __future__ import division
import networkx as nx
import matplotlib.pylab as plt
import operator

#archivo1 = "../data_TP1/netscience.gml"
archivo2 = "../data_TP1/new_as-22july06.gml"

#G_colab = nx.read_gml(archivo1)
G_internet = nx.read_gml(archivo2)

dict_grados_internet = G_internet.degree()

lista_grados = dict_grados_internet.values()

lista_grados.sort()
"""
d_grado_gradovecinos = {}

for n in dict_grados_internet.keys():
    vecinos = G_internet.neighbors(str(n))
    #print(len(vecinos))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_internet.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    d_grado_gradovecinos[str(dict_grados_internet.get(str(n)))] = grado_medio

#print(d_grado_gradovecinos)

# ahora queremos mirar por grado e ir promediando los grados medios
grados = d_grado_gradovecinos.keys()
grados = list(map(int, grados))

for i in range(1, max(grados) + 1):
    for key, value in d_grado_gradovecinos.items():
        if int(key) == i:
            print(i, key)
"""    

d_grado_gradovecinos = []

for n in dict_grados_internet.keys():
    vecinos = G_internet.neighbors(str(n))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_internet.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    tupla = dict_grados_internet.get(str(n)), grado_medio
    d_grado_gradovecinos.append(tupla)

#print(d_grado_gradovecinos[0])
"""
promedio_por_grados = {}

for i in range(1, max(lista_grados) + 1):
    suma = 0
    size = 0
    for j in d_grado_gradovecinos:
        if j[0] == i:
            suma = suma + j[1]
            size = size + 1
            promedio_por_grados[str(j[0])] = suma/size


sorted_x = sorted(promedio_por_grados.items(), key=operator.itemgetter(0))
"""

promedio_por_grados = []

for i in range(1, max(lista_grados) + 1):
#for i in lista_grados:
    suma = 0
    size = 0
    for j in d_grado_gradovecinos:
        if j[0] == i:
            
            suma = suma + j[1]
            size = size + 1
            tupla = (j[0], suma/size)
            
            #print(j, i)
            promedio_por_grados.append(tupla)

#print(d_grado_gradovecinos)
#print(promedio_por_grados)
#print(lista_grados)
#print(max(promedio_por_grados))
