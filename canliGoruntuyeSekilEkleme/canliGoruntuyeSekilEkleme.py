import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.rectangle(goruntu,(200,200),(400,400),(0,0,225),thickness=3)
    cv2.line(goruntu,(0,0),(500,0),(0,0,255),thickness=5)
    cv2.line(goruntu,(0,0),(0,500),(0,0,255),thickness=5)
    cv2.line(goruntu,(500,0),(500,500),(0,0,255),thickness=5)
    cv2.line(goruntu,(0,500),(500,500),(0,0,255),thickness=5)
    cv2.circle(goruntu,(150,150),20,(255,0,0),thickness=5)
    cv2.putText(goruntu,"Emirhan Erdem",(0,20),cv2.FONT_HERSHEY_COMPLEX,1,(200,0,0),thickness=2)


    cv2.imshow("Kamera",goruntu)
    if cv2.waitKey(25) & 0xFF== ord('q'):
        break


kamera.release
cv2.destroyAllWindows()