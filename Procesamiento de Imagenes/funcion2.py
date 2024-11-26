import cv2, numpy as np, os
def recortar(ruta):
    imagen = cv2.imread(ruta, -1) 

    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) 

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

    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    area_min = 5000 

    lista_imagenes = [] 

    for contorno in contornos: 

        area = cv2.contourArea(contorno) 

        if area >= area_min:     
            

            x,y,ancho,altura = cv2.boundingRect(contorno) 
            
            copia = imagen.copy()
            recorte = copia[y:y+altura, x:x+ancho]
            lista_imagenes.append(recorte) 
            
 
    for i, imagenes in enumerate(lista_imagenes):
        imagenes = cv2.resize(imagenes, (0,0), fx=1.5, fy=1.5)
        cv2.imwrite(f'Recortes/{ruta}.bmp',imagenes)
        #cv2.imshow(f"{ruta}:{i+1}", imagenes)
        #cv2.waitKey(0)  #Decimos cuanto tiempo va a durar la imagen, si colocamos 0 sera por un tiempo indefinido.
        #cv2.destroyAllWindows()
    
