import cv2
import numpy as np

resim = cv2.imread("ben.jpg")


resim[100:600,80:1000,1]=80
resim[100:600,80:1000,2]=20 


cv2.imshow("Benim Resmim",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()