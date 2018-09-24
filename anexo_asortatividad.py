#!/usr/bin/env python

from __future__ import division
import networkx as nx
import matplotlib.pylab as plt
from numpy import log10
from scipy.stats import linregress
from numpy import linspace

def turn_to_power(list, power): 
    return [number**power for number in list]

##########################################################
#################### ARCHIVO 2 ###########################
##########################################################

# red de internet
archivo2 = "../data_TP1/new_as-22july06.gml"

G_internet = nx.read_gml(archivo2)

dict_grados_internet = G_internet.degree()

lista_grados = dict_grados_internet.values()

lista_grados.sort()

d_grado_gradovecinos = []

for n in dict_grados_internet.keys():
    vecinos = G_internet.neighbors(str(n))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_internet.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    tupla = dict_grados_internet.get(str(n)), grado_medio
    d_grado_gradovecinos.append(tupla)

promedio_por_grados = []

datos = zip(*d_grado_gradovecinos)
datos_x = datos[0]
datos_y = datos[1]


diccionario_hist = {}
for i in range(1, max(lista_grados) + 1):
    acumulada = 0
    size = 0
    for t in d_grado_gradovecinos:    
        if t[0]==i:
            acumulada = acumulada + t[1]
            size = size + 1
    try:
        promedio = acumulada/size
        diccionario_hist[str(i)] = promedio
    except:
        pass

#diccionario_hist.items()
lista_dict = diccionario_hist.items()

hist = zip(*lista_dict)
lista_hist_x = list(hist[0])
lista_hist_y = list(hist[1])

lista_hist_x = list(map(int, lista_hist_x))

############
# inciso a-i, internet
############

plt.figure(1)
ax = plt.gca()
#ax.scatter(*zip(*d_grado_gradovecinos))
ax.scatter(datos_x, datos_y)
ax.scatter(lista_hist_x, lista_hist_y, c='r')
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('grado', fontsize=18)
plt.ylabel('grado medio de los vecinos', fontsize=16)
plt.grid('on')
plt.suptitle('Red de internet', fontsize=16)
plt.savefig('../inciso_a_i_internet.png')
#plt.show()
plt.close()

##########################################################################################
# ahora aplicamos log a los datos y volvemos a escala lineal para hacer un ajuste lineal #
##########################################################################################
lista_hist_x = list(map(float, lista_hist_x))
#print(lista_hist_x)

datos_log_x = log10(lista_hist_x)
datos_log_y = log10(lista_hist_y)

slope, intercept, r_value, p_value, std_err = linregress(datos_log_x, datos_log_y)
x = linspace(0, max(datos_log_x))
fit = slope*x + intercept

#######################
# inciso a iii internet
#######################

plt.figure(1)
plt.plot(datos_log_x, datos_log_y, '.')
plt.plot(x, fit, 'r--')
plt.xlabel('log(grado)', fontsize=18)
plt.ylabel('log(grado medio de los vecinos)', fontsize=16)
plt.suptitle('Red de internet', fontsize=16)
plt.grid('on')
plt.savefig('../inciso_a_iii_internet.png')
#plt.show()
plt.close()

##############################################
# inciso 4
##############################################

#nx.write_edgelist(G_internet, "test.edgelist.txt")

enlaces = open("test.edgelist.txt", "r").readlines()

suma = 0
for e in enlaces:
    e = e.split()
    grado1 = G_internet.degree(e[0])
    grado2 = G_internet.degree(e[1])
    producto = grado1*grado2
    suma = suma + producto

Se = 2*suma

S1 = sum(lista_grados)
S2 = sum(turn_to_power(lista_grados, 2))
S3 = sum(turn_to_power(lista_grados, 3))

r = (S1*Se - S2**2)/(S1*S3 - S2**2)

##########################################################
#################### ARCHIVO 1 ###########################
##########################################################

# red de colaboraciones cientificas
archivo1 = "../data_TP1/netscience_edgeslist.txt"
G_colab = nx.read_edgelist(archivo1, delimiter=";")

# diccionario con los grados de cada nodo
dict_grados_1 = G_colab.degree()
# lo convertimos a lista
lista_grados_1 = dict_grados_1.values()
# la ordenamos
lista_grados_1.sort()  

# Lista de tuplas. Hay una tupla por nodo. Cada tupla tiene en su primer casillero el 
# grado del nodo, y en el 2do casillero el promedio de los grados de todos sus vecinos
d_grado_gradovecinos_1 = []

for n in dict_grados_1.keys():
    vecinos = G_colab.neighbors(str(n))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_1.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    tupla = dict_grados_1.get(str(n)), grado_medio
    d_grado_gradovecinos_1.append(tupla)


