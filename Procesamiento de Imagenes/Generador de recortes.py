import os
from funcion2 import recortar
for name in os.listdir():
    if ".bmp" in name:
     recortar(name)
    else:
        pass