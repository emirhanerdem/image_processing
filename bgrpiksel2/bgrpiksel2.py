import cv2
import numpy as np

joker=cv2.imread("jokergorsel.jpg")
#joker[50,30]=[255,255,255]

for i in range(100,300):
    joker[70,i]=[255,255,255]


cv2.imshow("denemejoker",joker)

cv2.waitKey(0)
cv2.destroyAllWindows()