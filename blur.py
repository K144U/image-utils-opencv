import os 
import cv2

img = cv2.imread("bala.png")

img_blur = cv2.blur(img, (10,10))


cv2.imshow('img', img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
