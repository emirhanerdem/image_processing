import cv2
import numpy as np

image = cv2.imread("a.png")
meanFilter=cv2.blur(image,(3,3))
meanFilter2=cv2.blur(image,(9,3))
cv2.imshow("orjinal resim",image)
cv2.imshow("3x3 mean filter",meanFilter)
cv2.imshow("9x3 mean filter",meanFilter2)

medianFilter=cv2.medianBlur(image,3)
medianFilter2=cv2.medianBlur(image,5)
medianFilter3=cv2.medianBlur(image,15)


cv2.imshow("medyan filter 3x3",medianFilter)
cv2.imshow("medyan filter 5x5",medianFilter2)
cv2.imshow("medyan filter 15x15",medianFilter3)

gauss=cv2.GaussianBlur(image,(3,3),0)
gauss2=cv2.GaussianBlur(image,(5,5),0)
gauss3=cv2.GaussianBlur(image,(9,9),0)
cv2.imshow("gauss filter 3x3",gauss)
cv2.imshow("gauss filter 5x5",gauss2)
cv2.imshow("gauss filter 5x5",gauss3)




cv2.waitKey(0)
cv2.destroyAllWindows()