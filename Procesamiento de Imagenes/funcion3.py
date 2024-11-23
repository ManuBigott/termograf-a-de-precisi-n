import cv2, numpy as np

def promedio(ruta):
    imagen = cv2.imread(ruta, -1)

    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


    #bajo = np.array([0, 30, 30])
    #alto = np.array([60, 255, 255])

    #mascara = cv2.inRange(hsv, bajo, alto)

    temperatura_minima = 20
    temperatura_max = 100

    brillo = hsv[ :, :, 2]

    temperatura = temperatura_minima + (temperatura_max - temperatura_minima) * (brillo/255)

    print(np.mean(temperatura))

    cv2.imshow("imagen", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

promedio("Procesamiento de imagenes/Prueba/301.bmp")