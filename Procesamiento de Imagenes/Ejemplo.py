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
cap = cv2.VideoCapture('Termografia.mp4')      

while True:                        
    ret, frame = cap.read()       
    if ret == True:
     width = int(cap.get(3))          
     height = int(cap.get(4))           
     image = np.zeros(frame.shape, np.uint8)    
     smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
     hsv = cv2.cvtColor(smaller_frame, cv2.COLOR_BGR2HSV)     

     mask = cv2.inRange(hsv, RojoL, RojoH)               
     mask1 = cv2.inRange(hsv,AmarilloL,AmarilloH)
     mask2 = cv2.inRange(hsv,CianL,CianH)
     result = cv2.bitwise_and(smaller_frame, smaller_frame, mask=mask)       
     result1 = cv2.bitwise_and(smaller_frame, smaller_frame, mask=mask1)
     result2 = cv2.bitwise_and(smaller_frame, smaller_frame, mask=mask2)
     image[:height//2, :width//2] = smaller_frame        
     image[height//2:, :width//2] = result      
     image[:height//2, width//2:] = result1
     image[height//2:, width//2:] = result2
     image1 = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
     cv2.imshow('frame', image1)     
     if cv2.waitKey(30) == ord('q'):  
        break
    else: break
cap.release()    
cv2.destroyAllWindows()