import glob
from enriquecimiento_0 import etapa_0
from enriquecimiento_1 import etapa_1
from enriquecimiento_2 import etapa_2
from enriquecimiento_3 import etapa_3
from enriquecimiento_4 import etapa_4

input_files = glob.glob("./comunidades/*.txt")

# itero sobre las comunidades
for f in input_files[:4]:
    #print(f)
    
    # quiero extraer el numero de comunidad
    # me quedo con lo que antecede a .txt:
    s = f.split('.')[-2]
    
    # me quedo solo con el numero
    numero_de_comunidad = s.split('_')[1]
    
    ########################################
    
    print("COMUNIDAD %s" % (numero_de_comunidad))
    print("=============")
    
    print("Etapa 0")
    etapa_0(f, numero_de_comunidad)
    
    print("Etapa 1")
    etapa_1(numero_de_comunidad)
    
    print("Etapa 2")
    etapa_2(numero_de_comunidad)
    
    print("Etapa 3")
    etapa_3(numero_de_comunidad)
    
    print("Etapa 4")
    etapa_4(numero_de_comunidad)
    
    print()