promedio_por_grados_1 = []

datos_1 = zip(*d_grado_gradovecinos_1)
datos_x_1 = datos_1[0]
datos_y_1 = datos_1[1]

diccionario_hist_1 = {}
for i in range(1, max(lista_grados_1) + 1):
    acumulada = 0
    size = 0
    for t in d_grado_gradovecinos_1:    
        if t[0]==i:
            acumulada = acumulada + t[1]
            size = size + 1
    try:
        promedio = acumulada/size
        diccionario_hist_1[str(i)] = promedio
    except:
        pass
        
#diccionario_hist.items()
lista_dict_1 = diccionario_hist_1.items()

hist_1 = zip(*lista_dict_1)

lista_hist_x_1 = list(hist_1[0])
lista_hist_y_1 = list(hist_1[1])

lista_hist_x_1 = list(map(int, lista_hist_x_1))

plt.figure(1)
ax = plt.gca()
#ax.scatter(*zip(*d_grado_gradovecinos))
ax.scatter(datos_x_1, datos_y_1)
ax.scatter(lista_hist_x_1, lista_hist_y_1, c='r')
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('grado', fontsize=18)
plt.ylabel('grado medio de los vecinos', fontsize=16)
plt.grid('on')
plt.suptitle('Red de colaboraciones', fontsize=16)
plt.savefig('../inciso_a_i_colaboraciones.png')
#plt.show()
plt.close()

##########################################################################################
# ahora aplicamos log a los datos y volvemos a escala lineal para hacer un ajuste lineal #
##########################################################################################
lista_hist_x_1 = list(map(float, lista_hist_x_1))

datos_log_x_1 = log10(lista_hist_x_1)
datos_log_y_1 = log10(lista_hist_y_1)

slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = linregress(datos_log_x_1, datos_log_y_1)
x_1 = linspace(0, max(datos_log_x_1))
fit_1 = slope_1*x_1 + intercept_1

##############################################
# inciso 4
##############################################

nx.write_edgelist(G_colab, "test.edgelist_colab.txt")

enlaces_1 = open("test.edgelist_colab.txt", "r").readlines()

suma = 0
for e in enlaces_1:
    #print(e)
    e = e.split()
    #print(e[0] + " " + e[1])
    grado1 = G_colab.degree(e[0] + " " + e[1])
    #print(grado1)
    grado2 = G_colab.degree(e[2] + " " + e[3])
    #print(grado2)
    producto = grado1*grado2
    suma = suma + producto

Se_1 = 2*suma

S1_1 = sum(lista_grados_1)

S2_1 = sum(turn_to_power(lista_grados_1, 2))
S3_1 = sum(turn_to_power(lista_grados_1, 3))

r_1 = (S1_1*Se_1 - S2_1**2)/(S1_1*S3_1 - S2_1**2)

plt.figure(1)
plt.plot(datos_log_x_1, datos_log_y_1, '.')
plt.plot(x_1, fit_1, 'r--')
plt.xlabel('log(grado)', fontsize=18)
plt.ylabel('log(grado medio de los vecinos)', fontsize=16)
plt.grid('on')
plt.suptitle('Red de colaboraciones cientificas', fontsize=16)
#plt.show()
plt.savefig('../inciso_a_iii_colaboraciones.png')
plt.close()

#####################################################################################################
############################ RED DE PROTEINAS - INTERACCIONES BINARIAS ##############################
#####################################################################################################

# repito todo etiquetando con un 3

archivo3 = "../data_TP1/yeast_Y2H.txt"
G_3 = nx.read_edgelist(archivo3)

# diccionario con los grados de cada nodo
dict_grados_3 = G_3.degree()
# lo convertimos a lista
lista_grados_3 = dict_grados_3.values()
# la ordenamos
lista_grados_3.sort()  

# Lista de tuplas. Hay una tupla por nodo. Cada tupla tiene en su primer casillero el 
# grado del nodo, y en el 2do casillero el promedio de los grados de todos sus vecinos
d_grado_gradovecinos_3 = []

for n in dict_grados_3.keys():
    vecinos = G_3.neighbors(str(n))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_3.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    tupla = dict_grados_3.get(str(n)), grado_medio
    d_grado_gradovecinos_3.append(tupla)


promedio_por_grados_3 = []

datos_3 = zip(*d_grado_gradovecinos_3)
datos_x_3 = datos_3[0]
datos_y_3 = datos_3[1]

