from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import random

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data
    

generos = ldata("../dataset/dolphinsGender.txt")

# empiezo con louvain
particion = ldata("../particion_louvain.txt")

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

#print(generos_en_grupos)

###########################################################################################
######################## ahora reasigno los generos aleatoriamente ########################
###########################################################################################

sizes_grupos = []
for g in grupos:
    sizes_grupos.append(len(g))

# iteraciones
N = 5

for n in range(N):
    print("ITERACION %d" % (n))
    print("============")
    
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
    grupo_0 = asignacion_random[0:12]
    grupo_1 = asignacion_random[13:30]
    grupo_2 = asignacion_random[31:36]
    grupo_3 = asignacion_random[37:54]
    grupo_4 = asignacion_random[55:62]

    grupos_rand = [grupo_0, grupo_1, grupo_2, grupo_3, grupo_4]

    # armo las tuplas con las proporciones para cada grupo
    generos_en_grupos_rand = []

    # cuantos hay de cada cosa en cada grupo
    for i in range(cant_grupos):
        size_grupo = len(grupos_rand[i])
        
        cant_m = grupos_rand[i].count('m')
        cant_f = grupos_rand[i].count('f')
        cant_na = grupos_rand[i].count('NA')
        
        label = "Grupo " + str(i)
        generos_en_grupos_rand.append((label, cant_m/size_grupo, cant_f/size_grupo, cant_na/size_grupo))

    for g in generos_en_grupos_rand:
        print("%s, Prop. machos = %.2f, Prop. hembras = %.2f, Prop. NA = %.2f" % (g[0], g[1], g[2], g[3]))

