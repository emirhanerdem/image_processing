import cv2
import numpy as np

resim=cv2.imread("scofield.jpg")
ikiKatBuyuk=cv2.pyrUp(resim)
ikiKatKucuk=cv2.pyrDown(resim)

cv2.imshow("goruntu",resim)
cv2.imshow("iki kat buyuk boyutlu goruntu",ikiKatBuyuk)
cv2.imshow("iki kat kucuk boyutlu goruntu",ikiKatKucuk)

print(resim.shape)
print(ikiKatBuyuk.shape)
print(ikiKatKucuk.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()
