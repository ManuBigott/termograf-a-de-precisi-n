import os
from Funcion1 import Datos1
arch = open("dec.csv","a")
for name in os.listdir():
    if ".bmp" in name:
     a,b,c,d,e = Datos1(name)
     arch.write("{},{},{},{},{},{}\n".format(name,round(a,2),round(b,2),round(c,2),round(d,2),round(e,2)))
    else:
        pass
arch.close()