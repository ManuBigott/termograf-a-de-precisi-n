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
img = cv2.imread('imagen1.jpg', -1)  
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

mask = cv2.inRange(hsv, RojoL, RojoH)  
mask1 = cv2.inRange(hsv, AmarilloL, AmarilloH)  
mask2 = cv2.inRange(hsv, CianL, CianH)  
T = mask.shape
lista = []
lista1 =[]
lista2 =[]

for i in mask:  
    lista+=list(i)
for i in mask1:  
    lista1+=list(i)
for i in mask2:  
    lista2+=list(i) 

a1=0
b1=0
c1=0
for i in lista:  
    if int(i)==0:  
        a1+=1

for i in lista1:  
    if int(i)==0:  
        b1+=1

for i in lista2:  
    if int(i)==0:  
        c1+=1
a = T[0]*T[1]-a1
b = T[0]*T[1]-b1
c = T[0]*T[1]-c1
print("40 - 50: ",(a/(a+b+c))*100,)
print("20 - 30: ",(b/(a+b+c))*100)
print("0 - 10: ",(c/(a+b+c))*100)
print("Se analizo un ",((a+b+c)/(T[0]*T[1]))*100," % de toda la imagen.")