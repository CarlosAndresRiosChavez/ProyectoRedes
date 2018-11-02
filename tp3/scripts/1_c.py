# -*- coding: utf-8 -*-
from __future__ import division

# matriz de confusion
# para cada par de algoritmos tengo una matriz
# miro todos los pares de nodos y me fijo si en ambos algoritmos son compañeros de comunidad
# si son, suman un poroto

# informacion mutua
# tomo un par de algoritmos. Calculo la probabilidad de pertenecer a cada uno de los grupos de cada algoritmo
# calculo la probabilidad conjunta como cantidad(nodos1 int nodos2)/N

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data

particiones = ["../dataset/particion_louvain.txt", "../dataset/particion_edge_betweenness.txt", "../dataset/particion_fast_greedy_andres.txt", "../dataset/particion_infomap.txt"]

label_particion = ["Louvain", "Edge Betweenness", "Fast Greedy", "Infomap"]

cant_particiones = len(particiones)

"""
###########################################
########### Matriz de confusión ###########
###########################################
for i in range(cant_particiones):
    for j in range(cant_particiones):
    
        # agarro 2 particiones
        particion_1 = ldata(particiones[i])
        particion_2 = ldata(particiones[j])
        particion_1 = dict(particion_1)
        particion_2 = dict(particion_2)
        si_1_si_2 = 0
        no_1_si_2 = 0
        si_1_no_2 = 0
        no_1_no_2 = 0
        # delfines a y b. Busco las etiquetas en ambas part
        for d_a in particion_1:
            for d_b in particion_1:
            
                # descarto pares del mismo delfin
                if d_a == d_b:
                    continue
                
                # son vecinos en 1?
                if particion_1[d_a] == particion_1[d_b]:
                    if particion_2[d_a] == particion_2[d_b]:
                        # son vecinos en ambas
                        si_1_si_2 = si_1_si_2 + 1
                    else:
                        si_1_no_2 = si_1_no_2 + 1
                        
                if particion_1[d_a] != particion_1[d_b]:
                    if particion_2[d_a] == particion_2[d_b]:
                        no_1_si_2 = no_1_si_2 + 1
                    else:
                        # no son vecinos en ninguna
                        no_1_no_2 = no_1_no_2 + 1
                         
        print("Matriz de confusión - particiones " + label_particion[i] + " y " + label_particion[j])
        print(64*"=")
        print(si_1_si_2, no_1_si_2)
        print(si_1_no_2, no_1_no_2)
        
        # calculo la precision
        precision = (si_1_si_2 + no_1_no_2)/(si_1_si_2 + no_1_si_2 + si_1_no_2 + no_1_no_2)
        print("Precisión = %.2f\n" % (precision))
"""
#########################################
########### Información mutua ###########
#########################################

# agarro 2 particiones
particion_1 = dict(ldata(particiones[0]))
particion_2 = dict(ldata(particiones[1]))

cant_nodos = len(particion_1)

# para cada una calculo la proba de pertenecer a cada grupo
cant_grupos_1 = max(int(particion_1[d]) for d in particion_1) + 1
cant_grupos_2 = max(int(particion_2[d]) for d in particion_2) + 1

# ahora quiero saber cuantos miembros tiene cada comunidad
# es mas facil con count
# armo listas con las etiquetas de pertenencia de cada delfin

etiquetas_1 = []
etiquetas_2 = []

for d in particion_1:
    etiquetas_1.append(particion_1[d])

for d in particion_2:
    etiquetas_2.append(particion_2[d])

sizes_grupos_1 = []
sizes_grupos_2 = []
    
for i in range(cant_grupos_1):
    sizes_grupos_1.append(etiquetas_1.count(str(i)))

for i in range(cant_grupos_2):
    sizes_grupos_2.append(etiquetas_2.count(str(i)))
    
# ahora calculo las probabilidades de pertenecer a cada grupo
# es dividir la cant de nodos de cada grupo por la cant total de nodos

probas_grupos_1 = [s/cant_nodos for s in sizes_grupos_1]
probas_grupos_2 = [s/cant_nodos for s in sizes_grupos_2]


