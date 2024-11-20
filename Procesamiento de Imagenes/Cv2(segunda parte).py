import cv2  
import random

img = cv2.imread('logo.png', -1)
alto, ancho, canales = img.shape      # con el .shape devuelve una tupla con los valores mostrados
print(alto, ancho, canales)     

tag = img[100:200, 100:200]           # Cortamos teniendo en cuenta las dimensiones obtenidas
cv2.imshow('Image', tag)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

img[150:250,200:300] = tag            # Pegamos teniendo en cuenta que las partes a remplazar tienen que ser del mismo tamaño, tanto en fila como en columna.

cv2.imshow('Image', img)  
cv2.waitKey(0)  
cv2.destroyAllWindows() 