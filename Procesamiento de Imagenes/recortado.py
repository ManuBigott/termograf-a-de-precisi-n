import numpy as np, cv2

imagen = cv2.imread("bibliotecas/opencv_tutorial/imagenes/291.jpg", -1) #cambia la direccion a donde tengas la imagen

#imagen = cv2.resize(imagen, (0,0), fx = 0.5, fy= 0.5) redimensiono la imagen

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #convierto a hsv

#azules
Azul_oscuroL,Azul_oscuroH = np.array([120,50,50],np.uint8) , np.array([130,255,255],np.uint8)
AzulL,AzulH = np.array([180,50,50],np.uint8),np.array([190,255,255],np.uint8)

#cian
CianL,CianH = np.array([75,50,50],np.uint8),np.array([85,255,255],np.uint8)

#verde
VerdeL,VerdeH = np.array([60,50,50],np.uint8),np.array([70,255,255],np.uint8)

#amarillo
AmarilloL,AmarilloH = np.array([30,50,50],np.uint8),np.array([40,255,255],np.uint8)

#naranja
NaranjaL,NaranjaH = np.array([15,50,50],np.uint8),np.array([25,255,255],np.uint8)

#rojos
RojoL,RojoH = np.array([0,50,50],np.uint8),np.array([10,255,255],np.uint8)
Rojo_intensoL,Rojo_intensoH = np.array([120,50,50],np.uint8),np.array([130,255,255],np.uint8)

mask = cv2.inRange(imagen_hsv, NaranjaL, NaranjaH) #aplico la mascara

contornos, jerarquia= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#esta pinga me devuelve dos cosas, los contornos y la jerarquia de contornos (todavia no se como se usa)

area_min = 5000 #esto hay que investigarlo bien, le puse 4000 despues de hacer varias pruebas pero hay que encontrar la forma de generalizar
#porque si no crea muchos rectangulos que no son de nuestro interes (como en la imagen que pase ayer)

lista_imagenes = [] #lista para contener las imagenes recortadas

for contorno in contornos: #esta pinga recorre la lista de contornos

    #cv2.drawContours(imagen, contorno, -1, (0,255,0), 4) 

    area = cv2.contourArea(contorno) #calcula el area de cada contorno
    perimetro = cv2.arcLength(contorno, True) #calcula el perimetro de cada contorno
    

    if area >= area_min:    #filtro los contornos por su area 
        print(f"Área: {area}, Perímetro: {perimetro:.2f}")

        x,y,ancho,altura = cv2.boundingRect(contorno) #obtengo el inicio y final del contorno
        print(x,y,ancho,altura)
        
        copia = imagen.copy() #copio la imagen original
        lista_imagenes.append(copia[y:y+altura, x:x+ancho]) #agrego la imagen recortada a una lista
        #fijate que en el ancho ademas sume 75, porque si no no toma toda el area y esop es un problema
        #que todavia no se solucionar

        cv2.rectangle(imagen, (x,y), (x+ancho,y+altura), (255,0,0), 5)#destaco las areas con un fokin rectangulo

#esto es trivial
fondo = np.zeros(imagen.shape, np.uint8)

altura = int(imagen.shape[0])
ancho = int(imagen.shape[1])

imagen_pequeña = cv2.resize(imagen, (ancho//2, altura))
mask_pequeña = cv2.resize(mask, (ancho//2, altura))

mask_pequeña_color = cv2.cvtColor(mask_pequeña, cv2.COLOR_GRAY2BGR)


fondo[: , :ancho//2] = imagen_pequeña
fondo[: , ancho//2:] = mask_pequeña_color


cv2.imshow("hsv", fondo)
for i, imagenes in enumerate(lista_imagenes):
    imagenes = cv2.resize(imagenes, (0,0), fx=1.5, fy=1.5)
    cv2.imshow(f"imagen {i+1}", imagenes)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

