from __future__ import division
import networkx as nx
from community import best_partition
import matplotlib.pyplot as plt

def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data

G = nx.read_gml("./dolphins.gml")

partition = best_partition(G)

comm_0 = []
comm_1 = []
comm_2 = []
comm_3 = []
comm_4 = []

colores = ["blue", "green", "orange", "red", "purple"]

color_map = []

for node in G:
    for i in range(5):
        if partition[str(node)] == i:
            color_map.append(colores[i])
            
for p in partition:
    comm = partition[str(p)]
    
    if comm == 0:
        comm_0.append(p)
    if comm == 1:
        comm_1.append(p)
    if comm == 2:
        comm_2.append(p)
    if comm == 3:
        comm_3.append(p)
    if comm == 4:
        comm_4.append(p)

    #print(p, comm)

nx.draw(G,node_color = color_map,with_labels = True)
plt.suptitle("Louvain", fontsize = 18)
#plt.savefig("./delfines_louvain.png")
#plt.show()
