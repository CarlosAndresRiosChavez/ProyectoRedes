from __future__ import division
import networkx as nx
import numpy as np

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data
    
# lista de pares totales de la Y2H:
file_pares = "./tabla_5_zotenko_pares_totales.txt"
lista_pares = ldata(file_pares)

# lista de esenciales:
lista_esenciales_raw = ldata("./dataset/Essential_ORFs_paperHe_curado.txt")
lista_esenciales = []

for l in lista_esenciales_raw:
    lista_esenciales.append(l[0])

set_esenciales = set(lista_esenciales)
    
mismo_tipo = []
    
# separo CUALES pares son del mismo tipo:
for l in lista_pares:
    set_l = set(l)
    interseccion = set_l.intersection(set_esenciales)
    
    if (len(interseccion) == 0) or (len(interseccion) == 2):
        mismo_tipo.append(l)

# teniendo los pares del mismo tipo, para cada nodo calculo P_E