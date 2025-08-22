import cv2
import numpy as np

resim=cv2.imread("renkli.jpg")
kesit=resim[50:150,300:400]
resim[0:100,0:100]=kesit
resim[:,:,2]=255
resim[400:450,300:350]=(0,150,255)
cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows(0)