import cv2
import numpy as np

image=cv2.imread("logo.jpeg")
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(erosion,kernel,iterations=1)
#önce erosion(aşındırma) yapılır sonra delation yapılır ki görsel gürültüden kurtulsun

gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)


cv2.imshow("orijinal",image)
cv2.imshow("morfolojik işlem sonrasi",dilation)
cv2.imshow("gradyan",gradyan)

cv2.waitKey(0)
cv2.destroyAllWindows()