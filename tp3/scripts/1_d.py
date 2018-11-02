# -*- coding: utf-8 -*-

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import random
from numpy import linspace, mean

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data
    
generos = ldata("../dataset/dolphinsGender.txt")

particiones = ["../dataset/particion_louvain.txt", "../dataset/particion_edge_betweenness.txt", "../dataset/particion_fast_greedy_andres.txt", "../dataset/particion_infomap.txt"]


label_particion = ["Louvain", "Edge Betweenness", "Fast Greedy", "Infomap"]

# txt para guardar los p-valor
results = open("../p_valor.txt", "w")
    
# itero sobre las distintas particiones
for j in range(len(particiones)):

    print("Particion " + label_particion[j])
    
    # empiezo con louvain
    particion = ldata(particiones[j])

    grupos = []
    cant_grupos = int(max(v for u,v in particion)) + 1

    for i in range(cant_grupos):
        grupos.append([])

    for u,v in particion:
        for i in range(cant_grupos):
            if int(v) == i:
                grupos[i].append(u)
                
    # primero miro la distribucion de generos de esta particion
    # cuento la cantidad de machos y hembras en cada grupo

    # armo sets de generos:
    m = []
    f = []
    na = []

    for d,g in generos:
        if g == 'm':
            m.append(d)
        if g == 'f':
            f.append(d)
        if g == 'NA':
            na.append(d)
            
    cant_machos = len(m)
    cant_hembras = len(f)
    cant_na = len(na)

    generos_en_grupos = []

    for i in range(cant_grupos):
        #print("Grupo %s" % (i))
        label = "Grupo " + str(i)
        g = grupos[i]
        set_g = set(g)
        
        size_grupo = len(set_g)
        
        interseccion_m = set_g.intersection(m)
        interseccion_f = set_g.intersection(f)
        interseccion_na = set_g.intersection(na)
        
        #print(len(interseccion_m)/size_grupo, len(interseccion_f)/size_grupo, len(interseccion_na)/size_grupo)
        generos_en_grupos.append((label, len(interseccion_m)/size_grupo, len(interseccion_f)/size_grupo, len(interseccion_na)/size_grupo))

    ###########################################################################################
    ######################## ahora reasigno los generos aleatoriamente ########################
    ###########################################################################################

    sizes_grupos = []
    for g in grupos:
        sizes_grupos.append(len(g))

    # iteraciones
    N = 1000

    # con estas variables voy a hacer los histogramas
    # lista_m tiene que contener 4 histogramas, no uno
    hist_m = []
    hist_f = []
    hist_na = []

    for i in range(cant_grupos):
        hist_m.append([])
        hist_f.append([])
        hist_na.append([])

    for n in range(N):
        #print("ITERACION %d" % (n))
        #print("==============")
        
        etiquetas = []

        for d,g in generos:
            etiquetas.append(g)
            
        asignacion_random = []

        for i in range(62):
            r = random.choice(range(len(etiquetas)))
            p = etiquetas.pop(r)

            # ahora necesito meter p en bolsas
            # no lo necesito, puedo pensar que estan en orden, y se cuan largas son
            asignacion_random.append(p)

        # ahora extraigo la info de los grupos a partir de la lista
        # armo separadores de grupos por indice
        separadores = []
        
        # los separadores del grupo 0 los hago afuera del for
        separadores.append(0)
        separadores.append(0 + sizes_grupos[0])
        
        for i in range(1, cant_grupos):
            separadores.append(separadores[-1] + 1)
            separadores.append(separadores[-2] + sizes_grupos[i])
        
        grupos_rand = []
        
        for i in range(cant_grupos):
            g = asignacion_random[separadores[2*i]:separadores[2*i + 1]]
            grupos_rand.append(g)

        # armo las tuplas con las proporciones para cada grupo
        generos_en_grupos_rand = []

        # cuantos hay de cada cosa en cada grupo
        for i in range(cant_grupos):
            size_grupo = len(grupos_rand[i])
            
            cant_m = grupos_rand[i].count('m')
            cant_f = grupos_rand[i].count('f')
            cant_na = grupos_rand[i].count('NA')
            
            fraccion_m = cant_m/size_grupo
            fraccion_f = cant_f/size_grupo
            fraccion_na = cant_na/size_grupo
            
            hist_m[i].append(fraccion_m)
            hist_f[i].append(fraccion_f)
            hist_na[i].append(fraccion_na)
            
            label = "Grupo " + str(i)
            generos_en_grupos_rand.append((label, fraccion_m, fraccion_f, fraccion_na))

    # grafico histogramas
    
    # machos
    for i in range(cant_grupos):
        nombre = "../plots/" + label_particion[j] + " - Histograma machos - Grupo " + str(i) + ".png"
        titulo = label_particion[j] + " - Grupo " + str(i) + "\nN = " + str(N)
        
        # calculo el mean de la dist para saber de que lado esta mi valor experimental
        mean_dist = mean(hist_m[i])
        
        fig = plt.figure()
        #plt.hist(hist_m[i], bins = linspace(0, 1, 25), label='Modelo nulo')
        plt.hist(hist_m[i], label='Modelo nulo')
        
        # grafico el valor experimental
        plt.axvline(x = generos_en_grupos[i][1], color='red', label='Experimental')
        
        # señalo el maximo
        #plt.axvline(x = mean_dist, color='orange', label='Valor medio')
        
        # ademas calculo el p-valor
        # tengo que ver donde esta el maximo de la distribucion
        # recorro hist_m[i] y separo aquellos que son mas extremos que el valor experimental
        # me fijo si el valor experimental esta a la derecha o a la izq:
        if generos_en_grupos[i][1] > mean_dist:
            extremos = []
            for h in hist_m[i]:
                if h > generos_en_grupos[i][1]:
                    extremos.append(h)
            plt.hist(extremos, color='green', label='Extremos')
        else:
            extremos = []
            for h in hist_m[i]:
                if h < generos_en_grupos[i][1]:
                    extremos.append(h)
            plt.hist(extremos, color='green', label='Extremos')
        
        # para cada i tengo una lista de puntos extremos
        # los cuento y divido por el numero total de cuentas
        cuentas_totales = len(hist_m[i])
        cuentas_extremas = len(extremos)
        
        p_valor = cuentas_extremas/cuentas_totales
        
        results.write("%s - Machos - Grupo %d - p-valor = %.3f\n" % (label_particion[j], i, p_valor))
        
        plt.xlabel("fraccion de machos")
        plt.suptitle(titulo + " - p-valor = %.3f" % (p_valor))
        plt.legend()
        plt.savefig(nombre)
        plt.close(fig)
        
    # hembras
    for i in range(cant_grupos):
        nombre = "../plots/" + label_particion[j] + " - Histograma hembras - Grupo " + str(i) + ".png"
        titulo = label_particion[j] + " - Grupo " + str(i) + "\nN = " + str(N)
        
        mean_dist = mean(hist_f[i])
        
        fig = plt.figure()
        #plt.hist(hist_f[i], bins = linspace(0, 1, 25), label='Modelo nulo')
        plt.hist(hist_f[i], label='Modelo nulo')
        # grafico el valor experimental
        plt.axvline(x = generos_en_grupos[i][2], color='red', label='Experimental')
        
        #plt.axvline(x = mean_dist, color='orange', label='Valor medio')
        
        if generos_en_grupos[i][2] > mean_dist:
            extremos = []
            for h in hist_f[i]:
                if h > generos_en_grupos[i][2]:
                    extremos.append(h)
            plt.hist(extremos, color='green', label='Extremos')
        else:
            extremos = []
            for h in hist_f[i]:
                if h < generos_en_grupos[i][2]:
                    extremos.append(h)
            plt.hist(extremos, color='green', label='Extremos')
        
        cuentas_totales = len(hist_f[i])
        cuentas_extremas = len(extremos)
        
        p_valor = cuentas_extremas/cuentas_totales
        
        results.write("%s - Hembras - Grupo %d - p-valor = %.3f\n" % (label_particion[j], i, p_valor))
        
        plt.xlabel("fraccion de hembras")
        plt.suptitle(titulo + " - p-valor = %.3f" % (p_valor))
        plt.legend()
        plt.savefig(nombre)
        plt.close(fig)

    # NA
    for i in range(cant_grupos):
        nombre = "../plots/" + label_particion[j] + " - Histograma NA - Grupo " + str(i) + ".png"
        titulo = label_particion[j] + " - Grupo " + str(i) + "\nN = " + str(N)
        
        mean_dist = mean(hist_na[i])
        
        fig = plt.figure()
        #plt.hist(hist_na[i], bins = linspace(0, 1, 25), label='Modelo nulo')
        plt.hist(hist_na[i], label='Modelo nulo')
        # grafico el valor experimental
        plt.axvline(x = generos_en_grupos[i][3], color='red', label='Experimental')
        
        plt.axvline(x = mean_dist, color='orange')
        
        plt.xlabel("fraccion de NA")
        plt.suptitle(titulo)
        plt.legend()
        plt.savefig(nombre)
        plt.close(fig)

results.close()
