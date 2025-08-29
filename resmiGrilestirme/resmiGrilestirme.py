import cv2
import numpy as np

resim=cv2.imread("scofield.jpg") ## parametre olarak 0 girseydikte grileşirdi hiç uğraşmazdık alttaki gibi
griResim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
yukseklik1,genislik1,kanalSayisi1=resim.shape
yukseklik2,genislik2=griResim.shape

print("Orijinal",yukseklik1,genislik1,kanalSayisi1)
print("Grileşmiş",yukseklik2,genislik2)



cv2.imshow("Grilesmis Micheal",griResim)

cv2.waitKey(0)
cv2.destroyAllWindows()