diccionario_hist_3 = {}
for i in range(1, max(lista_grados_3) + 1):
    acumulada = 0
    size = 0
    for t in d_grado_gradovecinos_3:    
        if t[0]==i:
            acumulada = acumulada + t[1]
            size = size + 1
    try:
        promedio = acumulada/size
        diccionario_hist_3[str(i)] = promedio
    except:
        pass
        
lista_dict_3 = diccionario_hist_3.items()

hist_3 = zip(*lista_dict_3)

lista_hist_x_3 = list(hist_3[0])
lista_hist_y_3 = list(hist_3[1])

lista_hist_x_3 = list(map(int, lista_hist_x_3))

##########################################################################################
# ahora aplicamos log a los datos y volvemos a escala lineal para hacer un ajuste lineal #
##########################################################################################
lista_hist_x_3 = list(map(float, lista_hist_x_3))

datos_log_x_3 = log10(lista_hist_x_3)
datos_log_y_3 = log10(lista_hist_y_3)

slope_3, intercept_3, r_value_3, p_value_3, std_err_3 = linregress(datos_log_x_3, datos_log_y_3)
x_3 = linspace(0, max(datos_log_x_3))
fit_3 = slope_3*x_3 + intercept_3

###########
# inciso 4
###########

nx.write_edgelist(G_3, "test.edgelist_3.txt")

enlaces_3 = open("test.edgelist_3.txt", "r").readlines()

suma = 0
for e in enlaces_3:
    e = e.split()
    grado1 = G_3.degree(e[0])
    grado2 = G_3.degree(e[1])
    producto = grado1*grado2
    suma = suma + producto

Se_3 = 2*suma

S1_3 = sum(lista_grados_3)
S2_3 = sum(turn_to_power(lista_grados_3, 2))
S3_3 = sum(turn_to_power(lista_grados_3, 3))

r_3 = (S1_3*Se_3 - S2_3**2)/(S1_3*S3_3 - S2_3**2)

plt.figure(1)
plt.plot(datos_log_x_3, datos_log_y_3, '.')
plt.plot(x_3, fit_3, 'r--')
plt.xlabel('log(grado)', fontsize=18)
plt.ylabel('log(grado medio de los vecinos)', fontsize=16)
plt.grid('on')
plt.suptitle('Red de proteinas - interacciones binarias', fontsize=16)
plt.savefig('../inciso_a_iii_interacciones_binarias.png')
#plt.show()
plt.close()

plt.figure(1)
ax = plt.gca()
ax.scatter(datos_x_3, datos_y_3)
ax.scatter(lista_hist_x_3, lista_hist_y_3, c='r')
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('grado', fontsize=18)
plt.ylabel('grado medio de los vecinos', fontsize=16)
plt.grid('on')
plt.suptitle('Red de proteinas - interacciones binarias', fontsize=16)
plt.savefig('../inciso_a_i_interacciones_binarias.png')
#plt.show()
plt.close()

##################################################################################################
############################ RED DE PROTEINAS - COMPLEJOS PROTEICOS ##############################
##################################################################################################

# repito todo etiquetando con un 4

archivo4 = "../data_TP1/yeast_AP-MS.txt"
G_4 = nx.read_edgelist(archivo4)

# diccionario con los grados de cada nodo
dict_grados_4 = G_4.degree()
# lo convertimos a lista
lista_grados_4 = dict_grados_4.values()
# la ordenamos
lista_grados_4.sort()  

# Lista de tuplas. Hay una tupla por nodo. Cada tupla tiene en su primer casillero el 
# grado del nodo, y en el 2do casillero el promedio de los grados de todos sus vecinos
d_grado_gradovecinos_4 = []

for n in dict_grados_4.keys():
    vecinos = G_4.neighbors(str(n))
    grado_acumulado = 0
    for v in vecinos:
        # queremos calcular el promedio de los grados de los vecinos de este nodo (n)
        grado_acumulado = grado_acumulado + dict_grados_4.get(str(v))
    grado_medio = grado_acumulado/len(vecinos)
    tupla = dict_grados_4.get(str(n)), grado_medio
    d_grado_gradovecinos_4.append(tupla)

promedio_por_grados_4 = []

datos_4 = zip(*d_grado_gradovecinos_4)
datos_x_4 = datos_4[0]
datos_y_4 = datos_4[1]

diccionario_hist_4 = {}
for i in range(1, max(lista_grados_4) + 1):
    acumulada = 0
    size = 0
    for t in d_grado_gradovecinos_4:    
        if t[0]==i:
            acumulada = acumulada + t[1]
            size = size + 1
    try:
        promedio = acumulada/size
        diccionario_hist_4[str(i)] = promedio
    except:
        pass
        
lista_dict_4 = diccionario_hist_4.items()

hist_4 = zip(*lista_dict_4)

