import cv2
import numpy as np

resim1=cv2.imread("resim1.jpg")
resim2=cv2.imread("resim2.jpg")

#cv2.imshow("RESİM1",resim1)
#cv2.imshow("RESİM2",resim2)

toplam=cv2.add(resim1,resim2)
agirlikliToplama=cv2.addWeighted(resim1,0.8,resim2,0.2,0)


cv2.imshow("Birleştirilen Resim",toplam)
cv2.imshow("Agirlikli Resim",agirlikliToplama) #0.8 oranında resim 1 ağırlıklı birleştirildi
cv2.waitKey(0)
cv2.destroyAllWindows()