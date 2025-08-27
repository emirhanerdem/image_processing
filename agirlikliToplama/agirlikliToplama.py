import cv2
import numpy as np

resim1=cv2.imread("emelSayin.jpg")
resim2=cv2.imread("turkanSoray.jpg")

print(resim1[50,100])
print(resim2[100,160])
cv2.imshow("Emel Sayin",resim1)
cv2.imshow("Turkan Soray",resim2)

print(resim1[50,100]+resim2[100,160])
#255'i geçince devir atiyor bastan basliyor 240+50=34

cv2.waitKey(0)
cv2.destroyAllWindows()