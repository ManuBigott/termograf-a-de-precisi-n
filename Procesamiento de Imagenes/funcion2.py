import cv2, numpy as np, os
def recortar(nombre):
    imagen = cv2.imread(nombre, -1) 

    #imagen = cv2.resize(imagen, (0,0), fx = 0.5, fy= 0.5) redimensiono la imagen

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

    contornos, jerarquia= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    area_min = 5000 

    lista_imagenes = [] 

    ruta = nombre.split(".")[0]
    carpeta_recortes = os.path.join(ruta, "Recortes")
    os.makedirs(carpeta_recortes, exist_ok=True)

    i = 0
    
    for contorno in contornos: 

        #cv2.drawContours(imagen, contorno, -1, (0,255,0), 4) 

        area = cv2.contourArea(contorno) 

        #perimetro = cv2.arcLength(contorno, True) 
        

        if area >= area_min:     
            #print(f"Área: {area}, Perímetro: {perimetro:.2f}")
            i += 1

            x,y,ancho,altura = cv2.boundingRect(contorno) 
            #print(x,y,ancho,altura)
            
            copia = imagen.copy()
            recorte = copia[y:y+altura, x:x+ancho]
            lista_imagenes.append(copia[y:y+altura, x:x+ancho]) 
            archivo = os.path.join(carpeta_recortes, f"recorte {i}.jpg")
            cv2.imwrite(archivo, recorte)
 
    for i, imagenes in enumerate(lista_imagenes):
        
        cv2.imshow(f"imagen {i+1} recortada", imagenes)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
print(recortar("Procesamiento de Imagenes/Prueba/291.jpg"))