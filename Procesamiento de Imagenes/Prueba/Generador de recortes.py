import os
from Recortado1 import recortador
for name in os.listdir():
    if ".bmp" in name:
     recortador(name)
    else:
        pass