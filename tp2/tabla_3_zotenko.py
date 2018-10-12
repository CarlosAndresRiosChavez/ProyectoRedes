from __future__ import division
import networkx as nx
import matplotlib.pylab as plt
import numpy as np
from itertools import groupby
from collections import Counter
from random import choice

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

lista_esenciales_raw = ldata("./dataset/Essential_ORFs_paperHe_curado.txt")
lista_esenciales = []

for l in lista_esenciales_raw:
    lista_esenciales.append(l[0])

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
            if (x[0] == y):
                sublista.append(x)
    return sublista
	
esenciales_bin = subconjunto_ess(lista_grados_bin)

grado_esenciales = []
for e in esenciales_bin:
    grado_esenciales.append(e[1])    

# counter es un diccionario que tiene como keys los grados para los que hay nodos esenciales, y como values la cantidad de nodos esenciales para ese grado
counter = Counter(grado_esenciales)

nodos_bin = Gbin.nodes()

grados_que_tienen_esenciales = counter.keys()
cuantos_hay_que_remover = counter.values()

###################################################################################################
#################################### esto anda para grado fijo ####################################
###################################################################################################
"""
indice = 17

print("size total inicial = %d" % (Gbin.number_of_nodes()))
print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))

grado_check = grados_que_tienen_esenciales[indice]

print("remuevo de grado %d" % (grado_check))
print("===================")
print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
print("===========================")

# agrupo los nodos que tienen ese grado y que no son esenciales
nodos_de_interes = []
for i in dict_grados_bin:
    if Gbin.degree(i) == grado_check:
        nodos_de_interes.append(i)
        
# me falta descartar los esenciales
set_nodos_de_interes = set(nodos_de_interes)
set_esenciales = set(lista_esenciales)
nodos_de_interes = list(set_nodos_de_interes - set_esenciales)

removidos = 0

while removidos < cuantos_hay_que_remover[indice]:
    try:
        nodo_azar = choice(nodos_de_interes)
        Gbin.remove_node(nodo_azar)
        removidos = removidos + 1
        
        print("size total = %d" % (Gbin.number_of_nodes()))
        print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))
        
        # luego de remover un nodo, actualizo mi conjunto de nodos de interes
        nodos_de_interes = []
        for i in dict_grados_bin:
            if Gbin.degree(i) == grado_check:
                nodos_de_interes.append(i)
                
        # me falta descartar los esenciales
        set_nodos_de_interes = set(nodos_de_interes)
        set_esenciales = set(lista_esenciales)
        nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
    except:
        grado_check = grado_check - 1
        
        print("remuevo de grado %d" % (grado_check))
        print("===================")
        print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
        print("===========================")

        # agrupo los nodos que tienen ese grado y que no son esenciales
        nodos_de_interes = []
        for i in dict_grados_bin:
            if Gbin.degree(i) == grado_check:
                nodos_de_interes.append(i)
                
        # me falta descartar los esenciales
        set_nodos_de_interes = set(nodos_de_interes)
        set_esenciales = set(lista_esenciales)
        nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
        
    print("grado check = %d" % (grado_check))
"""
        
