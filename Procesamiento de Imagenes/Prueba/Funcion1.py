import numpy as np
import cv2
def Datos1(name):
 Azul_oscuroL,Azul_oscuroH = np.array([120,50,50],np.uint8) , np.array([130,255,255],np.uint8)
 AzulL,AzulH = np.array([180,50,50],np.uint8),np.array([190,255,255],np.uint8)
 CianL,CianH = np.array([75,50,50],np.uint8),np.array([85,255,255],np.uint8)
 VerdeL,VerdeH = np.array([60,50,50],np.uint8),np.array([70,255,255],np.uint8)
 AmarilloL,AmarilloH = np.array([30,50,50],np.uint8),np.array([40,255,255],np.uint8)
 NaranjaL,NaranjaH = np.array([15,50,50],np.uint8),np.array([25,255,255],np.uint8)
 RojoL,RojoH = np.array([0,50,50],np.uint8),np.array([10,255,255],np.uint8)
 Rojo_intensoL,Rojo_intensoH = np.array([120,50,50],np.uint8),np.array([130,255,255],np.uint8)
 img = cv2.imread(name, -1)  
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

 mask = cv2.inRange(hsv, RojoL, RojoH)  
 mask1 = cv2.inRange(hsv, AmarilloL, AmarilloH)  
 mask2 = cv2.inRange(hsv, CianL, CianH)
 mask3 = cv2.inRange(hsv, NaranjaL, NaranjaH)
 cv2.imwrite("nuevologo.png",mask)
 T = mask.shape
 lista = []
 lista1 =[]
 lista2 =[]
 lista3 =[]

 for i in mask:  
    lista+=list(i)
 for i in mask1:  
    lista1+=list(i)
 for i in mask2:  
    lista2+=list(i)
 for i in mask3:  
    lista3+=list(i)

 a1=0
 b1=0
 c1=0
 d1=0
 for i in lista:  
    if int(i)==0:  
        a1+=1

 for i in lista1:  
    if int(i)==0:  
        b1+=1

 for i in lista2:  
    if int(i)==0:  
        c1+=1
 for i in lista3:  
    if int(i)==0:  
        d1+=1
 a = T[0]*T[1]-a1
 b = T[0]*T[1]-b1
 c = T[0]*T[1]-c1
 d = T[0]*T[1]-d1
 if a+b+d+c != 0:
  return (a/(a+b+c+d))*100,(d/(a+b+c+d))*100,(b/(a+b+c+d))*100,(c/(a+b+c+d))*100,((a+b+c+d)/(T[0]*T[1]))*100
 else:
     return 0,0,0,0,0
# return 40 - 50,30 - 40,20 - 30,0 - 10, Porcentaje del analisis
