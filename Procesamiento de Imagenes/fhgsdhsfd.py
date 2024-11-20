import numpy as np
import cv2
Azul_oscuroL,Azul_oscuroH = np.array([120,50,50],np.uint8) , np.array([130,255,255],np.uint8)
AzulL,AzulH = np.array([180,50,50],np.uint8),np.array([190,255,255],np.uint8)
CianL,CianH = np.array([75,50,50],np.uint8),np.array([85,255,255],np.uint8)
VerdeL,VerdeH = np.array([60,50,50],np.uint8),np.array([70,255,255],np.uint8)
AmarilloL,AmarilloH = np.array([30,50,50],np.uint8),np.array([40,255,255],np.uint8)
NaranjaL,NaranjaH = np.array([15,50,50],np.uint8),np.array([25,255,255],np.uint8)
RojoL,RojoH = np.array([0,50,50],np.uint8),np.array([10,255,255],np.uint8)
Rojo_intensoL,Rojo_intensoH = np.array([120,50,50],np.uint8),np.array([130,255,255],np.uint8)
"""
RANGOS DE TEMPERATURA EN FUNCION DEL COLOR (HSV)
-20 - -10 Azul oscuro
-10 - 0 Azul
0 - 10  Cian
10 - 20 Verde
20 - 30 Amarillo
30 - 40 Naranja
40 - 50 Rojo
50 - 60 Rojo intenso
"""





frame = cv2.imread("imagen.jpg",-1)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         #Utilizamos imagen tipo hsv(por conveniencia).
lower_blue = np.array([90, 50, 50])                  #Indicamos el rango de colores que queremos captar(maximo-bajo).
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, RojoL, RojoH)                #La mascara lo que hace es captar los colores que indicamos dentro del rango(bajo-maximo), los que esten dentro del rango los deja como un 1 y los que no como 0.
mask1 = cv2.inRange(hsv,AmarilloL,AmarilloH)
result = cv2.bitwise_and(frame, frame, mask=mask)        #Trabajamos encima de la imagen y solo dejamos los pixeles que indique la mascara que hay que dejar.
result1 = cv2.bitwise_and(frame, frame, mask=mask1)


cv2.imshow('40 - 50', result)
cv2.imshow('20 - 30', result1)
cv2.waitKey(0)
cv2.destroyAllWindows()