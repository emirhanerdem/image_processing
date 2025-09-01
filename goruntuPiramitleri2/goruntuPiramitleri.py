import cv2
import numpy as np

resim=np.zeros((600,600,3),dtype="uint8")
print(resim)
resim[0,0]=255 #(0,0) pikseli 255 yani beyaz renkte yaptim

cv2.imshow("olusturulan resim",resim)


cv2.waitKey(0)
cv2.destroyAllWindows