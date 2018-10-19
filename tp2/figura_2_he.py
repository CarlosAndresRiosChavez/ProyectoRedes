from __future__ import division
import networkx as nx
import numpy as np
from operator import itemgetter
import matplotlib.pylab as plt
from scipy.stats import linregress

ftsize = 16

# titulos figuras
tit_y2h = "Red Y2H"
tit_apms = "Red AP-MS"
tit_lit = "Red LIT"
tit_reg = "Red REG"

# nombres figuras
path_y2h = "./fig_2_He_y2h.png"
path_apms = "./fig_2_He_apms.png"
path_lit = "./fig_2_He_lit.png"
path_reg = "./fig_2_He_reg.png"

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data

# archivos de redes
file_y2h = "./dataset/yeast_Y2H_curado.txt"
file_apms = "./dataset/yeast_AP-MS_curado.txt"
file_lit = "./dataset/yeast_LIT_curado.txt"
file_reg = "./dataset/yeast_LIT_Reguly_curado.txt"

# lista de esenciales:
lista_esenciales_raw = ldata("./dataset/Essential_ORFs_paperHe_curado.txt")
lista_esenciales = []

for l in lista_esenciales_raw:
    lista_esenciales.append(l[0])

set_esenciales = set(lista_esenciales)

############ PARAMETROS ############
# hasta que grado grafico antes de perder la linealidad

# para y2h: 14
# para apms: 36 o 20
# para lit: 12
# para reg: 19
g = 19

# elijo la red
lista = ldata(file_reg)

# titulo del grafico
titulo = tit_reg

# output path de la figura
path = path_reg

####################################

G = nx.Graph()
G.add_edges_from(lista)

grados = G.degree()
por_grado = sorted(G.degree_iter(),key=itemgetter(1),reverse=True)

max_grados = max([i for i in grados.values()]) 

# separo los nodos de la red por grado.
# empiezo con grado 1

# coordenadas de los puntos:
coord_x = []
coord_y = []

for i in range(1, max_grados + 1):
    grado = i
    
    nodos_del_grado = []
    for n in por_grado:
        if n[1] == grado:
            nodos_del_grado.append(n[0])
    
    # habra grados que no esten en la red:
    if len(nodos_del_grado) == 0:
        continue
    
    # ahora interseco los nodos de grado 1 con los esenciales
    nodos_del_grado = set(nodos_del_grado)
    interseccion = nodos_del_grado.intersection(set_esenciales)

    # ahora calculo la proporcion del total de ese grado que representan:
    P_E = len(interseccion)/len(nodos_del_grado)

    # la coordenada y del punto es:
    # OJO! cuando P_E = 1, el log da -inf (?)
    print(i)
    y = np.log(1 - P_E)
    
    coord_x.append(grado)
    coord_y.append(y)

# regresion lineal
# recorto la cantidad de puntos que ajusto:

coord_x = coord_x[:g]
coord_y = coord_y[:g]

slope, intercept, r_value, p_value, std_err = linregress(coord_x, coord_y)

t = np.linspace(0, g, 100)
f = slope*t + intercept
"""
plt.plot(coord_x, coord_y, 'o')
plt.plot(t, f, '--r')
plt.grid()
plt.xlabel("grado", fontsize = ftsize)
plt.ylabel("$ln(1 - P_E)$", fontsize = ftsize)
plt.suptitle(titulo, fontsize = ftsize)
plt.savefig(path)
#plt.show()
"""

# ahora exporto los valores de alpha y beta
def despeje(param):
    desp = 1 - np.exp(param)
    return desp

alpha = 