###################################################################################################
###################################################################################################
###################################################################################################
"""
for indice in range(len(counter)):

    print("size total inicial = %d" % (Gbin.number_of_nodes()))
    print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))

    grado_check = grados_que_tienen_esenciales[indice]

    print("remuevo de grado %d" % (grado_check))
    print("===================")
    print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
    print("===========================")

    # agrupo los nodos que tienen ese grado y que no son esenciales
    nodos_de_interes = []
    for i in dict_grados_bin:
        if Gbin.degree(i) == grado_check:
            nodos_de_interes.append(i)
            
    # me falta descartar los esenciales
    set_nodos_de_interes = set(nodos_de_interes)
    set_esenciales = set(lista_esenciales)
    nodos_de_interes = list(set_nodos_de_interes - set_esenciales)

    removidos = 0

    while removidos < cuantos_hay_que_remover[indice]:
        try:
            nodo_azar = choice(nodos_de_interes)
            Gbin.remove_node(nodo_azar)
            removidos = removidos + 1
            
            print("size total = %d" % (Gbin.number_of_nodes()))
            print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))
            
            # luego de remover un nodo, actualizo mi conjunto de nodos de interes
            nodos_de_interes = []
            for i in dict_grados_bin:
                if Gbin.degree(i) == grado_check:
                    nodos_de_interes.append(i)
                    
            # me falta descartar los esenciales
            set_nodos_de_interes = set(nodos_de_interes)
            set_esenciales = set(lista_esenciales)
            nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
        except:
            grado_check = grado_check - 1
            
            print("remuevo de grado %d" % (grado_check))
            print("===================")
            print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
            print("===========================")

            # agrupo los nodos que tienen ese grado y que no son esenciales
            nodos_de_interes = []
            for i in dict_grados_bin:
                if Gbin.degree(i) == grado_check:
                    nodos_de_interes.append(i)
                    
            # me falta descartar los esenciales
            set_nodos_de_interes = set(nodos_de_interes)
            set_esenciales = set(lista_esenciales)
            nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
            
        print("grado check = %d" % (grado_check))
"""

##################################################
### OJO!!! ESTA FUNCION DESTRUYE EL GRAFO!!!!! ###
##################################################

def tabla_3():
    for indice in range(len(counter)):
        """
        print("size total inicial = %d" % (Gbin.number_of_nodes()))
        print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))
        """
        grado_check = grados_que_tienen_esenciales[indice]
        """
        print("remuevo de grado %d" % (grado_check))
        print("===================")
        print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
        print("===========================")
        """
        # agrupo los nodos que tienen ese grado y que no son esenciales
        nodos_de_interes = []
        for i in dict_grados_bin:
            if Gbin.degree(i) == grado_check:
                nodos_de_interes.append(i)
                
        # me falta descartar los esenciales
        set_nodos_de_interes = set(nodos_de_interes)
        set_esenciales = set(lista_esenciales)
        nodos_de_interes = list(set_nodos_de_interes - set_esenciales)

        removidos = 0

        while removidos < cuantos_hay_que_remover[indice]:
            try:
                nodo_azar = choice(nodos_de_interes)
                Gbin.remove_node(nodo_azar)
                removidos = removidos + 1
                """
                print("size total = %d" % (Gbin.number_of_nodes()))
                print("size componente gigante = %d" % (len(max(nx.connected_components(Gbin), key=len))))
                """
                # luego de remover un nodo, actualizo mi conjunto de nodos de interes
                nodos_de_interes = []
                for i in dict_grados_bin:
                    if Gbin.degree(i) == grado_check:
                        nodos_de_interes.append(i)
                        
                # me falta descartar los esenciales
                set_nodos_de_interes = set(nodos_de_interes)
                set_esenciales = set(lista_esenciales)
                nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
            except:
                grado_check = grado_check - 1
                """
                print("remuevo de grado %d" % (grado_check))
                print("===================")
                print("cuantos hay que remover = %d" % (cuantos_hay_que_remover[indice]))
                print("===========================")
                """
                # agrupo los nodos que tienen ese grado y que no son esenciales
                nodos_de_interes = []
                for i in dict_grados_bin:
                    if Gbin.degree(i) == grado_check:
                        nodos_de_interes.append(i)
                        
                # me falta descartar los esenciales
                set_nodos_de_interes = set(nodos_de_interes)
                set_esenciales = set(lista_esenciales)
                nodos_de_interes = list(set_nodos_de_interes - set_esenciales)
                
            #print("grado check = %d" % (grado_check))
            
    size_comp_gigante = len(max(nx.connected_components(Gbin), key=len))
 
    return size_comp_gigante

for i in range(5):
    print i
    print tabla_3()
    Gbin = nx.Graph()
    Gbin.add_edges_from(lista_bin)

#print(counter)
#print(len(lista_grados_bin) - len(esenciales_bin))


"""
plt.hist(grado_esenciales, bins = np.arange(min(grado_esenciales), max(grado_esenciales) + 1))
plt.plot(counter.keys(), counter.values(), 'or')
plt.xlabel('grado de nodos esenciales')
plt.grid()
plt.show()
"""
