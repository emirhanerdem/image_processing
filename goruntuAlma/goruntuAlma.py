import cv2
import numpy as np

kamera=cv2.VideoCapture(0) # 0 yazarsak kendi bilgisayarımın kamerası, 1 dersek usbden bağlı olan kamera, 2 dersek videodan görüntü alır
while True:
    ret,goruntu=kamera.read()
    cv2.imshow("Kamera",goruntu)
    if cv2.waitKey(1)  &0xFF == ord ("q"):
        break



cv2.waitKey(0)
cv2.destroyAllWindows()