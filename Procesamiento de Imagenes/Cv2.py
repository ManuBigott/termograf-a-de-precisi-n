import cv2
import pandas as pd
import numpy as np
"""
-1, cv2.IMREAD_COLOR : Elimina la Transparencia.  
 0, cv2.IMREAD_GRAYSCALE : Deja todo en gris.  
 1, cv2.IMREAD_UNCHANGED : No hace nada.
 ROTATE_180: Rotar 180 grados.
 ROTATE_90_CLOCKWISE: Rotar 90 grados en sentidos de las agujas . 
 ROTATE_90_COUNTERCLOCKWISE: Rotar 90 grados en sentidos contrario de las agujas.
 """
img = cv2.imread('logo.png', 1)                           #Abrimos y guardamos en una variable la imagen 
img = cv2.resize(img, (0, 0),fx=1,fy=1)                   #Sirve para reducir el tamaño
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)     #Rotar la imagen
cv2.imwrite("nuevologo.png",img)                          #Guardamos una nueva imagen cambiando el nombre
lista = []
for i in img:
    lista+=list(i)
print(len(lista))
print(img[0][0])
print(list(img[0]))
img2 = pd.Series(list(img[0]))

cv2.imshow('Image', img)                 #Mostramos imagen.
cv2.waitKey(0)                           #Decimos cuanto tiempo va a durar la imagen, si colocamos 0 sera por un tiempo indefinido.
cv2.destroyAllWindows()                  #Cerrar la ventana