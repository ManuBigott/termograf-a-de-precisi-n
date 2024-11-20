import numpy as np
import cv2

cap = cv2.VideoCapture(0)       #Inicializamos en cap la webcam (el parametro dentro del parentesis del metodo .VideoCapture solo es para indicar cuantas camaras son).

while True:                        #Bucle salvaje, nos va a servir para repetir varias veces el metodo .imshow
    ret, frame = cap.read()        # Las capturas vienen acompañada de una tupla, la posicion 0 es un valor de referencia(no se necesita), la posicion 1 (frame) es la imagen en ese preciso instante de tiempo.
    width = int(cap.get(3))            # el metodo .get(n) es un flotante, si n es 3 indica las columnas,si n es 4 indica las filas.
    height = int(cap.get(4))           
    image = np.zeros(frame.shape, np.uint8)    # Vamos a crear un arreglo del mismo tamaño que nuestra imagen original(el metodo zero cambia todas las componentes del arreglo por 0)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # Vamos a reducir el frame a un cuarto de su tamaño, lo guardamos en smaller_frame
    image[:height//2, :width//2] = smaller_frame        
    image[height//2:, :width//2] = smaller_frame       #Ahora vamos a pegar nuestro frame en los cuadranetes correspondientes, tenemos las dimensiones originales de nuestra imagen(la division entera es por el metodo .get envia es un flotante)
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)     # Mostramos nuestra creacion.

    if cv2.waitKey(1) == ord('q'):  # el metodo .waitKey(n) es una ventana donde n dice cuanto va a durar (en milisegundos), dependiendo de la tecla que toques la instancia .waitKey(n) va a guardar en ella el unicode de esa letra, por eso se cierra en "q".
        break

cap.release()    # Cerramos la captura(El mismo procedimiento que le haciamos a los archivos, cerrar a lo ultimo)
cv2.destroyAllWindows()