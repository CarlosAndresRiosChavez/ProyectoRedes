#!/usr/bin/env python

from __future__ import division
import networkx as nx
import matplotlib.pylab as plt

#archivo1 = "../data_TP1/netscience.gml"
archivo2 = "../data_TP1/new_as-22july06.gml"

#G_colab = nx.read_gml(archivo1)
G_internet = nx.read_gml(archivo2)

dict_grados_internet = G_internet.degree()

#print(dict_grados_internet)

lista_grados = dict_grados_internet.values()
"""
lista_grados_ordenada = lista_grados.sort()
print(lista_grados_ordenada)
"""

lista_grados.sort()
print(lista_grados)

"""
for k in dict_grados_internet.keys():
    vecinos = G_internet.neighbors(str(k))
    #print(len(vecinos))
    for v in vecinos:
        #print( G_internet.degree(str(v)))
        #print(dict_grados_internet.get(str(v)))
    print('\n')
"""
