import cv2 
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")
#3 kenar çizdim ve üçgen oluşturdum
cv2.line(resim,(0,0),(100,100),(0,0,225),thickness=3)
cv2.line(resim,(100,0),(100,100),(0,0,225),thickness=3)
cv2.line(resim,(0,0),(100,0),(0,0,225),thickness=3)
#--
#üçgen çizme
cv2.circle(resim,(100,100),25,(0,255,0),thickness=3)
#metin kutusu çizme
cv2.putText(resim,"Emirhan Erdem",(20,150),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),thickness=1)


cv2.imshow("deneme",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()