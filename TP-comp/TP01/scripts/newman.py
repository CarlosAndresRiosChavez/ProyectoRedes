#Para esta seccion utilizo el trabajo de Alstott et al. (2014) DOI: http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0085777

import numpy as np
import math as ma
import networkx as nx
import powerlaw
from matplotlib import pyplot as plt

data_internet = nx.read_gml('DATA/as-22july06.gml')
a = list(data_internet)

amount = nx.Graph.order(data_internet)

grado = np.zeros(amount)
    
for i in range(0,amount):
  grado[i] = data_internet.degree[a[i]]

#Regla de Sturge para el numero de bins
print 1 + (3.322 * np.log10(amount))

datos_log, bines_log = np.histogram(grado,bins=np.logspace(np.log10(np.min(grado)),np.log10(np.max(grado)),15))
datos_lin, bines_lin = np.histogram(grado,bins=np.linspace(np.log10(np.min(grado)),np.log10(np.max(grado)),15)) 

#Ajuste a ley de potencias, vease: https://github.com/jeffalstott/powerlaw
ajuste = powerlaw.Fit(grado,xmin=1.0)
print(ajuste.power_law.alpha)
print(ajuste.power_law.xmin)
R, p = ajuste.distribution_compare('power_law', 'lognormal')

#El alpha de la ley de potencias esta dado por ajuste.power_law.alpha

#Plotting
fig = plt.figure(figsize=(15,10))
#plt.suptitle('Histogramas Datos Newman', fontsize=22)
#plt.subplot(2, 2, 1)
powerlaw.plot_pdf(grado, color='b')
ajuste.power_law.plot_pdf(color='b', linestyle='--')
#plt.subplot(2, 2, 2)
#powerlaw.plot_cdf(grado, color='b')
#plt.subplot(2, 2, 3)
powerlaw.plot_ccdf(grado, color='r')
#plt.subplot(2, 2, 4)
A = np.diff(bines_log)
ydata = np.divide(datos_log + 0.0,np.amax(datos_log))
print ydata
plt.loglog(np.diff(bines_log),ydata,'o')
#plt.plot(np.diff(bines_log)*ajuste.power_law.alpha,datos_log,'-')
plt.show()
#plt.savefig('maps.png', dpi=300)

