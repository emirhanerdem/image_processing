import cv2

resim1=cv2.imread("a.jpg")
resim2=cv2.imread("b.jpg")

print(resim1[120,100])
print(resim2[50,50])

cv2.imshow("a resmi",resim1)
cv2.imshow("b resmi",resim2)

print(resim1[120,100]+resim2[50,50])

cv2.waitKey(0)
cv2.destroyAllWindows()