# -*- coding: utf-8 -*-
from __future__ import division
from numpy import log

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
results = open("../1_c_precision.txt", "w")

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
        
        s = "%s vs %s - Precision = " % (label_particion[i], label_particion[j])
        results.write("%51s %.2f\n" % (s, precision))

results.close()
"""

#########################################
########### Información mutua ###########
#########################################

results = open("../1_c_informacion_mutua.txt", "w")

for x in range(cant_particiones):
    for y in range(cant_particiones):
    
        print("%s vs %s" % (label_particion[x], label_particion[y]))
        
        particion_1 = dict(ldata(particiones[x]))
        particion_2 = dict(ldata(particiones[y]))

        cant_grupos_1 = max(int(particion_1[d]) for d in particion_1) + 1
        cant_grupos_2 = max(int(particion_2[d]) for d in particion_2) + 1

        cant_nodos = len(particion_1)

        # separo los delfines por comunidad
        comunidades_1 = []
        for i in range(cant_grupos_1):
            comunidades_1.append([])

        for d in particion_1:
            comunidades_1[int(particion_1[d])].append(d)

        comunidades_2 = []
        for i in range(cant_grupos_2):
            comunidades_2.append([])

        for d in particion_2:
            comunidades_2[int(particion_2[d])].append(d)
            
        # armo la matriz de coocurrencia:
        coocurrencia = []
        for i in range(cant_grupos_1):
            coocurrencia.append([])
            
        for i in range(cant_grupos_1):
            for j in range(cant_grupos_2):
                s1 = set(comunidades_1[i])
                s2 = set(comunidades_2[j])
                inter =  s1.intersection(s2)
                coocurrencia[i].append(len(inter))

        # for c in coocurrencia:
            # print(c)
        # print()
            
        # la matriz de probas conjuntas es la de coocurrencia dividido por la cant total de delfines:
        probas_conjuntas = []
        for i in range(cant_grupos_1):
            probas_conjuntas.append([])
            
        for i in range(cant_grupos_1):
            for j in range(cant_grupos_2):
                probas_conjuntas[i].append(coocurrencia[i][j]/cant_nodos)

        #for p in probas_conjuntas:
        #    print(p)
        #print()

        # para cada par de particiones deberia obtener un valor de I
        # me hago otra matriz que tenga los argumentos del log

        args_log = []
        for i in range(cant_grupos_1):
            args_log.append([])
            
        for i in range(cant_grupos_1):
            for j in range(cant_grupos_2):
                p_c1 = len(comunidades_1[i])/cant_nodos
                p_c2 = len(comunidades_2[j])/cant_nodos
                
                denom = p_c1*p_c2
                
                args_log[i].append(probas_conjuntas[i][j]/denom)

        #for a in args_log:
        #    print(a)
        #print()

        # para calcular I tengo que sumar:
        I = 0
        for i in range(cant_grupos_1):
            for j in range(cant_grupos_2):
                if probas_conjuntas[i][j] == 0:
                    continue
                sumando = probas_conjuntas[i][j]*log(args_log[i][j])
                I = I + sumando

        #print(I)

        # me da mayor que 1. Puedo hacer la version normalizada

        H_c1 = 0
        for c in comunidades_1:
            p_c1 = len(c)/cant_nodos
            sumando = p_c1*log(p_c1)
            H_c1 = H_c1 - sumando

        H_c2 = 0
        for c in comunidades_2:
            p_c2 = len(c)/cant_nodos
            sumando = p_c2*log(p_c2)
            H_c2 = H_c2 - sumando

        # I normalizada:
        I_norm = 2*I/(H_c1 + H_c2)

        print("I_n = %.2f" % (I_norm))
        print()
        
        s = "%s vs %s - I_n = " % (label_particion[x], label_particion[y])
        results.write("%45s %.2f\n" % (s, I_norm))

results.close()
