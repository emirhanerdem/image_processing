import cv2
import numpy as np

# resim= cv2.imread("images.png",0) #0 koyduğumuzda siyah beyaz oluyor
resim= cv2.imread("images.png")
cv2.imshow("Logomuz",resim)

cv2.imwrite("yeniresim.png",resim)

print(resim[20,80])
print("Resmin Boyutu: "+str(resim.size))
print("Resmin Veri Tipi: "+str(resim.dtype))
print("Resmin Özellikleri: "+str(resim.shape))

cv2.waitKey(0)
cv2.destroyAllWindows() 