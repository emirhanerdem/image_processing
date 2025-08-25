import cv2
import numpy as np

resim = cv2.imread("micheal.jpg")
#cv2.imshow("Prison Break",resim)

aynalananResim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarResim=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT ,value=(0,0,225))
#cv2.imshow("Aynalanan Resim",aynalananResim)
#cv2.imshow("Uzatilan Resim",uzatilanResim)
#cv2.imshow("Tekrarlanan Resim",tekrarResim)
cv2.imshow("SarilanResim",sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()