#!/usr/bin/env python3


# Delfines


# Modulos ###########
from __future__ import division
import networkx as nx
import matplotlib.pylab as plt

archivo = "../data_TP1/new_dolphins.gml"
archivo2=open("../data_TP1/dolphinsGender.txt","r").readlines()
G = nx.read_gml(archivo)
"""
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
"""

# armamos un diccionario a partir del archivo dolphinsGender.txt

nombres = []
generos = []
gender_dict = {}
for i in archivo2:
    j=i.split("\t")
    
    #print(j[1])
    gender_dict[j[0]] = j[1].rstrip()
    
#print(gender_dict)

#print(type(gender_dict))
nx.set_node_attributes(G, gender_dict, 'gender')