lista_hist_x_4 = list(hist_4[0])
lista_hist_y_4 = list(hist_4[1])

lista_hist_x_4 = list(map(int, lista_hist_x_4))

##########################################################################################
# ahora aplicamos log a los datos y volvemos a escala lineal para hacer un ajuste lineal #
##########################################################################################
lista_hist_x_4 = list(map(float, lista_hist_x_4))

datos_log_x_4 = log10(lista_hist_x_4)
datos_log_y_4 = log10(lista_hist_y_4)

slope_4, intercept_4, r_value_4, p_value_4, std_err_4 = linregress(datos_log_x_4, datos_log_y_4)
x_4 = linspace(0, max(datos_log_x_4))
fit_4 = slope_4*x_4 + intercept_4

###########
# inciso 4
###########

nx.write_edgelist(G_4, "test.edgelist_4.txt")

enlaces_4 = open("test.edgelist_4.txt", "r").readlines()

suma = 0
for e in enlaces_4:
    e = e.split()
    grado1 = G_4.degree(e[0])
    grado2 = G_4.degree(e[1])
    producto = grado1*grado2
    suma = suma + producto

Se_4 = 2*suma
S1_4 = sum(lista_grados_4)
S2_4 = sum(turn_to_power(lista_grados_4, 2))
S3_4 = sum(turn_to_power(lista_grados_4, 3))

r_4 = (S1_4*Se_4 - S2_4**2)/(S1_4*S3_4 - S2_4**2)

plt.figure(1)
plt.plot(datos_log_x_4, datos_log_y_4, '.')
plt.plot(x_4, fit_4, 'r--')
plt.xlabel('log(grado)', fontsize=18)
plt.ylabel('log(grado medio de los vecinos)', fontsize=16)
plt.grid('on')
plt.suptitle('Red de proteinas - complejos proteicos', fontsize=16)
plt.savefig('../inciso_a_iii_complejos_proteicos.png')
#plt.show()
plt.close()

plt.figure(1)
ax = plt.gca()
ax.scatter(datos_x_4, datos_y_4)
ax.scatter(lista_hist_x_4, lista_hist_y_4, c='r')
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('grado', fontsize=18)
plt.ylabel('grado medio de los vecinos', fontsize=16)
plt.grid('on')
plt.suptitle('Red de proteinas - complejos proteicos', fontsize=16)
plt.savefig('../inciso_a_i_complejos_proteicos.png')
#plt.show()
plt.close()

Results = open("../Resultados_punto_4.txt", "w")

Results.write("Red de internet\n")
Results.write("===============\n")
Results.write("Parametros del ajuste:\n")
Results.write("pendiente = %.2f\n" % slope)
Results.write("intercept = %.2f\n" % intercept)
Results.write("r_value = %.2f\n" % r_value)
Results.write("p_value = %.2f\n" % p_value)
Results.write("std_err = %.2f\n" % std_err)
Results.write("Estimador de Newman:\n")
Results.write("r = %.2f\n\n" % r)

Results.write("Red de colaboraciones cientificas\n")
Results.write("=================================\n")
Results.write("Parametros del ajuste:\n")
Results.write("pendiente = %.2f\n" % slope_1)
Results.write("intercept = %.2f\n" % intercept_1)
Results.write("r_value = %.2f\n" % r_value_1)
Results.write("p_value = %.2f\n" % p_value_1)
Results.write("std_err = %.2f\n" % std_err_1)
Results.write("Estimador de Newman:\n")
Results.write("r = %.2f\n\n" % r_1)

Results.write("Red de proteinas - interacciones binarias\n")
Results.write("=========================================\n")
Results.write("Parametros del ajuste:\n")
Results.write("pendiente = %.2f\n" % slope_3)
Results.write("intercept = %.2f\n" % intercept_3)
Results.write("r_value = %.2f\n" % r_value_3)
Results.write("p_value = %.2f\n" % p_value_3)
Results.write("std_err = %.2f\n" % std_err_3)
Results.write("Estimador de Newman:\n")
Results.write("r = %.2f\n\n" % r_3)

Results.write("Red de proteinas - complejos proteicos\n")
Results.write("======================================\n")
Results.write("Parametros del ajuste:\n")
Results.write("pendiente = %.2f\n" % slope_4)
Results.write("intercept = %.2f\n" % intercept_4)
Results.write("r_value = %.2f\n" % r_value_4)
Results.write("p_value = %.2f\n" % p_value_4)
Results.write("std_err = %.2f\n" % std_err_4)
Results.write("Estimador de Newman:\n")
Results.write("r = %.2f\n\n" % r_4)
Results.close()