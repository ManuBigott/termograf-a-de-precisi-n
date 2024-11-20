import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         #Utilizamos imagen tipo hsv(por convenencia).
    lower_blue = np.array([90, 50, 50])                  #Indicamos el rango de colores que queremos captar(maximo-bajo).
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)      #La mascara lo que hace es captar los colores que indicamos dentro del rango(bajo-maximo), los que esten dentro del rango los deja como un 1 y los que no como 0.

    result = cv2.bitwise_and(frame, frame, mask=mask)    #Trabajamos encima de la imagen y solo dejamos los pixeles que indique la mascara que hay que dejar.

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()