# Modulos ###########

from __future__ import division
import networkx as nx
import matplotlib.pylab as plt

# Input files #################
# Funcion para leer input files
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

"""
# nos quedamos solo con los 2 primeros elementos de cada sub-lista
lista_reg_limpio = []
for i in lista_reg:
    lista_reg_limpio.append([i[0], i[1]])
"""
#print(lista_reg)


# Calcular numero de nodos ##############
# Utilizamos la funcion 'number_of_nodes' de Networkx
nodes_bin=Gbin.number_of_nodes()
nodes_mul=Gmul.number_of_nodes()
nodes_lit=Glit.number_of_nodes()
nodes_reg=Greg.number_of_nodes()

# Calcular numero de enlaces ##############
# Utilizamos la funcion 'number_of_edges' de Networkx
lbin = Gbin.number_of_edges()
lmul = Gmul.number_of_edges()
llit = Glit.number_of_edges()
lreg = Greg.number_of_edges()

# El grado medio para cada grafo
# Utilizamos la formula descripta arriba
avDegree_bin = 2*lbin/nodes_mul
avDegree_mul = 2*lmul/nodes_bin
avDegree_lit = 2*llit/nodes_lit
avDegree_reg = 2*lreg/nodes_reg

# Calculo del promedio de los clusterings locales (<Ci>) mediante la funcion 'average_clustering' de Networkx
ci_bin = nx.average_clustering(Gbin)
ci_mul = nx.average_clustering(Gmul)
ci_lit = nx.average_clustering(Glit)
ci_reg = nx.average_clustering(Greg)

# Imprimir tabla con todos los resultados del Problema 1
"""
print ("\t\tred_bin\t\tred_mul\t\tred_lit\t\tred_reg\n" \
      + "=======================================================================\n" \
      + "Nodos\t\t%d\t\t%d\t\t%d\t\t%d\n" %(nodes_bin, nodes_mul, nodes_lit, nodes_reg)  \
      + "Enlaces\t\t%d\t\t%d\t\t%d\t\t%d\n" %(lbin, lmul, llit, lreg) \
      + "<k>\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\n" % (avDegree_bin, avDegree_mul, avDegree_lit, avDegree_reg) \
      + "<C>\t\t%.4f\t\t%.4f\t\t%.4f\t\t%.4f\n" % (ci_bin, ci_mul, ci_lit, ci_reg))
"""

"""
longitud = len(lista_bin) 
num = 0
for x in lista_bin:
    gen1=x[0]
    gen2=x[1]

    for y in lista_mul:
        genA=y[0]
        genB=y[1]
        
        if gen1 == gen2 and genA == genB and gen1 in y and gen2 in y:
            num = num + 1

        if gen1 != gen2 and genA != genB and gen1 in y and gen2 in y:
            num = num + 1

fraction = num/longitud
print fraction
"""
"""
def overlap(lista1, lista2):
    longitud = len(lista1) 
    num = 0
    for x in lista1:
        gen1=x[0]
        gen2=x[1]

        for y in lista2:
            genA=y[0]
            genB=y[1]
            # cambiar esto por el sistema de los porotos
            if gen1 == gen2 and genA == genB and gen1 ==genA:
                num = num + 1

            if gen1 != gen2 and genA != genB and gen1 in y and gen2 in y:
                num = num + 1

    fraction = num/longitud
    return fraction
"""

"""
def overlap(lista1, lista2):
    longitud = len(lista1) 
    num = 0
    for x in lista1:
        for y in lista2:
            coincidencias = 0
            if x[0] == y[0]:
                coincidencias = coincidencias + 1
            if x[0] == y[1]:
                coincidencias = coincidencias + 1
            if x[1] == y[0]:
                coincidencias = coincidencias + 1
            if x[1] == y[1]:
                coincidencias = coincidencias + 1
            if coincidencias == 2 or coincidencias == 4:
                num = num + 1
    fraction = num/longitud
    return fraction
"""

def overlap(lista1, lista2):
    longitud = len(lista1) 
    num = 0
    for x in lista1:
        for y in lista2:
            if (x == y) or (x == y[::-1]):
                num = num + 1
                print("coincidencia", x, y)
    fraction = num/longitud 
    return fraction
#print(overlap(lista_bin, lista_mul))

tabla = []
"""
listFiles = [lista_bin, lista_mul, lista_lit, lista_reg]
for i in listFiles:
    for j in listFiles:
        print(listFiles.index(i), listFiles.index(j))
        o = overlap(i, j)
        tupla = (listFiles.index(i), listFiles.index(j), o)
        tabla.append(tupla)
"""
#print(tabla)

print(overlap(lista_reg, lista_reg))
#inter = nx.intersection(Gbin,Gmul)
#inter = inter.number_of_edges()



