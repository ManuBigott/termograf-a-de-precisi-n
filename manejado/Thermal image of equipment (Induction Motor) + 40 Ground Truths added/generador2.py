import os
from Funcion1 import Datos1
arch = open("dec1.csv","a")
arch.write("archivo,40 - 50,30 - 40,20 - 30,0 - 10,%\n")
for i in os.listdir():
    if not("." in i):
        for j in os.listdir(i):
            a,b,c,d,e = Datos1(i+"/"+j)
            arch.write("{},{},{},{},{},{}\n".format(j,round(a,2),round(b,2),round(c,2),round(d,2),round(e,2)))
arch.close()            
        
