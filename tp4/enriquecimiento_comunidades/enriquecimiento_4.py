from __future__ import division
import numpy as np
from scipy import stats
from operator import itemgetter

# para una comunidad

def etapa_4(numero_de_comunidades):

    input_files = ["./4/community_" + numero_de_comunidades + "_comparacion_frecuencias_BP.txt", "./4/community_" + numero_de_comunidades + "_comparacion_frecuencias_CC.txt", "./4/community_" + numero_de_comunidades + "_comparacion_frecuencias_MF.txt"]

    categorias = ["BP", "CC", "MF"]

    output_file = "./4/community_" + numero_de_comunidades + "_enriquecidos_"

    for r in range(len(categorias)):

    #########################

        input = input_files[r]

        # voy a armar la "planilla de excel" en una lista de tuplas. O listas.
        go_terms = np.loadtxt(input, dtype='str', delimiter = '\t', usecols=(0, 1))
        columnas = np.loadtxt(input, dtype='int', delimiter = '\t', usecols=(2, 3, 4, 5))

        planilla = []

        for i in range(len(go_terms)):
            sublista = [go_terms[i][0], go_terms[i][1], columnas[i][0], columnas[i][1], columnas[i][2], columnas[i][3]]
            planilla.append(sublista)
            
        # calculo la distribucion hipergeometrica. Va a ir a parar a una nueva columna, ie, un nuevo casillero de la tupla.
        # h es el p-value de la distribucion
        for i in range(len(planilla)):
            h = stats.hypergeom.pmf(planilla[i][2], planilla[i][5], planilla[i][4], planilla[i][3])
            planilla[i].append(h)
            
        # ahora ordeno las filas (elementos de la lista mas grande) por tamaño del p-value, de manera descendente. Esta en el lugar 6.
        planilla_ordenada = sorted(planilla, key=itemgetter(6))

        # ahora aplico la correccion de Benjamini-Hochson:
        # el cociente para cada p-value es: la cantidad de go terms en la comunidad, sobre el numero de orden del p-value.
        for i in range(len(planilla_ordenada)):
            cociente = len(planilla_ordenada)/(i + 1)
            planilla_ordenada[i][-1] = planilla_ordenada[i][-1]*cociente

        # ahora fijo un corte en 0.05 y veo que terminos estan enriquecidos en esta comunidad
        corte = 0.05
            
        # armo un txt con los terminos enriquecidos

        results = open(output_file + categorias[r] + ".txt", "w")
        results.write("codigo\t\tp-value\t\tsignificado\n")

        for p in planilla_ordenada:
            if p[-1] <= corte:
                #print(p[0], p[1])
                results.write("%s\t%.8f\t%s\n" % (p[0], p[-1], p[1]))

        results.close()

